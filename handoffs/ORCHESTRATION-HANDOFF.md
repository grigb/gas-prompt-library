# Orchestration Handoff Template

**This extends:** `~/.agents/prompts/handoffs/HANDOFF.md`

Use this template when handing off orchestrator context to a continuation orchestrator. This is NOT for general task handoffs - it's specifically for orchestration state transfer.

---

## TRIGGER PHRASES

Invoke this template when you encounter:
- "create handoff" (when operating as orchestrator)
- "hand off" (when operating as orchestrator)
- "handoff" (when operating as orchestrator)
- Mentioning `~/.agents/prompts/handoffs/HANDOFF.md` (in orchestrator context)
- Mentioning `~/.agents/prompts/handoffs/ORCHESTRATION-HANDOFF.md`
- "spawn continuation"
- "context limit" or "running low on context" (as orchestrator)
- "continue orchestration"

---

## ORCHESTRATION-SPECIFIC REQUIREMENTS

### 1. AGENTS.md Must Be Referenced FIRST

**Non-negotiable.** Every orchestration handoff prompt MUST start with:
```
Read AGENTS.md for context.
Then read PROJECT-RULES.md for onboarding.
```

This ensures the continuation orchestrator inherits project rules before reading orchestrator instructions.

### 2. Required Path References

Every orchestration handoff MUST include these paths:

| Path | Purpose |
|------|---------|
| `~/.agents/prompts/agents/agent-orchestrator.md` | Orchestrator behavioral instructions |
| Orchestration log path | Current state, task tracker, deferred decisions |
| Status beacon path (if exists) | Machine-parseable status for hierarchy |

### 3. DO NOT Duplicate Orchestrator Rules

Pass the PATH to `agent-orchestrator.md`, not its contents. This allows:
- Rules to be updated between handoffs
- Smaller prompt size
- Single source of truth

---

## ORCHESTRATION HANDOFF STRUCTURE

```markdown
---
agent_task_id: [AGENT_TASK_ID]
created: [YYYY-MM-DD-HH-MM-SSZ]
type: orchestration-handoff
orchestration_id: [orch-YYYY-MM-DD-HH-MM-SS-objective]
---

# Orchestration Handoff: [Objective]

## THE BIGGER PICTURE

**What This Orchestration Is Managing:**
[High-level objective - what the entire orchestration aims to accomplish]

**Current Batch/Phase:**
- Phase: [N of M]
- Batch: [name/number]
- Focus: [what this batch accomplishes]

**Completed Work:**
- [List major completed batches/tasks with outcomes]
- [Include task count: X/Y tasks completed]

**Pending Work:**
- [List remaining batches/tasks]
- [Include dependencies: "Batch 3 depends on Batch 2 verification"]

**Critical Blockers (if any):**
- [Blocker description] - Impact: [what's blocked] - Resolution: [action needed]

---

## PRIORITY NEXT ACTIONS FOR CONTINUATION

1. **[Action 1]** - [Why/Context]
   - Specifically: [detailed instruction]

2. **[Action 2]** - [Why/Context]

3. **[Action 3]** - [Why/Context]

---

## ORCHESTRATION STATE FILES

### Required Reading (In Order)
1. **Orchestrator Instructions:** `~/.agents/prompts/agents/agent-orchestrator.md`
2. **Orchestration Log:** `[FULL PATH to .dev/ai/orchestration/{timestamp}-orchestration-log.md]`
3. **Project Rules:** `AGENTS.md` (if not already read)

### Optional Context
- **Status Beacon:** `[FULL PATH to beacon.yaml, if exists]`
- **Work Order Index:** `.dev/ai/workorders/WO-INDEX.md`
- **Pending Sub-Agent Outputs:** `[list of .dev/ai/subtask-comms/*.md files to read]`

---

## PRODUCTION ACCESS (If Applicable)

**Include this section when orchestration involves server operations.**

Critical access commands the next orchestrator needs:

| Resource | Command |
|----------|---------|
| SSH to server | `ssh -i [KEY_PATH] [USER]@[HOST]` |
| Container access | `docker exec -it [CONTAINER] bash` |
| DB query | `[full command including password handling]` |
| Sync files | `rsync -avz -e "ssh -i [KEY]" [LOCAL] [REMOTE]` |
| Restart service | `[supervisorctl/systemctl command]` |

**Why this matters:** Sub-agents delegated by the continuation orchestrator won't have access to project docs or STATE-OF-THE-PROJECT.md context. Embedding commands here prevents "SSH denied" failures from missing key paths.

---

## DEFERRED DECISIONS (Pending Review)

| # | Decision | Default Applied | Risk | Reversible |
|---|----------|-----------------|------|------------|
| 1 | [topic] | [what was done] | LOW/MED | [how to undo] |

**User can override any decision in follow-up session.**

---

## TASK TRACKER SNAPSHOT

| Task | Status | Notes |
|------|--------|-------|
| T1 | completed | [outcome] |
| T2 | in_progress | [agent/output file] |
| T3 | pending | [dependency if any] |

---

**Agent Task ID:** [AGENT_TASK_ID]
```

---

## SPAWN COMMAND TEMPLATE

Use this ready-to-paste command to spawn the continuation orchestrator:

```python
Task(
    prompt="""You are the continuation orchestrator.

    READ THESE FILES IN ORDER:
    1. AGENTS.md (project rules)
    2. Orchestrator instructions: ~/.agents/prompts/agents/agent-orchestrator.md
    3. Orchestration log (YOUR CONTEXT): [FULL PATH TO LOG FILE]

    STATUS BEACON (if exists): [FULL PATH TO BEACON FILE]

    THE BIGGER PICTURE:
    - Managing: [objective]
    - Current phase: [N of M]
    - Completed: [X/Y tasks]
    - Next action: [specific next step]

    Your job: Continue this orchestration from where it stopped.
    Do NOT restart. Do NOT re-plan. Just continue executing.

    The orchestration log tells you exactly what to do next.
    """,
    run_in_background=True,
    model="opus"
)
```

---

## NEXT-SESSION PROMPT (Copy-Paste Ready)

```markdown
Read AGENTS.md for context.
Then read PROJECT-RULES.md for onboarding.

I'm continuing orchestration on [project-name].
Agent Task ID: [AGENT_TASK_ID] (preserve this ID in any handoffs you create)

READ IN ORDER:
1. Orchestrator instructions: ~/.agents/prompts/agents/agent-orchestrator.md
2. Orchestration log: [FULL ABSOLUTE PATH to orchestration log]

THE BIGGER PICTURE:
- Objective: [what we're accomplishing]
- Phase: [N of M] - [current phase name]
- Status: [X/Y tasks completed]
- Next: [immediate next action]

Continue executing from where the previous orchestrator stopped.
The log contains task tracker, deferred decisions, and execution history.
Do NOT re-plan or restart. Just continue.
```

---

## WHEN TO USE THIS VS BASE HANDOFF

| Situation | Template |
|-----------|----------|
| Orchestrator running out of context | ORCHESTRATION-HANDOFF.md |
| Orchestrator spawning continuation | ORCHESTRATION-HANDOFF.md |
| Sub-agent completing task | HANDOFF.md (base) |
| Any non-orchestrator handoff | HANDOFF.md (base) |
| Emergency/low-context orchestrator | ORCHESTRATION-HANDOFF.md (minimal version) |

---

## MINIMAL ORCHESTRATION HANDOFF (Low Context Mode)

When context is critically low, use this reduced format:

```markdown
---
agent_task_id: [AGENT_TASK_ID]
type: orchestration-handoff-emergency
---

# Orchestration Handoff (Emergency)

## IMMEDIATE NEXT ACTION
[Single most important next step]

## STATE FILES
- Log: [path]
- Beacon: [path if exists]

## TASK STATUS
- Completed: [count]
- Pending: [count]
- Blocked: [count with reasons]

---
Read: ~/.agents/prompts/agents/agent-orchestrator.md
Read: [log path]
Continue from where stopped.
```

---

## KEY DIFFERENCES FROM BASE HANDOFF

1. **Bigger Picture Section** - Orchestrators need high-level context about what they're coordinating, not just immediate actions

2. **State File References** - Must include orchestration log, beacon path, and sub-agent output paths

3. **Task Tracker Snapshot** - Quick reference for task status without reading full log

4. **Deferred Decisions Table** - Critical for continuity - next orchestrator needs to know what defaults were applied

5. **Spawn Command Template** - Ready-to-use Task() call for immediate continuation

6. **No Work Execution Context** - Orchestrators don't execute work, so handoffs focus on coordination state, not implementation details

---

## REMEMBER

- **The orchestration log IS your handoff context** - keep it updated throughout
- **Pass paths, not content** - let continuation read latest versions
- **AGENTS.md FIRST** - always reference before orchestrator instructions
- **Bigger picture matters** - continuation needs to understand what they're coordinating
- **Deferred decisions are critical** - next orchestrator must know what you decided without asking user

---

## ANTI-PATTERNS

**These are failure modes. Avoid them.**

### NEVER:
- Go IDLE when work orders remain (even if blocked)
- Report "no pending work" when WO-INDEX has READY items
- End session without updating orchestration log
- Treat a single blocker as "orchestration complete"
- Let context expire without creating handoff

### ALWAYS:
- Create handoff before session ends
- Preserve the bigger picture (objective, phase, remaining work)
- Include spawn command for continuation
- Update orchestration log incrementally, not just at end
- Distinguish between "task blocked" and "orchestration complete"

### Common Mistakes

| Mistake | Why It's Wrong | Correct Approach |
|---------|---------------|------------------|
| "STATUS: IDLE - SSH blocked" | Conflates blocker with completion | HANDOFF with blocker noted |
| "No pending work" when WOs remain | Ignores WO-INDEX | Check WO-INDEX before claiming done |
| Session ends without handoff | Context lost forever | Always create handoff |
| "Waiting for user" as final state | No continuation path | Create spawn command for next agent |
