# Orchestrator Pattern: Audit Observations Are Not Owner Gates After Correction

When a QA or audit worker records an observation as an optional UX improvement,
do not automatically preserve it as an owner decision gate after the owner
corrects it as no-action.

If the owner says the behavior should remain unchanged, reconcile every status
surface in the same closeout pass:

- Mark the related decision WO `OBSOLETE` or rejected/no-action.
- Resolve any blocker created from the observation.
- Remove owner-gated language from `PROJECT-STATUS`, `WO-INDEX`, open-agent
  ledgers, QA reports, and issue files.
- State the settled behavior plainly: preserve the current behavior unless the
  owner explicitly reopens it.

This prevents future orchestrators from converting an audit note into repeated
owner work after the owner has already settled the behavior.
