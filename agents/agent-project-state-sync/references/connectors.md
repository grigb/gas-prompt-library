# PSS Connector Catalog and Contract

Part of the Project State-Sync method
(`/Users/grig/.agents/docs/methodologies/project-state-sync-method.md`). A
connector is a pluggable INGEST adapter: it enumerates NEW raw source items since
its watermark and hands them over. It never classifies, translates, promotes, or
mutates project truth. Translation and reconciliation happen downstream.

## Connector contract

A connector, given its config entry and the run context, returns a list of raw
item records. Each real item carries:

- `connector_id`, `kind`
- `source_item_id` (stable within the connector; e.g. a session id, a filename)
- `content_sha256` (over the canonical source content)
- `dedupe_key` = `{connector_id}:{source_item_id}:{content_sha256}`
- `source_path` (absolute)
- `item_mtime` / `item_mtime_iso`
- `retain_strategy` (`immutable-reference` or `copy`) and `retain_ref` (absolute)
- `hint` (free-form type hint for the translate step)

Guarantees every connector must honor:

- Enumerate only items strictly newer than the connector cursor.
- Preserve provenance and compute the hash from canonical content before any
  synthesis.
- Never modify or delete a source. Retain is by reference unless the source is
  ephemeral, in which case copy verbatim into the SITS raw archive.
- Treat errors as state: emit an error item (`state: error`) and let the run
  continue. Never silently skip.
- Do not let an LLM crawl app databases, browser profiles, or broad filesystem
  paths. Deterministic enumeration only (SITS adapter rule).

The deterministic connectors below are implemented in `pss_ingest.py`. The
translate step reads their manifest; it is the only step allowed to classify.

## Built-in connectors

### claude-conversations  (RUNNABLE)

Reads Claude session transcript JSONL directly from the project's
`{HOME}/.claude/projects/<project-dir>/*.jsonl` store, enumerating files whose
mtime is newer than the cursor. Retain = immutable reference (the JSONL is
already durable).

IMPORTANT: the `css` / `claude-session-search.sh` helper referenced in
`~/.claude/CLAUDE.md` and in WO-366 DOES NOT EXIST on disk (it is documented but
was never built). This connector therefore does not shell out to `css`; it reads
the JSONL store directly, which is the deterministic source of truth. If a
harness exposes native session tools (for example `mcp__ccd_session_mgmt__*`),
the translate step may use them to read a session's content, but enumeration
stays file-based so the connector is harness-independent.

Config keys: `source_path` (the project's `.claude/projects/<dir>/`).

### meeting-transcripts  (RUNNABLE, with ASK-THE-OWNER fallback)

Scans configured globs for meeting transcript files (`.vtt`, `.txt`, `.md`,
`.json`) newer than the cursor and retains them by reference. Typical sources: a
project's meeting folders that follow the `raw/` + `processed/` convention, a
global capture directory, and an owner drop location.

ASK-THE-OWNER fallback: this connector only enumerates transcripts that EXIST. It
never fabricates one. Detecting a referenced-but-absent meeting (a calendar
event, a WO that says "consume this meeting", or an owner mention with no
transcript on disk) and asking the owner for it is the runbook's job in the
report step, not the enumerator's. The skill cross-references the window's WOs,
calendar, and owner mentions against found transcripts and lists any gap as an
owner ask with the exact drop path.

Config keys: `source_globs` (list of absolute globs, `**` supported),
`extensions` (optional override), `retain_strategy` (optional).

### project-inbox  (RUNNABLE, thin)

Reads new markdown packets from the project's inbox directories since the cursor
(for example a liaison inbox and a steward intake drop). Thin by design: it
enumerates packets; SITS classification and promotion happen in translate.
README / INDEX / protocol files are skipped.

Config keys: `source_dirs` (list of absolute inbox dirs).

### whatsapp-threads  (EXTENSION POINT, deferred by default)

WhatsApp has real upstream tooling in mature projects (a consume script plus
consumption cursors and tail checkpoints). Auto-running it from PSS would move a
live cursor that other steward flows depend on, so this connector is DEFERRED by
default: it emits a single informational item so the run report surfaces it, and
does not run the consume tool. To activate it for a project, wire the project's
existing consume tool as a deterministic pre-step that writes durable transcript
chunks into a directory, then point a `project-inbox` or `meeting-transcripts`
connector at that directory. Do not have PSS drive the live WhatsApp cursor until
that path is tested per project.

Config keys: `enabled`, `tool` (path to the project consume tool, informational),
`deferred_note`.

### deferred  (generic extension stub)

Any source with real tooling but deferred auto-run uses `kind: deferred` to
appear in reports without running. Use it to register a known-but-not-yet-wired
stream so it is visible, not forgotten.

## Adding a new connector

Two portable options, cheapest first:

1. Config-only reuse. If the new source can be reduced to "new files in a
   directory" or "new transcripts matching a glob", point a `project-inbox` or
   `meeting-transcripts` connector at it. No code change. This is the SITS
   principle: a new stream is a new registry entry, not a prompt edit.
2. New connector kind. If the source needs bespoke deterministic enumeration
   (an export format, an API pull), add a function to `pss_ingest.py`'s
   `CONNECTOR_DISPATCH` following the contract above, or register it as a SITS
   deterministic importer and have PSS read that importer's output directory via
   option 1. Prefer registering under SITS when the stream is owner-private, so
   privacy boundaries and the promotion ledger are inherited.

Never hardcode a project's absolute source path into `pss_ingest.py`; paths come
from the project config.
