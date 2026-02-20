Run an adversarial (red-team) end-to-end system review now (not a meta-review).

Project root:
`/Users/grig/work/peermesh/repo/knowledge-graph-lab-alpha/.dev/modules/peer-mesh-docker-lab`

Mission:
Try to break the system on paper and in validation checks: find where future agents could produce wrong conclusions while appearing compliant.

Execution steps:

1) Read the same canonical docs + charter and derive goals/design intent.
2) Inspect implementation in `sub-repos/docker-lab/`.
3) Run these checks for evidence:
- `cd /Users/grig/work/peermesh/repo/knowledge-graph-lab-alpha/.dev/modules/peer-mesh-docker-lab/sub-repos/docker-lab`
- `./scripts/deploy.sh --validate --evidence-root /tmp/claude-redteam-deploy --evidence-tag claude-redteam`
- `./scripts/security/validate-supply-chain.sh --severity-threshold CRITICAL --output-dir /tmp/claude-redteam-supply-chain`
- `./scripts/scalability/run-wave1-validation.sh --output-dir /tmp/claude-redteam-wave1`

4) Produce red-team report sections:
- Review Metadata (date, reviewer, charter version)
- Breach Verdict
- Top Exploits (P0/P1/P2) with trigger/impact/evidence/containment fix
- Contradiction Matrix (doc authority conflicts)
- Adversarial Test Cases (at least 8)
- Patch Set (exact text edits)
- Residual Risk Register (risk score + confidence)

5) Save report to:
`.dev/ai/reviews/SYSTEM-REVIEW-2026-02-20-redteam-run.md`

6) Return a concise summary in chat:
- P0 exploit list
- immediate containment actions
- approve/do-not-approve for long-horizon use

Constraints:
- Evidence-based only, cite exact file paths.
- Preserve provenance and work-order history.
- Respect parent-only `.dev` policy.
- Respect charter Section 6 guardrails.
- No code/doc edits unless explicitly requested after report.
