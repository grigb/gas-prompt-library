---
description: Generates a comprehensive, keyword-based knowledge index for a specific project domain.
author: PeerMesh Agents
created: 2026-01-15
version: 1.0
priority: high
scope: project
tags: [knowledge, index, research, scanner]
---

# PROJECT KNOWLEDGE INDEX GENERATION PROTOCOL

**Use this mode to generate a definitive `FULL_RESEARCH_INDEX.md` for a project.**
This process replaces ad-hoc searching with a systematic, comprehensive scan of all available knowledge sources.

## 1. SCOPING & CONCEPTUALIZATION

Before scanning, you must define WHAT you are looking for.

1.  **Read Project Context**: `VISION.md`, `README.md`, `AGENTS.md`.
2.  **Identify Core Domains**: What represent the "hard problems" or "core entities" of this project? (e.g., "Identity", "Federation", "Consensus", "Encryption").
3.  **Generate Keywords**: For each domain, list 5-10 specific technical keywords (e.g., "ActivityPub", "WebID", "CRDT", "Yjs").
4.  **Create Scope Artifact**: 
    - Create/Update `.dev/ai/planning/KNOWLEDGE_SCOPE.md`
    - Format:
      ```markdown
      # Knowledge Scope: [Project Name]
      
      ## Core Domains
      
      ### 1. [Domain Name]
      - **Concept**: [Brief description]
      - **Keywords**: [comma, separated, list]
      - **Rationale**: Why this matters.
      ```

## 2. SCANNING & INDEXING

Use the `source_scanner` (or `scan.py`) to execute a comprehensive scan based on your scope.

1.  **Configure Scanner**:
    - Use the keywords defined in `KNOWLEDGE_SCOPE.md`.
    - Target all sources in `~/.agents/knowledge-sources/INDEX.md` (or a subset if specified).
2.  **Run Scan**:
    - Execute the scan to generate a raw hit list.
3.  **Refine & Categorize**:
    - **Crucial**: The output MUST be hierarchical, not a flat list.
    - Structure: `Top Level Category` -> `Sub-Category` -> `Directory` -> `Files`.
    - Use the `classify_file` logic (update `scan.py` if needed for new domains) to group files intelligently.
4.  **Generate Artifact**:
    - Output file: `docs/FULL_RESEARCH_INDEX.md` (or temp location).

## 3. GLOBAL PROMOTION (Archival)

Turn this local index into a permanent global asset.

1.  **Timestamp & Archive**:
    - Copy the generated index to: `~/.agents/knowledge-sources/project-indexes/`
    - Name: `YYYY-MM-DD_[PROJECT-NAME]_master-index.md`
2.  **Register**:
    - Append entry to `~/.agents/knowledge-sources/INDEX.md` under "Shared Project Indexes".
    - `| Date | [Link](path) | Domain | Coverage Summary |`

## 4. PROJECT INTEGRATION

Connect the project to this new knowledge base.

1.  **Update AGENTS.md**:
    - Add "Knowledge Base" section pointing to the global file.
2.  **Update REFERENCE_INDEX.md** (if exists):
    - Link to the `file://` path of the global artifact.
3.  **Clean Up**:
    - Remove local `docs/FULL_RESEARCH_INDEX.md` if it duplicates the global one.

---

## EXECUTION PROMPT (Copy/Paste to start)

To initiate this process, run:

```text
I need to generate a full knowledge index for this project.
1. Read the vision and context.
2. Create .dev/ai/planning/KNOWLEDGE_SCOPE.md defining our core domains and keywords.
3. Use the knowledge scanner to find ALL matching documents in the global registry.
4. Generate a hierarchical index and promote it to the global ~/.agents system.
```
