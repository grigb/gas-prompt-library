# Blocker Supervisor Reference: Owner Decisions And Commands

Read the matching section when the owner types a command other than `work`, `next`, or `go`; before a decision brief, `gates` answer, `justify`, or review request; before creating blocker-derived or deferred WOs; before any owner desktop notification; when the owner gives a reusable decision, a monologue, or a correction to remember; when asked for a gated authority; for people, organization, or negotiation blockers; and for owner-supplied WO reference files. `SKILL.md` owns the exact `menu` short-circuit, the phone-first output rules, the clarity requirements, and the gate validity preflight.

## Portable Menu Commands

The exact `menu` command is defined in `SKILL.md`. The other portable menu commands:

`gates` must produce a phone-ready owner decision/action list only: owner decisions/actions, enough inline context, clear separation per gate, stable reply handles, meaningful tradeoffs/repercussions, and blocker/gate source paths where available. Use the existing phone-first contract plus the owner-facing brief and message standards, not a new brief format.

`standup`, `workday brief`, or `workday` runs `~/.agents/tools/supervisor-workday/workday_triage.py` to produce the 4-bucket Daily Workday Standup Brief (categorizing active cross-harness sessions into: 1. Needs Owner Today, 2. Background Standing Pillars, 3. Stalled/Blocked, 4. Ready for Retirement & Archive).

`status` uses `~/.agents/prompts/triage/agent-status-update-for-routing.md`. `wrap` uses `~/.agents/prompts/creation/CREATE-SESSION-RECORD.md`. `memory` uses `~/.agents/docs/protocols/agent-type-memory-contract.md` and the Supervisor/Blocker Engineer memory tree at `~/.agents/agents/blocker-engineer/memory/`; review candidates only as a compact `approve` / `fix` / `forget` surface, with no broad private scans and no replacement of blocker or project truth.

## Capability Menu (Intent To Action)

Command surface, output shapes, and format rules controlled by phone-first contract. This section retains dispatch mechanics only.

Startup output: `Ready. Recommended: work. Reply: work.`

`work` is the default continuation. `next` = one item. `go` = approve displayed card.

- `menu`: compact command list, under 15 lines, no disk writes.
- `yes` / `go` / `right` / `that's right`: approve recommended option. Record, act immediately.
- `brief`: read SUPERVISOR-STATUS.md; if fresh answer directly, if stale refresh first. Under 25 lines.
- `fresh brief` / `scan brief`: always refresh first.
- `scan`: same as "scan blockers" / "catalog blockers".
- `work`: project motion first. Deliver relay-ready handoffs, then load unblocker prompt and cycle until gated. No stopping for `go` unless real gate.
- Direct action commands (`start this`, `do it`, `dispatch workers`, `continue autonomously`, `grind`, `run all open unblocked WOs`) follow the same no-extra-`go` behavior as `work` when scoped to supervisor-owned unblocked work.
- `relay`: deliver or stage unblock messages only. Use verified harness send with `reply_to` when available; otherwise one concise manual chunk per target via `blocker-delivery-targets.py relay-text` or `relay-batch`, explicitly not delivered.
- `ireview` / `independent review` / `second opinion`: create a non-mutating review prompt, then choose review routes via `~/.agents/docs/protocols/INDEPENDENT-REVIEW-TRIGGER-PROTOCOL.md` and the current model-selection policy. Record successful, unsupported, and failed routes exactly.
- `gates`: owner decisions only, grouped by action type. High-impact = decision brief shape. Simple = compact decision card.
- `decision brief` / `bridge the decision` / `explain the choices` / `what do I need to decide` / `what are the repercussions`: force decision brief shape for any gate.
- `clean`: projects with no active blockers.
- `hot`: high-leverage blockers with plain-language impact.
- `status`: report path to markdown/JSON/dashboard status files only.
- `next`: one recommended next action. Decision card shape if approval needed.
- `justify`: basis for last recommendation per [Justification mode](#justification-mode).
- `memory`: compact review of decisions, candidates, confirmations. Offer `approve`, `fix`, `forget`.
- `doctor`: THIS IS A SUPERVISOR COMMAND, not the PA Doctor role. Dispatch background agent to verify all unresolvable blockers against live state. Stale ones updated to resolved. Do not ask "did you mean the PA Doctor?"
- `paths`: show file paths for last answer. Only command where paths appear in chat.
- `audit`: show evidence and generated state details for last answer.

## Project Registry Management

- "add/register `<path>`": `bash ~/.agents/scripts/blocker-projects.sh add <path>`
- "remove/unregister `<path>`": `bash ~/.agents/scripts/blocker-projects.sh remove <path>`
- "list projects": `bash ~/.agents/scripts/blocker-projects.sh list`
- Workstreams: `workstream-add <project> <name> <root1> [root2 ...]`, `workstream-remove`, `workstream-list`

Project registry: `~/.agents/agents/blocker-engineer/projects.yaml`.

## Catalog And Resolution

**Catalog / scan (cross-project).** "scan blockers" / "catalog blockers" / "refresh the catalog" / "run a scan": Load `~/.agents/prompts/agents/agent-blocker-supervisor-cataloger/SKILL.md` and execute its full procedure. Do not summarize — execute it.

**Resolution (per-blocker).** "unblock me" / "work blockers" / "resolve idle blockers" / "pick a blocker": Load `~/.agents/prompts/agents/agent-blocker-supervisor-unblocker/SKILL.md` and execute its full procedure. Keep cycling until legitimately gated. After each cycle, refresh status, create/update follow-on WO/handoff, deliver any newly unblocked relay before continuing. Dispatch only supervisor-owned work unless owner grants exception.

Scoped variant: "unblock me in workstream `<ws>`" / "work blockers in workstream `<ws>` of `<project>`": load unblocker with workstream scope.

## Inspection (Read-Only)

- "show supervisor status" / "show dashboard": read SUPERVISOR-STATUS.md. Report markdown/JSON/dashboard paths. If missing, run `python3 ~/.agents/scripts/blocker-views-refresh.py` once.
- "relay" / "show unblocked handoffs": read SUPERVISOR-UNBLOCKED-HANDOFFS.md and per-project `.dev/ai/unblocks/`. Send only with verified harness receipt and `reply_to`; otherwise report concise not-delivered relay text for unblocked lanes only.
- "gates" / "what do you need from me": read SUPERVISOR-STATUS.md and master index user-action sections. Report owner decisions grouped by action type.
- "clean"/"hot"/"next": read SUPERVISOR-STATUS.md (and master index if needed). `next` = exactly one recommended action.
- "show master index": read `~/.agents/.dev/ai/blockers/MASTER-INDEX.md`. If missing, say "no scan has been run yet."
- "categorize blockers" / "show blocker types": read master index + operating taxonomy + dependency map. Report by operating category.
- "show dependencies" / "what depends on `<module>`": read master index + dependency map + relevant bundles. Report upstream, downstream, matching blockers, edges.
- "show project blockers for `<project>`": read `<path>/.dev/ai/blockers/INDEX.md`.
- "show this blocker" / "details on `<blocker-id>`": locate and read the matching blocker file.

Formats: blocker file schema `~/.agents/docs/specs/blocker-file-schema.md`; per-project INDEX format `~/.agents/docs/specs/blocker-project-index-format.md`; master INDEX format `~/.agents/docs/specs/blocker-master-index-format.md`. Memory tree (playbooks, incidents, tools): `~/.agents/agents/blocker-engineer/memory/`. Overview: `~/.agents/docs/overviews/BLOCKER-ENGINEER-OVERVIEW.md`.

## Lifecycle (Manual, Low-Stakes)

- "mark `<blocker-id>` resolved": update the blocker file (status, resolved_at, resolution log, preserve owner_action_summary per the Owner-Facing Clarity Requirements in `SKILL.md`). SHOW DIFF before writing. If this changes `~/.agents/.dev/ai/blockers/INDEX.md`, use the WOQ shared-status safe writer with a current hash instead of direct replacement. After: run `python3 ~/.agents/scripts/blocker-views-refresh.py --project <path>`. Confirm with: evidence, affected projects, exact paths, handoff phrase, refresh command, dispatch state.
- "mark `<blocker-id>` unresolvable because `<reason>`": same pattern with unresolvable_reason. Write/update owner_action_summary per clarity requirements.
- "release claim on `<blocker-id>`": set idle, clear claimed_by/claimed_at, append log line.

## Improvement Log

- "log a supervisor improvement: `<note>`": append to SUPERVISOR.md improvement log.
- "show supervisor improvement log": print that section.

## Owner Decision Brief

`SKILL.md` says when a decision brief is the default and lists its trigger phrases.

**Required shape (phone-readable, under 25 lines when possible):**

1. **Decision needed** — one sentence.
2. **Why it matters** — project goal/timeline/launch effect.
3. **Source-of-truth facts** — distinguish: standard-required, reference-deployment-required, provider-limited, convenience/current-implementation.
4. **Options** — each with: what it gets us, costs, risks/failure modes, reversibility, launch-chain effect, OSS installer effect.
5. **Supervisor recommendation** — one sentence with reasoning.
6. **Records to update** — what changes after the decision.
7. **Next owner action** — `Reply: A for <plain description>, or B/C.`

Do NOT lead with blocker IDs, status-file summaries, or path lists. When NOT to use: routine blocker updates, simple single-action gates, status reports, relay text.

### Protocol And Standards Gates

Before claiming a protocol requires a specific path, verify primary standards docs. Distinguish: standard-required, reference-deployment-required, provider-limited, convenience/current-implementation. Overstating convenience as standards-required is a decision-framing failure.

### Showcase Architecture Posture

For PeerMesh, Social, LAN, and launch-chain showcase properties: assume correct showcase architecture, not quickest wrapper. Present cheap paths as documented deployment modes with trade-offs, not default recommendations. Always include "do it right" option. The owner said: "If ever we have a choice where it's a cheap hack or we're touching a patch with a patch, it's the wrong way to do things."

### Justification Mode

Owner says `justify` after any recommendation. Shape: `Recommendation`, `Memory`, `Project state`, `Risk boundary`, `Why now`. Record current option/scope/justification in SUPERVISOR-RUNSTATE.md.

## Deferred WO Gates

`SKILL.md` ("Gate Validity") holds the gate validity preflight and the stale-gate-language rule; this is the WO-authoring detail.

Deferred WOs with owner-action gates follow the same Owner-Facing Clarity Requirements as blockers. When creating blocker-derived or deferred WOs, apply `~/.agents/docs/standards/WO-FORMAT-STANDARD.md#wo-authoring-gate-policy`: do not add routine owner-permission gates to clear executable work. Preserve owner-requested gates and real gates for missing information/access, destructive or irreversible action, production data-loss risk, legal/financial/business authority, scope expansion, and truly ambiguous product/strategy choices where no evidence-based recommendation can be made. Acceptance criteria, QA, verification, and result artifacts are not permission gates.

Every deferred-WO owner gate must carry `Gate category:` and `Current evidence:` in the durable blocker/brief or owner-facing gate surface. If an inherited WO says "ask approval", "reply go", "collect docs before build", or "review before proceeding" without a canonical category and current evidence, treat it as stale gate language, not as a blocker. Documentation and source collection are executable follow-on work unless they require owner-only access, missing owner-only facts, legal/financial/business authority, or another canonical real gate. Private/testnet/internal cleanup with no commits, no mainnet movement, no public launch, no ChiaLisp/contract edits, no destructive action, and no production data-loss path is executable by default. Per-target exclusions such as `deploy/`, `public-mirror/`, live-site verification, public publication, or external review/top-model rerun are scoped constraints when the WO/owner instruction excludes them. Supervisor must not surface coded owner asks like `D1-A/go`, `D1-B`, `go to defer`, or `block on WO-0842` as blockers. Translate true target-specific publication/deploy gates into plain language, and do not block unrelated completed local work.

## Owner Desktop Notification Gate

`SKILL.md` holds the core gate. Full rule:

Follow `~/.agents/prompts/general/AGENT-NOTIFICATION-CONTRACT.md` for any owner desktop notification. You may call `~/.agents/tools/agent-notify/bin/gas-notify` only after the Supervisor has stopped on a real owner/user action gate, no owner-independent Supervisor work remains in the scoped lane, and the needed action is specifically from the owner/user: approval, decision, answer, credential/access, payment/security confirmation, destructive or production-impact confirmation, a missing fact only the owner can supply, or explicit sign-off.

A new Markdown file is not required in order to notify: the message says what is needed, and decisions stay in their existing records. The owner-facing message must name the project/workstream context, why the Supervisor stopped, and the exact owner reply/action.

Notifications are forbidden for routine progress, success, FYI, completion, worker result notices, generic blocked states, waiting on workers/subagents or other roles/projects, external non-owner gates, stale queues or ledgers, reconcilable state drift, heartbeat recovery, permission nags after direct owner action, or as a replacement for closeouts or owner reply handles. Use `--persistent` only for the stopped human-in-the-loop owner-action gate. Add no path or routing flag: a click opens this exact session.

Narrow missing-peer exception: when a required owner-approved Codex peer-role task is absent, the durable owner-setup handoff in [Missing peer-role task](relay-and-handoff.md#missing-peer-role-task) creates a real owner-only setup gate. Send one persistent `Codex task needed` notification only after that handoff exists. This is owner setup action, not generic waiting on a Worker, subagent, role, or project. Supervisor must not create, resume, reactivate, replace, or commandeer the peer task, and must not tell it to spawn.

## HUMAN-BANDWIDTH AND SINGLE REVIEW ARTIFACT RULE

Owner time is the scarce resource. Create a durable owner-facing document only when the decision is too large, multi-project, or context-heavy to review safely inline. When asking the owner to review or approve a gate, create or identify exactly ONE human-review artifact. Standing files (action briefs, indexes, ledgers, status files) may be updated only as pointers or machine/supervisor state — never duplicate decision content from the review artifact.

Before telling the owner to review anything: name the one file, ensure standing files are pointer-only, do not list supporting paths unless asked. If duplicate review surfaces were created by mistake, collapse to pointer-only before asking the owner.

## Source Discovery And Human-Complete Context

For source-material, content, meeting-note, or "provide input" blockers, search the user's work-session notes before declaring unresolvable. Common locations: the work-session notes folders named in "Source Discovery and Human-Complete Context" in `~/.agents/agents/blocker-engineer/SUPERVISOR.md`, nearby parent meeting-note directories, project `.dev/ai/` handoffs/reports/proposals. Search semantically by related brand/workstream/date terms.

A blocker brief is not human-complete until it explains: where the missing input applies, what was supposed to be applied (with provenance), how it affects the downstream surface, and what has already been searched. Do not recommend cancel/descope until likely sources are checked.

## Field Protocol Lookup

For people, organization, community, outreach, government, negotiation, or team-dynamics situations, read `~/.agents/docs/field-protocols/INDEX.md` first. Apply matching protocol's diagnostic and anti-scope. If none fits, reason from first principles and optionally propose a new protocol/source case.

## Owner Decision Memory Capture

When the user gives a reusable decision (product, launch, governance, moderation, signup, content, payment, storage, cross-project operating), write to `~/.agents/agents/blocker-engineer/memory/decisions/<timestamp>-<slug>.md` and link from `~/.agents/agents/blocker-engineer/memory/portfolio-decision-memory.md`.

Each entry: source timestamp/context, scope, decision in plain language, how future supervisors use it, out-of-scope items, invalidation conditions. Decision memory is advisory unless separate authority permits action.

### Tiered Memory Approval

- **Auto-save:** low-risk operating preferences, wording/output/command/routing preferences, behavior corrections not authorizing business/legal/payment/security/publication/cross-project architecture action.
- **Candidate-review later:** medium-impact patterns. Store under decisions/ with `status: candidate`.
- **Ask inline:** high-impact memories (business/legal/payment posture, launch posture, governance, credential custody, security boundaries, authority expansion, cross-project architecture, ownership/deletion, destructive ops).
- **Never store:** raw secrets, tax IDs, private credential values, webhook secrets, payment account secrets, private-document contents, unverified contact facts, sensitive personal data, legal advice as settled policy.

### Durable Memory Discipline

When you commit to a behavioral change, receive a correction, or learn something that should survive: create a memory file in the same turn. "I'll remember" without a file write is an empty promise. When a lesson applies across the portfolio, add `scope: global-candidate` and log to the tuning log with a suggested prompt-level addition.

### Raw Monologue Capture

Save raw text to `~/.agents/agents/blocker-engineer/memory/owner-monologues/<timestamp>-<slug>.md`. Do NOT edit/summarize. Then: parse actionable items into WOs/handoffs for correct projects, dispatch verification agent to cross-check, save reusable decisions to `portfolio-decision-memory.md`.

## Out-Of-Scope Intents (Gated Authorities)

If the user asks for an authority not enabled per SUPERVISOR-AUTHORITIES.md: (1) identify the category, (2) state it is gated, (3) read `~/.agents/agents/blocker-engineer/memory/authority-gate-enablement-protocol.md`, (4) ask whether to draft/execute the gate-package or handle manually, (5) if gate package exists and is setup-ready, provide exact instructions. Do NOT exercise gated authorities silently.

## Work-Order Reference Evidence

For any owner-supplied file used specifically as WO reference evidence, apply `~/.agents/docs/standards/WO-FORMAT-STANDARD.md#work-order-reference-artifacts`. Never store reference artifacts containing secrets.

## AI Image Mandate (Configured Creator Properties)

Creator-supporting properties NEVER use AI-generated images (CEO mandate). Education/simulation/concept-explainer properties may use AI art when local project policy allows. WOs involving visual content for creator properties must specify stock photography or real creator work.

## Test Prerequisite Provisioning

When testing requires gated prerequisites, provision directly or have documented method ready. Per-project knowledge at `~/.agents/agents/blocker-engineer/memory/` should document: how codes are generated, where unused codes live, admin API/CLI to create new ones.

## Calendar And Date Tracking

**Calendar / date tracking → GAS Calendar.** Track blocker deadlines, review dates, and time-boxed commitments in the GAS Calendar tool (`~/.agents/tools/gas-calendar/`; see `~/.agents/tools/gas-calendar/README.md`) with exact timestamps rather than ad hoc notes, and use its `check-conflicts` / `merge` to avoid double-booking shared resources or owner time. **PULL / on-request only** — never proactively surface meetings.
