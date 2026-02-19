Read `AGENTS.md` and `SOURCE_OF_TRUTH.md` first, then execute.
If `PROJECT-RULES.md` is missing, record that as a non-blocking governance gap and continue.

Context (already done):
- Stage 0 wide-lens reset is complete.
- Current critical path is `WO-PMDL-2026-02-19-017 -> WO-PMDL-2026-02-19-018`.
- Do not run Stage 4+ rebuild in this run.
- Do not return a report-only summary without WO-linked file changes.

Roots:
- Source root: `/Users/grig/work/peermesh/repo/knowledge-graph-lab-alpha`
- Module root: `/Users/grig/work/peermesh/repo/knowledge-graph-lab-alpha/.dev/modules/peer-mesh-docker-lab`
- Artifact root: `/Users/grig/work/peermesh/repo/knowledge-graph-lab-alpha/.dev/modules/peer-mesh-docker-lab/.dev/ai`

Primary objective for this run:
- Execute `WO-PMDL-2026-02-19-017` (Stage 1-3 re-ingestion and extraction reconciliation) with concrete, auditable deltas.

Authority files:
- `/Users/grig/work/peermesh/repo/knowledge-graph-lab-alpha/.dev/modules/peer-mesh-docker-lab/.dev/ai/workorders/WO-PMDL-2026-02-19-017.md`
- `/Users/grig/work/peermesh/repo/knowledge-graph-lab-alpha/.dev/modules/peer-mesh-docker-lab/.dev/ai/workorders/WO-INDEX.md`
- `/Users/grig/work/peermesh/repo/knowledge-graph-lab-alpha/.dev/modules/peer-mesh-docker-lab/.dev/ai/STATE-OF-THE-PROJECT.md`
- `/Users/grig/work/peermesh/repo/knowledge-graph-lab-alpha/.dev/modules/peer-mesh-docker-lab/.dev/ai/reports/stage0-reset-promoted-2026-02-19-06-23-51Z.txt`

Mandatory execution requirements:
1) Advance WO-017 acceptance criteria in this run (not status-only notes).
2) Produce real file changes (minimum 5 files), including all of:
   - `/Users/grig/work/peermesh/repo/knowledge-graph-lab-alpha/.dev/modules/peer-mesh-docker-lab/.dev/ai/ingestion/LEDGER.md`
   - `/Users/grig/work/peermesh/repo/knowledge-graph-lab-alpha/.dev/modules/peer-mesh-docker-lab/.dev/ai/ingestion/GATES.md`
   - `/Users/grig/work/peermesh/repo/knowledge-graph-lab-alpha/.dev/modules/peer-mesh-docker-lab/.dev/ai/reports/stage3/STAGE3-EXTRACTION-INVENTORY.md`
   - `/Users/grig/work/peermesh/repo/knowledge-graph-lab-alpha/.dev/modules/peer-mesh-docker-lab/.dev/ai/reports/stage3/STAGE3-TRACEABILITY-MATRIX.md`
   - `/Users/grig/work/peermesh/repo/knowledge-graph-lab-alpha/.dev/modules/peer-mesh-docker-lab/.dev/ai/reports/extraction-inventory.md`
   - `/Users/grig/work/peermesh/repo/knowledge-graph-lab-alpha/.dev/modules/peer-mesh-docker-lab/.dev/ai/workorders/WO-PMDL-2026-02-19-017.md`
3) Build a promoted-source impact summary from the Stage 0 promoted list:
   - include which promoted sources materially changed extraction outcomes,
   - include architecture/design pivots discovered from those sources,
   - include downstream targets likely affected in Stage 4+.
4) Run strict validator with explicit artifact root (Bash 5.3 runtime):
   - `/opt/homebrew/bin/bash /Users/grig/.agents/scripts/validate-k2b-gates.sh /Users/grig/work/peermesh/repo/knowledge-graph-lab-alpha/.dev/modules/peer-mesh-docker-lab --artifact-root /Users/grig/work/peermesh/repo/knowledge-graph-lab-alpha/.dev/modules/peer-mesh-docker-lab/.dev/ai --strict`
5) Save strict validator output to:
   - `/Users/grig/work/peermesh/repo/knowledge-graph-lab-alpha/.dev/modules/peer-mesh-docker-lab/.dev/ai/reports/<YYYY-MM-DD-HH-MM-SS>-wo-017-strict-validator.log`

Required run report:
- `/Users/grig/work/peermesh/repo/knowledge-graph-lab-alpha/.dev/modules/peer-mesh-docker-lab/.dev/ai/reports/<YYYY-MM-DD-HH-MM-SS>-wo-017-stage1-3-execution-progress.md`

Report must include:
- WO-017 acceptance criteria status before/after
- exact files changed
- selected/deferred/excluded counts referenced for this run
- promoted-source impact summary
- architecture/design pivots discovered from promoted corpus
- strict validator command + exit code + log path
- blockers requiring user decision
- exact next 3 executable shell commands (full commands only)

Disallowed output pattern:
- Do not end with only a maintenance summary.
- Do not output bare filenames/paths as commands.
- Do not claim completion of WO-017 without file-level evidence.

Final chat response format:
- Source root
- Module root
- Artifact root
- Resumed WO
- Acceptance criteria moved
- Files changed
- Promoted-source pivots discovered
- Strict validator command and exit code
- Blockers
- Exact next 3 commands
