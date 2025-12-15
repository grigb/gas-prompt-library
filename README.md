# AI Agent Prompts Library

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Status: Active Development](https://img.shields.io/badge/Status-Active%20Development-orange.svg)](#disclaimer)

A collection of prompt templates and agent instructions for AI agent orchestration systems.

---

## Disclaimer

**This is a work in progress.** These prompts are actively developed and used within the author's AI agent systems. Before using:

- Prompts work within specific orchestration systems and may reference external tools not included here
- Not exhaustively tested in isolation
- Continuously evolving as underlying systems develop
- May require adaptation for your use case

See the [LICENSE](LICENSE) file for the full disclaimer.

---

## Directory Structure

### `agents/` - Specialized Agents
**29 specialized AI agents** organized by expertise area.

Categories include:
- **Development**: Project orchestration, QA, implementation
- **Research**: Technical research, gap analysis, strategic intelligence
- **Business**: Executive coordination, financial planning, marketing
- **Creative**: UX design, content creation, innovation
- **Infrastructure**: Data analysis, security, tooling, diagnostics

See [`agents/README.md`](agents/README.md) for complete agent descriptions and usage.

### `creation/` - Artifact Creation
Prompts for generating structured documents:

| File | Purpose |
|------|---------|
| `CREATE-AUDITABLE-RECORD.md` | Audit trails and compliance documentation |
| `CREATE-FEATURE-REQUEST.md` | Feature requirements and specifications |
| `CREATE-WORK-PROPOSAL.md` | Work proposals with scope and resources |

### `general/` - Core Workflows
Essential prompts for common agent operations:

| File | Purpose |
|------|---------|
| `autonomous-mode-now.md` | Independent task completion mode |
| `verify-previous-work.md` | Verification of work claims with evidence |
| `prepare-work-for-review.md` | Package work for peer review |
| `review-my-plan.md` | Plan review before execution |
| `do-you-know-what-to-do-next.md` | Task progression and state assessment |
| `interface-audit-orchestrator.md` | Interface audit coordination |
| `parallel-review-orchestrator.md` | Parallel review coordination |

### `handoffs/` - Work Transfer
Standardized templates for agent-to-agent work transfers:

| File | Purpose |
|------|---------|
| `HANDOFF.md` | Standard handoff protocol |
| `HANDOFF-MINIMAL.md` | Lightweight quick transfers |
| `HANDOFF-DETAILED.md` | Comprehensive handoff with full context |

### `modes/` - Behavioral Modes
Special operational modes that modify agent behavior:

| File | Purpose |
|------|---------|
| `DISCUSSION-MODE.md` | Read-only analysis for planning and discussion |

### `research/` - Research Workflows
Specialized prompts for research:

| File | Purpose |
|------|---------|
| `deep-research-prompt-generator.md` | Transform briefs into comprehensive research prompts |
| `deep-research-master.md` | **SINGLE ENTRY POINT** for all Deep Research modes (One-Shot, Interactive, Pipeline) |
| `CONDUCT-MODEL-AUDIT.md` | Audit and evaluate AI model performance on research topics |
| `tri-agent-research-pipeline.md` | *Internal pipeline definition used by Master mode* |

### `work-orders/` - Work Order System
Complete work order lifecycle management:

| File | Purpose |
|------|---------|
| `CREATE-WORK-ORDER.md` | Generate executable work orders |
| `EXECUTE-WORK-ORDER.md` | Execute with progress tracking |
| `WORK-ORDER-INDEX.md` | Work order registries and tracking |

---

## Quick Reference

| Need to... | Use |
|------------|-----|
| Define specialized agent roles | `agents/` |
| Generate documents or proposals | `creation/` |
| Handle development workflows | `general/` |
| Transfer work between agents | `handoffs/` |
| Change agent behavior modes | `modes/` |
| Conduct deep research | `research/` |
| Manage structured work execution | `work-orders/` |

---

## Adding Prompts

1. **Choose the right directory** based on the prompt's function
2. **Use clear naming**: `ACTION-OBJECT.md` or `ROLE-NAME.md`
3. **Make prompts self-contained** with all necessary context
4. **Update this README** with the new prompt

---

## License

MIT License. See [LICENSE](LICENSE) for details.
