---
id: P-020
category: BLOCKED_WO
trigger: "Owner uses a short supervisor relay trigger, or asks whether there is a block they can lift"
source_session: 2026-05-16
---

# P-020: Supervisor Relay And Real Blocker Registration

**Action:** When the owner says `unblocked`, `relay`, `supervisor`, `next`,
`go`, or gives a supervisor handoff/blocker/work-order path, read the newest
relevant project unblock artifact and resume through the normal orchestrator
queue without asking the owner to explain the unblock again. If no path is
provided, search the project `.dev/ai/unblocks/`, `.dev/ai/subtask-comms/`,
`.dev/ai/blockers/`, `.dev/ai/workorders/`, and orchestration handoff pointers
for the newest supervisor/unblock item.

**Action:** When investigation reveals a real owner/external dependency that is
not in the blocker index, create or update the blocker before reporting
blocked. Never say "there is no blocker" and then end with `I am blocked.`
Say "No blocker file existed; I found the blocker and registered it," then give
the compact owner/supervisor unblock action and blocker path.

**Why:** The supervisor is the cross-project unblock router, while the
orchestrator owns project execution. The owner should not have to paste long
context into project agents after the supervisor writes durable files, and the
blocker catalog must not be treated as exhaustive when a fresh investigation
finds a missing credential, cloud setting, secure value, owner action, or
upstream dependency.

**Examples:** If LAN maps need a Google Maps JavaScript Map ID and the blocker
index lacks that entry, register the map config blocker immediately instead of
saying "no active map blocker" and then claiming `I am blocked.` If the owner
later tells LAN `unblocked`, the orchestrator reads the latest supervisor
handoff/blocker update and resumes the map work without asking for a pasted
brief.
