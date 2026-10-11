<div align="center">

# Serenity.skill

### Turn your investment agent into a supply-chain bottleneck hunter.

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
  <a href="SKILL.md"><img src="https://img.shields.io/badge/Agent%20Skill-SKILL.md-black" alt="Agent Skill"></a>
  <a href="README.md"><img src="https://img.shields.io/badge/README-%E4%B8%AD%E6%96%87-red" alt="Chinese README"></a>
  <a href="README.en.md"><img src="https://img.shields.io/badge/English-README.en.md-lightgrey" alt="English README"></a>
</p>

<p align="center">
  <a href="https://github.com/muxuuu/serenity-skill/stargazers"><img src="https://img.shields.io/github/stars/muxuuu/serenity-skill?logo=github" alt="GitHub Stars"></a>
  <a href="https://github.com/muxuuu/serenity-skill/forks"><img src="https://img.shields.io/github/forks/muxuuu/serenity-skill?logo=github" alt="GitHub Forks"></a>
  <a href="https://skills.sh/muxuuu/serenity-skill"><img src="https://skills.sh/b/muxuuu/serenity-skill" alt="skills.sh installs"></a>
  <a href="https://olud.ai/project/muxuuu-serenity-skill.html"><img src="https://olud.ai/badge.php?tool=muxuuu-serenity-skill" alt="olud.ai directory rank"></a>
</p>

<p align="center"><a href="https://trendshift.io/repositories/47219"><img src="https://trendshift.io/api/badge/trendshift/repositories/47219/daily" alt="TrendShift #22 Repository of the Day across all languages" width="250" height="55"></a></p>

</div>

Serenity.skill turns the supply-chain research patterns observed in public [Serenity / @aleabitoreddit](https://x.com/aleabitoreddit) material into a workflow for ordinary investment research. Start with a technology theme, map the system and its constrained inputs, investigate companies, and return research priorities with evidence and counterarguments.

The primary use case is an A-share technology or advanced-manufacturing theme scan. The same method also supports a company challenge, a comparison, or guided learning, and adapts to other requested markets. Funds and ETFs are an extension when requested.

## What the research covers

- What demand or technical change is putting pressure on the system?
- Which layers are difficult to expand or substitute?
- What does each company sell, and is the relevant product being developed, qualified, delivered or recognized as revenue?
- How can that business affect margins, cash flow and shareholder earnings?
- What expectations are already reflected in a dated valuation?
- What evidence would change the research priority?

The host agent supplies web search, browsing or filing access. This repository supplies the method and reference material, not a real-time data service or market-data account.

## Try it

```text
Use serenity-skill to research A-share AI semiconductors.
Compare the relevant supply-chain layers before ranking company research priorities.
Explain commercial progress, earnings, valuation pressure and the strongest counterargument.
Link material claims to dated original sources. Return fewer candidates if evidence is insufficient.
```

```text
Use serenity-skill to challenge the claim that [company/ticker] is a core CPO supplier.
Separate its product role, delivery status, ecosystem partners, direct customers,
attributable revenue and competing suppliers. Explain what is established and what is still unknown.
```

```text
Teach me the Serenity-inspired supply-chain method, one focused question at a time.
```

More starting questions are in the [prompt pack](assets/research-prompt-pack.md).

## Worked cases

- [A-share AI semiconductor scan](examples/a-share-ai-semiconductor-demo.md): five-company initial comparison with three research priorities.
- [TFC CPO company challenge](examples/cpo-company-challenge.md): what production, customer and financial evidence actually supports.
- [Learning conversation](examples/demo-conversation.md): a fictional teaching example.

The first two cases are in Chinese and use public materials checked as of September 14, 2026. They include financial periods, source links and unresolved questions. They are archived research examples, not continuously updated market recommendations.

## Installation

You need an Agent Skills-compatible host with its own search, browser or filing tools for current research. Research does not require Python. The optional maintainer structure check requires Python 3.

First obtain the repository:

```bash
git clone https://github.com/muxuuu/serenity-skill.git
cd serenity-skill
```

Alternatively, download and extract the repository ZIP, then open a terminal in the folder containing `SKILL.md`. Run the following commands from that folder.

### Codex

User-level installation:

```bash
SERENITY_DIR="$HOME/.agents/skills/serenity-skill"
mkdir -p "$SERENITY_DIR"
cp -R SKILL.md LICENSE references assets examples agents "$SERENITY_DIR"/
```

Invoke in Codex:

```text
$serenity-skill Research this investment theme with dated evidence and counterarguments.
```

### Claude Code

User-level installation:

```bash
SERENITY_DIR="$HOME/.claude/skills/serenity-skill"
mkdir -p "$SERENITY_DIR"
cp -R SKILL.md LICENSE references assets examples agents "$SERENITY_DIR"/
```

Invoke in Claude Code:

```text
/serenity-skill Challenge this company's CPO supplier thesis.
```

For project-only use, change `SERENITY_DIR` to the absolute destination path:

| Client | Directory inside the target project |
|---|---|
| Codex | `<project path>/.agents/skills/serenity-skill` |
| Claude Code | `<project path>/.claude/skills/serenity-skill` |

Start a new session after installation and confirm the skill is available. See the [Codex documentation](https://developers.openai.com/codex/skills) and [Claude Code documentation](https://code.claude.com/docs/en/skills). Other compatible clients use the same skill; consult their documentation for discovery paths and available research tools.

Verification scope, September 14, 2026: Codex CLI 0.147.0 loaded the revised skill and completed an offline company-claim exercise. The Claude Code directory and package structure were checked, but model invocation has not been verified. This is not an end-to-end validation of every client, model or live data source.

For an upgrade, first move the old installed `serenity-skill` directory outside the host's skill search paths as a backup, then copy the new package. Copying over an existing version leaves retired files behind; leaving a backup inside a skill search path can also load a duplicate. Repository READMEs, maintenance documents and `scripts/validate_skill.py` are not needed in the runtime directory.

## Research memo and local check

Use the [memo template](assets/thesis-template.md) for a structured report, translating its Chinese labels when needed. It covers business position, evidence, gaps, earnings, valuation, alternatives and conditions that would change the view. Explain research priorities in words rather than a composite numerical score.

From the repository folder:

```bash
python3 scripts/validate_skill.py .
```

This checks the skill name, description and directory, not investment conclusions.

## Repository layout

```text
serenity-skill/
├── SKILL.md
├── README.md
├── README.en.md
├── LICENSE
├── agents/openai.yaml
├── references/
├── assets/
│   ├── research-prompt-pack.md
│   └── thesis-template.md
├── scripts/validate_skill.py
├── examples/
│   ├── a-share-ai-semiconductor-demo.md
│   ├── cpo-company-challenge.md
│   └── demo-conversation.md
└── evals/test-cases.md
```

## Research boundary

This is an independent interpretation of public research material, with no official affiliation or endorsement. [Method sources](references/public-profile-and-evaluation.md) distinguish the inspiration from this project's own workflow.

The Skill provides research priorities, evidence, risks and next checks. It does not execute trades or operate accounts. Final investment decisions remain with the user. Company statements, technical evidence and financial data should support the particular claims being made.

## License

MIT
