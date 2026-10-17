# scout D · 英文期刊 in-press / online-first 专项（原样回传）

窗口 2026-10-11 ~ 10-17，判窗 Crossref `created`。

**方法与说明**
- 用 Crossref `filter=issn:…,from-created-date:2026-10-11,until-created-date:2026-10-17` 按刊直扫，分页取全，再做关键词筛选，并人工过一遍未命中标题。
- 作者单位来自 OpenAlex 的 `raw_affiliation_strings`（出版商交存机构串的聚合），**不是读论文原文**。Elsevier 的 Crossref 记录本身无单位、无摘要。
- 摘要与数字取自 OpenAlex 的摘要倒排索引。OpenAlex 当日免费额度中途用尽，标「未取到」的几条没能补。
- 全部候选 `published-online` 都是 None（Elsevier 常态，只有 `created`）。印本刊期都是名义日期，不作判窗依据。
- 与去重清单无重合。全部 ScienceDirect 页面出口 403，核验状态一律「Crossref + OpenAlex 元数据核，未读正文」。

### 每刊覆盖结论

| 刊 | ISSN | 窗口内条数 | 相关性结论 |
|---|---|---|---|
| IJHMT | 0017-9310 | 34 | 有，但偏弱（候选 30） |
| ATE | 1359-4311 | 65 | 有，较多（候选 3–5、9、11、12） |
| ICHMT | 0735-1933 | 59 | 有，较多（候选 6–8、10、15–23） |
| Energy Conversion & Management | 0196-8904 | 31 | **本期未检出**（最近为 122281 低温冷能区域供冷、122260 余热 Corrigendum，均不属冷板） |
| IJTS | 1290-0729 | 14 | 有，弱到中（候选 24–26） |
| ASME J. Electronic Packaging | 1043-7398 / 1528-9044 | **0** | 见下 |
| ASME J. Heat and Mass Transfer | 2832-8450 / 2832-8469 | **0** | 见下 |
| ASME J. Heat Transfer（补查） | 0022-1481 / 1528-8943 | **0** | 最新 `created` 是 2022 年，疑已停更或迁移 |
| IEEE TCPMT | 2156-3950 / 2156-3985 | 5 | 1 条相关（候选 27）。3743475 芯粒互连、3743562 TGV 铜突出、3743517 滤波器，均排除 |
| Applied Energy | 0306-2619 | 42 | **本期未检出** |
| Energy | 0360-5442 | 91 | 弱到中（候选 14、28；142722 车辆热管理架构生成设计，仅备注） |
| Case Studies in Thermal Eng. | 2214-157X | 23 | 弱（候选 29） |
| Physics of Fluids | 1070-6631 / 1089-7666 | 91 | **本期未检出**（5.0353101、5.0352639 沾边，不收） |
| Int. J. Heat and Fluid Flow | 0142-727X | 8 | 1 条（候选 13） |

**ASME 两刊的 ISSN 复核**
- Crossref `/journals` 确认：JEP 的 ISSN 就是 1043-7398 / 1528-9044，ASME JHMT 就是 2832-8450 / 2832-8469。**上期用的 ISSN 没错，窗口 0 条是真实的。**
- JEP 最新 `created` 2026-09-25（10.1115/1.4072719）；ASME JHMT 最新 `created` 2026-09-17（10.1115/1.4072697）。
- 另一点：ASME 的 `published-online` 比 `created` 晚一到两周（例 JEP 1.4072719：created 09-25、published-online 10-01）。未找到 `published-online` 落在 10-11~10-17 的条目，但未逐条验证。

---

### A. 两条上期挂账（首发）

### 候选 1 · 新月形针肋 vs 光滑小通道流动沸腾（挂账 112763）
- 标题：A comparative study of flow boiling heat transfer and pressure drop in crescent pin-fin and smooth minichannel heat sinks
- 作者：Fadi Alnaimat；Abdul Hanan Muhammad Zaheer（Crossref 写 "Abdul Hanan"）；Bobby Mathew
- raw_affiliation：Alnaimat 与 Mathew 均为 "Mechanical and Aerospace Engineering Department, College of Engineering, United Arab Emirates University, 15551 Al Ain, Abu Dhabi, United Arab Emirates" 与 "National Water and Energy Center, United Arab Emirates University, Al Ain, United Arab Emirates"。Abdul Hanan Muhammad Zaheer 仅前一条。
- 刊名/DOI：ICHMT vol.180 / 10.1016/j.icheatmasstransfer.2026.112763
- `created` 2026-10-03；`published-online` 无；印本名义 2026-11 → **窗口外**
- 性质：**实验**。去离子水，入口 80 °C，质量流速 180–360 kg/m²·s，热流密度 15.45–100.59 kW/m²，含高速可视化。
- 数字：新月形针肋最大 HTC 约 12–12.5 kW/m²·K，光滑通道约 7–7.2 kW/m²·K。针肋压降更高，压力波动更小。
- 相关性：中到强（微通道沸腾散热器），但热流密度只到约 100 kW/m²（约 10 W/cm²），数值很低。
- URL：https://doi.org/10.1016/j.icheatmasstransfer.2026.112763

### 候选 2 · 编码波纹并联微通道（挂账 112814）
- 标题：Encoded corrugation design for flow redistribution and thermohydraulic performance enhancement in parallel microchannels
- 作者：Yili Zhou；Ping Xu；Jie Xing；Shuguang Yao
- raw_affiliation：**取不到**（Crossref 无，OpenAlex 空）
- DOI：10.1016/j.icheatmasstransfer.2026.112814；`created` 2026-10-09 → **窗口外**
- 摘要：**取不到**。相关性强，但无数字，无法判断实验还是仿真。
- URL：https://doi.org/10.1016/j.icheatmasstransfer.2026.112814

---

### B. 窗口内新增（强相关）

### 候选 3 · 电池冷板拓扑设计 cGAN + Ridge 代理模型
- 标题：Two-stage cGAN-ridge surrogate for battery cold plate topology design
- 作者：Puneeth D. Shetty；Akhil Garg；Phi Long Nguyen（Crossref 写 Nguyen Phi Long）；Hai Hung Pham；Jonghoon Kim；Kexiang Wei
- raw_affiliation：Shetty — Department of Mechanical Engineering, National Institute of Technology Calicut, Kerala, India。Garg — Department of Chemistry and Materials Science, Advanced Materials Research Center, School of Science, Xi'an Jiaotong-Liverpool University, Suzhou, Jiangsu 215123, China。Nguyen — Center for Environmental Intelligence and College of Engineering & Computer Science, VinUniversity, Hanoi, Viet Nam，兼 School of Electrical and Electronic Engineering, Hanoi University of Industry。Pham — VinUniversity 同上。Kim — Energy Storage and Conversion Laboratory, Dept. of Electrical Engineering, Chungnam National University, Daejeon, South Korea。Wei — Hunan Provincial Key Laboratory of Vehicle Power and Transmission System, Hunan Institute of Engineering, Xiangtan 411104, China。
- 刊名/DOI：ATE vol.308 / 10.1016/j.applthermaleng.2026.133314；`created` 2026-10-12
- 数字：256×256 场约 35 ms 生成。71 个留出样例：拓扑 IoU 0.704，温度 SSIM 0.692。连通性 57/71，压力单调性均值 66.9%。Ridge 对三个温度目标 R²=0.311–0.607、Spearman ρ=0.761–0.830。**压降预测失败**（R²=−0.009，ρ=0.069），压降被排除出自动评分，仍靠 CFD 校核。20 个候选中只需 2–3 个送 CFD，但该缩减目标作者自述尚未对全 CFD 排序验证。作者明说它是约束惩罚型代理，不是 PDE 残差模型。
- 相关性：强。结论偏保守，写稿时别夸大。
- URL：https://doi.org/10.1016/j.applthermaleng.2026.133314

### 候选 4 · 激光器制冷剂冷板的数据高效多目标结构优化
- 标题：Data-efficient multi-objective structural optimization and design space exploration of refrigerant-based cold plate for laser device
- 作者：Qingwen Gui；Youwei He；Jiangshuo Cui；Yong Chen；Chaochao Zhou
- raw_affiliation：**取不到**（OpenAlex 404，尚未收录）；摘要与数字 **取不到**
- DOI：10.1016/j.applthermaleng.2026.133678；`created` 2026-10-17（窗口末日）
- URL：https://doi.org/10.1016/j.applthermaleng.2026.133678

### 候选 5 · 混合微通道 + 拱桥针肋热点缓解
- 标题：Localized hotspot mitigation using a hybrid microchannel heat sink with alternating-orientation arched-bridge pin-fins
- 作者：Xinglan Hou；Yongheng Yang；raw_affiliation **取不到**；摘要与数字 **取不到**
- DOI：10.1016/j.applthermaleng.2026.133571；`created` 2026-10-16
- URL：https://doi.org/10.1016/j.applthermaleng.2026.133571

### 候选 6 · 双侧液冷 SiC IGBT 模块的分区拓扑优化微通道热沉
- 标题：Zoned topology optimization of double-sided liquid-cooled microchannel heat sinks for the thermal management of SiC IGBT modules（Crossref 标题被截断，完整副标题以原文为准）
- 作者：Hanyang Xu；Yifan Wang；Wenchao Tian；Feiyang Li；Han Shen；Daowei Wu
- raw_affiliation：前五位为 "School of Electro-Mechanical Engineering, Xidian University, Xi'an 710071, China" 或 "State Key Laboratory of Electromechanical Integrated Manufacturing of High-Performance Electronic Equipments, Xidian University, Xi'an 710071, China"，或两者并列。Daowei Wu 为 "National Key Laboratory of Integrated Circuits and Microsystems, China"。
- DOI：10.1016/j.icheatmasstransfer.2026.112802；`created` 2026-10-13
- 性质：**仅仿真**（ANSYS FLUENT）
- 数字：相对常规直通道 MCHS，整体热性能因子提高 114–187%。TOPO_20（20 mm 宽高温核心区）平均 IGBT 模型温度降 3.62 K，平均 SiC 结温降 6.41 K，模块封装峰值热机械应力降 72.76 MPa。额定工况。
- URL：https://doi.org/10.1016/j.icheatmasstransfer.2026.112802

### 候选 7 · 肋腔耦合微通道（等流体域体积设计）
- 标题：Effect of coupled ribs and cavities on the hydrothermal comprehensive performance of microchannels under constant fluid domain volume（标题截断）
- 作者：Wenling Liao；Zhengbiao Jing；Shuaimei Lian；Fenghao Chen；Ao Li；Yuhan Xu；Pingping Liu
- raw_affiliation：除 Jing 外均为 "School of Mechanical Engineering, Chengdu Technological University, Chengdu, 611730, China"。Jing 为 "Chengdu Vocational & Technical College of Industry, Chengdu, 610218, China"。
- DOI：10.1016/j.icheatmasstransfer.2026.112861；`created` 2026-10-14
- 性质：仿真，Re=355–1065，五种构型。数字：DLMC-SRCS 平均综合性能 η 超过 1.8，峰值 1.847（Re=533）。
- URL：https://doi.org/10.1016/j.icheatmasstransfer.2026.112861

### 候选 8 · 肋间连通微通道热沉（ICMCHS）
- 标题：Numerical study on thermo-hydraulic performance of rib-interconnected microchannel heat sink
- 作者：Xiuxian Zou；邓晖（OpenAlex 显示名，英文名待确认）；Leyong Jiang；Wangbing Yu；Xiaohu Wu
- raw_affiliation：前四位 "School of Physics and Electronics, Hunan Normal University, Changsha, 410081, China"，Zou 与邓晖另加 "Yangtze Laboratory, Wuhan, 430205, China"。Xiaohu Wu：School of Integrated Circuits, Hubei University, Wuhan；Thermal Science Research Center, Shandong Institute of Advanced Technology, Jinan；Yangtze Laboratory。
- DOI：10.1016/j.icheatmasstransfer.2026.112881；`created` 2026-10-16
- 性质：仿真，Re=92–829。数字：Re=829 时三角肋 case 8 相对常规 MCHS，最高基底温度降 12.65 K，传热系数升 129.36%，温度不均匀度降 65.80%，PEC 1.99，最大热流容量 132.01 W/cm²（提高 122.20%）。
- URL：https://doi.org/10.1016/j.icheatmasstransfer.2026.112881

### 候选 9 · 超薄均热板：蒸腾启发微膜（实测）
- 标题：Transpiration-inspired micromembrane-enabled ultrathin vapor chambers with suppressed flow evolution
- 作者：Yuxi Wu；Guisheng Zou；Hang Yu；Kuan Zhao；Zhewen Xiong；Chengjie Du；Haishan Cao；Yahui Wang；Shaoning Mu；A Zhanwen；Jinpeng Huo；Lei Liu
- raw_affiliation：清华大学机械工程系 / 先进材料加工技术教育部重点实验室 / 洁净高效透平动力装备全国重点实验室（Wu、Zou、Yu、Du、Huo、Liu 等）；Xiong、Cao 为清华大学能源与动力工程系热科学与动力工程教育部重点实验室；Zhao 与 A Zhanwen 为 "School of Mechanical Engineering, Qinghai University, Xining, Qinghai, 810016, China"；Yahui Wang 与 Shaoning Mu 为 "S Lab, GIC, IDG, Lenovo (Beijing) Co., Ltd., Beijing, 100085, China"。
- DOI：10.1016/j.applthermaleng.2026.133601；`created` 2026-10-14
- 数字：干涸距离和热流约提高 2 倍。0.41 mm 与 0.31 mm 的 UTVC 在严格抗重力下支持 7 W/cm²，最大扩散温差分别小于 0.9 °C 与 1.2 °C，最大热负荷是开槽对照的 2 倍以上。
- 相关性：中（移动电子均热板，非冷板，但属电子散热硬件实测；有联想企业合作者）
- URL：https://doi.org/10.1016/j.applthermaleng.2026.133601

### 候选 10 · 笔记本双热源均热板（实测）
- 标题：Transient response and thermal safe operating area extension of dual-heat-source vapor chambers for high-performance laptops（标题截断）
- 作者：Jing Wang；Wentao Yan；Shuangfeng Wang
- raw_affiliation：均为 "Key Laboratory of Heat and Mass Transfer and Low-Carbon Conversion, Ministry of Education, School of Chemistry and Chemical Engineering, South China University of Technology, Guangzhou, 510640, China"
- DOI：10.1016/j.icheatmasstransfer.2026.112840；`created` 2026-10-13
- 数字：3.0 mm 厚；120 W–120 W 下启动 1051 s，比纯网芯对照在整个工况矩阵里短 5.8%–31.1%；190 W–190 W（共 380 W）最小总热阻 0.032 °C/W；280 W–60 W 不等载下局部峰值热流 58.33 W/cm²；75 °C 安全工作区面积比对照扩大 26.0%（100 °C 限值包络线基本一致）。
- URL：https://doi.org/10.1016/j.icheatmasstransfer.2026.112840

### 候选 11 · GaN 功率器件电场调控纳米 PCM
- 标题：Efficient thermal management of GaN power devices using electric-field-regulated nanoparticle-enhanced phase change materials
- 作者：Zirui Xu；Boyu Li；Dian Li；Jian Wu
- raw_affiliation：均为哈尔滨工业大学（"Heilongjiang Key Laboratory of Micro- and Nano-scale Fluid Flow and Heat Transfer" 与 "School of Energy Science and Engineering, Harbin Institute of Technology, Harbin, 150001, China"）
- DOI：10.1016/j.applthermaleng.2026.133567；`created` 2026-10-15
- 性质：**实验**，n-十八烷 + Al₂O₃ NePCM，热输入 2.4 W，电压 −15 到 +15 kV。
- 数字：0.02 vol.% Al₂O₃ 把完全熔化时间缩短 32.8%（9.67→6.50 h），但估算峰值结温无可测降低。施加 −10 kV 时对角双热源布局峰值结温由 109.7 降到 77.1 °C，峰值与平均红外表面温差减小近 10 °C。电极侧最大估算电功率 3.01 mW。
- URL：https://doi.org/10.1016/j.applthermaleng.2026.133567

### 候选 12 · 自驱两相冷却（多孔介质相变增压，无泵）
- 标题：A self-driven two-phase cooling method based on phase-change pressurization in porous media: Thermal and transport characteristics
- 作者：Rui Ma；Zehua Dong；Zhongwei Wang；Lin Wang；Shibin Li
- raw_affiliation：均为 "National Key Laboratory of Advanced Propulsion Technology, National University of Defense Technology, Changsha, Hunan, 410073, PR China"
- DOI：10.1016/j.applthermaleng.2026.133591；`created` 2026-10-14
- 数字：石英玻璃纤维毡毛细压力尺度 1.271 kPa，约为纳米气凝胶毡的 8.6 倍；填充质量 10 g 最优，有效控温持续 3500 s；相变增压与重力压力比约 4–24。热源 600 与 300 °C。
- 相关性：弱（高温、航空航天推进热管理，不是电子冷板）
- URL：https://doi.org/10.1016/j.applthermaleng.2026.133591

### 候选 13 · 蝉翼脉仿生电池液冷板（拓扑优化）
- 标题：Thermal–hydraulic design and multi-objective optimisation of a cicada-wing-vein-inspired liquid cooling plate for lithium-ion batteries（标题截断）
- 作者：Sen Zhan；Lei Yuan；Yonggang Liu；Shaojiang Dong；Junda Chen
- raw_affiliation：Zhan、Yuan、Dong、Chen 为 "School of Mechatronics and Vehicle Engineering, Chongqing Jiaotong University, Chongqing, 400074, China"；Zhan、Liu 另有 "State Key Laboratory of Mechanical Transmission for Advanced Equipment, Chongqing University, Chongqing, 400044, China"（Liu 仅此一条）。
- DOI：10.1016/j.ijheatfluidflow.2026.110749；`created` 2026-10-15
- 性质：仿真，正交设计、代理模型与 NSGA-II，再接拓扑优化。
- 数字：参数优化板相对初始仿生板，最高温降 1.79%，平均温降 1.39%，温度均匀性改善 13.28%，压降降 29.85%。拓扑优化板的数字在 3.5 g/s 下，摘要被截断未取到。
- URL：https://doi.org/10.1016/j.ijheatfluidflow.2026.110749

### 候选 14 · 无冷机双冷媒冷板集成热管理系统
- 标题：Design and Performance Evaluation of a Chiller-Free Integrated Thermal Management System Based on a Dual-Cooling-Media Cold P…（标题截断）
- 作者：待确认（未取）；raw_affiliation **取不到**；摘要 **取不到**
- DOI：10.1016/j.energy.2026.142688；`created` 2026-10-17
- URL：https://doi.org/10.1016/j.energy.2026.142688

---

### C. 中弱相关（备选）

15. **Tesla 阀微通道针肋参数研究**，ICHMT 10.1016/j.icheatmasstransfer.2026.112850，`created` 2026-10-15。作者 Ping Liu；Qiang Ke；Jun Wu；Han Zhou；Zhiwen Wang；Yi Jin。单位与摘要取不到。https://doi.org/10.1016/j.icheatmasstransfer.2026.112850
16. **机载间歇大功率电子设备 N-十五烷/膨胀石墨 PCM**，ICHMT 10.1016/j.icheatmasstransfer.2026.112845，`created` 2026-10-17。作者、单位、摘要均取不到。https://doi.org/10.1016/j.icheatmasstransfer.2026.112845
17. **PCM 圆柱热沉径向肋瞬态大热流（实验+仿真）**，ICHMT 10.1016/j.icheatmasstransfer.2026.112800，`created` 2026-10-12。Seok-Yong Lee（Konkuk Univ.）；Ju-Ho Jeong；Won-Woo Choi；J. Lee；Sung-Min Kim（Sungkyunkwan Univ. 为主）。20 片径向肋铝热沉加 n-二十烷，30 W 下达 50 °C 的时间由 7.1 增至 13.1 min（84%），50→35 °C 冷却时间由 32.8 增至 86.0 min，瞬态 Nu 关联式 R²=0.98、RMSE 1.98。https://doi.org/10.1016/j.icheatmasstransfer.2026.112800
18. **仿生梯度风冷翅片（径向槽）**，ICHMT 10.1016/j.icheatmasstransfer.2026.112874，`created` 2026-10-17。作者与摘要取不到。https://doi.org/10.1016/j.icheatmasstransfer.2026.112874
19. **R-1233zd(E) 上 gyroid 结构表面池沸腾**，ICHMT 10.1016/j.icheatmasstransfer.2026.112864，`created` 2026-10-15。Mohsen Khandan Bakavoli（单位 OpenAlex 未归入）；Wei-Han Huang（Rayvatek, Miaoli County, Taiwan）；Chi-Chuan Wang（Dept. of Mechanical Engineering, National Yang Ming Chiao Tung University, Hsinchu, Taiwan）。增材制造 TPMS gyroid，1 mm 与 1.2 mm 单元，1.5 bar 下低热流升热流段 HTC 比光滑铜面分别提高约 582% 与 183%。https://doi.org/10.1016/j.icheatmasstransfer.2026.112864
20. **超薄热管单层网芯毛细性能**，ICHMT 10.1016/j.icheatmasstransfer.2026.112803，`created` 2026-10-13。南京航空航天大学（Kehan Liu 等六位）。#100–#200 不锈钢网有效毛细半径 124.7–66.2 μm，修正系数 C=0.42 时偏差小于 3.6%。https://doi.org/10.1016/j.icheatmasstransfer.2026.112803
21. **复杂非凸微通道滑移流 MFS 无网格分析**，ICHMT 10.1016/j.icheatmasstransfer.2026.112820，`created` 2026-10-14。González（UTEM）、Díaz、Letelier、Cucumides（Universidad de Santiago de Chile）。500 个边界节点即得相对误差小于 0.03%，CPU 加速 35 倍。https://doi.org/10.1016/j.icheatmasstransfer.2026.112820
22. **纳米流体圆柱电池包扩散界面格子 Boltzmann**，ICHMT 10.1016/j.icheatmasstransfer.2026.112798，`created` 2026-10-11。Usama Habib；Xiaodong Wang；Hai Yu（均为 "School of Mathematics and Statistics, Northwestern Polytechnical University, Xi'an, 710129, China"）。加纳米颗粒后峰值电池温度仅降约 1 K。相关性弱。https://doi.org/10.1016/j.icheatmasstransfer.2026.112798
23. ICHMT 112715 / 112823 等其他条目：不相关或偏核电、PCHE，已排除。
24. **弯曲微通道滑移加肋腔复合结构**，IJTS 10.1016/j.ijthermalsci.2026.111432，`created` 2026-10-15。Yi Huang 等（Beihang University, Research Institute of Aero-Engine）。PEC 1.06–2.21。https://doi.org/10.1016/j.ijthermalsci.2026.111432
25. **背部集成风冷热沉对流—辐射耦合**，IJTS 10.1016/j.ijthermalsci.2026.111417，`created` 2026-10-14。Heng Zhang 等（China University of Geosciences, Beijing；Xiaohu Wu 为 Hubei University / Shandong Institute of Advanced Technology / Yangtze Laboratory）。入口 0.2 m/s、发射率 0.05→0.95 时，0.1 W 下最高芯片温度降约 10.8 °C，0.3 W 下降约 33.3 °C。https://doi.org/10.1016/j.ijthermalsci.2026.111417
26. **等离子体处理铜表面宏通道流动沸腾**，IJTS 10.1016/j.ijthermalsci.2026.111414，`created` 2026-10-15。Hamid Reza Mohammadi 等（Amirkabir University of Technology, Tehran；Shiraz University）。ONB 壁面过热度降 57–63%，HTC 增 127–155%，CHF 增 114–147%。https://doi.org/10.1016/j.ijthermalsci.2026.111414
27. **电子热管理双蒸发器冷却回路启动特性**，IEEE TCPMT 10.1109/tcpmt.2026.3742181，`created` 2026-10-12。Ruixue Yang；Chengcheng Fan；Zhiheng Zhu；Chengbin Zhang（OpenAlex 仅给 "Southeast University"，非出版商原串）。摘要取不到。相关性强（电子热管理环路），但无数字。https://doi.org/10.1109/tcpmt.2026.3742181
28. **TEC–热管–液冷混合电池热管理激活时机**，Energy 10.1016/j.energy.2026.142706，`created` 2026-10-14。Zihao Wu 等（Chang'an University；China Automotive Technology & Research Center, Tianjin）。5C 放电下混合系统最高温 316.38 K、温差 2.65 K（自然对流 366.09 K）；后置 TEC 激活使 COP 在 4C 与 3C 分别提高 15.1% 与 25.6%。https://doi.org/10.1016/j.energy.2026.142706
29. **高温热管**：CSTE 10.1016/j.csite.2026.108614，北航与航天五院钛—水 2 m 热管，20 °C 水冷非均匀冷却下输入 1300 W，相关性弱（航天）。
30. **IJHMT 窗口内弱相关**：两相热虹吸实验（10.1016/j.ijheatmasstransfer.2026.129675，核电事故被动散热背景，质量分数阈值 2.3%）；R134a 自然循环回路流动沸腾 CHF（129749，最大 HTC 16,145.5 W/m²·K，CHF 约 100–150 kW/m²）；超亲水钛面喷雾冷却（129739，作者与摘要未取到）。**IJHMT 本期没有冷板或微通道主题的强相关条目。**
31. **ATE 其他弱相关**：径向槽喷雾冷却（吉林大学，133624）、电池混合 PCM + 液冷三维热网络模型（UPPA 等，133587，78,000 种配置）。

### 规模提示
- 本期可直接作为冷板、微通道、功率模块液冷的强相关条目：候选 3、4、5、6、7、8、13（以及待补材料的 2、14）。
- 其中 2、4、5、14 摘要未取到，**必须经 verifier 复核才能写数字**。
- 摘要里的数字全部来自出版商摘要，不是论文正文数据。
