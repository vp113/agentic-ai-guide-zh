# 中文版 PDF 独立复验报告（第八轮·27f0588 发布前收尾）

- 审查对象：`update-latest-zh` 分支，HEAD `27f0588`（`docs(build): complete pre-release audit fixes`）
- 上轮报告：`f33ae2e`（`qa/independent-review.md` 第七轮，PDF 通过；剩余 README 页数、7 处结构引用、CLAUDE.md 事实错误等）
- 复验日期：2026-10-24
- 英文基准：arXiv `2606.24937v3`（Version 1.4，2026-09-29）
- 构建产物：`agentic-ai-guide-zh.pdf`，**679 页**，9,926,592 字节，MD5 `06381aca8a53605688ed37ce3ffe7875`；生成于 2026-10-24 10:07:42（+08）；源码最后修改 09:54:03，`build.py` 09:55:16，提交 10:09:02
- 审查范围：仅复核 `27f0588` 的收尾修改（9 个文件，+378/−11）；不重复此前已通过的全书翻译、技术勘误与版面验收
- 审查方式：只读仓库源码、PDF、日志、Git diff 与 CI 页面；另在临时目录对 `build.py` 做隔离行为测试。未修改源码、PDF 或其他文件，仅更新本报告

## 验收结论

**通过（发布验收）。** README 页数、7 处结构引用、目录编号间距、`build.py` 的 BibTeX 门禁与日志保留均已完成并验证；PDF 仍为 679 页，未发现新增内容、目录、引用或排版回归；CI run `40052969937` 为 success。

仍发现 **3 项新的 P3 文档一致性问题**（勘误文档指向实际未改、`qa/source-errata.md` 原第七轮记录（现第八轮）声称已改、两份 QA 文档的轮次编号彼此错位）及 1 项既有 P3 风格项；上述 3 项文档问题已在本轮同一发布收尾的文档清理中关闭（见文末注记），均不阻塞发布；另有若干 P4 维护项。

| 验收维度 | 结论 | 依据 |
|---|---|---|
| README 页数 | 通过 | `README.md:7/15` 均为 679，与 PDF 一致 |
| 7 处 `Section`/`Listing` 引用 | 通过 | 源码与 PDF 均无残留英文结构引用；p129/p191/p317/p327/p336/p337 已显示“第 X 节”“代码清单 16.13/16.14” |
| 目录编号间距 | 通过 | `book.tex:246–247` 加宽编号盒；p9 的 `11.10–11.12`、p25 的 `29.10–29.32`/`30.10–30.23` 与标题之间已有空隙 |
| `CLAUDE.md` 事实准确性 | 通过（文档清理后） | 字体回退、overfull 位置、CI/build 说明已修正；原 `CLAUDE.md:98` 的勘误文档指向已在本次清理中改为 `qa/source-errata.md` |
| `qa/source-errata.md` 事实准确性 | 通过（文档清理后） | 28.5 页码为 p568；原第七轮（现第八轮）记录中的过度声明已删除；两份文档轮次编号已按 `qa/source-errata.md` 的 QA 轮次对照表统一 |
| `build.py` BibTeX 门禁 | 通过 | 隔离测试：`There was 1 error` 触发退出；仅 warning 通过；缺 `book.blg` 退出 |
| `build.py` 日志保留/清理 | 通过 | 普通构建保留 `book.log`/`book.blg` 与 PDF，清理 `.aux/.toc/.out/.bbl` 等；`--keep` 保留全部；`--clean` 清空中间文件与 PDF |
| PDF 内容、目录、引用 | 通过 | 679 页；0 undefined / 0 multiply / 0 Missing character；目录页号与书签一致；图表 76/114/82、参考文献 460 条不变 |
| GitHub Actions | 通过 | run #2，push `27f0588`，success，3m20s；build 3m17s，release 0s（非标签）；产物 8.62 MB |
| 新增回归 | 无 | overfull 仍为既有 2 处；underfull 70 条、0 vbox；字体 54 个全部嵌入 |

---

## 一、README、结构引用与目录间距

### 1. README 页数（通过）

- `README.md:7` 的 Pages badge 已由 680 改为 679。
- `README.md:15` 正文“全书 31 章、6 个板块、679 页”已同步。
- 当前 PDF 为 679 页，三者一致。

### 2. 7 处结构引用（通过）

源码修改与 PDF 复核一致：

| PDF 页 | 源码 | 当前文本 |
|---|---|---|
| p129 | `contents/part1.tex:5303` | `（参见第 1.12.11 节）` |
| p191 | `contents/part2.tex:3170` | `它在第 6.9.8 节与其他 DPO 扩展…` |
| p317 | `contents/part5.tex:266` | `（参见第 16.4 节）` |
| p327 | `contents/part5.tex:999` | `智能体 RAG（第 16.7 节）…` |
| p336 | `contents/part5.tex:1655` | `（第 16.7 节）` 与 `代码清单 16.13` |
| p337 | `contents/part5.tex:1718` | `代码清单 16.14` |

- 对当前 PDF 全文扫描，`Section`、`Listing`、`Figure`、`Table`、`Appendix`、`Bibliography`、`Contents` 作为独立英文结构词的出现次数均为 **0**。
- 构建日志 0 undefined citation/reference；被引用的章节/清单编号均能解析。

### 3. 目录编号间距（通过）

- `book.tex:246–247` 将 `\l@section` / `\l@subsection` 的编号盒加宽为 3.0em / 4.2em。
- 渲染复核：
  - p9：`11.10 网络拓扑与通信模式`、`11.11 训练吞吐与模型 FLOPs 利用率`、`11.12 成本分析与云端部署` 均已有间隔；`11.10.1` 等子节编号也不再与标题粘连。
  - p25：`29.10 系统架构扩展题` 至 `29.32 图工程问题`、`30.10 智能体通信协议` 至 `30.23 关键智能体基准` 均已正常分隔。
- 目录仍为 p3–p26 共 24 页；抽查页号与书签目的地一致：11.10→228、11.11→229、11.12→230、29.10→603、29.32→630、28.5→568、附录 A→674。
- 加宽编号盒未新增 overfull；日志仍只有既有的 2 处 overfull。

---

## 二、`CLAUDE.md` 与 `qa/source-errata.md` 事实准确性

### 1. 已修正项（通过）

- `CLAUDE.md:47`：字体回退已改为“2 处 `TU/lmtt/bx/n → b/n` 属已知基线”；overfull 位置已改为“0.111 pt 在缩略语表 KTO 行、0.879 pt 在 `part5.tex` 窄表格单元”。两者与当前 `book.log` 一致。
- `CLAUDE.md:51`：CI 描述已补充 `TL2025-historic`、`make`、字体校验、日志门禁、分支与 BibTeX 失败策略，与实际工作流一致。
- `CLAUDE.md:34/97`：`book.log`/`book.blg` 保留策略与 `build.py` 实现一致。
- `qa/source-errata.md:66`：28.5 标题页码已由 p567 改为 **p568**，与重建的 680 页父版一致。

### 2. 未修正项（P3，已在文档清理中关闭）

- **`CLAUDE.md:98` 原写**：`Several source-inherited mathematical/technical errors are documented in qa/independent-review.md (Section 4).`
  - 实际情况：上游勘误记录在 **`qa/source-errata.md`**；本报告（以及第七轮报告）的第四节都不是勘误清单。本次清理已把该指向改为 `qa/source-errata.md`。
- **`qa/source-errata.md:78` 原声称**：原第七轮（现第八轮）“修正 `CLAUDE.md` 的字体回退、overfull 位置与**勘误文档指向**”。前两项属实，第三项与 `CLAUDE.md:98` 的实际内容不符，属记录过度声明。本次清理已删除该表述，并在第八轮记录中单独说明实际修复。

### 3. 轮次编号（已统一）

- 原问题：`qa/source-errata.md` 称 `f33ae2e` 为“第六轮”、`27f0588` 为“第七轮”；`qa/independent-review.md` 称 `f33ae2e` 为“第七轮”、`27f0588` 为“第八轮”，两份文档相差一轮。
- 处理：`qa/source-errata.md` 新增“QA 轮次对照”表，按提交/日期统一：第五轮 `377598d`、第六轮 `97f9430`、第七轮 `f33ae2e`、第八轮 `27f0588`；该文件对应节标题已改为“第七轮：排版与构建优化（f33ae2e）”和“第八轮：发布前收尾（27f0588）”。本报告标题同步标注“第八轮”。

### 4. 入库状态（通过）

- `27f0588` 已将 `CLAUDE.md` 与 `qa/independent-review.md` 纳入版本控制；本次更新前工作区为干净状态。
- `.gitignore` 仍正确忽略两个 PDF、`book.log`、`book.blg` 与中间文件；构建产物未被误纳入 Git。

---

## 三、`build.py` 行为验证

### 1. BibTeX 失败门禁（通过）

- `build.py:59–67` 新增 `check_bibtex_log()`：读取 `book.blg`，匹配 `There was/were N error`（N≥1）即打印日志并退出；`:87` 在 `bibtex` 之后、后续三次 XeLaTeX 之前调用。
- 隔离测试结果（临时目录，不触碰仓库）：
  - `There was 1 error in book.aux` → `SystemExit: BibTeX reported 1 error(s); see book.blg`。
  - `There were 2 warnings` → 正常通过。
  - 缺少 `book.blg` → `SystemExit: BibTeX did not produce book.blg`。
- `subprocess.run(..., check=True)` 仍保证 BibTeX 非零退出时构建失败；因此“非零退出”和“`.blg` 错误摘要”两条路径均是硬失败。

### 2. 日志保留与清理（通过）

- `build.py:95–100` 在普通构建结束时跳过 `AUDIT_LOGS = {book.log, book.blg}`，其余 `INTERMEDIATES` 删除。
- 隔离测试结果：
  - 普通构建后保留：`book.log`、`book.blg`、`book.pdf`、`agentic-ai-guide-zh.pdf`；`.aux/.toc/.out/.bbl/.fls` 均删除。
  - `--keep`：保留全部中间文件（含 `.aux/.toc`）。
  - `--clean`：删除中间文件、日志与两个 PDF。
- 当前仓库也符合该行为：`book.log`、`book.blg` 存在；`book.aux`、`book.toc`、`book.out`、`book.bbl` 均不存在；两个 PDF 存在且字节一致。这与 10:07 的构建使用普通 `build.py` 路径的行为一致。
- 说明：`build.py` 的门禁只覆盖 BibTeX；undefined reference / Missing character 的审计仍由人工 `grep book.log` 或 CI 完成。`CLAUDE.md` 未声称本地构建会自动做这一步，因此不算缺陷，仅列为 P4 可选增强。

---

## 四、PDF、目录、引用与日志

- PDF：679 页，A4；`book.pdf` 与 `agentic-ai-guide-zh.pdf` 字节一致（MD5 `06381aca…`）；标题/作者元数据正确；54 个字体全部嵌入；中文可正常提取，全文无 U+FFFD 替换字符；1 个数学扩展字体无 ToUnicode（既有，非 CJK 问题）。
- 日志：
  - 0 undefined citation/reference、0 multiply defined、0 Missing character、0 Rerun。
  - Overfull 仍为 2 处，尺寸与上一版一致：`0.111pt`（`book.tex:1250–1251`，缩略语表 KTO 行）与 `0.87877pt`（`contents/part5.tex:6896`，窄表格单元）。
  - `Underfull \hbox` 70 条、`Underfull \vbox` 0 条，与上一版相同；`TU/lmtt/bx/n → b/n` 字体回退 2 处，亦为既有基线。
  - `Text page 217 contains only floats` 1 条，对应图 11.5/11.6 满页，属既有现象。
- 目录与书签：
  - 书签 1144 条，总数与上一版一致；命名目标 11781 个；抽查书签页号与目录页号一致（见第一节）。
  - 目录编号盒加宽后未见标题溢出、点线错位或目录页数变化。
- 图表与参考文献：
  - 图 76、表 114、代码清单 82，编号集合与上一版完全一致，无重复/缺号。
  - 参考文献 [1]–[460] 连续，无缺号、无重复。
- 结论：本轮文本/目录改动未引入新的内容或排版回归。

---

## 五、GitHub Actions run `40052969937`

通过运行页（`https://github.com/vp113/agentic-ai-guide-zh-vp113/actions/runs/40052969937`）核实：

- Workflow `Build Book`，run #2，event `push`，branch `update-latest-zh`，head SHA `27f0588`。
- 状态：**Success**；总时长 3m 20s，build job 3m 17s；release job 0s（非标签触发，按预期跳过）。
- 产物：`agentic-ai-guide-zh-pdf`，8.62 MB，SHA-256 `9e6b4fb67a2ff81ccb50e1150ac733401347d5f5a397627d246ecb67a5a4f6a3`。
- 告警：1 warning（`actions/checkout@v4`、`actions/upload-artifact@v4` 仍以 Node.js 20 为目标）+ 1 notice（`ubuntu-latest` 迁移 Ubuntu 26），与上一轮相同，非阻塞。
- 限制：运行页要求登录才能查看 step 日志；build job success 说明字体校验与日志门禁未失败；本地同提交构建（679 页、0 undefined）可独立佐证。
- CI 产物 8.62 MB 与本地 9.93 MB 的差异应主要来自 Linux Noto CJK 与 Windows Noto Serif SC 的字体度量/子集差异，不是内容差异。

---

## 六、剩余问题

| 编号 | 级别 | 问题 | 影响 | 建议 |
|---|---|---|---|---|
| 1 | P3（已关闭） | `CLAUDE.md:98` 原把上游勘误指向 `qa/independent-review.md`（Section 4） | 后续维护者会找错文档 | 已改为 `qa/source-errata.md` |
| 2 | P3（已关闭） | `qa/source-errata.md:78` 原声称已修正“勘误文档指向”，与实际不符 | 审计记录过度声明 | 已删除该表述，并在第八轮记录中说明实际修复 |
| 3 | P3（已关闭） | `qa/source-errata.md` 与 `qa/independent-review.md` 的轮次编号原相差一轮 | 历史记录易混淆 | 已按提交/日期统一，见 `qa/source-errata.md` 的 QA 轮次对照表 |
| 4 | P3（既有风格） | 目录章条目与书签仍为 `1 …`，未带 `第 N 章`；附录目录为 `A 数学基础` | 与章页/部分页标签不完全统一 | 如需完全统一再改 `\@chapter` 的 TOC/书签 |
| 5 | P4 | CI 注释写 `main/development`，实际分支为 `main/update-latest-zh` | 注释误导 | 同步注释 |
| 6 | P4 | CI Node.js 20 告警、`ubuntu-latest` 迁移 notice | 未来兼容性 | 后续升级 action/runner |
| 7 | P4 | `[H]` 表格不可跨页，后续增行可能溢出 | 维护风险 | 修改 p110 附近内容后复查 |
| 8 | P4 | 多个小节前的显式 `\newpage` 造成页底大片留白（如 p629 约 80%） | 观感与页数；既有设计 | 如需紧凑排版可评估改为 `\Needspace` |
| 9 | P4 | `build.py` 不自动审计 undefined/Missing character | 本地构建需人工 `grep` | 可选：与 CI 日志门禁对齐 |

---

## 七、发布建议

1. **PDF 可以发布**：本轮 PDF、README、结构引用、目录间距与 `build.py` 的修复均已生效；679 页内容、目录、引用、字体与日志无新增回归；CI 构建成功。文档侧 3 项 P3 已在本轮文档清理中关闭。
2. **发布前文档清理已完成**：`CLAUDE.md:98` 的勘误文档指向、`qa/source-errata.md` 的对应过度声明，以及两份 QA 文档的轮次编号均已修正；详见文末注记。
3. **无需重复**：全书 31 章结构、12 项源文勘误、前几轮已通过的翻译/术语/版面检查，本轮不再重复。

---

## 八、文档清理注记（同一发布收尾）

- `CLAUDE.md` 的上游勘误指向已改为 `qa/source-errata.md`。
- `qa/source-errata.md` 删除了原第七轮（现第八轮）记录中“已修正勘误文档指向”的过度声明；实际修正记录在本节对应的第八轮条目中。
- 两份文档的轮次编号按 `qa/source-errata.md` 的“QA 轮次对照”统一：第五轮 `377598d`、第六轮 `97f9430`、第七轮 `f33ae2e`、第八轮 `27f0588`；历史记录保留，未改写既有验收结论。
