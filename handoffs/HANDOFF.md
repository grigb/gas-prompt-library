## TWO-TIER HANDOFF SYSTEM

### ⚠️ CRITICAL: WHEN TO CREATE HANDOFFS

**CREATE handoffs when:**
- ✅ There is UNFINISHED work to pass to the next agent
- ✅ Work is INCOMPLETE and needs continuation
- ✅ You are STOPPING mid-task and someone else needs to continue
- ✅ There are SPECIFIC NEXT ACTIONS for another agent to execute
- ✅ **USER EXPLICITLY REQUESTS a handoff**, regardless of work completion status

**DO NOT create handoffs when:**
- ❌ User explicitly says they don't want a handoff
- ❌ There are no actionable next steps AND user hasn't requested context preservation

**Critical Rule:** Always respect explicit user requests for handoffs. If user says "create a handoff" or "your work qualifies as a necessary handoff", create the handoff regardless of whether work appears complete. Context preservation for ongoing systems takes precedence over completion status.

**If work is complete AND user hasn't requested a handoff:** Create an audit/accomplishment file instead.

### STEP 0: Assess Task Complexity (Critical First Step)

**Simple tasks (use minimal handoff 30-50 lines):**
- Run specific command or test
- Update single file with clear instructions
- Fix known bug with defined solution
- Execute defined process step
- Mechanical work with no judgment calls needed

**Complex tasks (use detailed handoff 150-250 lines):**
- Integration of multiple sources requiring synthesis
- Design/architecture decisions requiring understanding
- Tasks requiring context to make judgment calls
- Multi-step tasks with interdependencies
- Work requiring understanding of "why" and "how to approach"

**Determine complexity BEFORE creating handoff.**

### STEP 1: Assess Context Level
Check user message for these triggers:

- **Low Context Triggers**: "low context", "running out", "context limited", "quick", "emergency"
- If found → Load ONLY Handoff-Minimal.md (emergency mode)
- If not found → Load based on task complexity from Step 0

### STEP 2: Load Instructions Based on Complexity
```bash
# Always load minimal instructions first
cat ~/.agents/prompts/handoffs/HANDOFF-MINIMAL.md

# Load detailed if task is complex:
# 1. No low context triggers AND
# 2. Task complexity = COMPLEX (from Step 0) AND
# 3. Adequate context remains
if [[ "$LOW_CONTEXT" != "true" ]] && [[ "$TASK_COMPLEXITY" == "complex" ]]; then
    cat ~/.agents/prompts/handoffs/HANDOFF-DETAILED.md
fi
```

### STEP 3: Execute Based on Loaded Instructions
Follow the instructions from the loaded prompt(s).

**Remember:** Action-first ≠ context-minimal. Action-first means lead with actions, support with understanding, not lead with accomplishments.

---

## LEGACY FULL PROMPT (Only if two-tier files unavailable)

**⚠️ WARNING: This legacy prompt is deprecated. Use HANDOFF-MINIMAL.md + HANDOFF-DETAILED.md instead.**

The legacy approach led to bloated handoffs. If you must use this, follow the ACTION-FIRST principle:

---

## HANDOFF CREATION PROCESS

### STEP 1: Identify Next Actions (NOT session summary)

**Focus:** What does the next agent need to DO?

1. **Analyze current state:** Review conversation, check for incomplete work, identify blockers
2. **Generate action list:** Create numbered, prioritized list of immediate next steps
3. **Define success criteria:** For each action, state expected outcome

**Output:** Concise action list (3-7 items, each with one-line context)

---

### STEP 2: Create Action-First Handoff Document

**File path:**
```bash
mkdir -p .dev/ai/handoffs/
TIMESTAMP=$(~/.agents/scripts/get-filename-prefix.sh)
FILE=".dev/ai/handoffs/${TIMESTAMP}-handoff-[project-id].md"
```

**Structure (IN THIS ORDER):**

```markdown
# Handoff: [Project] - [TIMESTAMP]

## PRIORITY NEXT STEPS

1. **[Action 1]** - [Why/Context in one line]
   - Command: `[if applicable]`
   - Expected outcome: [success criteria]

2. **[Action 2]** - [Why/Context]
   - Location: [file/path if relevant]

3. **[Action 3]** - [Why/Context]

## CRITICAL CONTEXT (Minimal)
[ONLY information needed to execute actions above]
- Current state: [brief - one line]
- Key blockers: [if any]
- Prerequisites: [if any]

## Work Status (Brief)
- Outstanding: WO-xxx (next: [action])
- Completed this session: WO-yyy ✓

## References (If needed for actions)
- Related docs: [specific files only]

## Full Session Details (if applicable)
[ONLY include if an audit was created just before this handoff]
For complete session context: .dev/ai/audits/[timestamp]-conversation-summary.md
```

**Rules:**
- **Simple tasks:** Target 30-50 lines
- **Complex tasks:** Target 150-250 lines (actions + understanding + strategy)
- Lead with actions, not accomplishments
- Context explains "why action matters" and "how to approach", not "what we did"
- Save detailed session history to audit file, not handoff
- **Reference documents:** Include full absolute paths inline where relevant (not just at end)

**Save and track:**
```bash
~/.agents/scripts/track-project.sh "[project]" "Handoff created" \
  "Handoff: [one-line summary]" "[agent]"
```

---

### STEP 3: Generate Next-Session Prompt

Create copy-paste prompt for next agent:

```markdown
I'm picking up work on [project-name].

1. Read the handoff at: [FULL ABSOLUTE PATH to handoff file]
2. Review project rules in [FULL PATH to CLAUDE.md / AGENTS.md]
3. BEGIN EXECUTING the priority next steps immediately

The handoff contains the complete action plan. Start work now - do not ask for confirmation or review. The actions have been approved.
```

**Critical:**
- Include full absolute path to handoff file
- Emphasize immediate execution - no asking for permission
- The handoff IS the approval to proceed

---

## FINAL OUTPUT

Present in order:

1. **Next actions list** (what to do, not what was done)
2. **Handoff file content** (action-first structure)
3. **Copy-paste prompt** (in code block)

Confirm file saved and tracked.

---

## EXAMPLES: When to Use Minimal vs Detailed

### Example 1: Simple Task (Minimal Handoff 40 lines)
**Task:** "Run tests and fix any failures"

```markdown
## PRIORITY NEXT STEPS

1. **Run test suite** - Verify current failures
   - Command: `npm test`
   - Expected: See 3 failing tests (auth.test.js, api.test.js)

2. **Fix each failure** - Check error messages and resolve
   - Files: `src/auth/login.ts:142`, `src/api/users.ts:89,102`
   - Reference: Test patterns in `/full/absolute/path/to/project/docs/testing-guide.md`

3. **Verify and commit** - All tests pass
   - Command: `npm test` (should show all green)
   - Commit: `git commit -m "fix: resolve test failures"`

## CRITICAL CONTEXT
- Current state: PR ready except 3 failing tests
- Blocker: Must pass before merge
- Tests are regression from yesterday's auth changes

## REFERENCES
- Test suite guide: `/full/absolute/path/to/project/docs/testing-guide.md`
```

**Why minimal works:** Mechanical execution, clear success criteria, no judgment calls needed.

---

### Example 2: Complex Task (Detailed Handoff 180 lines)
**Task:** "Integrate two style guides with different philosophies"

```markdown
## PRIORITY NEXT STEPS

1. **Integrate WRITING-STYLE.md into STYLE-GUIDE-HYBRID.md**
   - Create: `/full/absolute/path/to/project/.dev/discovery-kit/STYLE-GUIDE-MASTER.md`
   - Method: Layered integration (strategic + tactical)
   - Reference integration mapping: `/full/absolute/path/to/project/.dev/ai/handoffs/2025-10-10-integration-guide.md`

2. **Follow layered approach** - Don't copy-paste, synthesize
   - Layer 1: Keep all strategic principles from HYBRID
   - Layer 2: Add tactical quality from WRITING-STYLE
   - Layer 3: Synthesize overlapping sections
   - Integration instructions: `/full/absolute/path/to/project/.dev/ai/handoffs/2025-10-10-integration-guide.md` (section 3)

3. **Validate integration** - Test with real example
   - Write decision: "Use SQLite for MVP" using ONLY Master guide
   - Should provide: analogy, Why→What→How, filler removal, density levels, voice/tone
   - Reference examples: `/full/absolute/path/to/project/.dev/discovery-kit/example-decisions.md`

## BACKGROUND: Why This Integration Matters

Discovery Kit generates 15-20 pages per module. Without consistent standards:
- Some agents write verbose, rambling documents
- Some write terse, incomplete documents
- No consistency in analogies, rationale, structure

We need unified guide combining strategic (WHAT to write) + tactical (HOW to write clearly).

## UNDERSTANDING THE INPUTS

**STYLE-GUIDE-HYBRID.md** (850+ lines at `/full/absolute/path/to/project/.dev/discovery-kit/STYLE-GUIDE-HYBRID.md`)
- Contains: 5 Core Writing Principles, 5 Discovery Kit Principles, 11 document types
- Strong on: Document structure, strategic principles, what sections to include
- Weak on: Sentence-level clarity, word-level precision

**WRITING-STYLE.md** (446 lines at `/full/absolute/path/to/project/.dev/discovery-kit/WRITING-STYLE.md`)
- Contains: NO word limits, filler word list, density levels, voice/tone mapping
- Strong on: Sentence clarity, word choice, operational tactics
- Weak on: Document structure, strategic principles

**Why complementary:** HYBRID = document/section level, WRITING-STYLE = sentence/word level.
Both needed, not redundant.

## INTEGRATION STRATEGY

**Layer 1 (Strategic from HYBRID):**
Keep all 10 principles, 11 document types, writer's checklist, examples

**Layer 2 (Tactical from WRITING-STYLE):**
Enhance existing sections with filler word list, density framework, voice/tone mapping

**Layer 3 (Synthesize Overlaps):**
Where both cover same topic (active voice), combine into single enhanced section

**Critical:** Not copy-paste. Synthesize complementary content.
Reference: Content overview at `/full/absolute/path/to/project/.dev/discovery-kit/STYLE-GUIDE-CONTENT-OVERVIEW.md`

## POTENTIAL PITFALLS

1. **Duplication** - Both cover "active voice." Synthesize, don't duplicate.
2. **Seeming contradiction** - "No word limits" vs "clarity." Resolution: Long OK if structured.
3. **Losing unique value** - Check preservation list at `/full/absolute/path/to/project/.dev/discovery-kit/STYLE-GUIDE-CONTENT-OVERVIEW.md` (section 4)
4. **Over-simplifying** - This is complex. Budget 60-90 minutes. Read both guides completely first.

## SUCCESS CRITERIA

Write complete decision for "Use SQLite for MVP" using ONLY Master guide.

Must provide guidance on:
- ✓ Start with analogy
- ✓ Structure as Why→What→How
- ✓ Remove specific filler words (which ones?)
- ✓ Use high information density (what does this mean?)
- ✓ Use declarative factual voice (why for decisions?)

## REFERENCES
- Integration mapping: `/full/absolute/path/to/project/.dev/ai/handoffs/2025-10-10-integration-guide.md`
- Content preservation: `/full/absolute/path/to/project/.dev/discovery-kit/STYLE-GUIDE-CONTENT-OVERVIEW.md`
- Example decisions: `/full/absolute/path/to/project/.dev/discovery-kit/example-decisions.md`
- Full session audit: `/full/absolute/path/to/project/.dev/ai/audits/2025-10-10-20-29-conversation-summary.md`
```

**Why detailed needed:** Requires understanding inputs, making synthesis judgments, avoiding pitfalls.

---

**Use minimal when:** Agent just needs to DO (mechanical execution)
**Use detailed when:** Agent needs to UNDERSTAND before doing (synthesis/judgment)

---

**Remember:** Handoffs are action plans for agents with zero context. Provide minimum context for intelligent execution - no more, no less. Action-first doesn't mean context-last.
