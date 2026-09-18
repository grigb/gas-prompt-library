This output must be delivered as either:
- Canvas document(s) (if the platform supports canvases), or
- Artifact document(s) (if the platform supports artifacts),
while preserving identical structure and content.

## Hard requirements (no exceptions)
- Preserve 100% of substantive content: all claims, decisions, definitions, architectures, schemas, edge cases, assumptions, open questions, disagreements, corrections, and rationale.
- Do not summarize away details. Prefer verbatim where feasible; otherwise paraphrase with explicit fidelity to the original meaning.
- Capture both: (1) the final “report/answer” content and (2) the full conversational process that led to it.
- Do not invent facts or fill gaps. If something is implied, label it explicitly as an inference.

## Critical packaging requirement: NO LIMIT ON DOCUMENT COUNT
- Use as many canvases/artifacts as necessary.
- Never reduce scope, omit material, or compress detail to fit fewer documents.
- Split aggressively when approaching length limits.
- Duplication is allowed when needed to preserve fidelity and make standalone documents usable.

## Output sets (MUST produce all sets below)

### SET A — Forensic Archive (complete, neutral)
Purpose: preserve the full conversation record without bias.

### SET B — Synthesis Pack (type-agnostic; biased toward adopted decisions where applicable)
Purpose: produce a usable set of “final-form” documents organized by topic/deliverable, WITHOUT forcing a specific genre.
Rules:
- Each document in SET B must be assigned a Document Class that matches the content:
  - whitepaper
  - roadmap
  - product-spec
  - PRD
  - architecture-design-doc
  - research-memo
  - integration-guide
  - example-code-pack
  - schema-and-contracts
  - checklist/runbook
  - concept-brief / product-idea
  - prompt-pack / agent-brief
  - other (only if none fit)
- Do NOT reframe content into a whitepaper or roadmap unless the source material actually supports that structure.
- SET B must still preserve 100% of substantive content overall via explicit evidence excerpts and cross-links to SET A and SET C.

### SET C — Deliverable Exports (verbatim, standalone)
Purpose: every substantial artifact produced in-thread (and any artifact produced in the wrong format) must be exported as its own standalone document, verbatim, so it can be used directly.

## Deliverable discovery rules (must be explicit)
1) Scan the full conversation and identify EVERY deliverable produced or implied as “supposed to be exported”:
   - specs, PRDs, roadmaps, whitepapers, research, schemas, interface contracts, example code, build steps, prompts, checklists, diagrams-as-text, etc.
2) Create a Deliverables Manifest (DEL-###) with fields:
   - title
   - document class (from SET B classes, if applicable)
   - originating turn range
   - confidence (explicit vs inferred)
   - where exported verbatim in SET C (exact document ID)
   - where synthesized/organized in SET B (exact document ID(s))
3) Export each deliverable in SET C verbatim in its own document.
   - No merging multiple deliverables into one file unless they were authored as one artifact originally.

## Bias and emphasis rules (apply only inside SET B narratives)
- Classify every decision/artifact as:
  - ADOPTED (preferred path / “good idea”)
  - REJECTED
  - DEFERRED
  - UNKNOWN (insufficient evidence)
- Present ADOPTED items first as the recommended path where a recommendation exists in-thread.
- Preserve REJECTED items with rationale.
- Preserve DEFERRED items as deferred.
- Preserve UNKNOWN items as open questions/risks.
- “Good idea” signals must be evidenced in-thread. If classification requires inference, label it as inference.

## Splitting rules (mandatory)
- Each document must stay within platform length limits.
- When nearing limits, split into sequential parts with stable IDs:
  - e.g., B-ARCH-001-P1, B-ARCH-001-P2
- Splitting must not remove detail; it must only partition it.
- INDEX must link to every part.

## INDEX document (MUST be first)
Create an INDEX document first that explains the split and maps everything:
- Grouped by Output Set (A/B/C)
- For each document: Document ID, title, one-line purpose, covered turns, and cross-links
- Include the Deliverables Manifest (DEL-### → SET C doc ID + SET B doc ID(s))
- Include a Topic Map (topic → decisions/artifacts covered)

## Required structure inside EVERY document (same order)
1) Executive snapshot (only what’s necessary to orient the archive; no content loss elsewhere)
2) Chronological transcript (cleaned for readability but content-faithful; include timestamps/turn numbers if available)
3) Extracted artifacts (specs, models, schemas, lists, drafts, decisions) as durable sections
4) Decision log (decision, date/turn, rationale, alternatives rejected, dependencies)
5) Assumptions + unknowns + gaps (each with why it matters and what evidence is missing)
6) Actionable backlog (tasks phrased as build/test/research items, ordered by dependency)
7) Reference appendix (glossary of terms defined in-thread; canonical links mentioned; identifiers)

## Additional requirements for SET B (type-agnostic synthesis)
Inside section “3) Extracted artifacts”, include only the subsections that match the Document Class.
Mandatory for all classes:
- Adopted core (if any)
- Evidence excerpts (verbatim transcript snippets with turn IDs supporting adopted core)
Class-specific additions:
- If whitepaper: problem → adopted approach → architecture → implications → rejected/deferred → evidence
- If roadmap: phases → dependencies → acceptance gates → risks → evidence
- If research-memo: research questions → findings (verbatim) → gaps → next studies → evidence
- If example-code-pack: code blocks verbatim + how-to-run + constraints → evidence
- If architecture-design-doc: components → boundaries → data/control flows → contracts → evidence

## Formatting rules
- Use Markdown headings consistently (H1 for document title; H2 major sections; H3 subsections).
- Use stable IDs for cross-references (DEC-###, ART-###, GAP-###, DEL-###) and refer to them throughout.
- Use code fences for code, schemas, prompts, and command sequences exactly as written in the conversation.

## Output
Produce the document sets directly in Canvas and/or Artifact format, ready for Markdown download.
