# Deep Research Orchestrator (Unified)

**Purpose**: This is the Single Point of Entry for all Deep Research operations. It replaces multiple fragmented prompts.

**Usage**:
> "Activate Deep Research Mode." -> The agent will ask you which mode you want.
> "Running Deep Research in [Mode Name] mode." -> The agent will execute that specific pipeline.

---

## REQUIRED ROUTING PREFLIGHT

Before presenting or selecting a mode, read
`/Users/grig/.agents/docs/methodologies/research-tool-routing-method.md`.
Find Skills and Last 30 Days are first-class alternatives to a generic Deep
Research run, not optional afterthoughts.

Read the selected skill entry point completely before execution:

- `/Users/grig/.agents/skills/find-skills/SKILL.md`
- `/Users/grig/.agents/skills/last30days/SKILL.md`

Choose Find Skills when the unknown is whether a reusable capability already
exists. Choose Last 30 Days when the unknown is recent community discussion,
sentiment, recommendations, comparisons, trends, or adoption signals. Continue
to Modes A-D when the request needs prompt generation, iterative exploration,
multi-agent synthesis, or signed-in provider research. Use a combined route
when the decision needs more than one evidence class.

---

## 🟢 SELECT YOUR RESEARCH MODE

### ROUTE 0: "Find Skills" (Capability Discovery)
**Best for**: Discovering whether an existing skill, workflow, template, or specialized tool can perform the task.
**Workflow**: Read the installed skill -> Check the skills.sh leaderboard when applicable -> Search with `npx skills find` if needed -> Verify install count, source reputation, and repository quality -> Present candidates and request authorization before installation.
**Logic Source**: `/Users/grig/.agents/skills/find-skills/SKILL.md`
**Use Case**: The research question is really "does an agent capability for this already exist?"

### ROUTE 1: "Last 30 Days" (Recent Community Evidence)
**Best for**: Current community sentiment, recommendations, comparisons, fast-moving trends, hiring signals, and source-backed discussion from the recent window.
**Workflow**: Read the installed skill and every execution-required reference -> Run its bundled engine exactly as instructed -> Preserve its citations, dates, coverage limits, and output contract.
**Logic Source**: `/Users/grig/.agents/skills/last30days/SKILL.md`
**Use Case**: The decision depends on what people are actually saying or doing now.

### MODE A: "One-Shot Generator" (The Classic)
**Best for**: Generating a massive, detailed prompt for *another* agent to execute.
**Workflow**: You provide a topic -> Agent generates a 3,000+ word "Prompt Specification" file.
**Logic Source**: `~/.agents/prompts/research/deep-research-prompt-generator.md`
**Use Case**: You want to hand off a huge research task to an autonomous agent and walk away.

### MODE B: "Interactive Loop" (The Deep Dive)
**Best for**: Working *with* the agent to explore a topic deeply in real-time.
**Workflow**: Loop: [Plan -> Research Chunk -> Verify -> Next Chunk] until saturation.
**Logic Source**: `~/.agents/prompts/general/research-saturation-loop.md`
**Use Case**: You don't know exactly what you're looking for yet and want to explore.

### MODE C: "Tri-Agent Pipeline" (The Specialist Chain)
**Best for**: High-quality, multi-perspective production research.
**Workflow**: 4-Stage Pipeline:
1.  **Discovery** (Perplexity): Landscape mapping.
2.  **Synthesis** (Gemini): Ontology & Framework.
3.  **Blueprinting** (Claude): Technical Specs.
4.  **Briefing** (Codex): Executive Summary.
**Logic Source**: `~/.agents/prompts/research/tri-agent-research-pipeline.md`
**Use Case**: You need a polished, multi-faceted output (Strategy + Code + Brief).

### MODE D: "Browser Deep Research" (Human-Signed-In Providers)
**Best for**: Running human-supplied prompts or agent-generated knowledge-gap prompts through logged-in browser UIs with human authentication checkpoints.
**Workflow**: Normalize prompt source into a GAS Deep Research topic folder -> Confirm owner approval for prompt, providers, source scope, and quota/cost -> Run staged or promoted ChatGPT/OpenAI, Gemini, Claude, and/or Perplexity browser research -> Save verified local Markdown to canonical response files and synthesis.
**Logic Source**: `~/.agents/prompts/research/browser-deep-research-orchestrator.md`
**Use Case**: You want browser-only provider research modes, or an agent has hit a gap where signed-in provider research is the right backend. If approval is missing, create the normalized topic folder and mark it `queued_awaiting_owner_approval` instead of submitting.

---

## 🔵 ORCHESTRATION INSTRUCTIONS

### IF ROUTE 0 (Find Skills) MATCHES:
1. Read `/Users/grig/.agents/skills/find-skills/SKILL.md` completely.
2. Follow its discovery and quality-verification workflow.
3. Do not treat search results as evidence that a skill is safe or effective.
4. Do not install a candidate without explicit installation authorization.

### IF ROUTE 1 (Last 30 Days) MATCHES:
1. Read `/Users/grig/.agents/skills/last30days/SKILL.md` completely.
2. Resolve and read every execution-required reference from that skill directory.
3. Run the bundled research engine; do not substitute improvised web search.
4. Preserve the skill's output and provenance contract.

### IF USER SELECTS MODE A (One-Shot):
1.  Read `~/.agents/prompts/research/deep-research-prompt-generator.md` (The Classic/Prized Generator).
2.  Follow the instructions within that file to generate the prompt specification.
3.  Save the output to `[Topic]-Deep-Research-Prompt.md`.

### IF USER SELECTS MODE B (Interactive):
1.  Read `~/.agents/prompts/general/research-saturation-loop.md`.
2.  Adopt the **Deep Research & Synthesis Agent** persona immediately.
3.  Begin the loop at "Step 1: Clarify the target".

### IF USER SELECTS MODE C (Tri-Agent):
1.  Read `~/.agents/prompts/research/tri-agent-research-pipeline.md`.
2.  Follow the **Sequential Execution** steps defined there.
3.  Execute Stage 1 (Discovery) first.

### IF USER SELECTS MODE D (Browser Deep Research):
1.  Read `~/.agents/prompts/research/browser-deep-research-orchestrator.md`.
2.  Normalize the source prompt, whether human-supplied or agent-generated, into a standard GAS Deep Research topic folder with `.meta.md`, `prompt.md`, `responses/`, and `browser-provider-status.md`.
3.  Confirm owner approval for the prompt, provider list, source scope, account/session gates, and cost or quota risk.
4.  If approval is missing, set topic status to `queued_awaiting_owner_approval`, record the needed approval, and stop before opening provider sessions or submitting prompts.
5.  If approval exists, use staged single-provider invocation until provider gates pass; use promoted multi-provider invocation only after gates pass for the prompt class.
6.  Capture each completed provider run as verified local Markdown, normalize it into `responses/[provider]-browser-cli.md`, then update `sources.md`, `RESEARCH-SYNTHESIS.md`, and `handoff.md`.

---

## 🔴 CRITICAL OVERRIDES

*   **Context Saturation**: In ALL modes, you must ensure you have enough context before starting. If the request is vague, ask clarifying questions.
*   **File Deletion**: In Mode B and C, ensure you clean up 0-byte placeholder files at the end of the run.
