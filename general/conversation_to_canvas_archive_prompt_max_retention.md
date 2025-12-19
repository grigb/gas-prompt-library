This output must be delivered as either:
- **Canvas document(s)** (if the platform supports canvases), or
- **Artifact document(s)** (if the platform supports artifacts),
while preserving identical structure and content.

## Hard requirements
- Preserve 100% of substantive content: all claims, decisions, definitions, architectures, schemas, edge cases, assumptions, open questions, disagreements, corrections, and rationale.
- Do not summarize away details. Prefer verbatim where feasible; otherwise paraphrase with explicit fidelity to the original meaning.
- Capture both: (1) the final “report/answer” content and (2) the full conversational process that led to it.

## Packaging
- If a single document will exceed length limits, split into multiple **canvases/artifacts** with a strict, stable structure.
- Create an **INDEX** document first that explains the split, lists every document with a one-line description, and provides cross-links/anchors.
- Each document must include: title, scope, covered message range, and a “What changed vs prior document” note (if applicable).

## Required structure inside each document
1) Executive snapshot (only what’s necessary to orient the archive; no content loss elsewhere)
2) Chronological transcript (cleaned for readability but content-faithful; include timestamps/turn numbers if available)
3) Extracted artifacts (specs, models, schemas, lists, drafts, decisions) as durable sections
4) Decision log (decision, date/turn, rationale, alternatives rejected, dependencies)
5) Assumptions + unknowns + gaps (each with why it matters and what evidence is missing)
6) Actionable backlog (tasks phrased as build/test/research items, ordered by dependency)
7) Reference appendix (glossary of terms defined in-thread; canonical links mentioned; identifiers)

## Formatting rules
- Use Markdown headings consistently (H1 for document title; H2 major sections; H3 subsections).
- Use stable IDs for cross-references (e.g., `ID: DEC-003`, `ID: GAP-007`) and refer to them throughout.
- Use code fences for code, schemas, prompts, and command sequences exactly as written in the conversation.
- Do not invent facts or fill gaps. If something is implied, label it explicitly as an inference.

## Output
- Produce the document(s) directly in the platform’s supported format (Canvas and/or Artifact), ready for Markdown download.

