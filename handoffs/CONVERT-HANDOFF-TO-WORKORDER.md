# Convert Handoff to Work Order

**Purpose**: Transform valid remaining work from handoffs into actionable Work Orders.

**Invocation Pattern**: User provides handoff path BEFORE or WITH the trigger phrase:
```
1. Read the handoff at: /path/to/handoff.md
   Convert it to a Work Order if any work is still valid.

2. Review the handoff at ~/.agents/.dev/ai/handoffs/2026-01-30-handoff.md
   Check if work still needs to be done and convert to WO.

3. /path/to/handoff.md - convert to work order
```

**Trigger Phrases**:
- "review the remaining work including the handoff. Check to see if the work still needs to be done. Convert it to a Work Order if any part is still valid."
- "convert handoff to work order"
- "check if handoff work is still valid"
- "process handoff into WO"

**CRITICAL**: Extract the handoff path from the user's message. Do NOT ask for the path - it is provided in the invocation.

---

## PHASE 1: HANDOFF REVIEW

Execute these steps to extract actionable items from the handoff.

### Step 1: Read the Handoff

Parse the user's message to extract the handoff path. The path appears as an absolute or relative file path in the message text. Read the file immediately using the Read tool.

**If no path found in message**: Search for recent handoffs:
```bash
ls -la .dev/ai/handoffs/*.md | head -5
```
Then confirm the most recent one with the user before proceeding.

### Step 2: Extract Action Items
Parse the handoff and identify:

| Item Type | Location in Handoff | Status |
|-----------|-------------------|--------|
| Priority Next Steps | `## PRIORITY NEXT STEPS` section | Extract all numbered items |
| Outstanding Work | `## Work Status` or `## Outstanding Work` | Extract incomplete WOs |
| Blockers | `## Blockers` or `## Critical Context` | Note any blocking conditions |
| Prerequisites | `## Prerequisites` | List dependencies |

### Step 3: Capture Metadata
Extract from handoff frontmatter:
```yaml
agent_task_id: # Preserve for provenance chain
created: # Original handoff timestamp
project: # Project name
complexity: # simple or complex
```

---

## PHASE 2: VALIDITY CHECK

**CRITICAL**: Verify work has not already been completed before creating a Work Order.

### Step 1: Check Git History

After reading the handoff, extract the creation date from frontmatter. Run:
```bash
# Get commits since handoff creation
# Replace the date with actual value from handoff frontmatter
git log --since="2026-01-30" --oneline

# Check for modifications to files mentioned in handoff
git log --since="2026-01-30" --name-only
```

### Step 2: Verify File State

For each file or action mentioned in the handoff, verify current state:
```bash
# Check if expected files exist
ls -la /path/to/expected/file

# Check for incomplete markers in target areas
grep -rn "TODO\|FIXME\|WIP\|INCOMPLETE" .dev/ai/workorders/
```

**Adapt these commands** based on the specific files and patterns from the handoff you read in Phase 1.

### Step 3: Check Work Order Index

Look for existing work orders that may already cover this work:
```bash
ls -la .dev/ai/workorders/
cat .dev/ai/workorders/WO-INDEX.md
```

Search for keywords related to the handoff content in existing WOs.

### Step 4: Validate Against Current Codebase

Run any verification commands explicitly listed in the handoff's success criteria or validation sections. Check for existence of deliverables mentioned.

---

## PHASE 3: CONTEXT EXTRACTION

Gather current state information for the Work Order.

### Step 1: Codebase Snapshot

For each file referenced in the handoff, document current state:

```yaml
files_involved:
  - path: /Users/example/project/src/feature.ts
    exists: yes
    current_state: Contains stub implementation, 45 lines
    last_modified: 2026-01-28

  - path: /Users/example/project/tests/feature.test.ts
    exists: no
    current_state: Not yet created
```

Use `ls -la` and `head` to gather this information for actual files from the handoff.

### Step 2: Gather Search Patterns

For each action item, determine how to locate the relevant code:

```yaml
search_patterns:
  - action: "Add validation to user input"
    file: /Users/example/project/src/form.ts
    pattern: "function validateInput"
    context: "Function should be around line 50-60"
```

### Step 3: Document Prerequisites

```yaml
prerequisites:
  files_must_exist:
    - /Users/example/project/package.json
    - /Users/example/project/src/index.ts
  commands_must_pass:
    - npm test
  state_requirements:
    - All existing tests pass
```

### Step 4: Identify Related Documents

```bash
# Find related handoffs and work orders
ls -la .dev/ai/handoffs/
ls -la .dev/ai/workorders/
cat .dev/ai/workorders/WO-INDEX.md
```

---

## PHASE 4: WORK ORDER GENERATION

**Reference**: `~/.agents/prompts/work-orders/CREATE-WORK-ORDER.md` for full section details.

### Required Sections (Minimum)

Generate a Work Order with these sections. Match the structure in CREATE-WORK-ORDER.md.

1. **Order Header** (Section 1 in CREATE-WORK-ORDER.md)
   - Order ID: `WO-[PROJECT-ID]-[TIMESTAMP]-[SEQ]`
   - Title: From handoff's primary action
   - Priority: Inherit from handoff or assess
   - Source: `Handoff: [actual handoff filename]`

2. **Scope Statement** (Section 2)
   - Objective: Transform handoff actions into clear objective
   - Background: Reference original handoff context
   - In/Out of Scope: Extract from handoff boundaries

3. **Requirements** (Section 3)
   - Functional: From handoff success criteria
   - Technical: From handoff technical context
   - Quality: From handoff verification steps

4. **Implementation Details** (Section 4)
   - Approach: From handoff strategy section
   - Key decisions: From handoff decisions/rationale

5. **Task Breakdown** (Section 5)
   Transform each handoff action into executable task:
   ```
   T1: [Action from handoff - use actual text]
      Prerequisites: [From handoff context]
      Dependencies: [From handoff]
      Output: [From handoff expected outcome]
      Verification: [From handoff verification method]
   ```

6. **Execution Context** (Section 6 - **MANDATORY**)
   - Target Files: From Phase 3 codebase snapshot - use absolute paths
   - Verification Commands: From handoff + Phase 2 validation - use actual commands
   - Search Patterns: From Phase 3 search patterns
   - Codebase State Snapshot: Current state documentation

7. **Execution Graph** (Section 7 - **MANDATORY**)
   ```yaml
   depends_on: []  # List prior WO IDs from handoff
   blocks: []  # List downstream WO IDs
   can_parallelize_with: []  # Independent work
   execution_mode: serial  # or parallel
   prerequisites:
     files_must_exist: []
     commands_must_pass: []
   ```

8. **Acceptance Criteria** (Section 9)
   - Definition of Done: From handoff success criteria
   - Testing: From handoff verification steps

---

## PHASE 5: SAVE AND TRACK

### Step 1: Generate Work Order ID
```bash
# Get project ID
PROJECT_ID=$(grep "^id:" PROJECT-ID.md 2>/dev/null | cut -d: -f2 | xargs || basename "$PWD")

# Get timestamp
TIMESTAMP=$(~/.agents/scripts/get-filename-prefix.sh)

# Check for existing WOs with same prefix
EXISTING_COUNT=$(ls .dev/ai/workorders/WO-${PROJECT_ID}-${TIMESTAMP}-*.md 2>/dev/null | wc -l)
SEQUENCE=$(printf "%03d" $((EXISTING_COUNT + 1)))

WO_ID="WO-${PROJECT_ID}-${TIMESTAMP}-${SEQUENCE}"
echo "Work Order ID: $WO_ID"
```

### Step 2: Save Work Order
```bash
mkdir -p .dev/ai/workorders
WO_FILE=".dev/ai/workorders/${WO_ID}.md"
# Write work order content to file using Write tool
```

### Step 3: Track in Project System

After saving, run with actual values from the handoff and new WO:
```bash
~/.agents/scripts/track-project.sh "project-name" "Work order created from handoff" \
  "WO: Title of Work Order (from handoff handoff-filename.md)" "Agent Name"
```

### Step 4: Update Handoff Status

Add conversion note to the handoff file:
```markdown
---
**Converted to Work Order**: WO-project-2026-01-31-001
**Conversion Date**: 2026-01-31
**Converted By**: Claude Code
---
```

### Step 5: Archive Handoff (if fully converted)
```bash
# If all work converted, move to archive
mkdir -p .dev/ai/handoffs/archive
mv .dev/ai/handoffs/original-handoff.md .dev/ai/handoffs/archive/
```

---

## DECISION TREE

Use this flowchart to determine the appropriate action.

```
START: Read Handoff
    |
    v
[Is handoff readable and has actions?]
    |
    +-- NO --> Archive handoff as incomplete, report to user
    |
    +-- YES
        |
        v
    [Run validity checks from Phase 2]
        |
        v
    [Is ALL work complete?]
        |
        +-- YES --> Archive handoff, no WO needed
        |           Log: "Handoff [filename] archived - all work complete"
        |
        +-- NO
            |
            v
        [Is SOME work complete?]
            |
            +-- YES --> Extract ONLY remaining work
            |           Create focused WO for incomplete items
            |           Archive handoff with WO reference
            |
            +-- NO --> Full conversion to WO
                       All actions become WO tasks
```

### Staleness Check

| Handoff Age | Action |
|-------------|--------|
| < 3 days | Convert directly |
| 3-7 days | Validate all context still applies, then convert |
| > 7 days | **FLAG FOR HUMAN REVIEW** before converting |
| > 30 days | Recommend archival without conversion unless explicitly requested |

### Blocked Work Handling

If work is blocked:
1. Create WO with status: `BLOCKED`
2. Document blocker in WO `## Blockers & How to Resolve` section
3. Set `RESUME_AT: [first unblocked task]`
4. Include unblocking actions as T0 tasks

---

## EXAMPLES

### Example 1: Simple Handoff (Fully Valid)

**Input Handoff:**
```markdown
## PRIORITY NEXT STEPS

1. **Run test suite** - Verify failures fixed
   - Command: `npm test`
   - Expected: All tests pass

2. **Commit changes** - Document fix
   - Command: `git commit -m "fix: resolve auth tests"`
```

**Output Work Order:**
```markdown
# Work Order: Fix Auth Test Suite

**Order ID:** WO-myproject-2026-01-31-001
**Source:** Handoff: 2026-01-30-handoff-auth-tests.md
**Priority:** High
**Status:** NOT_STARTED

## Scope Statement
**Objective:** Verify and commit test suite fixes from previous session.

## Task Breakdown

T1: Run Test Suite
   Prerequisites: None
   Output: All tests passing
   Verification: `npm test` returns 0 exit code

T2: Commit Changes
   Prerequisites: T1 complete with passing tests
   Output: Committed changes
   Verification: `git log -1` shows new commit

## Execution Context
**Target Files:**
- path: /Users/dev/myproject/src/auth/login.ts
  current_state: Modified with fix (uncommitted)

**Verification Commands:**
```bash
npm test
# Expected: All tests passing
```
```

### Example 2: Partial Completion

**Input Handoff:**
```markdown
## PRIORITY NEXT STEPS

1. **Create new component** - DONE (verified via git log)

2. **Add unit tests** - NOT DONE
   - File: `src/components/Widget.test.tsx`

3. **Update documentation** - NOT DONE
   - File: `docs/components.md`
```

**Output Work Order:**
```markdown
# Work Order: Complete Widget Component - Tests and Docs

**Order ID:** WO-myproject-2026-01-31-002
**Source:** Handoff: 2026-01-30-handoff-widget.md (partial)
**Note:** Task 1 (component creation) already complete - excluded

## Task Breakdown

T1: Add Unit Tests
   Prerequisites: Widget component exists (verified)
   Output: Test file at src/components/Widget.test.tsx
   Verification: `npm test Widget.test` passes

T2: Update Documentation
   Prerequisites: None (can run parallel with T1)
   Output: Updated docs/components.md
   Verification: Widget section exists in documentation
```

### Example 3: Stale Handoff (>7 days)

**Agent Response:**
```markdown
## STALE HANDOFF DETECTED

**Handoff:** 2026-01-20-handoff-refactor.md
**Age:** 11 days (exceeds 7-day threshold)

**Recommended Action:** Human review required before conversion.

**Concerns:**
1. Codebase may have changed significantly
2. Requirements may have evolved
3. Context may be outdated

**Options:**
1. Review and confirm handoff is still valid, then I will convert
2. Archive handoff without conversion
3. Override and convert anyway (not recommended)

Please advise how to proceed.
```

---

## OUTPUT REQUIREMENTS

After conversion, provide:

1. **Confirmation Summary**
   ```
   Work Order Created: WO-[actual-ID]
   Saved to: .dev/ai/workorders/[actual-filename].md
   Source Handoff: [actual-handoff-path]
   Tasks Extracted: [N]
   Tasks Skipped (complete): [N]
   Handoff Status: [Archived | Updated with WO reference]
   ```

2. **Next Steps**
   - If immediate execution needed: Proceed to execute WO
   - If review needed: Present WO for approval
   - If blocked: Document blockers and await resolution

---

**Remember**: The goal is to preserve valuable work context while validating that the work is still needed. Do NOT create duplicate work. Do NOT convert completed items. ALWAYS verify current state before generating Work Orders.
