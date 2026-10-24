# scout-C 回传（仿真方法）· 原样存档

角度 C 仿真方法 · 第 11 期（窗口 2026-10-18 ~ 10-24）候选清单。
范围说明：本期没有直接做冷板内对流换热的 ML/ROM 论文。下列 8 条里，有较高价值的只有 1–3 条，且相关性都是中等偏弱，不是强。
已扫的源：arXiv API 按 submittedDate 窗口检索（neural operator/FNO/DeepONet、differentiable、turbulence closure、PINN、POD/ROM、surrogate、heat transfer/heat sink/cold plate/conjugate/microchannel/convection）；arXiv physics.flu-dyn 分类检索；Crossref 按 created 检索 IJHMT、JCP、CMAME、Physics of Fluids、IJTS、ATE。
去重：已报 arXiv id 和主题均无命中。
通用说明：arXiv 条目的单位在元数据里都没有，一律「待确认」。Crossref 期刊条目只有 PoF 那条带单位。以下所有条目均已用 fetch_source.py 取到元数据和摘要，但都没读 PDF 全文。

### 候选 1 · 神经算子分裂：复杂几何流体（CL-FNO）
- arXiv 预印本。Neural Operator Splitting for Fluid Dynamics in Complex Geometry
- 作者: Jianxiang Li; Xi Deng; Hong Chul Nam; Anima Anandkumar / 单位待确认
- 日期: 2026-10-20
- 数字（摘要原文）: 相对单个整步神经算子，平均相对 L2 滚动误差 2D 降 68%、3D 降 40%；误差水平相当时每步推理比 Monte Carlo 求解器快约 10^3 倍。
- 方法: 分步法每时间步拆为可解释子步分别学习，用条件线性 FNO（CL-FNO）；配对称采样与纠正循环压制自回归误差累积。
- 相关性: 中偏弱 —— 只涉及流体动力学，无温度场或传热。
- 来源: https://arxiv.org/abs/2610.27671

### 候选 2 · 立方域不可压流稀疏局部核算子学习
- arXiv 预印本。Local and Sparse Kernel Operator Learning for Incompressible Flows: An Operator Lagrange Formulation
- 作者: Ramansh Sharma; Matthew Lowery; Houman Owhadi; Varun Shankar / 单位待确认
- 日期: 2026-10-21
- 数字: 10 个流体基准上稀疏模型精度不低于早期稠密方法、优于神经算子；仿射项使强迫各向同性湍流误差降低一个数量级以上；Lagrange 求值在全局输出重构下比直接求值精度最多高近三个数量级。
- 相关性: 弱 —— 只处理不可压流，不含温度或传热。
- 来源: https://arxiv.org/abs/2610.29009

### 候选 3 · 面向换热器的降阶预测（热耦合 + 流动）
- 同行评审，Crossref 收录。Efficient and robust reduced-order prediction of thermal coupling and fluid flow in cross-flow heat exchangers
- 作者: Tao Luo; Xiaowei Zhu; Lei Zhu; Xin Huang; Bo Deng; Wenjun Sun / 待确认（Crossref 无单位）
- 日期: Crossref created 2026-10-21；出版日期字段 2027-03（卷期日期）。期刊 International Journal of Thermal Sciences。
- 关键数字: 无 —— Crossref 没有摘要，未取到全文，不要引用任何加速比或误差。
- 相关性: 中（仅凭标题判断，未读摘要）。具体方法与精度必须由 verifier 读原文后确认。
- 来源: https://doi.org/10.1016/j.ijthermalsci.2026.111423

### 候选 4 · k–ω SST 闭合在 PINN 中的适用性（湍流槽道）
- 同行评审。Evaluating k–ω shear stress transport closure model in physics-informed neural network for turbulent channel flow
- 作者/单位: Siyu Chen; Jinfeng Liu; Xuehua Zhang / Department of Chemical and Materials Engineering, University of Alberta, Edmonton（Crossref 单位字段，逐位相同）
- 日期: Crossref created 2026-10-20（出版日期字段 2026-10-01，不作判窗依据）。期刊 Physics of Fluids。
- 数字（摘要原文）: 2D 渐扩-渐缩槽道算例用 250 个内部参考点（占仿真网格点 0.25%）。去掉 ω-PDE 残差后，PINN 与 RANS 的相对 L2 误差：速度和压力约 5%，k 约 10%，ω 约 20%。
- 方法要点: 近壁 ω 的刚性是 PINN 学习的主要难点，会导致整个域的大误差。
- 相关性: 弱到中 —— 只有流动，没有传热。可作 NeuralFVM k-ω（第 4 期）的对照线索。
- 来源: https://doi.org/10.1063/5.0350893

### 候选 5 · 数据同化 + ML 辅助湍流建模（轴流压气机）
- arXiv 2610.26567，2026-10-19。Tom Moussie; Pierric Joseph; Marcello Meldi / 单位待确认。摘要无量化百分比。相关性弱（压气机流场，无传热）。

### 候选 6 · CuAD：CUDA 内核的离散伴随自动微分
- arXiv 2610.26694，2026-10-19（v2 10-20）。Seunghyun Joo / 单位待确认。伴随内核成本为原始内核 2–6 倍；Biot-Savart 上 CuAD 约 4 倍、Enzyme 声明 __restrict__ 时约 4 倍、无声明 9–240 倍、Clad 60–4400 倍；伴随与切线一致到 1e-13。相关性弱（算例为 Euler 翼型，非传热）。

### 候选 7 · 相关方法线索（够不上论文卡，未逐条深查）
- JCP 10.1016/j.jcp.2026.115496（created 2026-10-19）对流占优 ROM 稳定性；10.1016/j.jcp.2026.115505 NN-OpInf；10.1016/j.jcp.2026.115510 局部自适应谱算子 PINN。三条仅标题与作者，未取摘要。
- arXiv:2610.31364 Rayleigh-Bénard 二阶线性解耦格式（Nusselt 与已发表值相符 0.5% 内），相关性弱。
- arXiv:2610.26337 CIS-Transolver（汽车外流，平均相对误差较最优基线降 8.72%）、arXiv:2610.31465 RheOPT：几何/迁移学习神经算子，无传热，相关性弱。
- 判为不收：2610.27317、2610.30012、2610.30498、2610.27130、2610.27284、2610.27215。

### 本期未检出项（如实说明）
- 没有检到冷板、微通道热沉、共轭传热的 ML 代理/神经算子/PINN/ROM 新论文。arXiv 上 heat transfer/heat sink/cold plate/conjugate/microchannel 与各种 ML 关键词的组合检索，窗口内零命中。
- Crossref 上 IJHMT 窗口内无冷板类方法学新文（命中的 IJHMT 129746 是辐射 WSGG 的 PINN，与冷板无关）。CMAME 窗口内无直接相关条目。
- 可达性：arXiv API、Crossref、fetch_source.py 均正常。PoF 摘要来自 Crossref，未碰 pubs.aip.org。
