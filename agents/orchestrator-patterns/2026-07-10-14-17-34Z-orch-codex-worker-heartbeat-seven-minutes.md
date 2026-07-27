# Orchestrator Pattern: Codex Worker Heartbeat Is Ten Minutes

When dispatching or waiting on unresolved native Codex workers, create or
update a current-thread heartbeat immediately with `automation_update`,
`kind="heartbeat"`, `destination="thread"`, and a ten-minute cadence.

Set its prompt/message payload exactly to
`Please check to see if the agents are done now.` The prompt must contain
nothing else. This is an immutable transport literal with no agent discretion:
match its exact capitalization and final period; never paraphrase, expand,
specialize, prefix, suffix, or substitute it. Compare the returned automation
snapshot prompt to this payload; immediately correct the same heartbeat or
delete it and report failed coverage if it differs. On wake, load the standing
lifecycle contract and perform its notice-independent evidence order for only
known workers: exact result first, any already-present notice without requiring
one, native inventory once, an exact directly mapped child lifecycle/session
record, then ledger and concrete named progress. No notice means unknown, never
still-running. The wake grants no new scope; resume only Orchestrator work
already authorized by the owner, role, and current runstate. Unchanged
nonterminal state uses the harness quiet heartbeat response.

Use an RRULE equivalent to:

`FREQ=MINUTELY;INTERVAL=10`

Do not use a different cadence unless the owner explicitly asks for one.

When the worker is assimilated and no Codex-resolvable wait remains, delete the
heartbeat in the same closeout pass.
