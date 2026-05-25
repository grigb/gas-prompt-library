# Deep Research Orchestrator (Unified)

**Purpose**: This is the Single Point of Entry for all Deep Research operations. It replaces multiple fragmented prompts.

**Usage**:
> "Activate Deep Research Mode." -> The agent will ask you which mode you want.
> "Running Deep Research in [Mode Name] mode." -> The agent will execute that specific pipeline.

---

## 🟢 SELECT YOUR RESEARCH MODE

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
**Best for**: Running deep research through logged-in browser UIs with human authentication checkpoints.
**Workflow**: Human confirms topic, providers, sign-in, and prompt -> Agent runs ChatGPT/OpenAI, Gemini, Claude, and/or Perplexity browser research -> Agent saves raw outputs and synthesis.
**Logic Source**: `~/.agents/prompts/research/browser-deep-research-orchestrator.md`
**Use Case**: You want to use browser-only provider research modes where the agent must wait for sign-in, submit the prompt, recognize completion, and save results.

---

## 🔵 ORCHESTRATION INSTRUCTIONS

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
2.  Confirm the topic, provider list, and output directory.
3.  Open each requested provider in the browser, pause for user sign-in confirmation, run the approved prompt, wait for provider-specific completion signals, then save raw outputs and synthesis.

---

## 🔴 CRITICAL OVERRIDES

*   **Context Saturation**: In ALL modes, you must ensure you have enough context before starting. If the request is vague, ask clarifying questions.
*   **File Deletion**: In Mode B and C, ensure you clean up 0-byte placeholder files at the end of the run.
