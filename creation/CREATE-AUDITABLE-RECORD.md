
Capture a legacy auditable record of this session using only this chat. Be explicit. No outside context.

# Legacy Compatibility Notice

This prompt is a legacy audit alias. It is **not** a routine session-close method and it is **not** a parallel alternative to `/close-session`.

If the user's goal is a normal end-of-session closeout, stop and use `~/.agents/prompts/creation/CREATE-SESSION-RECORD.md` instead.
Do **not** recreate the retired default pair of `CREATE-AUDITABLE-RECORD` + `HANDOFF` for routine closeout.

# Preferred Workflow Notice

This standalone audit prompt remains supported for backward compatibility, explicit user requests, and older audit-only integrations.

For routine session-close use, prefer the unified `/close-session` workflow via `~/.agents/prompts/creation/CREATE-SESSION-RECORD.md`.
Use this legacy prompt when the user specifically wants a standalone audit artifact or when an older audit-only workflow must be preserved.

# Automatic Save Behavior
**ALWAYS save the full audit automatically** - no prompts or triggers required.

# Control triggers (optional modifiers)
- **Paste option:** if the user message includes "paste", after saving also paste the long audit to chat within the markers.
- **Short only:** if the message includes "short only" → produce only the short summary and do not save (rare use case).

# Time window and filename
Determine the work window from files touched in this session, not the current time.

- Identify the first and last files touched (created or edited).
- Set `TS_START` and `TS_END` from their UTC modification times using format `YYYY-MM-DD-HH-MM-SS` (year-month-day-hour-minute-second).
  - For file modification times: `date -r <file> +%Y-%m-%d-%H-%M-%S` (note: `-r` flag for file modification time)
  - **CRITICAL**: Format MUST include seconds (`-SS` suffix) - use `%Y-%m-%d-%H-%M-%S` format
- Compute `DURATION = TS_END − TS_START` in minutes and days.
- Filename uses end time: `FILE="${TS_END}-conversation-summary.md"`.
- If no files were touched: set `TS_START=Unknown`, `TS_END=Unknown`. Do not save unless a save trigger is present; if saving with no files touched, use the shared timestamp script: `TS_END=$(~/.agents/scripts/get-filename-prefix.sh)` to get current UTC in `YYYY-MM-DD-HH-MM-SS` format.

# Step 1: Short summary to screen
Write Markdown in this exact order:
# Conversation Summary (Short)
**Time Window:** Start: TS_START, End: TS_END, Duration: DURATION
## Starting Point
[What was provided at session start: user request, handoff file read, work order specified, etc.]
[CRITICAL: Include full absolute paths to any files that were provided/referenced at startup]
## Key Actions
## Results
## Decisions
## Next Actions and Owners
## Open Questions

Short rules:

- Facts only. Concise bullets. 300 words max.
- Link or ID every artifact.
- Mark unknowns as "–=Unknown".
- No text before or after the markers.
- **Starting Point MUST include full paths** to any handoffs, work orders, or context files read at session start

Output to chat wrapped exactly with:
** CONVERSATION SUMMARY START **
<full markdown>
**Time Window:** Start: TS_START, End: TS_END, Duration: DURATION
** CONVERSATION SUMMARY END **

# Step 2: Long audit (ALWAYS - automatic save)
Order:
# Conversation Summary
**Time Window:** Start: TS_START, End: TS_END, Duration: DURATION
## Starting Point and Scope
[What initiated this session and what context was provided]

**CRITICAL - Include all of the following:**
- Initial user request or prompt (exact wording if possible)
- Handoff file read (if any): **full absolute path** (e.g., `~/project/.dev/ai/handovers/2025-10-10-15-30-handoff-project.md`)
- Work order executed (if any): **full absolute path** (e.g., `~/project/.dev/ai/workorders/WO-project-20251010-001.md`)
- Prior audit referenced (if any): **full absolute path**
- Any other context files or documents referenced at startup: **full absolute paths**
- Project rules file location (AGENTS.md, CLAUDE.md, etc.)
- Working directory at session start

**Purpose:** Future agents need to trace the chain of handoffs/work orders to understand project history.

## Actions Taken
## Results and Artifacts
## Decisions and Rationale
## Errors, Blockers, Mitigations
## Gaps and Risks
## Next Actions and Owners
## Open Questions
## Provenance Log

Long rules:

- **Starting Point section is MANDATORY and must include full absolute paths to all startup files**
- Cite every created/modified document, file, link, or ID with exact names and locations
- Include items that exist only in chat or system memory by converting them into explicit notes
- Record commands, prompts, parameter values, and configs that affected outcomes
- Use UTC ISO timestamps where relevant
- If a section has nothing to report, write "None"

Saving behavior (ALWAYS executed automatically):

- Create directory if needed: `mkdir -p .dev/ai/audits/`
- Save location: `.dev/ai/audits/${TS_END}-conversation-summary.md`
- **Save the long audit to this location** (automatic - no prompt required)
- Track in project system:
  ```bash
  ~/.agents/scripts/track-project.sh "[project-name]" "Audit created" \
    "Audit: [brief summary] - Duration: [duration]" "[agent-name]"
  ```

**Optional pasting:**
- If user requested "paste", wrap long audit in markers and paste to chat:
  - Start of paste: ** CONVERSATION SUMMARY START **
  - End of paste:   **Time Window:** Start: TS_START, End: TS_END, Duration: DURATION
** CONVERSATION SUMMARY END **

Tracking confirmation (ALWAYS show):
After saving, confirm:
"✅ Audit saved to: .dev/ai/audits/${TS_END}-conversation-summary.md
✅ Tracked in project: [project-name]"
