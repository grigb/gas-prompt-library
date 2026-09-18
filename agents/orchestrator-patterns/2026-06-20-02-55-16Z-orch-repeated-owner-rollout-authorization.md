---
scope: global-candidate
agent: orchestrator
created: 2026-06-20T02:55:16Z
source_project: distributed-creatives-vault
---

# Pattern: Repeated Owner Rollout Authorization Is A Durable Unblock

When the owner says they have already given explicit authorization to run a production rollout work order and asks the orchestrator to work autonomously through the night, convert that message into durable unblock state immediately. Do not continue to preserve a prior "explicit authorization required" blocker unless the current message is ambiguous about the specific production mutation.

Correct response: resolve the authorization blocker, mark the rollout WO `IN_PROGRESS`, create or queue independent QA behind the rollout result, dispatch the rollout worker, and keep only unrelated time/input blockers active.
