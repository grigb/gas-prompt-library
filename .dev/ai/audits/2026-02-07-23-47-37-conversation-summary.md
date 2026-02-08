# Conversation Summary
**Time Window:** Start: 2026-02-07-20-14-00 (approx), End: 2026-02-07-23-47-37, Duration: ~3.5 hours (interactive, not continuous)

## Starting Point and Scope

User reported that an agent overwrote the protected instruction file `~/.agents/prompts/handoffs/HANDOFF.md`. Task: investigate git history, restore the correct version, and harden the file against future overwrites.

- **File under investigation:** `/Users/grig/.agents/prompts/handoffs/HANDOFF.md`
- **Working directory at session start:** `/Users/grig/.agents/prompts`
- **Project rules:** `/Users/grig/.agents/AGENTS.md` (referenced in global CLAUDE.md)
- **Global config:** `/Users/grig/.claude/CLAUDE.md`
- **Auditable record instructions:** `/Users/grig/.agents/prompts/creation/CREATE-AUDITABLE-RECORD.md`
- **No prior handoff or work order** -- initiated by direct user report

## Actions Taken

1. **Read current HANDOFF.md** -- Found it contained a FusionZoo "Add Parts Crash Debug" session handoff instead of the handoff instruction template.
2. **Checked git history** in the `prompts` submodule (`git log -- handoffs/HANDOFF.md`) -- Identified 8 commits touching the file.
3. **Identified the damage timeline:**
   - `483e8e5` (2026-01-31) -- Last correct version. Contains the instruction template with `<!-- DO NOT OVERWRITE -->` HTML comment header.
   - `fc8b4d6` (2026-02-07 06:37) -- Agent committed over it with a "Client Report Narrative Generator" handoff. Commit message: `docs: add client report handoff`.
   - Working tree (uncommitted) -- Another agent overwrote it again with a FusionZoo "Add Parts Crash Debug" handoff.
4. **Restored the file:** `git checkout 483e8e5 -- handoffs/HANDOFF.md` -- Confirmed restoration by verifying the `DO NOT OVERWRITE` header.
5. **Replaced HTML comment warning with visible markdown:** Changed the `<!-- -->` HTML comment block to a `#` heading + blockquote. HTML comments are invisible to LLMs processing markdown, which is why agents ignored the warning.
6. **Found locking script:** `/Users/grig/.agents/scripts/lock-system-files.sh` -- uses `chflags uchg` (macOS immutable flag). At time of investigation, `uchg` flag was not set on HANDOFF.md.
7. **User re-ran lock script** -- Verified all 4 protected files now have `uchg` flag active. Write test confirmed: `operation not permitted`.
8. **Investigated lock script history** -- User clarified that another agent had previously fixed the lock script (it was broken before today's fix). The script only has one commit in git (`bef19d3`), so the fix was likely uncommitted or happened in another context.
9. **Created mid-session audit** at `/Users/grig/.agents/prompts/.dev/ai/audits/2026-02-07-20-20-36-conversation-summary.md`.

## Results and Artifacts

- **Restored file:** `/Users/grig/.agents/prompts/handoffs/HANDOFF.md` -- restored to `483e8e5` version, then updated with visible markdown warning header replacing invisible HTML comments.
- **Lock verified:** All 4 protected files confirmed locked with `uchg` flag:
  - `/Users/grig/.agents/AGENTS.md`
  - `/Users/grig/.agents/prompts/handoffs/HANDOFF.md`
  - `/Users/grig/.agents/prompts/handoffs/HANDOFF-MINIMAL.md`
  - `/Users/grig/.agents/prompts/handoffs/HANDOFF-DETAILED.md`
- **Mid-session audit:** `/Users/grig/.agents/prompts/.dev/ai/audits/2026-02-07-20-20-36-conversation-summary.md`
- **Lock script:** `/Users/grig/.agents/scripts/lock-system-files.sh` (working, previously broken, fixed by another agent)
- **Unlock script:** `/Users/grig/.agents/scripts/unlock-system-files.sh`

## Decisions and Rationale

- **Restored to `483e8e5` not `fc8b4d6`:** Commit `fc8b4d6` was the first overwrite (client report handoff replacing the template), so we went back one further to the last version containing the instruction template.
- **Replaced HTML comments with markdown blockquote:** HTML comments are invisible to LLMs. A `#` heading and `>` blockquote will appear in agents' context windows, making the "do not overwrite" instruction visible.

## Errors, Blockers, Mitigations

- **Root cause of overwrites:** Two contributing factors: (1) the `DO NOT OVERWRITE` warning was in HTML comments, invisible to LLMs; (2) the lock script was broken before today, so `chflags uchg` was never effectively applied.
- **Mitigations applied:** Visible markdown warning + working lock script re-applied by user.

## Gaps and Risks

- Restored HANDOFF.md is not yet committed in the prompts submodule.
- The committed overwrite at `fc8b4d6` still exists in git history.
- `uchg` flags don't survive git operations (checkout, pull, submodule update create new inodes). A post-checkout hook would make the lock persistent.

## Next Actions and Owners

1. **Commit the restored + updated HANDOFF.md** in the prompts submodule -- Owner: User
2. **Consider a git post-checkout hook** to auto-reapply `chflags uchg` after git operations -- Owner: User

## Open Questions

- Should the lock script be integrated into a post-checkout or post-merge git hook to automatically re-apply after git operations?

## Provenance Log

- Session type: Interactive investigation and repair
- Agent: Claude Code (Opus 4)
- No prior handoff or work order -- initiated by direct user report
- Git operations performed in `/Users/grig/.agents/prompts` (submodule)
- Key commits examined: `483e8e5`, `fc8b4d6`
- Earlier audit (superseded): `/Users/grig/.agents/prompts/.dev/ai/audits/2026-02-07-20-20-36-conversation-summary.md`
