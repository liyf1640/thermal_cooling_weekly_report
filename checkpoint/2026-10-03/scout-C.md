# scout-C · 仿真方法（原样回传）

## 角度 C 仿真方法：本期未检出窗口内（2026-09-27 ~ 2026-10-03）新增

扫描范围：用 WebSearch 做了约 9 条英文 query，覆盖神经算子/FNO/DeepONet、几何神经算子、PINN 微通道/冷板、POD-ROM 与代理模型、可微分 CHT 求解器、湍流闭合学习。命中的 arXiv 条目都落在窗口外或已在去重清单内。WebSearch 对窗口内（2609.2x 之后 / 2610.x）arXiv 的覆盖有限，没有逐日翻 arXiv cs.LG / physics.flu-dyn 列表页，只能说"检索引擎未返回窗口内相关条目"。
→ **主流程备注：此处覆盖面不足，需主流程用 arXiv API 直接按日期区间补扫一次。**

### 上期挂账：MoE-PINN（10.1016/j.engappai.2026.115892）
**结论：仍然取不到任何性能数字。**
- fetch_source.py 对该 DOI 只返回元数据，没有摘要：
  - 标题：Dynamic weighted mixture-of-experts physics-informed learning for real-time microchannel cooling field reconstruction
  - 作者：Xingpu Feng; Yiming Liang; Sanli Liu; Yuqi Liu; Simon Maher; Min Chen
  - 刊物：Engineering Applications of Artificial Intelligence
  - 出版日期字段：2026-10，是卷期月份，不是在线日。
  - 单位：Crossref 无单位。
- 直接取 ScienceDirect 页返回 403，被代理拦截。
- Crossref API 输出被 fetch_source 截断在 6000 字符，只读到 funder 和 license 段，没读到 abstract 字段，也没看到 created / published-online 值。
- 补充旁证：Crossref 的 license 起始日为 2026-10-01，说明卷期版本可能在 2026-10-01 前后落地。只是旁证，不能当在线日。

### 窗口外 / 已知条目（均不建议作为本期候选）
- arXiv:2609.02982 "Equation Recast for Canonical Operator Learning Across Parametric PDEs"：v1 为 2026-09-02，窗口外。算例是托卡马克，与冷板相关性弱。
- arXiv:2608.28935 NeuralFlowNet（无数据 PINN 求解 N-S）：v1 为 2026-08-28，窗口外。纯流动不含换热，相关性弱。
- arXiv:2608.19426 "Implicit-adjoint finite-volume topology optimization of two-dimensional conjugate heat transfer"：搜索结果页标 2026-08-19 提交，窗口外，未用 fetch_source 核。
- DOI 10.1016/j.aitf.2026.100040 "Physically interpretable surrogate modeling of thermal fields in electronics cooling using combined POD and neural networks"：Crossref created 为 2026-05-09，窗口外。
- 2606.25259 / 2607.17357 已在去重清单内，丢弃。
