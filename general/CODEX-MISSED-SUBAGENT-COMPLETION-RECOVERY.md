# Codex Missed Subagent Completion Recovery

Paste the prompt below into the parent task that did not react to its child.
If more than one child is unresolved, name the intended child thread id or
agent path before pasting it.

## Ready-to-paste prompt

Perform one bounded, notice-independent lifecycle reconciliation for the exact
subagent whose completion this parent failed to assimilate.

Do not poll, wait, sleep, tail logs, repeatedly call status tools, scan broad
result directories, inspect unrelated sessions, launch a replacement, or
dispatch successor work. Use the child I named or the single exact unresolved
child in this parent's Open Codex Agents ledger. If that does not identify one
child uniquely, stop and ask me for its thread id or agent path.

Follow `/Users/grig/.agents/docs/protocols/codex-mac-native-worker-lifecycle.md`
and do this evidence-first pass:

1. Resolve the exact child thread id, child agent path, parent thread id,
   ledger entry, and named expected result artifact. You may inspect the native
   agent inventory once if available.
2. Read the exact named result artifact first. Then read the exact child's
   final message and lifecycle events from its one rollout file under either
   `/Users/grig/.codex/sessions/` or
   `/Users/grig/.codex/archived_sessions/`. Do not mine unrelated conversation
   content.
3. Read the exact parent rollout from child completion through the first later
   parent turn. Inspect `task_started`, matching inter-agent communication or
   subagent-notification records, `turn_aborted`, and `thread_rolled_back`.
4. If this Desktop launch used the completion-wake canary, inspect only the
   exact dated Desktop log and a bounded window around child completion for
   `codex_canary.completion_wake`, `codex.agent_communication`, the exact child
   id, and the exact parent id. Correlate send and receive by communication id.
   Also note any app-server disconnect/restart in that same window. Do not
   tail the log.
5. Classify the evidence using exactly these fields:
   - `CHILD_COMPLETE: yes|no|not-provable`
   - `RESULT_RECOVERED: artifact|final-message|none`
   - `PERSISTED_PARENT_RECEIPT: present|absent|not-inspected`
   - `PARENT_MAILBOX_DELIVERY: confirmed|failed-with-exact-error|not-provable`
   - `TRIGGER_TURN: true|false|not-provable`
   - `PARENT_WAKE: child-completion|user|heartbeat|other|none|not-provable`
   - `FIRST_POST-COMPLETION_PARENT_TURN: completed|aborted|rolled-back|none|not-provable`
   - `ASSIMILATION: completed|pending|blocked`
   - `CLEANUP: closed|close-ready|blocked`
6. Never infer `PARENT_MAILBOX_DELIVERY: failed` merely because the parent
   rollout lacks a receipt. In current V2 builds, enqueue is in memory and does
   not persist a receipt at enqueue time. A later parent turn can drain the
   item and then abort/roll back, erasing durable evidence. In that situation,
   report `PERSISTED_PARENT_RECEIPT: absent` and
   `PARENT_MAILBOX_DELIVERY: not-provable`.
7. Treat a correlated canary success plus receive event as confirmed mailbox
   enqueue. Treat a canary failure event as
   `failed-with-exact-error`. A send event without a receive event proves only
   sender acceptance, not parent enqueue.
8. Assimilate a valid terminal result into the already-authorized WO, ledger,
   and project state. Classify every child follow-up as `routed`, `completed`,
   `superseded`, `owner/external gate`, or `supervisor active`. Do not duplicate
   work that another lane has already advanced.
9. Call `close_agent` only if it is exposed and assimilation is complete. Do
   not describe `interrupt_agent` as closure. If native close is unavailable,
   leave the worker `close-ready` and say why.
10. Write one durable reconciliation artifact in the current project's
    `.dev/ai/orchestration/` directory. Report exact timestamps and absolute
    evidence paths, the corrected classifications, owner action required, and
    the already-authorized next step. Do not claim certainty beyond the
    retained evidence.

