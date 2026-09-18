# Contributing to the AI Agent Prompts Library

Welcome! This library powers AI agent orchestration systems with carefully crafted prompts and specialized agent definitions. We appreciate contributions that help make these prompts clearer, more effective, and better organized.

## Ways to Contribute

### 1. Adding New Agents

New agents expand our specialized capabilities. Before creating one:

1. **Check existing agents** in `agents/README.md` to avoid duplication
2. **Read the format guide** at `agents/_agent-format-guide.md` for complete requirements
3. **Follow the naming convention**: `agent-[domain]-[specialty].md` in kebab-case
4. **Place in the correct directory**: All agents go in `agents/`

### 2. Improving Existing Prompts

Improvements might include:
- Clearer instructions that reduce ambiguity
- Better examples that demonstrate expected behavior
- Condensed wording that maintains meaning with fewer tokens
- Fixed errors or outdated information

### 3. Documentation Improvements

Help others use the library by:
- Clarifying usage instructions in READMEs
- Adding practical examples
- Improving directory organization descriptions

### 4. Reporting Issues

Found a problem? Open an issue describing:
- Which prompt or agent is affected
- What behavior you expected
- What actually happened
- Steps to reproduce (if applicable)

## Agent Format Requirements

Every agent file must include these elements:

### Required YAML Frontmatter

```yaml
---
name: agent-name-in-kebab-case
description: When to use this agent. Include 3-5 invocation examples showing context, user request, and task.
model: sonnet|opus|haiku
color: blue|red|green|yellow|purple|orange
---
```

**Field details:**

| Field | Required | Format |
|-------|----------|--------|
| `name` | Yes | Lowercase kebab-case, unique across all agents |
| `description` | Yes | 1-2 sentence overview + 3-5 invocation examples |
| `model` | Yes | `sonnet` (default), `opus` (complex reasoning), or `haiku` (simple tasks) |
| `color` | Recommended | Visual identifier for UI display |

### Required Content Structure

After frontmatter, include:

1. **Agent Identity** - Role, expertise level, core competencies
2. **Operating Principles** - 4-8 core behavioral directives
3. **Methodology** - 3-6 phase process for handling tasks
4. **Communication Protocol** - Expected output formats
5. **Constraints** - Hard limits and anti-patterns

**Target length**: 300-400 lines (excluding frontmatter examples)

See `agents/_agent-format-guide.md` for complete specifications, examples, and the conversion checklist.

## Pull Request Process

### Before You Start

1. Fork the repository
2. Create a feature branch: `git checkout -b add-agent-[name]` or `improve-[prompt-name]`
3. Make your changes following the format guidelines

### What Makes a Good PR

**Do:**
- Focus on one change per PR (one new agent, one prompt improvement)
- Test your prompt with an actual AI model when possible
- Follow existing naming conventions and file organization
- Update the relevant README if adding new files
- Write clear commit messages explaining what and why

**Avoid:**
- Mixing unrelated changes in one PR
- Adding "nice to have" background information that bloats prompts
- Breaking existing functionality
- Introducing duplicate agents that overlap with existing ones

### Submission Steps

1. Commit your changes with a clear message
2. Push to your fork
3. Open a pull request with:
   - Summary of what you're adding or changing
   - Why this change helps the library
   - Any testing you've done

### Review Process

- A maintainer will review your PR
- You may receive feedback or requests for changes
- Once approved, your contribution will be merged

## Quality Standards

All contributions should:

- **Be purpose-driven** - Serve a specific, well-defined function
- **Be self-contained** - Include all necessary context
- **Be consistent** - Follow established patterns
- **Be testable** - Produce predictable, reliable results
- **Be token-efficient** - Say what's needed without unnecessary words

## Code of Conduct

We maintain a professional, collaborative environment:

- **Be respectful** - Constructive feedback only, no personal criticism
- **Be helpful** - Share knowledge and support other contributors
- **Be patient** - Review takes time; everyone is doing their best
- **Be open** - Welcome different perspectives and approaches

Harassment, discrimination, or disrespectful behavior will not be tolerated.

## Questions?

If you're unsure about something:
- Check existing prompts for patterns to follow
- Review the format guide for agent-specific questions
- Open an issue to discuss before starting significant work

Thank you for helping improve this library!
