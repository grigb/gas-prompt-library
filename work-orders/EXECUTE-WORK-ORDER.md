# Execute Work Order Protocol

You are executing a work order autonomously. NO USER INTERACTION AVAILABLE.

**Git & Commit Rules**: See `~/.agents/docs/GIT-OPERATING-RULES.md`
- No automatic commits without explicit approval
- NO branch creation without permission
- ZERO AI ATTRIBUTION POLICY on all commits
- Always pause and ask before git operations

## Starting Execution

### MANDATORY VALIDATION FIRST
```bash
# Validate work order completeness BEFORE starting
~/.agents/scripts/validate-work-order.sh .dev/ai/workorders/[WO-ID].md

# If validation fails:
# - STOP immediately
# - Report validation errors to user
# - DO NOT attempt execution
# - Request work order be fixed
```

**If validation passes:**

1. **Load work order**: Read from `.dev/ai/workorders/[WO-ID].md`
2. **Read all context files**: Read every file listed in "Read First" (Complex/Standard tier) or referenced in Scope
3. **Run verification commands**: Execute ALL commands from "Verification" section
4. **If verifications fail**: STOP and mark as BLOCKED with details
5. **Resume or start**: Begin first task, or resume from last incomplete task
6. **Update status**: Set STATUS to IN_PROGRESS, update AGENT and timestamp

### 📊 OPTIONAL: CREATE PM TRACKING TASK

For substantial work orders (30+ minutes), create a tracking task:

```bash
# Extract work order details
WO_TITLE=$(grep "^# " .dev/ai/workorders/[WO-ID].md | head -1 | sed 's/^# //')
WO_ESTIMATE=$(grep "Estimated effort:" .dev/ai/workorders/[WO-ID].md | grep -oE '[0-9]+' | head -1)

# Create task in PM system
PM_TASK_ID=$(~/.agents/tools/project_manager/backend/update-pm-state.sh \
    --project "$(basename $PWD)" \
    --create-task \
    --title "$WO_TITLE" \
    --description "Work order [WO-ID]" \
    --status in_progress \
    --estimate-minutes "$((WO_ESTIMATE * 60))" \
    | grep "Task #" | grep -oE '[0-9]+')

# Save task ID to work order metadata section for completion tracking
echo "PM Task ID: $PM_TASK_ID" >> .dev/ai/workorders/[WO-ID].md
```

**Benefits:**
- Real-time progress visible in dashboard
- Unified task tracking across all work
- Historical record of work completed

## During Execution - Critical Rules

### Progress Tracking:
- Check off subtasks as completed
- If blocked on a task, mark it and move to next independent task
- Document any issues encountered for the Completion section

## Low Context Protocol

When context window drops below 30%:
1. Save all work immediately
2. Note exact stopping point in the WO body
3. Create handoff with WO path: "Continue WO at [path]"

## Completion Protocol

🚨 **CRITICAL: You MUST complete ALL steps below. Do NOT skip accomplishment registration.**

1. Run ALL test commands listed
2. Verify success criteria met
3. Update STATUS to COMPLETED
4. Update completion timestamp
5. Track in project system:
   ```bash
   ~/.agents/scripts/track-project.sh "[project]" "Work order completed" \
     "Completed: [work-order-id]" "[agent]"
   ```

### 6. 📊 UPDATE PM TASK STATUS (RECOMMENDED)
   ```bash
   # If you created a PM task at start, mark it done
   # Find task ID from work order metadata or database:
   PM_TASK_ID=$(grep "PM Task ID:" .dev/ai/workorders/[WO-ID].md | cut -d: -f2 | tr -d ' ')

   if [ -n "$PM_TASK_ID" ]; then
       ~/.agents/tools/project_manager/backend/update-pm-state.sh \
           --project "$(basename $PWD)" \
           --update-task \
           --task-id "$PM_TASK_ID" \
           --status done
   fi

   # Or create completion task if no tracking task exists:
   ~/.agents/tools/project_manager/backend/update-pm-state.sh \
       --project "$(basename $PWD)" \
       --create-task \
       --title "[WO-title]" \
       --status done \
       --description "Completed work order [WO-ID]"
   ```

### 7. 🚨 CREATE ACCOMPLISHMENT ENTRY (MANDATORY - DO NOT SKIP)
   ```bash
   # Extract title from work order
   WO_TITLE=$(grep "^# " .dev/ai/workorders/[WO-ID].md | head -1 | sed 's/^# //')
   WO_PRIORITY=$(grep "Priority:" .dev/ai/workorders/[WO-ID].md | cut -d: -f2 | tr -d ' ' | tr '[:upper:]' '[:lower:]')
   
   # Infer accomplishment type from title and priority
   # Check title for type keywords first (more accurate)
   if echo "$WO_TITLE" | grep -qiE "(doc|documentation|guide|manual|readme|spec)"; then
       WO_TYPE="Documentation"
   elif echo "$WO_TITLE" | grep -qiE "(test|testing|spec|coverage|qa)"; then
       WO_TYPE="Testing"
   elif echo "$WO_TITLE" | grep -qiE "(refactor|restructure|cleanup|migrate)"; then
       WO_TYPE="Refactoring"
   elif echo "$WO_TITLE" | grep -qiE "(fix|bug|error|issue|resolve)"; then
       WO_TYPE="Bug Fix"
   # Fallback: Map priority to type (lower priority often = docs/testing)
   elif [ "$WO_PRIORITY" = "low" ]; then
       WO_TYPE="Documentation"
   else
       # Default for Critical/High/Medium priority work orders
       WO_TYPE="Feature Implementation"
   fi

   # Create accomplishment entry
   ~/.agents/scripts/create-accomplishment.sh "$WO_TITLE" "$WO_TYPE" "[WO-ID]" "[agent]"

   # Update the created file with actual details
   echo "📝 Update accomplishment entry with:"
   echo "   - Actual technical details (files modified, lines changed)"
   echo "   - Real impact assessment"
   echo "   - Validation results"
   echo "   - Links to changelogs and audits"
   ```
8. **VALIDATE ACCOMPLISHMENT SYSTEM**:
   ```bash
   ~/.agents/scripts/validate-accomplishments.sh
   ```

## Recovery Protocol (If Resuming)
1. **Verify previous work**:
   ```bash
   # Check files in operations log exist
   for file in [files_from_log]; do
     [ -f "$file" ] && echo "✓ $file" || echo "✗ MISSING: $file"
   done
   ```
2. **Start from RESUME_AT** location
3. **Re-run tests** for completed tasks to verify

## Autonomous Execution Rules

- No user to ask questions -- work from work order only
- If truly blocked, set status to BLOCKED and append a `## Blocker`
  section to the WO body with the blocker description
- Write a BLOCKED file to `.dev/ai/subtask-comms/` per the
  orchestrator's result protocol
- Document everything needed for the Completion section

## Recovery (If Resuming Incomplete Work)

1. Read the WO completely
2. Identify which tasks are already done (check outputs exist)
3. Continue from the first incomplete task
4. Re-validate previous work before building on it

## WO Format Reference

Work orders follow the tiered format defined in
`~/.agents/docs/standards/WO-FORMAT-STANDARD.md`. This execution
protocol applies to all tiers (Simple, Standard, Complex).
