# SKILL.md Format Guide for GAS Agents

## What is SKILL.md?

SKILL.md is the agentskills.io standard for agent capability packaging. Adopted
by 32+ tools including all GAS harnesses. A SKILL.md directory bundles metadata
and the full prompt in one portable unit.

## Directory Structure

```
~/.agents/prompts/agents/agent-<name>/
  SKILL.md         # YAML frontmatter + full prompt body
```

A backward-compat symlink keeps old paths working:
```bash
ln -sf agent-<name>/SKILL.md ~/.agents/prompts/agents/agent-<name>.md
```

## Frontmatter Schema

```yaml
---
name: <slug>                    # lowercase-hyphenated, no "agent-" prefix
description: >
  One or two sentences. Include "Use when:" phrases so harnesses can route.
metadata:
  author: gas-system            # or your agent/team name
  version: "1.0"
  category: <string>            # e.g. core-development, research, qa
  scope: <string>               # single-project | portfolio | global
  tiers: [1, 2, 3]              # complexity tiers this agent handles (1-3)
  model: opus                   # preferred model: opus | sonnet
  effort: high                  # effort level: low | medium | high
  harnesses: [claude, codex]    # supported runtimes
  max_concurrent_tasks: 5       # optional; omit if not applicable
  tags: [tag1, tag2]            # searchable keywords
  projects: [slug, ...]         # optional; project slugs this agent is bound to (future project binding)
---
```

## Body

Everything after the closing `---` is the agent prompt verbatim. No changes
to the prompt content are needed during migration — copy it exactly.

If the old file already had frontmatter (name/description/model blocks),
fold those values into the new SKILL.md frontmatter and strip the old block.

## Updating Indexes

After creating a SKILL.md directory, update two files:

1. `~/.agents/prompts/TRIGGER-INDEX.md` — change path in trigger table rows
   from `agent-<name>.md` to `agent-<name>/SKILL.md`

2. `~/.agents/prompts/agents/_AGENT-INDEX.md` — update the agent table row
   path from `agent-<name>.md` to `agent-<name>/SKILL.md`

## Migration Steps (for each remaining agent)

1. `mkdir -p ~/.agents/prompts/agents/agent-<name>/`
2. Write SKILL.md: new frontmatter + stripped body
3. `mv agent-<name>.md agent-<name>.md.bak`
4. `ln -sf agent-<name>/SKILL.md agent-<name>.md`
5. Update TRIGGER-INDEX.md and _AGENT-INDEX.md rows
6. Verify: `head -5 agent-<name>.md && wc -l agent-<name>/SKILL.md`

## Reference

- Spec: agentskills.io  
- Proof-of-concept: `agent-orchestrator/SKILL.md` (2226 lines, migrated 2026-05-20)
