---
id: P-008
category: VERIFICATION
trigger: "Every VPS deploy completes"
source_session: 2026-04-03
---

# P-008: Live QA After Deploy

**Action:** Run authenticated curl checks against the deployed endpoints to verify changes are live. Use the agent-login cookie.
**Why:** Deploy success does not equal feature working. The owner expects live verification evidence.
**Examples:** Deploy completes -- curl the new API endpoint with auth cookie, verify 200 response with expected data.
