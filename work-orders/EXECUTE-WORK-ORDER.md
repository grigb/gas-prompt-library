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
2. **Check progress**: Look at Execution Tracker section
3. **Run verification commands**: Execute ALL commands from Section 6 "Verification Commands"
4. **If verifications fail**: STOP and mark as BLOCKED with details
5. **Resume or start**: Find RESUME_AT location or begin T1
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

### After EVERY File Operation:
```yaml
# Add to files log immediately:
files_modified:
  - path: src/module.js
    lines_changed: 45-67
    timestamp: 2025-10-07-20-15
    backup_location: .backups/module.js.bak
```

### Progress Tracking:
- Check off subtasks: `- [x]` as you complete them
- Update task status: ⬜ → 🔄 → ✅ or ❌
- Save work order every 5 minutes minimum
- Update COMPLETE: X/Y tasks counter

### Use These EXACT Markers:
- `- ✅` Task complete
- `- 🔄` Currently working on this
- `- ⬜` Not started yet
- `- ❌` Blocked/Failed (add reason)

## Low Context Protocol
```yaml
# When context < 30%:
1. Update: CONTEXT_REMAINING: low
2. Save all work immediately
3. Mark current task as 🔄 (in progress)
4. Note exact stopping point in RESUME_AT
5. Create handoff with just: "Continue WO at [path]"
```

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

## Update Format for Quick Edits
Just update this block at the top of WO:
```yaml
# Quick Status (Update First)
STATUS: IN_PROGRESS
COMPLETE: 3/7 tasks
BLOCKED: none
RESUME_AT: T4 subtask 2
LAST_UPDATE: 2025-10-07-20-30
AGENT: claude-code
CONTEXT_REMAINING: medium
```

## CRITICAL: You Are Autonomous
- No user to ask questions
- Work from work order only
- If truly blocked, mark with ❌ and move to next task
- Document everything in the work order
- The work order IS your state - keep it current
