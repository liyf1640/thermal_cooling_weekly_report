# scout-A · 冷板仿真与设计（原样回传）

窗口 2026-09-27 ~ 2026-10-03。

总体说明：
- **arXiv 本窗口未检出角度 A 的新增预印本。** 用 arXiv 检索页与 WebSearch 扫过，API 被限流，结论覆盖不完整。
- 窗口内只有 2609.30785（Job Class Thermal Intent Aware Liquid Cooling Allocation for AI Data Centers），2026-09-25 提交=窗口外，主题为数据中心调度，不收。
- 2609.08387（电池冷却流道风险感知扩散修复）v1 = 2026-09-08，窗口外，不收（亦不在去重清单，非重复）。
- 期刊候选以 Crossref `created` 判窗。`published-online` 多为 None（候选 7、9 例外）。
- 去重：所有候选 DOI 均不在已报 DOI 清单内。Energy 142527 与已报 142364 是不同文章。
- **重要限制**：Crossref 对多数 Elsevier 论文无摘要无单位，fetch_source 只返回题录。除候选 9、10 外**无任何性能数字**。
- 取不到的字段一律写「未取到」，无猜测。

### 候选 1 · 径向歧管微通道热沉多目标拓扑设计（非均匀热源）
- Multi-Objective Topology Design and Optimization of Radial Manifold Microchannel Heat Sinks in Non-uniform Heat Source
- 期刊同行评审（Energy）；DOI 10.1016/j.energy.2026.142527
- Crossref created = `2026-10-02T15:24:46Z`；published-online 缺失；印本 2026-10 不作依据 → 窗口内
- Hanwei Lv; Yasong Sun; Zican Lin; Xiaolong Chang; Huquan Cao; Yifan Wang; Jing Ma。单位未取到
- 摘要未取到，无数字。对象：芯片/电子热沉（据标题）。相关性 **强**

### 候选 2 · 带 3D 歧管的嵌入式微针肋热沉（高功率电子）
- Embedded micro-pin-fin heat sink with 3D manifold for cooling high-power electronics
- 期刊同行评审（IJHMT）；DOI 10.1016/j.ijheatmasstransfer.2026.129613
- created = `2026-09-28T10:31:05Z`；印本 2027-02 → 窗口内
- Zhiyao Jiang; Wei Xiao; Weiheng Li; Bai Song。单位未取到
- 无摘要无数字。相关性 **强**（与 scout-D 候选 1 为同一篇）

### 候选 3 · EV SiC 功率模块液冷热沉多目标拓扑优化
- DOI 10.1016/j.applthermaleng.2026.133472；created = `2026-10-01T16:52:55Z` → 窗口内
- Youyou Gao; Xing Xu; Cong Liang; Heping Ling。单位未取到。无摘要无数字
- 对象：功率电子（SiC 模块），非数据中心芯片。相关性 **中到强**（与 scout-D 候选 2 同一篇）

### 候选 4 · 非均匀高热流下芯片冷却嵌入式针肋微通道优化
- Optimization design of an embedded pin-fin microchannel structure for chip cooling under non-uniform high heat fluxes
- 期刊同行评审（Int. Commun. Heat Mass Transfer）；DOI 10.1016/j.icheatmasstransfer.2026.112696
- created = `2026-09-28T13:11:51Z`；印本 2026-11 → 窗口内
- Yangyu Deng; Fei Xin; Qiang Lyu。单位未取到。无摘要无数字
- 对象：芯片冷却。相关性 **强**

### 候选 5 · 开放微通道选择性表面改性 + 射流冲击气液分离通路
- DOI 10.1016/j.ijthermalsci.2026.111369；created = `2026-10-02T00:16:23Z` → 窗口内
- Yuming Guo; Yifei Li; Yong Qin; Liang Zhao。单位未取到。无摘要无数字
- 相关性 **中到强**；是否针对芯片未核（与 scout-D 候选 6 同一篇）

### 候选 6 · 3D 堆叠 IC 冷板 + 侧歧管混合冷却数值研究
- DOI 10.1109/tcpmt.2026.3739728；created = `2026-10-02T19:05:03Z` → 窗口内
- Chukwudi Azubuike / Mohammad Tradat / Bahgat Sammakia（均 Binghamton University，Crossref 原始机构串）
- 无摘要无数字。对象：芯片冷板（3D 堆叠 IC）。相关性 **强**（与 scout-D 候选 4 同一篇）

### 候选 7 · 带三角形侧壁沟槽的歧管微通道流动沸腾热水力性能
- Thermal-Hydraulic Performance of Flow Boiling in a Manifold Microchannel with Triangular Sidewall Grooves
- J. Fluid Flow, Heat and Mass Transfer（Avestia）；DOI 10.11159/jffhmt.2026.029
- https://jffhmt.avestia.com/2026/029.html
- created = `2026-10-02T13:15:32Z`；published-online = `[[2026]]`（仅年份）→ 窗口内（据 created）
- Pengyang Jin; Haocheng Wang; Yong Ren。单位未取到。无摘要无数字
- 小刊，质量需判断。相关性 **中到强**

### 候选 8 · 新月形针肋 vs 光滑微通道热沉流动沸腾对比
- DOI 10.1016/j.icheatmasstransfer.2026.112763；created = `2026-10-03T10:16:59Z` → 窗口内
- Fadi Alnaimat; Abdul Hanan; Bobby Mathew。单位未取到。无摘要无数字。相关性 **中**

### 候选 9 · 仿鲨鱼皮翅片微通道热沉（Görtler 型二次流强化）★有摘要
- Thermo-hydraulic performance of a Shark-skin-inspired finned microchannel heat sink with Görtler-type secondary flow enhancement
- 期刊同行评审（Physics of Fluids）；DOI 10.1063/5.0347413
- created = `2026-10-01T08:35:06Z`；**published-online = 2026-10-01** → 窗口内
- Ge Gao; Guangze Li; Yuhui Wang; Liuyong Chang; Longfei Chen; Feng Han
- 已取到的机构串：Hangzhou International Innovation Institute, Beihang University；School of Aeronautic Science and Engineering, Beihang University；Tianmushan Laboratory；College of Energy and Power Engineering, Nanjing University of Aeronautics and Astronautics。**逐位对应关系未取全**
- 摘要（Crossref 节选）：全尺寸微通道热沉高保真湍流数值模拟，realizable k–ε。仿生翅片在所考察 Reynolds 数范围内打破强化换热与压降上升的权衡。**具体数字被截断，未取到**
- 对象：高功率密度集成电路微通道热沉。相关性 **中**（纯 CFD，翅片形状设计）

### 候选 10 · 低 GWP 制冷剂两相 D2C 针肋冷板的系统压力影响 ★有摘要
- Effect of system pressure on the thermal resistance and pumping power of a pin-fin cold plate for two-phase direct-to-chip cooling using low GWP refrigerants
- **SSRN 预印本（未同行评审）**；DOI 10.2139/ssrn.7536705
- created = `2026-09-28T13:47:12Z` → 窗口内
- Wookyoung Kim; Kyeonghui Hong; Jinsub Kim; Kong Hoon Lee。单位未取到
- 摘要（Crossref 节选）：铜冷板，加热面 25.4×25.4 mm，R1233zd(E)/R1234ze(E)/R1234yf 过冷流动沸腾。入口温度 40 °C，输入功率 45 W 到标称 1 kW，质量流量 0.152–2.235 kg/min，过冷度 1.8–39.9 K，高速摄影 + 测温。出口平衡干度判为单相液体的工况也出现核态沸腾。**1 kW 下热阻的结论被截断，未取到**
- 对象：芯片冷板（数据中心 D2C 两相）。相关性 **强**（实验类）

### 其它弱相关，仅备查
- Advances in Direct-to-Chip Liquid Cooling Integration，ECTC 2026，DOI 10.1109/ectc51846.2026.00097，Crossref created = 2026-10-01，作者 L.W. Mirkarimi 等，单位 Adeia。**会议 2026-05 召开，created 只是 DOI 登记日**，偏集成工艺非仿真设计
- Hydraulic Data Reconciliation and Pumping-Power Assessment of an Eight-Channel Microchannel Cold Plate，SSRN，DOI 10.2139/ssrn.7541497，created = 2026-09-29，仅题录
- Thermal Analysis and Experimental Studies of a Plate-Fin Heat Sink Integrated with U-Shaped Liquid-Cooling Channel，IARJSET，DOI 10.17148/iarjset.2026.131003，created = 2026-10-03，小刊质量存疑
- Optimization of chimney design for an extruded radial heat sink...，IJHMT，DOI 10.1016/j.ijheatmasstransfer.2026.129656，created = 2026-10-02，空冷，相关性弱
- Thermohydraulic and Thermodynamic Optimization of Supercritical CO2 Cooling in a Serpentine Microchannel for High Heat Flux Electronics，J. Supercritical Fluids，DOI 10.1016/j.supflu.2026.107166，created = 2026-10-02，未取到摘要
- Structural Design and Parameter Optimization of a Center-Rotary Cooling Belt...，SSRN，DOI 10.2139/ssrn.7548797，created = 2026-10-01，对象是电池冷却带

### 本角度未检出的方向
- 生成式设计（扩散/GAN/VAE）、ROM 或神经算子代理、共轭传热 CFD：窗口内未检出新增
- Crossref 14 个主题 query 全库检索，其中 5 个被限流（429）未重跑：jet impingement cooling heat sink、data center liquid cooling、generative design heat sink、pin fin heat sink、direct-to-chip cooling。**数据中心与 D2C 覆盖相对薄**
