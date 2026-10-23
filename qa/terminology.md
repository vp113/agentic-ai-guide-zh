# 中文版术语约定

本文件记录中文版的术语选择，供后续翻译、同步上游和审校时参照。它不是要求全文机械替换的词表；修改时仍需结合上下文，并保持同一章节内的用法一致。

## 总原则

1. **公认中文译名用中文**：已有稳定、通行中文译名的概念，使用中文，例如“多智能体”“上下文”“提示工程”“延迟”“工作流”。
2. **专有名词、无稳定译名或易歧义的术语保留英文**：例如 `Transformer`、`Token`、`Agent`、`harness`、`schema`、`MCP`、`A2A`；`Prompt` 作为对象/构件时也保留英文。
3. **首次出现给全称**：不常见缩写首次出现时写作“中文（English Full Name, ABBR）”，例如“组相对策略优化（Group Relative Policy Optimization, GRPO）”。
4. **不译代码实体**：`\label`、`\ref`、`\cite`、URL、代码标识符、数学环境中的变量名不翻译；代码内 `#` 注释可译。
5. **不做盲目全文替换**：同一英文词在不同章节可能已形成不同的中文/英文习惯（见下文“章节内一致性”），只统一同一概念在同一语境中的混用形式。

## 保留英文的核心术语

以下术语按项目既有约定保留英文，中文可作为首次出现的解释性括注，但正文不强制改用中文：

| 术语 | 说明 |
|---|---|
| `Agent` | 核心术语；中文“智能体”用于“智能体 AI”、章标题和既有复合词 |
| `Transformer`、`Token`、`Attention`、`Embedding` | 通用架构/模型术语；各章按既有习惯使用英文或中文，见“章节内一致性” |
| `Policy`、`Reward` | 强化学习术语；中文“策略”“奖励”用于“策略梯度”“奖励模型”等固定复合词 |
| `Prompt` | 作为对象/构件（`System Prompt`、`Prompt 模板`、`Prompt 链`、`Prompt 缓存`）保留英文 |
| `harness`、`schema` | 运行时/数据结构术语，保留英文 |
| `MCP`、`A2A`、`RAG`、`CoT`、`RLHF`、`PPO`、`GRPO` | 协议、方法或缩写；首次出现给全称 |

## 统一使用的中文术语

| 概念 | 采用写法 | 避免/说明 |
|---|---|---|
| multi-agent | 多智能体 | 避免“多 Agent”；与第 26 章标题《多智能体系统》一致 |
| single-agent | 单智能体 | 避免“单 Agent” |
| context / context window | 上下文 / 上下文窗口 | `Model Context Protocol`、`Context Relevancy` 等专名与指标名除外 |
| prompt engineering | 提示工程 | 避免“Prompt 工程” |
| prompt injection | 提示注入 | 避免“Prompt 注入”“prompt injection”；攻击语境专用 |
| hint injection | 注入提示（Hint Injection） | 与安全术语“提示注入”区分；见第 6 部分循环工程清单 |
| system prompt | `System Prompt` | 避免“系统提示”“系统 Prompt”“系统 prompt”；代码/公式/引文中的小写原样保留 |
| prompt template / chain / cache | `Prompt 模板` / `Prompt 链` / `Prompt 缓存` | 避免“提示模板/链/缓存” |
| human-in-the-loop | 人机协同 | 避免“人在回路”；首次出现可括注 `Human-in-the-Loop` |
| approval gate | 审批门控 | “审批”指流程/门控，“批准”指具体动作，二者可并存 |
| workflow | 工作流 | 正文避免 `Workflow`；`Graph Workflow` 等模式名、代码标识符除外 |
| latency | 延迟 | 避免“时延” |
| throughput | 吞吐量 | 名词用“吞吐量”；“高吞吐”“吞吐能力”等定语可保留“吞吐” |
| evaluation | 评估 | 系统化基准测试/评测套件语境可用“评测”；同一段落内保持一致 |
| agentic UI | `Agentic UI` | 第 28 章标题与正文统一；避免“Agent 化 UI” |
| agentic RAG | 智能体 RAG | 与第 16 章一致；避免“Agent 化 RAG” |
| sandbox / guardrail / orchestration | 沙箱 / 护栏 / 编排 | — |
| memory / planning / reflection / trajectory | 记忆 / 规划 / 反思 / 轨迹 | — |
| router / chunk / vector | 路由 / 分块 / 向量 | 代码标识符（`router`、`chunk`）不译 |
| quantization / distillation / pruning | 量化 / 蒸馏 / 剪枝 | — |

## 章节内一致性

`Attention`、`Embedding`、`Policy`、`Reward`、`Prompt` 等术语在全书并非逐字统一：第 1 章大量使用“注意力”“嵌入”“策略”“奖励”，第 2、5、6 章的部分小节则保留英文。这是既有译文的风格，本轮不做跨章强制统一。处理原则是：

- 在同一章、同一节或同一段内，不混用同一概念的中英文形式；
- 首次出现可用“中文（English）”括注，之后沿用该章节的主导形式；
- 新增译文优先沿用所在章节的既有写法，而不是引入第三种译法。

## 歧义与例外

- **`Context`**：正文概念统一为“上下文”；`Model Context Protocol`、`Context Relevancy`、`Context-Free Grammar`、`In-Context Learning`、`Context rot` 括注、代码与指标名保留英文。首次出现的中文括注（如“上下文窗口（context window）”“短期（context window）”）可保留英文。
- **`System Prompt`**：正文与表格统一为 `System Prompt`；代码注释/字符串、数学 `\text{system prompt}`、以及作为攻击示例引用的原句保留小写 `system prompt`。
- **`Prompt`**：对象/构件保留英文；已成词的“提示工程”“提示注入”用中文；“提示”作动词（hint/prompt）时保留中文。
- **`Agentic`**：`Agentic AI`、`Agentic UI` 作为术语保留英文；一般形容词用“智能体模式/工作流/场景/系统”，不再写“Agent 化”或“Agentic 模式”。
- **原文类别标签/引文**：直接引用英文原文的类别名（如 Anthropic 的 `Workflows`）或首现括注（如 `Human in the Loop`）可保留原形，不强制改写。
- **“审批”与“批准”**：`审批门控`、`审批流程` 用“审批”；“用户批准/拒绝”“等待批准”用“批准”。
- **“评估”与“评测”**：一般评估用“评估”；基准测试、评测套件、评测框架可用“评测”，但避免在同一段内来回切换。

## 本轮修改记录（2026-10-23）

- `多 Agent` / `单 Agent` → `多智能体` / `单智能体`（第 5、6 部分及代码注释/图表标题）。
- 第 18 章 `Context` / `Context Window` → `上下文` / `上下文窗口`；保留 `Model Context Protocol` 等专名。
- `Prompt 工程` → `提示工程`；`Prompt 注入` / `prompt injection` → `提示注入`。
- `系统提示` / `系统 Prompt` / 正文中的 `system prompt` / `System prompt` → `System Prompt`（代码、公式与引文中的小写原样保留）；`System 消息` → `系统消息`。
- `提示模板/链/缓存` → `Prompt 模板/链/缓存`。
- `Agent 化 UI` → `Agentic UI`；`Agent 化 RAG` → `智能体 RAG`；其余 `Agent 化` → `智能体`。
- `时延` → `延迟`（只替换独立词形；见下节“替换操作注意事项”）；`人在回路` → `人机协同`；第 18 章正文 `Workflow` → `工作流`。
- 第 6 部分“提示注入”（hint injection）改为“注入提示（Hint Injection）”，消除与安全术语的歧义。

## 替换操作注意事项

- **禁止无边界短词替换**：`时延` 本身是 `同时延迟` 的子串。若对 `时延` 做全局替换，会把“同时延迟”改成“同延迟迟”；第五轮曾出现该回归。应匹配独立词形（如“首 Token 时延”）或先加边界，替换后搜索 `延迟迟`、`同延迟` 复查。
- **英文术语加词边界**：替换 `Agent`、`Prompt` 等短词时避免命中 `Agentic`、`Agents`、`Promptflow` 等更长词。
- **替换后检查 diff**：扫描重复字、中文间空格、跨词断句与异常标点，并核对受影响 PDF 页面。
