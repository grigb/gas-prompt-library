## INSTRUCTION TO AGENT

Your task is to **generate a deep research prompt**, not to answer any question.

The `<INPUT_CONTEXT>` is raw material (omitted here, replaced with placeholder). Use it only to build the research prompt.

Do not solve or answer the content directly.

Before generating a Deep Research prompt, read
`/Users/grig/.agents/docs/methodologies/research-tool-routing-method.md` and
classify the request. If the real need is capability discovery, route to
`/Users/grig/.agents/skills/find-skills/SKILL.md`. If it is recent community
evidence, route to `/Users/grig/.agents/skills/last30days/SKILL.md`. Continue
with this generator when the user explicitly wants a reusable research prompt
or the question needs broad authoritative, academic, official, historical, or
multi-source investigation. For combined work, name every selected route and
its evidence contribution in the generated prompt.



<INPUT_CONTEXT>

[ YOUR RESEARCH TOPIC HERE ]

</INPUT_CONTEXT>




<DEEP_RESEARCH_PROMPT_TASK version="2025-09-30">

### RESEARCHER ROLE

You are an expert in the relevant research domain with 15+ years of applied and academic experience. You combine theoretical grounding with practical engineering knowledge. You write with precision, rigor, and an evidence‑driven style. Your role is to design a deep research assignment that can be executed by another agent without needing further clarification.

### EXECUTION DIRECTIVE

ASSIGNMENT ID: RES-2025-[AXIS]-001
Research Type: [market analysis | technical evaluation | academic literature survey | policy review]
Research Method: peer‑reviewed papers, preprints, benchmarks, vendor docs, analyst reports, case studies
Research Route: [capability-discovery | recent-community-evidence | standard-deep-research | browser-provider-deep-research | combined]

Decision Context: The deliverable must inform stakeholders with clear technical, financial, or policy implications.

Deliverable Form: Single inline markdown report. If length exceeds runtime limits, follow Segmented Delivery Protocol (Segment 1..N) while maintaining depth.

Objectivity: Include pros and cons, risks, trade‑offs, and confidence levels. Distinguish fact from speculation. Report gaps explicitly.

### SCOPE SPECIFICATION

* Define at least 8–12 objects of study on the canonical axis (tools, methods, platforms, policies, etc.).
* Provide 200+ words of analysis per object.
* Executive summary ≥500 words.
* Timeframe: Emphasize most recent 12–24 months, with historical grounding if needed.
* Geography: Global unless otherwise specified.
* Inclusion: Open‑source and proprietary equally.
* Exclusion: Defunct products unless historically relevant.
* Adjacent categories may be included if they illuminate gaps.
* Minimum relevance threshold: ≥30%.
* Explicitly list all inclusions and exclusions.

### CONTEXT SATURATION

Provide a fictionalized but detailed deployment context: team composition, budget, timeline, previous failures, measurable success criteria, and stakeholder needs. Ensure ≥500 words of environment description so the downstream research agent understands stakes and constraints.

### RESEARCH METHODOLOGY

* Specify exact search strategies and sample queries.
* Define evaluation framework and comparison dimensions.
* Evidence rules: prioritize peer‑reviewed or vendor‑authored docs; flag blog‑only claims as low confidence.
* Language policy: output in English; summarize non‑English with translation confidence.
* Ordering: rank by likelihood of meeting requirements and evidence strength.
* Discovery: expand seed list through adjacent categories, OSS repositories, conference agendas, and analyst quadrants.

### OUTPUT SPECIFICATIONS

* Format: unstructured markdown. No JSON, CSV, or file attachments.
* Structure:

  * # [Main Research Title]
  * ## Executive Summary [≥500 words]
  * ## Domain Overview (include Inventory Preview)
  * ## Detailed Findings (≥200 words per object)
  * ## Comparative Analysis
  * ## Implementation Considerations
  * ## Recommendations
  * ## Conclusion and Next Steps
* Depth: ≥3,500 words total; target ≥4,000.
* Segmented Delivery Protocol: Segment 1 = title, executive summary, domain overview; Segments 2..N = detailed findings; Final Segment = analysis, recommendations, conclusion.
* Quality standards: professional tone, technical accuracy, balanced perspective, evidence‑based.
* Output enforcement: deliver inline only, no links or attachments, no XML/JSON wrappers.

</DEEP_RESEARCH_PROMPT_TASK>

## ENFORCEMENT

Output must be one or more complete deep research prompts following this template.

Do not provide answers or analysis.
