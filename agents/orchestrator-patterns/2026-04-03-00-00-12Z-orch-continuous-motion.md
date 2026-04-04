---
id: P-012
category: SESSION_LIFECYCLE
trigger: "All current agents complete and there's no user input pending"
source_session: 2026-04-03
---

# P-012: Continuous Motion

**Action:** Check WO-INDEX for NOT_STARTED or IN_PROGRESS WOs. If any are agent-executable, start them. If all blocked, create the handoff and report idle.
**Why:** Owner said "work autonomously throughout the night" and "don't stop at all". Idle time is wasted time.
**Examples:** All 5 agents finish -- check WO-INDEX, find 3 unstarted WOs, launch agents for all 3 immediately.
