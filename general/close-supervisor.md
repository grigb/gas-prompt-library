# Supervisor Session Close Preflight - Internal Subroutine

This prompt is the supervisor-specific capture preflight for
`/Users/grig/.agents/prompts/creation/CREATE-SESSION-RECORD.md`.

It is normally invoked by `CREATE-SESSION-RECORD.md` when the active role is
Blocker Supervisor, Supervisor, or Supe. The owner should not have to remember
or call a separate supervisor closeout prompt.

If this prompt is invoked directly, run the same preflight, produce the capture
packet below, then return to
`/Users/grig/.agents/prompts/creation/CREATE-SESSION-RECORD.md` so there is one
final session record. Do not create a second standalone supervisor closeout
record unless the owner explicitly asks for one.

## Routing

Before imposing supervisor-only requirements, determine whether this session has
Blocker Supervisor signals.

Use these signals when the owner did not specify the role:

- explicit Blocker Supervisor, Supervisor, or Supe role assignment;
- loaded prompt or charter under
  `/Users/grig/.agents-gas-prompt-library/agents/agent-blocker-supervisor/` or
  `/Users/grig/.agents/agents/blocker-engineer/SUPERVISOR.md`;
- blocker files, blocker indexes, supervisor runstate/status, or blocker
  lifecycle work under `/Users/grig/.agents/agents/blocker-engineer/`;
- project-local blocker lifecycle artifacts under
  `{PROJECT_ROOT}/.dev/ai/blockers/`;
- session scope: blocker discovery, cataloging, owner-attention blocker gates,
  unblock routing, registry/control-plane work, manual lifecycle mutation,
  supervisor-owned dispatch, or Master Steward to Supervisor sync.

Routing outcomes:

- If no supervisor signals exist, output
  `SUPERVISOR CLOSE PREFLIGHT: not applicable - continue normal CREATE-SESSION-RECORD flow.`
  Then stop this subroutine and return to normal `CREATE-SESSION-RECORD.md`
  handling. Do not impose supervisor-only capture requirements.
- If supervisor signals exist, run the Supervisor checklist below.
- If the session also has Project Steward or Master Steward signals, keep this
  preflight limited to supervisor-owned blocker state. Do not import Steward
  correction, monologue, project-wisdom, or knowledge-tree capture obligations.

## Non-Negotiable Capture Standard

Before final session record creation, complete every applicable step below. Do
not skip steps. Do not say "already done" without naming the file path. If a
step produces no output, say `N/A - nothing to capture` for that step.

The unified session-record flow does not weaken supervisor state-capture
obligations. This preflight exists because supervisor sessions must preserve
blocker routing truth, current source-of-truth state, owner-attention blockers,
Master Steward sync needs, and dispatch/no-poll compliance before the final
session record is written.

## Authoritative State and False-Stale Standard

Supervisor closeout must separate verified current state from inherited claims.

Authoritative state hierarchy:

- Individual blocker files are authoritative for blocker lifecycle status.
- Project blocker indexes and
  `/Users/grig/.agents/.dev/ai/blockers/MASTER-INDEX.md` are summary surfaces.
- `SUPERVISOR-RUNSTATE.md`, `SUPERVISOR-STATUS.md`, and generated views are
  working surfaces that can become stale.
- Old session records, subtask-comms artifacts, dispatch ledgers, and index
  summaries are provenance or hints, not final proof of current blocker state.

For every blocker touched, record one of:

- `verified_current`: you checked the authoritative blocker file or refreshed
  source surface during this closeout;
- `inherited_unverified`: the state came from a session record, index, old
  status surface, or agent claim and must not be treated as current;
- `changed_this_session`: the blocker changed during this session, with before
  and after status plus the authoritative file path.

If a claim is stale, contradicted, or unverified, say so plainly in the capture
packet. Do not hand a successor a stale blocker claim as if it were current.

This blocker-state hierarchy is the supervisor specialization of the shared
**Ground-Truth Re-Scan Gate** in
`/Users/grig/.agents/prompts/creation/CREATE-SESSION-RECORD.md`, which also
governs two dimensions beyond blocker files: the **working tree** (run `git
status --short` — never report an inherited "dirty"/"clean") and the **newest
unblock artifact** (run `ls -t .dev/ai/unblocks/ | head` — never cite an inherited
"newest already processed"). Run those two checks here as well before any
blocked/done/dirty/newest claim. The `ground_truth_rescanned_at:` stamp is owned
by the calling CREATE-SESSION-RECORD flow; nothing in this preflight may
contradict it. The peermesh-social closeout that called a committed tree "dirty"
and cited a stale "newest unblock" is exactly the failure this gate prevents.

## Supervisor Checklist

### 0. Current Supervisor Lane And Shared Blocker-State Safety

Treat this closeout as retiring only the current Supervisor session lane, not
closing global blocker supervision, the whole Blocker Supervisor role, sibling
Supervisor lanes, or any active unblocker, cataloger, project, or worker lane.
Record lane identity: role, supervisor mode, harness, thread/session id or
handle when available, thread title/name when available, `agent_task_id` when
available, blocker scope touched, and final session-record path. Use
`unknown-not-provided` for unavailable fields.

Treat shared blocker state as concurrent-lane state that other Supervisor lanes
may be using right now: `/Users/grig/.agents/.dev/ai/blockers/` including
`MASTER-INDEX.md` and project `INDEX.md`, individual blocker lifecycle files,
`SUPERVISOR-RUNSTATE.md`, `SUPERVISOR-STATUS.md`, the owner-attention queue,
`ms-updates.md`, `ms-dispatch.md`, processed-ack obligations, and relay/archive
manifests. Never clear, rewrite, or reset these just to make this closeout look
final. Write shared blocker state only through the canonical blocker lifecycle
command, `tools.woq.cli shared-status write` with a current target hash, a
one-file append-only status artifact, an owned managed block, or a safe
writer/lock/base-hash mechanism.

Preserve unresolved sibling Supervisor, unblocker, cataloger, project-lane, and
worker activity discovered in master indexes, status reports, relay manifests,
open-agent ledgers, or blocker lifecycle files. One Supervisor closeout must not
close, archive, clear, supersede, or mark complete another Supervisor session,
another supervisor-owned worker, or a blocker lane it does not own without
distinct target proof plus explicit authority. Same-role relay stays
external-only: do not archive sibling Supervisor sessions or require a
Supervisor-to-itself `processed_ack`, and direct-relay to another Supervisor
only with proof of a distinct target session/thread. If direct relay is
unavailable, write a durable not-delivered fallback rather than making the owner
copy and paste by default. A fresh successor Supervisor may read this session
record for context but does not inherit execution, dispatch, or
blocker-lifecycle-mutation permission from it.

Use partial-lane wording such as `this Supervisor session lane is closed; other
supervisor lanes may remain active`. Do not write `global blocker supervision
complete`, `all blockers resolved`, or `nothing else is active` unless fresh
live blocker files, master index, and relay/ack evidence prove no sibling
Supervisor lane remains active and this session has authority for that global
claim. This section preserves, and does not weaken, the existing scan-first,
dispatch-don't-grind, no-poll, gate-validity preflight, ground-truth re-scan,
phone-first owner output, and self-recipient filter rules; closeout does not
authorize project execution, ordinary project orchestration, or inline
implementation.

### 1. Supervisor Mode

Classify the session mode as exactly one of:

- `advisor`
- `catalog`
- `unblocker`
- `registry`
- `manual-lifecycle`
- `unknown`

Use the dominant mode from actual work performed, not the owner's initial
phrase. If multiple modes occurred, list secondary modes in the notes.

### 2. Blockers Touched

For every blocker touched, capture:

- blocker ID;
- project name and project path when known;
- authoritative blocker file path;
- status before;
- status after;
- whether state is `verified_current`, `inherited_unverified`, or
  `changed_this_session`;
- evidence path or command/source used for the state claim;
- unresolved gate, if any.

If no blocker was touched: `Blockers touched: 0.`

### 3. Master Index and Project Index Sync

Capture whether these surfaces changed or need sync:

- `/Users/grig/.agents/.dev/ai/blockers/MASTER-INDEX.md`;
- any project-local `.dev/ai/blockers/INDEX.md`, generated blocker view, or
  blocker status surface touched by the session.

For each surface, record:

- `changed`, `in-sync`, `needs-sync`, `not-checked`, or `not-applicable`;
- absolute file path;
- reason.

Do not claim indexes are synchronized unless they were actually checked or
refreshed during the session.

If this preflight or the calling session closeout writes
`/Users/grig/.agents/.dev/ai/blockers/INDEX.md`, reread
`/Users/grig/.agents/docs/protocols/woq-role-lifecycle.md` and use
`/Users/grig/.agents/.venv/bin/python3 -m tools.woq.cli shared-status write`
with a current target hash. Do not carry an index replacement forward from
inherited context.

### 4. Workstream Routing

Capture blocker lifecycle work by workstream:

- dispatched;
- deferred;
- completed;
- needing owner attention;
- routed to project orchestrator/agent;
- routed to Master Steward;
- not applicable.

For each item, include the blocker ID, workstream name when known, target role,
artifact path, and current routing state.

### 5. Owner-Attention Queue

List every blocker requiring owner input.

Each item must include:

- blocker ID;
- exact blocker file path;
- plain-language owner ask;
- action type: verbal approval, choose between options, provide information, do
  something external, delegate, credential/authentication, payment/legal, or
  ownership/destructive action;
- what the answer unblocks.

If no owner-attention blockers remain: `Owner-attention queue: empty.`

### 6. Master Steward Sync

Capture whether either file needs or received an entry:

- `/Users/grig/.agents/agents/blocker-engineer/ms-updates.md`;
- `/Users/grig/.agents/agents/blocker-engineer/ms-dispatch.md`.

Use:

- `entry-written`;
- `entry-needed`;
- `not-needed`;
- `not-checked`.

If an entry is needed but not written, include the exact pending message and why
it was not written during closeout.

### 7. Dispatch and No-Poll Compliance

Record supervisor-owned workers or external dispatches without instructing the
successor to poll them.

For each active or completed worker/dispatch, capture:

- worker or dispatch ID when available;
- purpose;
- work order or handoff path;
- expected result artifact path;
- ledger/runstate path;
- current known state;
- whether a native completion notice, result artifact, or bounded critical-path
  synchronization is still required.

Do not write "poll", "watch", "tail", "keep checking", or any equivalent
successor instruction. The successor may use native completion notices, read a
named result artifact after a completion event, or perform one bounded
critical-path synchronization only when blocked on that exact result.

### 8. Files Updated

List every file updated during the supervisor session or this preflight. Include
only absolute paths. If no files were updated: `Files updated: none.`

### 9. Next Supervisor Action

Provide exactly one concrete next supervisor action based on current blocker
state.

Valid forms:

- work the next named actionable supervisor-owned blocker;
- refresh a named stale index or project blocker view before lifecycle mutation;
- present the single owner-attention gate named above;
- reconcile one named completed worker result after native completion notice or
  bounded critical-path synchronization;
- route a named handoff to the named project orchestrator/agent;
- report `queue empty` only when no actionable, owner-gated, stale, or routed
  supervisor-owned work remains.

Do not end with a generic "continue", "say next", or bare blocker/work-order ID.

## Capture Packet for CREATE-SESSION-RECORD

After completing the checklist, output this packet. The calling
`CREATE-SESSION-RECORD.md` flow embeds or references this packet in one final
session record suitable for same-role takeover.

```text
SUPERVISOR CLOSE CAPTURE PACKET:
  Supervisor closeout applicable: [yes|no]
  ground_truth_rescanned_at: [YYYY-MM-DDTHH:MM:SSZ — from the shared re-scan gate; required if any blocked/done/dirty/newest claim follows]
  git_status_short: [EMPTY — tree clean | list of genuinely-uncommitted files]
  newest_unblock_artifact: [top of `ls -t .dev/ai/unblocks/`, or none]
  Supervisor mode: [advisor|catalog|unblocker|registry|manual-lifecycle|unknown]
  Secondary modes: [list or N/A]
  Agent task ID: [id or unknown-not-provided]
  Harness: [harness or unknown-not-provided]
  Thread/session id or handle: [id/handle or unknown-not-provided]
  Thread title/name: [title/name or unknown-not-provided]
  Blocker scope touched: [scope or unknown-not-provided]
  Session record path: [absolute path or unknown-not-provided]
  Supervisor current-lane retirement: [recorded/N/A]
  Supervisor sibling-lane preservation: [preserved/no sibling evidence/N/A]
  Supervisor shared blocker-state write mode: [canonical-lifecycle/shared-status-write/append-only/managed-block/safe-writer/N/A]
  Supervisor partial-lane wording: [this Supervisor session lane is closed; other supervisor lanes may remain active/global-final-proven/N/A]
  Successor supervisor permission: context-only/no inherited execution or lifecycle-mutation permission
  supervisor subroutine path: /Users/grig/.agents/prompts/general/close-supervisor.md
  Session record entrypoint: /Users/grig/.agents/prompts/creation/CREATE-SESSION-RECORD.md
  Source work orders or handoffs: [absolute paths or N/A]
  Authoritative state files checked:
    - [absolute path] - [purpose]
  Blockers touched:
    - blocker_id: [id]
      project: [name or unknown]
      project_path: [absolute path or unknown]
      blocker_path: [absolute path]
      status_before: [status or unknown]
      status_after: [status or unchanged]
      state_integrity: [verified_current|inherited_unverified|changed_this_session]
      evidence: [path/source]
      remaining_gate: [gate or N/A]
  Master index sync:
    - path: /Users/grig/.agents/.dev/ai/blockers/MASTER-INDEX.md
      state: [changed|in-sync|needs-sync|not-checked|not-applicable]
      reason: [brief reason]
  Project index sync:
    - path: [absolute path]
      state: [changed|in-sync|needs-sync|not-checked|not-applicable]
      reason: [brief reason]
  Workstream routing:
    - blocker_id: [id or N/A]
      workstream: [name or unknown]
      routing_state: [dispatched|deferred|completed|needing-owner-attention|routed-to-project|routed-to-MS|not-applicable]
      target_role: [role or N/A]
      artifact_path: [absolute path or N/A]
  Owner-attention queue:
    - blocker_id: [id]
      blocker_path: [absolute path]
      action_type: [type]
      exact_ask: [copy-pasteable ask]
      unblocks: [plain-language outcome]
  MS sync:
    ms-updates.md: [entry-written|entry-needed|not-needed|not-checked]
    ms-dispatch.md: [entry-written|entry-needed|not-needed|not-checked]
    pending_entry: [exact text or N/A]
  Dispatch/no-poll state:
    - worker_or_dispatch_id: [id or unknown]
      purpose: [brief purpose]
      work_order_or_handoff_path: [absolute path or N/A]
      expected_result_path: [absolute path or N/A]
      ledger_or_runstate_path: [absolute path or N/A]
      current_known_state: [state]
      successor_instruction: [native completion notice|read named result after completion|one bounded critical-path sync if blocked|N/A]
  Files updated:
    - [absolute path]
  False-stale notes:
    - [verified/current distinction or N/A]
  Next supervisor action: [one concrete action]
```
