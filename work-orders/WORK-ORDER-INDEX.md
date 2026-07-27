# Work Order Index Template

Generate and maintain a work order index for tracking all work orders in a project.

## File Location
Save to: `.dev/ai/workorders/WO-INDEX.md`

## Shared Status Write Boundary

`WO-INDEX.md` is a shared status surface, not a normal hand-edited scratch
file. Read-only inspection is allowed. Any write or status synchronization must
use one of these safe paths:

- **GAS root index:** use the WOQ shared-status safe writer with the current
  full target hash. If the safe writer refuses the update, write the proposed
  index text and the exact refusal to the worker result artifact for
  parent/session-owned assimilation.
- **Project-local index:** acquire the project-local `.WO-INDEX.lock/`, reread
  the index after acquiring the lock, write only the scoped entry/status change,
  and release only your own lock. On lock contention, write the proposed update
  to `index-pending/<role>/` or the exact result artifact instead of waiting or
  overwriting.
- **Workers, QA, and read-only agents:** default to result-artifact-only
  shared-status authority. Their status updates must name both the WO file
  change needed and the `WO-INDEX.md` synchronization needed through the
  authorized parent, steward, liaison, triage, or maintenance writer lane.

Generated-boundary exception: the exact owner-approved sections listed in
`/Users/grig/.agents/docs/protocols/woq-role-lifecycle.md` (currently
`woq-live-status`, and exactly `WO-GASECAP-20260714-001` through `006` in
`gas-external-capability-integration`) are scheduler-generated from trusted WOQ
lifecycle state plus WO files. Do not hand-edit them or create
`index-pending`/`*-index-proposed.md` work for them. Update the WO file only.
Every unflipped section continues to use the safe paths above.

## Update Triggers
- When creating new work orders
- When completing work orders
- When updating work order status
- During handoff creation
- On "show work queue" command

## Index Structure

```markdown
# Work Order Index
**Last Updated:** [YYYY-MM-DD-HH-MM-SS]
**Project:** [Project Name]

## Outstanding Work Orders

### Critical Priority
| WO ID | Title | Status | Created | Created By | Blocked By | Age |
|-------|-------|--------|---------|------------|------------|-----|
| WO-xxx | [Title] | NOT_STARTED | [Date] | [Agent] | - | [Days] |

### High Priority
| WO ID | Title | Status | Created | Created By | Blocked By | Age |
|-------|-------|--------|---------|------------|------------|-----|
| WO-xxx | [Title] | IN_PROGRESS | [Date] | [Agent] | WO-yyy | [Days] |

### Medium Priority
| WO ID | Title | Status | Created | Created By | Blocked By | Age |
|-------|-------|--------|---------|------------|------------|-----|

### Low Priority
| WO ID | Title | Status | Created | Created By | Blocked By | Age |
|-------|-------|--------|---------|------------|------------|-----|

## Completed This Session
| WO ID | Title | Completed | Completed By | Time Taken |
|-------|-------|-----------|--------------|------------|
| WO-xxx | [Title] | [Timestamp] | [Agent] | [Actual vs Est] |

## Blocked Work Orders
| WO ID | Title | Blocked On | Reason |
|-------|-------|------------|--------|
| WO-xxx | [Title] | External approval | Waiting for customer |
| WO-yyy | [Title] | WO-xxx | Depends on completion |

## Work Order Statistics
- **Total Outstanding:** [Count]
- **Completed Today:** [Count]
- **Blocked:** [Count]
- **Average Age:** [Days]
- **Completion Rate:** [Percentage]

## Discovered Work (Not Yet WO)
Items found during work that may need work orders:
- [ ] [Description of potential work]
- [ ] [Another item needing investigation]

## Work Order Relationships
```mermaid
graph TD
    WO-001 --> WO-003
    WO-002 --> WO-003
    WO-003 --> WO-004
    WO-004 --> WO-005
```
```

## Query Commands

Support these queries:

- "Show all outstanding work orders" → Display outstanding section
- "Show blocked work" → Display blocked section
- "Show work by priority" → Group by priority
- "Show oldest work orders" → Sort by age
- "Show work order dependencies" → Display relationship graph

## Maintenance Rules

1. **Never delete entries** - Move completed to archive
2. **Synchronize status through the safe boundary** when work order status
   changes: update the WO file only if your role has live-write authority, and
   synchronize `WO-INDEX.md` through the safe writer, project-local lock, or
   result-artifact fallback.
3. **Track all WOs** - Including those from previous sessions
4. **Age calculation** - Days since creation
5. **Relationship tracking** - Update blocks/blocked-by

## Archive Location

Completed work orders older than 7 days move to:
`.dev/ai/workorders/WO-ARCHIVE.md`

## Integration Points

- **With Handoffs:** Pull outstanding WO list from here
- **With Proposals:** Add generated WOs here
- **With Tracking:** Reference this in project tracking
- **With Reviews:** Update effectiveness scores here
- **With Accomplishments:** Auto-create accomplishment entries when WOs complete
- **With Changelogs:** Link to detailed change documentation

## Index Update Command

```bash
# After any WO status change
echo "Updated WO-xxx status to COMPLETED" >> .dev/ai/workorders/WO-CHANGELOG.md
# Synchronize WO file status and WO-INDEX.md through the allowed role boundary:
# - GAS root: WOQ shared-status safe writer with current full target hash
# - project-local: .WO-INDEX.lock/ + reread-after-lock + scoped update
# - worker/QA fallback: proposed WO file status and index sync in result artifact
# Track change
~/.agents/scripts/track-project.sh "[project]" "WO Index updated" \
  "[change summary]" "[agent]"

# If status changed to COMPLETED, create accomplishment entry
if [[ "$NEW_STATUS" == "COMPLETED" ]]; then
  ~/.agents/scripts/create-accomplishment.sh "WO-xxx Title" "Feature Implementation" "WO-xxx" "[agent]"
  echo "Created accomplishment entry for completed WO-xxx"
fi
```
