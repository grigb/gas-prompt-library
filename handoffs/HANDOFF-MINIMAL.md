# Minimal Handoff Instructions

## ⚠️ CRITICAL: WHEN TO CREATE HANDOFFS

**CREATE handoff when:**
- ✅ Work is UNFINISHED and needs continuation
- ✅ You're stopping mid-task
- ✅ There are SPECIFIC NEXT ACTIONS for another agent
- ✅ **USER EXPLICITLY REQUESTS a handoff**, regardless of work completion status

**DO NOT create handoff when:**
- ❌ User explicitly says they don't want a handoff
- ❌ There are no actionable next steps AND user hasn't requested context preservation

**Critical Rule:** Always respect explicit user requests for handoffs. If user says "create a handoff" or "your work qualifies as a necessary handoff", create the handoff regardless of whether work appears complete. Context preservation for ongoing systems takes precedence over completion status.

**If work is complete AND user hasn't requested a handoff:** Use audit/accomplishment instead.

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
→ **USE LOW CONTEXT MODE** (skip to that section, don't load additional prompts)

## LOW CONTEXT MODE
**Priority: Give next agent their immediate action items**

### Immediate Actions (Save After Each):
1. **Create file**:
   ```bash
   mkdir -p .dev/ai/handoffs/
   TIMESTAMP=$(~/.agents/scripts/get-filename-prefix.sh)
   FILE=".dev/ai/handoffs/${TIMESTAMP}-handoff-emergency.md"
   ```

2. **Write NEXT ACTIONS FIRST** (what to do, not what was done):
   ```markdown
   # Emergency Handoff - [timestamp]

   ## IMMEDIATE NEXT ACTIONS
   1. [Action 1] - [Why it matters]
   2. [Action 2] - [Why it matters]
   3. [Action 3] - [Why it matters]

   ## Outstanding Work
   - WO-xxx: [Status] - Next step: [specific action]
   - WO-yyy: [Status] - Blocked by: [blocker]

   ## Current State (one line)
   Was working on: [15 words max]
   ```
   **SAVE FILE NOW**

3. **STOP HERE** in low context mode. Focus on actions, not history.

## NORMAL MODE
**Use when context is adequate**

### Step 1: ACTION-FIRST Structure
```markdown
# Handoff: [Project] - [YYYY-MM-DD-HH-MM-SS]

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

## Full Session Details (if audit exists)
[ONLY include if an audit was created just before this handoff]
For complete context, see: .dev/ai/audits/[timestamp]-conversation-summary.md
```

### Step 2: Keep It Lean (For Simple Tasks)
- Lead with actions (what to do next)
- Support with minimal context (why/how)
- Save "what we did" for audit files, not handoffs
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

After creating handoff, generate copy-paste prompt:

```markdown
I'm picking up work on [project-name].

1. Read the handoff at: [FULL ABSOLUTE PATH to handoff file]
2. Review project rules in [FULL PATH to AGENTS.md / CLAUDE.md]
3. BEGIN EXECUTING Priority Next Steps immediately

The handoff is the complete action plan. Start work now - do not ask for confirmation or additional input. These actions have been reviewed and approved.
```

## Decision Tree
```
Low Context? → EMERGENCY MODE → Actions only
Normal Context? → ACTION-FIRST STRUCTURE
Need Why/How? → Load Handoff-Detailed.md for context sections
Size > 50 lines? → Moving audit/history to separate doc
```

## Remember
- **Actions first, history last** (or not at all)
- Next agent needs a todo list, not a diary
- Context is "why you need to do this", not "what I did"
- Save comprehensive session records to audit files
- **Reference documents throughout:** Include full absolute paths inline where relevant to actions
- **Balance:** Enough context for intelligent execution, not so minimal agent must guess