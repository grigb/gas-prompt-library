# Orchestrator Learned Patterns

> **READ-ONLY INDEX.** This file is an overview of all learned patterns.
> Individual patterns live in `~/.agents/prompts/agents/orchestrator-patterns/*.md` (one file per pattern).
> The orchestrator MUST read this index AND scan the patterns directory during Phase 1 (Context Acquisition).

## How This System Works

1. **During sessions:** The orchestrator observes what the owner asks for repeatedly
2. **After sessions:** New patterns are written as **individual files** in the patterns directory (see "Adding New Patterns" below)
3. **In future sessions:** The orchestrator reads this index and scans `~/.agents/prompts/agents/orchestrator-patterns/*.md`, applying all patterns WITHOUT being asked
4. **The goal:** Each session, the owner should need to ask for LESS because the orchestrator already knows
5. **Concurrency-safe:** Multiple agents can write new patterns simultaneously -- each creates its own file, no overwrites

## Directory Structure

```
~/.agents/prompts/agents/
  orchestrator-learned-patterns.md          ← THIS FILE (read-only index)
  orchestrator-patterns/                     ← Individual pattern files
    2026-04-03-00-00-01Z-orch-maximum-parallel-execution.md
    2026-04-03-00-00-02Z-orch-auto-deploy-after-impl.md
    ...
```

---

## Pattern Index

### BATCH_DELEGATION
- **P-001:** Maximum Parallel Execution -- Launch ALL non-conflicting tasks in parallel
- **P-002:** Auto-Deploy After Implementation -- Deploy immediately when tests pass
- **P-003:** Auto-Deploy Batching -- Batch 3-5 deploys instead of deploying after each WO

### CLEANUP
- **P-004:** Sweep for Untracked Work -- Scan for loose ends after every 3+ WO batch
- **P-005:** WO-INDEX Reconciliation -- Fix stale index entries after status changes
- **P-006:** Auto-Update STATE-OF-THE-PROJECT -- Update project state after 5+ WOs complete

### VERIFICATION
- **P-007:** Test Suite After Code Changes -- Run tests immediately after any src/ modification
- **P-008:** Live QA After Deploy -- Authenticated curl checks after every deploy

### BLOCKED_WO
- **P-009:** Prepare Owner-Blocked WOs for Instant Closure -- Scripts + action cards for owner
- **P-010:** Auth Cookie Acquisition -- Get sl_session cookie at session start

### SESSION_LIFECYCLE
- **P-011:** Session Handoff at End -- Comprehensive handoff with evidence links
- **P-012:** Continuous Motion -- Never idle; check WO-INDEX and launch unstarted work

### WORKSTREAM
- **P-013:** Full Workstream Creation -- Auto-scaffold proposal + WOs + dependency graph
- **P-014:** Build vs. Integrate Decision -- Research existing implementations before building

---

## Adding New Patterns

**Concurrency-safe protocol:** Each agent writes its own file. NEVER modify another agent's pattern file. NEVER modify this index file during a session -- it is updated separately.

### File Location

```
~/.agents/prompts/agents/orchestrator-patterns/
```

### File Naming Convention

```
{timestamp}-{agent-id-last4}-{slug}.md
```

Where:
- `{timestamp}` = output of `~/.agents/scripts/get-filename-prefix.sh` (YYYY-MM-DD-HH-MM-SSZ format)
- `{agent-id-last4}` = last 4 characters of the agent's session/process ID (or `orch` for the orchestrator itself) -- prevents collision at the same second
- `{slug}` = kebab-case description (e.g., `auto-deploy-after-impl`)

**Example filenames:**
```
2026-04-03-21-45-32Z-a4e5-auto-deploy-after-impl.md
2026-04-03-21-45-32Z-b7f2-sweep-untracked-work.md
2026-04-03-21-45-33Z-orch-batch-delegation.md
```

### Individual Pattern File Format

```markdown
---
id: P-NNN
category: BATCH_DELEGATION | CLEANUP | VERIFICATION | BLOCKED_WO | SESSION_LIFECYCLE | WORKSTREAM
trigger: "when X happens"
source_session: 2026-04-03
---

# P-NNN: Pattern Name

**Action:** What the orchestrator does
**Why:** What problem this solves
**Examples:** Concrete examples
```

### When to Add a Pattern

1. The owner asks for something you should have done automatically
2. Note it in the orchestration log: `### Pattern Observed: [description]`
3. Create a new pattern file in the directory using the naming convention above
4. Use the next sequential P-NNN number (scan existing files to find the highest)

**The test:** If the owner has to say it twice across sessions, it's a pattern. Add it.

### Rules

- **NEVER modify another agent's pattern file** -- only create new files
- **NEVER modify this index file during a session** -- index updates are a separate housekeeping task
- **One pattern per file** -- keeps diffs clean and prevents merge conflicts
- **Timestamps prevent collisions** -- even if two agents write at the same second, the agent-id suffix differentiates them
