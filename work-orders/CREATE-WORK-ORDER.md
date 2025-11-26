# Work Order Creation Protocol

## 🚨 AUTOMATIC TRIGGERING RULES (MANDATORY)

**READ THIS FIRST:** Work order creation is now MANDATORY in certain situations.

### When Work Orders Are REQUIRED (Agent MUST create)

**You MUST create a work order (cannot proceed with direct execution) when ANY of these thresholds are met:**

1. **Message Count Threshold**
   - Current conversation has reached **3+ messages** on the same task
   - Action: STOP and create work order before proceeding

2. **Task Complexity Threshold**
   - TodoWrite shows **5+ subtasks**
   - Action: STOP and create work order before proceeding

3. **Time Estimate Threshold**
   - Estimated time to complete is **30+ minutes**
   - Action: STOP and create work order before proceeding

4. **Handoff Threshold**
   - User mentions "come back later" or "another agent"
   - Context window drops below 20%
   - Work will span multiple sessions
   - Action: STOP and create work order immediately

5. **User Explicit Request**
   - User says "create a work order for this"
   - Action: Create work order as requested

### Agent Response Template (When Threshold Met)

```
🚨 WORK ORDER REQUIRED

This task meets the following thresholds:
- [x] 3+ messages needed
- [ ] 5+ subtasks identified
- [x] 30+ minutes estimated
- [ ] Handoff likely

I must create a work order before proceeding to ensure:
✅ Work can be handed off to other agents
✅ Progress is tracked across sessions
✅ Context is preserved for recovery

Creating work order: WO-{project}-{timestamp}-{seq}
After creating the work order, I will immediately begin execution.

User can interrupt with: "stop" or "don't start yet"
User can override requirement with: "skip work order and proceed"
```

**CRITICAL: AUTO-EXECUTION AFTER CREATION**

When agent automatically creates work order (thresholds 1-3), agent MUST:
1. Create work order with full context
2. Save to disk and track
3. **Immediately begin executing the work order**
4. Update status to IN_PROGRESS
5. Continue working until complete

**Exception:** If user says "stop", "wait", or "don't start yet" → Agent creates WO but pauses

### When to Suggest PROPOSAL Instead

**If the work is LARGE/COMPLEX, suggest a proposal FIRST:**

**Proposal indicators:**
- **5+ major tasks** (not subtasks)
- **Multi-week timeline** (3+ weeks estimated)
- **Architectural decisions** needed
- **Multiple alternatives** should be evaluated
- **Cross-system changes** affecting multiple modules

**Agent response when proposal needed:**
```
🚨 PROPOSAL RECOMMENDED

This appears to be a complex initiative:
- Estimated major tasks: 8
- Estimated timeline: 3-4 weeks
- Architectural decisions required

I recommend creating a PROPOSAL first, which will then generate coordinated work orders.

Would you like me to:
1. Create a proposal (recommended for this complexity)
2. Create work orders directly (if you prefer)
```

### User Override Protocol

**Users CAN override work order requirement** by explicitly saying:
- "skip work order and proceed"
- "no work order needed"
- "execute directly"

**When user overrides, you MUST:**
1. Acknowledge the override
2. Warn about tracking/handoff limitations
3. Still use TodoWrite for task tracking
4. Still create accomplishment entry when complete

**Override response template:**
```
⚠️ Work order skipped by user request

Proceeding with direct execution.

Note: This work will not be tracked in the work order system.
If handoff is needed, manual context transfer will be required.

Using TodoWrite for task tracking instead.
```

---

## Standard Work Order Generation

Generate a comprehensive work order from the conversation context. Execute all steps sequentially without pausing for review. **ALWAYS save the work order to disk and track it in the project tracking system.**

# Control Triggers
- **Standard work order:** Default behavior - generate full work order with all sections, save, and track
- **Quick work order:** If message includes "quick" → produce condensed version, save, and track
- **Multiple orders:** If message includes "split" → create separate work orders for independent tasks
- **Skip tracking:** If message includes "no track" → save work order but skip tracking system (rare)

# Work Order Requirements

## 🚨 CRITICAL CONTEXT REQUIREMENT

**Sub-agents receive ZERO conversation context.** Every work order MUST be completely self-contained.

**VALIDATION BEFORE FINALIZING:**
Before presenting the work order, verify Section 6 (Execution Context) includes:

- ✅ Absolute paths to ALL target files
- ✅ Current state verification commands
- ✅ Search patterns for locating code sections
- ✅ List of files sub-agent must read for context
- ✅ Codebase state snapshot from conversation

**If Section 6 is incomplete, the work order is DEFECTIVE and will cause sub-agent failure.**

---

## PHASE 1 - CONTEXT ANALYSIS
1. **Review conversation:** Analyze the preceding conversation for requirements
2. **Extract objectives:** Identify what needs to be accomplished
3. **Gather constraints:** Note any limitations, dependencies, or prerequisites
4. **Identify deliverables:** Determine expected outputs and success criteria
5. **EXTRACT FILE CONTEXT (MANDATORY):**
   - Identify EVERY file mentioned in conversation
   - Note current line numbers/sections if discussed
   - Capture exact search patterns used to locate code
   - Record current implementation details mentioned
   - List ALL files a sub-agent would need to read

## PHASE 2 - WORK ORDER CREATION
Generate a structured work order containing:

### 1. Order Header
- **Order ID:** WO-[PROJECT-ID]-[YYYY-MM-DD-HH-MM-SS]-[seq]
  - **PROJECT-ID**: From PROJECT-ID.md in repo root (e.g., "ecommerce-platform", "auth-system")
  - **YYYY-MM-DD-HH-MM-SS**: Timestamp in format 2025-10-08-12-30-45 (use `~/.agents/scripts/get-filename-prefix.sh`)
  - **seq**: 001, 002, 003 if multiple WOs in same session
  - **Example**: WO-agents-system-2025-10-08-12-30-45-001
  - **CRITICAL**: Always check PROJECT-ID.md first. If missing, create it before generating WO ID.
- **Title:** Clear, descriptive title of the work
- **Priority:** Critical/High/Medium/Low
- **Requested by:** User or system that initiated
- **Created:** [Timestamp]
- **Estimated effort:** Time/complexity estimate

### 2. Scope Statement
- **Objective:** What must be accomplished
- **Background:** Context from conversation that led to this work order
- **In scope:** Explicit list of what's included
- **Out of scope:** Explicit list of what's NOT included

### 3. Requirements
- **Functional requirements:** What the solution must do
- **Technical requirements:** Technology constraints and standards
- **Quality requirements:** Performance, security, testing standards
- **Documentation requirements:** What needs to be documented

### 4. Implementation Details
- **Approach:** Recommended implementation strategy
- **Key decisions from conversation:** Important choices already made
- **Open questions:** Items requiring clarification
- **Risks:** Potential issues and mitigation strategies

### 5. Task Breakdown
**Create executable tasks with:**

- Task number (T1, T2, etc.)
- Clear description
- Prerequisites/dependencies
- Expected output
- Verification method

Example format:
```
T1: [Task description]
   Prerequisites: [What must exist/be true before starting]
   Dependencies: [Other tasks that must complete first]
   Output: [Specific deliverable]
   Verification: [How to confirm completion]

T2: [Task description]
   Prerequisites: T1 completion
   Dependencies: None
   Output: [Specific deliverable]
   Verification: [How to confirm completion]
```

### 6. Execution Context (MANDATORY - Sub-agents CANNOT infer)

**🚨 CRITICAL: This section is MANDATORY. Sub-agents receive ZERO conversation context.**

#### Target Files (REQUIRED)
**Primary targets** (files that WILL be created or modified):
```yaml
- path: /absolute/path/to/file.ext
  purpose: [what we're changing/creating]
  current_state: [what exists NOW - verify with grep/read first]
  line_range: [if modifying: "lines 45-67" or "section starting with '## Header'"]
  backup_required: yes/no
```

**Related files** (files sub-agent MUST read for context):
```yaml
- path: /absolute/path/to/dependency.ext
  purpose: [why sub-agent needs to read this]
  sections: [specific sections to read, or "entire file"]
```

#### Verification Commands (REQUIRED)
**Run BEFORE starting work** to verify codebase state:
```bash
# Verify target file exists and contains expected content
grep -n "SECTION_MARKER" /path/to/file
# Expected output: "Line 123: ## SECTION_MARKER"

# Verify dependencies are in place
ls -la /path/to/dependency.ext
# Expected: File exists

# Verify current implementation state
grep -c "OLD_PATTERN" /path/to/file
# Expected: "5" (or specific count)
```

#### Search Patterns (for locating code sections)
```yaml
- pattern: "## EXACT SECTION HEADER"
  file: /absolute/path/to/file.ext
  purpose: "Find start of section to replace"
  context: "Section should be between lines X-Y approximately"

- pattern: "function specificFunction("
  file: /absolute/path/to/file.ext
  purpose: "Locate function to modify"
```

#### Codebase State Snapshot
**Current implementation details** (capture from conversation):

- Existing behavior: [describe what the code does NOW]
- Known issues: [problems that exist in current code]
- Constraints: [things that cannot be changed]
- Integration points: [other systems that depend on this]

### 7. Execution Graph (MANDATORY - Enables Parallel Execution)

**🚨 CRITICAL: Agents use this to determine serial vs parallel execution.**

#### Dependencies
**Work orders this WO depends on:**
```yaml
depends_on:
  - WO-{project}-{timestamp}-{seq}-{title}
    required_tasks: [T1, T2, T3]  # Which tasks must complete
    required_outputs:
      - output_name: "/absolute/path/to/file.ext"
      - another_output: "/absolute/path/to/other.ext"
    reason: "Brief explanation of why this is needed"

# OR if no dependencies:
# depends_on: []
```

**VALIDATION:**

- Each WO ID must be exact filename (without .md)
- Required outputs must be absolute paths
- Reason helps agents understand relationship

#### Blocks
**Work orders that cannot start until this WO completes:**
```yaml
blocks:
  - WO-{project}-{timestamp}-{seq}-{title}
  - WO-{project}-{timestamp}-{seq}-{another-title}

# OR if doesn't block anything:
# blocks: []
```

#### Parallelization
**Work orders that CAN run in parallel with this one:**
```yaml
can_parallelize_with:
  - WO-{project}-{timestamp}-{seq}-{title}
    reason: "Both depend only on WO-1, operate on different files"
    safety_check: "No shared file writes, independent modules"

# OR if must run alone:
# can_parallelize_with: []
```

**RULES for determining can_parallelize_with:**

- ✅ Neither WO depends on the other
- ✅ Both operate on different files
- ✅ No shared state modifications
- ✅ No sequential data flow required
- ❌ If unsure, leave empty (safer to run serially)

#### Execution Mode
```yaml
execution_mode: serial  # serial | parallel | conditional

# serial: Must run alone, sequentially
# parallel: Can run with others if dependencies met
# conditional: Depends on runtime state (rare)
```

#### Prerequisites Verification
**Conditions that MUST be true before starting:**
```yaml
prerequisites:
  files_must_exist:
    - /absolute/path/to/required/file.ext
    - /absolute/path/to/another/file.ext

  commands_must_pass:
    - command: "grep -q 'PATTERN' /path/to/file"
      purpose: "Verify target section exists"
    - command: "test -d /path/to/directory"
      purpose: "Ensure directory structure ready"

  environment_vars:
    - AGENTS_DIR: ~/.agents
    - PROJECT_ROOT: .

  state_requirements:
    - "Previous WO-X must be status: COMPLETED"
    - "File /path/to/output from WO-Y must exist"
```

### 8. Resources & References
- **Conversation context:** Link to original discussion
- **Related documents:** Any referenced files or documentation
- **External resources:** APIs, libraries, or tools mentioned

### 9. Acceptance Criteria
- **Definition of done:** Specific, measurable completion criteria
- **Testing requirements:** What tests must pass
- **Review requirements:** Who needs to review/approve
- **Documentation complete:** What docs must exist
- **Accomplishment tracking:** Automatic accomplishment entry created in `.dev/ai/accomplishments/` when WO status = COMPLETED

### 10. Execution Notes
- **Starting point:** Where to begin implementation
- **Critical path:** Must-do items in sequence
- **Parallel opportunities:** Tasks that can run simultaneously
- **Handoff ready:** Information needed for agent handoff
- **Completion process:** When this work order is marked COMPLETED, an accomplishment entry will be automatically created in `.dev/ai/accomplishments/YYYY-MM-DD-HH-MM-SS-[title].md`

### 11. Work Order Metadata
- **Parent Document:** [Proposal/Handoff/Manual ID if applicable]
- **Status:** NOT_STARTED | IN_PROGRESS | BLOCKED | COMPLETED
- **Created By:** [Agent-Name] @ [Timestamp]
- **Priority:** Critical | High | Medium | Low
- **Blocks:** [WO-IDs that depend on this]
- **Blocked By:** [WO-IDs this depends on]

### 12. Autonomous Execution Tracker
**CRITICAL: Update this section AS YOU WORK - This is how we track progress**

```yaml
# Quick Status (Update First)
STATUS: NOT_STARTED  # NOT_STARTED | IN_PROGRESS | BLOCKED | COMPLETED
COMPLETE: 0/[N] tasks
BLOCKED: none
RESUME_AT: T1
LAST_UPDATE: [timestamp]
AGENT: [agent-name]
CONTEXT_REMAINING: high  # high | medium | low | critical
```

**Task Progress Checklist** (Update checkboxes as you work):
✅ = Complete | 🔄 = In Progress | ⬜ = Not Started | ❌ = Blocked

```markdown
- ⬜ T1: [Task description]
  - [ ] Read required files: [list paths]
  - [ ] Create/modify: [path/to/file]
  - [ ] Test: [exact test command]
  - [ ] Verify: [success criteria]

- ⬜ T2: [Task description]
  - [ ] Subtask with specific file paths
  - [ ] Another subtask with commands
```

### 13. File Operations Log
**Update immediately after EVERY file operation**

```yaml
files_created:
  # - path: [exact/path/to/file.ext]
  #   timestamp: [YYYY-MM-DD-HH-MM-SS]
  #   purpose: [why created]

files_modified:
  # - path: [exact/path/to/file.ext]
  #   lines_changed: [start-end or "multiple sections"]
  #   timestamp: [YYYY-MM-DD-HH-MM-SS]
  #   backup_location: [if backed up]

files_read:
  # - path: [exact/path/to/file.ext]
  #   purpose: [why needed]
```

### 14. Test Commands & Verification
**Exact commands to verify work - no user interaction required**

```bash
# Unit tests
test_command_1: "npm test specific.test.js"
expected_output: "All tests passing"

# Integration test
test_command_2: "curl -X GET localhost:3000/endpoint"
expected_output: "200 OK with JSON response"

# Verification
verify_command: "grep -r 'TODO' src/ | wc -l"
expected_output: "0 (no TODOs remaining)"
```

### 15. Autonomous Execution Instructions
**YOU ARE WORKING WITHOUT USER INTERACTION - Follow exactly:**

1. **On Start:**
   - **VERIFY CODEBASE STATE FIRST** - Run all verification commands from section 6
   - If verification fails, STOP and mark as BLOCKED with details
   - Update STATUS to IN_PROGRESS
   - Set AGENT and timestamp
   - Read all files listed in "Execution Context" section

2. **During Work:**
   - Check off subtasks as completed
   - Update files log after EVERY operation
   - Save work order every 5 minutes
   - If blocked, mark with ❌ and reason

3. **If Context Low:**
   - Update CONTEXT_REMAINING
   - Save all work immediately
   - Mark current task as 🔄
   - Create minimal handoff with WO path

4. **On Completion:**
   - Run ALL test commands
   - Update STATUS to COMPLETED
   - Add review notes if needed

### 16. Recovery Instructions
**If picking up incomplete work:**

1. Check RESUME_AT location
2. Verify files in operations log exist
3. Continue from last unchecked subtask
4. Validate previous work before proceeding

### 17. Review Section (Post-Completion)
**[Filled after work complete]**

- **Completed By:** [Agent] @ [Time]
- **Actual vs Estimated:** [Time/complexity comparison]
- **Issues Encountered:** [Any problems not anticipated]
- **Follow-up WOs Created:** [List any spawned work orders]

## PHASE 3 - SAVE AND TRACK

### File Management
1. **Get Project ID:**
   ```bash
   # Check for PROJECT-ID.md
   if [ -f "PROJECT-ID.md" ]; then
     PROJECT_ID=$(grep "^id:" PROJECT-ID.md | cut -d: -f2 | xargs)
   else
     # Create PROJECT-ID.md from template if missing
     echo "⚠️ PROJECT-ID.md missing - creating from template"
     cp ~/.agents/templates/PROJECT-ID.md ./PROJECT-ID.md
     # Use directory name as fallback
     PROJECT_ID=$(basename "$PWD" | tr '[:upper:]' '[:lower:]' | tr ' ' '-')
     echo "Using directory-based ID: $PROJECT_ID"
   fi
   ```

2. **Generate timestamp:** Get current timestamp in format `YYYY-MM-DD-HH-MM-SS` using utility script
   ```bash
   TIMESTAMP=$(~/.agents/scripts/get-filename-prefix.sh)
   ```

3. **Determine sequence:** If multiple work orders from same conversation, use -001, -002, etc.
   ```bash
   # Check for existing WOs with same project+timestamp prefix
   EXISTING_COUNT=$(ls .dev/ai/workorders/WO-${PROJECT_ID}-${TIMESTAMP}-*.md 2>/dev/null | wc -l)
   SEQUENCE=$(printf "%03d" $((EXISTING_COUNT + 1)))
   ```

4. **Build Work Order ID:**
   ```bash
   WO_ID="WO-${PROJECT_ID}-${TIMESTAMP}-${SEQUENCE}"
   # Example: WO-agents-system-2025-10-08-12-30-45-001
   ```

5. **Create directory:** `mkdir -p .dev/ai/workorders/`

6. **Save location:** `.dev/ai/workorders/${WO_ID}.md`

7. **Write file:** Save complete work order to disk

8. **Confirm save:** Explicitly verify file was written successfully

### Tracking Integration
After saving, execute tracking command:
```bash
~/.agents/scripts/track-project.sh "[project-name]" "Work order created" \
  "WO: [work-order-title]" "[agent-name]"
```

**Completion Tracking**: When this work order is completed, the system will automatically:
1. Create an accomplishment entry in `.dev/ai/accomplishments/`
2. Update the accomplishments index
3. Track completion in the project system
4. Link to related changelogs and audits

Parameters:

- Project name: From context or "general"
- Action: "Work order created"
- Details: Work order title
- Agent: Current agent name
- Prompt: "create work order"
- Related files: Leave empty
- Reference URI: Absolute path to saved work order with `file://` prefix

## PHASE 4 - FINAL OUTPUT

Present the complete work order wrapped in markers:

```
** WORK ORDER START **

# Work Order: [Title]
**Order ID:** WO-[PROJECT-ID]-[YYYY-MM-DD-HH-MM-SS]-[seq]
**Generated:** [Timestamp]
**Status:** Ready for Execution
**Saved to:** [Full path to saved file]
**Tracked in:** [Project name]

[All sections from Phase 2]

## Agent Pickup Instructions
This work order is complete and ready for any agent to execute.
All necessary context from the conversation has been captured above.

---

## 🚨 MANDATORY: Upon Work Order Completion

**When you complete this work order, you MUST register the accomplishment:**

```bash
~/.agents/scripts/create-accomplishment.sh \
  "[Work Order Title]" \
  "[Type: Feature Implementation|Bug Fix|Documentation|Testing|Refactoring]" \
  "[WO-ID]" \
  "[Your Agent Name]"
```

**This is REQUIRED. Do not mark work order as COMPLETED without creating accomplishment entry.**

**Example:**
```bash
~/.agents/scripts/create-accomplishment.sh \
  "Work Order Enforcement System Implementation" \
  "Feature Implementation" \
  "WO-agents-system-20251030-enforcement" \
  "Claude Code Sonnet 4.5"
```

After creating the accomplishment:
1. Update the accomplishment file with actual details (summary, work completed, technical details, impact)
2. Update work order STATUS to COMPLETED
3. Update accomplishments index (done automatically by script)

** WORK ORDER END **
```

# Output Rules
- Be comprehensive - include ALL context needed for execution
- Extract concrete details from conversation
- Make tasks independently executable
- Include verification methods for each task
- Preserve important decisions and rationale from discussion
- **ALWAYS confirm file was written and tracked successfully**
- Include file path and tracking confirmation in output

# Completeness Checklist
Before finalizing, verify work order has:

- [ ] All context from conversation captured
- [ ] Clear scope and objectives
- [ ] Executable task breakdown
- [ ] Success criteria defined
- [ ] Resources and references listed
- [ ] **Section 6 (Execution Context) is COMPLETE with:**
  - [ ] Absolute paths to ALL target files
  - [ ] Current state of each file documented
  - [ ] Verification commands to run before starting
  - [ ] Search patterns for locating code sections
  - [ ] List of files to read for context
  - [ ] Codebase state snapshot from conversation
- [ ] **Section 7 (Execution Graph) is COMPLETE with:**
  - [ ] Dependencies listed (or explicitly marked as empty)
  - [ ] Blocks listed (or explicitly marked as empty)
  - [ ] Parallelization analyzed and documented
  - [ ] Execution mode specified (serial/parallel/conditional)
  - [ ] Prerequisites defined with verification commands
- [ ] No critical information missing
- [ ] **Sub-agent could execute this with ZERO additional context**
- [ ] **Agent orchestrator can determine serial vs parallel execution**

# Review Prompt
After presenting the work order, confirm:
"✅ Work order saved to: [path]
✅ Tracked in project: [project-name]

Options:

- 'approve' to mark ready for execution
- 'split' to create multiple work orders
- 'revise [section]' to modify specific parts
- 'expand [task]' for more detail on a task"
