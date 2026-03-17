---
name: project-inception
description: |
  Use when a concept has been discussed for the first time and needs to go from idea to execution-ready
  package. This is the counterpart to PROJECT-TEAM-HANDOFF: handoff transfers an EXISTING project;
  inception takes a CONCEPT and produces everything a team needs to execute it.
  Produces: research brief, draft blueprint, phased work orders, team configuration, initiative package,
  and board direction issue.
  <example>
  user: "We just discussed building a webhook relay. Incept it."
  assistant: Spawns 5 parallel sub-agents, produces complete initiative package.
  </example>
  <example>
  user: "Incept this concept: distributed cache layer for PSE queries."
  assistant: Reads conversation context, produces research brief + blueprint + WOs + team config.
  </example>
tags: inception, project, kickoff, initiative, blueprint, work-order, team, paperclip
---

# Project Inception -- Concept to Execution-Ready Package

Produce a complete initiative package so a team can execute a newly discussed concept without
asking questions. **Inputs:** `{concept}` (the idea) and `{conversation-context}` (key points,
decisions, constraints). **Output:** `.dev/ai/initiatives/{project-slug}/`
(use `~/.agents/scripts/get-filename-prefix.sh` for timestamp prefixes).

## Deliverables (6 Documents)

1. **Research Brief** -- `RESEARCH-BRIEF.md`
2. **Draft Blueprint** -- `BLUEPRINT-DRAFT.md`
3. **Work Orders** -- `workorders/WO-{project}-{timestamp}-{NNN}.md` (one per phase)
4. **Team Configuration** -- `TEAM-CONFIG.md`
5. **Initiative Package** -- `STATUS.md` (initiative metadata + queue entry)
6. **Board Direction** -- `BOARD-DIRECTION.md` (initial issue for Team Lead)

## Execution Strategy -- Parallel Sub-Agents

Do NOT produce all 6 documents sequentially. Spawn background sub-agents per SO-016
(orchestrators delegate, never block). Sub-agents write to `.dev/ai/initiatives/{project-slug}/tmp/`.
The synthesis agent assembles final documents and deletes `tmp/` after.

### Agent 1 -- Research (background, Opus)

Scan for prior art and feasibility. Write `tmp/research.md`.

**Instructions:**
- Search `~/.agents/` for existing code, tools, or modules related to `{concept}`
- Search `~/.agents/.dev/ai/proposals/` for prior proposals on this topic
- Search `~/.agents/docs/research/` for existing research
- Check `~/.agents-projects/` for related upstream projects
- Check owner's GitHub stars for relevant bookmarked repos: `~/.agents/scripts/github-stars-search.sh '<keywords>'`
- Assess technical feasibility: what exists, what is missing, what is hard
- Identify key design decisions the team must make
- Recommend an approach (build vs adopt vs extend existing)
- Note any OSS prior art worth examining

### Agent 2 -- Blueprint (background, Opus)

Draft the blueprint from the concept and conversation context. Write `tmp/blueprint.md`.

**Instructions:**
- Define "done" in concrete, testable terms (what does the user see/experience when this works?)
- Core mechanics: how does it work? Data flow, key components, integration points
- Definition of Done with 10-20 testable criteria grouped by tier (mandatory, quality, stretch)
- Constraints: what cannot change, what must be preserved, performance targets
- Dependencies: what this needs from other systems, what other systems need from this
- This is a DRAFT -- label it clearly. The team will refine it after research completes
- Follow blueprint conventions from `~/.agents/docs/BLUEPRINT-SYSTEM-INDEX.md`

### Agent 3 -- Work Orders (background, Opus)

Create phased work orders from the concept. Write `tmp/workorders/` (one file per WO).

**Instructions:**
- Read `tmp/blueprint.md` (wait for Agent 2 output if needed -- check for file existence)
- Break work into phases: each phase = one WO with 3-7 tasks
- Phase 1 should be a standalone deliverable (no partial value -- the team ships something usable)
- Each WO follows the format in `~/.agents/prompts/work-orders/CREATE-WORK-ORDER.md`
- Each task has: description, dependencies, success criteria, verification command
- Build the dependency DAG: which WOs block which
- Estimate effort per WO (hours or days)
- Include Section 7 (Execution Graph) with depends_on, blocks, can_parallelize_with
- Model recommendation per WO (Opus for architecture/ambiguous, Sonnet for mechanical leaf work)

### Agent 4 -- Team Configuration (background, Sonnet)

Prepare the team setup. Write `tmp/team-config.md`.

**Instructions:**
- Determine if this fits an existing Paperclip company or needs a new one
- Define agent roster: roles needed (team-lead, dev-workers, research, triage, QA)
- For each agent: role, model (Opus/Sonnet), heartbeat interval, skills needed
- Reference agent prompts from `~/.agents/prompts/agents/_AGENT-INDEX.md`
- Heartbeat config: interval, max concurrent workers, approval gates
- Special agents: does this concept need a doctor, a monitor, a specialist?
- If no Paperclip infrastructure exists yet, specify manual execution with GAS sub-agents instead

### Agent 5 -- Synthesis (sequential, Opus -- runs AFTER Agents 1-4)

Assemble all 6 final documents from `tmp/` outputs.

1. Read all `tmp/` outputs. Reconcile: if research found existing solutions, adjust blueprint and WOs
2. Assemble RESEARCH-BRIEF, BLUEPRINT-DRAFT (enriched with research), work orders (adjusted for feasibility), TEAM-CONFIG
3. Create STATUS.md and BOARD-DIRECTION.md (formats below)
4. Delete `tmp/`. Output the summary block (see Final Output)

## Document Formats

### STATUS.md

```markdown
# Initiative: {concept name}

**Slug:** {project-slug}
**Created:** {timestamp}
**Status:** READY_FOR_TEAM
**Origin:** Conversation inception on {date}
**Owner:** {from conversation context, or "TBD"}

## Summary
{2-3 sentences: what this is and why it matters}

## Documents
- Research Brief: {absolute path}
- Blueprint Draft: {absolute path}
- Work Orders: {absolute path to workorders/ dir} ({count} WOs)
- Team Config: {absolute path}
- Board Direction: {absolute path}

## Estimated Effort
- Total WOs: {count}
- Critical path: {WO chain}
- Estimated calendar time: {days/weeks}
- Parallel tracks: {count}

## Dependencies
- Blocks: {what this initiative blocks, or "nothing"}
- Blocked by: {what blocks this initiative, or "nothing"}
- External: {external dependencies}

## Next Action
{One sentence: what must happen next for this to start executing}
```

### BOARD-DIRECTION.md

```markdown
# Board Direction: {concept name}

**For:** Team Lead
**Priority:** {from conversation context}
**Created:** {timestamp}

## Directive
{What the team must accomplish, in 3-5 sentences. Written as a directive from the board.}

## Context Documents (Read Before Acting)
1. Research Brief: {absolute path} -- what exists and what is feasible
2. Blueprint Draft: {absolute path} -- what "done" looks like
3. Work Orders: {absolute path} -- phased execution plan
4. Team Config: {absolute path} -- who does what

## Expected First Actions
1. Read all context documents above
2. Produce a state report confirming you understand the scope
3. Review and refine the blueprint draft (it is a draft, not final)
4. Begin Phase 1 work orders -- they are designed to be independently shippable
5. Post status after first heartbeat cycle

## Constraints
{Key constraints from the conversation: budget, timeline, technical limits, owner preferences}

## Success Criteria
{Top 3-5 criteria from the blueprint that define when this initiative is DONE}
```

## Model Selection and Formatting

- Agents 1, 2, 3, 5: **Opus** (judgment, synthesis, architecture). Agent 4: **Sonnet** (mechanical roster assembly). Escalate Sonnet to Opus on rework.
- No tables in output documents (unreadable in terminals). Use labeled sections and bullet lists.
- All paths absolute. No emoji. No vague language -- be specific or mark `UNKNOWN -- team must determine: {what}`.
- Distinguish "concept discussed" from "design decided" from "implementation exists."

## Final Output

After writing ALL documents, output to the user:

```
Initiative incepted: {concept name}
  Package: {absolute path to initiative directory}
  Research: {one-line summary of feasibility}
  Blueprint: {one-line summary of what done looks like}
  Work orders: {count} WOs, {count} phases, est. {time}
  Team: {roster summary}
  Board direction: {absolute path}
  Next action: {one sentence}
```

Do not offer to do more. The 6 documents are the deliverable.
