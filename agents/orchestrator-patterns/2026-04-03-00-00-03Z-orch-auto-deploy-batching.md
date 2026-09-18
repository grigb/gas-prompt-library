---
id: P-003
category: BATCH_DELEGATION
trigger: "Multiple WOs complete in close succession"
source_session: 2026-04-03
---

# P-003: Auto-Deploy Batching

**Action:** Batch deploys -- wait for the current batch of agents to finish, then deploy once with all changes. Don't deploy after every single WO.
**Why:** Deploying after every single change wastes VPS build time. Batch 3-5 changes per deploy.
**Examples:** 4 WOs finish within 10 minutes -- deploy once with all 4 changes, not 4 separate deploys.
