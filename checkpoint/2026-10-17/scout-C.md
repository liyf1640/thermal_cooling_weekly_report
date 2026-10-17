# scout C · 仿真方法（原样回传）

窗口 2026-10-11 ~ 2026-10-17。结论：有 1 条中强相关，其余均弱。

扫描范围：
- arXiv API（submittedDate 区间）：16 组 query，覆盖 CHT、heat sink、cold plate、microchannel、liquid cooling、neural operator/DeepONet/FNO、differentiable solver、turbulence closure、PINN、ROM/POD、surrogate CFD、Nusselt+ML、data center cooling、topology optimization。命中 21 条，逐条看过标题。
- Crossref：按 created 日期筛窗口，4 组 query。
- 命中的 arXiv id 与去重清单无重合。WebSearch 一次，未检出窗口内内容。

### 候选 1 · 微通道热沉两层降维模型 VTLM（中强）
- 标题: Versatile two-layer model for thermohydraulic prediction of microchannel heat sinks
- 作者: Chih-Hsiang Chen; Kentaro Yaji
- 机构: 取不到。arXiv 元数据无单位，未读 PDF，不予推断。
- arXiv: 2610.16716，v1 提交 2026-10-12
- 方法: 属降阶/低维建模，非 ML。把 3D 共轭传热问题降为两层耦合的 2D 场，保留平面内流道和翅片几何，沿通道高度方向用水力和热学封闭式补偿（壁面摩擦、流体侧和翅片侧层间换热）。封闭式依据代表性通道几何、流动发展状态和翅片构型取值。
- 验证: 与 3D 参考模型对比，覆盖宽范围的通道宽高比和工况，含均匀与非均匀翅片，另含变宽的扩张-收缩翅片通道。摘要称整体吻合度优于已有两层模型，给出保守的适用筛选准则。
- 数字: 摘要未给定量误差或加速比，需读全文。
- 相关性: 中强。直接面向微通道冷板和热沉的快速热水力预测，可作拓扑优化或参数扫描的内层快速求解器。弱点是不含学习成分，且验证限于直通道和有限的变宽通道。
- URL: https://arxiv.org/abs/2610.16716

### 线索（弱相关）
- **线索 A**：CLNO（守恒局部神经算子），arXiv:2610.16040，v1 2026-10-12。作者 Buxuan Wang; Rongzu Li; Qingsong Zou；机构取不到。有限体积式通量预测加精细尺度重构，强制离散守恒，能泛化到不同 Re/Ma、分辨率和边界条件，在周期性基准上推理成本约为 LNO 的 3–5 倍。弱点: 只做可压缩流，无传热、无壁面湍流、无固体耦合。https://arxiv.org/abs/2610.16040
- **线索 B**：GeONet，arXiv:2610.19493，v1 2026-10-14。作者 Md Lal Mamud 等 16 人（末位 Glenn Hammond）；机构取不到。几何编码 DeepONet 变体，预测多孔介质压力场，3 个留出域 NRMSE 0.0381–0.0500，对比 DeepONet 基线 0.1483–0.2040。弱点: 只预测稳态压力，无温度场，非冷板几何。https://arxiv.org/abs/2610.19493
- **线索 C**：arXiv:2610.18045，3D 湍流流场超分辨重构（多尺度神经算子、状态空间模型、NS 残差软约束、MoE）。作者 Hanlin Kong; Jianan Wei; Yuntian Chen; Yujia Wang; Wenguan Wang；机构取不到。v1 2026-10-13。弱点: 评测对象是典型湍流系统与大气再分析数据，无传热、无壁面受限流。https://arxiv.org/abs/2610.18045
- **线索 D**：arXiv:2610.15885，几何条件化 U-Net 代理模型，预测变房间尺寸下的室内气流与温度场（CaNN 与 CoNN 比较）。作者 Shaofan Wang; Philipp Geyer；机构取不到。v1 2026-10-11。弱点: 建筑室内空调场景，无冷板内容，摘要无定量数字。https://arxiv.org/abs/2610.15885
- **线索 E**：DOI 10.1016/j.icheatmasstransfer.2026.112737，Crossref created 2026-10-15。标题 An energy-form physics-informed neural network with geometry-adaptive hard constraints for steady heat conduction across two- and three-dimensional domains。作者 Zhaoyang Hu; Lin Zhang；机构取不到。弱点: 仅稳态导热 PINN，无对流，无流固耦合；摘要未读。https://doi.org/10.1016/j.icheatmasstransfer.2026.112737

### 窗口内未收录
- 10.1016/j.icheatmasstransfer.2026.112849（Arnav Garg，对流传热求解器的稳定化变化检测）：属求解器验证诊断，非建模方法，无摘要，不推荐。
- 其余 Crossref 命中（微通道和热沉的纯 CFD 参数研究，如 ICHMT 112881、ATE 133571）属其他角度。

### 未检出
窗口内未检出：冷板或热沉 CHT 的神经算子/FNO/DeepONet、可微分求解器、湍流闭合学习、PINN 对流传热、POD-ROM 代理模型。
