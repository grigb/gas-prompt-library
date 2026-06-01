# Steward Session Close — Mandatory Capture Before Retiring

Run this prompt before closing ANY steward session. It ensures nothing is lost
even if the steward skipped its turn-close checklist during the session.

## Instructions

You are about to close this session. Before producing a session record or
stopping, complete every step below. Do not skip steps. Do not say "already
done" without naming the file path. If a step produces no output, say
"N/A — nothing to capture" for that step.

### 1. Corrections

Scan this conversation for every owner correction ("don't do X", "stop",
"that's wrong", "no", "you should have", any frustration signal). For each:

- State what the owner corrected (one line)
- Create a memory file NOW if one does not already exist
- State the file path

If zero corrections: "No corrections this session."

### 2. Decisions

Scan for every owner decision ("approved", "go with X", "we're doing Y",
"use X", "defer", "kill", any choice made). For each:

- State the decision (one line)
- Record it in the appropriate artifact: decision-log.md, active-constraint.md,
  memory file, or WO status update
- State the file path

If zero decisions: "No decisions this session."

### 3. Monologues

Scan for any substantive owner monologue (3+ sentences of strategic thinking,
venting, planning, or context-sharing). For each:

- Save raw to `{PROJECT_ROOT}/.dev/ai/conversations/` if not already saved
- State the file path

If zero monologues: "No monologues this session."

### 4. New Facts

Scan for any new facts learned this session: credentials, paths, people,
relationships, constraints, tool behaviors, project state changes. For each:

- Store in the right layer: project-local memory, universal role memory, or
  private owner context
- State the file path

If zero new facts: "No new facts this session."

### 5. Project Wisdom

Did you learn anything about how this project works, what patterns succeed or
fail, or what the owner cares about for this project specifically? If yes,
update `{PROJECT_ROOT}/.dev/ai/roles/project-steward/project-wisdom.md`.

### 6. WO + INDEX Sync

Check every WO you touched this session. Is the WO file status consistent with
WO-INDEX.md? Fix any mismatches now.

### 7. Active Constraint

Did the active constraint change? If yes, update active-constraint.md. If
you're not sure, re-read it and confirm it still reflects reality.

### 8. Tuning Log

Did you notice any behavioral failure in yourself this session — something the
prompt should have prevented but didn't? If yes, append to the tuning log at
`/Users/grig/.agents/agents/tuning/steward-tuning-log.md`. Do NOT fix your own
prompt.

## Master Steward Additions

If operating as Master Steward, also complete these:

### 9. Knowledge Tree

For every project discussed this session where a decision was made, the phase
changed, or new context was shared: update
`~/.agents-private/project-steward/master-steward/knowledge/projects/{slug}.md`
(bump `last_updated`). Update MASTER-INDEX if the phase or priority line
changed. List every file you updated.

If no projects discussed: "No knowledge tree updates."

### 10. Supervisor Sync

Did this session resolve a blocker, complete a WO, or make an owner decision
the supervisor tracks? If yes, append to
`~/.agents/agents/blocker-engineer/ms-updates.md`.

### 11. Dispatch Surface

Did this session identify blocker-lifecycle work for the supervisor? If yes,
write to `~/.agents/agents/blocker-engineer/ms-dispatch.md`.

### 12. Inbox

Are there owner thoughts from this session that arrived while work was running
and haven't been filed? If yes, file them to the MS inbox at
`~/.agents-private/project-steward/master-steward/inbox/`.

## Summary Report

After completing all steps, output a summary:

```
SESSION CLOSE CAPTURE:
  Corrections captured: [count] ([paths])
  Decisions recorded: [count] ([paths])
  Monologues saved: [count] ([paths])
  New facts stored: [count] ([paths])
  Project wisdom updated: [yes/no]
  WO/INDEX mismatches fixed: [count]
  Active constraint: [updated/unchanged]
  Tuning log entries: [count]
  MS knowledge tree updates: [count] (MS only)
  MS supervisor sync: [yes/no] (MS only)
  MS dispatch entries: [count] (MS only)
```

Then proceed to create the session record using
`~/.agents/prompts/creation/CREATE-SESSION-RECORD.md`.
