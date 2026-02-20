# GAS Prompt Library

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Status: Active Development](https://img.shields.io/badge/Status-Active%20Development-orange.svg)](#disclaimer)

A collection of **80+ prompt templates and agent instructions** for AI agent orchestration systems. Part of the [Global Agents System](https://github.com/grigb/agents-global-system) ecosystem.

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

### `agents/` — 40 Specialized Agents
Agent role definitions organized by expertise area:

**Development & Engineering**
- `agent-dev-worker.md` — Implementation and coding tasks
- `agent-dev-overseer.md` — Code review and verification
- `agent-dev-general-contractor.md` — Project coordination
- `agent-qa-full-review.md` — Quality assurance
- `agent-testing-validation.md` — Testing strategies
- `agent-codebase-investigator.md` — Code exploration
- `agent-orchestrator.md` — Multi-agent coordination
- `agent-manager-orchestrator.md` — Portfolio-level orchestration
- `agent-tooling.md` — Tool development

**Research & Analysis**
- `agent-deep-research.md` — Comprehensive research
- `agent-research-analysis.md` — Research synthesis
- `agent-research-gap-analysis.md` — Gap identification
- `agent-data-analysis-visualization.md` — Data insights
- `agent-strategic-intelligence.md` — Strategic analysis
- `agent-document-analysis-audit.md` — Document auditing

**Business & Operations**
- `agent-chief-of-staff.md` — Executive coordination
- `agent-chief-reality-officer.md` — Fact checking
- `agent-project-coordinator.md` — Project management
- `agent-financial-analysis-planning.md` — Financial planning
- `agent-marketing-expert.md` — Marketing strategy
- `agent-communication-stakeholder.md` — Stakeholder management

**Creative & Design**
- `agent-ux-design.md` — UX design
- `agent-visual-designer.md` — Visual design
- `agent-creative-writer-spiritual.md` — Creative writing
- `agent-content-crafting-alignment.md` — Content strategy
- `agent-innovation-ideation.md` — Innovation

**Infrastructure & Support**
- `agent-triage.md` — Work order capture
- `agent-documentation-librarian.md` — Documentation
- `agent-document-author-specialist.md` — Technical writing
- `agent-document-review-specialist.md` — Doc review
- `agent-security-compliance.md` — Security audit
- `agent-process-analysis-retrospective.md` — Process improvement
- `agent-process-design-optimization.md` — Process design
- `agent-mac-performance-diagnostics-specialist.md` — Mac diagnostics
- `agent-network-diagnostics-specialist.md` — Network diagnostics
- `agent-learning-knowledge-management.md` — Knowledge management
- `agent-white-paper-architect.md` — White papers
- `agent-software-product-builder.md` — Product development

See [`agents/_AGENT-INDEX.md`](agents/_AGENT-INDEX.md) for complete list.

### `creation/` — Artifact Generation (5 prompts)
Structured document creation:

| File | Purpose |
|------|---------|
| `CREATE-AUDITABLE-RECORD.md` | Audit trails and compliance documentation |
| `CREATE-FEATURE-REQUEST.md` | Feature requirements and specifications |
| `CREATE-EXEMPLARY-PROJECT-STATE-PACK.md` | High-signal state pack with concise onboarding and deep evidence |
| `CREATE-EXEMPLARY-PROJECT-STATE-PACK-LAN.md` | LAN-prefilled state-pack refresh prompt for consistent project summaries |
| `CREATE-WORK-PROPOSAL.md` | Work proposals with scope and resources |

### `general/` — Core Workflows (20 prompts)
Essential prompts for daily agent operations.
Rule: `general/` is for reusable, project-agnostic prompts only. Project-specific directives must not live here.

| File | Purpose |
|------|---------|
| `autonomous-mode-now.md` | Independent task completion mode |
| `delegate-subtasks-for-everything.md` | Sub-agent delegation strategy |
| `do-you-know-what-to-do-next.md` | Task progression assessment |
| `go-deeper.md` | Deep analysis expansion |
| `interface-audit-orchestrator.md` | Interface audit coordination |
| `name-this-conversation.md` | Conversation naming |
| `organize-docs-and-dirs.md` | Document organization |
| `parallel-review-orchestrator.md` | Parallel review coordination |
| `prepare-work-for-review.md` | Package work for peer review |
| `review-loose-ends.md` | Find unfinished work |
| `review-my-plan.md` | Plan review before execution |
| `rewind-for-handoff.md` | Create handoff from history |
| `subtask-pre-work-report.md` | Pre-execution planning |
| `universal-app-build-prompt.md` | Universal app building |
| `verify-previous-work.md` | Verification with evidence |
| `whats-next.md` | Next steps identification |
| `wrap-up-and-shutdown.md` | Session cleanup |

### `handoffs/` — Work Transfer + Project Directives (6 prompts)
Agent-to-agent work transfer protocols and project-bound directive packs:

| File | Purpose |
|------|---------|
| `HANDOFF.md` | Standard handoff protocol |
| `HANDOFF-MINIMAL.md` | Lightweight quick transfers |
| `HANDOFF-DETAILED.md` | Comprehensive handoff |
| `MANAGER-HANDOFF.md` | Manager-level context transfer |
| `ORCHESTRATION-HANDOFF.md` | Orchestrator-specific handoff |
| `CONVERT-HANDOFF-TO-WORKORDER.md` | Convert handoff to executable WO |
| `k2b-project-directives/` | Project-specific K2B directives (temporary, project-bound) |

### `modes/` — Behavioral Modes (2 prompts)
Operational mode modifiers:

| File | Purpose |
|------|---------|
| `DISCUSSION-MODE.md` | Read-only analysis for planning |
| `GENERATE-PROJECT-INDEX.md` | Project index generation |

### `research/` — Research Workflows (5 prompts)

| File | Purpose |
|------|---------|
| `deep-research-master.md` | **Single entry point** for all Deep Research modes |
| `deep-research-prompt-generator.md` | Transform briefs into research prompts |
| `tri-agent-research-pipeline.md` | Internal tri-agent pipeline |
| `CONDUCT-MODEL-AUDIT.md` | Model performance auditing |
| `perplexity-claude-in-chrome.md` | Perplexity + Claude integration |

### `work-orders/` — Work Order System (3 prompts)
Complete work order lifecycle:

| File | Purpose |
|------|---------|
| `CREATE-WORK-ORDER.md` | Generate executable work orders |
| `EXECUTE-WORK-ORDER.md` | Execute with progress tracking |
| `WORK-ORDER-INDEX.md` | Work order registries |

### `workflows/` — Workflow Protocols (1 prompt)

| File | Purpose |
|------|---------|
| `PEER_REVIEW_PROTOCOL.md` | Structured peer review process |

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
| Run structured review processes | `workflows/` |

---

## Integration

These prompts are designed for use with the [Global Agents System](https://github.com/grigb/agents-global-system) (GAS) but can be adapted for:

- Claude Code / Claude Desktop
- Cursor IDE
- GitHub Copilot
- Continue.dev
- Custom orchestration systems

---

## Adding Prompts

1. **Choose the right directory** based on the prompt's function
2. **Use clear naming**: `ACTION-OBJECT.md` or `ROLE-NAME.md`
3. **Make prompts self-contained** with all necessary context
4. **Update this README** with the new prompt
5. **Run tests** to ensure consistency

---

## Related Resources

- [Global Agents System](https://github.com/grigb/agents-global-system) — Core infrastructure
- [PROMPT-PATH-INDEX.md](PROMPT-PATH-INDEX.md) — Fast file lookup index
- [TRIGGER-INDEX.md](TRIGGER-INDEX.md) — Mode trigger phrases
- [agents/_AGENT-INDEX.md](agents/_AGENT-INDEX.md) — Complete agent catalog

---

## License

MIT License. See [LICENSE](LICENSE) for details.
