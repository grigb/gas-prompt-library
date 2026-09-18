# Tri-Agent Research Pipeline (Mode 3)

**Purpose**: A formalized, multi-model research pipeline designed to leverage the specific "Persona Strengths" of different AI models. This mode separates the research process into 4 distinct stages, each handled by the model best suited for it.

**When to use**:
- For complex, high-stakes research projects.
- When "one-shot" generation is insufficient.
- When you need to move from "broad landscape" to "specific technical spec" with high fidelity.

---

## The Pipeline

### Stage 1: Discovery (The Landscape)
**Model**: Perplexity (or Search-Optimized Model)
**Goal**: Map the territory. Find the key players, papers, and concepts.
**Prompt Pattern**:
> "Survey the market for **[Topic]**. Identify key players, academic papers, emerging standards, and open-source tools.
> Output a 'Reading List' of the top 10 most relevant resources with URLs and brief summaries.
> Do NOT try to synthesize yet; just find the highest-quality raw nodes."

### Stage 2: Synthesis (The Ontology)
**Model**: Gemini (The Architect)
**Goal**: Create the mental model. Define entities, relationships, and "Why".
**Input**: The "Discovery" output from Stage 1.
**Prompt Pattern**:
> "Review these findings. Synthesize them into a Coherent Domain Ontology.
> 1. Define the core entities and their relationships.
> 2. Identify the strategic trade-offs a decision-maker faces.
> 3. Create a conceptual framework for evaluating options in this space.
> Focus on the 'Why' and the 'What'. Do not write code yet."

**Output Requirements**: See "Research Synthesis Output Standards" section below.

### Stage 3: Blueprinting (The Spec)
**Model**: Claude (The Engineer)
**Goal**: Detailed implementation specifications. "How" to build it.
**Input**: The "Ontology" from Stage 2.
**Prompt Pattern**:
> "Based on this ontology and framework, write a Detailed Implementation Specification.
> 1. Define the data schemas (SQL/JSON).
> 2. Write the API contracts or Interface definitions.
> 3. Provide concrete code snippets for the core logic.
> 4. Outline the specific 'How-To' steps for execution.
> Focus on pragmatism and deployability."

### Stage 4: Briefing (The Executive Summary)
**Model**: Codex CLI (The Cheat Sheet)
**Goal**: High-density executive 1-pager.
**Input**: The "Blueprint" from Stage 3.
**Prompt Pattern**:
> "Summarize the key technical decisions, architectural patterns, and strategic recommendations into a high-density, bulleted Executive Briefing Note.
> Focus on:
> - Key Decisions made
> - Stack selected
> - Risks & Mitigations
> - Immediate Next Steps
> Limit to 1 page. Zero fluff."

---

## Orchestration Instructions

1.  **Sequential Execution**: This pipeline MUST be run sequentially. The output of Stage N is the *context* for Stage N+1.
2.  **Context Passing**:
    *   Pass the *entire* output of the previous stage to the next model.
    *   Do not summarize it yourself; let the next model read the full context.
3.  **Human-in-the-Loop (Optional)**: You may pause between stages to review the output and steer the next stage (e.g., "Refine this ontology before generating specs").

---

## Research Synthesis Output Standards

All research synthesis outputs (Stage 2 and final consolidated documents) MUST include:

### 1. YAML Front Matter

```yaml
---
document_type: research-synthesis
schema_version: "1.0"
synthesis_id: "[YYYY-MM-DD]-[topic-slug]"

project:
  name: "[Project Name]"
  slug: "[project-slug]"
  domain: "[domain]"

topic:
  id: "[topic-id]"
  title: "[Title]"
  keywords:
    - keyword-1
    - keyword-2

sources:
  count: [number]
  models:
    - model-1
    - model-2

dates:
  created: "[YYYY-MM-DD]"
  updated: "[YYYY-MM-DD]"

quality:
  completeness_percent: [0-100]
  confidence: [high|medium|low]
  status: [complete|in-progress]

knowledge_graph:
  entities: [list of concepts]
  technologies: [list of tech]
  patterns: [list of patterns]
---
```

### 2. Consensus Matrices (REQUIRED)

Document where sources agree/disagree with explicit percentages:

```markdown
## Consensus Matrices

### [Category] Consensus
| Recommendation | Agreement | Sources Agreeing |
|----------------|-----------|------------------|
| [Item] | 100% (5/5) | All sources |
| [Item] | 80% (4/5) | source-a, source-b, source-c, source-d |

### Areas of Divergence
| Topic | Perspective A | Perspective B | Resolution |
|-------|--------------|---------------|------------|
| [Topic] | [View] (60%) | [Alt View] (40%) | [When each applies] |
```

### 3. Cross-Project Discovery

Synthesis files enable cross-project search:
```bash
grep -r "document_type: research-synthesis" ~/work/
```
