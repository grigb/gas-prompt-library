# DC Relay Steward Result Contract

The DC Steward returns a declarative result file. The result file is the only
source the deterministic WhatsApp relay apply command may use to close inbound
items or enqueue outbound WhatsApp completions.

Do not embed executable code, shell commands, SQL, JavaScript, or free-form
instructions for the apply command. The apply command owns all side effects.

## Lifecycle Rotation Is Separate

Relay lifecycle rotation is controller work, not a WhatsApp result/apply side
effect. The DC Relay may include deterministic lifecycle metadata in the steward
handoff, but the `dc-relay-result/v1` file must not use `outbound_messages`,
`outbound_attachments`, `inbound_items`, or free-form apply instructions to
archive relay threads, create replacement relay threads, retarget heartbeats, or
reset relay lifecycle state.

The Steward/controller consumes these lifecycle fields from the relay handoff:

```yaml
lifecycle:
  rotation_due: true
  cycle_count: 100
  max_relay_cycles: 100
  relay_thread_id: codex-thread-old-relay
  relay_model: gpt-5.3-codex-spark
  relay_reasoning: high
```

When `rotation_due` is `true`, the Steward/controller must follow the lifecycle
rotation runbook:

`/Users/grig/work/obsidian-vault/distributed-creatives-vault/.dev/ai/processes/whatsapp/dc-relay-lifecycle-rotation-runbook.md`

Replacement relay creation must use model `gpt-5.3-codex-spark` and reasoning
`high`. The supported Codex app sequence is `set_thread_archived`,
`create_thread`, `set_thread_title`, `automation_update`, then verification. If
those tools are unavailable, report
`BLOCKED_RELAY_LIFECYCLE_CONTROLLER_REQUIRED`. Do not edit raw
`/Users/grig/.codex/automations` files and do not send WhatsApp directly.

## Result Location

Preferred private result directory:

`/Users/grig/.agents-private/whatsapp-live/relay-results/dc-vault/`

Filename:

`<batch_id>.json` or `<batch_id>.yaml`

## Required Shape

```yaml
schema_version: dc-relay-result/v1
batch_id: dc-relay-YYYYMMDDTHHMMSSZ-<short-id>
project_slug: dc-vault
created_at: "2026-06-13T00:00:00Z"
created_by: dc-steward
relay_agent: dc-relay
status: complete
summary: Short internal summary of what the steward decided.

inbound_items:
  - queue_item_id: 20260613T000000.000000000Z-example-dc-vault-inbound.md
    correlation_id: example-correlation
    source_message_id: example-source-message
    action: close_done
    reason: Covered by outbound_messages[0].

outbound_messages:
  - outbound_id: dc-relay-out-001
    target: whatsapp
    body: "Concise steward-authored WhatsApp response."
    reply_to_source_message_id: example-source-message
    covers_queue_item_ids:
      - 20260613T000000.000000000Z-example-dc-vault-inbound.md
    send_policy: enqueue_for_wa_live_daemon

outbound_attachments:
  - outbound_id: dc-relay-file-001
    target: whatsapp
    path: "/Users/grig/path/to/steward-brief.md"
    filename: "steward-brief.md"
    mime_type: "text/markdown"
    caption: "Steward brief attached."
    reply_to_source_message_id: example-source-message
    reply_to_source_sender: "15551230001@s.whatsapp.net"
    covers_queue_item_ids:
      - 20260613T000000.000000000Z-example-dc-vault-inbound.md
    send_policy: enqueue_for_wa_live_daemon

work_order_actions: []
blockers: []
audit_notes:
  - "Steward interpreted the batch as one request plus a correction."
```

## Allowed `status`

- `complete`: steward produced all needed close/enqueue decisions.
- `partial`: some items can be closed/enqueued and some must remain pending.
- `blocked`: no queue state should be closed except items explicitly listed
  with `action: mark_failed` or `action: leave_pending`.

## Allowed Inbound Actions

- `close_done`: deterministic apply command closes the inbound item as handled.
- `leave_pending`: item remains pending; include a reason.
- `mark_failed`: item failed; include a reason safe for audit.
- `mark_stale`: item is no longer actionable; include a reason.

## Allowed Outbound Target

Only `whatsapp` is accepted for this relay.

## Allowed Outbound Attachments

`outbound_attachments` is optional. Use it when the steward wants WhatsApp to
receive a local file attachment rather than only text.

Each attachment directive must include:

- `outbound_id`: unique within both `outbound_messages` and
  `outbound_attachments`.
- `target`: must be `whatsapp`.
- `path`: absolute local path to the file.
- `filename`: recipient-facing filename; if omitted, apply derives the basename.
- `mime_type`: valid MIME type such as `text/markdown` or `application/pdf`.
- `reply_to_source_message_id`: source WhatsApp message id for reply threading;
  if omitted, apply uses the covered inbound item source id when available.
- `covers_queue_item_ids`: one or more claimed inbound queue item ids.
- `send_policy`: must be `enqueue_for_wa_live_daemon`.

Optional attachment fields:

- `caption`: short document caption.
- `reply_to_source_sender`: sender JID for quoted-reply context when known.

Apply must reject an attachment before mutating queue state when `path` is
relative, missing, non-regular, empty, larger than 5,242,880 bytes, or when
`filename` is not a basename.

## Allowed Send Policy

Only `enqueue_for_wa_live_daemon` is accepted. The apply command should enqueue
outbound rows/items for the existing WhatsApp live daemon to send on its held
connection. The DC Steward and DC Relay must not connect to WhatsApp directly.

## Apply Command Contract

Target command, to be implemented by the WhatsApp live tool:

```bash
/Users/grig/.agents/tools/whatsapp-live/dist/wa-live dc-relay-apply \
  --result /Users/grig/.agents-private/whatsapp-live/relay-results/dc-vault/<batch_id>.json \
  --project dc-vault
```

Optional guarded attachment processing:

```bash
/Users/grig/.agents/tools/whatsapp-live/dist/wa-live dc-relay-apply \
  --result /Users/grig/.agents-private/whatsapp-live/relay-results/dc-vault/<batch_id>.json \
  --project dc-vault \
  --attachment-config /Users/grig/.agents/tools/whatsapp-live/config.gas-wa-live.json
```

The optional attachment path above is still a dry-run unless
`--send-live-attachments` is also present and the WhatsApp config send gates
allow the `--attachment-trigger` value. Live attachment posts must go through the
existing guarded `send-file` / `SendDocument` path and append to the send audit
log.

Expected behavior:

- validate schema version and project slug;
- validate every referenced inbound queue item exists in the canonical
  WhatsApp relay store;
- transition listed inbound items according to their allowed actions;
- create outbound WhatsApp completion rows/items for `outbound_messages`;
- validate and create outbound attachment rows/items for
  `outbound_attachments`;
- write an append-only audit record;
- fail closed if any referenced item is missing, duplicated, already closed in
  an incompatible state, has an invalid action, or references an invalid
  attachment.

If this command is missing or fails, the DC Steward or DC Relay must report
`BLOCKED_MISSING_APPLY_SCRIPT` or `BLOCKED_APPLY_FAILED` and must not hand-edit
the database.

## Batch Snapshot Command Contract

Target command, to be implemented by the WhatsApp live tool:

```bash
/Users/grig/.agents/tools/whatsapp-live/dist/wa-live dc-relay-batch \
  --project dc-vault \
  --format json
```

Expected behavior:

- atomically claim all currently new inbound items for the project into one
  relay batch;
- return one JSON object describing the claimed batch;
- preserve queue order by received/created time;
- include the raw message body and reply/quote context needed by the steward;
- include queue item ids and correlation/source message ids needed by the result
  contract;
- not contact the DC Steward;
- not close, fail, stale, or enqueue outbound items.

If this command is missing, the DC Relay must report
`BLOCKED_MISSING_RELAY_BACKEND_COMMANDS`.
