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

Flat `agent-<name>.md` compatibility files and symlinks are obsolete. The
package directory is the sole live prompt entrypoint. Historical archives may
retain old paths, but live indexes, generators, and validators must use
`agent-<name>/SKILL.md`.

## Generated Codex Plugin Projection

Do not move the canonical package to satisfy Codex distribution. Mapped GAS
skills are copied as complete trees into:

```text
/Users/grig/.agents/plugin-packages/<plugin>/
  .codex-plugin/plugin.json
  skills/<frontmatter-name>/SKILL.md
```

`/Users/grig/.agents/config/plugin-bundles.json` maps canonical source,
frontmatter identity, plugin target, policy, exclusions, and provenance. Run
`/Users/grig/.agents/tools/gas-plugin-packager/generate.py` to update generated
copies and `validate.py` to prove complete-file-list/SHA-256 parity. Never
hand-edit generated descendants or installed caches.

Codex uses the plugin namespace `<plugin>:<frontmatter-name>`. Claude and
Gemini continue to use reviewed canonical adapters and must not be redirected
through generated Codex roots.

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
  # Do not hardcode model or effort execution hints here. Dispatchers select
  # models using /Users/grig/.agents/docs/MODEL-SELECTION-POLICY.md and
  # /Users/grig/.agents/tools/usage-management/scripts/select-model.sh.
  harnesses: [claude, codex]    # supported runtimes
  max_concurrent_tasks: 5       # optional; omit if not applicable
  tags: [tag1, tag2]            # searchable keywords
  projects: [slug, ...]         # optional; project slugs this agent is bound to (future project binding)
---
```

## Computer-Use Category Precedent

Every dispatch-capable prompt must carry the canonical `computer-use` task-
shape instruction: a separate Worker doing repetitive, tool-intensive full QA,
end-to-end walkthroughs, dogfood runs, or similar computer/browser execution
with defined acceptance criteria may invoke `--category computer-use --surface <verified-surface>` only on
an already-authorized Codex surface whose live allowlist proves the target is
addressable. The category target is policy-owned; do not hardcode its native
model ID. It is excluded from coding, diagnosis, implementation,
architecture, security, legal/medical, high-stakes judgment, and ambiguous
research; it changes only model+effort selection and never authorizes a
provider/harness switch. If the surface is not addressable, use the ordinary
same-harness route.

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
4. Do not recreate the flat path or compatibility symlink
5. Update TRIGGER-INDEX.md and _AGENT-INDEX.md rows
6. Verify the canonical package and run the role metadata validator
7. If mapped, regenerate and validate the Codex plugin projection

## Reference

- Spec: agentskills.io  
- Proof-of-concept: `agent-orchestrator/SKILL.md` (2226 lines, migrated 2026-05-20)
