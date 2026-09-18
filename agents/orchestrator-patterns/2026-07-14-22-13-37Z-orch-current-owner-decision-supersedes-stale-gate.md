---
id: P-033
category: CLEANUP
trigger: "when a current owner correction conflicts with an older approval, gate, or recommendation artifact"
source_session: 2026-07-14
scope: global-candidate
---

# P-033: Current Owner Decision Supersedes Stale Gate

**Action:** Treat the current explicit owner correction as authoritative for the active scope, reconcile the older approval/gate and every dependent WO, blocker, worker, heartbeat, and recommendation before dispatching or advising the next step.

**Why:** MACUSE retained an older approval to test Cua after the owner had decided not to use Cua, causing a stale WO-110 recommendation and obscuring whether `agent-desktop` was actually working.

**Examples:** Mark the obsolete engine-specific gate terminal, preserve its historical evidence, retire its worker/control claims, and route the still-valid product outcome into clean successor work orders.
