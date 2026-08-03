# Orchestrator Pattern: Harness-Neutral Worker Heartbeat Is Thirty Minutes

Before closing a turn with unresolved Workers, unassimilated known results,
expected direct replies, or another known parent-resolvable reconciliation
condition, obtain a fresh same-parent heartbeat receipt using the current
harness adapter from:

`/Users/grig/.agents/docs/protocols/harness-native-worker-lifecycle-heartbeat.md`

Native completion notices remain first-class but are not heartbeat coverage.
The live default cadence is 30 minutes. Codex schedule/RRULE examples use:

`FREQ=MINUTELY;INTERVAL=30`

Claude uses a live current-session `/loop 30m` receipt or supported
CronCreate/schedule receipt. Registration or configuration files alone are not
coverage. Another harness uses a verified native same-session mechanism or
reports `unavailable`/`failed` coverage with durable recovery state.

Set the prompt/message payload exactly to
`Please check to see if the agents are done now.` and nothing else. On wake,
perform one bounded known-result reconciliation: exact result first, any
already-present notice without requiring one, native inventory once, exact
directly mapped child lifecycle state, then ledger plus concrete named
progress. No notice means unknown, never still-running. Preserve no-poll,
collision-safe identity, active-lane, current-session permission,
single-writer, Worker-result, and parent-only retirement rules.

Never mutate, retarget, pause, adopt, disable, or delete a foreign heartbeat.
Each exact owner migrates its own heartbeat at its next valid ownership
preflight.

The payload is immutable and gives no agent discretion. Never paraphrase it;
preserve its exact capitalization and final period. Compare the returned
automation snapshot or native receipt to the canonical payload. After the full
ownership preflight, the exact owner corrects the same heartbeat or deletes it
and reports failed coverage when the payload differs.
