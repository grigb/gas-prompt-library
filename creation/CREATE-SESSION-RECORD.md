# CREATE SESSION RECORD

Create one unified session-close artifact that preserves:
- forward actionability for the next agent or next session
- backward audit traceability for recovery and long-term review

Core principle:
`One session = one record. Forward actions + current state + backward traceability = one artifact.`

This replaces the end-of-session pair of:
- conversation audit
- standard continuation handoff

It does **not** replace orchestration handoffs used for delegation, subtask coordination, or `.dev/ai/subtask-comms/`.

## Single Owner-Facing Closeout Entrypoint

This is the only owner-facing routine session retirement prompt for normal agents, Project Steward sessions, Master Steward sessions, and Blocker Supervisor/Supe sessions. The owner should not have to know which role was active or call a separate steward or supervisor closeout prompt.

The owner's preferred closeout phrase is a first-class trigger for this prompt:

```text
It's time to retire this agent's context. Create a session record. The next agent will takeover the role that you have performed if needed. PLEASE follow all of these instructions (READ ONLY): ~/.agents/prompts/creation/CREATE-SESSION-RECORD.md
```

When this phrase appears, follow this file as the entrypoint even if the session was steward-led or supervisor-led.

## Concurrent Control-Lane Closeout Safety

The owner runs multiple Master Steward, Project Steward, and Blocker Supervisor
sessions at the same time. Closing one control-lane session must be additive,
merge-safe, and order-independent. This umbrella invariant governs every
closeout path and runs before the Role-Aware Closeout Router below and before
any shared-surface write. The role preflights implement the role-specific
detail and must not be duplicated here: the steward preflight
`/Users/grig/.agents/prompts/general/close-steward.md` (sections `### 0` and
`### 9. Current-Lane Retirement And Sibling-Lane Preservation`), the supervisor
preflight `/Users/grig/.agents/prompts/general/close-supervisor.md` (section
`### 0. Current Supervisor Lane And Shared Blocker-State Safety`), and the
Master Steward overlay `Concurrent Closeout And Shared-Home Preservation` in
`/Users/grig/.agents/docs/overviews/MASTER-STEWARD-VARIANT.md`. This section
states the shared model once and references those preflights rather than
re-implementing them.

**Reusable vocabulary.** A `current session lane` is the single session being
retired now. A `sibling lane` is any other Master Steward, Project Steward,
Supervisor, worker, or orchestrator session that may be running concurrently. A
`shared surface` is any file or ledger that concurrent lanes read or write,
such as `.dev/ai/PROJECT-STATUS.md`, role memory indexes, Master Steward
private indexes, blocker master indexes, relay manifests, status ledgers, and
`.dev/ai/sessions/`. `append-only` means adding a new record or addendum
without rewriting existing content. A `safe writer` is a lock, base-hash, owned
managed block, or documented single-writer mechanism that makes a replacement
write concurrency-safe. `distinct target proof` is evidence of a separate
session/thread — a different thread id, handle, title, or named replacement —
that is required before acting on another lane. A `partial lane closeout`
retires only the current session lane and explicitly leaves sibling lanes
intact.

Apply all ten rules below before role routing and before any shared write:

1. **Lane identity first.** Record the `current session lane` identity before
   writing anything: role, mode, project root or global scope, harness,
   thread/session id or handle when available, thread title/name when
   available, `agent_task_id`, and the output session-record path. Use
   `unknown-not-provided` for any unavailable field; do not invent identity.
   If this session is a fork or continuation that inherited another lane's
   context or identity, it must establish and record its OWN distinct lane
   identity — including a fresh session token generated at closeout — and must
   not reuse the parent lane's session-record path or present the parent's
   thread/session id as its own. Inherited identity fields alone do not make a
   lane distinct, because a fork may inherit the parent's `agent_task_id` or
   session id; the fresh session token is what guarantees a fork-safe, distinct
   session-record path.

2. **Current lane only.** The session record retires only the `current session
   lane`. It may describe a `sibling lane` as referenced or active, but it must
   not mark any sibling lane closed, complete, archived, acknowledged,
   processed, cleared, or superseded without distinct current evidence and
   authority for that exact external lane.

3. **Order-independent closeout.** Closing session A before session B, or B
   before A, must leave recoverable state either way. No closeout may depend on
   being the final closeout unless it can prove every required sibling lane is
   already closed or acknowledged. Do not make the owner choose closeout order;
   this invariant makes order irrelevant by construction.

4. **Partial lane closeout wording.** When sibling sessions may remain active,
   write a `partial lane closeout` in plain state such as `this session lane is
   closed; other Master Steward/Project Steward/Supervisor lanes may remain
   active`. Do not write `Master Steward is complete`, `the project is closed`,
   or `Supervisor is done` based only on the current lane.

5. **Append-only by default.** Shared closeout surfaces are `append-only` or
   one-file-per-session by default. A replacement write requires a `safe
   writer`, base hash, lock, or documented single-writer ownership.

6. **Shared-surface write guard.** Before writing to a `shared surface` such as
   `.dev/ai/PROJECT-STATUS.md`, role memory indexes, Master Steward private
   indexes, blocker master indexes, relay manifests, or status ledgers,
   identify whether this closeout is appending, replacing an owned managed
   block, or proposing text for parent assimilation. Never clear or rewrite a
   shared surface just to make this closeout look final.

7. **Sibling-lane preservation.** If active worker, orchestrator, steward, or
   supervisor ledgers exist, reread the relevant ledger immediately before any
   status replacement and preserve unresolved sibling-lane state. If that
   preservation cannot be proven, write an addendum, session record, or owned
   managed block instead of a replacement.

8. **Relay independence.** Same-role relay is allowed only with `distinct
   target proof`. If no distinct target is proven, record the current session
   as closed and relay as not applicable or a durable not-delivered fallback,
   and do not wait for or require self-acks. This preserves, and does not
   weaken, the WO-PI-012 relay contract in `Status Routing and Self-Relay
   Before Final Retirement` below: the self-recipient filter, the `reply_to`
   envelope, fresh receipt evidence, the durable not-delivered fallback,
   processed-ack timing, archive owner/token safety, and the no-polling rule
   all remain binding.

9. **Archive boundary.** The closing session may archive only itself, and only
   when every required external recipient has processed the closeout or no
   external recipients exist. It must not archive a `sibling lane` session
   merely because it found that session's files.

10. **Ground-truth language.** The Ground-Truth Re-Scan Gate below continues to
    govern every `blocked`, `done`, `dirty`, and `newest` claim. This
    concurrency rule additionally governs claims about whole roles, shared
    directories, and sibling session state: a partial-lane view of one shared
    surface is not proof that a sibling lane is closed, complete, or safe to
    overwrite.

### Worked Example — Two Master Steward Lanes, Either Order

Two Master Steward sessions, MS-A and MS-B, share
`/Users/grig/.agents-private/project-steward/master-steward/` and the global
`.dev/ai/sessions/` surface.

- MS-A closes first: it records its own lane identity, writes its own
  one-file-per-session record, appends any shared-home update as an
  `append-only` addendum, and writes the `partial lane closeout` `this Master
  Steward session lane is closed; other Master Steward lanes may remain active`.
  It does not touch MS-B's record, does not mark Master Steward globally
  complete, and does not archive MS-B.
- MS-B closes second: it rereads the shared home, finds MS-A's appended
  addendum still intact, records its own lane identity, and writes its own
  record the same way.

Either order — A then B, or B then A — leaves both records and the shared home
recoverable and intact. Neither lane cleared the other, because each retired
only its `current session lane` and treated the other as a preserved `sibling
lane`.

## Role-Aware Closeout Router (Run First)

Before writing the session record, identify the active role/mode from the current session.

Run role routing in this order:
- If the active role is actually Project Steward or Master Steward, use the steward branch.
- Otherwise, if any supervisor signal exists, use the supervisor branch.
- Otherwise, use normal CREATE-SESSION-RECORD behavior.

Do not let supervisor sessions silently fall through to generic closeout. If a supervisor signal exists, the supervisor preflight must run before the final record, unless you explicitly record why it could not run under `STATE -> Open Questions and Risks`.

Steward signals include:
- active role, greeting, or user instruction names Project Steward, Master Steward, steward, Stew, or MS
- a loaded Project Steward role prompt or Master Steward overlay
- a referenced path under `/Users/grig/.agents-private/project-steward/master-steward/`
- a referenced project-local path under `.dev/ai/roles/project-steward/`
- session context showing steward-only duties such as monologue capture, project wisdom capture, source-to-stewardship routing, or steward-of-stewards work

If the active role is Project Steward or Master Steward, or steward signals exist and no supervisor-specific active role is present, treat the session as Project Steward or Master Steward closeout:
- execute `/Users/grig/.agents/prompts/general/close-steward.md` first as an internal steward subroutine
- do not copy or summarize the full steward checklist here
- complete the subroutine's required steward capture/status updates as applicable
- return to this prompt and write the final unified session record under `.dev/ai/sessions/`
- record the steward subroutine path in frontmatter and `BACKWARD` provenance

Supervisor signals include:
- active role, greeting, or user instruction names Blocker Supervisor, blocker supervisor, supervisor, Supe, or blocker-supervisor
- a loaded blocker-supervisor prompt or a path referencing `agent-blocker-supervisor`
- blocker-engineer or unblocker paths, including `agent-blocker-supervisor-unblocker`
- blocker `MASTER-INDEX` paths or session context involving blocker master-index synchronization
- blocker lifecycle files, blocker registry operations, owner-attention queues, idle/claimed/resolved blocker state, or manual blocker lifecycle transitions
- `ms-updates` or `ms-dispatch` paths used for supervisor-to-Master-Steward blocker routing
- session context primarily focused on blockers, blocker cataloging, blocker resolution, blocker source-of-truth integrity, or no-poll compliance for blocker work

If any supervisor signal is present and the active role is not actually Project Steward or Master Steward, treat the session as Blocker Supervisor/Supe closeout:
- execute `/Users/grig/.agents/prompts/general/close-supervisor.md` first as an internal supervisor preflight
- do not copy or summarize the full supervisor checklist here
- complete the preflight's required blocker integrity/source-of-truth checks as applicable
- return to this prompt and write the final unified session record under `.dev/ai/sessions/`
- record the supervisor subroutine path in frontmatter and `BACKWARD` provenance
- record supervisor provenance fields without expanding non-supervisor records

Do not run the steward subroutine for supervisor sessions unless the active role is actually Project Steward or Master Steward.

If the active role is neither steward nor supervisor, do not run either role subroutine. Continue with normal CREATE-SESSION-RECORD behavior and keep the record compact according to the selected complexity tier.

If the active role is unclear, infer from durable signals instead of asking the owner to choose the closeout path. Use role activation text, loaded role prompts, Master Steward overlay references, steward-private paths, project-local steward role paths, blocker-supervisor prompt references, blocker-engineer paths, blocker `MASTER-INDEX` paths, blocker lifecycle files, `ms-updates`/`ms-dispatch` paths, prior handoff/session/work-order paths, and current session context. If neither steward nor supervisor signals exist after inference, proceed as a non-steward/non-supervisor continuation session and record any role uncertainty under `STATE -> Open Questions and Risks`.

Final artifact rule: the owner-facing closeout output is still one saved session record in `.dev/ai/sessions/`. Steward or supervisor subroutine updates may be referenced as supporting artifacts, but they do not replace the final session record.

## Ground-Truth Re-Scan Gate (MANDATORY before any "blocked"/"done" assertion)

This gate exists because closeouts have asserted against **inherited** state instead of **current** state: a real session called the working tree "dirty with uncommitted WO changes" when those changes had since been committed, and cited an **older** unblock artifact as the "newest already processed" while a newer one sat unread. The closeout trusted what it carried forward. Inherited state is a hint, never proof.

**Rule (P5 — no assertion without re-scan):** You may NOT write any "blocked", "done", "complete", "still blocked", "dirty tree", or "newest artifact" conclusion — in the session record, in the PROJECT-STATUS.md update, or in the chat summary — until you have run the re-scan below and stamped `ground_truth_rescanned_at:` in the record. A passive intention to "check" is insufficient; you must RUN the commands and SHOW their output. This applies to every closeout path: normal, Project Steward, Master Steward, and Blocker Supervisor.

Run this from `{project_root}` (the working directory whose `.dev/ai/` you are closing out). Use absolute paths if the working directory is ambiguous.

### Step 1 — Run the re-scan commands and capture output

```bash
# Stamp the scan time first so the record proves the scan happened.
GROUND_TRUTH_RESCANNED_AT=$(date -u +%Y-%m-%dT%H:%M:%SZ)
echo "ground_truth_rescanned_at: ${GROUND_TRUTH_RESCANNED_AT}"

# 1. TREE STATE — never trust an inherited "dirty"/"clean" claim.
#    Empty output = clean tree. Any line = genuinely uncommitted, named explicitly.
echo "--- git status --short ---"
git status --short

# 2. NEWEST UNBLOCK — never trust an inherited "newest already processed".
#    -t sorts newest-first; the TOP line is the real newest, not whatever you remember.
echo "--- newest unblock artifacts (newest first) ---"
ls -t .dev/ai/unblocks/ 2>/dev/null | head || echo "(no .dev/ai/unblocks/ in this project)"
```

For each blocker or WO you are about to characterize as blocked/done, **re-read its live `status:` field** from the authoritative file at this moment — do not carry forward a status from an earlier point in the session, an index, or a prior session record:

```bash
# 3. LIVE STATUS — re-read the authoritative file's own status field, now.
echo "--- live status of items being characterized ---"
grep -m1 -E '^(status|unresolvable_reason):' .dev/ai/blockers/<BLOCKER-ID>.md   # repeat per item
grep -m1 -E '^(status):' .dev/ai/workorders/<WO-ID>.md                          # repeat per item
```

### Step 2 — Reconcile what you were about to write against what the scan shows

Visible checklist — fill in every line from the **command output above**, not from memory:

```text
GROUND-TRUTH RE-SCAN (closeout gate):
  [ ] ground_truth_rescanned_at: <stamp from Step 1>
  [ ] git status --short output:
        <paste the actual lines, or "EMPTY — tree clean">
      -> tree characterization I will write: <clean | dirty: only the files listed above>
         (if EMPTY you MUST NOT write "dirty"; if non-empty, name ONLY those files)
  [ ] newest unblock in .dev/ai/unblocks/ (top of `ls -t`): <filename or "none">
      -> matches the artifact I was treating as "newest"? <yes | NO — corrected to the file above>
  [ ] live status re-read for each item I call blocked/done:
        <ID>: status=<value now>  (matches my assertion? yes | NO — corrected)
        ...
  [ ] No "blocked"/"done"/"dirty"/"newest" claim in this record contradicts the four lines above.
```

If any line disagrees with what you intended to assert, the **scan wins** — rewrite the assertion before continuing. A committed tree is `clean`; a newer unblock than the one you remembered is the real newest; a blocker whose live `status:` is `resolved`/`idle` is not "still blocked".

### Step 3 — Stamp it (the assertion is invalid without this)

Put the stamp in the session-record frontmatter (`ground_truth_rescanned_at:`) AND in the BACKWARD provenance log. No "blocked" or "done" assertion in this record is valid without a `ground_truth_rescanned_at:` stamp newer than the work it describes. If you genuinely could not run the scan (no shell, not a git repo), write `ground_truth_rescanned_at: UNABLE — <reason>` and record under `STATE -> Open Questions and Risks` that all blocked/done claims are inherited-unverified.

This gate is a hard precondition for the **PROJECT-STATUS.md Update** and **Final Check Before Saving** sections below.

## Routing Rule

- Routine session close, including low-context or emergency closeout, uses this prompt.
- Steward session close still uses this prompt; `/Users/grig/.agents/prompts/general/close-steward.md` is an internal subroutine, not a separate owner-facing routine closeout prompt.
- Blocker Supervisor/Supe session close still uses this prompt; `/Users/grig/.agents/prompts/general/close-supervisor.md` is an internal preflight, not a separate owner-facing routine closeout prompt.
- Explicit request for a legacy standard handoff uses `~/.agents/prompts/handoffs/HANDOFF.md` only as a compatibility surface, not as the default session-close choice.
- Delegation, orchestration transfer, or `.dev/ai/subtask-comms/` coordination uses `~/.agents/prompts/handoffs/ORCHESTRATION-HANDOFF.md`.
- Explicit request for a standalone historical audit or an older audit-only integration uses `~/.agents/prompts/creation/CREATE-AUDITABLE-RECORD.md` as a legacy audit alias.

## When to Use This Flow

Use this prompt when the user requests any of:
- `/close-session`
- `close session`
- `create session record`
- `wrap this session`
- `save the session`
- a combined audit + next-steps artifact
- `It's time to retire this agent's context. Create a session record. The next agent will takeover the role that you have performed if needed. PLEASE follow all of these instructions (READ ONLY): ~/.agents/prompts/creation/CREATE-SESSION-RECORD.md`

You may also use it at a natural session close when the user clearly wants continuity, traceability, or resumability.

Do **not** use this flow when:
- the user explicitly asks for an orchestration handoff
- the user explicitly asks for a legacy standard handoff artifact
- the user explicitly asks for standalone audit-only output
- the destination path is `.dev/ai/subtask-comms/`
- you are delegating work to another agent mid-execution
- the artifact is for multi-agent coordination rather than session close

For those cases, use `~/.agents/prompts/handoffs/ORCHESTRATION-HANDOFF.md` or the orchestrator-specific handoff flow.

## Save Target

Save the artifact to:
`.dev/ai/sessions/{timestamp}-session-{project}-{session-token}.md`

The `{session-token}` is a fork-safe per-session disambiguator generated fresh
at closeout (see Provenance and Naming). Two forked same-role sessions on the
same project can close in the same one-second `{timestamp}`, and because a fork
may inherit the parent's `agent_task_id`/session id, `{timestamp}` plus
`{project}` alone is not unique. The token must not rely solely on
`agent_task_id`/session id; it is a fresh random value, and a no-overwrite
collision guard ensures an existing `.dev/ai/sessions/` record is never
overwritten. Use this same unique path for the `session_record_path`
frontmatter and the final chat path.

Do not save session-close records to:
- `.dev/ai/audits/`
- `.dev/ai/handoffs/`

Legacy audit and handoff directories remain historical archives. New session-close records belong in `.dev/ai/sessions/`.

## Complexity Tiers

Assess complexity before writing.

### Emergency / Low Context
Use when the user mentions:
- `low context`
- `running out`
- `context limited`
- `quick`
- `emergency`
- `hitting limit`

Target:
- 20-40 lines
- preserve only execution-critical facts
- keep `BACKWARD` minimal, not absent

### Simple
Use for a single, low-ambiguity task or brief mechanical session.

Target:
- 50-80 lines
- compact `BACKWARD`

### Standard
Use for multi-step sessions with some judgment or synthesis.

Target:
- 100-180 lines
- standard `BACKWARD`

### Complex
Use for integration, design judgment, interdependent steps, or blocker-heavy work.

Target:
- 180-300 lines
- detailed `BACKWARD`
- when the 35-40% reduction target matters, steer toward the validated 217-235 line / 4.8-5.2k token band
- treat the lower half of the tier as the default for validated complex cases; 300 lines is a hard ceiling, not a normal target

## Provenance and Naming

Every session record must include `agent_task_id`.

Every session record must also preserve closeout provenance:
- active `role`
- active `mode`
- source closeout prompt path: `/Users/grig/.agents/prompts/creation/CREATE-SESSION-RECORD.md`
- steward subroutine path used, or `None`
- supervisor subroutine path used, or `None`
- supervisor mode and blocker provenance when the supervisor branch runs
- prior handoff, work-order, session, or related artifact paths when they exist

Rules:
- If you received an `agent_task_id` from a prior handoff, work order, or session record, reuse it.
- If no `agent_task_id` exists, generate one with:

```bash
AGENT_TASK_ID=$(~/.agents/scripts/get-agent-task-id.sh session-record)
```

Include `agent_task_id` in:
- frontmatter
- footer
- next-session prompt

Create the output path with a fork-safe per-session token and a no-overwrite
collision guard. The token must not rely solely on `agent_task_id`/session id,
because a fork may inherit those; generate a fresh random token at closeout,
portable across macOS and Linux shells:

```bash
mkdir -p .dev/ai/sessions/
TIMESTAMP=$(~/.agents/scripts/get-filename-prefix.sh)

# Fresh per-session token. openssl is portable across macOS/Linux; the
# ${$}${RANDOM} fallback keeps it working when openssl is unavailable.
gen_session_token() {
  openssl rand -hex 3 2>/dev/null || printf '%s' "${$}${RANDOM}"
}
SESSION_TOKEN="$(gen_session_token)"

# Optional: prefix a short form of an available agent_task_id, but the fresh
# random SESSION_TOKEN is what guarantees fork-safety even when agent_task_id
# was inherited from the parent lane.
SHORT_TASK_ID="$(printf '%s' "${AGENT_TASK_ID:-}" | tr -cd 'A-Za-z0-9' | tail -c 4)"
[ -n "$SHORT_TASK_ID" ] && SESSION_TOKEN="${SHORT_TASK_ID}-${SESSION_TOKEN}"

FILE=".dev/ai/sessions/${TIMESTAMP}-session-[project-id]-${SESSION_TOKEN}.md"

# No-overwrite collision guard: never overwrite an existing session record. If a
# sibling fork wrote first in the same second, regenerate the token and retry.
while [ -e "$FILE" ]; do
  SESSION_TOKEN="$(gen_session_token)"
  FILE=".dev/ai/sessions/${TIMESTAMP}-session-[project-id]-${SESSION_TOKEN}.md"
done
```

Use the saved file path exactly in the record, in the `session_record_path`
frontmatter, and in the final chat response. Because the token is generated
fresh at closeout and guarded against collision, two forked same-role sessions
on the same project closing in the same second resolve to different files and
neither overwrites the other.

## Required Frontmatter

```yaml
---
agent_task_id: [AGENT_TASK_ID]
created: [YYYY-MM-DD-HH-MM-SSZ]
project: [project-name]
role: [active role or continuation agent]
mode: [active mode or session-close]
type: session-record
complexity: [emergency|simple|standard|complex]
ground_truth_rescanned_at: [YYYY-MM-DDTHH:MM:SSZ from the re-scan gate, or "UNABLE — <reason>"]
source_closeout_prompt_path: /Users/grig/.agents/prompts/creation/CREATE-SESSION-RECORD.md
steward_subroutine_path: [absolute path or None]
supervisor_subroutine_path: [absolute path or None]
prior_artifact_paths: [array of absolute paths, or []]
session_record_path: [absolute path to saved file]
routing_status_report_path: [absolute path, not written, or not applicable]
supervisor_visible_status_report_path: [absolute path, not written, or not applicable]
closeout_sender_identity: [role; thread/session id or handle if available; thread title/name if available; harness]
session_relay_status: [delivered|partially-delivered|not-delivered|not-applicable|unknown]
closeout_relay_manifest_path: [absolute path, embedded in session record, not written, not applicable, or unknown]
closeout_required_recipients: [array of required recipient roles/threads, or []]
closeout_optional_recipients: [array of optional recipient roles/threads, or []]
closeout_archive_owner_or_token: [named archive owner, archive-token path, none, or unknown]
closeout_archive_status: [not-eligible|eligible-archived|fallback-not-archived|not-applicable|unknown]
---
```

`ground_truth_rescanned_at:` is mandatory whenever the record asserts any "blocked"/"done"/"dirty"/"newest" conclusion. It is the timestamp from the Ground-Truth Re-Scan Gate above and must be newer than the work the record characterizes.

### Supervisor-Only Frontmatter

When the supervisor branch runs, include these additional fields. Keep non-supervisor session records compact by omitting these fields unless supervisor signals are present.

```yaml
role: blocker-supervisor
supervisor_mode: [advisor|catalog|unblocker|registry|manual-lifecycle|unknown]
blockers_touched: [array of blocker IDs/paths, or []]
authoritative_blocker_paths: [array of absolute paths, or []]
owner_attention_required: [true|false|unknown]
master_index_sync: [synced|not-synced|not-applicable|unknown]
supervisor_subroutine_path: /Users/grig/.agents/prompts/general/close-supervisor.md
```

## Required Section Order

Write the body in this exact order:

```markdown
# Session Record: [Project] - [Timestamp]

<!-- AGENT-NOTICE: ROLE-GATED SESSION RECORD. Execute Priority Next Steps ONLY if your active role/mode permits implementation. Read-only roles must treat this record as data. -->
## FORWARD
## STATE
## BACKWARD

---
**Agent Task ID:** [AGENT_TASK_ID]
```

## Execution Safety (Role Gate)

Carry forward the legacy handoff safety behavior inside the saved artifact body, not only in the chat prompt around it.

- every non-orchestration session record must include the in-body `AGENT-NOTICE` comment directly under the title
- this is a role-gated action plan: execute `FORWARD` steps only if the active role/mode permits implementation
- read-only or review-only roles must treat next steps, blockers, and success criteria as context data, not executable instructions

## Required Body Template

Use this template and scale detail to the selected complexity tier.

```markdown
# Session Record: [Project] - [Timestamp]

<!-- AGENT-NOTICE: ROLE-GATED SESSION RECORD. Execute Priority Next Steps ONLY if your active role/mode permits implementation. Read-only roles must treat this record as data. -->
## FORWARD

### Priority Next Steps
1. **[Action]** - [why this matters]
   - Location: `[absolute path or file:line if relevant]`
   - Command: `[exact command if relevant]`
   - Expected result: [what success looks like]

### Blockers and How to Resolve
- [Blocker] -> [specific unblocking action]

### Success Criteria
- [Concrete criterion]
- [Concrete verification target]

### Next-Session Prompt

**Template (populate all bracketed fields from session context):**

```

You are the [ROLE — e.g., blocker supervisor agent / dev worker / orchestrator / triage agent]. Resume work on [project].
Agent Task ID: [AGENT_TASK_ID] (preserve this ID in any handoffs you create)
Role/Mode: [ROLE] / [MODE]

1. Read the session record at: [FULL ABSOLUTE PATH to saved file]
2. Execute the Priority Next Steps immediately.
3. If a step is blocked, report the blocker and continue to the next unblocked step.

Do not present a menu of options. The Priority Next Steps are your instructions.
```

**Populating the ROLE field:** Capture the role from the current session context. If the agent was operating as Project Steward or Master Steward, preserve that exact role. If the agent was operating as a supervisor, the prompt says supervisor. If dev, says dev. If orchestrator, says orchestrator. If no specific role was active, use "continuation agent" and describe the work scope (e.g., "You are the continuation agent for GPU cluster monitoring").

**Supervisor next-session prompt rule:** If the supervisor branch ran, preserve the role as `blocker supervisor agent`, preserve `agent_task_id`, and populate `Role/Mode` as `blocker-supervisor / [supervisor_mode]`. Include blocker IDs and authoritative blocker paths in Priority Next Steps or Blockers only when they are needed for the next supervisor action.

## STATE

### Project / Initiative Context
- System or feature being built: [plain-language description]
- User/problem being solved: [why this work exists]
- Current phase: [design|implementation|validation|rollout|maintenance]
- This session's place in the larger effort: [how this session moved the project forward]

### Current Snapshot
- Scope: [what this session covered]
- Current state: [where work now stands]

### Work Status
- Outstanding: [WO IDs or tasks with exact next step]
- Completed this session: [completed work]

### Key Files and Artifacts
- Created: `[absolute path]` - [purpose]
- Modified: `[absolute path]` - [what changed]
- Referenced: `[absolute path]` - [why it matters]

### Key Decisions and Rationale
- [Decision] -> [why]

### Open Questions and Risks
- [Question or risk]

### Status Routing and Relay
- Routing status report: `[absolute path, not written, or not applicable]`
- Supervisor-visible status report: `[absolute path, not written, or not applicable]`
- Harness identified: `[Codex|Claude|Gemini/Antigravity|unknown]`
- Sender identity: `[role; thread/session id or handle if available; thread title/name if available; harness]`
- Direct relays attempted: `[target -> delivered with receipt | not delivered | not applicable]`
- Durable fallback packets: `[absolute path or None]`
- Closeout relay manifest: `[absolute path, embedded in session record, not written, or not applicable]`
- Required relay recipients: `[required recipients or []]`
- Optional relay recipients: `[optional recipients or []]`
- Processed-ack requirements: `[recipient -> processed_ack path or durable ack id]`
- Archive owner/archive-token: `[named owner, archive-token path, none, or unknown]`
- Archive rule: `receivers must not archive this sending session until every required recipient in the manifest has written a processed ack`

## BACKWARD

### Starting Point and Scope
- Initial request: [what initiated the session]
- Startup inputs:
  - `[full absolute path]` - [why it was loaded]
- Working directory: `[absolute path]`
- Project rules source: `[full absolute path to AGENTS.md or equivalent]`

### Actions Taken
- [chronological action]
- [chronological action]

### Results and Evidence
- [result] -> [artifact, file path, command, or verification evidence]

### Errors, Blockers, and Mitigations
- [issue] -> [response or mitigation]

### Provenance Log
- Agent task id: `[AGENT_TASK_ID]`
- Ground truth re-scanned at: `[YYYY-MM-DDTHH:MM:SSZ from the re-scan gate, or UNABLE — reason]`
- Source closeout prompt: `/Users/grig/.agents/prompts/creation/CREATE-SESSION-RECORD.md`
- Steward subroutine: `[absolute path to /Users/grig/.agents/prompts/general/close-steward.md if used, otherwise None]`
- Role/mode: `[role] / [mode]`
- Prior artifact chain: `[prior handoff/session record/work order path if applicable]`
- Commands: `[important command or script]`
- Tracking: `[track-project.sh call or status note]`
- Related artifact chain: `[prior handoff/session record/work order path if applicable]`
- Routing status prompt: `/Users/grig/.agents/prompts/triage/agent-status-update-for-routing.md`
- Relay protocol: `/Users/grig/.agents/docs/protocols/universal-harness-relay-protocol.md`
- Session relay status: `[delivered|partially-delivered|not-delivered|not-applicable|unknown]`

---
**Agent Task ID:** [AGENT_TASK_ID]
```

## Section Rules

### `FORWARD`
- always comes first
- must be specific, prioritized, and executable
- remains role-gated: action steps are executable only for roles/modes allowed to implement
- include blockers even if there is only one
- **any blocker listed here, and any "complete"/"done" claim, must survive the Ground-Truth Re-Scan Gate** — a blocker whose live `status:` re-read shows `resolved`/`idle` is not a blocker; do not carry one forward from earlier in the session
- include success criteria whenever unfinished work remains
- if work is complete, say so directly and keep only any real follow-on or monitoring item
- do not write filler such as `continue from here`

**Priority Next Steps requirements — each step MUST have:**
- **Action**: what to do (verb-first, unambiguous)
- **Location**: absolute file path, URL, or service endpoint
- **Expected outcome**: what success looks like (measurable or verifiable)
- Commands must be exact and runnable, not vague (e.g., `pytest tools/pse/tests/ -v` not "run the tests")
- If a step requires an owner decision before execution, present it as a **Blocker** ("Owner must decide X before Y can proceed"), not as a menu option for the agent

**Anti-patterns (do NOT do these):**
- Do NOT present a list of options for the user to choose from. The Priority Next Steps are INSTRUCTIONS, not suggestions.
- Do NOT write "consider doing X or Y" — pick the right action or flag it as a blocker requiring owner input.
- Do NOT use vague language like "continue work on...", "look into...", "explore options for..." — state the exact action.

### `STATE`
- this is the shared current-state snapshot for both continuation and audit review
- include enough project / initiative context that a future agent reading only a series of session records can tell what the system is, what problem it solves, and what phase the work is in
- cite exact files with absolute paths
- include IDs for work orders, proposals, findings, or reports when relevant
- list only the files and artifacts that matter for continuation or review
- if a subsection is empty, write `None`

### `BACKWARD`
- startup provenance with full absolute paths is mandatory
- preserve enough chronology to explain how the current state was reached
- record commands, scripts, parameter values, or verification steps that materially affected the outcome
- do not restate every trivial action
- for emergency mode, compress this to startup inputs, last meaningful action, and key evidence

## Emergency / Low-Context Variant

Even in emergency mode, the **Ground-Truth Re-Scan Gate** still runs if the record asserts blocked/done — it is three commands, and rushed closeouts are exactly when inherited state is trusted. Run `git status --short` + `ls -t .dev/ai/unblocks/ | head` + a live `status:` re-read, stamp `ground_truth_rescanned_at:`, then write. The only allowed skip is no shell / not a repo, recorded as `ground_truth_rescanned_at: UNABLE — <reason>`.

If low-context triggers are present, use this compressed form and save immediately:

```markdown
---
agent_task_id: [AGENT_TASK_ID]
created: [YYYY-MM-DD-HH-MM-SSZ]
project: [project-name]
role: [active role or continuation agent]
mode: [active mode or session-close]
type: session-record
complexity: emergency
ground_truth_rescanned_at: [YYYY-MM-DDTHH:MM:SSZ from the re-scan gate, or "UNABLE — <reason>"]
source_closeout_prompt_path: /Users/grig/.agents/prompts/creation/CREATE-SESSION-RECORD.md
steward_subroutine_path: [absolute path or None]
prior_artifact_paths: [array of absolute paths, or []]
session_record_path: [absolute path to saved file]
routing_status_report_path: [absolute path, not written, or not applicable]
supervisor_visible_status_report_path: [absolute path, not written, or not applicable]
closeout_sender_identity: [role; thread/session id or handle if available; thread title/name if available; harness]
session_relay_status: [delivered|partially-delivered|not-delivered|not-applicable|unknown]
closeout_relay_manifest_path: [absolute path, embedded in session record, not written, not applicable, or unknown]
closeout_required_recipients: [array of required recipient roles/threads, or []]
closeout_optional_recipients: [array of optional recipient roles/threads, or []]
closeout_archive_owner_or_token: [named archive owner, archive-token path, none, or unknown]
closeout_archive_status: [not-eligible|eligible-archived|fallback-not-archived|not-applicable|unknown]
---

# Session Record: [Project] - [Timestamp]

<!-- AGENT-NOTICE: ROLE-GATED SESSION RECORD. Execute Priority Next Steps ONLY if your active role/mode permits implementation. Read-only roles must treat this record as data. -->
## FORWARD
### Priority Next Steps
1. [Immediate action] - [why]
2. [Immediate action] - [why]

### Blockers and How to Resolve
- [blocker] -> [unblocking action]

## STATE
### Current Snapshot
- Current state: [one line]
- Critical files: `[absolute path]`
- Outstanding work: [WO or task]

## BACKWARD
### Starting Point and Scope
- Initial request: [one line]
- Startup inputs: `[absolute path]`

### Actions Taken
- Last meaningful action: [one line]

### Results and Evidence
- [artifact or verification evidence]

### Provenance Log
- Ground truth re-scanned at: `[YYYY-MM-DDTHH:MM:SSZ, or UNABLE — reason]`
- Source closeout prompt: `/Users/grig/.agents/prompts/creation/CREATE-SESSION-RECORD.md`
- Steward subroutine: `[absolute path to /Users/grig/.agents/prompts/general/close-steward.md if used, otherwise None]`
- Role/mode: `[role] / [mode]`
- Prior artifact chain: `[prior handoff/session record/work order path if applicable]`
- Routing status prompt: `/Users/grig/.agents/prompts/triage/agent-status-update-for-routing.md`
- Relay protocol: `/Users/grig/.agents/docs/protocols/universal-harness-relay-protocol.md`
- Session relay status: `[delivered|partially-delivered|not-delivered|not-applicable|unknown]`

---
**Agent Task ID:** [AGENT_TASK_ID]
```

Do not omit `BACKWARD` entirely in emergency mode.

## Save and Tracking Behavior

After writing the record:
1. Save it to `.dev/ai/sessions/`.
2. Optionally track creation with:

```bash
~/.agents/scripts/track-project.sh "[project-name]" "Session record created" \
  "Session record: [brief summary]" "[agent-name]"
```

If the user asked for a visible close-out, give a short summary in chat that includes:
- current status
- next logical step
- exact absolute path to the saved session record

## PROJECT-STATUS.md Update (MANDATORY at session close)

As part of parent/session close, update `{project_root}/.dev/ai/PROJECT-STATUS.md`
to reflect the final state. This gives the supervisor a one-line status check.

**Writer boundary:** Routine closeout from the parent/session owner must route
`PROJECT-STATUS.md` writes through the WOQ shared-status safe writer when the
target is `/Users/grig/.agents/.dev/ai/PROJECT-STATUS.md`:

```bash
/Users/grig/.agents/.venv/bin/python3 -m tools.woq.cli shared-status write ...
```

Before writing, reread
`/Users/grig/.agents/docs/protocols/woq-role-lifecycle.md`, read the live target,
capture its current SHA-256 or header SHA-256 with `shared-status hash`, and use
that hash in the safe-writer call. Parallel workers, bounded QA workers, and
read-only workers must not write PROJECT-STATUS.md; they write their exact result
artifact with proposed status text and any recommended shared-surface changes for
parent assimilation.

**Active-worker preservation:** If a closeout occurs while a parent
orchestration has active native workers or an open agents ledger, reread
`/Users/grig/.agents/.dev/ai/orchestration/open-codex-agents.md` immediately
before writing PROJECT-STATUS.md, capture its current SHA-256, and pass
`--parent-closeout --base-active-ledger-sha256 <sha>` to the safe writer. Do not
erase active worker state, expected result artifact paths, or unresolved
dispatch-wave notes from inherited or stale context.

**WOQ managed-block preservation:** The safe writer preserves existing WOQ
managed blocks byte-for-byte unless an owned managed block is explicitly named:
`<!-- WOQ:BEGIN managed-block id="project-status" ... -->` through
`<!-- WOQ:END managed-block id="project-status" -->`. Routine session closeout
may update only the legacy narrative/header status outside that block. The
managed block may be replaced only by the approved WOQ renderer path; if you
cannot complete the safe-writer call, do not write `PROJECT-STATUS.md`; put
proposed status text in the session record for parent assimilation.

**Precondition:** `status: blocked` here is a "blocked" assertion and is invalid
without the Ground-Truth Re-Scan Gate having run. Before writing `status:
blocked`, confirm the gate's `git status --short` and live blocker/WO `status:`
re-read actually show the work is still blocked **now** — do not carry forward a
"blocked" from earlier in the session. If the re-scan shows the gating upstream is
`resolved`/`idle` or the gating tree is now committed, write `status: working`
with the genuinely-remaining item, not `status: blocked`. The `## Blocked Items`
reason must match the live `status:`/`unresolvable_reason:` you re-read, not an
inherited reason.

If work remains unblocked:
```
status: working
updated: <ISO timestamp>
agent: <role from this session>

## Active Work
- <remaining WO or task>
- <next planned item>
```

If work is blocked:
```
status: blocked
updated: <ISO timestamp>
agent: <role from this session>

## Blocked Items (priority order)
1. <what is blocked> — <plain-language reason>

## Completed This Session
- <what was done before hitting blocks>
```

Use the safe writer in `replace` mode for a full closeout replacement, or
`addendum` mode for stale-but-non-destructive notes. Line 1 of replacement
content must be `status: working` or `status: blocked`. Never delete this file.

## Status Routing and Self-Relay Before Final Retirement (MANDATORY)

Before the agent is closed for good, it must route and relay its own closeout
results. The owner should not have to copy/paste between sessions when a
supported relay path exists.

1. Read `/Users/grig/.agents/prompts/triage/agent-status-update-for-routing.md`.
2. Produce the routing status update from the final session state.
3. Write the append-only project-local and supervisor-visible status reports
   required by that prompt when file writes are available.
4. Read `/Users/grig/.agents/docs/protocols/universal-harness-relay-protocol.md`.
5. Identify the current harness as `Codex`, `Claude`, `Gemini/Antigravity`, or
   `unknown`.
6. Identify sender identity before building recipients: current role, current
   thread/session id or handle when available, current thread title/name when
   available, and harness. Record it in frontmatter and in `STATE -> Status
   Routing and Relay`.
7. Identify the agents/sessions that need the closeout result: owner-visible
   thread, Blocker Supervisor, Master Steward, active Orchestrator/project lane,
   parent thread, worker target, or other explicitly named return recipient.
8. Apply the self-recipient filter before required/optional classification and
   before closeout relay manifest creation: remove the sender's own current
   session from required and optional recipients. If no thread id or handle is
   available, role-name matching prevents obvious self-targets: a closing
   Blocker Supervisor does not direct-relay to Blocker Supervisor, a closing
   Master Steward does not direct-relay to Master Steward, and a closing
   Project Steward does not direct-relay to the same current Project Steward
   session. Same-role relay is allowed only with proof of a distinct target
   session/thread, such as a named replacement or a separate role instance with
   a different thread id or handle.
9. Classify external closeout relay recipients as required or optional. Required
   recipients are the agents/sessions that must process the closeout before the
   sending Codex session can be archived. The sender's own current session must
   not be a required recipient and must not be required to write a
   `processed_ack`.
10. If the self-recipient filter leaves no external recipients, record
   `not-applicable - no external recipient after self-recipient filter` or
   equivalent and do not fake a direct send. If the filter leaves only one
   external recipient, do not create a multi-recipient archive manifest unless
   archive coordination is otherwise required.
11. For multi-recipient closeout relay, create or name a closeout relay manifest
   that records required recipients, optional recipients, per-recipient
   `processed_ack` paths, and either a named archive owner or archive-token
   path. Record that manifest in frontmatter and in `STATE -> Status Routing
   and Relay`.
12. Relay yourself: send what you need to send to the agents you need to send it
   to in the sessions available in the current harness. In Codex, use exposed
   receipt-producing Codex relay routes such as same-harness thread send tools
   when available. In Claude or Gemini/Antigravity, use only exposed
   receipt-producing native thread/agent/team message routes.
13. Every successful direct relay must include a return-capable `reply_to`
   envelope, the closeout relay manifest path when a manifest exists, and fresh
   receipt evidence in the session record.
14. Tell every closeout receiver that it may write its processed ack only after
   it has copied, captured, or otherwise assimilated what it needs from the
   session record, routing status update, and referenced artifacts.
15. Tell every closeout receiver that it must not archive the sending session
   until all required recipients in the manifest have written processed acks;
   only the named archive owner or archive-token holder may call an exposed
   receipt-producing archive route such as Codex `set_thread_archived`.
16. If direct relay is unavailable, unsupported, unsafe, lacks a target, or
   cannot produce fresh receipt evidence, write or stage the durable relay
   packet/status report and say explicitly that it was not delivered. Do not
   ask the owner to copy/paste as the default fallback.
17. Do not poll, watch, tail logs, or wait-loop for relay replies or processed
    acks. Use native reply/completion notices, bounded heartbeat recovery when
    already required, or the named durable ack/result path.

## Final Check Before Saving

Confirm all of the following:
- file path is under `.dev/ai/sessions/`
- **Ground-Truth Re-Scan Gate ran:** `git status --short`, `ls -t .dev/ai/unblocks/ | head`, and a live `status:` re-read were actually executed with output shown, and `ground_truth_rescanned_at:` is stamped in frontmatter + BACKWARD provenance (or `UNABLE — <reason>` with the risk recorded)
- **No inherited-state contradiction:** no "blocked"/"done"/"dirty"/"newest" claim in this record (or in the PROJECT-STATUS.md update) contradicts the re-scan output — a clean tree is never called "dirty", and the cited "newest" unblock is the top of `ls -t`
- `FORWARD`, `STATE`, and `BACKWARD` all exist
- next actions, blockers, and success criteria are explicit when work remains
- the in-body `AGENT-NOTICE` role-gated execution notice is present
- startup provenance includes full absolute paths
- `agent_task_id` is present
- role/mode and source closeout prompt path are present
- steward sessions ran `/Users/grig/.agents/prompts/general/close-steward.md` first and recorded that path, or no steward signal was present
- prior handoff, work-order, session, or related artifact paths are preserved when they exist
- for complex records where the reduction target matters, the draft is intentionally shaped toward 217-235 lines / 4.8-5.2k tokens
- orchestration handoff content was not mixed into this artifact
- the Next-Session Prompt includes a concrete ROLE (not generic)
- every Priority Next Step has action + location + expected outcome
- **Continuation quality gate:** Could a fresh agent with ZERO context from this conversation read only the Next-Session Prompt + FORWARD section and start executing immediately? If not, add the missing context. The test is: paste the Next-Session Prompt into a blank conversation — does the agent know what it is, what to do first, and where to do it?
- PROJECT-STATUS.md at `{project_root}/.dev/ai/PROJECT-STATUS.md` has been updated with final state by the parent/session owner using the WOQ safe writer when it is the guarded agents-system path, or this was a worker/QA closeout and the proposed PROJECT-STATUS text was written only to the result artifact for parent assimilation
- `/Users/grig/.agents/prompts/triage/agent-status-update-for-routing.md` was read and the routing status update was produced
- append-only routing status reports were written when file writes were available, or exact write limitations were recorded
- `/Users/grig/.agents/docs/protocols/universal-harness-relay-protocol.md` was read before relay selection
- current harness was identified as Codex, Claude, Gemini/Antigravity, or unknown
- sender identity was recorded before recipient selection: current role, current thread/session id or handle when available, current thread title/name when available, and harness
- needed relay targets were identified, the sender's own current session was removed from required/optional recipients, obvious same-role self-targets were marked not applicable unless a distinct target session/thread was proven, and direct relay was attempted only through exposed receipt-producing harness routes
- every successful direct relay records receipt evidence and a `reply_to` envelope; every unsupported/unverified relay records the durable fallback path and explicit not-delivered wording
- multi-recipient closeout relays record external required recipients, external optional recipients, processed-ack paths, and archive owner/archive-token in a closeout relay manifest; if no external recipients remain after self-recipient filtering, relay is recorded as not applicable and no fake direct send is created
- relay packets tell receivers not to archive the sending Codex session until every required processed ack exists; only the named archive owner or archive-token holder may use an exposed receipt-producing archive route, otherwise the fallback must say the session was not archived
