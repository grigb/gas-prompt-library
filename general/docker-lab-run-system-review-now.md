Run a full end-to-end system review now (not a review of the review process).

Project root:
`/Users/grig/work/peermesh/repo/knowledge-graph-lab-alpha/.dev/modules/peer-mesh-docker-lab`

Goal:
Execute one real review cycle using the charter method, derive system intent from source docs, validate against implementation + runnable checks, and produce concrete improvement suggestions.

Do this exactly:

1) Read these docs first, in this order:
- `DOCKER-LAB-AGENT-LONG-HORIZON-REVIEW-CHARTER.md`
- `VISION.md`
- `SOURCE_OF_TRUTH.md`
- `AGENTS.md`
- `STATE-OF-PROJECT.md`
- `.dev/ai/STATE-OF-THE-PROJECT.md`
- `.dev/ai/workorders/WO-INDEX.md`
- `.dev/ai/DOCKER-LAB-DONE-DONE.md`
- `.dev/ai/decisions/2026-02-19-ceo-mandate-gas-project-index-scoping.md`
- `sub-repos/docker-lab/docs/ARCHITECTURE.md`
- `sub-repos/docker-lab/docs/DEPLOYMENT.md`
- `sub-repos/docker-lab/docs/SECURITY.md`
- `sub-repos/docker-lab/docs/SUPPLY-CHAIN-SECURITY.md`
- `sub-repos/docker-lab/docs/SCALABILITY-RESILIENCE-WAVE1.md`

2) Inspect implementation evidence in:
- `sub-repos/docker-lab/scripts/`
- `sub-repos/docker-lab/infra/opentofu/`
- `sub-repos/docker-lab/docs/`

3) Run these non-destructive checks and use results as evidence:
- `cd /Users/grig/work/peermesh/repo/knowledge-graph-lab-alpha/.dev/modules/peer-mesh-docker-lab/sub-repos/docker-lab`
- `./scripts/deploy.sh --validate --evidence-root /tmp/claude-system-review-deploy --evidence-tag claude-system-review`
- `./scripts/security/validate-supply-chain.sh --severity-threshold CRITICAL --output-dir /tmp/claude-system-review-supply-chain`
- `./scripts/scalability/run-wave1-validation.sh --output-dir /tmp/claude-system-review-wave1`

4) Produce a real review report with these sections:
- Review Metadata (date, reviewer, charter version)
- Derived Goals
- Derived Design Intent
- Implementation Evidence
- Alignment Matrix (ALIGNED / PARTIALLY_ALIGNED / NOT_ALIGNED / UNVERIFIED)
- Alignment Summary Counts
- Suggestions (priority, risk, confidence)
- Provenance Guardrails Check
- Open Questions

5) Save report to:
`.dev/ai/reviews/SYSTEM-REVIEW-2026-02-20-claude-run.md`

6) Also return a concise executive summary in chat:
- top 5 findings
- top 3 suggested next work orders
- confidence score (0-100)

Constraints:
- Evidence-based only, cite exact file paths.
- Preserve provenance; do not rewrite prior decisions.
- Respect parent-only `.dev` policy.
- Respect charter Section 6 guardrails.
- Do not edit code/docs unless explicitly asked afterward.
