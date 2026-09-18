---
id: P-010
category: BLOCKED_WO
trigger: "Session start, or when authenticated API calls are needed"
source_session: 2026-04-03
---

# P-010: Auth Cookie Acquisition

**Action:** Obtain sl_session cookie via POST /api/auth/agent-login with the shared secret. Cache for the session (7-day validity).
**Why:** Many verification and QA steps require authentication. Get the cookie early, use it throughout.
**Examples:** Session starts -- immediately acquire auth cookie before any QA or verification tasks.
