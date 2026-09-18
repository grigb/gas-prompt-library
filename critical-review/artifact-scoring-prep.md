# Critical Review Artifact Scoring Prep

Use this prompt for Critical Review packet preparation before any high-effort review dispatch.

This is a lighter-model, remedial, cheapest-passing preparation phase. Do not dispatch Fable, a frontier model, or `ireview` top-model review for this scoring task. Reserve Fable/frontier/`ireview` high-effort model use for the final Critical Review after the packet readiness checker passes.

## Inputs

- Critical Review draft or review question:
- Candidate artifact list with absolute paths:
- Known risk class:
- Known dependencies or provenance notes:
- Freshness evidence if available:
- Project principles/goals or durable-posture summary if available:
- Known owner-gate surfaces or likely follow-up classes if available:
- Known Social/peers.social substrate relevance if LAN/PeerMesh/PM Social/UM/MSF/SIGGRAPH are in scope:
- Requested high-effort model directive if owner supplied one, such as GPT-5.6 Sol Extra High / never Spark:

## Task

Score each candidate artifact from 1 to 5 on each dimension before computing any final rank. Keep the dimension scores separate so a later agent can see why an artifact was included or excluded.
When the evidence supports a best durable posture, preserve that posture and the reasons weaker paths were rejected so the final Fable prompt can use it directly instead of turning the issue into an owner menu.
Also preserve project-motion context: what safe work can continue after the review, what would create a future Critical Review trigger, and what would make a rerun redundant.

Dimensions:

- Review-question relevance: can this artifact directly answer the review question?
- Risk leverage: would a finding here materially change the decision, safety gate, or priority?
- Evidence centrality: is this primary evidence rather than summary, hearsay, or stale context?
- Runtime evidence value: for software/runtime reviews, is this source/config/deploy/test/verification evidence
  required to judge security, money, production, architecture, privacy, data-loss, or launch readiness?
- Dependency centrality: is this needed to interpret another included artifact?
- Freshness: is the artifact current enough for the review question?
- Provenance quality: is the source, author, timestamp, or chain of custody clear?
- Noise risk: will this consume context without likely value?

Use this default final score unless the review question gives a stronger domain-specific formula:

`(review-question relevance + risk leverage + evidence centrality + runtime evidence value + dependency centrality + freshness + provenance quality) - noise risk`

## Output Format

For each candidate artifact:

- Path:
- Review-question relevance: 1-5, with reason
- Risk leverage: 1-5, with reason
- Evidence centrality: 1-5, with reason
- Runtime evidence value: 1-5, with reason
- Dependency centrality: 1-5, with reason
- Freshness: 1-5, with reason
- Provenance quality: 1-5, with reason
- Noise risk: 1-5, with reason
- Final score:
- Include / exclude / available on request:

Then produce:

- Recommended imported-file packet: ordered paths with one-line inclusion rationale.
- Best-posture summary: one short statement of the strongest evidence-backed posture, or the exact missing evidence if it is not knowable.
- Follow-up classification notes: any candidate items that look like direct safe remediation, safe WO dispatch, true owner gate, external blocker, or Fable/top-model direct-edit follow-up.
- Project-motion notes: likely next front after review: direct edit, Codex/project lane, blocker-supervisor lane, owner live/production gate, evidence loop, or future Critical Review trigger.
- Rerun/hold note: whether the current packet suggests no redundant top-model rerun now, and what ordinary project execution should continue instead.
- Social substrate note: for LAN/PeerMesh/PM Social/UM/MSF/SIGGRAPH, how peers.social functions as trust/auth substrate through identity/lifecycle authority, tenant SSO, follow/unfollow proof, authenticated tenant-health proof, UM selective-disclosure adoption, or presentation/story proof.
- Required code/config/deploy/test/verification evidence: paths that must not be left as optional lookup for
  high-risk software/runtime reviews.
- Claim-to-evidence map: major risk claims mapped to required evidence, or explicit missing-evidence findings.
- Exclusions list: paths excluded and why.
- Unresolved evidence gaps: missing artifacts, stale sources, unclear provenance, or dependency gaps the final reviewer should treat as limitations.
- Secret-scrub concerns: any artifact that must be scrubbed before dispatch; do not quote secret values.
- Confidence: high, medium, or low, with one sentence explaining what would change the confidence.

## Boundary

This task prepares the target list only. It does not perform the Critical Review, does not issue `GO` / `GO_WITH_CHANGES` / `HOLD` / `NO_GO`, and does not call or simulate Fable/frontier/`ireview` top-model judgment.
