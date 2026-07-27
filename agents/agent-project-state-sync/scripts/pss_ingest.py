#!/usr/bin/env python3
"""
pss_ingest.py - Project State-Sync deterministic INGEST + RETAIN helper.

Part of the Project State-Sync method (PSS):
  /Users/grig/.agents/docs/methodologies/project-state-sync-method.md
Runbook:
  /Users/grig/.agents/prompts/agents/agent-project-state-sync/SKILL.md

This script owns the DETERMINISTIC half of the cycle: it enumerates every new
source item across the configured connectors since the last run (watermarks),
computes content hashes, dedupes against the shared dedupe index, records
immutable retain references, and emits a per-run INGEST MANIFEST. It performs no
LLM work and mutates no project truth. TRANSLATE / RECONCILE / REPORT are the
agent's job (see SKILL.md), driven off the manifest this script produces.

Design guarantees:
  - Originals are never modified. Retain is by immutable reference + hash
    (large files are pointed at, not copied) unless a connector opts into copy.
  - `plan` is read-only: it writes only the run manifest, never watermarks or
    the dedupe index.
  - `advance` is the only mutating command: it appends dedupe entries and moves
    watermarks forward, and is meant to run ONLY after the full cycle succeeds,
    so a failed run never loses signal (the window re-opens next run).
  - Fail-open per connector: a broken connector is recorded as an error item in
    the manifest, and the run continues. Errors are state, not silent skips.

Run it with the GAS venv interpreter (PyYAML lives there):
  /Users/grig/.agents/.venv/bin/python3 \
    /Users/grig/.agents/prompts/agents/agent-project-state-sync/scripts/pss_ingest.py \
    plan --config <ABS_PATH_TO_config.yaml>

Commands:
  plan     Enumerate new items since watermarks -> write run manifest. No mutation.
  advance  Given a run manifest, append dedupe entries + advance watermarks.
  show     Print the current watermarks + dedupe/promotion ledger sizes.
  self-test  Synthetic smoke test on a temp project. No external state touched.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import glob
import hashlib
import json
import os
import sys
import tempfile
from pathlib import Path

try:
    import yaml  # PyYAML, present in /Users/grig/.agents/.venv
except Exception:  # pragma: no cover - explicit guidance beats a raw traceback
    sys.stderr.write(
        "ERROR: PyYAML not importable. Run this script with the GAS venv:\n"
        "  /Users/grig/.agents/.venv/bin/python3 <this-script> ...\n"
    )
    raise

SCHEMA_VERSION = "pss-ingest/1"
PARSER_VERSION = "1.0.0"  # bump when enumeration/hashing semantics change


# --------------------------------------------------------------------------
# small utilities
# --------------------------------------------------------------------------

def utcnow() -> str:
    return _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def run_id() -> str:
    return _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%d-%H-%M-%SZ")


def expand(path: str, project_root: str, home: str) -> str:
    """Resolve placeholders + user/home. Never leaves a literal ~ in a path."""
    if path is None:
        return path
    out = (
        path.replace("{PROJECT_ROOT}", project_root)
        .replace("{HOME}", home)
        .replace("$HOME", home)
    )
    out = os.path.expanduser(out)
    return out


def sha256_file(p: Path, cap_bytes: int = 0) -> str:
    h = hashlib.sha256()
    with p.open("rb") as fh:
        if cap_bytes and cap_bytes > 0:
            h.update(fh.read(cap_bytes))
        else:
            for chunk in iter(lambda: fh.read(1024 * 1024), b""):
                h.update(chunk)
    return h.hexdigest()


def mtime_iso(p: Path) -> str:
    return (
        _dt.datetime.fromtimestamp(p.stat().st_mtime, _dt.timezone.utc)
        .strftime("%Y-%m-%dT%H:%M:%SZ")
    )


def atomic_write(target: Path, data: str) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(target.parent), suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(data)
        os.replace(tmp, target)
    finally:
        if os.path.exists(tmp):
            os.remove(tmp)


def append_jsonl(target: Path, rows: list[dict]) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("a", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")


def load_json(p: Path, default):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return default


def load_dedupe_keys(p: Path) -> set[str]:
    keys: set[str] = set()
    if not p.exists():
        return keys
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            keys.add(json.loads(line).get("dedupe_key", ""))
        except Exception:
            continue
    return keys


# --------------------------------------------------------------------------
# connectors: each returns a list of raw item dicts (no truth decisions)
# --------------------------------------------------------------------------

def _cursor_mtime(watermarks: dict, cid: str) -> float:
    return float(watermarks.get(cid, {}).get("cursor_mtime", 0.0) or 0.0)


def connector_claude_conversations(conn, ctx) -> list[dict]:
    """
    Reads Claude session transcript JSONL directly from the project's
    ~/.claude/projects/<dir>/ store. The `css` helper named in CLAUDE.md does
    NOT exist on disk, so this connector never shells out to it; it reads the
    JSONL files by mtime. New/updated session files since the cursor are items.
    Retain = immutable reference (the JSONL is already the durable store).
    """
    src = Path(expand(conn["source_path"], ctx["project_root"], ctx["home"]))
    items: list[dict] = []
    if not src.exists():
        return [_error_item(conn, f"source_path not found: {src}")]
    cutoff = _cursor_mtime(ctx["watermarks"], conn["id"])
    for jf in sorted(src.glob("*.jsonl")):
        st = jf.stat()
        if st.st_mtime <= cutoff:
            continue
        sha = sha256_file(jf)
        items.append(_item(
            conn, source_item_id=jf.stem, content_sha256=sha,
            source_path=str(jf), item_mtime=st.st_mtime,
            retain_strategy="immutable-reference", retain_ref=str(jf),
            hint="claude-session-transcript",
        ))
    return items


def _transcript_globs(conn, ctx) -> list[str]:
    globs = conn.get("source_globs") or ([conn["source_path"]] if conn.get("source_path") else [])
    return [expand(g, ctx["project_root"], ctx["home"]) for g in globs]


def connector_meeting_transcripts(conn, ctx) -> list[dict]:
    """
    Scans configured transcript globs (VTT/TXT/MD) for meeting recordings newer
    than the cursor. It does NOT invent a transcript when one is missing: the
    ASK-THE-OWNER fallback for a referenced-but-absent meeting is the agent's
    job in the runbook (it cross-references WOs / calendar / owner mentions).
    Retain = immutable reference to the raw file in place.
    """
    items: list[dict] = []
    cutoff = _cursor_mtime(ctx["watermarks"], conn["id"])
    exts = tuple(conn.get("extensions", [".vtt", ".txt", ".md", ".json"]))
    seen: set[str] = set()
    for gpat in _transcript_globs(conn, ctx):
        for match in glob.glob(gpat, recursive=True):
            p = Path(match)
            if not p.is_file() or p.suffix.lower() not in exts:
                continue
            rp = str(p.resolve())
            if rp in seen:
                continue
            seen.add(rp)
            st = p.stat()
            if st.st_mtime <= cutoff:
                continue
            items.append(_item(
                conn, source_item_id=p.name, content_sha256=sha256_file(p),
                source_path=rp, item_mtime=st.st_mtime,
                retain_strategy=conn.get("retain_strategy", "immutable-reference"),
                retain_ref=rp, hint="meeting-transcript",
            ))
    return items


def connector_project_inbox(conn, ctx) -> list[dict]:
    """
    Reads new markdown packets from the project's inbox directories (e.g. the
    liaison inbox, the steward intake drop) since the cursor. Thin by design:
    classification/promotion of each packet is the TRANSLATE/RECONCILE step
    (SITS taxonomy), not this enumerator.
    """
    items: list[dict] = []
    cutoff = _cursor_mtime(ctx["watermarks"], conn["id"])
    dirs = conn.get("source_dirs") or ([conn["source_path"]] if conn.get("source_path") else [])
    for d in dirs:
        base = Path(expand(d, ctx["project_root"], ctx["home"]))
        if not base.exists():
            items.append(_error_item(conn, f"inbox dir not found: {base}"))
            continue
        for p in sorted(base.glob("*.md")):
            if p.name.lower() in ("readme.md", "index.md", "_protocol.md", "_readme.md"):
                continue
            st = p.stat()
            if st.st_mtime <= cutoff:
                continue
            items.append(_item(
                conn, source_item_id=p.name, content_sha256=sha256_file(p),
                source_path=str(p), item_mtime=st.st_mtime,
                retain_strategy="immutable-reference", retain_ref=str(p),
                hint="inbox-packet",
            ))
    return items


def connector_deferred(conn, ctx) -> list[dict]:
    """
    Extension-point connectors (e.g. whatsapp-threads) that have real upstream
    tooling but whose auto-run is intentionally deferred. Emits a single
    informational item so the run report can surface it without running it.
    """
    note = conn.get("deferred_note", "connector deferred; wire per references/connectors.md")
    return [{
        "connector_id": conn["id"], "kind": conn["kind"], "state": "deferred",
        "note": note, "tool": conn.get("tool"), "detected_at": utcnow(),
    }]


CONNECTOR_DISPATCH = {
    "claude-conversations": connector_claude_conversations,
    "meeting-transcripts": connector_meeting_transcripts,
    "project-inbox": connector_project_inbox,
    "whatsapp-threads": connector_deferred,
    "deferred": connector_deferred,
}


def _item(conn, *, source_item_id, content_sha256, source_path, item_mtime,
          retain_strategy, retain_ref, hint) -> dict:
    return {
        "connector_id": conn["id"],
        "kind": conn["kind"],
        "state": "new",
        "source_item_id": source_item_id,
        "content_sha256": content_sha256,
        "dedupe_key": f"{conn['id']}:{source_item_id}:{content_sha256}",
        "source_path": source_path,
        "item_mtime": item_mtime,
        "item_mtime_iso": _dt.datetime.fromtimestamp(
            item_mtime, _dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "retain_strategy": retain_strategy,
        "retain_ref": retain_ref,
        "hint": hint,
        "imported_at": utcnow(),
    }


def _error_item(conn, message) -> dict:
    return {
        "connector_id": conn["id"], "kind": conn.get("kind"), "state": "error",
        "error": message, "detected_at": utcnow(),
    }


# --------------------------------------------------------------------------
# plan / advance
# --------------------------------------------------------------------------

def build_context(cfg: dict, config_path: Path) -> dict:
    home = str(Path.home())
    project_root = expand(cfg.get("project_root", "{PROJECT_ROOT}"), "", home)
    if "{PROJECT_ROOT}" in project_root or not project_root:
        # default to the dir two levels above run-state if not set explicitly
        project_root = str(config_path.resolve().parent)
    rs = cfg.get("run_state", {})
    watermarks_path = Path(expand(
        rs.get("watermarks_path", "{PROJECT_ROOT}/run-state/watermarks.json"),
        project_root, home))
    dedupe_path = Path(expand(
        rs.get("dedupe_index", "{PROJECT_ROOT}/run-state/dedupe-index.jsonl"),
        project_root, home))
    runs_dir = Path(expand(
        rs.get("runs_dir", "{PROJECT_ROOT}/run-state/runs"),
        project_root, home))
    watermarks = load_json(watermarks_path, {}).get("connectors", {}) \
        if watermarks_path.exists() else {}
    return {
        "home": home,
        "project_root": project_root,
        "watermarks_path": watermarks_path,
        "dedupe_path": dedupe_path,
        "runs_dir": runs_dir,
        "watermarks": watermarks,
        "config_path": str(config_path.resolve()),
        "project_slug": cfg.get("project_slug", "unknown"),
    }


def cmd_plan(cfg: dict, ctx: dict) -> dict:
    dedupe_keys = load_dedupe_keys(ctx["dedupe_path"])
    connectors = [c for c in cfg.get("connectors", []) if c.get("enabled", True)]
    per_connector = []
    all_items: list[dict] = []
    for conn in connectors:
        fn = CONNECTOR_DISPATCH.get(conn.get("kind"))
        if fn is None:
            raw = [_error_item(conn, f"unknown connector kind: {conn.get('kind')}")]
        else:
            try:
                raw = fn(conn, ctx)
            except Exception as exc:  # fail-open
                raw = [_error_item(conn, f"connector raised: {exc!r}")]
        new, dup, err, deferred = [], [], [], []
        for it in raw:
            if it.get("state") == "error":
                err.append(it)
            elif it.get("state") == "deferred":
                deferred.append(it)
            elif it.get("dedupe_key") in dedupe_keys:
                it["state"] = "duplicate"
                dup.append(it)
            else:
                new.append(it)
        all_items.extend(new + dup + err + deferred)
        per_connector.append({
            "connector_id": conn["id"], "kind": conn["kind"],
            "new": len(new), "duplicate": len(dup),
            "errors": len(err), "deferred": len(deferred),
        })
    rid = run_id()
    manifest = {
        "schema": SCHEMA_VERSION,
        "parser_version": PARSER_VERSION,
        "run_id": rid,
        "generated_at": utcnow(),
        "project_slug": ctx["project_slug"],
        "project_root": ctx["project_root"],
        "config_path": ctx["config_path"],
        "window": {
            "note": "each connector enumerates items newer than its own cursor",
            "watermarks_at_plan": ctx["watermarks"],
        },
        "summary": per_connector,
        "items": all_items,
    }
    manifest_path = ctx["runs_dir"] / f"{rid}-ingest-manifest.json"
    atomic_write(manifest_path, json.dumps(manifest, indent=2, ensure_ascii=False))
    manifest["_manifest_path"] = str(manifest_path)
    return manifest


def cmd_advance(manifest_path: Path, ctx: dict) -> dict:
    manifest = load_json(manifest_path, None)
    if manifest is None:
        raise SystemExit(f"cannot read manifest: {manifest_path}")
    new_items = [i for i in manifest.get("items", []) if i.get("state") == "new"]
    # 1) append dedupe entries so these items are never re-ingested as new
    rows = []
    for it in new_items:
        rows.append({
            "dedupe_key": it["dedupe_key"],
            "connector_id": it["connector_id"],
            "source_item_id": it["source_item_id"],
            "content_sha256": it["content_sha256"],
            "record_path": it.get("retain_ref"),
            "first_seen_at": it["imported_at"],
            "run_id": manifest["run_id"],
            "state": "ingested",
        })
    if rows:
        append_jsonl(ctx["dedupe_path"], rows)
    # 2) advance each connector cursor to the newest item mtime it produced
    wm_doc = load_json(ctx["watermarks_path"], {}) if ctx["watermarks_path"].exists() else {}
    connectors = wm_doc.get("connectors", {})
    newest: dict[str, float] = {}
    for it in new_items:
        cid = it["connector_id"]
        newest[cid] = max(newest.get(cid, 0.0), float(it.get("item_mtime", 0.0)))
    for cid, mt in newest.items():
        entry = connectors.get(cid, {})
        entry["cursor_mtime"] = max(float(entry.get("cursor_mtime", 0.0) or 0.0), mt)
        entry["last_run_at"] = utcnow()
        entry["last_run_id"] = manifest["run_id"]
        connectors[cid] = entry
    # connectors that produced no new items still get a last_run_at stamp
    for cs in manifest.get("summary", []):
        cid = cs["connector_id"]
        entry = connectors.get(cid, {})
        entry.setdefault("cursor_mtime", 0.0)
        entry["last_run_at"] = utcnow()
        entry["last_run_id"] = manifest["run_id"]
        connectors[cid] = entry
    wm_doc["connectors"] = connectors
    wm_doc["updated_at"] = utcnow()
    wm_doc["schema"] = SCHEMA_VERSION
    atomic_write(ctx["watermarks_path"], json.dumps(wm_doc, indent=2, ensure_ascii=False))
    return {"advanced": list(newest.keys()), "dedupe_appended": len(rows),
            "watermarks_path": str(ctx["watermarks_path"])}


# --------------------------------------------------------------------------
# cli
# --------------------------------------------------------------------------

def _load_cfg(config_path: Path) -> dict:
    if not config_path.exists():
        raise SystemExit(f"config not found: {config_path}")
    return yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}


def _print_plan_summary(manifest: dict) -> None:
    print(f"PSS INGEST PLAN  run_id={manifest['run_id']}  project={manifest['project_slug']}")
    print(f"manifest: {manifest.get('_manifest_path')}")
    for cs in manifest["summary"]:
        print(f"  {cs['connector_id']:<28} kind={cs['kind']:<20} "
              f"new={cs['new']} dup={cs['duplicate']} err={cs['errors']} deferred={cs['deferred']}")
    errs = [i for i in manifest["items"] if i.get("state") == "error"]
    for e in errs:
        print(f"  ERROR [{e.get('connector_id')}]: {e.get('error')}")
    defs = [i for i in manifest["items"] if i.get("state") == "deferred"]
    for d in defs:
        print(f"  DEFERRED [{d.get('connector_id')}]: {d.get('note')}")


def _self_test() -> int:
    import shutil
    tmp = Path(tempfile.mkdtemp(prefix="pss-selftest-"))
    try:
        conv = tmp / "conv"
        conv.mkdir()
        (conv / "sess-a.jsonl").write_text('{"x":1}\n', encoding="utf-8")
        meet = tmp / "meet"
        meet.mkdir()
        (meet / "m1.vtt").write_text("WEBVTT\n", encoding="utf-8")
        cfg = {
            "project_slug": "selftest",
            "project_root": str(tmp),
            "run_state": {
                "watermarks_path": str(tmp / "run-state/watermarks.json"),
                "dedupe_index": str(tmp / "run-state/dedupe-index.jsonl"),
                "runs_dir": str(tmp / "run-state/runs"),
            },
            "connectors": [
                {"id": "conv", "kind": "claude-conversations", "source_path": str(conv)},
                {"id": "meet", "kind": "meeting-transcripts",
                 "source_globs": [str(meet / "**/*.vtt")]},
                {"id": "wa", "kind": "whatsapp-threads", "enabled": True,
                 "deferred_note": "deferred by design"},
            ],
        }
        cfg_path = tmp / "config.yaml"
        cfg_path.write_text(yaml.safe_dump(cfg), encoding="utf-8")
        ctx = build_context(cfg, cfg_path)
        m1 = cmd_plan(cfg, ctx)
        assert sum(c["new"] for c in m1["summary"]) == 2, m1["summary"]
        # advance, then re-plan: the two items must now be duplicates (idempotent)
        cmd_advance(Path(m1["_manifest_path"]), ctx)
        ctx2 = build_context(cfg, cfg_path)
        m2 = cmd_plan(cfg, ctx2)
        assert sum(c["new"] for c in m2["summary"]) == 0, m2["summary"]
        assert any(c["deferred"] == 1 for c in m2["summary"]), m2["summary"]
        print("self-test OK: 2 new -> advance -> 0 new (idempotent), deferred surfaced")
        return 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Project State-Sync ingest helper")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p_plan = sub.add_parser("plan", help="enumerate new items -> manifest (read-only)")
    p_plan.add_argument("--config", required=True)
    p_plan.add_argument("--json", action="store_true", help="print full manifest JSON")
    p_adv = sub.add_parser("advance", help="append dedupe + advance watermarks (mutating)")
    p_adv.add_argument("--config", required=True)
    p_adv.add_argument("--run", required=True, help="path to a run manifest json")
    p_show = sub.add_parser("show", help="print current watermarks + ledger sizes")
    p_show.add_argument("--config", required=True)
    sub.add_parser("self-test", help="synthetic smoke test")

    args = ap.parse_args(argv)

    if args.cmd == "self-test":
        return _self_test()

    config_path = Path(os.path.abspath(args.config))
    cfg = _load_cfg(config_path)
    ctx = build_context(cfg, config_path)

    if args.cmd == "plan":
        manifest = cmd_plan(cfg, ctx)
        if getattr(args, "json", False):
            print(json.dumps(manifest, indent=2, ensure_ascii=False))
        else:
            _print_plan_summary(manifest)
        return 0

    if args.cmd == "advance":
        res = cmd_advance(Path(os.path.abspath(args.run)), ctx)
        print(json.dumps(res, indent=2, ensure_ascii=False))
        return 0

    if args.cmd == "show":
        print(json.dumps({
            "watermarks_path": str(ctx["watermarks_path"]),
            "watermarks": ctx["watermarks"],
            "dedupe_keys": len(load_dedupe_keys(ctx["dedupe_path"])),
        }, indent=2, ensure_ascii=False))
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
