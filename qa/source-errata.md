# 英文 v1.4 源文勘误记录

- 基准：arXiv `2606.24937v3`（Version 1.4，2026-09-29）
- 复核日期：2026-10-22
- 范围：`qa/independent-review.md` 中列出的 12 类源文继承问题
- 原则：英文源文件不作为本仓库的修改对象；中文版在确认有误后直接修正，并在下表记录依据。未能确认的内容保留原文。

| # | 位置（中文） | 原问题 | 依据 | 处理 |
|---|---|---|---|---|
| 1 | `contents/appendix-math.tex` 矩阵乘法 | 把矩阵—向量乘法说成 `k=n, m=1` 的特例；`m` 是输出行数，不能设为 1 | 设 `A ∈ R^{m×k}`、`x ∈ R^k`，把 `x` 视为 `k×1` 矩阵，则乘积记号中第二矩阵的列数 `n=1` | 已改为“`x` 视为 `k×1` 矩阵（即 `n=1`）的特例” |
| 2 | `contents/appendix-math.tex` 半正定 | 称注意力得分矩阵是半正定的；`QK^T` 一般不对称，也不保证 `x^T A x ≥ 0` | 半正定的标准定义针对对称矩阵；注意力得分矩阵不是 Gram/协方差矩阵 | 已改为“协方差矩阵与 Gram 矩阵都是对称半正定的；注意力得分矩阵一般不对称，通常不具有这一性质” |
| 3 | `contents/appendix-math.tex` 低秩与 LoRA | LoRA 被指向“第 3 章” | 本版 LoRA 位于第 1 章《LLM 架构与优化方法》 | 已改为第 1 章 |
| 4 | `contents/appendix-math.tex` 正规方程 | 只要求 `m > n`，未要求 `A` 列满秩；秩亏时 `A^T A` 不可逆 | 正规方程 `(A^T A)^{-1} A^T b` 存在的前提是 `A` 列满秩（或改用伪逆） | 已补充“且 `A` 列满秩” |
| 5 | `contents/part6.tex` GRPO 算力节省 | 生成占 60%、生成加速 8×，却称整体加速 4× | Amdahl 定律：`1/(0.4 + 0.6/8) ≈ 2.1×` | 已改为“约 2.1×” |
| 6 | `contents/part6.tex` 70B/32 资源分配 | `70B/32 = 2.2GB 参数` 把参数量与字节数混为一谈 | `70e9/32 ≈ 2.2e9` 参数；BF16 每参数 2 字节，约 4.4GB | 已改为“约 2.2B 参数（BF16 下约 4.4GB）” |
| 7 | `contents/part1.tex` 投机解码期望 token | α=0.8、k=5 时写 3.4；按公式 `(1-α^{k+1})/(1-α)` 应为 3.689 | 直接代入：`(1-0.8^6)/0.2 = 3.68928` | 已改为“约 3.7” |
| 8 | `contents/part1.tex` 70B 前向 FLOPs | 每 token 约 140 TFLOP | 前向约 `2 × 70e9 = 140e9` FLOP = 140 GFLOP | 已改为“约 140 GFLOP” |
| 9 | `contents/part1.tex` FlashAttention roofline | 152 GB/s 被称为“HBM 容量的 7.6%” | A100 HBM 带宽约 2 TB/s；`152/2000 ≈ 7.6%`，与容量（40/80GB）无关 | 已改为“HBM 带宽的 7.6%” |
| 10 | `contents/part2.tex` DPO 的 β | 称 β 越大策略越激进、β 越小越保守，方向与 KL 约束相反 | DPO 的 KL 正则目标为 `max E[r] - β KL(π‖π_ref)`，最优策略为 `π* ∝ π_ref exp(r/β)`；β 越大指数项越接近 1，策略越接近 reference（DPO 论文 arXiv:2305.18290, Eq. 3–7） | 已改为“β 越大 KL 约束越强、越保守；β 越小越激进” |
| 11 | `contents/part2.tex` SimPO 长度归一化 | 称长度归一化防止偏好“短”回答 | SimPO 论文（arXiv:2405.14734）§2.2/§4.2：去掉长度归一化会导致模型偏向生成更长但质量更低的序列，即归一化抑制对长回答的偏好 | 已改为“抑制模型对长回答的偏好” |
| 12 | `book.bib` 重复参考文献 | 6 组重复条目进入参考文献表；实际还有 2 组未被引用的重复键 | 按标题、作者、年份与 URL 比对；保留带 URL 且引用较多的键，重定向引用后删除重复项 | 已去重：Mamba、LoRA、Lost in the Middle、Self-Consistency、StreamingLLM、Tree of Thoughts、OpenRLHF、ALiBi；参考文献由 466 条降至 460 条 |

## 未解决问题

在最初 12 项范围内无未解决问题。上述 12 类问题均已对照数学推导、论文原文或书目元数据确认，并在中文版中修正；英文源文件未改动。

## 后续 P2/P3 处理（2026-10-23）

第三轮复验发现的下列问题已核实并修正：

- **P2-1 GRPO 长度归一化**：`contents/part3.tex` 中“防止偏向较短回答”改为“消除回答长度对损失与梯度尺度的放大”；原英文注释保留，并加注勘误。
- **P2-2 EXO 元数据**：`ji2024exo` 改为 Haozhe Ji 等，*Towards Efficient Exact Optimization of Language Model Alignment*，ICML 2024，arXiv:2402.00856。
- **P2-3 NCA 作者**：`chen2024nca` 改为 Huayu Chen、Guande He、Lifan Yuan、Ganqu Cui、Hang Su、Jun Zhu。
- **P2-4 OpenRLHF 作者**：`hu2024openrlhf` 改为 Jian Hu、Xibin Wu、Weixun Wang、Xianyu、Dehao Zhang、Yu Cao（对应 arXiv:2405.11143v3 作者页）。
- **P3-1 英文注释**：恢复 DPO β 两条原始英文注释；第 5–9、11 项保留英文原句并补充 `% 勘误` 注。
- **P3-2 PSD 定义**：明确限定“对于对称矩阵 A”，并说明特征值等价条件。
- **P3-3 errata 引证与笔误**：修正“注意力得分矩阵”笔误；DPO 依据改为 KL 正则目标与最优策略推导。
- **P3-4 errata 结论**：限定为“最初 12 项范围内无”，并补记本轮 P2/P3 处理。

未处理的 P3：p110 标题/浮动体分页、p595 空白等排版遗留；CI 固定 TeX Live 版本与字体回退复核。这两项属于排版/构建环境优化，不改变正文技术内容。

## 说明

- 第 10、11 项是英文 v1.4 自身的语义错误；中文版修正后与英文原文出现有意偏差，后续同步上游时需保留本勘误。
- 第 12 项在英文 `references.bib` 中同样存在重复键；本仓库只清理中文版 `book.bib`，未修改上游。
- P2-2–P2-4 在英文 `references.bib` 中同样存在；本仓库只修正中文版 `book.bib`，未修改上游。
