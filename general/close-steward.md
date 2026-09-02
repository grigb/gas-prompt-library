# Steward Session Close Preflight - Internal Subroutine

This prompt is the steward-specific capture preflight for
`/Users/grig/.agents/prompts/creation/CREATE-SESSION-RECORD.md`.

It is normally invoked by `CREATE-SESSION-RECORD.md` when the active role is
Project Steward or Master Steward. The owner should not have to remember or
call a separate steward closeout prompt.

If this prompt is invoked directly, run the same preflight, produce the capture
packet below, then return to
`/Users/grig/.agents/prompts/creation/CREATE-SESSION-RECORD.md` so there is one
final session record. Do not create a second standalone steward closeout record
unless the owner explicitly asks for one.

This preflight is artifact-only. It does not rename, archive, close, move,
create, fork, hand off, or replace a visible task. Apply the separate
task-lifecycle authority and successor-continuity gate in
`CREATE-SESSION-RECORD.md` before any such action.

## Routing

Before imposing steward-only requirements, determine whether this session has
Project Steward or Master Steward signals.

Use these signals when the owner did not specify the role:

- explicit role assignment or loaded prompt;
- Master Steward overlay, Master Steward startup overlay, or master-steward
  private paths under `/Users/grig/.agents-private/project-steward/master-steward/`;
- project-local steward role directories and artifacts under
  `{PROJECT_ROOT}/.dev/ai/roles/project-steward/`;
- session scope: single project means Project Steward; cross-project portfolio,
  priority, grouping, activation, dispatch-locality, or steward-of-stewards
  work means Master Steward.

Routing outcomes:

- If no steward signals exist, output
  `STEWARD CLOSE PREFLIGHT: not applicable - continue normal CREATE-SESSION-RECORD flow.`
  Then stop this subroutine and return to normal `CREATE-SESSION-RECORD.md`
  handling. Do not impose steward-only capture requirements.
- If Project Steward signals exist and no Master Steward signals exist, run the
  Project Steward checklist only.
- If Master Steward signals exist, run the Project Steward checklist first,
  then run the Master Steward additions.
- If both signal sets appear, treat the session as Master Steward when any
  Master Steward overlay, master-steward private path, or cross-project
  portfolio scope is present. Otherwise treat it as Project Steward.

## Non-Negotiable Capture Standard

Before final session record creation, complete every applicable step below. Do
not skip steps. Do not say "already done" without naming the file path. If a
step produces no output, say `N/A - nothing to capture` for that step.

The unified session-record flow does not weaken steward capture obligations.
This preflight exists because steward sessions must preserve corrections, owner
decisions, monologues, new facts, project wisdom, WO/index sync, active
constraints, tuning failures, and, for Master Steward, portfolio state before
the final session record is written.

**Ground-truth re-scan applies here too.** Any "blocked", "done", "dirty tree",
or "newest artifact" claim you make in this preflight (e.g. WO/INDEX sync status,
remaining-work state) is governed by the Ground-Truth Re-Scan Gate in
`/Users/grig/.agents/prompts/creation/CREATE-SESSION-RECORD.md`. Before asserting
such state, re-run `git status --short`, check `ls -t .dev/ai/unblocks/ | head`,
and re-read the live `status:` of any WO/blocker you characterize. The
`ground_truth_rescanned_at:` stamp is owned by the calling CREATE-SESSION-RECORD
flow; this subroutine must not contradict it.

## Provenance for Steward Capture Artifacts

Every capture artifact created or updated by this preflight must include
provenance in frontmatter, an adjacent metadata block, or a dated log entry.
Use the artifact's existing style; do not corrupt structured files.

Include:

- `agent_task_id`: current task/session/thread identifier if available; if not
  available, use `unknown-not-provided` and do not invent one;
- `steward_role_type`: `project-steward` or `master-steward`;
- `source_closeout_prompt_path`:
  `/Users/grig/.agents/prompts/creation/CREATE-SESSION-RECORD.md`;
- `steward_subroutine_path`:
  `/Users/grig/.agents/prompts/general/close-steward.md`;
- `source_work_orders_or_handoffs`: source WO paths, handoff paths, or `N/A`;
- `files_updated`: absolute paths updated by this capture step.

Do not use `/Users/grig/.agents/prompts/general/close-steward.md` as
`source_closeout_prompt_path` for supporting capture artifacts produced under
the unified closeout flow. `source_closeout_prompt_path` identifies the
owner-facing closeout prompt. `steward_subroutine_path` identifies this
internal steward preflight.

## Project Steward Checklist

### 0. Current Project Steward Lane And Shared Project-Local Surface Safety

Treat this closeout as recording only the current Project Steward session lane,
not retiring the visible task, closing the project, the whole Project Steward
role, sibling project lanes, or any active Orchestrator/worker/Supervisor lane.
Record lane identity:
project root, role, mode, harness, thread/session id or handle when available,
thread title/name when available, `agent_task_id` when available, and final
session-record path. Use `unknown-not-provided` for unavailable fields.

`.dev/ai/sessions/` is one-record-per-session. Write this session's record or
capture packet as its own record and never rewrite, delete, clear, or
supersede sibling session records. A fresh successor Project Steward may read
the record as context, but does not inherit execution, dispatch, status/index
progression, source-processing, or worker-launch permission from it.

Treat `{PROJECT_ROOT}/.dev/ai/roles/project-steward/` as shared project-local
state. Prefer one-file-per-memory or one-file-per-session notes and append-only
addenda. Replacement writes require a safe writer, lock, base hash, or owned
managed block. Do not replace shared steward files just to make this closeout
look final.

Before replacing `{PROJECT_ROOT}/.dev/ai/PROJECT-STATUS.md`, reread active
Project Steward, Orchestrator, worker, and Supervisor ledgers/status files for
this project and preserve unresolved sibling-lane state. If that preservation
cannot be proven, write an addendum, session record, relay/result artifact, or
owned managed block instead of replacement. When a sibling Project Steward or
Orchestrator exists, report or relay this closeout result without overwriting
their queue, status, ledger, or ownership surfaces.

Use partial-lane wording such as `this Project Steward session record is
complete; the visible task remains active unless a separate lifecycle gate
completed; other project lanes may remain active`. Avoid `project complete`,
`stewardship complete`, and `nothing else is active` unless current evidence
proves no sibling Project Steward, Orchestrator, worker, or Supervisor lane
remains active, or the claim is explicitly scoped to this session.

### 1. Corrections

Scan this conversation for every owner correction ("don't do X", "stop",
"that's wrong", "no", "you should have", any frustration signal). For each:

- State what the owner corrected in one line.
- Create a memory file NOW if one does not already exist.
- Add the provenance required above.
- State the absolute file path.

If zero corrections: `No corrections this session.`

### 2. Decisions

Scan for every owner decision ("approved", "go with X", "we're doing Y",
"use X", "defer", "kill", any choice made). For each:

- State the decision in one line.
- Record it in the appropriate artifact: `decision-log.md`,
  `active-constraint.md`, memory file, or WO status update.
- Add the provenance required above.
- State the absolute file path.

If zero decisions: `No decisions this session.`

### 3. Monologues

Scan for any substantive owner monologue: 3+ sentences of strategic thinking,
venting, planning, or context-sharing. For each:

- Save raw to `{PROJECT_ROOT}/.dev/ai/conversations/` if not already saved.
- Add the provenance required above.
- State the absolute file path.

If zero monologues: `No monologues this session.`

### 4. New Facts

Scan for any new facts learned this session: credentials, paths, people,
relationships, constraints, tool behaviors, project state changes. For each:

- Store in the right layer: project-local memory, universal role memory, or
  private owner context.
- Add the provenance required above.
- State the absolute file path.

If zero new facts: `No new facts this session.`

### 5. Project Wisdom

Did you learn anything about how this project works, what patterns succeed or
fail, or what the owner cares about for this project specifically? If yes,
update `{PROJECT_ROOT}/.dev/ai/roles/project-steward/project-wisdom.md` with
the provenance required above.

If no update is needed: `N/A - no project wisdom update.`

### 6. WO + INDEX Sync

Check every WO you touched this session. Is the WO file status consistent with
the project-local `WO-INDEX.md`? Fix any mismatches now and list the absolute
paths updated.

The GAS root is different: its work-order index is generated from WOQ and is
**not** hand-maintained. `/Users/grig/.agents/.dev/ai/workorders/WO-INDEX.md` is
retired; the index is
`/Users/grig/.agents/.dev/ai/workorders/WO-INDEX.woq-generated-view.md`.
Hand-writes to it are refused. Do not update the index and do not queue an index
change for it — fix the Work Order file only, with
`/Users/grig/.agents/.venv/bin/python3 -m tools.woq.cli work-order write`, and
the index is rebuilt from it. Owner-approved cutover 2026-08-12,
WO-GAS-WOQLIVE-014; details in
`/Users/grig/.agents/docs/protocols/woq-role-lifecycle.md`.

**Last step — cascade terminal completions (GASINTEG-A).** For every WO or blocker
you moved to a terminal state this session (WO `COMPLETED`/`SUPERSEDED`; blocker
`resolved`/`unresolvable`/`superseded`), run the reconcile cascade as the final
action so dependents never sit falsely blocked after their gate clears:

```
~/.agents/.venv/bin/python3 ~/.agents/scripts/reconcile-dependents.py <wo-id|blocker-id>
```

It is idempotent and conservative (sole-gate-cleared → auto-flip + emit a downstream
unblock artifact; one-of-several-gates → note only; protected owner/legal/payment gates
→ flag, never auto-close). List any downstream unblocks it emitted. The cataloger's
Phase 3b runs the same sweep on every refresh, so this is belt-and-suspenders for the
write-time path — never a substitute for it.

If no WOs were touched: `N/A - no touched WOs.`

### 7. Active Constraint

Did the active constraint change? If yes, update `active-constraint.md` with
the provenance required above. If you are not sure, re-read it and confirm it
still reflects reality.

If unchanged: `Active constraint unchanged.`

### 8. Tuning Log

Did you notice any behavioral failure in yourself this session - something the
prompt should have prevented but did not? If yes, append to the tuning log at
`/Users/grig/.agents/agents/tuning/steward-tuning-log.md`. Do NOT fix your own
prompt. Add the provenance required above.

If zero tuning issues: `No steward tuning issues noticed.`

## Master Steward Additions

Run this section only when the routing step classified the session as Master
Steward.

Before writing any Master Steward closeout artifact, apply the overlay-specific
Concurrent Closeout And Shared-Home Preservation rule in
`/Users/grig/.agents/docs/overviews/MASTER-STEWARD-VARIANT.md#concurrent-closeout-and-shared-home-preservation`.

### 9. Current-Lane Retirement And Sibling-Lane Preservation

Treat this closeout as recording only the current Master Steward session lane,
not retiring the visible task or shutting down Master Steward globally. Record lane identity: role, mode,
harness, thread/session id or handle when available, thread title/name when
available, `agent_task_id` when available, active project or portfolio scope,
and session-record path. Use `unknown-not-provided` for unavailable fields.

Use partial-lane wording such as `this Master Steward session record is
complete; the visible task remains active unless a separate lifecycle gate
completed` unless a fresh preflight and sibling-lane reconciliation actually prove no
sibling Master Steward lanes remain active or pending and the current session
has authority to make a global closeout claim. Preserve sibling Master Steward
lanes and pending worker/orchestrator activity discovered in session records,
subtask-comms, active-agent ledgers, status reports, relay manifests, explicit
owner context, or current harness state.

Write shared Master Steward home updates only through append-only addenda,
one-file-per-session notes, owned managed blocks, or a safe
writer/lock/base-hash mechanism. Never clear or rewrite
`/Users/grig/.agents-private/project-steward/master-steward/` indexes,
ledgers, memory, knowledge summaries, inboxes, state files, or session notes
based only on this session closeout. Label any portfolio snapshot as this
current lane's last verified view unless a fresh portfolio preflight and
sibling-lane reconciliation actually ran during closeout.

Relay to another Master Steward only with proof of a distinct target
session/thread. Without distinct target proof, record durable state for
takeover and do not require a Master-Steward-to-itself acknowledgement.

### 10. Knowledge Tree

For every project discussed this session where a decision was made, the phase
changed, or new context was shared: update
`/Users/grig/.agents-private/project-steward/master-steward/knowledge/projects/{slug}.md`
and bump `last_updated`. Update `MASTER-INDEX.md` if the phase or priority line
changed. Add the provenance required above. List every absolute file path you
updated.

If no projects discussed: `No knowledge tree updates.`

### 11. Supervisor Sync

Did this session resolve a blocker, complete a WO, or make an owner decision
the supervisor tracks? If yes, append to
`/Users/grig/.agents/agents/blocker-engineer/ms-updates.md` with the provenance
required above.

If not applicable: `MS supervisor sync: no.`

### 12. Dispatch Surface

Did this session identify blocker-lifecycle work for the supervisor? If yes,
write to `/Users/grig/.agents/agents/blocker-engineer/ms-dispatch.md` with the
provenance required above.

If not applicable: `MS dispatch entries: 0.`

### 13. Inbox

Are there owner thoughts from this session that arrived while work was running
and have not been filed? If yes, file them to the Master Steward inbox at
`/Users/grig/.agents-private/project-steward/master-steward/inbox/` with the
provenance required above.

If not applicable: `MS inbox updates: 0.`

## Capture Packet for CREATE-SESSION-RECORD

After completing the applicable checklist, output this packet. The calling
`CREATE-SESSION-RECORD.md` flow embeds or references this packet in one final
session record suitable for same-role takeover.

```text
STEWARD CLOSE CAPTURE PACKET:
  Steward role type: [project-steward|master-steward|not-applicable]
  Agent task ID: [id or unknown-not-provided]
  source_closeout_prompt_path: /Users/grig/.agents/prompts/creation/CREATE-SESSION-RECORD.md
  steward_subroutine_path: /Users/grig/.agents/prompts/general/close-steward.md
  Source work orders or handoffs: [paths or N/A]
  Files updated: [absolute paths or N/A]
  Project root: [absolute path or unknown-not-provided]
  Lane mode: [mode or unknown-not-provided]
  Harness: [harness or unknown-not-provided]
  Thread/session id or handle: [id/handle or unknown-not-provided]
  Thread title/name: [title/name or unknown-not-provided]
  Session record path: [absolute path or unknown-not-provided]
  Project Steward current-lane retirement: [recorded/N/A]
  Visible task lifecycle authority: [record-only/separate explicit owner instruction]
  Successor continuity before archive: [not-required/ready-with-receipt/required-not-established]
  Project Steward sibling-lane preservation: [preserved/no sibling evidence/N/A]
  Project Steward shared-surface write mode: [append-only/one-file-per-session/safe-writer/managed-block/N/A]
  PROJECT-STATUS ledger preservation: [reread-and-preserved/addendum-only/N/A]
  Project Steward sessions policy: one-record-per-session
  Successor steward permission: context-only/no inherited execution permission
  Corrections captured: [count] ([paths])
  Decisions recorded: [count] ([paths])
  Monologues saved: [count] ([paths])
  New facts stored: [count] ([paths])
  Project wisdom updated: [yes/no]
  WO/INDEX mismatches fixed: [count]
  Active constraint: [updated/unchanged]
  Tuning log entries: [count]
  MS current-lane retirement: [recorded/N/A]
  MS sibling-lane preservation: [preserved/no sibling evidence/N/A]
  MS shared-home write mode: [append-only/one-file-per-session/safe-writer/managed-block/N/A]
  MS portfolio snapshot label: [current lane last verified view/fresh preflight reconciled/N/A]
  MS knowledge tree updates: [count or N/A]
  MS supervisor sync: [yes/no or N/A]
  MS dispatch entries: [count or N/A]
  MS inbox updates: [count or N/A]
  Summary for final session record: [brief same-role takeover summary]
```

Then return to
`/Users/grig/.agents/prompts/creation/CREATE-SESSION-RECORD.md` for the final
session record. Do not produce a second final record.
