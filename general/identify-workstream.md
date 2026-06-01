# Identify Your Workstream

When asked "what workstream are you working in?" or given this prompt, respond with:

```
Workstream: [name from projects.yaml, or propose a new name if unregistered]
Project: [parent project slug from projects.yaml]
Roots: [absolute paths to the directories you're working in]
Harness: [claude or codex, per the harness split policy]
One-liner: [what this workstream does in 10 words or fewer]
```

Check `/Users/grig/.agents/agents/blocker-engineer/projects.yaml` for existing workstream names under the `workstreams:` array of your parent project. If your work doesn't match any registered workstream, propose a new name and roots.

The harness split policy is at `/Users/grig/.agents-private/project-steward/master-steward/HARNESS-SPLIT-POLICY-2026-06-01.md`. In short: GAS/Fusion/DC/Standards = Claude. PeerMesh/LAN/Knowledge = Codex.
