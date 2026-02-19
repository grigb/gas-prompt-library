Read AGENTS.md and PROJECT-RULES.md for context first, then execute.

Project context resolution (do not ask the user to fill placeholders):
- `PROJECT_SOURCE_ROOT`: current working directory (`pwd`), treated as the source workspace root.
- `PROJECT_NAME` / `PROJECT_ID`: resolve in this order:
  1. `PROJECT-ID.md` in `PROJECT_SOURCE_ROOT` (`project:`, `id:`, or `**Project Name**:` field)
  2. repository directory basename
  3. git remote repo name (fallback only)
- `K2B_ARTIFACT_ROOT`: resolve with policy-aware precedence:
  1. explicit `K2B_ARTIFACT_ROOT:` in `PROJECT-RULES.md`, `AGENTS.md`, or project governance docs
  2. if exactly one established candidate exists among:
     - `PROJECT_SOURCE_ROOT/.dev/ai`
     - `PROJECT_SOURCE_ROOT/.dev/modules/*/.dev/ai`
  3. fallback: `PROJECT_SOURCE_ROOT/.dev/ai`
- If `K2B_ARTIFACT_ROOT` differs from `PROJECT_SOURCE_ROOT/.dev/ai`, record this as a project-specific deviation in decision audit.

Resolved context variables for this run:
- `PROJECT_SOURCE_ROOT`
- `K2B_ARTIFACT_ROOT`
- `PROJECT_NAME`

Rule authority (this prompt is an entrypoint, not the source of truth):
- `/Users/grig/.agents/docs/methodologies/knowledge-to-build-method.md`
- `/Users/grig/.agents/modes/KNOWLEDGE-TO-BUILD-MODE.md`
- `/Users/grig/.agents/docs/vision/VISION-ADDENDUM-knowledge-index-to-build-mandate.md`
If this prompt and those files diverge, follow the authority files and record divergence in decision audit.

Goal:
Create or reconcile full Knowledge-to-Build (K2B) project infrastructure, including mandatory Stage -1 (resource gather) and Stage 0 (knowledge-index projection + corpus materialization), so this project can run K2B immediately regardless of current repo state.

Canonical references (do not duplicate these files, link to them):
- /Users/grig/.agents/docs/methodologies/knowledge-to-build-method.md
- /Users/grig/.agents/modes/KNOWLEDGE-TO-BUILD-MODE.md
- /Users/grig/.agents/knowledge-sources/INDEX.md
- /Users/grig/.agents/knowledge-sources/PROCESS.md
- /Users/grig/.agents/docs/vision/VISION-ADDENDUM-knowledge-index-to-build-mandate.md
- /Users/grig/.agents/scripts/validate-k2b-gates.sh
- /Users/grig/.agents/scripts/k2b-stage0-init.sh
- /Users/grig/.agents/templates/k2b/K2B-BOOTSTRAP-REPORT-TEMPLATE.md
- /Users/grig/.agents/templates/k2b/K2B-DECISION-AUDIT-TEMPLATE.md
- /Users/grig/.agents/templates/k2b/STAGE0-PROJECT-MASTER-INDEX.md
- /Users/grig/.agents/templates/k2b/STAGE0-SOURCE-SELECTION.md
- /Users/grig/.agents/templates/k2b/STAGE0-MATERIALIZATION-MODE.md
- /Users/grig/.agents/templates/k2b/STAGE0-SOURCE-MAP.md
- /Users/grig/.agents/templates/k2b/LEDGER-TEMPLATE.md
- /Users/grig/.agents/templates/k2b/GATES-TEMPLATE.md
- /Users/grig/.agents/templates/k2b/EXTRACTION-INVENTORY-TEMPLATE.md
- /Users/grig/.agents/templates/k2b/VALIDATION-REPORT-TEMPLATE.md
- /Users/grig/.agents/templates/k2b/BUILD-EXTRACTION-TEMPLATE.md

Execution constraints:
1. Detect current state first and produce a gap list.
2. Be idempotent: reuse existing files/directories when possible; do not create duplicates.
3. Never destroy existing project work; merge or append safely.
4. Use absolute paths in all outputs.
5. No markdown tables in generated reports; use headings and bullet lists.
6. Preserve provenance: any localized corpus artifact must map back to origin source paths.

Stage -1 is mandatory before Stage 0:
0. If Stage -1/0 files are missing, scaffold first (recommended):
   - `/Users/grig/.agents/scripts/k2b-stage0-init.sh --project-root "$PROJECT_SOURCE_ROOT" --artifact-root "$K2B_ARTIFACT_ROOT" --project-name "$PROJECT_NAME" --mode localized`
1. Create/refresh candidate inventory:
   - `K2B_ARTIFACT_ROOT/knowledge-index/CANDIDATE-SOURCES.md`
2. Enumerate candidate pools and absolute paths from:
   - project docs/work orders/reports/decisions/research/handoffs
   - relevant global index artifacts under `/Users/grig/.agents/knowledge-sources/`
   - approved external source pools
3. Produce dry-run disposition proposal (`selected`, `deferred`, `excluded`) with counts and rationale.

Stage 0 is mandatory before Stage 1:
1. Create or locate a project-lens master index in:
   - /Users/grig/.agents/knowledge-sources/project-indexes/
2. Create project-local Stage 0 artifacts:
   - `K2B_ARTIFACT_ROOT/knowledge-index/PROJECT-MASTER-INDEX.md`
   - `K2B_ARTIFACT_ROOT/knowledge-index/SOURCE-SELECTION.md`
   - `K2B_ARTIFACT_ROOT/knowledge-index/MATERIALIZATION-MODE.md`
3. Choose materialization mode:
   - reference: keep sources remote; use absolute paths
   - localized: create local corpus artifacts with provenance mapping
4. If mode is localized (default for active planning/design/build), create:
   - `K2B_ARTIFACT_ROOT/knowledge-corpus/SOURCE-MAP.md`
   - `K2B_ARTIFACT_ROOT/knowledge-corpus/imports/`
   - `K2B_ARTIFACT_ROOT/knowledge-corpus/synthesis/`

Required K2B infrastructure (create if missing, reconcile if present):
- `K2B_ARTIFACT_ROOT/ingestion/LEDGER.md`
- `K2B_ARTIFACT_ROOT/ingestion/GATES.md`
- `K2B_ARTIFACT_ROOT/ingestion/records/`
- `K2B_ARTIFACT_ROOT/ingestion/reports/`
- `K2B_ARTIFACT_ROOT/research/RESEARCH-INDEX.md`
- `K2B_ARTIFACT_ROOT/reports/extraction-inventory.md`
- `K2B_ARTIFACT_ROOT/reports/validation-report.md`
- `K2B_ARTIFACT_ROOT/reports/build-extraction.md`
- `K2B_ARTIFACT_ROOT/specs/`
- `K2B_ARTIFACT_ROOT/workorders/WO-INDEX.md`
- `K2B_ARTIFACT_ROOT/decisions/`
- `K2B_ARTIFACT_ROOT/K2B-README.md`

K2B-README.md must include:
- project-specific scope and milestone target
- Stage -1 summary (candidate pool and disposition baseline)
- Stage 0 summary (project index file, selected sources, materialization mode)
- source corpus locations (remote and/or localized)
- chosen application profile(s)
- stage-by-stage artifact map for this project (Stage -1 through Stage 7)
- command examples for running K2B in this repo
- when to run `/Users/grig/.agents/scripts/validate-k2b-gates.sh`

MANDATORY DELIVERABLES (required on every bootstrap/reconciliation run):
- `K2B_ARTIFACT_ROOT/reports/K2B-BOOTSTRAP-REPORT-<YYYY-MM-DD-HH-MM-SS>.md`
- `K2B_ARTIFACT_ROOT/reports/K2B-DECISION-AUDIT-<YYYY-MM-DD-HH-MM-SS>.md`

Hard requirement:
- Both deliverables are mandatory on every bootstrap/reconciliation run.
- Missing either file means the run is incomplete.

Bootstrap report must include:
- Executive summary
- Detected starting state
- Stage -1 setup details:
  - candidate pools scanned
  - candidate count and dry-run disposition counts
- Stage 0 setup details:
  - project master index used/created
  - materialization mode selected and why
  - selected/deferred/excluded counts
  - provenance status
- Files/dirs created
- Files updated
- Existing assets reused
- Gate-readiness snapshot:
  - Stage -1 gate
  - Stage 0 gate
  - G1/G2/G3/G4/G5/G6/G7 where applicable
- Blockers and risks
- Validation commands run and outcomes
- K2B improvement feedback (critical):
  - what in K2B docs/mode/validator was unclear or brittle
  - false positives/false negatives in validation
  - missing templates or automation
  - naming/path/discoverability issues
  - prioritized recommendations:
    - P1 fixes (high impact)
    - P2 improvements
    - P3 polish
  - exact proposed file-level changes to GAS (do not apply globally, just propose)

Decision audit must include:
- Baseline assumptions used for this project
- Stage -1 and Stage 0 decision rationale (mode and source promotion/defer/exclude logic)
- Project-specific deviations from canonical K2B bootstrap flow
- Why each deviation was necessary in this project state
- Before/after source counts (`selected`, `deferred`, `excluded`)
- Evidence paths that prove each major decision
- Residual risks created by those decisions
- Reversal plan (how to undo/adjust key decisions safely)

Validation:
- Verify every required path exists.
- Verify all selected Stage 0 sources resolve (remote or local).
- If enough artifacts exist, run:
  `/Users/grig/.agents/scripts/validate-k2b-gates.sh "$PROJECT_SOURCE_ROOT" --artifact-root "$K2B_ARTIFACT_ROOT"`
- If artifacts are not sufficient yet, explicitly mark validator as "not applicable yet" and explain why.

Final response format:
- Resolved project source root
- Resolved K2B artifact root
- Resolved project name/id
- Root policy decision (default or override, with reason)
- Bootstrap report path
- Decision audit path
- Materialization mode used
- Project master index path used
- Created paths
- Updated paths
- Reused paths
- Remaining blockers
- Exact next 3 commands to begin Stage 1 immediately
