<div align="center">

# Serenity.skill

### 让 Agent 用 Serenity 式投研方法，筛出上涨逻辑更清楚的股票和基金方向

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
  <a href="SKILL.md"><img src="https://img.shields.io/badge/Agent%20Skill-SKILL.md-black" alt="Agent Skill"></a>
  <a href="README.md"><img src="https://img.shields.io/badge/README-%E4%B8%AD%E6%96%87-red" alt="中文"></a>
  <a href="README.en.md"><img src="https://img.shields.io/badge/English-README.en.md-lightgrey" alt="English"></a>
</p>

<p align="center">
  <a href="https://github.com/muxuuu/serenity-skill/stargazers"><img src="https://img.shields.io/github/stars/muxuuu/serenity-skill?logo=github" alt="GitHub Stars"></a>
  <a href="https://github.com/muxuuu/serenity-skill/forks"><img src="https://img.shields.io/github/forks/muxuuu/serenity-skill?logo=github" alt="GitHub Forks"></a>
  <a href="https://skills.sh/muxuuu/serenity-skill"><img src="https://skills.sh/b/muxuuu/serenity-skill" alt="skills.sh installs"></a>
  <a href="https://olud.ai/project/muxuuu-serenity-skill.html"><img src="https://olud.ai/badge.php?tool=muxuuu-serenity-skill" alt="serenity-skill 在 olud.ai 的目录徽章"></a>
</p>

<p align="center"><a href="https://trendshift.io/repositories/47219"><img src="https://trendshift.io/api/badge/trendshift/repositories/47219/daily" alt="TrendShift 全语言日榜第 22 名" width="250" height="55"></a></p>

</div>

看到 AI 半导体、机器人、CPO、算力、电力设备、创新药这些热点，很多人能感受到热度，却很难判断该看哪条产业链、哪类公司、哪只股票、哪个基金方向。

Serenity.skill 把 [Serenity / @aleabitoreddit](https://x.com/aleabitoreddit) 公开内容中可观察到的投研路径做成 Agent Skill。它会从热点出发，拆产业链，找供应链瓶颈，筛候选公司和基金方向，再检查公告、财报、客户、产能和风险，最后整理成一份优先研究清单。

它的工作方式很简单：先把热点拆开，看真实需求在哪里，再看哪个环节更难扩产、更难替代，最后回到股票和基金方向，判断哪些线索更值得继续深挖。

它适合面对热点信息流、希望建立系统筛选流程的投资者：让 AI 先完成第一轮深度研究，把模糊热度变成有逻辑、有证据、有风险边界的研究方向。

> Research support only. Serenity.skill 负责研究、排序和推理；最终买卖决策由你自己决定。

## 为什么是 Serenity 式方法

[Serenity / @aleabitoreddit](https://x.com/aleabitoreddit) 在公开内容中长期围绕 AI、半导体、光通信、机器人等科技主题做供应链研究。他的核心思路很清楚：大行情里真正有价值的机会，常常藏在系统扩张时最难绕开的关键环节。

Serenity.skill 复用的是这套公开方法论中的研究路径：

- 从大热点开始，先看真实需求来自哪里。
- 把主题拆成下游需求、系统集成、芯片/器件、设备、材料、封测、基础设施。
- 找低供应商数量、长验证周期、扩产困难、客户认证严格、材料纯度要求高的环节。
- 再回到股票和基金方向，判断谁更靠近真实瓶颈，谁主要只是蹭主题。
- 最后检查公告、财报、问询函、订单、产能、客户和风险，给出优先研究排序。

这个仓库做的是公开资料研究工具。它吸收 Serenity 式研究的结构化思路，同时要求所有公司判断回到公告、交易所文件、财报、电话会、监管/项目文件、专利、标准、可信媒体和专业分析。

## 它能帮你做什么

| 你现在遇到的问题 | 可以这样问 AI | Serenity.skill 会帮你看什么 |
|---|---|---|
| 刷到一个热点，感觉全网都在说，自己不知道从哪下手 | `最近 AI 半导体很火，普通人应该先研究哪些方向？` | 先拆产业链，再把更接近真实需求和扩产瓶颈的方向排出来 |
| 想买机器人方向，分不清整机、零部件、减速器、传感器谁更关键 | `机器人产业链里，哪些环节更可能先出机会？` | 比较不同环节的供需紧张度、竞争格局和证据强弱 |
| 看到别人推荐一只股票，担心它只是蹭热点 | `帮我挑战这家公司是不是 CPO 核心供应商` | 查它在产业链里的真实位置、客户证据、收入质量和主要风险 |
| 想买主题基金或 ETF，分不清哪个细分方向更值得看 | `机器人主题基金应该重点看哪些上游环节？` | 找基金背后的核心受益链条，提示需要核验的持仓方向 |
| 手里有几只候选股，想让 AI 帮你排个研究顺序 | `比较 A、B、C 三家公司，谁的上涨逻辑更清楚？` | 按产业链位置、证据强度、估值压力、风险点做优先级排序 |
| 每天刷消息很焦虑，想建立一套固定筛选流程 | `带我学 Serenity 式产业链研究，每次只问我一个问题` | 从热点、需求、卡点、证据、风险一步步建立研究框架 |

## 直接复制这个 Prompt

```text
用 serenity-skill 深度调研现在 A 股 AI 半导体产业链。
请联网查公告、财报、问询函、互动易、招投标、环评/能评、专利、客户认证和财务质量，
先排产业链层级，再给出通常 3–5 个值得优先研究的标的；证据不足时可以少给，
并说明卡住的环节、产业链位置、证据、排序理由和主要风险。
```

```text
用 serenity-skill 帮我研究最近机器人方向。
先拆产业链，再判断哪些环节更接近真实供需瓶颈，
最后给出股票和基金方向的优先研究清单。
```

```text
用 serenity-skill 挑战 [公司/股票代码]。
它到底卡在哪一层？证据够不够？市场可能高估了什么？
什么情况说明这个判断应该降级？
```

更多可复制模板见 [assets/research-prompt-pack.md](assets/research-prompt-pack.md)。

## 输出长什么样

```text
我会先看 [方向 A]，再看 [方向 B] 和 [方向 C]。

如果你想找股票线索，我会优先研究这几家公司：

1. [公司 A]：最接近 [关键瓶颈环节]，上涨逻辑来自 [需求增长/产能紧张/客户验证/国产替代]。
2. [公司 B]：处在 [产业链位置]，适合跟踪 [订单/毛利率/产能利用率]。
3. [公司 C]：弹性更大，但需要确认 [核心风险或缺失证据]。

如果你更想买基金或 ETF，我会先看暴露在 [细分方向 A] 和 [细分方向 B] 的产品，
再检查它们的前十大持仓里有没有 [公司 A]、[公司 B] 这类真正靠近瓶颈的公司。

我会暂时降低 [热门方向 X] 的优先级，因为它的故事很热，但现在还缺 [订单证据/利润兑现/客户认证]。

下一步先查三件事：
1. [公司 A] 最新财报里 [关键业务] 的收入和毛利率有没有变化。
2. [公司 B] 有没有新的客户认证、订单或扩产公告。
3. [相关基金/ETF] 的持仓是不是集中在真正受益的环节。
```

完整示例：

- [A 股 AI 半导体初筛：五家公司，三条优先研究线索](examples/a-share-ai-semiconductor-demo.md)
- [天孚通信 CPO 挑战：量产、客户与利润分别证明到哪一步](examples/cpo-company-challenge.md)
- [研究方法教学对话（虚构示例）](examples/demo-conversation.md)

前两篇是截至 2026-09-14 的真实公开资料研究，含来源、财务期间和未完成的核验项，供查看方法如何使用；不作为持续更新的行情或买入清单。

## 安装

需要一个能读取 Skill 文件的 Agent 客户端，以及它自己的联网搜索、浏览器或公告数据工具。Serenity.skill 提供研究方法，不附带实时行情服务或数据账号。研究本身不依赖 Python；下方维护用结构检查需要 Python 3。

先取得仓库并进入目录：

```bash
git clone https://github.com/muxuuu/serenity-skill.git
cd serenity-skill
```

也可以下载仓库 ZIP、解压后，在终端进入其中包含 `SKILL.md` 的目录。以下命令均从这个目录执行。

### Codex

用户级安装：

```bash
SERENITY_DIR="$HOME/.agents/skills/serenity-skill"
mkdir -p "$SERENITY_DIR"
cp -R SKILL.md LICENSE references assets examples agents "$SERENITY_DIR"/
```

在 Codex 中调用：

```text
$serenity-skill 研究现在 A 股 AI 半导体产业链，说明优先研究方向、证据和反方理由。
```

### Claude Code

用户级安装：

```bash
SERENITY_DIR="$HOME/.claude/skills/serenity-skill"
mkdir -p "$SERENITY_DIR"
cp -R SKILL.md LICENSE references assets examples agents "$SERENITY_DIR"/
```

在 Claude Code 中调用：

```text
/serenity-skill 挑战天孚通信是 CPO 核心供应商的说法，逐项核对原始披露。
```

只希望在某个项目使用时，把上述 `SERENITY_DIR` 改为目标项目的绝对路径：

| 客户端 | 项目内目录 |
|---|---|
| Codex | `<项目路径>/.agents/skills/serenity-skill` |
| Claude Code | `<项目路径>/.claude/skills/serenity-skill` |

安装后新开一个会话，确认能找到并调用 `serenity-skill`。目录规则见 [Codex 官方文档](https://developers.openai.com/codex/skills)和 [Claude Code 官方文档](https://code.claude.com/docs/en/skills)。其他兼容客户端使用同一份 Skill，安装位置和联网工具以各客户端文档为准。

验证范围（2026-09-14）：Codex CLI 0.147.0 已实际加载新版，并完成离线材料下的公司主张辨析；Claude Code 的目录与包结构已核对，模型调用尚未实测。这不代表所有客户端、模型和联网数据源已经完成端到端验证。

已有旧版本时，先把旧 `serenity-skill` 安装目录移到 Skill 搜索目录以外备份，再复制新版。直接覆盖不会移除旧版已退役的文件；在同一搜索目录留着旧副本还可能重复加载。仓库内的 README、维护文档和 `scripts/validate_skill.py` 不需要复制到运行目录。

## 研究备忘录

需要完整报告时，可以让 Agent 使用 [研究模板](assets/thesis-template.md)，整理产业链位置、已确认事实、缺失证据、利润与估值、替代路线和失效条件。研究优先级由证据和推理解释，不使用综合数字评分。

维护者可在仓库目录检查 Skill 的基本结构：

```bash
python3 scripts/validate_skill.py .
```

这条命令检查名称、描述和目录，不验证投资结论。

## 仓库结构

```text
serenity-skill/
├── SKILL.md
├── README.md
├── README.en.md
├── references/
│   ├── deep-research-workflow.md
│   ├── evidence-ladder.md
│   ├── market-source-playbook.md
│   ├── public-profile-and-evaluation.md
│   └── risk-and-compliance.md
├── assets/
│   ├── research-prompt-pack.md
│   └── thesis-template.md
├── scripts/
│   └── validate_skill.py
├── examples/
│   ├── a-share-ai-semiconductor-demo.md
│   ├── cpo-company-challenge.md
│   └── demo-conversation.md
└── evals/
    └── test-cases.md
```

## 研究边界

Serenity.skill 是独立的公开方法论项目，灵感来自 [Serenity / @aleabitoreddit](https://x.com/aleabitoreddit) 公开内容中可观察到的研究范式。它帮助做研究、排序和推理，功能范围限于研究辅助。

它提供研究优先级、证据链、风险核验和下一步检查清单。交易执行、账户操作、收益承诺和最终买卖判断始终由用户自己控制。

强结论应以公告、交易所文件、财报、电话会、监管/项目文件、专利、标准、可信媒体和专业分析为依据。社交媒体内容适合作为线索来源，最终判断要回到更强证据。

## License

MIT
