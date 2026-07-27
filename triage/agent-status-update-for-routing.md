# Agent Status Update for Routing

Use this prompt when the owner asks any running agent for a status update that
can be relayed to the owner, the Blocker Supervisor, and the Master Steward.

You are the reporting agent. Your job is to produce a compact, actionable,
source-labeled status update from what you actually know now. This is a status
report, not permission to continue the work.

## Active Session Adoption

Prompt changes are file-based. Already-running agents do not automatically know
about this prompt or the supervisor status inbox unless they reread the relevant
file or the owner pastes instructions that point to it.

When the owner asks you to use this prompt, read this file before producing the
status update. If you are the Blocker Supervisor or Master Steward and the
owner mentions newly synced agent status reports, reread your current role
prompt/overlay sections that mention
`/Users/grig/.agents/agents/blocker-engineer/agent-status-inbox/` before
answering.

New sessions started after the prompt update should load the current files
during normal startup. Existing sessions need explicit reload text from the
owner or a bounded reread of the named prompt path.

## Default Behavior

This is a single paste-anywhere prompt. It requires no extra flags or mode
settings from the owner.

When the owner asks you to use this prompt:

1. Read this file.
2. Produce the status update.
3. Print the status update in the current thread.
4. Write the append-only project-local status report when `project_root` is
   known and file writes are available.
5. Write the append-only supervisor-visible status report when file writes are
   available.

Do not dispatch agents, update work orders, update blockers, modify indexes, or
mutate shared state beyond the append-only status report writes described
below.

Self-recipient guard: before treating `Relay to Blocker Supervisor` or
`Relay to Master Steward` as direct relay targets, identify the reporting
agent's current role/session, thread id or handle when available, thread
title/name when available, and harness. If the reporting agent is the same
current role/session as the apparent target, the section is not a direct relay
target. Write `not applicable - sender is this role/session` or equivalent in
that relay section and capture the information locally in the status report.
Same-role direct relay is allowed only with proof of a distinct target
session/thread, such as a named replacement or a different thread id/handle.

If file writes are unavailable in the current harness, still return the status
update in the thread and set `Sync writes` to `not written` with the exact
limitation. Do not ask the owner for another flag.

## File Sync Writes

Make the status immediately available through file-based sync. Do not edit
shared status files directly.

Write append-only files only:

1. Primary project-local status report, when `project_root` is known:
   `{PROJECT_ROOT}/.dev/ai/subtask-comms/{UTC_TIMESTAMP}-agent-status-update-for-routing.md`
2. Supervisor-visible copy or pointer:
   `/Users/grig/.agents/agents/blocker-engineer/agent-status-inbox/{UTC_TIMESTAMP}-{PROJECT_SLUG}-{ROLE_SLUG}-status.md`

If `project_root` is unknown, do not invent a project-local path. Write only
the supervisor-visible file, use `unknown-project` in the filename/front matter,
and call out the missing project root in the report.

Filename rules:

- Get the timestamp from a deterministic command such as
  `date -u +%Y-%m-%d-%H-%M-%SZ`.
- Slugify project, workstream, and role names to lowercase ASCII with
  non-alphanumeric characters changed to `-`.
- Never overwrite an existing file. If the computed filename exists, add a
  short unique suffix.

Supervisor-visible files MUST include YAML front matter followed by the full
status update or a pointer plus the `Relay to Blocker Supervisor` section:

```yaml
---
schema: agent-status-update-for-routing.v1
created_at: "<ISO 8601 UTC timestamp>"
project: "<project name or unknown>"
project_root: "<absolute path or unknown>"
workstream: "<name or unknown>"
reporting_agent_role: "<role or unknown>"
state: "<active|waiting|blocked|ready-for-handoff|complete|unknown>"
supervisor_actionable: true
master_steward_actionable: false
primary_status_report_path: "<absolute path or same-as-this-file>"
source_basis: "<context only, named files, completion notices, etc.>"
---
```

Set `supervisor_actionable: false` only when the report has no blocker, gate,
stale-state, access, credential, owner-action, external dependency, or unblock
routing content. Set `master_steward_actionable: true` when the report has
portfolio, priority, cross-project, ownership, continuity, or dispatch-locality
content.

Do not write directly to:

- `/Users/grig/.agents/agents/blocker-engineer/SUPERVISOR-STATUS.md`
- `/Users/grig/.agents/agents/blocker-engineer/SUPERVISOR-RUNSTATE.md`
- any project `PROJECT-STATUS.md`
- any work order index
- any blocker file or blocker index

Those surfaces are updated only by their owning roles after they ingest the
report.

## Allowed Context

Use only:

- the current conversation/thread context;
- your current assignment, work order, dispatch packet, or role prompt if it is
  already in context or explicitly named;
- exact state files, ledgers, blocker files, result artifacts, session records,
  or status docs already named in context or supplied with this prompt;
- files you created or were explicitly assigned to create;
- completion notices that are already visible in the current context.

Do not:

- poll, watch, tail, or repeatedly check another agent;
- scan broad result directories;
- perform fresh project discovery unless exact paths were supplied and one
  bounded read is necessary for an accurate status;
- infer completion from silence, stale logs, file visibility, or "should be
  done";
- claim another role has received this update unless you have direct receipt
  evidence;
- expose secrets, credentials, private raw source text, or unnecessary personal
  information.

If state is uncertain, say `unknown` and name the exact missing or stale source.

## Report Principles

- Use absolute paths for every referenced local artifact.
- Distinguish facts, inferences, and unknowns.
- Prefer plain-language status over cryptic ID-only summaries.
- State the freshness and basis of the update.
- Separate current-agent work from work that belongs to the Orchestrator,
  Blocker Supervisor, Master Steward, or owner.
- If there is no material change, say so directly and provide the last known
  state plus the source basis.
- If you are a worker, include the expected result artifact path and whether it
  has been written.
- If a blocker exists without durable blocker state, call that out as a
  pipeline defect rather than burying it.

## Output Format

Use this exact structure.

```text
# Agent Status Update

[WS: <workstream-id-or-intake-triage> | state: <active|waiting|blocked|ready-for-handoff|complete|unknown>]

Status freshness:
- As of: <local date/time if known, otherwise "not known">
- Source basis: <current context, named files read, completion notices, or "context only">
- Confidence: <high|medium|low> because <one concise reason>
- Stale or unknown sources: <none known, or exact paths/sources>

Identity:
- Reporting agent/role: <role or unknown>
- Harness/thread/session: <Codex, Claude, browser, native worker, or unknown>
- Project: <name or unknown>
- Project root: </absolute/path or unknown>
- Workstream: <name or unknown>
- Current assignment / WO: <id/title or unknown>
- Expected result artifact: </absolute/path, none, or unknown>

Current state:
- State: <one sentence>
- What changed since the last update: <bullets or "No material change known">
- What is still in progress: <bullets or "None known">
- What is complete: <bullets or "None known">
- Evidence / artifacts: <absolute paths, commands/results already known, or "none">

Native/background workers:
- <worker/session id or label>: <assignment>; status <running|completed-unassimilated|blocked|unknown>; expected artifact <absolute path or unknown>; last direct evidence <context/file/notice or unknown>
- If no workers are known: None known.

Blockers and gates:
- Owner-action gate: <decision/input/approval needed, or none known>
- Blocker Supervisor-actionable gate: <credential/access/external/service/time/tool/blocker issue, or none known>
- Master Steward-actionable signal: <priority/cross-project/ownership/continuity/routing issue, or none known>
- External/time/service gate: <gate, responsible party/system, and unblock condition, or none known>
- Durable blocker state: <path/status if present, "missing", or "not applicable">

Next safe actions:
- Current reporting agent should: <continue/stop/handoff/wait only if mechanism exists>
- Orchestrator or project lane should: <action or none known>
- Blocker Supervisor should: <action or none known>
- Master Steward should: <action or none known>
- Owner needs to: <action or none known>

Relay to owner:
<Plain-language update the owner can act on without opening another file.>

Relay to Blocker Supervisor:
<Only blocker, gate, access, credential, external dependency, stale-state, or unblock-routing facts. Include exact paths and unblock conditions. If none, say "No Supervisor-actionable blocker known." If you are the current Blocker Supervisor session, say "not applicable - sender is this role/session" unless you can prove a distinct Blocker Supervisor target session/thread.>

Relay to Master Steward:
<Only portfolio, project priority, cross-project dependency, ownership, continuity, dispatch-locality, or strategic-routing facts. Include exact paths and decision points. If none, say "No Master-Steward-actionable signal known." If you are the current Master Steward session, say "not applicable - sender is this role/session" unless you can prove a distinct Master Steward target session/thread.>

References:
- </absolute/path>: <why it matters>
- If no references are available: None.

Sync writes:
- Primary status report: </absolute/path, not written, or not applicable>
- Supervisor-visible report: </absolute/path, not written, or not applicable>
- Sync limitations: <none, or exact reason a write was not possible>
```

## Routing Guidance

Use `Relay to Blocker Supervisor` for:

- blockers the current agent cannot resolve;
- missing credentials, access, 2FA, CAPTCHAs, payment, legal, policy, hardware,
  service dashboard, or external-team gates;
- stale or contradictory blocker/index/project status;
- missing durable blocker state for a real blocker;
- paste-ready handoff text or exact owner-action wording that would unblock
  work.

Do not use `Relay to Blocker Supervisor` as a direct relay target when the
reporting agent is the current Blocker Supervisor session. Mark it
`not applicable - sender is this role/session` unless a distinct Supervisor
target session/thread is proven.

Use `Relay to Master Steward` for:

- changes to project priority, active/inactive status, ownership, or strategic
  direction;
- cross-project dependencies or conflicts;
- decisions that affect which project should receive work next;
- evidence that work belongs in a different project, workstream, or lane;
- continuity facts that future agents should not have to rediscover.

Do not use `Relay to Master Steward` as a direct relay target when the
reporting agent is the current Master Steward session. Mark it
`not applicable - sender is this role/session` unless a distinct Master Steward
target session/thread is proven.

Use `Relay to owner` for:

- a short summary of what is happening;
- what needs the owner's attention, if anything;
- exact paths only when the owner needs them to act.

## Hard Stops

If this prompt conflicts with a more specific owner instruction in the same
message, follow the owner instruction and report the conflict.

If you cannot determine the project or assignment, still output the template
with `unknown` fields. Do not ask the owner to restate context before giving the
best status you can.

If continuing the underlying work would be useful, do not continue unless the
owner explicitly asked for continuation. This prompt is for status extraction
and routing.
