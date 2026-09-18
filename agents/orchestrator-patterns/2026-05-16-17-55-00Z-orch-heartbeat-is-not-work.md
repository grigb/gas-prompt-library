---
id: P-021
category: SESSION_LIFECYCLE
trigger: "Orchestrator dispatches Codex workers, creates a heartbeat, or ends with I am working"
source_session: 2026-05-16
---

# P-021: Heartbeat Is Not Work

**Action:** Treat a heartbeat automation as recovery only. It is not work, not
worker evidence, and not a reason to say `I am working.`

**Action:** Before ending with `I am working.`, pass the visible-work check:
name each active worker, its plain task, its expected result location, and its
runtime status. At least one worker must be `running` or `effective`, or the
orchestrator must be actively doing owner-requested work in the current turn.

**Action:** If a worker was dispatched but runtime status is unknown, do one
bounded reconciliation check when possible. If it still cannot be confirmed,
say "dispatched, cannot confirm running" and do not claim `I am working.`

**Action:** Keep the owner-facing dispatch report phone-sized. Do not end a
working turn with "Next step: wait for the worker." Waiting is not an owner
action.

**Why:** The owner reads the final status seal as the operational truth. A
heartbeat is only a delayed reminder. If no active worker is visible or
confirmed, saying `I am working.` makes the owner believe project work is moving
when the orchestrator may actually be idle.

**Example:** After creating a LAN TV map worker and a heartbeat, do not write
"I am working" unless the worker ledger says the worker is running/effective.
Use compact output such as:

```text
Working: TV Near Me map panel.
Worker: Euclid, running, result -> LAN subtask-comms.
Recovery: heartbeat registered.
I am working.
```

If the runtime cannot confirm active work:

```text
Started: TV Near Me map worker.
Cannot confirm: runtime visibility unknown.
Recovery: heartbeat registered.
I am blocked.
```
