---
name: project-team-handoff
description: |
  Use when an existing project owner (agent or orchestrator) must package everything a NEW team needs to take over a project. This is NOT a regular handoff (same-role context preservation) — this is a TRANSFER to a different team with no assumed prior knowledge.
  Produces three companion documents: the handoff itself, a done-done cross-reference, and a verification script.
  <example>
  user: "Hand off the PA project to the new Paperclip team."
  assistant: Reads project state, produces comprehensive transfer document at the specified path.
  </example>
tags: handoff, transfer, team, paperclip, onboarding, blueprint, done-done
---

# Project Team Handoff — Transfer Document Generator

You are preparing to transfer ownership of a project to a new team that has NO prior context.
Produce a complete, self-contained handoff document so the new team can start work without asking
any questions. Output path: caller specifies; default `{project}/.dev/ai/handoffs/{PREFIX}-team-handoff-{project-name}.md`.
Use `~/.agents/scripts/get-filename-prefix.sh` for the timestamp prefix.

## Companion Documents

A handoff is NOT just one document. Produce ALL of the following:

**Always produced:**
1. **The handoff** (Sections 1-15 below) -- the main transfer document.
2. **Verification script** -- at `{project}/scripts/verify-handoff-claims.sh`. A runnable shell script that tests every verifiable claim in the handoff. See Section 14.

**Produced when a done-done definition exists:**
3. **Done-done cross-reference** -- at `{project}/.dev/ai/status/{project-name}-handoff-donedone-cross-reference.md`. See Section 13.

**Created during the handoff if they do not already exist:**
4. **Done-done definition** -- Most projects will NOT have this yet. If none exists, CREATE ONE as part of the handoff process. It does not need to be exhaustive -- capture the criteria you can derive from vision docs, WOs, proposals, and your honest assessment. Even 10-15 testable criteria are better than none. Save to `{project}/.dev/ai/status/{project-name}-done-done-definition.md`. Then produce the cross-reference (item 3) against it.
5. **Blueprint stub** -- If no blueprint exists and the project has meaningful architecture, create a minimal blueprint stub (INDEX + README + a single BLUEPRINT.md with current-state architecture and known gaps). This gives the new team a spec to work against. Save to `{project}/blueprints/{project-name}/` or `{project}/.dev/ai/blueprints/{project-name}/`. If the project is too early-stage for a blueprint, state this in Section 10 and skip.

The goal: the new team inherits not just a description of the project, but the scaffolding to measure progress. Creating these artifacts during handoff is the RIGHT time -- you have the context, the new team does not.

## Research Phase — Do This Before Writing

Collect the following in parallel before writing a single line of the document. Use sub-agents for parallelism where possible.

**Project state:**
1. Read all vision and roadmap files in the project directory.
2. Read Owner's Agent memory at `~/.agents/pa/owners-agent-memory/` (standing orders, owner preferences).
3. Read the project's doctor or specialist knowledge base if one exists (e.g., `{project}/doctor/`).
4. Check `~/.agents/.dev/ai/workorders/WO-INDEX.md` for open or recent WOs on this project.
5. Check `~/.agents/.dev/ai/proposals/` for accepted proposals affecting this project.

**Live verification (CRITICAL -- do not trust prior documents alone):**
6. List running processes, PIDs, LaunchAgents, and ports relevant to this project.
7. Run actual health checks (curl endpoints, check PIDs, verify file existence). Record the raw output.
8. Note the last 5 git commits on relevant repos.

**Blueprint and artifact state (most projects will have few or none of these -- that is normal):**
9. Check for blueprints: `{project}/.dev/ai/blueprints/` or `{project}/blueprints/`. If found, note pillars, versions, last-updated. If NOT found, note this -- you will create a stub during the handoff (see Companion Documents).
10. Check for Change Orders: `{project}/.dev/ai/change-orders/` -- list any pending or recently approved COs. If none exist, skip.
11. Check for completion audits or DPA reports: `{project}/.dev/ai/audits/` -- note the most recent and its verdict. If none exist, skip.
12. Check for open Findings: `{project}/.dev/ai/findings/` -- count by severity. If none exist, skip.
13. Determine the initiative lifecycle stage: PROPOSAL, PLANNING, EXECUTION, VERIFICATION, COMPLETE, MAINTENANCE.

**Done-done and prior handoffs (chain of custody):**
14. Check for any existing done-done definition: `{project}/.dev/ai/status/*done-done*` or `{project}/.dev/ai/status/*definition*`. Most projects will NOT have one -- that is expected. If none exists, you will create one during the handoff (see Companion Documents).
15. Read the most recent prior handoff: `{project}/.dev/ai/handoffs/` -- sorted by date, read the latest. Note what the prior team said was working vs what you observe now. If no prior handoff exists, this is the first transfer.
16. Read any cross-reference documents: `{project}/.dev/ai/status/*cross-reference*`. If none exist, skip.

**External dependencies:**
17. Check all external dependency health: LLM provider status, API token validity, credential freshness, third-party service availability. For each, verify NOW (do not trust cached state).

## Execution Strategy — How to Produce This Document

This document has 15 sections. Do NOT attempt to write them all in a single agent pass. The sections are largely independent and should be produced in parallel by multiple sub-agents. A single-pass approach runs out of context, loses quality in later sections, and takes too long.

### Parallelization

Spawn 4 parallel sub-agents for the research-and-write work, then a 5th synthesis agent that depends on their outputs. This works with both Claude Code (Agent tool) and Codex (background agents).

**Agent 1 -- Operational State** (Sections 1-3: Project Identity, Current State, Architecture)
- Work: read service health, check processes, scan project files, verify live endpoints.
- Produces: the "what is" sections.

**Agent 2 -- Standards and Knowledge** (Sections 4-5: Knowledge Base Pointers, Standards and Protocols)
- Work: read GAS docs, list artifact locations, check doctor KBs and prior handoffs.
- Produces: the reference sections.

**Agent 3 -- Monitoring and Dependencies** (Sections 6-7: External Dependencies, Active Monitoring)
- Work: check live services, verify credentials, read monitor state files.
- Produces: operational health sections.

**Agent 4 -- Specifications and Completion** (Sections 8-11: Unfinished Work, Lessons Learned, Blueprint Status, Definition of Done)
- Work: read blueprints, WOs, proposals, done-done definitions.
- Produces: the "what should be" sections.
- If blueprints or done-done definitions do not exist, this agent CREATES them (per the Companion Documents rules above).

**Agent 5 -- Synthesis** (Sections 12-15: GAS Artifacts, Done-Done Cross-Reference, Verification Script, Recommended First Actions)
- Work: reads outputs from Agents 1-4, produces the cross-cutting sections that tie everything together.
- Runs AFTER Agents 1-4 complete. This is a sequential dependency -- do not launch it in parallel.

### Output Convention

Each sub-agent writes its sections to a temporary file:
```
.dev/ai/handoffs/tmp/{timestamp}-handoff-part-{N}.md
```
The synthesis agent (Agent 5) reads all parts and assembles the final consolidated handoff document at the path specified by the caller (or the default path). Delete the temporary files after successful assembly.

### Model Selection

All handoff sub-agents MUST use the top available model (Opus for Claude, or equivalent for Codex/Gemini). Handoff documents are institutional knowledge -- the quality of the handoff directly determines whether the receiving team succeeds or fails. Do not use cheaper models to save tokens here.

## Output Contract — Write These Sections in Order

### 1. Project Identity
- Project name, one-sentence purpose, and why it matters to the owner.
- Owner standing orders that apply (from owners-agent memory or AGENTS.md).
- Vision document and roadmap locations (absolute paths).

### 2. Current State — Honest Assessment

Do NOT embellish. Write what is actually true. Distinguish three categories clearly:

**Category A: Works and verified NOW** (you ran the health check, you saw the response)
- List each capability with the exact verification you performed (curl command, test name, observed output).
- Include timestamp of verification.

**Category B: Code exists but NOT verified end-to-end**
- Code was committed but has not been confirmed working through the full user-facing path.
- CRITICAL: "Code exists in the runtime" does NOT mean "feature works for the user." The feature is only verified when a user-facing test confirms it (e.g., a Matrix user sees chunked responses, not just that chunker.py exists). State exactly which path segments are untested.

**Category C: Broken, missing, or known-failing**
- Exact error messages if available.
- What has been attempted and why it failed.

**Parity tags** (if blueprints exist): tag each feature area with MATCH (impl = spec), DRIFT (impl diverges from spec), MISSING (spec exists, no impl), or ORPHANED (impl exists, no spec).

**Operational reality:** services, ports, PIDs, LaunchAgents — what is running right now. Include exit codes for LaunchAgents (non-zero = problem).

### 3. Architecture Map
- Key directories and their roles (absolute paths).
- Service dependency graph (what talks to what, protocol/port).
- Configuration files and credentials locations (paths only, never values).
- Database files and schema/migration locations. Any symlinks that matter.

### 4. Knowledge Base Pointers
- Doctor or specialist knowledge base (absolute path).
- Research reports, accepted proposals that shaped current design (absolute paths).
- Work orders in progress or recently completed (absolute paths, WO IDs).
- Incident history: what broke, when, what changed as a result.
- Prior handoffs: list the chain with dates and key conclusions from each.

### 5. Standards and Protocols
List applicable GAS standards the new team must internalize. Use absolute paths.

**Tier 1 -- Mandatory day-1 reading (before writing any code or WOs):**
- Work Order Decision Framework: `/Users/grig/.agents/docs/WORK-ORDER-DECISION-FRAMEWORK.md`
- Git Operating Rules: Section in `/Users/grig/.agents/AGENTS.md` (search "VERSION CONTROL & GIT OPERATING RULES")
- Coding Rules: `/Users/grig/.agents/docs/coding-rules/INDEX.md` (especially G1: no duplicates, G3: imports, G10: tests, G12: error handling)
- Verification Protocols (L1-L4): `/Users/grig/.agents/docs/VERIFICATION-PROTOCOLS.md`
- Artifact Ecosystem + Blueprint System: `/Users/grig/.agents/docs/ARTIFACT-ECOSYSTEM.md` and `/Users/grig/.agents/docs/BLUEPRINT-SYSTEM-INDEX.md`

**Tier 2 -- Required within first week:**
- Sub-Agent Orchestration: `/Users/grig/.agents/docs/SUB-AGENT-ORCHESTRATION-GUIDE.md`
- Testing Practices: `/Users/grig/.agents/docs/TESTING-PRACTICES.md`
- Discovery/Findings Protocol: `/Users/grig/.agents/docs/DISCOVERY-FINDINGS-GUIDE.md`
- Path and Filename Conventions: `/Users/grig/.agents/docs/PATH-CONVENTIONS.md`
- Timestamp Utilities: `/Users/grig/.agents/docs/TIMESTAMP-UTILITIES-GUIDE.md`
- Terminal Output Standards: `/Users/grig/.agents/docs/TERMINAL-OUTPUT-STANDARDS.md`

### 6. External Dependencies and Credential Health
List EVERY external dependency the project relies on and its CURRENT health.

For each dependency:
- Name and purpose (e.g., "Gemini CLI -- primary LLM provider for live chat")
- How to verify health (exact command)
- Current status (verified NOW, not from a prior report)
- Credential location (path only, never values)
- Credential freshness: when last refreshed, whether automated or manual
- What breaks if this dependency fails
- Failover behavior (if any)

Common dependencies to check: LLM CLI tools (claude, gemini, kimi, codex), Matrix homeserver credentials, email/calendar API tokens, Paperclip embedded Postgres, third-party API keys.

Mark dead dependencies explicitly: `DEAD -- {name}: {error}. Must be removed or credential-refreshed before use.`

### 7. Active Monitoring
- Monitors that exist and where their state files live (absolute paths).
- Monitor calibration status: are the monitor's verdicts trustworthy? If the monitor says 0% pass rate but the canary says things work, the monitor is miscalibrated. State this explicitly.
- Known false alarms: what they look like and why they fire.
- Baseline metrics: what "healthy" looks like in specific numbers.
- How to silence or tune alerts.
- Recovery time: how long from failure detection to automatic recovery? Is there an auto-recovery mechanism or does a human/agent need to intervene?

### 8. Unfinished Work
- Issues or WOs in progress (IDs, locations, current status).
- Deferred items: what and why (intentionally parked, not forgotten).
- Dependencies on other projects or teams (what is blocked on what).
- Open decisions and where the decision thread lives.
- Open Findings by severity, with absolute paths to each.
- Pending Change Orders: ID, summary, and whether they block active work.
- Initiative lifecycle stage and what must happen to advance to the next stage.

### 9. Lessons Learned
- Approaches that worked and why.
- Approaches that failed -- specific enough to prevent repetition.
- Gotchas the new team WILL hit (frame as certainties to force reading).
- Owner preferences not written down anywhere else.
- Patterns from prior handoffs: what the previous team got wrong that this handoff corrects.

### 10. Blueprint and Specification Status

Most projects will not have blueprints at handoff time. That is normal -- blueprints are demanding to create and often only become worthwhile at the point of team transfer.

**If blueprints exist:**
- Blueprint index location (absolute path).
- Active blueprints by pillar/area with version and last-updated date.
- Pending Change Orders: CO ID, summary, status (PROPOSED/APPROVED/IMPLEMENTED).
- Parity gaps: areas where spec and implementation are known to diverge (reference Section 2 parity tags).

**If NO blueprints exist (the common case):**
- State explicitly: "No blueprints existed prior to this handoff."
- If you created a blueprint stub as part of this handoff (see Companion Documents), reference its location and note it is a starting point, not a complete spec.
- Identify which areas would benefit most from a full blueprint (typically: architecture, core data flows, and the feature area with the most active development).

### 11. Definition of Done and Completion Criteria

Most projects will not have a formal done-done definition at handoff time. If one did not exist, you should have created one as part of this handoff (see Companion Documents).

**If a done-done definition exists (pre-existing or just created):**
- Done-done definition location (absolute path).
- Summary: total criteria count, how many MET vs NOT MET, by tier.
- Parity Check 1 (Vision to Blueprint): Does every vision goal have a corresponding blueprint? Status. (Skip if no blueprints exist.)
- Parity Check 2 (Blueprint to Implementation): Does every blueprint have a verified implementation? Status. (Skip if no blueprints exist.)
- Parity Check 3 (Implementation to Done-Done): Does every implementation have a done-done criterion with a testable verification? Items WITHOUT criteria are gaps.

**If you created the done-done definition during this handoff:**
- Note that it was created as part of the transfer, not by the original team.
- Flag any criteria where you had to guess at the target (e.g., "latency target set to 60s based on observed behavior -- owner should confirm").
- The new team should review and refine the criteria in their first week.

**Always include:**
- Quality gates: testing coverage, documentation completeness, deployment readiness, security review.
- Date and verdict of last completion audit (or "No completion audit exists").
- The "new user test": Can a new agent, given only this handoff and the codebase, build and run the project without asking questions? If not, state what is missing.

### 12. GAS Artifact Locations
Consolidated index of all GAS artifact paths relevant to this project. Omit any that do not exist.
- Blueprints: `{project}/.dev/ai/blueprints/` or `{project}/blueprints/`
- Change Orders: `{project}/.dev/ai/change-orders/`
- Work Orders: `{project}/.dev/ai/workorders/` and global `~/.agents/.dev/ai/workorders/`
- Proposals: `~/.agents/.dev/ai/proposals/`
- Findings: `{project}/.dev/ai/findings/`
- Audits and DPA Reports: `{project}/.dev/ai/audits/`
- STATE-OF-PROJECT: `{project}/.dev/ai/STATE-OF-THE-PROJECT.md`
- Handoffs: `{project}/.dev/ai/handoffs/`
- Done-Done Definition: `{project}/.dev/ai/status/`
- Cross-References: `{project}/.dev/ai/status/`
- Vision: `{project}/docs/vision/` or `~/.agents/docs/vision/`
- K2B Specs: `{project}/.dev/ai/k2b-specs/`
- Research: `{project}/.dev/ai/research/` or `~/.agents/docs/research/`
- Recipes: `{project}/recipes/` or `{project}/pa/recipes/`
- Doctor KB: `{project}/doctor/`
- Owner Memory: `~/.agents/pa/owners-agent-memory/`

### 13. Done-Done Cross-Reference (Companion Document)

Produce a separate companion document at `{project}/.dev/ai/status/{project-name}-handoff-donedone-cross-reference.md`.

If no done-done definition existed AND you could not create one (insufficient context), state this and recommend creating one as the new team's first action. Skip the rest of this section.

Otherwise (whether the done-done definition was pre-existing or you just created it), the cross-reference MUST include:

**Section A: Coverage Matrix**
For each done-done criterion: does the handoff address it? Current status? What gap remains?

**Section B: Handoff Items Without Done-Done Criteria**
Items in the handoff that have no corresponding testable success criterion. These are gaps the new team must close by adding criteria. For each: what criterion should be added, to which tier, and why.

**Section C: Contradiction Detection**
CRITICAL: Explicitly check for contradictions between:
- Handoff says "WORKING" but done-done says "NOT STARTED" (common when code exists but isn't end-to-end verified)
- Handoff says "IMPLEMENTED" but metrics show it isn't meeting targets
- Prior handoff claims vs current observed state
For each contradiction: state both sides, explain which is correct, and what the new team should trust.

**Section D: Risk Assessment**
- Criteria with no WO or proposal covering them
- Criteria depending on external/owner actions
- Longest path to completion (ranked by calendar time)

**Section E: Recommended Priority**
- First 24 hours: orientation and triage actions
- First week: the one thing that must improve
- First month: what tier to target

### 14. Verification Script (Companion Document)

Produce a runnable shell script at `{project}/scripts/verify-handoff-claims.sh` that tests every verifiable claim in the handoff.

The script must:
- Check each health endpoint mentioned in the handoff
- Verify each file/directory claimed to exist
- Check each LaunchAgent's status and exit code
- Test each credential/token for validity (without exposing values)
- Report PASS/FAIL per claim with the section number it verifies
- Exit 0 only if all claims pass; exit 1 otherwise
- Be runnable by the new team on day 1 as their first action

Example output format:
```
[PASS] Section 2A: Runtime health at :8201 (status: ok)
[PASS] Section 2A: Gateway health at :8300 (status: ok)
[FAIL] Section 2A: Paperclip health at :3100 (connection refused)
[PASS] Section 6: Claude CLI auth valid
[FAIL] Section 6: Kimi CLI auth (402: membership expired)
---
Results: 14 PASS, 2 FAIL
```

### 15. Recommended First Actions
- What the new Team Lead should do in the first 30 minutes.
- **First command:** Run `{project}/scripts/verify-handoff-claims.sh` to see what the handoff claims vs reality.
- Critical path: the one thing that must be true before anything else starts.
- Quick wins: low-effort, high-signal tasks to verify the environment.
- Verification commands: exact shell commands to confirm services are running and tests pass.
- Read the project's blueprints (Section 10 paths) before modifying any code.
- If you created the done-done definition and/or blueprint stub during this handoff, tell the new team to review and refine them in week 1.
- If no completion audit exists, recommend running a Mode A Design Parity Audit.
- If the cross-reference (Section 13) found contradictions, resolve them before starting new work.
- Who to contact if something is unclear (agent cards, Paperclip agent IDs).

## Formatting Rules
- No tables. Use labeled sections and bullet lists.
- All paths absolute (start with `/Users/` or `$HOME`). No emoji.
- Do NOT embellish. State facts or state uncertainty as: `UNKNOWN -- new team must verify: {what to check}`.
- No vague language ("mostly working", "should be fine"). Be specific or be uncertain.
- Distinguish "code exists" from "feature works end-to-end for the user." This distinction prevents the most common handoff lie.

## Final Step

After writing ALL documents (handoff + verification script + any created done-done/blueprint/cross-reference), output to the user:
```
Team handoff written to: {absolute path}
Cross-reference written to: {absolute path}
Verification script written to: {absolute path}
State: {one line -- what works / what does not}
Open work: {count of open WOs/issues}
Critical blockers: {count, or "none"}
Contradictions found: {count, or "none"}
Done-done gaps: {count of handoff items without criteria}
First action: {one sentence}
```
Do not offer to do more. The three documents are the deliverable.
