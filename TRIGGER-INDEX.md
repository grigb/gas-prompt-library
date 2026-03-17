# TRIGGER-INDEX: Global Trio Trigger Mappings

**Purpose:** Map short-form trigger phrases to agent prompt files for rapid self-activation without verbose context-setting.

**Priority:** Explicit triggers override implicit detection. First matching trigger wins.

---

## Primary Agent Triggers

### Agent Zero (Layer 0 Meta-Orchestrator)

| Trigger Phrase | Target Prompt | Description |
|----------------|---------------|-------------|
| `agent zero` | `~/.agents/prompts/agents/agent-zero.md` | Agent Zero -- owner's reasoning partner and meta-orchestrator |
| `agent0` | `~/.agents/prompts/agents/agent-zero.md` | Short form for Agent Zero |
| `a0` | `~/.agents/prompts/agents/agent-zero.md` | Abbreviated form for Agent Zero |
| `GAS A0` | `~/.agents/prompts/agents/agent-zero.md` | External reference form for Agent Zero |
| `M` | `~/.agents/prompts/agents/agent-zero.md` | Single-letter shorthand for Agent Zero |
| `owner's agent` | `~/.agents/prompts/agents/agent-zero.md` | Legacy trigger (still works) |
| `board director` | `~/.agents/prompts/agents/agent-zero.md` | Board-level strategic view |
| `meta-orchestrator` | `~/.agents/prompts/agents/agent-zero.md` | Cross-domain orchestration |
| `big picture` | `~/.agents/prompts/agents/agent-zero.md` | Holistic world-state synthesis |
| `where are we` | `~/.agents/prompts/agents/agent-zero.md` | Cross-domain status check |

**Core Principle:** Layer 0. Sits above all hierarchy, all companies, all projects. Reasons across the full fabric of the owner's world. Never implements -- thinks, connects, prioritizes, delegates.

**Activation Regex:** `(?i)\b(agent\s*zero|agent\s*0|a0|gas\s+a0|owner'?s\s+agent|board\s+director|meta[\s-]orchestrator|big\s+picture|where\s+are\s+we)\b`

---

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

### Orchestrator Agent (Multi-Agent Coordination)

| Trigger Phrase | Target Prompt | Description |
|----------------|---------------|-------------|
| `orchestrator` | `~/.agents/prompts/agents/agent-orchestrator.md` | Multi-agent workflow orchestration |
| `orchestrate` | `~/.agents/prompts/agents/agent-orchestrator.md` | Coordinate agent workflow |
| `coordinate` | `~/.agents/prompts/agents/agent-orchestrator.md` | Project coordination |
| `orchestration` | `~/.agents/prompts/agents/agent-orchestrator.md` | Alias for orchestrator |
| `launch orchestrator` | `~/.agents/prompts/agents/agent-orchestrator.md` | Explicit orchestrator launch |
| `you are the orchestrator` | `~/.agents/prompts/agents/agent-orchestrator.md` | Role assignment phrase |
| `act as orchestrator` | `~/.agents/prompts/agents/agent-orchestrator.md` | Role activation phrase |

**Core Principle:** "Conductor, not musician." Delegates to workers, NEVER executes. One approval, then runs to completion.

**Activation Regex:** `(?i)\b(orchestrat(or|e|ion)|coordinate|launch\s+orchestrator|act\s+as\s+orchestrator|you\s+are\s+(the\s+)?orchestrator)\b`

---

### Manager Orchestrator Agent (Portfolio Coordination)

| Trigger Phrase | Target Prompt | Description |
|----------------|---------------|-------------|
| `manager orchestrator` | `~/.agents/prompts/agents/agent-manager-orchestrator.md` | Portfolio-level orchestration |
| `coordinate projects` | `~/.agents/prompts/agents/agent-manager-orchestrator.md` | Multi-project coordination |
| `portfolio` | `~/.agents/prompts/agents/agent-manager-orchestrator.md` | Portfolio management mode |
| `portfolio orchestration` | `~/.agents/prompts/agents/agent-manager-orchestrator.md` | Portfolio orchestration |
| `manage orchestrators` | `~/.agents/prompts/agents/agent-manager-orchestrator.md` | Manage child orchestrators |

**Core Principle:** "VP, not engineer." Coordinates OTHER orchestrators, not workers. Multi-project scope.

**Activation Regex:** `(?i)\b(manager\s+orchestrator|coordinate\s+projects|portfolio(\s+orchestration)?|manage\s+orchestrators)\b`

---

### GAS Manager Agent (L4 WO Execution)

| Trigger Phrase | Target Prompt | Description |
|----------------|---------------|-------------|
| `gas manager` | `~/.agents/prompts/agents/agent-gas-manager.md` | Layer 4 execution engine |
| `gas team` | `~/.agents/prompts/agents/agent-gas-manager.md` | GAS Team launch/dispatch |
| `gas teams` | `~/.agents/prompts/agents/agent-gas-manager.md` | GAS Teams launch/dispatch |
| `launch gas team` | `~/.agents/prompts/agents/agent-gas-manager.md` | Explicit GAS Team launch |
| `launch gas teams` | `~/.agents/prompts/agents/agent-gas-manager.md` | Explicit GAS Teams launch |
| `execute work orders` | `~/.agents/prompts/agents/agent-gas-manager.md` | Execute next ready WO |
| `run gas loop` | `~/.agents/prompts/agents/agent-gas-manager.md` | Start GAS manager loop behavior |

**Core Principle:** L4 autonomous PM loop. Picks ready WOs, selects strategy, spawns workers, monitors completion, updates status.

**Activation Regex:** `(?i)\b(gas\s+manager|gas\s+teams?|launch\s+gas\s+teams?|execute\s+work\s+orders|run\s+gas\s+loop)\b`

---

### PA Maintenance Agent (Infrastructure Maintenance)

| Trigger Phrase | Target Prompt | Description |
|----------------|---------------|-------------|
| `pa maintenance` | `~/.agents-gas-prompt-library/agents/agent-pa-maintenance.md` | Full PA maintenance session |
| `pa doctor` | `~/.agents-gas-prompt-library/agents/agent-pa-maintenance.md` | PA health diagnosis |
| `pa mechanic` | `~/.agents-gas-prompt-library/agents/agent-pa-maintenance.md` | PA repair and fix |
| `maintain pa` | `~/.agents-gas-prompt-library/agents/agent-pa-maintenance.md` | PA maintenance trigger |
| `fix pa` | `~/.agents-gas-prompt-library/agents/agent-pa-maintenance.md` | PA fix trigger |
| `pa health` | `~/.agents-gas-prompt-library/agents/agent-pa-maintenance.md` | PA health check trigger |

**Core Principle:** Maintenance only. Diagnose, repair, and document. Never implement new features.

**Activation Regex:** `(?i)\b(pa\s+(maintenance|doctor|mechanic|health)|maintain\s+pa|fix\s+pa)\b`

---

### Paperclip Worker Agent (Paperclip-Managed Heartbeat Worker)

| Trigger Phrase | Target Prompt | Description |
|----------------|---------------|-------------|
| `paperclip worker` | `~/.agents/prompts/agents/agent-paperclip-worker.md` | Paperclip-managed heartbeat worker |
| `paperclip agent` | `~/.agents/prompts/agents/agent-paperclip-worker.md` | Paperclip-managed heartbeat worker |
| `you are a paperclip` | `~/.agents/prompts/agents/agent-paperclip-worker.md` | Paperclip bootstrap trigger |

**Core Principle:** Lifecycle managed by Paperclip. Wakes on heartbeat, checks inbox, does work, exits. Does NOT act as standalone GAS agent.

**Activation Regex:** `(?i)\b(paperclip\s+(worker|agent)|you\s+are\s+a\s+paperclip)\b`

---

### Alignment Check-In Protocol (Alignment Verification)

| Trigger Phrase | Target Prompt | Description |
|----------------|---------------|-------------|
| `alignment check` | `~/.agents/docs/ALIGNMENT-CHECK-IN-PROTOCOL.md` | Full alignment verification against source of truth |
| `check-in` | `~/.agents/docs/ALIGNMENT-CHECK-IN-PROTOCOL.md` | Periodic alignment check |
| `are we on track` | `~/.agents/docs/ALIGNMENT-CHECK-IN-PROTOCOL.md` | Plan-vs-reality assessment |
| `verify alignment` | `~/.agents/docs/ALIGNMENT-CHECK-IN-PROTOCOL.md` | Source-of-truth comparison |
| `status check against plan` | `~/.agents/docs/ALIGNMENT-CHECK-IN-PROTOCOL.md` | Full protocol run |
| `holistic view` | `~/.agents/docs/ALIGNMENT-CHECK-IN-PROTOCOL.md` | Top-level project state assessment |
| `zoom out for a sec` | `~/.agents/docs/ALIGNMENT-CHECK-IN-PROTOCOL.md` | Step back and assess big picture |
| `where are we at` | `~/.agents/docs/ALIGNMENT-CHECK-IN-PROTOCOL.md` | Current state synthesis |
| `I forgot what we were doing` | `~/.agents/docs/ALIGNMENT-CHECK-IN-PROTOCOL.md` | Full context reload and orientation |

**Core Principle:** Deliberate, periodic alignment ritual. Loads 8 source-of-truth documents, verifies WO integrity, checks blueprint alignment, assesses pillar health, produces report, executes corrections. Uses incremental caching to avoid re-verifying unchanged items.

**Standing Order:** SO-027 -- must run before every phase transition and at least once per Agent Zero session.

**Activation Regex:** `(?i)\b(alignment\s+check|check[\s-]in|are\s+we\s+on\s+track|verify\s+alignment|status\s+check\s+against\s+plan|holistic\s+view|zoom\s+out|where\s+are\s+we\s+at|forgot\s+what\s+we\s+were\s+doing)\b`

---

### Deep Research Mode (Structured Research)

| Trigger Phrase | Target Prompt | Description |
|----------------|---------------|-------------|
| `deep research` | `~/.agents/modes/DEEP-RESEARCH-MODE.md` | Structured multi-source research |
| `research mode` | `~/.agents/modes/DEEP-RESEARCH-MODE.md` | Activate deep research mode |
| `comprehensive research` | `~/.agents/modes/DEEP-RESEARCH-MODE.md` | Full research with citation tracking |
| `conduct deep research` | `~/.agents/modes/DEEP-RESEARCH-MODE.md` | Research execution trigger |
| `run deep research` | `~/.agents/modes/DEEP-RESEARCH-MODE.md` | Research execution trigger |

**Core Principle:** Structured, multi-source research with citation tracking, prompt generation, and knowledge vault integration. All substantial research that becomes permanent reference documentation MUST use this mode.

**Activation Regex:** `(?i)\b(deep\s+research|research\s+mode|comprehensive\s+research|(conduct|run)\s+deep\s+research)\b`

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

### Mac Performance Diagnostics Specialist (macOS Troubleshooting)

| Trigger Phrase | Target Prompt | Description |
|----------------|---------------|-------------|
| `mac agent` | `~/.agents/prompts/agents/agent-mac-performance-diagnostics-specialist.md` | macOS performance diagnostics agent |
| `mac help` | `~/.agents/prompts/agents/agent-mac-performance-diagnostics-specialist.md` | Quick Mac help trigger |
| `mac technician` | `~/.agents/prompts/agents/agent-mac-performance-diagnostics-specialist.md` | Mac technician role |
| `mac tech` | `~/.agents/prompts/agents/agent-mac-performance-diagnostics-specialist.md` | Short form for Mac technician |
| `mac diagnostics` | `~/.agents/prompts/agents/agent-mac-performance-diagnostics-specialist.md` | Mac diagnostics trigger |
| `mac performance` | `~/.agents/prompts/agents/agent-mac-performance-diagnostics-specialist.md` | Mac performance analysis trigger |
| `mac doctor` | `~/.agents/prompts/agents/agent-mac-performance-diagnostics-specialist.md` | Mac doctor / health check trigger |
| `you are the mac agent` | `~/.agents/prompts/agents/agent-mac-performance-diagnostics-specialist.md` | Role assignment phrase |
| `act as mac agent` | `~/.agents/prompts/agents/agent-mac-performance-diagnostics-specialist.md` | Role activation phrase |

**Core Principle:** macOS performance specialist. Diagnoses CPU, GPU, memory, disk, thermal, and fan issues. Never modifies system files without explicit approval.

**Activation Regex:** `(?i)\b(mac\s+(agent|help|technician|tech|diagnostics|performance|doctor)|you\s+are\s+(the\s+)?mac\s+agent|act\s+as\s+mac\s+agent)\b`

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
4. **Fallback**: No match = default agent behavior (read AGENTS.md for context)

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

**Last Updated:** 2026-03-16
**Version:** 1.0.0
