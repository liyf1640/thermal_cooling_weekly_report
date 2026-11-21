# scout-C 回传 · 仿真方法（原样存档）

时间窗 2026-11-15 ~ 2026-11-21。
- arXiv API 起初 429，**重试后成功**，查了 7 组关键词（neural operator / surrogate / PINN / ROM-POD /
  GNN-diffusion-differentiable / CHT+ML / microchannel+ML，各取最新 40 条，按 updated ≥ 11-14 过滤）。
  **窗口内只有 1 篇涉及冷板。**
- 另按 Crossref created 窗口做了 4 组关键词查询。命中的会议论文在 Crossref 上**都没有摘要**，
  覆盖面闸门所需的「摘要字面」拿不到 → 只能算线索。
- 去重清单上的 arXiv id 与方法类论文卡均未再命中。HAWFNO 未重新提出。

## ① 覆盖面内（摘要明确涉及冷板或电子散热）
### 1. EJBench：由电池冷板 CHT 设计活动构建的工程判断基准
- Bookkeeping Is Not Judgement: EJBench, an Engineering Judgement Benchmark Built from a Conjugate Heat Transfer Design Campaign
- arXiv:2611.21707；2026-11-16 投稿（v1）
- 作者：James Sadler; Rotimi Alabi; Kotub Uddin。**单位待确认**（arXiv 元数据无单位，需读 PDF）。
- 摘要关键内容：是 **LLM 工程判断基准，不是 CFD 加速方法**。任务为不跑仿真、由少量已有结果预测新工况表现并决策。
  题材取自**电池冷板**共轭换热设计活动。三类任务：把无标签测试结果匹配到工况点；选择先揭示哪些已存储算例再签字；
  按电芯峰值温度对新工况排序。答案取自收敛仿真，不用 LLM 评判。
  **十个前沿模型最佳得分 0.71**，模型对做错和做对的任务给出几乎相同的置信度。
  用 LoRA + 强化学习对 Qwen3.5-9B 后训练，留出测试集得分自 **0.071 升到 0.106**。发布了划分、评测脚本与排行榜。
- 覆盖面依据（摘要原文）："Its tasks come from a conjugate heat transfer design campaign for battery cold plates"
- 相关性：冷板字面满足，但**对象是电池冷板**，且方法学价值偏弱（LLM 评测、非场建模）。
- 预印本、未同行评审。置信度高（fetch_source 取到摘要原文）。

## ② 相关方法线索（相关性弱或摘要未核）
### 2. THERMINIC 2026：Synopsys，AI 驱动的非参数几何优化散热器
- AI-Driven, Non-Parametric Geometry Optimization for Heat Sink Design
- DOI 10.1109/therminic70452.2026.11779745；Crossref created **2026-11-19**（published 记为 2026-09，会议 9 月召开、晚入库）
- 作者：Achref Rabhi; Daniel Haase; Sivasubramani Krishnaswamy; Julio Benavides Rodriguez; Tobias Berg（**均 Synopsys Inc.**）
- 摘要：Crossref 未提供，无数字。标题字面含 heat sink，但闸门条件未能核实。置信度中。

### 3. THERMINIC 2026：SiC 功率模块热降阶模型，用于动力总成冷却系统设计
- Thermal Reduced-Order Modelling of a SiC Power Module for Powertrain Cooling System Design
- DOI 10.1109/therminic70452.2026.11779773；created **2026-11-19**
- 作者：Karnon Koné（Safran Tech / Institut PPRIME, CNRS-ENSMA-Université de Poitiers）; Matthieu Fénot; Etienne Videcoq（均 Institut PPRIME）;
  Amal Zeaiter; Sulivan Küttler（均 Safran Tech）
- 摘要：Crossref 未提供。题名含功率半导体与冷却系统，**是否涉及冷板需核原文**。置信度中。

### 4. THERMINIC 2026：IGBT 模块参数化模型降阶，用于系统级电热仿真
- Parametric Model Order Reduction of an IGBT Module for System-Level Electro-Thermal Simulation
- DOI 10.1109/therminic70452.2026.11779736；created **2026-11-19**
- 作者：Shashwat Kamal Gogoi; Aliakbar Taghdiri; Philipp Hickisch; Dennis Hohlfeld; Tamara Bechtold（均 University of Rostock）
- 摘要：Crossref 未提供。属功率半导体热 MOR，**与冷板对流建模关联偏弱**。置信度中。

### 5. ESTC 2026：功率电子模块热-机械有限元的数值稳定降阶模型
- Accelerating Finite Element Thermal-Mechanical Analyses of Power Electronic Modules by Numerically Stable Reduced-Order Models
- DOI 10.1109/estc68880.2026.11778957；created **2026-11-17**
- 作者：Sheikh Hassan（University of Greenwich）; Mark Sherriff; Kangkana Baishya; Pearl Agyakwa; Paul Evans（均 University of Nottingham）;
  Stoyan Stoyanov（University of Greenwich）
- 摘要：Crossref 未提供。偏热-机械，**与冷板对流关联最弱**。置信度中低。

### 6. 歧管微通道热沉：高斯过程代理 + NSGA-II（与 scout A 候选 1 同条）
- 10.54097/fdaate22；created/published 2026-11-20；*Academic Journal of Applied Sciences*（Darcy & Roy Press）
- 作者：Weifu Huang; Wenyan Xue（均 Guangdong Ocean University, College of Mechanical and Energy Engineering, Yangjiang, China）
- 摘要关键内容：三个结构参数控制热阻、压降与壁温均匀性，**样本只有几十个**；
  解析式拟合压降 **R²=0.8994**、热阻 **R²=0.6229**（热阻因两个大系数相互抵消而**参数不可辨识**）；
  对比高斯过程回归与两种树集成，把单次目标评估自一次仿真降为一次矩阵乘法；
  NSGA-II 求 Pareto 前沿、TOPSIS 给等权折中解，再用拉丁超立方权重扫描检验稳定性；
  推荐设计**无 pin fin、深度比 4.48、4 排**，压降为热阻最优解的 **36.4%**、热阻增加 **4.4%**，100 组随机权重中 **71 组**仍最优。
- 覆盖面依据：摘要只有 "manifold microchannel heat sink"，**没有字面的芯片或电子散热，闸门条件不满足**。
- 期刊论文，评审深度待确认；**出版社较小，建议谨慎**。置信度高（摘要已取到）。

### 7. 热源过渡 FNO：燃料电池负载变化下的瞬态温度场（相关性弱）
- A heat-source transition fourier neural operator for transient temperature field prediction in fuel cells under load changes
- DOI 10.1016/j.ijheatmasstransfer.2026.129923；created **2026-11-19**；published-print 2027-04（不作依据）；IJHMT
- 作者：Jing Sun; Yucai Shao; Anping Xie; Mingyan Xing; Xin Liang; Guobin Zhang; Qiang Zheng; Huan Wang。单位待确认。
- 摘要：Crossref 取不到。**对象是燃料电池，无电子散热字面依据** → 建议不收。置信度中。

## 明确不收的命中
- arXiv 2611.25512：Centralized-UPS 数据中心电气代理，属电力系统，与冷却无关。
- 10.2139/ssrn.7693278：直接芯片液冷服务器冷板布置的热水力优化，**不是仿真方法**；SSRN 通道不可用，不核。
- 10.1016/j.ijheatmasstransfer.2026.129924：新型几何微通道热沉，**是结构设计不是仿真方法**，已交其他角度。

**结论：本期窗口内，覆盖面内的 ML-for-CFD / 神经算子 / PINN 冷板论文未检出。唯一过闸门的是 EJBench，且只是边缘相关。**
