---
id: P-004
category: CLEANUP
trigger: "After every batch of WO completions (3+ WOs closed)"
source_session: 2026-04-03
---

# P-004: Sweep for Untracked Work

**Action:** Launch an agent to scan all session artifacts, code TODOs, deploy warnings, QA notes, and plan gaps. Create WOs for anything found.
**Why:** Owner asked "create work orders for loose ends and anything untracked" multiple times. Loose ends accumulate silently.
**Examples:** After closing 5 WOs, launch a sweep agent that finds 3 undocumented TODOs and a deploy warning -- creates WOs for each.
