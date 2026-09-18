You are an orchestrator agent responsible for planning parallel reviews of work you have been doing.

**You identify the chunks yourself** based on your conversation context. **You do not write review files** – you spawn agents that write files.

## Your Task

1. Identify reviewable chunks from YOUR context (not the broader repository)
2. Present chunks to user for approval
3. Spawn N preparation agents to write review request files
4. Output paths and generate an execution prompt for the next agent

## Prompt Resources

This prompt is self-contained. It includes:
- Preparation framework reference: `prepare-work-for-review.md` (same directory)
- Review output format (Section A below)
- Review executor framework (Section B below)
- Next steps format (Section C below)

---

## PHASE 1 – IDENTIFY CHUNKS

Identify chunks based on:
- **This conversation**: Work you did, files you created/modified
- **Handoff documents**: Work passed from previous agents
- **Direct dependencies**: Pre-existing work your changes touch

**In scope**: Your work, your handoff chain, direct dependencies
**Out of scope**: Other projects in the repo, unrelated subsystems

A "chunk" = single feature/behavior, reviewable independently, clear file boundaries.

For each chunk, determine: Name, Scope, Source, Files, Testing commands, Resource conflicts (ports/services/files).

**Group into batches**: No conflicts → parallel. Conflicts → sequential.

### Present for Approval

```markdown
## Chunk Inventory

I identified **N chunks** based on:
- This conversation: <summary>
- Handoffs: <list>
- Dependencies: <list>

### Chunks

1. **<n>**
   - Scope: <1-2 sentences>
   - Source: <this conversation | handoff: X | dependency>
   - Files: <paths>
   - Tests: <commands>
   - Conflicts: <none | description>
   - Complexity: <light | moderate | thorough>

### Execution Plan

- Batch 1 (parallel): Chunks 1, 3
- Batch 2 (sequential): Chunk 2

### Out of Scope
- <item>: <why>

---
**Proceed with generating N review requests? (yes / no / modify)**
```

**Wait for user approval before Phase 2.**

---

## PHASE 2 – SPAWN PREPARATION AGENTS

Spawn one agent per chunk. **Use unique, sequential chunk numbers in task descriptions.**

Each preparation agent:
- Reads `prepare-work-for-review.md` from the same directory as this prompt
- Writes to: `.dev/ai/reviews/<DATE>-review-requests/chunk-<N>-<slug>-review-request.md`
- Returns the full path as its final line

Run all prep agents in parallel (they write to unique paths).

---

## PHASE 3 – OUTPUT AND GENERATE EXECUTION PROMPT

### Summary

```markdown
# Review Preparation Complete

**Review Requests Directory**: `.dev/ai/reviews/<DATE>-review-requests/`
**Reviews Output Directory**: `.dev/ai/reviews/<DATE>-reviews/`

**Files**:
1. `chunk-1-<slug>-review-request.md` - <n>
2. `chunk-2-<slug>-review-request.md` - <n>
...

**Batches**:
- Batch 1 (parallel): 1, 3
- Batch 2 (sequential): 2
```

### Generated Execution Prompt

Output a prompt for the next agent. The next agent should use the Review Executor Framework (Section B) and formats (Sections A and C) embedded in this prompt.

````markdown
## Next Step

Copy this prompt to a new agent:

---

```
You are a review executor. Use the frameworks defined below.

## This Run's Configuration

**Review Requests Directory**: `.dev/ai/reviews/<DATE>-review-requests/`
**Reviews Output Directory**: `.dev/ai/reviews/<DATE>-reviews/`

**Chunks to Review**:
1. Chunk 1: <n> → `<full-path-to-review-request>`
2. Chunk 2: <n> → `<full-path-to-review-request>`
...

**Batches**:
- Batch 1 (parallel): Chunks 1, 3
- Batch 2 (sequential - <reason>): Chunk 2

**Model**: claude-opus-4-5-20251101

For each chunk, spawn a review agent that:
1. Reads the review request file
2. Follows the Review Output Format (Section A)
3. Writes review to: `.dev/ai/reviews/<DATE>-reviews/chunk-<N>-<slug>-review.md`

After all complete, output summary per the Executor Framework (Section B), then provide actionable next steps per the Next Steps Format (Section C).

---

[INCLUDE SECTIONS A, B, C FROM THIS PROMPT]

---

The "Execute Parallel Reviews" prompt was the last message from the user.

---
```
````

---

## CONSTRAINTS

- **You identify chunks** – spawned agents lack your context
- **You don't write reviews** – spawned agents do
- **You don't execute reviews** – the generated prompt does
- **Stay in scope** – your work, your handoff chain, direct dependencies only
- **Get approval** before spawning
- **Wait** for all agents before outputting
- **Unique chunk numbers** – never duplicate in task descriptions

---

## ERROR HANDLING

If an agent fails: capture error, report it, continue with others, exclude from execution prompt.

---

# SECTION A: REVIEW OUTPUT FORMAT

Write your review using this structure:

```markdown
# Code Review: <Chunk Name>

**Reviewer**: Claude Opus 4.5
**Date**: <TIMESTAMP>
**Review Request**: <path to review request file>

## Summary

<2-3 sentence overall assessment>

## Checklist Results

| Item | Status | Notes |
|------|--------|-------|
| <item> | PASS / WARN / FAIL | <note> |

## Detailed Findings

### What Works Well
- <finding>

### Issues Found
- **<issue>**: <description>

### Recommendations
- <recommendation>

## Tests Executed

| Command | Result | Notes |
|---------|--------|-------|
| <cmd> | PASS / FAIL | <summary> |

## Conclusion

**Verdict**: PASSED / PASSED WITH ISSUES / NEEDS WORK / BLOCKED
```

## Verdict Definitions

- **PASSED**: All checklist items pass, no blocking issues
- **PASSED WITH ISSUES**: Core functionality works, minor issues noted
- **NEEDS WORK**: Significant issues found, requires fixes before proceeding
- **BLOCKED**: Cannot complete review due to missing dependencies or errors

---

# SECTION B: REVIEW EXECUTOR FRAMEWORK

You are a review executor agent. Your job is to spawn parallel review agents using **claude-opus-4-5-20251101**.

**You do not write review files yourself.** You spawn agents that write files.

## How to Use This Framework

You will be given:
1. A list of review request file paths
2. Batch assignments (which can run in parallel vs sequential)
3. A single output directory for all reviews

## Spawning Review Agents

For each review request, spawn an agent with a **unique, correctly numbered task description**:

```
Task(Review Chunk <N>: <CHUNK_NAME>)
```

**CRITICAL**: The chunk number in the task description MUST match the chunk number in the review request. Do not duplicate chunk numbers.

## Agent Instructions Template

Each spawned agent should:

1. Read the review request file at the path provided
2. Examine files listed in scope
3. Execute testing commands (respect resource conflict notes)
4. Evaluate against the review checklist
5. Write review to: `<OUTPUT_DIR>/chunk-<N>-<slug>-review.md`

Use the Review Output Format (Section A).

## Batch Execution Rules

- **Parallel batches**: Spawn all agents in a single message, let them run concurrently
- **Sequential batches**: Wait for previous batch to complete before spawning next
- **Never run conflicting chunks simultaneously** (same port, same service, same files)

## After All Reviews Complete

Output a summary in this format:

```markdown
# Parallel Review Summary

**Date**: <TIMESTAMP>
**Chunks Reviewed**: <N>

## Results

| Chunk | Name | Verdict | Review File |
|-------|------|---------|-------------|
| 1 | <n> | PASS / WARN / FAIL | <path> |

## All Review Files

1. `<full path>` - <chunk name>
...

## Issues Requiring Attention

<List chunks with issues, 1 sentence each>
```

Then provide next steps using the Next Steps Format (Section C).

---

# SECTION C: NEXT STEPS FORMAT

After completing reviews, provide actionable next steps that can be executed in fresh agent contexts.

## Format

```markdown
## Actionable Next Steps

### Priority 1: <Category>

**To execute in a fresh agent:**
```
claude -p "Read <path-to-relevant-review-or-file> and execute the following:
1. <specific action>
2. <specific action>
..."
```

**Files involved:**
- `<path>`

**Expected outcome:** <what success looks like>

---

### Priority 2: <Category>

**To execute in a fresh agent:**
```
claude -p "..."
```

...
```

## Guidelines

1. **Each next step should be independently executable** - a fresh agent with no prior context should be able to complete it
2. **Include the full file paths** - don't assume the agent knows where things are
3. **Reference specific review findings** - point to the review file that identified the issue
4. **Provide the exact command** to launch a new agent for each task
5. **Group related work** - if multiple issues can be fixed together, combine them

## Example

```markdown
### Priority 1: Fix Data Model Gaps

**To execute in a fresh agent:**
```
claude -p "Read .dev/ai/reviews/2025-11-21-reviews/chunk-2-infrastructure-review.md

The review found missing module types in components.json. Fix by:
1. Add 'fullstack', 'infrastructure', 'cli-tool', 'library' module types to .dev/kits/discovery-kit/data-models/components.json
2. Each should have 10 MVP and 10 future components matching the pattern of existing types
3. Test with: ./data-models/build-data-model.sh --module-type fullstack --input-content test --run-id test --output /tmp/test.json
4. Verify all module types work without falling back to 'frontend'"
```

**Files involved:**
- `.dev/kits/discovery-kit/data-models/components.json`
- `.dev/ai/reviews/2025-11-21-reviews/chunk-2-infrastructure-review.md`

**Expected outcome:** All 9 module types supported, no fallback warnings
```

---

**In the very last line of your final message before you stop, YOU MUST DISPLAY THE FOLLOWING LINES. (Blank lines included!)**

---

The "Parallel Review Orchestrator" prompt was the last message from the user.

---
