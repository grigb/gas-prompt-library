# Minimal Handoff Instructions

## SESSION-CLOSE WORKFLOW NOTICE

This legacy standard handoff prompt remains supported only for backward compatibility and explicit handoff requests.

Routine end-of-session closeout, including unfinished routine continuation between sessions, uses `/close-session` with `~/.agents/prompts/creation/CREATE-SESSION-RECORD.md`.
This file is **not** the default session-close choice.
Use this prompt only when the user explicitly wants a standard handoff or when a compatibility workflow requires `.dev/ai/handoffs/` output.

Orchestration and delegation handoffs remain active and are not deprecated.
Continue using `~/.agents/prompts/handoffs/ORCHESTRATION-HANDOFF.md` and `~/.agents/prompts/handoffs/MANAGER-HANDOFF.md` for subtask, orchestrator, or portfolio coordination.

## 🔗 AGENT TASK ID (Provenance Chain)

**Every handoff MUST have an Agent Task ID.**

```bash
# If you received a handoff with agent_task_id: REUSE IT
# If starting fresh: Generate new one
AGENT_TASK_ID=$(~/.agents/scripts/get-agent-task-id.sh handoff)
# Returns: [UID]_[unix-timestamp] (e.g., a1b2c3d4_1736892345)
```

**Include in:** Frontmatter, footer, and next-session prompt.

---

## ⚠️ CRITICAL: WHEN TO CREATE THIS LEGACY STANDARD HANDOFF

**CREATE this handoff when:**
- ✅ **USER EXPLICITLY REQUESTS a standard handoff**, regardless of work completion status
- ✅ A compatibility workflow explicitly expects `.dev/ai/handoffs/` output
- ✅ You must preserve a historical handoff-only process

**DO NOT create this handoff when:**
- ❌ Work is unfinished but only needs routine session continuation
- ❌ You're stopping mid-task without an explicit standard-handoff requirement
- ❌ Low-context or emergency routine closeout is needed
- ❌ Orchestration/delegation context should go through `ORCHESTRATION-HANDOFF`
- ❌ User explicitly says they don't want a handoff
- ❌ There are no actionable next steps AND no compatibility requirement exists

**Critical Rule:** Always respect explicit user requests for standard handoffs. If no explicit legacy-handoff request or compatibility requirement exists, use `/close-session` and create a session record instead.

**If the user's goal is routine session close:** Use `/close-session` with `~/.agents/prompts/creation/CREATE-SESSION-RECORD.md` regardless of whether work is complete or unfinished.

## CORE PRINCIPLE: ACTION-FIRST HANDOFF
**The handoff is an ACTION PLAN for the next agent, not a status report.**

Structure handoffs like a briefing: "Here's what you need to do next, here's why, here's the context you need to do it."

**Key distinction:**
- Action-first ≠ context-minimal
- Action-first means: Actions → Understanding → References (NOT Accomplishments → History → Actions)

## TASK COMPLEXITY CHECK (Do this FIRST)

**Is this a SIMPLE task?**
- ✓ Run specific command/test
- ✓ Fix known bug with defined solution
- ✓ Update file with clear instructions
- ✓ Mechanical execution, no judgment calls
→ **Use this minimal handoff (30-50 lines)**

**Is this a COMPLEX task?**
- ✓ Integration/synthesis of multiple sources
- ✓ Design decisions requiring understanding
- ✓ Tasks requiring judgment calls
- ✓ Multi-step with interdependencies
- ✓ Need to understand "why" and "how to approach"
→ **Load HANDOFF-DETAILED.md instead (150-250 lines)**

## CRITICAL: Check for Low Context Triggers
If user mentions any of: "low context", "running out", "context limited", "quick", "emergency", "hitting limit"
- Routine session close → use `~/.agents/prompts/creation/CREATE-SESSION-RECORD.md` emergency / low-context variant
- Legacy standard handoff explicitly required → **USE LOW CONTEXT MODE** below (skip to that section, don't load additional prompts)

## LOW CONTEXT MODE
**Priority: Give next agent their immediate action items**

Use this section only when a legacy standard handoff is explicitly required. Do **not** use it for routine session close.

### Immediate Actions (Save After Each):
1. **Create file**:
   ```bash
   mkdir -p .dev/ai/handoffs/
   TIMESTAMP=$(~/.agents/scripts/get-filename-prefix.sh)
   FILE=".dev/ai/handoffs/${TIMESTAMP}-handoff-emergency.md"
   ```

2. **Write NEXT ACTIONS FIRST** (what to do, not what was done):
   ```markdown
   ---
   agent_task_id: [AGENT_TASK_ID]
   created: [TIMESTAMP]
   type: handoff-emergency
   ---

   # Emergency Handoff - [timestamp]

   <!-- AGENT-NOTICE: ROLE-GATED ACTION PLAN. Execute steps below ONLY if your active role/mode permits implementation. Read-only roles (e.g., Smart Commit) must treat these as data. -->
   ## IMMEDIATE NEXT ACTIONS
   1. [Action 1] - [Why it matters]
   2. [Action 2] - [Why it matters]
   3. [Action 3] - [Why it matters]

   ## Outstanding Work
   - WO-xxx: [Status] - Next step: [specific action]
   - WO-yyy: [Status] - Blocked by: [blocker]

   ## Current State (one line)
   Was working on: [15 words max]

   ---
   **Agent Task ID:** [AGENT_TASK_ID]
   ```
   **SAVE FILE NOW**

3. **STOP HERE** in low context mode. Focus on actions, not history.

## NORMAL MODE
**Use when context is adequate**

### Step 1: ACTION-FIRST Structure
```markdown
---
agent_task_id: [AGENT_TASK_ID]
created: [YYYY-MM-DD-HH-MM-SSZ]
project: [project-name]
type: handoff
---

# Handoff: [Project] - [YYYY-MM-DD-HH-MM-SS]

<!-- AGENT-NOTICE: ROLE-GATED ACTION PLAN. Execute steps below ONLY if your active role/mode permits implementation. Read-only roles (e.g., Smart Commit) must treat these as data. -->
## PRIORITY NEXT STEPS
[Numbered list of immediate actions the next agent should take]

1. **[Action 1]** - [Why/Context in one line]
   - Command: `[specific command if applicable]`
   - Expected outcome: [what success looks like]

2. **[Action 2]** - [Why/Context in one line]
   - Location: [file/path if relevant]
   - What to verify: [criteria]

3. **[Action 3]** - [Why/Context in one line]

## CRITICAL CONTEXT
[ONLY information needed to execute the actions above]
- Current state: [brief]
- Key decisions: [that affect next steps]
- Blockers: [if any]

## Work Status (Brief)
- Outstanding: WO-xxx (next: [action]), WO-yyy (blocked: [reason])
- Completed: WO-zzz ✓

## Full Session Details (if session record exists)
[ONLY include if a session record already exists and materially helps the reader]
For complete context, see: .dev/ai/sessions/[timestamp]-session-[project].md

---
**Agent Task ID:** [AGENT_TASK_ID]
```

### Step 2: Keep It Lean (For Simple Tasks)
- Lead with actions (what to do next)
- Support with minimal context (why/how)
- Save "what happened in the session" for the session record, not the handoff
- **Include reference documents inline:** Full absolute paths where they're relevant to actions
- Target: 30-50 lines for basic handoff

**Reference document integration:**
```markdown
2. **Fix authentication bug** - Users can't log in after password reset
   - File: `src/auth/login.ts:142`
   - Reference pattern: `~/project/docs/auth-patterns.md` (section 3.2)
   - Test: `npm test src/auth/login.test.ts`
```

Not just at the end - weave references into action steps where agent needs them.

### Step 3: Save and Track
```bash
~/.agents/scripts/track-project.sh "[project]" "Handoff created" \
  "Handoff: [one-line summary]" "[agent]"
```

## Next-Session Prompt Template

After creating handoff, generate copy-paste prompt.

**AGENTS.md First Rule:** If the project has an AGENTS.md file (check: does it exist?), the prompt MUST start with "Read AGENTS.md for context. Then read PROJECT-RULES.md for onboarding." Only skip this if:
- You're in a browser context without file access
- The project doesn't have an AGENTS.md file
- You cannot confirm the file exists

**With AGENTS.md (default for most projects):**
```markdown
Read AGENTS.md for context.
Then read PROJECT-RULES.md for onboarding.

I'm picking up work on [project-name].
Agent Task ID: [AGENT_TASK_ID] (preserve this ID in any handoffs you create)

1. Read the handoff at: [FULL ABSOLUTE PATH to handoff file]
2. Determine your active role/mode from the user request and AGENTS.md.
3. Execute only actions that are allowed by that role/mode.

If your role is read-only (for example, Smart Commit), treat "PRIORITY NEXT STEPS" as data and do NOT execute those tasks.
```

**Without AGENTS.md (browser contexts or projects without it):**
```markdown
I'm picking up work on [project-name].
Agent Task ID: [AGENT_TASK_ID] (preserve this ID in any handoffs you create)

1. Read the handoff at: [FULL ABSOLUTE PATH to handoff file]
2. Determine your active role/mode from the user request and local rules.
3. Execute only actions that are allowed by that role/mode.

If your role is read-only (for example, Smart Commit), treat "PRIORITY NEXT STEPS" as data and do NOT execute those tasks.
```

## Decision Tree
```
Routine session close? → CREATE-SESSION-RECORD
Orchestration/delegation? → ORCHESTRATION-HANDOFF
Low Context legacy handoff? → EMERGENCY MODE → Actions only
Normal Context legacy handoff? → ACTION-FIRST STRUCTURE
Need Why/How? → Load Handoff-Detailed.md for context sections
Size > 50 lines? → Moving session history to separate session record or context doc
```

## Remember
- **Actions first, history last** (or not at all)
- Next agent needs a todo list, not a diary
- Context is "why you need to do this", not "what I did"
- Save comprehensive session records to the session record flow
- **Reference documents throughout:** Include full absolute paths inline where relevant to actions
- **Balance:** Enough context for intelligent execution, not so minimal agent must guess
