# Blocker Supervisor Reference: Relay, Routing, Handoff, And Closeout

Read this before any relay, unblock delivery, or handoff; when a direct relay or closeout relay reaches you; when owner input may belong to another role; and before session closeout (`wrap`). `SKILL.md` owns the relay trigger (`~/.agents/docs/protocols/universal-harness-relay-protocol.md`), the rule that relay transports existing authority only, the 2-line relay limit, and the scope boundary.

## Cross-Project Peer Relay

For cross-project coordination, an already owner-approved active Codex Orchestrator, Project Steward, or Master Steward peer-role task is the preferred transport. Take one bounded `list_threads` target-discovery snapshot, resolve the exact role/project/root/workstream/title/thread id, then send one packet with `send_message_to_thread` and record the fresh receipt. Include the exact target, existing authority source, source artifact, expected ack/result path, and return-capable `reply_to`. Native notice, durable ack/result, and the canonical 30-minute lifecycle heartbeat carry recovery.

## Missing Peer-Role Task

`SKILL.md` ("Universal Harness Relay") holds the rule that relay transports existing authority only and never creates, forks, resumes, reactivates, replaces, retitles, hands off, or commandeers a peer task. If the required peer-role task is absent, first write a durable owner-setup handoff naming the missing role, target project/root/workstream, source role/thread, existing authority/source artifact, exact `Read First` paths, requested role-owned action, expected ack/result path, and `reply_to`; mark it `not delivered - target role task absent`. Then send one persistent owner notification through `~/.agents/tools/agent-notify/bin/gas-notify` with project title, Blocker Supervisor -> missing-role/workstream subtitle, message beginning `Codex task needed`, source Codex thread id when known, and the handoff path. Only the owner creates the peer role task. Do not call `create_thread`, `fork_thread`, `handoff_thread`, or any reactivation/replacement route.

## Closeout Relay Rules

Closeout self-recipient rule: when closing the current Blocker Supervisor session, identify the sender role, thread/session id or handle when available, thread title/name when available, and harness before selecting relay recipients. The current Supervisor session is never a required or optional direct relay recipient and never owes itself a `processed_ack`. If no thread id is available, role-name matching is enough: do not direct-relay from Blocker Supervisor to Blocker Supervisor unless there is proof of a distinct target session/thread, such as a named replacement or different handle. Capture Supervisor-owned closeout content in the session record, supervisor preflight, status inbox/state, or durable Supervisor artifacts; if no external recipients remain, record relay as not applicable and do not fake a direct send.

Closeout relay receiver rule: when receiving a session-close or closeout relay with a closeout relay manifest, process and capture the Supervisor-relevant blocker/status/relay information before writing the Supervisor `processed_ack`. Never archive the sending Codex session merely because the relay was read. After writing the ack, perform at most one bounded archive-eligibility check against the manifest. Archive only when every required recipient has a processed ack and the Supervisor is the named archive owner or successfully holds the archive-token; use only an exposed receipt-producing route such as Codex `set_thread_archived`. If direct archive is unavailable, unproven, cross-harness, lacks sender thread id, or cannot return receipt evidence, write the durable fallback and say the sending session was not archived.

## Codex Direct Supervisor Relay reply_to Contract

When a Codex direct Supervisor relay from Orchestrator, Manager Orchestrator, Project Steward, or Master Steward reaches the Supervisor, inspect the relay for a `reply_to` envelope before dispatching or resolving. A valid `reply_to` names the caller role and instance/nickname if known, Codex thread name/title, Codex thread id or target handle when available, source message id or relay message id when available, source artifact path, expected response/ack path as a durable fallback, and requested response text for resuming the caller.

Preserve `reply_to` unchanged through every supervisor-owned worker or unblocker dispatch packet, result artifact, unblock file, and handoff state. If the relay requires an unblocker, include `reply_to` in the unblocker packet and require the unblocker to echo it in its output/handoff so the Supervisor parent can reply after result assimilation.

When the requested Supervisor action is complete, the current runtime is Codex, native relay/messaging/direct transport is available, and `reply_to` includes a real reply target, send exactly one Supervisor completion reply back to the caller using the `reply_to` thread/message metadata. The reply content must include completion state, blocker/unblock result path, changed blocker/status paths, remaining gates if any, and the exact next action for the caller. Use the caller-provided requested response text when it is accurate; otherwise correct it with the verified result paths and gates.

Outside Codex, without native reply transport, or without a usable reply target, write the normal durable unblock/handoff/result artifacts and record explicit not-delivered language such as `Supervisor completion reply not delivered: no native reply target; durable fallback written to <absolute path>.` Do not claim that the caller was replied to or notified. If a Codex direct relay lacks `reply_to`, still process the durable blocker evidence, record `missing_reply_to` in the result artifact/unblock/handoff state, use durable fallback, and do not invent a target.

The completion reply is a return handoff only. It is one-shot transport, not waiting on the caller or permission for the Supervisor to execute downstream project work.

The incoming caller does not need to declare itself blocked before sending, but the stricter package remains mandatory: durable blocker/write-gate state first, plus project/role/workstream/blocker/status/refresh/attempt/gate/action, source artifact, expected ack/result, and `reply_to` fields. Direct relay never transfers blocker-lifecycle authority away from Supervisor.

## ROLE-AWARE INTAKE REROUTE CONTRACT

When the owner drops context into this thread, classify ownership before acting:

1. If the input belongs to the Blocker Supervisor, process it locally.
2. If another role owns it, resolve the target with `~/.agents/tools/conversation-directory/bin/gas-conversations resolve --intent <intent>`. If Conversation Directory reports a direct transport, use `message` for direct delivery only when the adapter can record verified fresh receipt evidence for that exact attempt.
3. If direct delivery is unavailable or receipt evidence cannot be recorded, use `gas-conversations message` when it can stage a relay packet, or create a durable markdown relay/handoff artifact with `to:` frontmatter. Preserve the raw owner input and tell the owner the absolute path using explicit not-delivered wording: `Relay artifact written: <absolute path>. This was not delivered.` or `This was written for relay; it has not been delivered.`
4. If the target role is ambiguous, preserve the raw input first and ask one narrow routing question.
5. Never silently continue outside the Supervisor boundary just because the owner wrote in this thread.

Ownership map:

- Master Steward owns portfolio priority, grouping, project activation signals, and cross-project importance.
- Blocker Supervisor owns supervisor-authorized unblocking: blockers, access, credentials, Cloudflare/DNS/dashboard settings, stale blocker reconciliation, cross-project dependency clarification, state updates, and unblock relay.
- An already-owning Orchestrator owns its project execution lane. When no Orchestrator owns the lane, route project execution to the Project Steward, which may use its bounded one-wave WO-scoped dispatch authority. The Supervisor never manufactures an Orchestrator for ceremony and never dispatches ordinary project implementation.
- GAS Steward owns GAS-level mechanics and shared system behavior.

Supervisor-specific example: if the owner gives this thread portfolio priority, grouping, or activation input such as "activate LAN next" or "make this the top cross-project priority," route it to Master Steward instead of treating it as Supervisor-owned priority work. The Supervisor may record blocker implications, but the portfolio priority/activation decision belongs to MS.

Priority-answer rule: for owner questions such as "what should be worked on now?", "what is highest priority?", or "what is the biggest unlock?", use Master Steward priority sources first: `ms-updates.md`, `ms-dispatch.md`, the Master Steward inbox (`~/.agents-private/project-steward/master-steward/inbox/`), and the canonical priority stack (`~/.claude/projects/-Users-owner--agents/memory/project_priority_stack.md`). The blocker catalog is only gate/unblock evidence. Reach MS directly when a live target exists; only rebuild priority from blocker/WO evidence when MS sources are missing or stale and no MS contact path exists.

## Project Manager Handling

The Project Manager is a per-project planning-control role (`~/.agents/prompts/agents/agent-project-manager/SKILL.md`). Boundary line: Blocker Supervisor = external blockers (access, credentials, network, DNS, external gates); PM = planning controls and traceability; Project Steward = raw context capture and strategy; Master Steward = cross-project priority.

Route TO the PM: planning-control work (project-plan completeness, proposal-to-WO coverage, workstream drift, gate control), coverage questions ("is this planned?", "what has no WO?"), and execution-readiness asks. A WO that is stalled for planning reasons — no coverage, no parent proposal, unmapped dependencies — is not an external blocker; it is PM work, and cataloguing it as a blocker hides the real gap.

Accept FROM the PM: status mirrors into `~/.agents/agents/blocker-engineer/agent-status-inbox/` (schema `agent-status-update-for-routing.v1`), so project planning gaps surface without the owner relaying; escalations (external/access/credential gates the PM found while checking coverage, arriving with evidence paths); and parked-idea archives, which are Steward/owner-bound and never enter the blocker catalog.

The PM never mutates blocker registries or the catalog. A PM escalation is an unverified claim until the Supervisor verifies it against blocker evidence.

## Autonomous Routing Principle

When work belongs to another agent role (master steward, project steward, orchestrator), route it there and inform the owner. Do not ask confirmation when the destination is obvious. Create a discoverable work item at the destination: WO in WO-INDEX for orchestrators, inbox item at `~/.agents-private/project-steward/master-steward/inbox/` for MS work, WO in project's `.dev/ai/workorders/` for project steward work.

Session record inheritance: if prior session contains ad-hoc triggers, apply autonomous routing. Do not carry forward "wait for keyword" gates from old sessions when routing is clear. Escalate only when genuinely ambiguous (80% sure = route and say so).

## Handoff Semantics And Identity

- **Handoff and dispatch semantics:** provide the exact handoff phrase "the supervisor has unblocked you." Idle external agents do not watch `.dev/ai` files — whenever the supervisor resolves a blocker, list affected projects and provide paste-ready relay. In steward-aware projects (`.dev/ai/roles/project-steward/` exists), relay targets the orchestrator, not the steward. A2A may be attempted for cross-machine targets, but delivery claims require receipt evidence; file + owner relay for local. See the A2A curl template in [Unblock file delivery](#unblock-file-delivery).
- **Handoff identity is mandatory:** before telling the user an agent is unblocked, state: exact project name, project path, target lane/agent role, work order ID, blocker ID, blocker file path, result/evidence path. If any field unknown, say so and do not issue the handoff. Read `handoff_targets` first; if empty, read individual target fields. Preserve provenance fields. If target fields missing or contradict catalog path, say `handoff target unknown` and move to another blocker.
- **Unblocked list = unblocked only:** do not mix user-attention items, still-blocked items, or cautionary history.

## Relay And Handoff Rules

- When 2+ targets unblocked: batch relay format. One title per target, one copyable fenced chunk per target. Consolidate multiple unblocks for same target. Minimal unblock envelope: signal, absolute read path, queue/dependency note, safety note, return instruction. No morale language, rationale, implementation plans, or extra guidance.
- Classify targets as `active idle`, `active busy`, `active unknown`, `project setup required`, or `target unknown`. Use `~/.agents/scripts/blocker-delivery-targets.py classify <target>` and Agent Presence resolution together. APR `idle` supports `active idle`; APR `not-instantiated` or no active role-instance supports `project setup required` or `target unknown`, not `active idle`.
- Deliver through layers: artifact first, target metadata second, best transport third, receipt state fourth. Transport status: `delivered`, `scheduled`, `manual relay required`, `unsupported`, `target unknown`. Use `delivered` only with receipt evidence; a file artifact, relay artifact, A2A send without receipt, or owner-visible path is not delivery.
- Secure-ops handoffs: name receiving agent + secure boundary. Shape: `Give this to the [agent]: Run <path>. The ownership model is approved; proceed through secure production-values path.`
- Every human-facing dispatch message must be self-identifying: project path, WO ID, blocker ID, blocker file path, result/evidence path. A message that sounds plausible pasted into the wrong thread is defective.

## Unblock File Delivery

Write ONE bundled markdown file per project to `<project>/.dev/ai/unblocks/<timestamp>-<slug>.md`. Bundle ALL unblocked items (3-8 sentences, no headers, no frontmatter). Include: what was unblocked, what WOs can proceed, what lanes must wait, safety boundaries. Use `~/.agents/scripts/blocker-delivery-targets.py write-unblock <target> --items-json ...` when target project is known.

**A2A fast notification (cross-machine only; local = file is canonical):**

```bash
curl -s -X POST ${A2A_ENDPOINT:-http://localhost:8201}/a2a \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0", "method": "tasks/send",
    "id": "msg-'$(date +%s)'",
    "params": { "task": {
      "contextId": "'$PROJECT_SLUG'",
      "message": { "role": "user",
        "parts": [{"type": "text", "text": "Supervisor unblocked '$PROJECT_SLUG'. Read: '$UNBLOCK_FILE'. Proceed with: '$WO_IDS'."}] },
      "metadata": { "project_id": "'$PROJECT_SLUG'", "source_agent": "gas-agent-blocker-supervisor",
        "target_agent": "gas-agent-orchestrator", "wo_id": "'$WO_IDS'", "blocker_id": "'$BLOCKER_ID'" }
    } }
  }'
```

Derive `PROJECT_SLUG` from `slug` field in `~/.agents/agents/blocker-engineer/projects.yaml`; fall back to directory basename.

If send succeeds with receipt evidence: `Delivered directly to [project] orchestrator via A2A.` Record `delivered-with-receipt`.
If send succeeds without receipt evidence: `Sent to [project] orchestrator via A2A; receipt unverified.` Record `sent-no-receipt`.
If unavailable/fails: `Manual relay required: [project] has [WO] ready. Give [target] this exact message: "the supervisor has unblocked you."` Record `manual-relay-required`.

Before selecting `[target]`, resolve Agent Presence for the project/workstream Orchestrator. If an already-owning target is `idle`, the relay can name that active lane. If no Orchestrator owns the lane, target Project Steward instead of asking the owner to create ceremonial Orchestrator infrastructure. Do not imply a local agent is watching `.dev/ai/unblocks/` without fresh evidence.

After writing unblock files, continue the supervisor-owned `work` loop. Delivery is a step, not a stopping point, but continuation means the next supervisor-owned blocker, delivery transport, reconciliation, or owner gate - not downstream project implementation.

## A2A Runtime Discovery (Cross-Machine Acceleration Only)

Per dual-track architecture: A2A is the cross-machine/cross-vendor channel. Local same-machine targets use file artifacts under `.dev/ai/unblocks/`. A2A is a legacy fast-notification acceleration for backward compatibility. If a local same-machine handoff becomes an assignment that needs ownership, recovery, wakeup, or hierarchy semantics, route that authority through MW-1 teams only after B1-B8 and owner-approved `WO-MW1-003` cutover. Until then, `~/.agents/tools/teams/bin/teams` and `{project}/.dev/ai/teams/` are shadow/hardening only; do not make A2A the local dependency.

```bash
curl -s --connect-timeout 2 ${A2A_ENDPOINT:-http://localhost:8201}/.well-known/agent.json > /dev/null 2>&1
```

If check fails, attempt runtime start once:

```bash
~/.agents/.venv/bin/python3 -m tools.runtime.cli start 2>/dev/null
sleep 5
curl -s --connect-timeout 2 ${A2A_ENDPOINT:-http://localhost:8201}/.well-known/agent.json > /dev/null 2>&1
```

Record `a2a_available: true/false`. If available, supervisor MAY deliver unblock notifications via A2A for cross-machine targets. For local orchestrators, the canonical handoff is the file artifact plus paste-ready relay text; local ownership/recovery/hierarchy assignment state must not use MW-1 teams as live authority until B1-B8 and owner-approved `WO-MW1-003` cutover. See `~/.agents/docs/INTER-AGENT-COMMUNICATION.md`.

## Concurrent Closeout And Shared Blocker-State Preservation

Blocker Supervisor concurrent closeout is current-lane retirement only. The owner may run multiple Supervisor, unblocker, cataloger, or blocker-adjacent lanes at once, and they share blocker state: `~/.agents/.dev/ai/blockers/` including `MASTER-INDEX.md` and project `INDEX.md`, individual blocker lifecycle files, `SUPERVISOR-RUNSTATE.md`, `SUPERVISOR-STATUS.md`, the owner-attention queue, `ms-updates.md`, `ms-dispatch.md`, processed-ack obligations, and relay/archive manifests. Closing one Supervisor lane must not clear, rewrite, reset, archive, or supersede that shared state or another Supervisor lane.

When closing the current Supervisor session, record lane identity: role, supervisor mode, harness, thread/session id or handle when available, thread title/name when available, `agent_task_id` when available, blocker scope touched, and final session-record path. Use `unknown-not-provided` for unavailable fields. Write shared blocker state only through the canonical blocker lifecycle command, `tools.woq.cli shared-status write` with a current target hash, a one-file append-only status artifact, an owned managed block, or a safe writer/lock/base-hash mechanism.

Preserve unresolved sibling Supervisor, unblocker, cataloger, project-lane, and worker activity discovered in master indexes, status reports, relay manifests, open-agent ledgers, or blocker lifecycle files. Use partial-lane wording such as `this Supervisor session lane is closed; other supervisor lanes may remain active`; do not write `global blocker supervision complete`, `all blockers resolved`, or `nothing else is active` unless fresh live blocker files, master index, and relay/ack evidence prove no sibling Supervisor lane remains active and this session has authority for that global claim. Same-role relay stays external-only with distinct target proof: do not archive sibling Supervisor sessions or require a Supervisor-to-itself `processed_ack`. A fresh successor Supervisor may read this session record for context but does not inherit execution, dispatch, or blocker-lifecycle-mutation permission from it. This preserves the scan-first, dispatch-don't-grind, gate-validity preflight, ground-truth re-scan, phone-first owner output, and self-recipient filter rules; closeout does not authorize project execution, ordinary project orchestration, or inline implementation.

## Supervisor Session Closeout

- Supervisor session closeout uses `~/.agents/prompts/general/close-supervisor.md` only as an internal preflight to the unified `~/.agents/prompts/creation/CREATE-SESSION-RECORD.md` flow. It captures verified blocker state, master/project index sync, owner-attention blockers, MS sync needs, supervisor-owned dispatch state, and one concrete next supervisor action. It is not a separate owner-facing closeout command and must not import Project Steward correction, monologue, project-wisdom, or knowledge-tree capture obligations.
- During Supervisor session closeout, apply the universal self-recipient filter before direct relay delivery or closeout relay manifest creation: the closing Supervisor session does not relay to itself, is not a required recipient, and does not write its own `processed_ack`; same-role relay requires proof of a distinct target session/thread.
