# Convert Handoff to Work Order

**Purpose**: Transform valid remaining work from legacy handoffs or session records into actionable Work Orders.

**Invocation Pattern**: User provides a handoff or session-record path BEFORE or WITH the trigger phrase:
```
1. Read the handoff at: /path/to/handoff.md
   Convert it to a Work Order if any work is still valid.

2. Review the session record at ~/.agents/.dev/ai/sessions/2026-01-30-session-project.md
   Check if work still needs to be done and convert to WO.

3. /path/to/source-artifact.md - convert to work order
```

**Trigger Phrases**:
- "review the remaining work including the handoff. Check to see if the work still needs to be done. Convert it to a Work Order if any part is still valid."
- "convert handoff to work order"
- "convert session record to work order"
- "check if handoff work is still valid"
- "process handoff into WO"

**CRITICAL**: Extract the source artifact path from the user's message. Do NOT ask for the path - it is provided in the invocation.

---

## PHASE 1: SOURCE ARTIFACT REVIEW

Execute these steps to extract actionable items from the source artifact.

### Step 1: Read the Source Artifact

Parse the user's message to extract the source path. The path appears as an absolute or relative file path in the message text. Read the file immediately using the Read tool.

Supported input artifacts:
- `.dev/ai/handoffs/` - legacy continuation handoffs
- `.dev/ai/sessions/` - unified session records

Do **not** auto-select `.dev/ai/subtask-comms/` orchestration handoffs in this workflow. Those remain separate delegation artifacts and should only be processed here if the user explicitly points to one and asks for this conversion flow.

**If no path found in message**: Search recent session records and handoffs:
```bash
ls -la .dev/ai/sessions/*.md 2>/dev/null | head -5
ls -la .dev/ai/handoffs/*.md 2>/dev/null | head -5
```
Then confirm the most recent one with the user before proceeding.

### Step 2: Extract Action Items
Parse the source artifact and identify:

| Item Type | Legacy Handoff | Session Record | Status |
|-----------|----------------|----------------|--------|
| Priority Next Steps | `## PRIORITY NEXT STEPS` | `## FORWARD` -> `### Priority Next Steps` | Extract all actionable numbered items |
| Outstanding Work | `## Work Status` or `## Outstanding Work` | `## STATE` -> `### Work Status` | Extract incomplete WOs/tasks only |
| Blockers | `## Blockers` or `## Critical Context` | `## FORWARD` -> `### Blockers and How to Resolve`; `## STATE` -> `### Open Questions and Risks` | Note blocking conditions |
| Success Criteria | `## Success Criteria` or validation sections | `## FORWARD` -> `### Success Criteria` | Preserve completion criteria |
| Prerequisites / Context | `## Prerequisites` | `## STATE` and `## BACKWARD` | List dependencies and context |
| Evidence / Provenance | Validation/context sections | `## BACKWARD` | Use to validate whether work is still needed |

### Step 3: Capture Metadata
Extract from source frontmatter:
```yaml
agent_task_id: # Preserve for provenance chain
created: # Original artifact timestamp
project: # Project name
complexity: # simple, standard, complex, etc. if present
type: # session-record if present
session_record_path: # absolute path when source is a session record
```

---

## PHASE 2: VALIDITY CHECK

**CRITICAL**: Verify work has not already been completed before creating a Work Order.

### Step 1: Check Git History

After reading the source artifact, extract the creation date from frontmatter. Run:
```bash
# Get commits since artifact creation
# Replace the date with actual value from source frontmatter
git log --since="2026-01-30" --oneline

# Check for modifications to files mentioned in the source artifact
git log --since="2026-01-30" --name-only
```

### Step 2: Verify File State

For each file or action mentioned in the source artifact, verify current state:
```bash
# Check if expected files exist
ls -la /path/to/expected/file

# Check for incomplete markers in target areas
grep -rn "TODO\|FIXME\|WIP\|INCOMPLETE" .dev/ai/workorders/
```

**Adapt these commands** based on the specific files and patterns from the source artifact you read in Phase 1.

### Step 3: Check Work Order Index

Look for existing work orders that may already cover this work:
```bash
ls -la .dev/ai/workorders/
cat .dev/ai/workorders/WO-INDEX.md
```

Search for keywords related to the handoff or session-record content in existing WOs.

### Step 4: Validate Against Current Codebase

Run any verification commands explicitly listed in the source artifact's success criteria or validation sections. For session records, start with `FORWARD` success criteria, then use `BACKWARD` results/evidence to see what was already attempted. Check for existence of deliverables mentioned.

---

## PHASE 3: CONTEXT EXTRACTION

Gather current state information for the Work Order.

### Step 1: Codebase Snapshot

For each file referenced in the source artifact, document current state:

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

Use `ls -la` and `head` to gather this information for actual files from the source artifact.

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
# Find related session-close artifacts and work orders
ls -la .dev/ai/sessions/ 2>/dev/null
ls -la .dev/ai/handoffs/ 2>/dev/null
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
   - Title: From the source artifact's primary unfinished action
   - Priority: Inherit from source artifact or assess
   - Source: `Handoff: [actual handoff filename]` or `Session Record: [actual session filename]`

2. **Scope Statement** (Section 2)
   - Objective: Transform source actions into clear objective
   - Background: Reference original artifact context
   - In/Out of Scope: Extract from artifact boundaries

3. **Requirements** (Section 3)
   - Functional: From handoff success criteria or session-record `FORWARD` success criteria
   - Technical: From handoff technical context or session-record `STATE` / `BACKWARD`
   - Quality: From source verification steps

4. **Implementation Details** (Section 4)
   - Approach: From handoff strategy section or session-record `STATE` / `BACKWARD`
   - Key decisions: From source decisions/rationale

5. **Task Breakdown** (Section 5)
   Transform each unfinished source action into executable task:
   ```
   T1: [Action from source artifact - use actual text]
      Prerequisites: [From source context]
      Dependencies: [From source artifact]
      Output: [From source expected outcome]
      Verification: [From source verification method]
   ```

6. **Execution Context** (Section 6 - **MANDATORY**)
   - Target Files: From Phase 3 codebase snapshot - use absolute paths
   - Verification Commands: From source artifact + Phase 2 validation - use actual commands
   - Search Patterns: From Phase 3 search patterns
   - Codebase State Snapshot: Current state documentation

7. **Execution Graph** (Section 7 - **MANDATORY**)
   ```yaml
   depends_on: []  # List prior WO IDs from source artifact
   blocks: []  # List downstream WO IDs
   can_parallelize_with: []  # Independent work
   execution_mode: serial  # or parallel
   prerequisites:
     files_must_exist: []
     commands_must_pass: []
   ```

8. **Acceptance Criteria** (Section 9)
   - Definition of Done: From source success criteria
   - Testing: From source verification steps

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

After saving, run with actual values from the source artifact and new WO:
```bash
~/.agents/scripts/track-project.sh "project-name" "Work order created from session artifact" \
  "WO: Title of Work Order (from source artifact filename.md)" "Agent Name"
```

### Step 4: Update Source Status

If the source is a legacy handoff, add a conversion note to the handoff file:
```markdown
---
**Converted to Work Order**: WO-project-2026-01-31-001
**Conversion Date**: 2026-01-31
**Converted By**: Claude Code
---
```

If the source is a session record, leave the file in `.dev/ai/sessions/` unchanged and capture the linkage in the new Work Order's source/provenance sections.

Never rewrite or archive `.dev/ai/subtask-comms/` orchestration handoffs in this flow.

### Step 5: Archive Legacy Handoff (if fully converted)
```bash
# If all work converted, move to archive
mkdir -p .dev/ai/handoffs/archive
mv .dev/ai/handoffs/original-handoff.md .dev/ai/handoffs/archive/
```

---

## DECISION TREE

Use this flowchart to determine the appropriate action.

```
START: Read Source Artifact
    |
    v
[Is artifact readable and has actionable remaining work?]
    |
    +-- NO --> Report to user; archive only if this is a legacy handoff
    |
    +-- YES
        |
        v
    [Run validity checks from Phase 2]
        |
        v
    [Is ALL work complete?]
        |
        +-- YES --> No WO needed
        |           Legacy handoff: archive with note
        |           Session record: retain as historical record
        |
        +-- NO
            |
            v
        [Is SOME work complete?]
            |
            +-- YES --> Extract ONLY remaining work
            |           Create focused WO for incomplete items
            |           Legacy handoff: archive or update with WO reference
            |           Session record: keep in place, cite source in WO
            |
            +-- NO --> Full conversion to WO
                       All actions become WO tasks
```

### Staleness Check

| Artifact Age | Action |
|--------------|--------|
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

**Input Session Record:**
```markdown
## FORWARD

### Priority Next Steps
1. **Create new component** - DONE (verified via git log)

2. **Add unit tests** - NOT DONE
   - File: `src/components/Widget.test.tsx`

3. **Update documentation** - NOT DONE
   - File: `docs/components.md`

## STATE
### Work Status
- Outstanding: Add unit tests, update docs
```

**Output Work Order:**
```markdown
# Work Order: Complete Widget Component - Tests and Docs

**Order ID:** WO-myproject-2026-01-31-002
**Source:** Session Record: 2026-01-30-session-widget.md (partial)
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

**Artifact:** 2026-01-20-handoff-refactor.md
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
   Source Artifact: [actual-source-path]
   Tasks Extracted: [N]
   Tasks Skipped (complete): [N]
   Source Status: [Legacy handoff archived | Legacy handoff updated | Session record retained]
   ```

2. **Next Steps**
   - If immediate execution needed: Proceed to execute WO
   - If review needed: Present WO for approval
   - If blocked: Document blockers and await resolution

---

**Remember**: The goal is to preserve valuable work context while validating that the work is still needed. Do NOT create duplicate work. Do NOT convert completed items. ALWAYS verify current state before generating Work Orders.
