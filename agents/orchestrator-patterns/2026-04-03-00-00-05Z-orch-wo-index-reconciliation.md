---
id: P-005
category: CLEANUP
trigger: "After every batch of WO status changes (3+ changes)"
source_session: 2026-04-03
---

# P-005: WO-INDEX Reconciliation

**SUPERSEDED FOR THE GAS ROOT (2026-08-12, WO-GAS-WOQLIVE-014).** The GAS root work-order index is generated from WOQ and is not hand-maintained: `/Users/grig/.agents/.dev/ai/workorders/WO-INDEX.md` is retired, the index is `/Users/grig/.agents/.dev/ai/workorders/WO-INDEX.woq-generated-view.md`, and hand-writes to it are refused. There is no index to reconcile there — it cannot drift from the WO files because it is rebuilt from them. Do not launch a reconciliation sweep against the GAS root index. To change what it says, change the Work Order file (`woq work-order write`). This pattern still applies to project-local `{PROJECT_ROOT}/.dev/ai/workorders/WO-INDEX.md`, which remains hand-maintained.

**Action (project-local only):** Launch an agent routed through `/Users/grig/.agents/tools/usage-management/scripts/select-model.sh` to reconcile a project-local WO-INDEX.md with actual WO file statuses. Fix stale entries.
**Why:** A hand-maintained WO-INDEX drifts from actual WO statuses during rapid execution. Owner shouldn't have to ask for this.
**Examples:** A project-local WO-INDEX shows 3 WOs as IN_PROGRESS but their files say COMPLETED -- agent fixes the index.
