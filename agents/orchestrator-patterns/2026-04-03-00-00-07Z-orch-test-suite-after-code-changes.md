---
id: P-007
category: VERIFICATION
trigger: "Any agent modifies code in pm-module-social/src/ or pm-module-holochain/src/"
source_session: 2026-04-03
---

# P-007: Test Suite After Code Changes

**Action:** Run `npm run test:run` and `npx tsc --noEmit` immediately. If failures, fix before proceeding.
**Why:** Broken tests block everything. Catch them immediately.
**Examples:** Agent modifies 3 files in src/modules/ -- immediately run test suite before marking WO complete.
