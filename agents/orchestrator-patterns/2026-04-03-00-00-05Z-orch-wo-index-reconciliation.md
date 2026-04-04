---
id: P-005
category: CLEANUP
trigger: "After every batch of WO status changes (3+ changes)"
source_session: 2026-04-03
---

# P-005: WO-INDEX Reconciliation

**Action:** Launch a Sonnet agent to reconcile WO-INDEX.md with actual WO file statuses. Fix stale entries.
**Why:** WO-INDEX drifts from actual WO statuses during rapid execution. Owner shouldn't have to ask for this.
**Examples:** WO-INDEX shows 3 WOs as IN_PROGRESS but their files say COMPLETED -- agent fixes the index.
