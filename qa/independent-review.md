# 中文版 PDF 独立验收报告（第七轮·发布验收）

- 审查对象：`update-latest-zh` 分支，HEAD `f33ae2e`（`build(zh): fix layout orphans and localize structural labels`）
- 上轮审查：HEAD `97f9430`（第六轮，增量通过，剩余 3 项 P3）
- 验收日期：2026-10-23
- 英文基准：arXiv `2606.24937v3`（Version 1.4，2026-09-29）
- 构建产物：`agentic-ai-guide-zh.pdf`，**679 页**，9,927,219 字节，MD5 `62c84f0cf987a1a2f369bc2254fee88d`；生成于 2026-10-23 19:22:08（+08）；源码最后修改 19:17:08，提交 19:25:13
- 审查范围：仅复核 `f33ae2e` 的排版、结构标签与构建增量（7 个文件，+114/−15）；不重复已通过的翻译与 12 项技术勘误检查
- 审查方式：只读源码、PDF、日志与 CI 页面。为验证 680→679 页重排，另在临时目录重建父提交 `97f9430`（680 页）做逐句内容比对；未修改工作区源码、PDF 或 Git

## 验收结论

**PDF 本体通过发布验收。** 三项排版修复（p110 标题/表格分离、原 p595 大块空白、28.5 孤行标题）均已在 PDF 中确认生效；680→679 页重排未造成正文、图表、目录条目或参考文献缺失；中文结构标签、目录、书签、图表编号与交叉引用整体正确；CI run `39945963089` 为 success。未发现新的 P0/P1/P2 级 PDF 缺陷。

仓库层面仍有若干非阻塞项，其中 **README 页数仍写 680（P2，文档，非 PDF）**，建议合并/发布前修正；另有 6 项 P3 与 4 项 P4 维护项，详见第七节。

| 验收维度 | 结论 | 依据 |
|---|---|---|
| p110 小节标题与表 1.19 分离 | 通过 | 父版 p110 以 `1.15.2 方法对比` 结束、表在 p111；新版 p110 标题与完整表 1.19 同页，p111 从 1.15.3 开始 |
| 原 p595 的 flushbottom 大块空白 | 通过 | 父版 p595 Q19/Q20 之间约 116 pt（80 dpi 下 129 px）拉伸空白；新版 p594 Q19/Q20 紧接，Q21 起于 p595；`Underfull \vbox ... \output` 70→0 |
| 第 28 章 28.5 孤行标题 | 通过 | 父版 p568 页底仅 `28.5 生成式 UI`；新版 p568 标题后接正文与 28.5.1 |
| 其他孤行、空白、浮动体 | 通过 | 679 页逐页墨迹扫描，无新的页中大片空白；页底空白分布与父版基本一致；仅 p217 为纯浮动体页（父版 p218，既有） |
| 中文结构标签、目录、书签 | 通过（2 项 P3） | 目录/部分/章/图/表/代码清单/附录/参考文献均为中文；1558 条 `.toc` 锚点（页面显示 1144 条）、1144 条书签、2671 个链接均有效 |
| 图表编号与交叉引用 | 通过（2 项 P3） | 76 图 / 114 表 / 82 代码清单，编号集合与父版完全一致；[1]–[460] 连续；0 undefined |
| 680→679 页内容完整性 | 通过 | 父版重建恰为 680 页；目录锚点、图表编号集合、参考文献集合完全一致；正文逐句比对仅 9 处差异，均可解释 |
| CI 工作流与构建结果 | 通过（1 warning + 1 notice） | run #1，push `update-latest-zh` @ `f33ae2e`，success，build 3m3s；产物 8.62 MB |
| PDF 与构建日志 | 通过 | 0 undefined / 0 multiply defined / 0 Missing character；overfull 仅既有 2 处；字体 54 个全部嵌入 |
| 文档纳入 Git | 有条件通过 | `qa/independent-review.md` 本轮更新后适合入库；`CLAUDE.md` 需先修正 3 处事实错误；README 页数需改 |

---

## 一、排版修复复核（通过）

### 1. p110：1.15.2 标题与表 1.19（通过）

- 父提交 `97f9430` 的 p110 最后一个正文行是 `1.15.2 方法对比`；表 1.19 作为浮动体落到 p111，形成“标题在页底、表格在下一页”的孤行。
- 新版 p110 同页呈现 `1.15.2 方法对比`、表题 `表 1.19: 现代推理引擎支持的投机解码方法。` 与全部 7 行表体（标准方案、Medusa、Eagle、Eagle-2、N-gram Lookup、Lookahead、多 token 预测）；p111 直接以 `1.15.3 Medusa 多头推测解码` 开始。
- 实现为 `contents/part1.tex:4148` 的 `\Needspace{12\baselineskip}` + `contents/part1.tex:4152` 的 `\begin{table}[H]` + `\footnotesize`。表格未超出页面，未产生新的 overfull；字号虽降为 `\footnotesize`，正文与表体仍清晰可读。
- **残留风险（P4）**：`[H]` 表格不可跨页，若未来增删该表行或改用更宽字体，存在溢出风险；修改附近内容后应复查 p110。另需注意，表 1.19 由 `\small` 降为 `\footnotesize`（11pt 文档中约 10pt→9pt），是为同页容纳标题与表格所做的可读性取舍；当前印刷清晰，若后续要求更大字号，应改为可跨页长表或重新排版。

### 2. 原 p595：Q19/Q20 之间的拉伸空白（通过）

- 父版 p595 中，Q19 与 Q20 两个 `questionbox` 之间出现约 116 pt（80 dpi 渲染下 129 px）的页中空白：`\flushbottom` 把两盒之间唯一的可伸缩胶水拉满整页。
- 新版（因前文重排整体前移一页）p594 中 Q19/Q20 紧接排列，空白只保留在页面底部，Q21 从 p595 开始。视觉复核确认页中不再有异常胶水间隙。
- 量化佐证：父版日志有 70 条 `Underfull \vbox (badness ...) has occurred while \output is active`，新版为 **0**；总 underfull 由 140 条降至 70 条（其余 70 条 `Underfull \hbox` 总数一致，仅 `5614–5617` 一带的合并/拆分方式略有差异）。
- 页底剩余留白约 65 px（40 dpi 渲染，约页面高度 14%），是 Q21 大盒不可拆分导致的自然留白，不是拉伸空白。

### 3. 第 28 章 28.5「生成式 UI」孤行（通过）

- 父版 p568 的最后一个正文行正是 `28.5 生成式 UI`，标题下无正文。
- 新版 p568 中，`28.5 生成式 UI` 位于页面上部（第 9 个文本行），随后是“生成式 UI 概念”框、引言段与 `28.5.1 用 React Server Components 构建动态界面`；表 28.1 位于 p568 顶部，与正文衔接正常。
- `contents/part5.tex:16933` 的 `\Needspace{12\baselineskip}` 生效。

### 4. 全书孤行、空白与浮动体扫描（通过）

- 对 679 页以 40 dpi 逐页渲染并统计墨迹行：
  - 页中最大内部空白为 37 px（标题页除外）；未发现新的页中大块空白。父版 p595 的异常已消除。
  - 页底留白 > 80 px 的页面：父版 60 页，新版 61 页；> 100 px：均为 53 页。最大留白页分两类：p339、p185、p115、p156、p130、p644 等为章末页，p673 为参考文献末页；p629、p366、p71、p69 等为源码中显式 `\newpage` 另起小节（如 `part6.tex:3869`、`part5.tex:3670`、`part1.tex:1413`、`part1.tex:1333`），属既有分页设计。两类留白在父版中同样存在（>100 px 页数两版均为 53），不是本轮回归。
  - 平均页底留白由 22.9 px 增至 28.7 px（40 dpi，约 1.7% 页高），与全局 `\raggedbottom` 的预期一致，未造成新的显著空洞。
- 标题位于页底的候选页逐页检查（p55、p140、p170、p230、p341、p369、p372、p375、p378、p403、p423、p452、p520、p544、p563、p567）：标题后均至少有一行正文，未发现真正的孤行。p567 的 `28.4.7 框架对比` 仅带一行正文、表格在下一页，属临界但可接受。
- p217 为 `Text page 217 contains only floats`，页面由图 11.5/11.6 完整占满；父版对应 p218，属既有行为，不是新问题。

---

## 二、中文结构标签、目录、书签、编号与交叉引用

### 1. 结构标签（通过）

已在渲染页逐项核对：

| 标签 | 位置 | 结果 |
|---|---|---|
| 目录 | p3 | `目录` |
| 部分 | p48 | `第 I 部分` + `基础`；目录中为 `第 I 部分 基础` |
| 章 | p560 | `第 28 章` + `Agentic UI 框架` |
| 图 | p217 | `图 11.5:`、`图 11.6:` |
| 表 | p568 | `表 28.1:` |
| 代码清单 | p570 | `代码清单 28.3:` |
| 附录 | p674 | `附录 A` + `数学基础` |
| 参考文献 | p645 | `参考文献` |

- `book.tex:230–280` 的 `\contentsname`、`\figurename`、`\tablename`、`\appendixname`、`\bibname`、`\lstlistingname` 与 `\chapterlabel` 均已生效；`\@part`/`\@makechapterhead` 的本地化重定义未破坏 hyperref 书签或目录链接。
- 正文中的硬编码 `Chapter~\ref`、`Table~\ref` 已改为 `第~\ref~章`、`表~\ref`；PDF p329 的 `表 16.2`、p334 的 `表 16.5` 等已确认。

### 2. 目录与书签（通过，附 2 项 P3）

- `.toc` 源共 1558 条，锚点集合与父版**完全一致**（1558/1558），级别分布一致：part 6、chapter 39、section 324、subsection 775、subsubsection 13、paragraph 401；页面实际显示到 subsection 级，共 1144 条。
- 1558 个 `.toc` 锚点均有同名命名目标且页号一致；另有一处 `lstnumber.-77.15` 的页号差异，但它是 listings 行号锚点、不是目录条目，不影响目录。
- 全书 1144 条书签，层级为 −1/0/1/2（6/39/324/775）；书签标题均为中文，未发现 `Chapter`/`Figure`/`Table`/`Appendix`/`Bibliography` 等英文结构词。
- 2671 个链接注解，0 个缺少 `/Dest` 或 `/A` 目标；目录、GAS 关联框与正文交叉链接均可达。
- **P3-1（既有）**：目录中 5 字符章节号（如 p9 的 `11.10网络拓扑与通信模式`、`11.11训练吞吐…`、`11.12成本分析…`，p25 的 `29.10`–`29.32`、`30.10`–`30.23`）与标题之间没有空隙。父版同样如此，非本轮回归；可在 `\l@section` 的目录编号盒宽度上统一修正。
- **P3-2（既有风格）**：目录章条目仍为 `1 LLM 架构与优化方法`、书签章标题仅 `LLM 架构与优化方法`（不含 `第 1 章`），而章页与部分页已中文化；附录目录条目为 `A 数学基础`。这与英文版数字式目录一致，不影响可读性；若追求完全统一，可在 `\@chapter` 的 `\addcontentsline`/书签中加 `第 N 章`。

### 3. 图表编号与交叉引用（通过）

- 图 76 个、表 114 个、代码清单 82 个；新旧 PDF 的编号集合完全相同，无重复、无缺号。
- 图表题注前缀已分别变为 `图`、`表`、`代码清单`，编号主体未变。
- 参考文献 [1]–[460] 连续，无缺号、无重复，共 460 条。
- 构建日志 0 条 undefined citation/reference、0 条 multiply defined。

### 4. 仍为英文的结构引用（P3）

正文仍有 7 处英文结构引用（`Section`/`Listing`），均为硬编码而非 `\ref` 生成：

| PDF 页 | 源码 | 文本 |
|---|---|---|
| p129 | `contents/part1.tex:5303` | `（参见 Section~\ref{sec:constrained-decoding}）` |
| p191 | `contents/part2.tex:3170` | `它在 Section~\ref{sec:simpo} 与…` |
| p317 | `contents/part5.tex:266` | `（参见 Section~\ref{sec:chunking}）` |
| p327 | `contents/part5.tex:999` | `智能体 RAG（Section~\ref{sec:agentic_rag}）…` |
| p336 | `contents/part5.tex:1655` | `（Section~\ref{sec:agentic_rag}）` 与 `Listing~\ref{lst:async_retrieve}` |
| p337 | `contents/part5.tex:1718` | `Listing~\ref{lst:incremental_index}` |

建议统一为 `第~\ref~节`、`代码清单~\ref`。这是本轮标签本地化的遗漏，不影响链接与编号，列为 P3。

---

## 三、680→679 页重排的内容完整性（通过）

1. 在临时目录用同一套 XeLaTeX/BibTeX 序列重建父提交 `97f9430`，得到 **680 页**，与此前报告一致；新版为 **679 页**，页数变化来自排版而非内容删减。
2. 目录锚点集合 1558/1558 完全一致；图表/代码清单编号集合（76/114/82）完全一致；参考文献 [1]–[460] 完全一致。
3. 将两版正文按阅读顺序拼接，去掉页眉、页码与结构标签后逐句比对（句子长度 ≥20 字）：
   - 旧版 8658 句中仅 9 句在新版中找不到逐字匹配；新版 8657 句中同样仅 9 句在旧版中找不到匹配。
   - 9 个差异片段可归为以下几类：`System 消息 → 系统消息`（有意修正）；`Table 16.2 → 表 16.2`、`Table 16.5 → 表 16.5`、`Table A.1 → 表 A.1`、`Bibliography → 参考文献`（标签本地化）；1.15.2 表 1.19 与 28.5/表 28.1 的浮动体顺序及表行顺序变化；`AllGather/ReduceScatter` 的断行差异。
   - 归一化正文长度 784,099→784,076 字符（−23），与标签缩短量相符。
4. 结论：**没有段落、章节、图表、题注或参考文献条目在 680→679 页重排中丢失。**

---

## 四、CI 工作流与 GitHub Actions 结果（通过）

### 1. 工作流改动

`.github/workflows/build.yml` 的改动均已核对：

- TeX Live 镜像由 `texlive/texlive:latest` 固定为 `texlive/texlive:TL2025-historic`（注释说明如需字节级复现可再固定 digest）。
- 安装 `make`，并在编译前用 `fc-list` 校验 Noto Serif/Sans CJK SC。
- `make dist` 后新增产物与日志校验：PDF 非空、`book.log` 非空、`Citation/Reference ... undefined` 与 `Missing character` 不得出现。
- push 触发分支加入 `update-latest-zh`；release job 仍仅在 `v*` 标签触发。
- `Makefile` 的 `-bibtex` 改为 `bibtex`，并在 `.blg` 出现 `There was/were N error` 时失败；不再静默忽略 BibTeX 错误。

### 2. Run `39945963089`

通过 GitHub Actions 运行页核实（`https://github.com/vp113/agentic-ai-guide-zh/actions/runs/39945963089`）：

- Workflow：`Build Book`，run #1，event `push`，branch `update-latest-zh`，head SHA `f33ae2e`。
- 状态：**Success**；总时长 3m 7s，其中 build job 3m 3s；release job 0s（非标签触发，按预期跳过）。
- 产物：`agentic-ai-guide-zh-pdf`，8.62 MB，SHA-256 `90b7a6654cd0f97c094f0144c0f9d8ca93204189f3bb9d2d8cd3649b76630ac4`。
- 非阻塞告警：1 条 warning（`actions/checkout@v4`、`actions/upload-artifact@v4` 仍以 Node.js 20 为目标，被强制在 Node.js 24 上运行）与 1 条 notice（`ubuntu-latest` 将于 2026-10-19 起迁移到 Ubuntu 26）。
- 限制：运行页提示 “Sign in to view logs”，未登录状态无法逐行查看 step 日志；但 build job 为 success，说明新增的日志校验 step 未失败。本地同提交构建（679 页、0 undefined）可独立佐证。
- CI 产物 8.62 MB 与本地 9.93 MB 的差异应主要来自 Linux Noto CJK 与 Windows Noto Serif SC 的字体度量/子集差异，符合 `CLAUDE.md` 的说明，不是内容差异。

### 3. CI 小问题（P4）

- 工作流顶部注释写 “push to main/development”，实际分支过滤为 `main, update-latest-zh`；建议同步注释。
- Node.js 20 告警建议后续升级到 `actions/checkout@v5`、`actions/upload-artifact@v5`，与本轮验收无关。

---

## 五、PDF 与构建日志（通过）

- PDF：A4，679 页；`book.pdf` 与 `agentic-ai-guide-zh.pdf` 字节一致（MD5 均为 `62c84f0c…`）；标题/作者/主题/关键词元数据正确；54 个字体全部嵌入；中文可用 `pypdf` 正常提取，无 U+FFFD 替换字符。1 个数学扩展字体无 ToUnicode（既有，非 CJK 问题）。
- 日志：
  - 0 undefined citation/reference、0 multiply defined、0 Missing character、0 Rerun。
  - Overfull 仅 2 处，且与父版完全同尺寸：`0.111pt`（`book.tex:1242–1243`，缩略语表 KTO 行）与 `0.87877pt`（`contents/part5.tex:6896`，窄表格单元）。
  - `Underfull \hbox` 总数为 70 条，与父版一致；仅 `5614–5617` 一带的合并/拆分方式略有差异，无新增类型。`Underfull \vbox ... \output` 由 70 条降为 0。
  - `TU/lmtt/bx/n → TU/lmtt/b/n` 字体回退仍为 2 处（`\texttt` 粗体），与父版一致。
  - `LaTeX Warning: Text page 217 contains only floats` 1 条，对应图 11.5/11.6 满页，属既有现象。
- 未发现新的严重问题。

---

## 六、`CLAUDE.md` 与 `qa/independent-review.md` 的入库审查

当前 `git status` 仅有这两个未跟踪文件；`.gitignore` 未排除它们或 `qa/*.md`，可直接 `git add`。两者均不含密钥、个人信息或客户数据，适合纳入版本控制。

### 1. `CLAUDE.md`

**适合纳入 Git**：内容为项目构建、目录结构、翻译与字体约定，无密钥、无个人信息；对后续维护和 Claude Code 会话有实际价值。提交前建议修正 3 处事实错误：

1. **`CLAUDE.md:46` 字体回退表述**：现写 “zero font-shape warnings”，但 `grep 'Font shape' book.log` 会命中 2 组 `TU/lmtt/bx/n` 不可用、回退到 `b/n` 的 `LaTeX Font Info`（第 186、4716 行）。这是既有基线，不是回归；应改为“2 处 `\texttt` 粗体回退属已知基线”。
2. **`CLAUDE.md:46` overfull 位置**：现写两个 overfull 在 “bibliography and a narrow table cell”。实际 `0.111pt` 在缩略语表的 `KTO` 行（`book.tex:1242`），只有 `0.879pt` 在 `part5.tex:6896` 的窄表格单元；应改正。
3. **`CLAUDE.md:61` 文档指向**：现写 `qa/independent-review.md` 的 “Section 4 records known upstream-inherited issues”。实际上游勘误记录在 `qa/source-errata.md`；`independent-review.md` 的第四节是 PDF/排版复核。应改为指向 `qa/source-errata.md`。
4. 建议同时更新 `CLAUDE.md:50` 的 CI 描述，补充 `TL2025-historic` 固定、`make` 安装、字体校验与日志门禁；这是不完整而非错误（P4）。
5. **`CLAUDE.md:37–46` 的日志审计流程与 `build.py` 不一致**：文档要求构建后 `grep book.log`，但 `build.py:80–82` 在非 `--keep` 时会删除 `book.log`；直接执行 `python build.py` 后将找不到日志。建议默认保留日志，或在文档中明确使用 `python build.py --keep`。

### 2. `qa/independent-review.md`

**本轮更新后适合纳入 Git**：

- 已改写为 `f33ae2e` 的第七轮验收记录，与当前 PDF、日志和 CI 对应；无密钥、无个人信息。
- 仓库已跟踪 `qa/source-errata.md` 与 `qa/terminology.md`，继续跟踪本报告与现有 `qa/` 文档策略一致，可作为发布审计记录。
- 旧版报告中的本地绝对路径 `D:/agentic-ai-guide-zh-upstream/...` 已在本轮移除；如后续需要注明基准源码位置，建议使用“本地英文 v1.4 源码（未入库）”这类描述性写法，避免把个人目录结构带入公开仓库（P4）。
- 若决定不跟踪，应在 `CLAUDE.md` 中删除对其的引用，避免指向不存在或仅本地存在的文件。

### 3. 相关文档问题（不在本轮修改范围）

- **README 页数（P2，文档）**：`README.md:7` 的 Pages badge 与 `README.md:15` 的正文仍写 **680 页**，当前 PDF 为 679 页。这是本轮页数变化引入的公开文档不一致，建议发布前改为 679。
- **`qa/source-errata.md:66`（P3）**：写 28.5 标题“原在 p567 页底”；本次以 `97f9430` 重建的 680 页 PDF 中，该孤行标题在 **p568** 页底（p567 页底是 `28.4.7 框架对比` 与其一行正文）。其余页码引用（p110、p595、p528、p383、p372、p655 等）均与重建结果一致，故判断为单处笔误，建议核对后改为 p568。
- **`build.py` 与 Makefile/CI 不一致（P3）**：`build.py:72` 仍直接调用 `bibtex`，没有 Makefile 新增的 `.blg` 错误门禁，也没有字体/日志校验；而 `CLAUDE.md` 指定 Windows 本地用 `build.py`。建议把 BibTeX 错误检查同步到 `build.py`，避免本地 Windows 构建静默通过。本轮 PDF 的 `.blg` 仅有 2 条 warning（`nvidia_oo_agents_2026` 缺 institution、`watkins1989learning` 缺 journal），无 error。

---

## 七、剩余问题汇总

| 编号 | 级别 | 问题 | 影响 | 建议 |
|---|---|---|---|---|
| 1 | **P2（文档）** | `README.md:7/15` 仍写 680 页 | 公开页数与 PDF 不符 | 改为 679 |
| 2 | P3 | 7 处英文结构引用：5 处 `Section`（p129/p191/p317/p327/p336）、2 处 `Listing`（p336/p337） | 标签本地化不完整，链接正常 | 改为 `第~\ref~节`、`代码清单~\ref` |
| 3 | P3 | `CLAUDE.md` 3 处事实错误（字体回退、overfull 位置、勘误文档指向） | 误导后续维护 | 按第六节修正后再入库 |
| 4 | P3 | `qa/source-errata.md:66` 的 28.5 页码疑为 p567（实际 p568） | 审计记录不精确 | 核对后修正 |
| 5 | P3 | `build.py` 缺少 BibTeX 错误门禁/字体与日志校验，且默认删除 `book.log` 与 CLAUDE.md 审计流程不符 | Windows 本地构建可能静默忽略 BibTeX 错误，或无法按文档审计日志 | 与 Makefile 对齐，并保留日志或明确 `--keep` |
| 6 | P3（既有） | 目录中 5 字符章节号与标题无空隙（如 `11.10网络…`、`29.10系统…`） | 目录排版瑕疵，非本轮回归 | 调整 `\l@section` 编号盒宽度 |
| 7 | P3（既有风格） | 目录章条目与书签仍为 `1 …`，未带 `第 N 章`；附录目录为 `A 数学基础` | 与章页/部分页标签不完全统一 | 如需完全统一再改 `\@chapter` 的 TOC/书签 |
| 8 | P4 | CI 注释写 `main/development`，实际为 `main/update-latest-zh` | 注释误导 | 同步注释 |
| 9 | P4 | CI Node.js 20 告警、`ubuntu-latest` 迁移 notice | 未来兼容性 | 后续升级 action/runner |
| 10 | P4 | `[H]` 表格不可跨页，后续增行可能溢出 | 维护风险 | 修改 p110 附近内容后复查 |
| 11 | P4（既有） | 多个小节前的显式 `\newpage` 造成页底大片留白（如 p629 约 80%，p366/p71/p69） | 观感与页数；非本轮回归 | 如需紧凑排版可评估改为 `\Needspace`，但会改变全书分页 |

---

## 八、发布建议

1. **PDF 可以发布**：三项排版修复均生效；680→679 页重排经父版重建与逐句比对确认无内容缺失；日志、字体、编号、目录、书签与链接均无新增严重问题。
2. **发布/合并前建议完成**：把 `README.md` 的 680 改为 679（P2）；如需完全中文化，补掉 5 处 `Section` 与 2 处 `Listing`（P3）。
3. **入库前建议完成**：修正 `CLAUDE.md` 的 3 处事实错误；核对 `qa/source-errata.md:66` 页码；把 `build.py` 的 BibTeX 门禁与 Makefile 对齐。
4. **无需重复**：全书 31 章结构计数、12 项源文勘误、第六轮已通过的术语与文本修复，本轮不再重复检查。
