# What's Next?

Report your status using ONE of the modes below. Pick the mode that matches your actual state.

---

## MODE A: IDLE
Use this if there's nothing left to do.

```
STATUS: IDLE

Assignment was: [1 sentence]
Completed: [what got done]
Artifacts: [file paths if any]

No pending work. Awaiting new instructions.
```

---

## MODE B: READY TO WORK
Use this if you know what to do and can proceed autonomously.

```
STATUS: READY

Working on: [1 sentence]

QUEUE (pick one or say "go"):
1. [task] — [1-line description]
2. [task] — [1-line description]
3. [task] — [1-line description]

Reply with a number, "all", or "go" to continue autonomously.
```

If there are loose ends not yet in work orders, add:
```
UNTRACKED (needs work orders):
- [item]
- [item]
```

---

## MODE C: NEED INPUT
Use this if you're blocked and need decisions or approvals.

```
STATUS: BLOCKED — NEED INPUT

Working on: [1 sentence]

DECISIONS NEEDED:
1. [Question?]
   Context: [2-3 sentences max - why this matters, what happens either way]
   Options: [A] ... / [B] ... / [C] ...

2. [Question?]
   Context: ...
   Options: ...

Reply with your choices (e.g., "1A, 2B") or ask for more detail on any item.
```

---

## MODE D: HANDOFF (Orchestrators Only)
Use this when session is ending or context is running low.

```
STATUS: HANDOFF

Orchestration objective: [1 sentence]
Completed this session: [summary]
Remaining: [what's left]

Handoff created: [path to orchestration log]
Spawn command: [ready-to-paste command for next orchestrator]

Blockers for next orchestrator:
- [blocker]: [what's needed to resolve]
```

---

## Rules

- Pick ONE mode. Don't mix them.
- Keep it short. No preamble, no recap of everything.
- List known work orders/proposals only if directly relevant to the queue or blockers.
- "Loose ends" = work mentioned but not in a formal work order. Flag these briefly.
- Don't re-read files. Use what you know from this conversation.

### Orchestrator Rules
- Orchestrators should NEVER use MODE A (IDLE) when work remains
- Even if blocked, use HANDOFF not IDLE
- Include spawn command so next agent can continue
