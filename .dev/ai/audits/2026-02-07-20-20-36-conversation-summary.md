# Conversation Summary
**Time Window:** Start: 2026-02-07-20-14-00 (approx), End: 2026-02-07-20-20-36, Duration: ~7 minutes

## Starting Point and Scope

User reported that an agent overwrote a protected instruction file. Initial request: investigate what happened to `~/.agents/prompts/handoffs/HANDOFF.md` and restore the correct version.

- **Handoff file read:** `/Users/grig/.agents/prompts/handoffs/HANDOFF.md` (the file under investigation)
- **Working directory at session start:** `/Users/grig/.agents/prompts`
- **Project rules:** `/Users/grig/.agents/AGENTS.md` (referenced in global CLAUDE.md)
- **Global config:** `/Users/grig/.claude/CLAUDE.md`

## Actions Taken

1. **Read current HANDOFF.md** -- Found it contained a FusionZoo "Add Parts Crash Debug" session handoff instead of the handoff instruction template.
2. **Checked git history** in the `prompts` submodule (`git log -- handoffs/HANDOFF.md`) -- Identified 8 commits touching the file.
3. **Identified the damage timeline:**
   - `483e8e5` (2026-01-31) -- Last correct version. Contains the instruction template with `<!-- DO NOT OVERWRITE -->` HTML comment header.
   - `fc8b4d6` (2026-02-07 06:37) -- Agent committed over it with a "Client Report Narrative Generator" handoff. Commit message: `docs: add client report handoff`.
   - Working tree (uncommitted) -- Another agent overwrote it again with a FusionZoo "Add Parts Crash Debug" handoff.
4. **Restored the file:** `git checkout 483e8e5 -- handoffs/HANDOFF.md` -- Confirmed restoration by verifying the `DO NOT OVERWRITE` header.
5. **Investigated locking script:** Found `~/.agents/scripts/lock-system-files.sh` which uses `chflags uchg` (macOS immutable flag). Checked file flags with `ls -lO` -- no `uchg` flag was set, meaning the lock was not active when agents overwrote the file.
6. **Replaced HTML comment warning with visible markdown:** Changed the `<!-- -->` HTML comment block to a `#` heading + blockquote. HTML comments are invisible to LLMs processing markdown, which is likely why agents ignored the warning.

## Results and Artifacts

- **Restored file:** `/Users/grig/.agents/prompts/handoffs/HANDOFF.md` -- restored to `483e8e5` version then updated with visible markdown warning header.
- **Lock script found:** `/Users/grig/.agents/scripts/lock-system-files.sh` -- confirmed it targets HANDOFF.md but the `uchg` flag was not active.
- **Unlock script found:** `/Users/grig/.agents/scripts/unlock-system-files.sh`

## Decisions and Rationale

- **Restored to `483e8e5` not `fc8b4d6`:** Commit `fc8b4d6` was the first overwrite (client report handoff replacing the template), so we went back one further to the last version that actually contained the instruction template.
- **Replaced HTML comments with markdown blockquote:** HTML comments (`<!-- -->`) are stripped during markdown rendering and invisible to LLMs. A `#` heading and `>` blockquote will be parsed and seen by agents in their context window, making the "do not overwrite" instruction much more likely to be followed.

## Errors, Blockers, Mitigations

- **Root cause of overwrites:** Agents read the file path `~/.agents/prompts/handoffs/HANDOFF.md` and interpreted it as the destination for their session handoff, ignoring the (invisible) HTML comment warning. The instruction to save to `.dev/ai/handoffs/` was present but not prominent enough.
- **Lock not active:** The `chflags uchg` immutable flag was not set on the file when the overwrites occurred. Possible reasons: script was never run, or `git checkout` cleared the flag, or the unlock script was run. The flag would need to be re-applied after any git operation that replaces the file.

## Gaps and Risks

- The `uchg` flag needs to be re-applied now that the file has been restored and edited. User should run: `~/.agents/scripts/lock-system-files.sh`
- The `git checkout` operation will strip `uchg` flags (new inode), so the lock must be re-applied after any git restore.
- Other files in the `PROTECTED_FILES` list in the lock script may also be vulnerable.
- The committed overwrite at `fc8b4d6` still exists in git history. The current working tree fix needs to be committed.
- File is restored but not yet committed.

## Next Actions and Owners

1. **Commit the restored + updated HANDOFF.md** -- Owner: User
2. **Re-run lock script:** `~/.agents/scripts/lock-system-files.sh` -- Owner: User
3. **Consider adding a pre-commit hook** that rejects changes to protected files, as `uchg` flags don't survive git operations -- Owner: User

## Open Questions

- Was `lock-system-files.sh` actually run before the overwrites, or was it created but never executed?
- Should the lock script be integrated into a post-checkout or post-merge git hook to automatically re-apply after git operations?

## Provenance Log

- Session type: Interactive investigation and repair
- Agent: Claude Code (Opus 4)
- No prior handoff or work order -- initiated by direct user report
- Git operations performed in `/Users/grig/.agents/prompts` (submodule)
- Key commits examined: `483e8e5`, `fc8b4d6`
