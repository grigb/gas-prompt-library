# Orchestrator Pattern — Dispatch Through Work Orders

Observed: The owner corrected a Grant Engine orchestration thread because the Orchestrator appeared to be doing implementation work inline.

Pattern: When assigned Orchestrator role, treat implementation as worker-owned by default. Mark existing ready WOs in progress, spawn native workers with exact WO/result paths and disjoint write scopes, update parent-owned ledgers/status surfaces, and keep inline work to orchestration state only.

Scope: global-candidate.
