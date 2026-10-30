# Agent Notification Contract (gas-notify)

**Purpose:** Drop-in prompt fragment. Paste the "Embed this" block into any agent's
prompt so it knows how to put a notification on the owner's Mac correctly. A click opens
the exact session that asked.

**What this documents:** the `gas-notify` CLI we built — a local, same-machine macOS
desktop notification helper for GAS agents. It writes a JSON payload, launches a native
GAS sender app, and the sender app posts the notification and handles the click.

- CLI: `~/.agents/tools/agent-notify/bin/gas-notify`
- Human/setup docs: `~/.agents/tools/agent-notify/README.md`
- Architecture/protocol: `~/.agents/docs/protocols/notification-protocol.md`
- It is **local only** — not a relay, push service, email, or SMS. It does not replace
  durable status files, work-order results, or blocker records.

---

## Embed this in agent prompts

> **Notifying the owner.** When you need the owner's attention on this machine, send a
> macOS notification with the GAS notifier. Do **not** reimplement it.
>
> ```bash
> ~/.agents/tools/agent-notify/bin/gas-notify \
>   --title "<Project name>" \
>   --subtitle "<Your agent identity> - Workstream: <workstream> - <thread/WO/location>" \
>   --message "<what you need from the owner>"
> ```
>
> Add no path and no routing flag. `gas-notify` finds your session, and a click opens it.
>
> **A new Markdown file is not required in order to notify.** The notification text says
> what is needed, and the owner answers in your session. Decisions still go in their
> existing records, such as decision cards, blockers and work orders.
>
> **Three-line display contract** (these are the only lines the owner sees — make each count):
> - `--title` → the **project name** (e.g. `Agents System`, `LAN Platform`). Never a generic
>   label like `GAS`, `Notification`, or the reason.
> - `--subtitle` → **who you are + workstream + where to find you** (thread id, WO id, or path).
>   This is how the owner knows which agent/thread needs them.
> - `--message` → **what you need from the owner**, in words that make sense on their own:
>   `Approve the deploy to staging?`, not `Owner input needed`.
>
> **Temporary (default) vs persistent:**
> - Default is temporary (a banner). Use it sparingly. Send nothing for routine progress,
>   success, FYI, completion or Worker result notices.
> - Add `--persistent` **only** when you have stopped on a real owner/user action gate and no
>   owner-independent work remains: an approval, decision, answer, credential/access,
>   payment/security confirmation, destructive or production-impact confirmation, a missing
>   fact only the owner can supply, or explicit sign-off.
> - Do not notify for generic blocked states, waiting on workers/subagents or other
>   roles/projects, external non-owner gates, stale queues or ledgers, reconcilable state
>   drift, heartbeat recovery, or permission nags after direct owner action.
> - One narrow setup gate also qualifies: a required owner-approved Codex peer-role task is
>   absent **after** you wrote the durable owner-setup handoff. Only the owner can create that
>   role task. This is owner setup action, not generic waiting on a Worker, subagent, role, or
>   project. Use message `Codex task needed: create the approved <role> task for
>   <project/workstream>`, route the click to the source Codex thread when known, and include
>   the durable handoff path. Do not create/resume/reactivate/replace/commandeer the task or
>   tell a peer task to spawn.
>
>   Canonical missing-role notification pattern (run only after the handoff exists; omit
>   `--target-harness codex --thread-id ...` when the source Codex thread id is unknown):
>
>   ```bash
>   ~/.agents/tools/agent-notify/bin/gas-notify \
>     --title "<Project name>" \
>     --subtitle "<source-role> -> <target-role> | Workstream: <workstream> | <source-thread-or-WO>" \
>     --message "Codex task needed: create the approved <target-role> task for <project>/<workstream>. Read the owner-setup handoff." \
>     --persistent \
>     --target-harness codex \
>     --thread-id "<source-codex-thread-id>" \
>     --artifact-path "<absolute-owner-setup-handoff-path>" \
>     --project "<project>" \
>     --cwd "<absolute-project-root>" \
>     --workstream "<workstream>" \
>     --notification-id "codex-task-needed-<source-thread-id>-<target-role>-<unique-id>"
>   ```
>
> **Click routing (automatic):**
> - **Claude Desktop:** the click opens your exact session. `gas-notify` reads
>   `$CLAUDE_CODE_HOST_SESSION_ID`.
> - **Codex:** the click opens your exact thread. `gas-notify` reads `$CODEX_THREAD_ID`.
> - **Claude Code in a terminal:** the click focuses the terminal app only. No session link
>   exists. Name your location in `--subtitle`.
> - **No session (scheduled jobs):** the click opens `--artifact-path` if you give one.
> - To send the click somewhere else on purpose, pass `--open-url <url-or-absolute-path>`.

---

## Reference (for the owner / tool maintainers)

### Full flag set
Required: `--title`, `--message` (alias `--body`).
Common: `--subtitle`, `--sound NAME`, `--sound-volume N`, `--temporary` (default) / `--persistent`
(aliases `--require-click`, `--sticky`), `--notification-id ID`, `--group ID`.

### Sound
`--persistent` plays the house sound (`Hero`) automatically — those are gates that block
work, so they must be heard. `--temporary` is silent unless you pass `--sound NAME`, because
automation sends those constantly and a default there would be a noise storm. `--sound off`
silences either. `GAS_NOTIFY_DEFAULT_SOUND` gives both styles a default.

Sound plays via `afplay`, not the notification framework, so Focus/Do Not Disturb, the system
alert volume, and per-app notification permissions **cannot** suppress it. It follows output
volume only. Do not add your own `afplay` call — `gas-notify` already handles the audible cue.

### `--group` replaces, it does not label
Notifications sharing a `--group` id update the earlier one **in place**: no new banner, no
sound. Omit it unless replacement is what you want.
Click metadata: `--open-url URL`, `--activate-app BUNDLE_ID`, `--target-harness NAME`,
`--thread-id ID`, `--artifact-path PATH`, `--cwd PATH`, `--project NAME`, `--workstream NAME`.
`--dry-run` prints the payload and sends nothing.

### How the click target is chosen
`gas-notify` chooses at send time, first match wins:
1. `--open-url` or `--activate-app` from the sender.
2. `$CLAUDE_CODE_HOST_SESSION_ID` (`local_<id>`) → `claude://claude.ai/epitaxy/local_<id>`.
3. `$CODEX_THREAD_ID` → `codex://threads/<id>`.
4. Claude Code with no Desktop id → focuses the app in `$__CFBundleIdentifier` (the terminal).
5. `--artifact-path` → opens that file.

### Claude link behavior (probed 2026-10-30)
- Opens the exact session, including one off screen or in another sidebar group.
- An archived session opens and stays archived.
- An unknown id shows an empty pane and creates nothing.
- Never build `claude://resume` links. They import sessions and bring back deleted ones.
  `$CLAUDE_CODE_SESSION_ID` is a different id and does not work in the session link.

### On-disk artifacts
- Payloads: `~/.agents/data/agent-notify/payloads/<id>.json`
- Click records: `~/.agents/data/agent-notify/clicks/`
- Sender app delivery events: `~/.agents/data/agent-notify/app-events/`

### macOS setup (one-time, owner)
Send one temporary and one persistent test so both sender apps register, then in
`System Settings > Notifications`: set `GAS Notify Temporary` → Alert Style `Temporary`,
`GAS Notify Persistent` → Alert Style `Persistent`, and **Show previews → Always** for both
(otherwise the body shows as the literal word `Notification`). Rebuild apps if needed:
`~/.agents/tools/agent-notify/bin/build-gas-notify-apps`.

### Do / Don't
- DO lead `--title` with the project; carry identity in `--subtitle`.
- DO reserve `--persistent` for true HITL gates.
- DO treat a missing required owner-approved Codex peer-role task as a true HITL setup gate
  only after the durable owner-setup handoff exists; the owner creates the task.
- DO let `gas-notify` route the click. Add `--open-url` only to send it somewhere else.
- DON'T write a new Markdown file just to notify.
- DON'T use this for routine success/progress.
- DON'T use the missing-peer exception for generic waiting on Workers, subagents, roles, or
  projects, and don't use it to create, resume, reactivate, replace, or commandeer peer tasks.
- DON'T treat it as a network relay; it is local same-machine only.
