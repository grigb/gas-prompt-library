# Blocker Supervisor Reference: Startup And Work Pass

Read this after the startup reads named in `SKILL.md`, and before each `work`, `next`, `brief`, `status`, `gates`, `relay`, or check-in pass whose rules are not in your context. `SKILL.md` owns the role, the scope boundary, the two defaults, and gate validity; this file holds the procedures they call for. Do not grind these procedures inline: a scan that is more than one bounded read is dispatched per Default 2.

## Startup Steps After The Reads

These continue steps 1 and 2 under "Startup" in `SKILL.md`.

2a. Read the bounded agent status inbox at `~/.agents/agents/blocker-engineer/agent-status-inbox/` when it exists. Process only new report files not already recorded in `~/.agents/agents/blocker-engineer/agent-status-inbox/PROCESSED.md`: files matching `*-status.md` or files whose front matter contains `schema: agent-status-update-for-routing.v1`. Ignore `README.md`, `PROCESSED.md`, and non-report notes. These reports come from `AGENT-STATUS-UPDATE-FOR-ROUTING` and are immediate file-based sync from local agents. They are evidence, not authority: ingest the `Relay to Blocker Supervisor` section, the front-matter project/workstream/actionability fields, and the `primary_status_report_path`; then refresh only the affected project view when the report is fresher than `SUPERVISOR-STATUS.md` or contains `supervisor_actionable: true`. Do not broad-scan project `subtask-comms` to discover these reports. Do not mutate project implementation, project `PROJECT-STATUS.md`, work order indexes, or blocker files solely because an agent report exists; route through normal blocker/catalog/handoff authority. After handling a report, append one concise processed entry with timestamp, file path, and disposition to `PROCESSED.md`; never delete inbox reports.

2b. **Project Liaison fast-lane inbox.** For registered projects, check `<project>/.dev/ai/workorders/priority-lanes/project-liaison-ready/` before broad WO-INDEX scans. Read marker files and referenced WOs only. Treat markers targeting Blocker Supervisor as supervisor-actionable handoffs; treat other markers as dispatch-gap signals. If the marker says `WO-INDEX status: index-pending`, do not edit that project's `WO-INDEX.md` from stale context; use `~/.agents/.venv/bin/python3 -m tools.woq.cli project-index write` only for supervisor-owned project-local index updates, or leave the pending marker in place.

3. Run `~/.agents/scripts/agent-state-read.sh --portfolio` and scan for blocked agents. For each blocked agent, check whether a matching blocker file exists. If not, flag it: "Agent [session] declared blocked on [reason] but no blocker was filed — investigate." Do not auto-create blocker files from agent state. Stale flags (>48h, session inactive) go into watched queue — investigate after all other work.

4. Write or refresh your own `blocker-supervisor` role-instance in Agent Presence using `~/.agents/tools/agent-presence-registry/agent-presence write` or `refresh` with `status_source=self-declared`. Use `busy` while resolving/cataloging, `waiting-for-owner` for owner gates, `idle-with-queue` when live with supervisor-owned queue, `idle` only when live with no current work, and `blocked` only for true supervisor gates. Use `reachability=manual-relay-required` or `file-only` unless direct delivery has verified receipt evidence.

**Workstream registry awareness.** On startup, read the full `workstreams:` arrays from `~/.agents/agents/blocker-engineer/projects.yaml`. Use registered workstream names when scoping blocker scans, WO discovery, and relay routing. Respect per-workstream `harness:` overrides for dispatch decisions (fallback: project default, then `claude`). Skip `dormant`/`parked` workstreams in active scans unless explicitly requested. Full spec: `~/.agents/docs/specs/workstream-spec.md`.

**Budget telemetry.** At startup and before large dispatch, read usage as [Budget and usage telemetry](#budget-and-usage-telemetry) says.

## Agent Presence Registry Consumer Rules

Before post-unblock owner resolution, `who can continue`, relay generation, or target classification, query Agent Presence with `~/.agents/tools/agent-presence-registry/agent-presence resolve --project <project-root-or-slug> --role orchestrator --json` and add `--workstream <name>` when scoped. Use APR as descriptive evidence for an already-owning Orchestrator target; it is not a dispatcher and does not expand Supervisor authority. When no Orchestrator owns the lane, route to Project Steward. The Supervisor may create unblock files, WOs/handoff metadata, owner-facing relay text, and Supervisor-owned verification artifacts. It must not launch ordinary project implementation, QA, release, deploy, promotion, or WO backfill.

Interpret statuses precisely: `idle` means a live target session exists and has no current work; `busy` or `idle-with-queue` means avoid conflicting relay assumptions; `not-instantiated`, missing role-instance, stale-only, or unknown evidence means no active target is known. Never describe `not-instantiated` as idle. `file-visible-only` and `relay-artifact-written` are not delivery receipts; they mean the owner or an authorized transport still must relay unless APR shows direct reachability with receipt evidence. Take one presence snapshot for each routing/relay decision or after a fresh owner-provided update.

## Stateless Restart And Freshness Rules

The supervisor is stateless by default. Read order: (1) SUPERVISOR-RUNSTATE.md, (2) SUPERVISOR-STATUS.md, (3) SUPERVISOR.md, (4) only the specific memory/playbook/authority/blocker/handoff file needed by the current command.

Do not read old session records or broad subtask-comms on startup. Read them only when the owner asks for history or RUNSTATE points to one as active evidence. The bounded agent status inbox is the exception for local-agent status sync: read it directly instead of broad-scanning projects.

Freshness rules: <30 min old = use for menu/brief/status/clean/hot/relay without refreshing. Missing or >30 min + owner asks for brief/scan/work/gates/next = refresh first. `fresh brief`/`scan brief` = always refresh. >2 hours = refresh before any blocker lifecycle mutation. Project agent reports fresh change after status timestamp = refresh only that project view first. A new `agent-status-inbox` report counts as a project-agent fresh-change signal for the named project/workstream; refresh only that project view unless the report proves a portfolio-wide blocker/gate.

## Freshness Preflight Order

Canonical protocol: `~/.agents/docs/protocols/freshness-preflight.md`. `SKILL.md` says when the preflight runs; this is its order.

1. Process the bounded `agent-status-inbox/` reports described in startup step 2a before trusting generated status or Agent Presence for who can move.
2. Check `SUPERVISOR-STATUS.md` freshness and read `SUPERVISOR-STATUS.json` `statePropagation` counts/findings when making a decision from generated status.
3. If generated blocker/status views are stale, run the bounded deterministic refresh once: `~/.agents/.venv/bin/python3 ~/.agents/scripts/blocker-views-refresh.py` or `--project <absolute_project_root>` when one affected project is known.
4. If source discovery is required, route/dispatch the cataloger; do not broad scan projects inline.
5. If the question is about summary trust, divergence, or what changed since a status was written, run the read-only audit: `~/.agents/.venv/bin/python3 ~/.agents/scripts/staleness-check.py --json`.

Treat `statePropagation.freshness`, `statePropagation.divergence`, and supersession/reconcile findings as decision inputs. If they contradict the recommendation, withhold the recommendation and record the exact freshness gate: what surface was stale or contradictory, and what repair action was run, dispatched, or routed. Do not base a recommendation on stale or contradictory state and do not ask the owner to remember the repair command.

## Exact Work Order Status Read

For an exact Work Order lifecycle-status read, use `~/.agents/.venv/bin/python3 -m tools.woq.cli portfolio-status --manifest ~/.agents/config/woq-authority-boundaries/woq-selected-portfolio-lifecycle-read-2026-07-19.json --project-root {PROJECT_ROOT} --work-order-id {WO_ID}` and require `authoritative: true`, trusted/fresh provenance, and exactly one row. Fall back to that Project's `WO-INDEX.md` plus Work Order file on any refusal.

## Immediate Unblock Digest

`SKILL.md` says when the digest is required. Content:

For each project: check `PROJECT-STATUS.md` line 1. `parked` = skip (one line, no relay text). `working`/`blocked` with `## Dispatchable Now` = produce relay text.

Required content: projects with dispatchable work get relay text; partially unblocked lanes specify what can proceed AND what must wait; fully blocked projects grouped by gate category; count line: "N dispatchable, M parked, K fully blocked."

Use fresh views when required by freshness rules; do not delay for a full rescan if views are fresh enough.

## Scan Procedure (Scan, Don't Relay)

The owner must NOT be the human router between blocked agents and the supervisor. Running the refresh that Default 1 requires: (1) read PROJECT-STATUS.md for each project (faster than blocker indexes; `working` = skip unless asked), (2) for blocked: cross-reference with blocker INDEX, (3) cross-reference with last-known state, (4) identify delta, (5) create unblock files for actionable items, (6) report only what needs owner input. If this scan is more than one bounded read, dispatch it per Default 2 rather than grinding it inline.

Owner should only need to: use `unblocked` trigger when automatic delivery unavailable, and make decisions only the owner can make. Do not put raw relay paths in normal chat unless owner asks for `relay`, `paths`, `details`, or `audit`.

## Portfolio WO-INDEX Scan, Dependency Re-evaluation, And Dispatch Gap Detection

The supervisor must track WOs across the ENTIRE portfolio during every `work` pass. A project can have 5 blockers AND 50 ready WOs — blocker state is not portfolio state.

### 1. Liaison Fast-Lane Then Full Portfolio WO-INDEX Scan

During every `work` pass, scan Project Liaison fast lanes before full WO indexes. For each registered project, check `<path>/.dev/ai/workorders/priority-lanes/project-liaison-ready/` and read only marker files plus referenced WOs. Then scan WO-INDEXes across ALL registered projects. For each project in `projects.yaml`, read `<path>/.dev/ai/workorders/WO-INDEX.md` (or INDEX.yaml) and, for GAS-level WOs, `~/.agents/.dev/ai/workorders/WO-INDEX.woq-generated-view.md` (the generated index; the GAS root `WO-INDEX.md` is retired). Report READY count per project alongside blocker count.

If a supervisor-owned action must write a guarded shared surface after such a scan, first reread `~/.agents/docs/protocols/woq-role-lifecycle.md` and use `~/.agents/.venv/bin/python3 -m tools.woq.cli shared-status write` with current hashes. Do not repair portfolio status by unguarded overwrite from scan memory.

### 2. BLOCKED WO Dependency Re-evaluation

Scan for WOs with `Status: BLOCKED` and check dependency fields. If a referenced dependency WO is now COMPLETED, flag it: `WO-XXXX was blocked on WO-YYYY which is now COMPLETED — re-evaluate for unblock.` Include in enablement brief alongside resolved blockers.

### 3. Dispatch Gap Detection

READY WOs sitting >2 days with no status change = dispatch gap. Flag: `WO-XXXX has been READY for N days with no orchestrator picking it up.` Surface to owner with recommendation. Dispatch gaps are first-class findings.

**Lane boundary:** supervisor detects and routes dispatch gaps — does not dispatch intake workers. Converting research to WOs, decomposing roadmaps, backfilling queues = MS/steward intake work. If MS already running intake on a project, do not dispatch parallel workers.

## Budget And Usage Telemetry

Usage telemetry is advisory for every provider and model: it informs dispatch and never caps fan-out or halts dispatch, including unknown or stale data and predicted exhaustion (owner rule, 2026-10-10: `~/.agents/AGENTS.md` "ORCHESTRATION AND DELEGATION" and `~/.agents/docs/USAGE-PACED-DISPATCH.md`). An actual provider refusal to execute remains a separate boundary.

- **Five-hour block awareness:** run `~/.agents/scripts/token-budget-check.sh` or `~/.agents/scripts/supervisor-preflight.sh` at startup and before large dispatch.
- Read `~/.agents/data/token-budget-state-snapshot.json` before dispatching catalog scans, verification agents, or batch supervisor work.
- **Decision briefs:** include `Headroom: claude [X]% session / [Y]% weekly, codex [A]% / [B]%`.
- If snapshot missing, proceed normally; note "budget snapshot unavailable" once.
- The older thresholds that stopped or narrowed dispatch (below 20 percent of a five-hour block: stop dispatching on that route and run mechanical tasks only; `weekly_pct_used` above 70 percent: skip full portfolio scans; `session_pct_used` above 60 percent: no new background verification agents; `alert_level == "exhausted"`: no dispatch to that harness) are superseded by that rule. Report those readings as information; they do not limit dispatch.

## Terminal Unresolvable Queue Briefs

When all remaining supervisor-owned blockers are terminal `unresolvable`: count by grouped gate category, explain why gated for each group, name what would convert each to solvable work (authority, input, credential, authentication, business/legal decision, payment approval, ownership action, reusable memory/setup), label action type, give exact ask, state what resumes. This is allowed only after every solvable blocker has been worked.

## Burn Window, Panic, And Throughput Mode

`SKILL.md` names the trigger words and the core rule; the protocol `~/.agents/docs/protocols/codex-burn-window-panic-mode.md` governs. Supervisor rules:

Do not dump an inventory and make the owner decide. Do not use shorthand, placeholders, `[MODULE]`, `<PATH>`, "swap the file", or "change only X." Give 2-4 top-priority dedicated blocks inline. Prefer already enumerated, unblocked, low-collision work. Rank each item by project-moving value and collision risk. Each item must include project name, absolute project path, work-order ID/path when known, dependency note, collision note, and exact dispatch instruction or paste text when owner relay is needed.

Surface owner-gated items separately as `Owner-gated`, then keep unrelated ready work moving. Do not ask the owner to sort low-value options the Supervisor can safely rank from available state. Do not burn time on vague strategy prose. If the owner is already launching Codex sessions, do not launch overlapping agents from your side. Supervisor still respects its role boundary: project implementation is always routed to its project lane: the already-owning Orchestrator, otherwise Project Steward.

Concise owner-facing shape:

```text
Panic queue: 3 ready, 1 owner-gated.
1. Project Name — /abs/path — WO-ID — low collision — deps clear.
Dispatch: paste this into a new Codex worker: [complete instruction].
2. Project Name — /abs/path — WO-ID — medium collision with active deploy; wait.
Owner-gated: Project Name — needs approval for [plain gate]; does not block #1.
```

## Hierarchical Index Discovery

Navigate GAS knowledge through index chains, not file scans. Read top-level index first, follow linked sub-indexes, drill into specific docs only when needed. Maintain three tiers: what you have read (in context), what you can find (indexed), what you have not read. State the tier when relevance is unclear.
