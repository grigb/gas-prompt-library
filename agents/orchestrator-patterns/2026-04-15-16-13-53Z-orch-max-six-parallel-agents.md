---
id: P-017
category: BATCH_DELEGATION
trigger: "When planning or launching parallel work, cap live concurrent agents at six unless the owner explicitly overrides that limit"
source_session: 2026-04-15
---

# P-017: Maximum Six Parallel Agents

**Action:** Never launch more than six agents in parallel at once. Before starting a new batch, count currently active agents and only launch enough new workers to stay at or below six concurrent agents. If more work is ready, queue it in the orchestration plan and fire the next tranche only after active slots free up.

**Why:** The owner explicitly corrected the orchestrator to prevent over-parallelization. Excessive parallel agent counts make orchestration harder to reason about, increase collision risk, and burn attention on coordination overhead instead of throughput.

**How to apply:**
1. Before launching a batch, count active agents already running in the current orchestration.
2. If active count is 6 or more, launch nothing new until a slot clears.
3. If active count is below 6, launch only enough new workers to reach 6 total, never beyond it.
4. Record the cap in the orchestration log whenever it changes batching behavior.
5. Treat the six-agent ceiling as a hard owner directive unless the owner explicitly says otherwise.

**Examples:**
- If 4 agents are active and 5 independent WOs are ready, launch only 2 now and leave 3 queued for the next tranche.
- If 1 agent is active and 3 sidecar review tasks are useful, launching all 3 is acceptable because total concurrency becomes 4.
- If 6 agents are already running, do not launch a 7th just because it is independent; wait for a completion signal first.
