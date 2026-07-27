# Agent Notification Contract (gas-notify)

**Purpose:** Drop-in prompt fragment. Paste the "Embed this" block into any agent's
prompt so it knows how to put a notification on the owner's Mac correctly, including
safe Claude click routing.

**What this documents:** the `gas-notify` CLI we built — a local, same-machine macOS
desktop notification helper for GAS agents. It writes a JSON payload, launches a native
GAS sender app, and the sender app posts the notification and handles the click.

- CLI: `/Users/grig/.agents/tools/agent-notify/bin/gas-notify`
- Human/setup docs: `/Users/grig/.agents/tools/agent-notify/README.md`
- Architecture/protocol: `/Users/grig/.agents/docs/protocols/notification-protocol.md`
- It is **local only** — not a relay, push service, email, or SMS. It does not replace
  durable status files, work-order results, or blocker records.

---

## Embed this in agent prompts

> **Notifying the owner.** When you need the owner's attention on this machine, send a
> macOS notification with the GAS notifier. Do **not** reimplement it.
>
> ```bash
> /Users/grig/.agents/tools/agent-notify/bin/gas-notify \
>   --title "<Project name>" \
>   --subtitle "<Your agent identity> - Workstream: <workstream> - <thread/WO/location>" \
>   --message "<short reason>" \
>   --notification-id "<short-slug>-$(date +%s)"
> ```
>
> **Three-line display contract** (these are the only lines the owner sees — make each count):
> - `--title` → the **project name** (e.g. `Agents System`, `LAN Platform`). Never a generic
>   label like `GAS`, `Notification`, or the reason.
> - `--subtitle` → **who you are + workstream + where to find you** (thread id, WO id, or path).
>   This is how the owner knows which agent/thread needs them.
> - `--message` → the **short reason**: `Owner input needed`, `Review gate`, `Blocked`,
>   `Work order complete`.
>
> **Temporary (default) vs persistent:**
> - Default is temporary (a banner). Use it sparingly — for routine progress/FYI/success,
>   prefer writing a durable artifact and sending nothing.
> - Add `--persistent` **only** when you have stopped at a human-in-the-loop gate and cannot
>   continue correctly without owner input (approval, blocking ambiguity, credential/payment/
>   security confirmation, or a destructive-action decision).
>
> **Click routing:**
> - **Codex agents:** `--target-harness codex --thread-id <conversation-id>` makes the click
>   reopen your exact Codex thread (`codex://threads/<id>`). This works — use it.
> - **Claude Code agents:** `--target-harness claude` focuses Claude Desktop only. It does
>   not resume, import, create, or resurrect a session. Put your thread id / WO in
>   `--subtitle` for visual orientation. If you want the click to land somewhere useful,
>   use `--open-url /abs/path/to/handoff-or-status.md`, or omit `--target-harness claude`
>   and use `--artifact-path /abs/path/to/handoff-or-status.md` so the artifact fallback opens.
>
> Use a unique `--notification-id` each send (the `-$(date +%s)` suffix) so repeated
> notifications don't overwrite each other's payloads.

---

## Reference (for the owner / tool maintainers)

### Full flag set
Required: `--title`, `--message` (alias `--body`).
Common: `--subtitle`, `--sound NAME`, `--temporary` (default) / `--persistent`
(aliases `--require-click`, `--sticky`), `--notification-id ID`, `--group ID`.
Click metadata: `--open-url URL`, `--activate-app BUNDLE_ID`, `--target-harness NAME`,
`--thread-id ID`, `--artifact-path PATH`, `--cwd PATH`, `--project NAME`, `--workstream NAME`.

### Click-routing priority (native app, first match wins)
1. `--open-url` → opens the URL/file.
2. `--target-harness codex` + `--thread-id` → `codex://threads/<id>`, then focuses Codex. **Works.**
3. `--target-harness claude` → focuses Claude Desktop only. It does not resume, import,
   create, or resurrect a session.
4. `--activate-app BUNDLE_ID` → just brings that app to the front (e.g.
   `com.anthropic.claudefordesktop`) without importing/resurrecting anything. Safe.
5. `--artifact-path PATH` → opens a durable file. Safe, and the recommended Claude click target.

Because step 1 wins over everything, setting `--open-url` is the clean way to give a
Claude notification a useful, side-effect-free click destination while also using
`--target-harness claude` for metadata. If you prefer `--artifact-path`, omit
`--target-harness claude` so the artifact fallback opens.

### Finding your own thread id
- **Claude Code:** `$CLAUDE_CODE_SESSION_ID` if exported, else the newest session file:
  `ls -t ~/.claude/projects/<project-slug>/*.jsonl | head -1` (strip dir + `.jsonl`).
  Use it as **subtitle text only**; Claude click routing focuses the app, not a specific thread.
- **Codex:** use the harness conversation id with `--target-harness codex --thread-id`.

### On-disk artifacts
- Payloads: `/Users/grig/.agents/data/agent-notify/payloads/<id>.json`
- Click records: `/Users/grig/.agents/data/agent-notify/clicks/`
- Sender app delivery events: `/Users/grig/.agents/data/agent-notify/app-events/`

### macOS setup (one-time, owner)
Send one temporary and one persistent test so both sender apps register, then in
`System Settings > Notifications`: set `GAS Notify Temporary` → Alert Style `Temporary`,
`GAS Notify Persistent` → Alert Style `Persistent`, and **Show previews → Always** for both
(otherwise the body shows as the literal word `Notification`). Rebuild apps if needed:
`/Users/grig/.agents/tools/agent-notify/bin/build-gas-notify-apps`.

### Do / Don't
- DO lead `--title` with the project; carry identity in `--subtitle`.
- DO reserve `--persistent` for true HITL gates.
- DO give Claude clicks a safe durable destination with `--open-url`, or with
  `--artifact-path` when not using `--target-harness claude`.
- DO use `--target-harness claude` only when focusing Claude Desktop is the desired click action.
- DON'T use this for routine success/progress — write a durable artifact instead.
- DON'T treat it as a network relay; it is local same-machine only.
