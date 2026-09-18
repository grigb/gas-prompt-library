---
id: P-018
category: WORKSTREAM
trigger: "When a proposal, WO set, or rollout scaffold has just been created and execution is about to begin"
source_session: 2026-04-20
---

# P-018: Commit Boundary Before WO Launch

**Action:** Before launching execution on a newly created WO stream, verify that the stream-defining artifacts are already committed or otherwise isolated from the implementation work that follows. If the relevant scaffold is already committed, proceed immediately. If not, create or request a clean boundary before mixing implementation edits into the same change set.

**Why:** The owner explicitly required: commit first, then begin the work orders. This keeps planning/scaffolding changes distinct from implementation changes, reduces review ambiguity, and makes rollback/replay easier.

**Examples:**
- A proposal and six new WOs are created, then the owner says "begin the work orders" — first confirm the WO scaffold commit exists, then start `WO-001`.
- A rollout plan is drafted but uncommitted, and execution is requested — do not blend rollout creation and implementation into one ambiguous worktree if a clean boundary can be established first.
