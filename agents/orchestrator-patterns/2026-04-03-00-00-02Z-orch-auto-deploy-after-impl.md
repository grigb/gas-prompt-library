---
id: P-002
category: BATCH_DELEGATION
trigger: "Any WO implementation completes with tests passing"
source_session: 2026-04-03
---

# P-002: Auto-Deploy After Implementation

**Action:** Immediately launch a deploy agent to push changes to VPS via the deploy script. Don't wait to be asked.
**Why:** Owner never wants to manually trigger deploys. Every successful implementation should be live ASAP.
**Examples:** WO completes, tests pass -- immediately launch deploy agent without asking.
