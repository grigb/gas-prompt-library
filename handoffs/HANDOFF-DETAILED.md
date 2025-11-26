# Detailed Handoff Instructions
**ONLY loaded for COMPLEX tasks requiring understanding before execution**

## ⚠️ CRITICAL: WHEN TO CREATE HANDOFFS

**CREATE handoff when:**
- ✅ Work is UNFINISHED and needs continuation
- ✅ Complex task is partially complete
- ✅ There are SPECIFIC NEXT ACTIONS requiring context
- ✅ **USER EXPLICITLY REQUESTS a handoff**, regardless of work completion status

**DO NOT create handoff when:**
- ❌ User explicitly says they don't want a handoff
- ❌ There are no actionable next steps AND user hasn't requested context preservation

**Critical Rule:** Always respect explicit user requests for handoffs. If user says "create a handoff" or "your work qualifies as a necessary handoff", create the handoff regardless of whether work appears complete. Context preservation for ongoing systems takes precedence over completion status.

**If work is complete AND user hasn't requested a handoff:** Use audit/accomplishment instead.

## CORE PRINCIPLE: CONTEXT SERVES ACTION
All context sections must answer: "What does the next agent need to know to take the next actions?"

**This detailed structure is for COMPLEX tasks:**
- Integration/synthesis of multiple sources
- Design decisions requiring understanding
- Tasks requiring judgment calls and strategy
- Multi-step work with interdependencies

**DO NOT include:**
- Detailed summaries of what was completed (save for audit files)
- Session chronologies (save for audit files)
- Extensive file listings (reference specific files only)
- Celebratory status updates (focus on what's left to do)

## When to Add Context Sections
Add context ONLY when it directly enables next actions:

- **WHY** an action is needed (decisions that create work)
- **HOW** to approach an action (strategy, method, technical constraints)
- **WHAT** will block progress (dependencies, prerequisites, pitfalls)
- **WHERE** to find information needed (specific files/docs with full absolute paths)

## Extended Sections for Complex Tasks

### Background Section (WHY this matters)
**2-3 paragraphs explaining problem and solution**
```markdown
## BACKGROUND: Why This Integration/Design/Task Matters

**The Problem:**
[What problem are we solving? Why does it exist? What's the impact?]

**The Solution:**
[What approach are we taking? Why this approach?]

**Current State:**
[Where are we now? What exists? What's missing?]
```

### Understanding Inputs Section (WHAT you're working with)
**For integration/synthesis tasks: Explain each component**
```markdown
## UNDERSTANDING THE INPUTS

**Component A** (size/location at `/full/absolute/path/to/component-a.md`)
- Contains: [key content summary]
- Strong on: [areas of strength]
- Weak on: [gaps or limitations]
- Reference for details: `/full/absolute/path/to/component-a.md`

**Component B** (size/location at `/full/absolute/path/to/component-b.md`)
- Contains: [key content summary]
- Strong on: [areas of strength]
- Weak on: [gaps or limitations]
- Reference for details: `/full/absolute/path/to/component-b.md`

**Relationship:**
- Complementary because: [how they work together]
- Overlapping on: [where they cover same ground - must synthesize]
- Distinct in: [unique value of each]
```

### Strategy Section (HOW to approach)
**Layered approach, method, critical principles**
```markdown
## INTEGRATION/IMPLEMENTATION STRATEGY

**Method: [e.g., Layered Integration, Test-Driven, Iterative Refinement]**

**Layer 1 ([from Source A]):**
- Keep: [what to preserve]
- Why: [rationale]

**Layer 2 ([from Source B]):**
- Add: [what to integrate]
- Where: [how to fit it in]

**Layer 3 (Synthesize Overlaps):**
- Both cover: [topic]
- Approach: [how to combine without duplication]

**Reference:** Detailed strategy at `/full/absolute/path/to/strategy-doc.md`
```

### Execution Prerequisites
**Information needed BEFORE starting next actions**
```markdown
## Prerequisites for Next Steps
- Action 1 requires: [specific file/state/dependency]
  - File location: `/full/absolute/path/to/required-file.md`
- Action 2 needs: [API key/permission/configuration]
  - Config reference: `/full/absolute/path/to/config-guide.md`
- Action 3 blocked until: [condition met]
```

### Technical Context
**Implementation details that guide approach**
```markdown
## Technical Context
- Architecture decision: Using [X] because [constraint/requirement]
  - Architecture doc: `/full/absolute/path/to/architecture.md`
- Key constraint: [limitation that affects how to implement]
- Integration point: [system/API that must be considered]
  - Integration guide: `/full/absolute/path/to/integration-guide.md`
```

### Decisions That Create Work
**Only include if they generate new actions**
```markdown
## Active Decisions
- Chose [X] approach → Next: implement [specific action]
- Decided to split [Y] → Next: create WO for [component]
- Postponed [Z] until [date] → Next: review on [trigger]
```

### Potential Pitfalls Section (WHAT to avoid)
**3-5 common mistakes with prevention strategies**
```markdown
## POTENTIAL PITFALLS

1. **[Pitfall name]** - [What could go wrong]
   - Why it happens: [common cause]
   - How to avoid: [specific prevention]
   - Reference: `/full/absolute/path/to/lessons-learned.md` (if applicable)

2. **[Pitfall name]** - [What could go wrong]
   - Resolution: [how to handle if it happens]

3. **[Pitfall name]** - [What could go wrong]
   - Check: [validation to prevent this]
```

### Success Criteria Section (HOW to know you're done)
**Test cases and validation steps**
```markdown
## SUCCESS CRITERIA

**Test:** [Concrete example to validate work]
- Example: "Write complete decision for 'Use SQLite for MVP' using ONLY Master guide"

**Must provide/include:**
- ✓ [Criterion 1] - [what this looks like]
- ✓ [Criterion 2] - [what this looks like]
- ✓ [Criterion 3] - [what this looks like]

**Validation steps:**
1. [Step to verify quality]
2. [Step to verify completeness]
3. [Step to verify nothing was lost]

**Reference:** Test examples at `/full/absolute/path/to/test-examples.md`
```

### Blockers & Unblocking Actions
**Focus on what to do about blockers**
```markdown
## Blockers & How to Resolve
- WO-xxx blocked by [dependency] → Action: contact [person/team]
  - Dependency doc: `/full/absolute/path/to/dependency-info.md`
- WO-yyy needs [approval] → Action: draft proposal for review
  - Approval process: `/full/absolute/path/to/approval-guide.md`
- WO-zzz waiting on WO-xxx → Action: start WO-aaa in parallel
```

### Critical State Information
**Only what affects execution, not comprehensive status**
```markdown
## Current State (Execution-Critical)
- Files modified but uncommitted: [list] - commit before next step
- Tests currently failing: [specific test] - must fix before deploying
- Feature flag state: [flag=value] - affects behavior of [feature]
```

### Discovery-Driven Actions
**New information that creates new work**
```markdown
## New Actions from Discoveries
- Found [issue] → Action: create WO to address [specific fix]
- Discovered [pattern] → Action: refactor [component] using [approach]
- Learned [constraint] → Action: update [doc/design] before proceeding
```

### Essential References
**Links to information needed for next actions - FULL ABSOLUTE PATHS**
```markdown
## REFERENCES

**For Understanding:**
- Component A details: `/full/absolute/path/to/component-a.md`
- Component B details: `/full/absolute/path/to/component-b.md`
- Overall strategy: `/full/absolute/path/to/strategy-doc.md`

**For Execution:**
- Action 1 guide: `/full/absolute/path/to/action-1-guide.md` (section 3)
- Action 2 template: `/full/absolute/path/to/template.md`
- Validation examples: `/full/absolute/path/to/test-cases.md`

**For Context:**
- Full session audit: `/full/absolute/path/.dev/ai/audits/[timestamp]-conversation-summary.md`
- Prior work orders: `/full/absolute/path/.dev/ai/workorders/WO-xxx.md`
- Related decisions: `/full/absolute/path/docs/decisions/[decision].md`

**Critical:** Include full absolute paths, not relative paths. Future agents need exact locations.
```

## Size Management Rules

### If Handoff Exceeds 250 Lines:
**Even complex tasks shouldn't need more than 250 lines. Refocus.**

1. **Review and cut:**
   - Remove "what we did" summaries → save to audit file
   - Remove exhaustive file listings → reference specific files only
   - Check for redundancy in explanations

2. **For truly massive context:**
   Create separate context document and reference it:
   ```markdown
   ## Extended Context
   See: `/full/absolute/path/.dev/ai/handoffs/[timestamp]-context.md`
   ```

3. **Handoff should contain (even for complex tasks):**
   - Next actions (numbered, prioritized)
   - Understanding needed (WHAT you're working with)
   - Strategy (HOW to approach)
   - Pitfalls (WHAT to avoid)
   - Success criteria (HOW to validate)
   - References with full absolute paths

**Target for complex tasks: 150-250 lines**
**Target for simple tasks: 30-50 lines (use HANDOFF-MINIMAL.md)**

### When History Matters:
Move comprehensive session records to audit files:
```bash
# Use the audit creation prompt for full session documentation
~/.agents/prompts/creation/CREATE-AUDITABLE-RECORD.md
```

## Work Order Integration

### Outstanding WOs in Handoff:
```markdown
## Outstanding Work
- WO-xxx: [one-line status] → **Next:** [specific action to take]
- WO-yyy: [one-line status] → **Blocked:** [blocker + how to unblock]
```

### When to Create New WOs:
Create WOs for discovered incomplete work, then **reference them in next actions**:
1. Create WO file with full task details
2. Add to handoff: "Next: Execute WO-xxx (see .dev/ai/workorders/...)"

## Handoff Completeness Checklist

Before finalizing, verify handoff answers:

- [ ] **What should I do first?** (clear priority action)
- [ ] **What do I need to know to do it?** (minimal context)
- [ ] **What will block me?** (prerequisites, dependencies)
- [ ] **Where do I find more info?** (specific file references)
- [ ] **What's the current state?** (one-line status, not detailed history)

**NOT required:**
- ❌ Comprehensive "what we did" sections
- ❌ Celebratory status updates
- ❌ Extensive file modification lists
- ❌ Chronological session narrative

## Progressive Save Strategy

In case of context exhaustion:
```bash
# Save ACTIONS first
cat > $FILE << 'EOL'
## PRIORITY NEXT STEPS
1. [Action]
2. [Action]
EOL

# Then add context if room
cat >> $FILE << 'EOL'
## Critical Context
[Minimal context]
EOL
```

## Final Validation for Complex Task Handoffs

Handoff quality test - Can the next agent:

1. **Start work immediately?** (actions are clear, specific, prioritized)
2. **Understand what they're working with?** (inputs/components explained)
3. **Know how to approach it?** (strategy/method provided)
4. **Avoid common mistakes?** (pitfalls flagged with prevention)
5. **Validate success?** (test cases and criteria defined)
6. **Find needed information?** (full absolute paths to all references)

**Balance test:**
- Too minimal: Agent makes wrong judgment calls, loses content, misses approach
- Too detailed: Agent drowns in history, can't find the actions
- Just right: Agent understands task, has strategy, can execute intelligently

If any question = "no" → add that specific info.
If all questions = "yes" → stop adding.

**Remember:** For complex tasks, 150-250 lines is expected and appropriate. Don't over-minimize.

## Next-Session Prompt for Complex Tasks

After creating detailed handoff, generate copy-paste prompt:

```markdown
I'm picking up work on [project-name] - complex integration/synthesis task.

1. Read the COMPLETE handoff at: [FULL ABSOLUTE PATH to handoff file]
2. Read it entirely - it contains Background, Strategy, Pitfalls, and Success Criteria
3. Review project rules in [FULL PATH to AGENTS.md / CLAUDE.md]
4. BEGIN EXECUTING Priority Next Steps immediately following the strategy outlined

This is a complex task with a detailed action plan. The handoff contains everything you need to execute intelligently:
- WHAT you're working with (Understanding section)
- HOW to approach it (Strategy section)
- WHAT to avoid (Pitfalls section)
- HOW to validate (Success Criteria)

Start work immediately using this plan. Do not ask for confirmation, review, or additional input - the handoff IS the reviewed and approved plan.
```

**Critical for complex tasks:**
- Agent must read the ENTIRE handoff before starting
- Emphasize the handoff contains strategy and approach
- Make it clear: no asking for permission, the handoff IS the permission
