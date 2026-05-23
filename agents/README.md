# 🤖 Specialized Agent Directory

This directory contains specialized AI agents designed for specific domains and workflows. Each agent is optimized for particular types of tasks and can be invoked through various AI platforms and tools.

## 🚀 How to Use Agents

### **In Claude Code & Cursor**
Agents are designed to work within coding environments where you can invoke specialized capabilities:

```bash
# Invoke via task tool (recommended for complex work)
<task>agent-orchestrator: Design multi-agent workflow for project launch</task>

# Direct agent invocation
Use agent-orchestrator for coordinating complex projects
```

### **In Chat Interfaces (Claude, Gemini, Codex)**
For conversational use, reference the specific agent by name and provide context:

```
"I need the agent-research-analysis to investigate microservices architecture options"
"Use agent-dev-general-contractor to audit this code for production readiness"
```

### **Agent Selection Guidelines**
- **Complex coordination** → `agent-orchestrator`
- **Code review/QA** → `agent-dev-general-contractor`
- **Research tasks** → `agent-research-analysis`
- **UI/UX design** → `agent-ux-design`
- **Data analysis** → `agent-data-analysis-visualization`

### **Agent Categories**

## 🏗️ **Core Development Agents**

### `agent-orchestrator.md`
**Master coordinator for complex multi-agent workflows**
- Analyzes complex requests and designs optimal agent configurations
- Breaks down projects into parallel/sequential workstreams
- Coordinates multiple specialized agents
- **Use for:** Large projects requiring multiple agents, workflow design, dependency mapping

### `agent-dev-general-contractor.md`
**Senior QA lead and integration specialist**
- Audits code quality, security, and test coverage
- Guides integration of components from specialized workers
- Performs pre-deployment verification
- **Use for:** Code reviews, integration testing, production readiness checks

### `agent-dev-overseer.md`
**Development process monitor and quality assurance**
- Oversees development workflows and milestones
- Monitors progress and identifies bottlenecks
- Ensures development standards and practices
- **Use for:** Process monitoring, workflow optimization, standards enforcement

### `agent-dev-worker.md`
**Core implementation and coding specialist**
- Executes specific development tasks and features
- Implements technical specifications
- Handles coding and debugging work
- **Use for:** Feature implementation, bug fixes, technical development

### `agent-software-product-builder.md`
**End-to-end product development coordinator**
- Builds complete software products from concept to deployment
- Manages full product lifecycle
- Coordinates technical and business requirements
- **Use for:** Product development, full-stack solutions, MVP creation

## 🔬 **Research & Analysis Agents**

### `agent-research-analysis.md`
**Expert researcher for technical, legal, and market topics**
- Conducts systematic research with evidence-based findings
- Analyzes technical systems and architectures
- Investigates legal/regulatory frameworks
- **Use for:** Technology research, compliance analysis, market investigation

### `agent-research-gap-analysis.md`
**Specialist in identifying knowledge and research gaps**
- Analyzes existing research and identifies missing information
- Maps knowledge landscapes and gaps
- Guides research prioritization
- **Use for:** Research planning, knowledge assessment, gap identification

### `agent-strategic-intelligence.md`
**Strategic analysis and intelligence gathering**
- Provides strategic insights and analysis
- Gathers competitive intelligence
- Analyzes market trends and opportunities
- **Use for:** Strategic planning, competitive analysis, market research

### `agent-external-research-prompt-engineer.md`
**Adversarial prompt engineer for external frontier-LLM research prompts**
- Reviews, critiques, redesigns, and authors prompts pasted into Claude.ai, Gemini Advanced, Perplexity Pro, ChatGPT, Grok, and Kimi
- Scores prompts against a 12-primitive library for frame discipline, anti-validation, deliverable shape, source discipline, and reality hooks
- **Use for:** Reviewing research prompts before external paste, hardening prompts against validation-bait, creating reusable deep-research prompt templates

## 💼 **Business & Operations Agents**

### `agent-chief-of-staff.md`
**Executive coordination and strategic planning**
- Manages executive-level coordination
- Handles strategic planning and execution
- Coordinates cross-functional initiatives
- **Use for:** Strategic planning, executive coordination, project oversight

### `agent-chief-reality-officer.md`
**Reality-checking and feasibility assessment**
- Ensures realistic assessments and plans
- Identifies risks and constraints
- Provides objective analysis
- **Use for:** Risk assessment, feasibility studies, reality checks

### `agent-financial-analysis-planning.md`
**Financial modeling and business planning**
- Analyzes financial implications and models
- Plans business strategies and budgets
- Evaluates economic viability
- **Use for:** Financial planning, business analysis, ROI assessment

### `agent-marketing-expert.md`
**Marketing strategy and campaign design**
- Develops marketing strategies and campaigns
- Analyzes market positioning and branding
- Plans promotional activities
- **Use for:** Marketing strategy, campaign planning, brand development

### `agent-project-coordinator.md`
**Project management and milestone tracking**
- Coordinates project activities and timelines
- Tracks milestones and deliverables
- Manages stakeholder communication
- **Use for:** Project management, milestone tracking, stakeholder coordination

### `agent-project-steward.md`
**Single-project advisor/operator and project-local memory steward**
- Captures raw monologues before synthesis
- Maintains project-local wisdom under `.dev/ai/roles/project-steward/`
- Keeps owner-private context outside project-readable files
- Produces top-level-down strategic briefs with blockers and unblock paths
- Maps dependencies and creates/refines work orders
- Separates reusable GAS process from project-specific facts
- **Use for:** "you are the project steward", "steward this project", "project brief", "steward brief", complex thought capture, governance/process synthesis, zero-to-one project stewardship

## 🎨 **Creative & Design Agents**

### `agent-ux-design.md`
**User experience design and interface optimization**
- Designs user interfaces and experiences
- Optimizes usability and accessibility
- Creates wireframes and prototypes
- **Use for:** UI/UX design, interface design, user research

### `agent-content-crafting-alignment.md`
**Content creation and strategic alignment**
- Creates aligned content and messaging
- Ensures brand consistency
- Develops content strategies
- **Use for:** Content creation, messaging alignment, brand consistency

### `agent-innovation-ideation.md`
**Creative problem-solving and innovation generation**
- Generates innovative solutions and ideas
- Facilitates creative brainstorming
- Explores novel approaches
- **Use for:** Innovation, ideation, creative problem-solving

### `agent-communication-stakeholder.md`
**Stakeholder communication and relationship management**
- Manages stakeholder communications
- Builds relationships and manages expectations
- Facilitates collaboration
- **Use for:** Stakeholder management, communication planning, relationship building

## 🔧 **Technical & Infrastructure Agents**

### `agent-data-analysis-visualization.md`
**Data analysis and visualization specialist**
- Analyzes complex datasets
- Creates data visualizations and insights
- Performs statistical analysis
- **Use for:** Data analysis, visualization, statistical modeling

### `agent-testing-validation.md`
**Quality assurance and validation testing**
- Designs and executes test strategies
- Validates system functionality
- Ensures quality standards
- **Use for:** Testing, validation, quality assurance

### `agent-security-compliance.md`
**Security assessment and compliance management**
- Conducts security audits and assessments
- Ensures compliance with standards
- Identifies security vulnerabilities
- **Use for:** Security audits, compliance, risk management

### `agent-tooling.md`
**Tool development and infrastructure management**
- Develops and maintains development tools
- Manages technical infrastructure
- Optimizes development workflows
- **Use for:** Tool development, infrastructure, workflow optimization

### `agent-network-diagnostics-specialist.md`
**Network troubleshooting and diagnostics**
- Diagnoses network issues and problems
- Performs network analysis and optimization
- Troubleshoots connectivity issues
- **Use for:** Network diagnostics, troubleshooting, connectivity issues

## 📊 **Process & Knowledge Agents**

### `agent-process-analysis-retrospective.md`
**Process improvement and retrospective analysis**
- Analyzes processes and workflows
- Conducts retrospectives and lessons learned
- Identifies improvement opportunities
- **Use for:** Process improvement, retrospectives, workflow analysis

### `agent-process-analysis-retrospective-quick.md`
**Rapid process analysis and feedback**
- Provides quick process assessments
- Delivers immediate feedback and insights
- Identifies quick wins and improvements
- **Use for:** Quick assessments, immediate feedback, rapid improvements

### `agent-process-design-optimization.md`
**Process design and workflow optimization**
- Designs optimal processes and workflows
- Optimizes efficiency and effectiveness
- Streamlines operations
- **Use for:** Process design, workflow optimization, operational efficiency

### `agent-document-analysis-audit.md`
**Document review and audit processes**
- Performs detailed document analysis
- Conducts audits and reviews
- Ensures document quality and compliance
- **Use for:** Document analysis, auditing, compliance review

### `agent-synthesis-integration.md`
**Knowledge synthesis and system integration**
- Synthesizes information from multiple sources
- Integrates disparate systems and data
- Creates unified knowledge bases
- **Use for:** Knowledge synthesis, system integration, data unification

### `agent-learning-knowledge-management.md`
**Learning systems and knowledge organization**
- Manages knowledge bases and learning systems
- Organizes information and documentation
- Facilitates learning and knowledge sharing
- **Use for:** Knowledge management, learning systems, information organization

## 📋 **Agent Usage Best Practices**

### **When to Use Multiple Agents**
- **Complex projects** → Start with `agent-orchestrator` to design the workflow
- **Quality assurance** → Use `agent-dev-general-contractor` for integration verification
- **Research-heavy work** → Combine `agent-research-analysis` with domain specialists

### **Agent Communication**
- Agents are designed to hand off work seamlessly
- Use clear task descriptions when invoking agents
- Reference specific agent names for targeted capabilities

### **Platform Integration**
- **Cursor/Claude Code**: Use task syntax for agent invocation
- **Chat interfaces**: Reference agents by name in conversation
- **Automated workflows**: Chain agents using handoff protocols

Each agent is optimized for its specific domain while maintaining compatibility with the broader agent ecosystem. Reference the main prompts README for integration with work order systems and handoff protocols.
