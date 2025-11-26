# Prompt File Path Index

**Purpose**: Fast lookup index for all prompt files. Agents should check this file FIRST before searching.

## Quick Lookup Table

| Logical Name | Actual Path |
|-------------|-------------|
| CREATE-WORK-PROPOSAL | `~/.agents/prompts/creation/CREATE-WORK-PROPOSAL.md` |
| CREATE-AUDITABLE-RECORD | `~/.agents/prompts/creation/CREATE-AUDITABLE-RECORD.md` |
| CREATE-FEATURE-REQUEST | `~/.agents/prompts/creation/CREATE-FEATURE-REQUEST.md` |
| CREATE-WORK-ORDER | `~/.agents/prompts/work-orders/CREATE-WORK-ORDER.md` |
| EXECUTE-WORK-ORDER | `~/.agents/prompts/work-orders/EXECUTE-WORK-ORDER.md` |
| WORK-ORDER-INDEX | `~/.agents/prompts/work-orders/WORK-ORDER-INDEX.md` |
| HANDOFF | `~/.agents/prompts/handoffs/HANDOFF.md` |
| HANDOFF-DETAILED | `~/.agents/prompts/handoffs/HANDOFF-DETAILED.md` |
| HANDOFF-MINIMAL | `~/.agents/prompts/handoffs/HANDOFF-MINIMAL.md` |
| DISCUSSION-MODE | `~/.agents/prompts/modes/DISCUSSION-MODE.md` |
| DEEP-RESEARCH-PROMPT-GENERATOR | `~/.agents/prompts/research/deep-research-prompt-generator.md` |

## Full Directory Structure

```
~/.agents/prompts/
├── README.md                           # Main prompts documentation
├── PROMPT-PATH-INDEX.md               # THIS FILE - fast lookup
├── ORGANIZE-DOCS+DIRS.md              # Documentation organization guide
│
├── agents/                             # Specialized AI agents
│   ├── README.md                       # Agent directory index
│   ├── agent-orchestrator.md
│   ├── agent-dev-general-contractor.md
│   ├── agent-dev-overseer.md
│   ├── agent-dev-worker.md
│   ├── agent-software-product-builder.md
│   ├── agent-research-analysis.md
│   ├── agent-research-gap-analysis.md
│   ├── agent-strategic-intelligence.md
│   ├── agent-chief-of-staff.md
│   ├── agent-chief-reality-officer.md
│   ├── agent-financial-analysis-planning.md
│   ├── agent-marketing-expert.md
│   ├── agent-project-coordinator.md
│   ├── agent-ux-design.md
│   ├── agent-content-crafting-alignment.md
│   ├── agent-innovation-ideation.md
│   ├── agent-communication-stakeholder.md
│   ├── agent-data-analysis-visualization.md
│   ├── agent-testing-validation.md
│   ├── agent-security-compliance.md
│   ├── agent-tooling.md
│   ├── agent-network-diagnostics-specialist.md
│   ├── agent-process-analysis-retrospective.md
│   ├── agent-process-analysis-retrospective-quick.md
│   ├── agent-process-design-optimization.md
│   ├── agent-document-analysis-audit.md
│   ├── agent-synthesis-integration.md
│   └── agent-learning-knowledge-management.md
│
├── creation/                           # Document creation prompts
│   ├── CREATE-WORK-PROPOSAL.md        # Work proposal generation
│   ├── CREATE-AUDITABLE-RECORD.md     # Auditable record creation
│   └── CREATE-FEATURE-REQUEST.md      # Feature request creation
│
├── work-orders/                        # Work order management
│   ├── CREATE-WORK-ORDER.md           # Work order creation
│   ├── EXECUTE-WORK-ORDER.md          # Work order execution
│   └── WORK-ORDER-INDEX.md            # Work order index
│
├── handoffs/                           # Handoff protocols
│   ├── HANDOFF.md                     # Standard handoff
│   ├── HANDOFF-DETAILED.md            # Detailed handoff
│   └── HANDOFF-MINIMAL.md             # Minimal handoff
│
├── modes/                              # Special operation modes
│   └── DISCUSSION-MODE.md             # Discussion mode protocol
│
├── research/                           # Research prompts
│   └── deep-research-prompt-generator.md
│
└── general/                            # General purpose prompts
    ├── do-you-know-what-to-do-next.md
    ├── prepare-work-for-review.md
    ├── autonomous-mode-now.md
    ├── review-my-plan.md
    └── verify-previous-work.md
```

## Usage Instructions for AI Agents

### STEP 1: Check This Index FIRST
Before searching, read this file to find the exact path.

### STEP 2: Direct Read
Use the exact path from the table above.

### STEP 3: Only Search If Not Listed
If the file isn't in this index, THEN use search tools.

## Common Patterns

- **Creation tasks**: Check `creation/` directory
- **Work orders**: Check `work-orders/` directory
- **Handoffs**: Check `handoffs/` directory
- **Specialized agents**: Check `agents/` directory
- **Modes**: Check `modes/` directory
- **General prompts**: Check `general/` directory

## Path Resolution

All paths use `~/.agents/prompts/` as the base directory.

Example resolution:
- Index shows: `~/.agents/prompts/creation/CREATE-WORK-PROPOSAL.md`
- Full path: `/Users/grig/.agents/prompts/creation/CREATE-WORK-PROPOSAL.md`

---

**Last Updated**: 2025-11-25
**Maintained by**: Automated sync from directory structure
