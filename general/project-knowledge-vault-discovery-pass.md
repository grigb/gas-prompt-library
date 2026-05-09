# Project Knowledge Vault Discovery Pass

Use this prompt when a project orchestrator or worker needs to search the
owner's knowledge vaults for documents that may affect the current project
work. This is a discovery and synthesis pass, not implementation.

## Goal

Find related knowledge-vault documents that may change, improve, extend,
defer, simplify, or remove features in the project being worked on.

The agent must look beyond the exact topic already being discussed. The point
is to discover adjacent product, architecture, user-experience, legal,
business, research, or prior-decision material that the current project agent
may not know exists.

## Inputs

The caller should provide:

- Project name.
- Absolute project path.
- Current work order, blocker, or feature area.
- Current implementation context or known constraints.
- Any seed topics, terms, people, brands, documents, or examples.

Default knowledge roots to search unless the project provides a narrower list:

- `/Users/grig/work/obsidian-vault`
- `/Users/grig/work/obsidian-vault-llm-wiki`
- project-local `.dev/ai/` research, findings, handoffs, reports, and
  work-order records

## Required Search Strategy

Use exact and semantic search patterns. Start narrow, then fan out:

1. Search for project/module names, brand names, work-order terms, feature
   names, and protocol names.
2. Search for adjacent user-problem terms, not just implementation terms.
3. Search for known alternatives, risks, and "should we do this differently"
   language.
4. Search for prior decisions and old research that may have been forgotten.
5. Search project-local `.dev/ai/` records so recent agent work is not
   disconnected from older vault knowledge.

Use `rg` first. If QMD or another approved semantic index is available and
already configured for the relevant vault, use it as a second pass. Do not
invent documents or infer that a topic exists without a path-backed source.

## Output

Write a report under the project, normally:

`<project_path>/.dev/ai/research/<YYYY-MM-DD>-knowledge-vault-discovery-<topic>.md`

The report must include:

- Search roots and search terms used.
- Source documents reviewed, with absolute paths.
- Relevant facts and ideas, grouped by source.
- "Potential feature additions" with rationale.
- "Potential feature changes" with rationale.
- "Potential feature removals or simplifications" with rationale.
- "Risks or gates" including legal, payment, custody, privacy, security,
  child-safety, owner-review, or external-service constraints.
- "Recommended work-order changes" listing exact WOs to create, amend, defer,
  or leave unchanged.
- "Do not change" section for items that are interesting but out of scope.

## Rules

- Do not implement project code in this pass.
- Do not treat old research as binding unless it is a recorded owner decision,
  current project policy, or explicitly ratified by the current work order.
- Do not ask the owner to reread large documents unless a specific decision is
  truly needed.
- Prefer a short synthesis over a dump of quotes.
- If the search finds nothing meaningful, say that plainly and list the search
  terms so a future pass can improve them.
- If documents conflict, preserve the conflict and recommend a small decision
  brief rather than choosing silently.

## Final Response

Return:

- Report path.
- Top 3 source documents.
- Top 3 recommended project changes, or `none`.
- Any owner decisions needed, or `none`.
