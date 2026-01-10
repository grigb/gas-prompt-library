# TRIGGER-INDEX: Global Trio Trigger Mappings

**Purpose:** Map short-form trigger phrases to agent prompt files for rapid self-activation without verbose context-setting.

**Priority:** Explicit triggers override implicit detection. First matching trigger wins.

---

## Primary Agent Triggers

### Dev Agent (Implementation)

| Trigger Phrase | Target Prompt | Description |
|----------------|---------------|-------------|
| `dev` | `~/.agents/prompts/agents/agent-dev-worker.md` | Core implementation agent |
| `dev tool` | `~/.agents/prompts/agents/agent-dev-worker.md` | Alias for dev agent |
| `dev agent` | `~/.agents/prompts/agents/agent-dev-worker.md` | Explicit dev agent request |
| `you are the dev agent` | `~/.agents/prompts/agents/agent-dev-worker.md` | Role assignment phrase |
| `act as dev` | `~/.agents/prompts/agents/agent-dev-worker.md` | Role activation phrase |
| `use the dev tool` | `~/.agents/prompts/agents/agent-dev-worker.md` | Tool invocation phrase |

**Activation Regex:** `(?i)\b(dev\s*(agent|tool)?|act\s+as\s+dev|you\s+are\s+(the\s+)?dev)\b`

---

### Triage Agent (Work Order Capture)

| Trigger Phrase | Target Prompt | Description |
|----------------|---------------|-------------|
| `triage` | `~/.agents/prompts/agents/agent-triage.md` | Work order capture agent |
| `triage agent` | `~/.agents/prompts/agents/agent-triage.md` | Explicit triage request |
| `you are the triage agent` | `~/.agents/prompts/agents/agent-triage.md` | Role assignment phrase |
| `act as triage` | `~/.agents/prompts/agents/agent-triage.md` | Role activation phrase |
| `capture this` | `~/.agents/prompts/agents/agent-triage.md` | Quick capture trigger |
| `log this` | `~/.agents/prompts/agents/agent-triage.md` | Quick log trigger |

**Activation Regex:** `(?i)\b(triage(\s+agent)?|act\s+as\s+triage|you\s+are\s+(the\s+)?triage|capture\s+this|log\s+this)\b`

---

### QA Agent (Quality Assurance)

| Trigger Phrase | Target Prompt | Description |
|----------------|---------------|-------------|
| `qa` | `~/.agents/prompts/agents/agent-qa-full-review.md` | Quality assurance agent |
| `qa agent` | `~/.agents/prompts/agents/agent-qa-full-review.md` | Explicit QA request |
| `you are the qa agent` | `~/.agents/prompts/agents/agent-qa-full-review.md` | Role assignment phrase |
| `act as qa` | `~/.agents/prompts/agents/agent-qa-full-review.md` | Role activation phrase |
| `full review` | `~/.agents/prompts/agents/agent-qa-full-review.md` | Comprehensive QA trigger |
| `quality review` | `~/.agents/prompts/agents/agent-qa-full-review.md` | Quality review trigger |

**Activation Regex:** `(?i)\b(qa(\s+agent)?|act\s+as\s+qa|you\s+are\s+(the\s+)?qa|full\s+review|quality\s+review)\b`

---

### Commit Agent (Smart Commits)

| Trigger Phrase | Target Prompt | Description |
|----------------|---------------|-------------|
| `commit agent` | `~/.agents/modes/SMART-COMMIT-MODE.md` | Smart commit mode |
| `smart commit` | `~/.agents/modes/SMART-COMMIT-MODE.md` | Intelligent commit grouping |
| `group commits` | `~/.agents/modes/SMART-COMMIT-MODE.md` | Commit grouping trigger |
| `commit files` | `~/.agents/modes/SMART-COMMIT-MODE.md` | File commit trigger |
| `analyze commits` | `~/.agents/modes/SMART-COMMIT-MODE.md` | Commit analysis trigger |

**Activation Regex:** `(?i)\b(commit\s+agent|smart\s+commit|group\s+commits|commit\s+files|analyze\s+commits)\b`

---

## Trio Activation (Multi-Agent Coordination)

| Trigger Phrase | Target Prompts | Description |
|----------------|----------------|-------------|
| `trio` | All three primary agents | Activate dev + triage + qa |
| `activate trio` | All three primary agents | Explicit trio activation |
| `trio mode` | All three primary agents | Multi-agent mode |

**Trio Activation Behavior:**

When trio is activated:

1. **Triage Agent** scans for pending work orders in `.dev/ai/workorders/`
2. **Dev Agent** picks up highest priority READY work order
3. **QA Agent** validates completed work before status change to COMPLETED

**Trio Orchestration:**

```
User Input → Triage (capture) → Dev (implement) → QA (verify) → Complete
```

**Activation Regex:** `(?i)\b(trio(\s+mode)?|activate\s+trio)\b`

---

## Trigger Detection Protocol

### First-Message Detection

When a user's first message matches any trigger phrase:

1. **Extract trigger** from message using regex patterns
2. **Load target prompt** file immediately
3. **Announce activation** with role greeting
4. **Enter role scope** - operate ONLY within role boundaries

### Priority Rules

1. **Explicit > Implicit**: "you are the dev agent" beats "use dev"
2. **First Match Wins**: Process triggers left-to-right
3. **Trio Overrides Singles**: "activate trio" supersedes individual triggers
4. **Fallback**: No match = default agent behavior (read AGENTS.md)

### Ambiguous Trigger Handling

When trigger is ambiguous:

1. Ask for clarification: "Did you want the dev agent, triage agent, or QA agent?"
2. Provide context: List what each agent does
3. Wait for explicit confirmation

---

## Self-Activation Protocol

**MANDATORY BEHAVIOR:** When an agent detects a trigger phrase in the user's first message:

```
1. IMMEDIATELY read the target prompt file
2. LOAD the role definition and constraints
3. ANNOUNCE role activation: "[Role] agent activated. Ready to [primary action]."
4. OPERATE exclusively within role scope
5. FORBID actions outside role boundaries
```

**Example Interaction:**

```
User: "dev - fix the auth bug in login.js"
Agent: [Reads agent-dev-worker.md]
Agent: "Dev Worker agent activated. Ready to investigate and fix the auth bug in login.js."
[Proceeds with dev-only actions: analyze, plan, execute, verify]
```

---

## Validation Checklist

- [ ] `use the dev tool` activates dev agent without reading AGENTS.md header
- [ ] `activate trio` instantiates all three protocols
- [ ] `mode: qa` switches to QA agent context
- [ ] `triage` enters triage-only mode (no implementation)
- [ ] Trigger system works across all projects using global ~/.agents/

---

## Adding New Triggers

To add a new trigger:

1. Add entry to appropriate section in this file
2. Update regex pattern for the agent
3. Test trigger activation in fresh session
4. Verify role boundaries are enforced

**Format:**

```markdown
| `trigger phrase` | `path/to/prompt.md` | Description |
```

---

**Last Updated:** 2026-01-09
**Version:** 1.0.0
