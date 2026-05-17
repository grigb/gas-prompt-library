---
id: P-019
category: SESSION_LIFECYCLE
trigger: "A Codex orchestrator launches native background workers and is about to end the turn with unresolved workers"
source_session: 2026-05-09
---

# P-019: Register Codex Heartbeat Before Idle

**Action:** Before ending a Codex orchestrator turn with unresolved native
background workers, create or update the self-retiring heartbeat
automation for the current conversation workstream and log the automation id,
cadence, and active-worker reason. If the automation tool is unavailable, log
the exact runtime/tool reason before using `I am working.`

**Why:** Owner corrected that the orchestrator must not rely on the user or an
idle parent thread to notice background-worker completion. Launch evidence alone
is not enough to end a Codex worker-dispatch turn; the heartbeat is the required
temporary lifecycle bridge until a central event-driven completion bridge exists.

**Examples:** After spawning `WO-PMSL-2026-05-09-549`, register a 3-minute
heartbeat if local time is 06:30-21:59, or a 10-minute heartbeat if local time
is 22:00-06:29. When a heartbeat tick crosses a time window boundary, update the
existing automation in place. When all workers are closed, delete the heartbeat
immediately and log removal.
