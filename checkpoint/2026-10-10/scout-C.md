# scout-C · 仿真方法（原样回传）

## 候选 1 · Cova-PINN：流固共轭传热的跨域守恒 PINN（TPMS 换热器）
- arXiv 预印本（未见同行评审）
- Cova-PINN: Cross-Domain Conservation Physics-Informed Neural Network for Fluid-Solid Conjugate Heat Transfer in Complex Geometries
- 作者 Weizheng Zhang; Xunjie Xie; Hao Pan; Lin Lu / 单位待确认（arXiv 元数据无单位）
- 2026-10-08（arXiv 提交日）；https://arxiv.org/abs/2610.11108
- 摘要数字：4 种 TPMS 换热器上相对最接近基线 MUSA-PINN-CHT，**平均出口温度误差降低 37.7%**、
  **器件级闭合误差降低 60.2%**；另在几何不同的 DualMS 设计上有一致增益。摘要未给加速比。
- 相关性 中（多域 PINN 做流固共轭传热，思路可迁移到冷板；对象是 TPMS 换热器非冷板，且是 PINN 非快速代理）
- 核验状态：已用 fetch_source 核摘要；单位未核

## 候选 2 · 多层多芯片功率模块热扩散的 PINN
- Physics-informed neural networks for thermal spreading of multilayer multichip power modules
- 作者 Yonghun Kim; Changhyeon Yoon; Haeun Lee; Seonu Bae; Nana Kang; Changwoo Han; Dongmin Shin; Jungwan Cho; Sooyoung Lee; Hyoungsoon Lee / 待确认
- Crossref created 2026-10-05（published-print 2026-11 不作依据）；ICHMT
- DOI 10.1016/j.icheatmasstransfer.2026.112739
- 关键数字：无（Crossref 未给摘要）；相关性 中；仅元数据，需 verifier 复核

## 候选 3 · 数据中心 AI 热感知容量规划（CFD 代理，10000X 加速）
- arXiv 预印本（评论称 Presented at DesignCon 2026）
- AI-driven Thermal-aware Data Center Capacity Planning；作者 Yixing Li; Mark Fenton; Matthew Kaufeler; Ka Ming Leung; Xin Ai; Zhiyu Zeng / 待确认
- **2026-10-01（窗口外）**；https://arxiv.org/abs/2610.02442
- 摘要：对未见过的数据中心设计相对高保真 CFD 达 "10000X speedup"，预测毫秒级；摘要未给误差数值
- 相关性 弱（机房级风冷/HVAC 温度场代理，不是冷板内对流换热）

## 候选 4 · 弱线索：分支-主干神经算子中精确 PDE 残差的消融（制动盘热传导）
- SSRN 预印本，未同行评审；作者 Franklin Kamche / 待确认；created 2026-10-08
- DOI 10.2139/ssrn.7584766
- 摘要：64 个有限元算例训练；精确 PDE 残差相对纯数据训练无可测增益、训练成本 3.2 倍；
  latent POD 基线落后纯数据算子 15.4 倍；推理比参考求解器快约 25 倍
- 相关性 弱（纯导热无对流；结论对冷板神经算子代理的训练设计有参考意义）

## 候选 5 · 弱线索（建议不收）：SAGE-PINN 轴对称多物理 PINN
- arXiv 2610.10449（2026-10-07）；作者 Raj Maurya; Joyprakash Akhuli; Doyel Pandey / 待确认
- 摘要：轴向速度与温度相对 L2 误差 1.6% / 9.1%（中心工况范围）；算例是狭窄动脉中纳米流体
- 相关性 弱（限轴对称几何与生物医学算例，对冷板无直接用处）

## 本期未检出（不凑数）
- 神经算子（FNO/DeepONet/几何算子）：本窗内无针对冷板或传热的新增（arXiv 只命中 2610.07811、2610.04241，与传热无关）
- 可微分求解器：本窗内无传热/CFD 相关新增
- 湍流闭合学习：只有 arXiv 2610.12170（2026-10-08，EKI 在线校准二维谱涡粘闭合），二维强迫湍流无传热，仅弱线索
- 降阶模型 ROM：本窗内无对流/传热新增
- 冷板/微通道/热沉的 ML 代理与 PINN：arXiv 本窗无新增
- 检索说明：WebSearch 对日期不敏感；主要靠 arXiv API 按提交日倒序过滤 + Crossref created 过滤。
  **未单独检查 JCP、CMAME、Physics of Fluids 期刊页，只经 Crossref 间接覆盖，可能有遗漏。**
