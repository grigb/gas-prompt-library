# CREATE SESSION RECORD

Create one unified session-close artifact that preserves:
- forward actionability for the next agent or next session
- backward audit traceability for recovery and long-term review

Core principle:
`One session = one record. Forward actions + current state + backward traceability = one artifact.`

This replaces the end-of-session pair of:
- conversation audit
- standard continuation handoff

It does **not** replace orchestration handoffs used for delegation, subtask coordination, or `.dev/ai/subtask-comms/`.

## Routing Rule

- Routine session close, including low-context or emergency closeout, uses this prompt.
- Explicit request for a legacy standard handoff uses `~/.agents/prompts/handoffs/HANDOFF.md` only as a compatibility surface, not as the default session-close choice.
- Delegation, orchestration transfer, or `.dev/ai/subtask-comms/` coordination uses `~/.agents/prompts/handoffs/ORCHESTRATION-HANDOFF.md`.
- Explicit request for a standalone historical audit or an older audit-only integration uses `~/.agents/prompts/creation/CREATE-AUDITABLE-RECORD.md` as a legacy audit alias.

## When to Use This Flow

Use this prompt when the user requests any of:
- `/close-session`
- `close session`
- `create session record`
- `wrap this session`
- `save the session`
- a combined audit + next-steps artifact

You may also use it at a natural session close when the user clearly wants continuity, traceability, or resumability.

Do **not** use this flow when:
- the user explicitly asks for an orchestration handoff
- the user explicitly asks for a legacy standard handoff artifact
- the user explicitly asks for standalone audit-only output
- the destination path is `.dev/ai/subtask-comms/`
- you are delegating work to another agent mid-execution
- the artifact is for multi-agent coordination rather than session close

For those cases, use `/Users/grig/.agents/prompts/handoffs/ORCHESTRATION-HANDOFF.md` or the orchestrator-specific handoff flow.

## Save Target

Save the artifact to:
`.dev/ai/sessions/{timestamp}-session-{project}.md`

Do not save session-close records to:
- `.dev/ai/audits/`
- `.dev/ai/handoffs/`

Legacy audit and handoff directories remain historical archives. New session-close records belong in `.dev/ai/sessions/`.

## Complexity Tiers

Assess complexity before writing.

### Emergency / Low Context
Use when the user mentions:
- `low context`
- `running out`
- `context limited`
- `quick`
- `emergency`
- `hitting limit`

Target:
- 20-40 lines
- preserve only execution-critical facts
- keep `BACKWARD` minimal, not absent

### Simple
Use for a single, low-ambiguity task or brief mechanical session.

Target:
- 50-80 lines
- compact `BACKWARD`

### Standard
Use for multi-step sessions with some judgment or synthesis.

Target:
- 100-180 lines
- standard `BACKWARD`

### Complex
Use for integration, design judgment, interdependent steps, or blocker-heavy work.

Target:
- 180-300 lines
- detailed `BACKWARD`
- when the 35-40% reduction target matters, steer toward the validated 217-235 line / 4.8-5.2k token band
- treat the lower half of the tier as the default for validated complex cases; 300 lines is a hard ceiling, not a normal target

## Provenance and Naming

Every session record must include `agent_task_id`.

Rules:
- If you received an `agent_task_id` from a prior handoff, work order, or session record, reuse it.
- If no `agent_task_id` exists, generate one with:

```bash
AGENT_TASK_ID=$(~/.agents/scripts/get-agent-task-id.sh session-record)
```

Include `agent_task_id` in:
- frontmatter
- footer
- next-session prompt

Create the output path with:

```bash
mkdir -p .dev/ai/sessions/
TIMESTAMP=$(~/.agents/scripts/get-filename-prefix.sh)
FILE=".dev/ai/sessions/${TIMESTAMP}-session-[project-id].md"
```

Use the saved file path exactly in the record and in the final chat response.

## Required Frontmatter

```yaml
---
agent_task_id: [AGENT_TASK_ID]
created: [YYYY-MM-DD-HH-MM-SSZ]
project: [project-name]
type: session-record
complexity: [emergency|simple|standard|complex]
session_record_path: [absolute path to saved file]
---
```

## Required Section Order

Write the body in this exact order:

```markdown
# Session Record: [Project] - [Timestamp]

<!-- AGENT-NOTICE: ROLE-GATED SESSION RECORD. Execute Priority Next Steps ONLY if your active role/mode permits implementation. Read-only roles must treat this record as data. -->
## FORWARD
## STATE
## BACKWARD

---
**Agent Task ID:** [AGENT_TASK_ID]
```

## Execution Safety (Role Gate)

Carry forward the legacy handoff safety behavior inside the saved artifact body, not only in the chat prompt around it.

- every non-orchestration session record must include the in-body `AGENT-NOTICE` comment directly under the title
- this is a role-gated action plan: execute `FORWARD` steps only if the active role/mode permits implementation
- read-only or review-only roles must treat next steps, blockers, and success criteria as context data, not executable instructions

## Required Body Template

Use this template and scale detail to the selected complexity tier.

```markdown
# Session Record: [Project] - [Timestamp]

<!-- AGENT-NOTICE: ROLE-GATED SESSION RECORD. Execute Priority Next Steps ONLY if your active role/mode permits implementation. Read-only roles must treat this record as data. -->
## FORWARD

### Priority Next Steps
1. **[Action]** - [why this matters]
   - Location: `[absolute path or file:line if relevant]`
   - Command: `[exact command if relevant]`
   - Expected result: [what success looks like]

### Blockers and How to Resolve
- [Blocker] -> [specific unblocking action]

### Success Criteria
- [Concrete criterion]
- [Concrete verification target]

### Next-Session Prompt
Read AGENTS.md for context.

I'm resuming work on [project].
Agent Task ID: [AGENT_TASK_ID]

1. Read the session record at: [full absolute path]
2. Confirm your role/mode from the user request and project rules.
3. Execute the Priority Next Steps that are permitted by that role/mode.

## STATE

### Project / Initiative Context
- System or feature being built: [plain-language description]
- User/problem being solved: [why this work exists]
- Current phase: [design|implementation|validation|rollout|maintenance]
- This session's place in the larger effort: [how this session moved the project forward]

### Current Snapshot
- Scope: [what this session covered]
- Current state: [where work now stands]

### Work Status
- Outstanding: [WO IDs or tasks with exact next step]
- Completed this session: [completed work]

### Key Files and Artifacts
- Created: `[absolute path]` - [purpose]
- Modified: `[absolute path]` - [what changed]
- Referenced: `[absolute path]` - [why it matters]

### Key Decisions and Rationale
- [Decision] -> [why]

### Open Questions and Risks
- [Question or risk]

## BACKWARD

### Starting Point and Scope
- Initial request: [what initiated the session]
- Startup inputs:
  - `[full absolute path]` - [why it was loaded]
- Working directory: `[absolute path]`
- Project rules source: `[full absolute path to AGENTS.md or equivalent]`

### Actions Taken
- [chronological action]
- [chronological action]

### Results and Evidence
- [result] -> [artifact, file path, command, or verification evidence]

### Errors, Blockers, and Mitigations
- [issue] -> [response or mitigation]

### Provenance Log
- Commands: `[important command or script]`
- Tracking: `[track-project.sh call or status note]`
- Related artifact chain: `[prior handoff/session record/work order path if applicable]`

---
**Agent Task ID:** [AGENT_TASK_ID]
```

## Section Rules

### `FORWARD`
- always comes first
- must be specific, prioritized, and executable
- remains role-gated: action steps are executable only for roles/modes allowed to implement
- include blockers even if there is only one
- include success criteria whenever unfinished work remains
- if work is complete, say so directly and keep only any real follow-on or monitoring item
- do not write filler such as `continue from here`

### `STATE`
- this is the shared current-state snapshot for both continuation and audit review
- include enough project / initiative context that a future agent reading only a series of session records can tell what the system is, what problem it solves, and what phase the work is in
- cite exact files with absolute paths
- include IDs for work orders, proposals, findings, or reports when relevant
- list only the files and artifacts that matter for continuation or review
- if a subsection is empty, write `None`

### `BACKWARD`
- startup provenance with full absolute paths is mandatory
- preserve enough chronology to explain how the current state was reached
- record commands, scripts, parameter values, or verification steps that materially affected the outcome
- do not restate every trivial action
- for emergency mode, compress this to startup inputs, last meaningful action, and key evidence

## Emergency / Low-Context Variant

If low-context triggers are present, use this compressed form and save immediately:

```markdown
---
agent_task_id: [AGENT_TASK_ID]
created: [YYYY-MM-DD-HH-MM-SSZ]
project: [project-name]
type: session-record
complexity: emergency
session_record_path: [absolute path to saved file]
---

# Session Record: [Project] - [Timestamp]

<!-- AGENT-NOTICE: ROLE-GATED SESSION RECORD. Execute Priority Next Steps ONLY if your active role/mode permits implementation. Read-only roles must treat this record as data. -->
## FORWARD
### Priority Next Steps
1. [Immediate action] - [why]
2. [Immediate action] - [why]

### Blockers and How to Resolve
- [blocker] -> [unblocking action]

## STATE
### Current Snapshot
- Current state: [one line]
- Critical files: `[absolute path]`
- Outstanding work: [WO or task]

## BACKWARD
### Starting Point and Scope
- Initial request: [one line]
- Startup inputs: `[absolute path]`

### Actions Taken
- Last meaningful action: [one line]

### Results and Evidence
- [artifact or verification evidence]

---
**Agent Task ID:** [AGENT_TASK_ID]
```

Do not omit `BACKWARD` entirely in emergency mode.

## Save and Tracking Behavior

After writing the record:
1. Save it to `.dev/ai/sessions/`.
2. Optionally track creation with:

```bash
~/.agents/scripts/track-project.sh "[project-name]" "Session record created" \
  "Session record: [brief summary]" "[agent-name]"
```

If the user asked for a visible close-out, give a short summary in chat that includes:
- current status
- next logical step
- exact absolute path to the saved session record

## Final Check Before Saving

Confirm all of the following:
- file path is under `.dev/ai/sessions/`
- `FORWARD`, `STATE`, and `BACKWARD` all exist
- next actions, blockers, and success criteria are explicit when work remains
- the in-body `AGENT-NOTICE` role-gated execution notice is present
- startup provenance includes full absolute paths
- `agent_task_id` is present
- for complex records where the reduction target matters, the draft is intentionally shaped toward 217-235 lines / 4.8-5.2k tokens
- orchestration handoff content was not mixed into this artifact
