---
id: P-034
category: VERIFICATION
trigger: "before asking the owner to inspect a dashboard or other user interface after a sprint"
source_session: 2026-07-18
---

# P-034: Semantic UI Output QA Before Owner Handoff

**Action:** Require final QA to exercise the actual deployed interface and judge
the rendered words, counts, grouping, state transitions, reports, and user
meaning—not merely HTTP success, absence of console errors, control presence,
or fail-closed behavior. Do not ask the owner to inspect the interface until an
independent acceptance pass proves the output is coherent and actionable.

**Why:** A dashboard can be technically safe and error-free while still showing
contradictory, duplicated, misleading, or incomprehensible results. The owner
should not be the first person to discover those failures.

**Examples:** Compare a downloaded report with the latest on-page findings;
repeat the primary action twice; verify the same snapshot drives every summary;
separate health failures from proposed file changes; ensure disabled actions
name the exact blocker and next step.
