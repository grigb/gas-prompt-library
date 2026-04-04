---
id: P-001
category: BATCH_DELEGATION
trigger: "Any time the orchestrator has 2+ independent tasks"
source_session: 2026-04-03
---

# P-001: Maximum Parallel Execution

**Action:** Launch ALL non-conflicting tasks in a single message with multiple Agent calls. Never serialize independent work.
**Why:** Owner repeatedly said "delegate in batches as quickly as possible in parallel" and "go all in parallel where logic permits". The orchestrator was launching tasks one at a time.
**Examples:** 5 independent WOs across different repos -- launch all 5 simultaneously instead of one at a time.
