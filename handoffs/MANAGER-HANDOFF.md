---
name: manager-handoff
description: |
  Manager-to-manager handoff template for transferring portfolio orchestration context.
  Use when a manager orchestrator needs to hand off to a continuation manager.
applies_to: manager-orchestrator
extends: ORCHESTRATION-HANDOFF.md
---

# Manager Orchestration Handoff Template

**This extends:** `~/.agents/prompts/handoffs/ORCHESTRATION-HANDOFF.md`

Use this template when handing off manager orchestrator context to a continuation manager. This is for portfolio-level handoffs, NOT for standard orchestrator or worker handoffs.

---

## TRIGGER PHRASES

Invoke this template when you encounter:
- "create handoff" (when operating as manager orchestrator)
- "manager handoff"
- "portfolio handoff"
- Mentioning `~/.agents/prompts/handoffs/MANAGER-HANDOFF.md`
- "spawn continuation manager"
- "context limit" or "running low on context" (as manager orchestrator)
- "continue managing"

---

## MANAGER-SPECIFIC REQUIREMENTS

### 1. AGENTS.md Must Be Referenced FIRST

**Non-negotiable.** Every manager handoff prompt MUST start with:
```
Read AGENTS.md
```

This ensures the continuation manager inherits project rules before reading manager instructions.

### 2. Required Path References

Every manager handoff MUST include these paths:

| Path | Purpose |
|------|---------|
| `~/.agents/prompts/agents/agent-manager-orchestrator.md` | Manager behavioral instructions |
| Manager log path | Portfolio state, decisions made, child orchestrations |
| Manager beacon path (if exists) | Aggregated status for hierarchy |

### 3. DO NOT Duplicate Manager Rules

Pass the PATH to `agent-manager-orchestrator.md`, not its contents. This allows:
- Rules to be updated between handoffs
- Smaller prompt size
- Single source of truth

---

## MANAGER HANDOFF STRUCTURE

```markdown
---
agent_task_id: [AGENT_TASK_ID]
created: [YYYY-MM-DD-HH-MM-SSZ]
type: manager-handoff
manager_id: [mgr-YYYY-MM-DD-HH-MM-SS-scope]
---

# Manager Handoff: [Portfolio/Scope]

## IMMEDIATE ACTION REQUIRED

**What the next manager should do FIRST:**

1. **[Action 1]** - [Why urgent]
   - Specifically: [detailed instruction]
   - Beacon to check: [path if relevant]

2. **[Action 2]** - [Why/Context]

3. **[Action 3]** - [Why/Context]

---

## PORTFOLIO STATE

**Manager:** [manager_id]
**Scope:** [portfolio description]
**Time:** [current timestamp]

### Health Summary

| Health | Count | Orchestrations |
|--------|-------|----------------|
| Green  | [N]   | [orch-ids]     |
| Yellow | [N]   | [orch-ids]     |
| Red    | [N]   | [orch-ids]     |

**Overall Portfolio Health:** [green/yellow/red] (worst child determines health)

### Progress Summary

| Metric | Count |
|--------|-------|
| Total Orchestrations | [N] |
| On Track | [N] |
| At Risk | [N] |
| Blocked | [N] |
| Completed | [N] |

---

## ACTIVE ORCHESTRATIONS

| ID | Project | Health | Progress | On Track | Blockers |
|----|---------|--------|----------|----------|----------|
| orch-[id] | [name] | [color] | [%] | Yes/No | [brief or None] |
| orch-[id] | [name] | [color] | [%] | Yes/No | [brief or None] |
| orch-[id] | [name] | [color] | [%] | Yes/No | [brief or None] |

**Beacon paths:**
- `orch-[id]`: `.dev/ai/orchestration/[id]-beacon.yaml`
- `orch-[id]`: `.dev/ai/orchestration/[id]-beacon.yaml`

---

## ATTENTION REQUIRED

**Orchestrations needing intervention (priority order):**

1. **[orch-id]** - [Issue summary]
   - Health: [color]
   - Duration blocked: [time]
   - Recommended action: [what to do]
   - Beacon: [path]

2. **[orch-id]** - [Issue summary]
   - Health: [color]
   - Escalation received: [yes/no]
   - Recommended action: [what to do]

---

## CROSS-ORCHESTRATION CONFLICTS

**Resource conflicts between orchestrations:**

| Conflict | Orchestrations | Resource | Status | Resolution |
|----------|---------------|----------|--------|------------|
| [id] | orch-A vs orch-B | [shared resource] | [pending/resolved] | [action taken or needed] |

**Active conflicts requiring resolution:**
- [Conflict description and recommended resolution]

**Resolved conflicts this session:**
- [Conflict] - Resolution: [what was decided] - Rationale: [why]

---

## DECISIONS MADE

### Priority Injections Issued

| Timestamp | To Orchestration | Action | Reason | Acknowledged |
|-----------|-----------------|--------|--------|--------------|
| [time] | [orch-id] | [reprioritize/defer/escalate] | [why] | [yes/no/pending] |

### Escalations Handled

| Timestamp | From Orchestration | Issue | Resolution |
|-----------|-------------------|-------|------------|
| [time] | [orch-id] | [escalation description] | [how resolved] |

### Deferred Decisions

| # | Decision | Default Applied | Risk | Reversible |
|---|----------|-----------------|------|------------|
| 1 | [topic] | [what was done] | LOW/MED | [how to undo] |

**User can override any decision in follow-up session.**

---

## MANAGER STATE FILES

### Required Reading (In Order)
1. **Manager Instructions:** `~/.agents/prompts/agents/agent-manager-orchestrator.md`
2. **Manager Log:** `[FULL PATH to .dev/ai/orchestration/{manager-id}-manager-log.md]`
3. **Project Rules:** `AGENTS.md` (if not already read)

### Child Orchestration Beacons
- `[FULL PATH to each active child beacon]`

### Optional Context
- **Manager Beacon:** `[FULL PATH to manager beacon, if exists]`
- **Work Order Index:** `.dev/ai/workorders/WO-INDEX.md`

---

## MANAGER LOG REFERENCE

**Full manager log:** `[FULL PATH to .dev/ai/orchestration/{manager-id}-manager-log.md]`

The log contains:
- Complete execution history
- All decisions and rationale
- Child orchestration launch commands
- Escalation handling details
- Priority injection records

---

## CONTINUATION SPAWN COMMAND

Use this ready-to-paste command to spawn the continuation manager:

```python
Task(
    prompt="""You are the continuation manager orchestrator.

    READ THESE FILES IN ORDER:
    1. AGENTS.md (project rules)
    2. Manager instructions: ~/.agents/prompts/agents/agent-manager-orchestrator.md
    3. Manager log (YOUR CONTEXT): [FULL PATH TO MANAGER LOG FILE]

    MANAGER BEACON (if exists): [FULL PATH TO MANAGER BEACON FILE]

    PORTFOLIO STATE:
    - Managing: [portfolio scope/objective]
    - Active orchestrations: [N]
    - Health: [N] green, [N] yellow, [N] red
    - On track: [N], At risk: [N]
    - Immediate attention: [list of orch-ids needing intervention]

    CHILD BEACONS TO READ:
    - [path to beacon 1]
    - [path to beacon 2]
    - [path to beacon 3]

    Your job: Continue managing this portfolio from where it stopped.
    Do NOT re-launch orchestrators that are already running.
    Read their current beacons and continue monitoring.
    Handle any pending escalations or interventions first.

    The manager log tells you exactly what to do next.
    """,
    run_in_background=True,
    model="opus"
)
```

---

## NEXT-SESSION PROMPT (Copy-Paste Ready)

```markdown
Read AGENTS.md

I'm continuing manager orchestration on [portfolio/scope].
Agent Task ID: [AGENT_TASK_ID] (preserve this ID in any handoffs you create)

READ IN ORDER:
1. Manager instructions: ~/.agents/prompts/agents/agent-manager-orchestrator.md
2. Manager log: [FULL ABSOLUTE PATH to manager log]

PORTFOLIO STATE:
- Scope: [portfolio description]
- Active orchestrations: [N] ([N] green, [N] yellow, [N] red)
- On track: [N], At risk: [N]
- Immediate action: [most urgent next step]

CHILD BEACONS:
[List all active child beacon paths]

Continue managing from where the previous manager stopped.
The log contains portfolio state, decisions made, and child orchestration status.
Do NOT re-launch running orchestrators. Read their beacons and continue monitoring.
Handle any pending escalations or interventions FIRST.
```

---

## MINIMAL MANAGER HANDOFF (Low Context Mode)

When context is critically low, use this reduced format:

```markdown
---
agent_task_id: [AGENT_TASK_ID]
type: manager-handoff-emergency
---

# Manager Handoff (Emergency)

## IMMEDIATE NEXT ACTION
[Single most important thing - usually an intervention or escalation]

## STATE FILES
- Manager log: [path]
- Manager beacon: [path if exists]

## PORTFOLIO STATUS
- Active: [count] orchestrations
- Green: [count] | Yellow: [count] | Red: [count]
- Needing intervention: [orch-ids]

## CHILD BEACONS
[List all active child beacon paths]

---
Read: ~/.agents/prompts/agents/agent-manager-orchestrator.md
Read: [manager log path]
Continue from where stopped. Handle interventions first.
```

---

## WHEN TO USE THIS VS OTHER HANDOFFS

| Situation | Template |
|-----------|----------|
| Manager running out of context | MANAGER-HANDOFF.md |
| Manager spawning continuation | MANAGER-HANDOFF.md |
| Orchestrator handoff (non-manager) | ORCHESTRATION-HANDOFF.md |
| Worker/sub-agent handoff | HANDOFF.md (base) |
| Any non-manager/orchestrator handoff | HANDOFF.md (base) |

---

## KEY DIFFERENCES FROM ORCHESTRATION HANDOFF

1. **Portfolio State Section** - Aggregated view across all child orchestrations

2. **Health Summary** - Green/yellow/red counts with orchestration IDs

3. **Active Orchestrations Table** - Status of each child orchestrator

4. **Attention Required Section** - Priority-ordered list of orchestrations needing intervention

5. **Cross-Orchestration Conflicts** - Resource conflicts between children

6. **Decisions Made** - Priority injections and escalation handling records

7. **Child Beacon References** - All child beacon paths for continuation

8. **No Task Tracker** - Managers track orchestrations, not individual tasks

---

## ANTI-PATTERNS

**These are failure modes. Avoid them.**

### NEVER:
- Re-launch orchestrators that are already running
- Micromanage task-level details (that's the orchestrator's job)
- Ignore escalations from child orchestrators
- Let portfolio health degrade without intervention
- End session without updating manager log and creating handoff

### ALWAYS:
- Create handoff before session ends
- Include all child beacon paths
- Document decisions and priority injections
- Handle escalations before ending session
- Aggregate health status accurately (worst child = your health)

### Common Mistakes

| Mistake | Why It's Wrong | Correct Approach |
|---------|---------------|------------------|
| Re-launching running orchestrators | Duplicates work, wastes resources | Read beacons, continue monitoring |
| Ignoring yellow health | Yellow becomes red | Intervene early |
| Missing child beacon paths | Continuation can't find state | List all beacon paths explicitly |
| "All green, done" | Orchestrations still running | Monitor until completion |
| Delegating to workers directly | Violates manager role | Delegate to orchestrators only |

---

**Agent Task ID:** [AGENT_TASK_ID]
```

---

## REMEMBER

- **The manager log IS your handoff context** - keep it updated throughout
- **Pass paths, not content** - let continuation read latest versions
- **Portfolio health = worst child health** - aggregate accurately
- **Handle escalations FIRST** - pending escalations are urgent
- **List ALL child beacon paths** - continuation needs to find them
- **You coordinate orchestrators, not workers** - maintain abstraction level
