---
title: "Agent Tool Exposure Guide"
created: 2026-06-05
source_work_order: WO-AAO-005
scope: Agent-facing entry point for Agent Attention Optimization guidance in GAS
---

# Agent Tool Exposure Guide

Use this guide when the user asks to expose, publish, optimize, or make a GAS tool, skill, MCP server, A2A agent, OpenAPI endpoint, SKILL.md package, workflow, or capability discoverable by agents or developer communities.

Do not use this guide as the default path for Universal Manifest work. Universal Manifest work only enters this path when the Master Steward or UM Steward explicitly routes it here.

## Start Here

Read these files in order:

1. `/Users/grig/.agents/.dev/ai/research/agent-attention-optimization/INDEX.md`
2. `/Users/grig/.agents/.dev/ai/research/agent-attention-optimization/phase-2-agent-attention-optimization-methodology.md`
3. `/Users/grig/.agents/.dev/ai/research/agent-attention-optimization/COMMUNITY-LAUNCH-CHECKLIST.md`
4. `/Users/grig/.agents/.dev/ai/research/agent-attention-optimization/ECOSYSTEM-MONITORING-PLAN.md`
5. `/Users/grig/.agents/.dev/ai/research/agent-attention-optimization/AAO-TAXONOMY-MAPPING.md`
6. `/Users/grig/.agents/.dev/ai/reports/2026-06-05-16-42-21Z-aao-program-steward-handoff-report.md`

The AAO knowledge base root is `/Users/grig/.agents/.dev/ai/research/agent-attention-optimization/`.

## Related Codex Browser-Control Routing

For Codex browser-visible work, frontend/local dashboard verification,
authenticated web apps, or questions about Chrome Extension versus Computer
Use, in-app Browser, Agent Browser, CDP, or Playwright-style tooling, read:

`/Users/grig/.agents/docs/browser-control/codex-browser-tool-routing.md`

That policy is a GAS-wide tool-routing rule, not an AAO exposure workflow.
Use it before selecting a browser-control surface.

## Use AAO When

- A GAS capability needs an agent-facing description, contract, manifest, registry listing, or public launch plan.
- A tool is hard for agents to find, choose, invoke, or distinguish from nearby tools.
- A capability is being prepared for MCP, A2A, OpenAPI, SKILL.md, well-known metadata, JSON-LD, WoT, marketplace, or registry exposure.
- A launch needs both human community discovery and agent discovery.
- An existing exposure lane needs verification, monitoring, or lifecycle review.

## Do Not Use AAO When

- The task is only to implement internal feature behavior with no discoverability or exposure surface.
- The request is to apply bulk tool description fixes already assigned to another work order.
- The work is Universal Manifest-specific and has not been explicitly routed here by Master Steward or UM Steward.

## Taxonomy

- AEO: Answer Engine Optimization. Get tools surfaced in direct AI answers.
- GEO: Generative Engine Optimization. Get tools cited or recommended in AI-generated content.
- LLMO: Large Language Model Optimization. Make tool descriptions and schemas parseable and selectable by LLMs.
- AXO: Agent Experience Optimization. Make tools discoverable, evaluable, invocable, observable, and safe for agents.

AAO usually centers AXO and LLMO first, then uses AEO/GEO through documentation, community launch, and content strategy.

## First Optimization Gate

Tool description quality is the first gate before protocol or launch work. Check whether the capability has:

- a clear short description with what, when, and constraints;
- a long description with when to use, when not to use, examples, failure modes, and side effects;
- semantic aliases matching likely agent and user language;
- typed inputs, outputs, and errors;
- trust, cost, latency, rate limit, and safety signals;
- negative disambiguation against similar tools.

Do not assume MCP, A2A, OpenAPI, or a registry listing will fix a weak capability description.

## Launch And Monitoring

Use `/Users/grig/.agents/.dev/ai/research/agent-attention-optimization/COMMUNITY-LAUNCH-CHECKLIST.md` before public release, MCP server publication, registry submission, or community promotion. It covers GitHub presence, README quality, tool descriptions, `/llms.txt`, JSON-LD, registry order, 48-hour launch execution, and post-launch cadence.

Use `/Users/grig/.agents/.dev/ai/research/agent-attention-optimization/ECOSYSTEM-MONITORING-PLAN.md` when a capability needs ongoing visibility tracking, competitor monitoring, protocol-change monitoring, AI share-of-voice baselines, or description-selection evals.

## Minimum Agent Workflow

1. Identify the capability and owner.
2. Read the AAO index and methodology.
3. Classify the capability by taxonomy layer and tool archetype.
4. Improve the capability contract and tool description before choosing an exposure lane.
5. Select the exposure lane from the methodology: MCP, A2A, OpenAPI, SKILL.md, well-known metadata, semantic index, JSON-LD, WoT, marketplace, or registry.
6. Verify discovery, evaluation, authorization, invocation, errors, side effects, and observability.
7. Use the launch checklist if the capability will be public or community-facing.
8. Use the monitoring plan once discovery or publication begins.
