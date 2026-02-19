# Keyboard Shortcut Audit Handoff

---
agent_task_id: ecc80dda_1771488591
created: 2026-02-19T08-09-53Z
project: hotgrids
type: handoff
status: IN_PROGRESS
priority: HIGH
---

# Handoff: hotgrids keyboard shortcut parity + cleanup

## Context Snapshot

You are continuing after an active keyboard shortcut audit for the V2 shortcut path and parity across gamer/original layouts.

The `F` key/fullscreen trigger is currently wired through the active stack, but there are likely still incomplete shortcut-system artifacts from previous refactors that should be cleaned up before finalizing this fix.

I paused after identifying implementation mismatches and type-level breakage.

## Immediate Findings

1. Active runtime stack is `App.tsx -> hooks/useKeyboardShortcutsV2.ts -> config resolver + config`.
2. `App.tsx` is passing `hasSelection` to `useKeyboardShortcuts` at `App.tsx:3931`, but V2 handler props do not declare that prop.
3. `npx tsc --noEmit` is currently failing in this area and also in unreferenced shortcut-rewrite files.
4. Files `hooks/useKeyboardShortcutsV3.ts`, `contexts/KeyboardActionContext.tsx`, and `components/KeyboardActionRegistrar.tsx` are present but not imported/used in `App.tsx` and expose action typing mismatches.
5. `components/KeyboardSettings.tsx` and `components/KeyboardHelpOverlay.tsx` share shifted/unshifted alias logic that marks some keys as enabled even when modifier state is not present.
6. `config/keyboardShortcuts.config.ts` looks internally consistent between `original` and `gamer` (55 actions each) and the V2 runtime action map covers all configured actions.

## Priority Next Actions

1. Fix type contract and unblock compile for keyboard path.
   - Update `hooks/useKeyboardShortcutsV2.ts` props to include or remove `hasSelection`, or remove that prop from `App.tsx` usage at `App.tsx:3931`.
   - Re-run `npx tsc --noEmit` and confirm zero keyboard-related errors.

2. Resolve dual shortcut-stack cleanup decision.
   - Decide whether V3/context/registrar files are intended as replacement architecture.
   - If not intended, remove unused dead-end files and references: `hooks/useKeyboardShortcutsV3.ts`, `contexts/KeyboardActionContext.tsx`, `components/KeyboardActionRegistrar.tsx`.
   - If intended, finish wiring and align `ActionName` + resolver contracts before they can be considered active.

3. Tighten on-screen key display parity.
   - In `components/KeyboardSettings.tsx`, review `getShortcutKeyAliases` and `keyToActions` behavior (around lines ~196-260) so shifted bindings do not falsely highlight unshifted keys.
   - In `components/KeyboardHelpOverlay.tsx`, apply the same parity logic in `getShortcutKeyAliases` and key state checks (around lines ~108-123 and ~165-195).
   - Validate that displayed key activation only lights keys with fully matching action+modifier combinations.

4. Verify keyboard parity audit against all modes/layouts.
   - Confirm action availability in `hooks/useKeyboardShortcutsV2.ts`, config, and active settings overlay for both presets.
   - Confirm overlay/action list parity for `gamer` and `original` in app by running in dev mode (`npm run dev -- --port 3007` from repo).

5. Produce final validation pass.
   - Run `npm run -s build` and keep as baseline.
   - Run `npx tsc --noEmit` and ensure the keyboard-related errors are no longer blocking.
   - Manually verify `F` fullscreen behavior and help/settings key map in both presets.

## Current Open Files with Scope

1. `App.tsx:3719-3949`
2. `hooks/useKeyboardShortcutsV2.ts:5-76`
3. `components/KeyboardSettings.tsx:196-260`
4. `components/KeyboardHelpOverlay.tsx:108-123, 165-195`
5. `config/keyboardShortcuts.config.ts` (both presets)
6. `hooks/useKeyboardShortcutsV3.ts` (unused)
7. `contexts/KeyboardActionContext.tsx` (unused)
8. `components/KeyboardActionRegistrar.tsx` (unused)

## Current Repo Signal

There are uncommitted changes in the working tree (`git status --short`) and two untracked audit/proposal/workorder documents in `.dev/ai/`. Do not assume clean baseline.

## Suggested Final Checks

1. `cd /Users/grig/work/hotgrids/repo/hotgrids && npx tsc --noEmit`
2. `cd /Users/grig/work/hotgrids/repo/hotgrids && npm run -s build`
3. `cd /Users/grig/work/hotgrids/repo/hotgrids && npm run dev -- --port 3007`

## QA Checklist

1. `F` key toggles fullscreen reliably on default and override bindings.
2. No visual key-map "ghost" enablements for shift-only bindings (e.g., keys that look active without required shift).
3. No stale shortcut actions listed in UI that do not execute.
4. No dead shortcut stack files left active/incomplete without clear path.

agent_task_id: ecc80dda_1771488591
