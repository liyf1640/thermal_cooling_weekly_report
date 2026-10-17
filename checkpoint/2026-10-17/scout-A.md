# scout A · 冷板仿真与设计（原样回传）

窗口 2026-10-11~10-17，按 Crossref `created` / arXiv v1 判窗。
取数说明：sciencedirect、nature.com 等出版商站点被代理拒绝（403 / ENOTFOUND）。摘要和单位来自 Crossref + OpenAlex（`abstract_inverted_index` 与 `raw_affiliation_strings`）。OpenAlex 的单位是整篇的机构串集合，不一定逐作者对应。`fetch_source.py` 对 DOI 只返回 Crossref 元数据，基本没有摘要。
已扫：arXiv API 按 cold plate / microchannel / heat sink / liquid cooling / flow boiling / jet impingement / conjugate heat transfer / topology optimization / neural operator 查询，Crossref 按期刊 ISSN（IJHMT、ATE、ICHMT、IJTS、ECM、IJHFF）直扫，另做关键词扫描。IJHMT 的 ISSN 扫描只回了 15 条上下，疑似不全。

## 一、上期挂账三项（三项首发 created 均在窗口外，属上期尾巴，非本窗新增）

### 挂账1 · 新月形针肋 vs 光滑小通道流动沸腾
- 标题：A comparative study of flow boiling heat transfer and pressure drop in crescent pin-fin and smooth minichannel heat sinks
- 作者（Crossref 原文串）：Fadi Alnaimat; Abdul Hanan; Bobby Mathew。OpenAlex 的作者名为 Abdul Hanan Muhammad Zaheer，两处不一致，需 verifier 看原文。
- 单位（OpenAlex 原始串）：Mechanical and Aerospace Engineering Department, College of Engineering, United Arab Emirates University, 15551 Al Ain, Abu Dhabi, United Arab Emirates；另有 National Water and Energy Center, United Arab Emirates University（Alnaimat、Mathew）
- 期刊：Int. Commun. Heat Mass Transf.；DOI 10.1016/j.icheatmasstransfer.2026.112763
- Crossref created：2026-10-03，窗口外（issued 2026-11 是卷期）
- 内容：**实验**，去离子水，入口温度 80 °C，质量流速 180–360 kg/m²·s，热流密度 15.45–100.59 kW/m²，带高速摄影。新月形针肋表面最大 HTC 约 12–12.5 kW/m²·K，光滑表面同条件约 7–7.2 kW/m²·K。针肋压降更高，但压力波动更小、流动更稳。
- URL：https://doi.org/10.1016/j.icheatmasstransfer.2026.112763
- 判断：摘要和单位来自 OpenAlex（出版商页取不到），可信度中高。窗口外，不能按本窗新增算。它是小通道（minichannel）而非冷板，热流密度只到 100 kW/m²（约 10 W/cm²），数据中心相关性弱到中。

### 挂账2 · 编码波纹并联微通道
- 标题：Encoded corrugation design for flow redistribution and thermohydraulic performance enhancement in parallel microchannels
- 作者（Crossref）：Yili Zhou; Ping Xu; Jie Xing; Shuguang Yao
- 单位：取不到（Crossref 和 OpenAlex 均为空）
- 期刊：Int. Commun. Heat Mass Transf.；DOI 10.1016/j.icheatmasstransfer.2026.112814
- Crossref created：2026-10-09，窗口外
- 摘要：取不到（Crossref 和 OpenAlex 均无），性能数字取不到，不推定。
- URL：https://doi.org/10.1016/j.icheatmasstransfer.2026.112814
- 判断：仍无法写进周报正文，只能写标题级信息。窗口外。

### 挂账3 · Nature Electronics 水平向上微流体
- 标题：Horizontal-up microfluidics for embedded chip cooling with a dielectric fluid
- 作者（Crossref）：Wei Xiao; Zhihu Wu; Zhiyao Jiang; Yuxi Wang; Wei Wang; Bai Song
- 单位（OpenAlex 原始串）：National Key Laboratory of Advanced Micro and Nano Manufacture Technology, Peking University, Beijing, China；School of Mechanics and Engineering Science, Peking University（Xiao、Wu、Jiang、Wang Yuxi、Song）；School of Integrated Circuits, Peking University（Wang Wei）
- 期刊：Nature Electronics；DOI 10.1038/s41928-026-01724-y
- published-online / created：2026-10-07 / 2026-10-07T09:02:56Z，窗口外
- 摘要：一手摘要仍取不到（Crossref 和 OpenAlex 均无）。
- 性能数字：WebSearch 返回的二手新闻稿称介质为 HFE-7100，临界热流密度（CHF）1,570 W/cm²，设计为水平入口加竖直出口。新闻稿原文页（interestingengineering.com、globalsources.com）打不开，只见到搜索摘要。其中一家是聚合站，可能含 AI 改写。**该数字未经一手核验，写稿前必须核。**
- 关于 "HU"：Crossref 标题是 "Horizontal-up microfluidics"，二手稿描述为水平入口加竖直出口，与 horizontal-up 吻合。**"HU" 作为缩写的定义出自论文正文，未取到，不能确认。**
- URL：https://doi.org/10.1038/s41928-026-01724-y
- 判断：期刊和单位可信。窗口外。数字可信度低，待核。

## 二、窗口内候选（created 在 10-11~10-17）

### 候选1 · 微通道热沉两层降阶模型 VTLM（arXiv）
- 标题：Versatile two-layer model for thermohydraulic prediction of microchannel heat sinks
- 作者：Chih-Hsiang Chen; Kentaro Yaji
- 单位：arXiv 元数据无单位，取不到
- arXiv:2610.16716（v1 提交 2026-10-12）
- 内容：把 3D 共轭传热问题降为两个耦合的 2D 场，保留面内流道和翅片几何，通道高度方向用水力和热闭合项补偿。对照 3D 参考模型，在多种宽高比和工况下评估，含均匀和非均匀翅片以及扩张-收缩通道，比既有两层模型整体吻合更好。给出直通道的保守筛选准则。摘要无加速比数字。
- URL：https://arxiv.org/abs/2610.16716
- 判断：已 fetch_source 取摘要，窗口内，去重清单未命中。相关性强：ROM / 共轭传热降阶，可直接用于拓扑优化和代理建模的低成本评估。arXiv 预印本，未经评审。

### 候选2 · SiC IGBT 双面液冷微通道分区拓扑优化
- 标题：Zoned topology optimization of double-sided liquid-cooled microchannel heat sinks for the thermal management of SiC IGBT modules
- 作者：Hanyang Xu; Yifan Wang; Wenchao Tian; Feiyang Li; Han Shen; Daowei Wu
- 单位（OpenAlex）：School of Electro-Mechanical Engineering, Xidian University, Xi'an；State Key Laboratory of Electromechanical Integrated Manufacturing of High-Performance Electronic Equipments, Xidian University；Daowei Wu 单位为 National Key Laboratory of Integrated Circuits and Microsystems, China
- 期刊：ICHMT；DOI 10.1016/j.icheatmasstransfer.2026.112802；created 2026-10-13
- 内容：**ANSYS Fluent 仿真**。进口区、高温设计域、出口设计域三区分区拓扑优化。相对常规直通道 MCHS，综合热性能因子提升 114–187%。TOPO_20 使 IGBT 模型平均温度降 3.62 K，SiC 结温平均降 6.41 K，封装峰值热应力降 72.76 MPa。
- URL：https://doi.org/10.1016/j.icheatmasstransfer.2026.112802
- 判断：窗口内，去重清单未命中。摘要来自 OpenAlex（摘要末尾被截断，不影响上述数字）。相关性强（拓扑优化加微通道液冷，电力电子）。仿真，无实验。

### 候选3 · 电池冷板拓扑设计的两阶段 cGAN-岭回归代理
- 标题：Two-stage cGAN-ridge surrogate for battery cold plate topology design
- 作者：Puneeth D. Shetty; Akhil Garg; Nguyen Phi Long; Hai Hung Pham; Jonghoon Kim; Kexiang Wei
- 单位（OpenAlex）：Shetty — Dept of Mechanical Engineering, National Institute of Technology Calicut, Kerala, India；Garg — Xi'an Jiaotong-Liverpool University, Suzhou；Nguyen、Pham — Vin University / Hanoi University of Industry, Viet Nam；Kim — Chungnam National University, Daejeon, South Korea；Wei — Hunan Institute of Engineering, Xiangtan
- 期刊：Applied Thermal Engineering；DOI 10.1016/j.applthermaleng.2026.133314；created 2026-10-12
- 内容：FiLM 条件 cGAN 由工况生成拓扑、温度、压力场，256×256 约 35 ms。71 个留出样本：拓扑 IoU 0.704，温度 SSIM 0.692。连通性成立 57/71，压力单调性均值 66.9%。第二阶段 Ridge 排序温度目标 R²=0.311–0.607，Spearman ρ=0.761–0.830，**压降预测失败（R²=−0.009）**，压降改由 CFD 校验。论文自承「2–3/20 候选进 CFD」的减算量目标尚未对照全 CFD 排序验证。
- URL：https://doi.org/10.1016/j.applthermaleng.2026.133314
- 判断：窗口内，未命中去重。摘要来自 OpenAlex。相关性中到强（生成式设计加代理，但对象是电池冷板，且论文自陈局限明显）。

### 候选4 · 激光器制冷剂冷板的数据高效多目标结构优化
- 标题：Data-efficient multi-objective structural optimization and design space exploration of refrigerant-based cold plate for laser device
- 作者：Qingwen Gui; Youwei He; Jiangshuo Cui; Yong Chen; Chaochao Zhou
- 单位、摘要：取不到（OpenAlex 请求失败，Crossref 无）
- 期刊：Applied Thermal Engineering；DOI 10.1016/j.applthermaleng.2026.133678；created 2026-10-17
- URL：https://doi.org/10.1016/j.applthermaleng.2026.133678
- 判断：窗口内，未命中去重。仅标题级信息，无法写数字，需 verifier 复核。相关性强（制冷剂冷板，代理优化）。

### 候选5 · 肋-互连微通道热沉（数值）
- 标题：Numerical study on thermo-hydraulic performance of rib-interconnected microchannel heat sink
- 作者：Xiuxian Zou; Hui Deng; Leyong Jiang; Wangbing Yu; Xiaohu Wu
- 单位（OpenAlex 整篇机构串，非逐作者对应）：School of Integrated Circuits, Hubei University, Wuhan；School of Physics and Electronics, Hunan Normal University, Changsha；Thermal Science Research Center, Shandong Institute of Advanced Technology, Jinan；Yangtze Laboratory, Wuhan
- 期刊：ICHMT；DOI 10.1016/j.icheatmasstransfer.2026.112881；created 2026-10-16
- 内容：**数值**。Re 92–829。三角肋方案（case 8）在 Re=829 时：最高基底温度降 12.65 K，HTC 提高 129.36%，温度不均匀度降 65.80%，PEC 1.99，最大热流容量 132.01 W/cm²（相对增幅被截断，未读到）。
- URL：https://doi.org/10.1016/j.icheatmasstransfer.2026.112881
- 判断：窗口内，未命中去重。相关性中，属通道强化，不是冷板系统级设计。摘要为 OpenAlex 的截断版。

### 候选6 · 肋-腔耦合微通道（恒流体域体积）
- 标题：Effect of coupled ribs and cavities on the hydrothermal comprehensive performance of microchannels under constant fluid domain volume
- 作者：Wenling Liao; Zhengbiao Jing; Shuaimei Lian; Fenghao Chen; Ao Li; Yuhan Xu; Pingping Liu
- 单位（OpenAlex 整篇串）：Chengdu Vocational & Technical College of Industry, Chengdu；School of Mechanical Engineering, Chengdu Technological University, Chengdu
- 期刊：ICHMT；DOI 10.1016/j.icheatmasstransfer.2026.112861；created 2026-10-14
- 内容：**数值**，Re 355–1065。五种构型，DLMC-SRCS 平均综合性能 η 超过 1.8，Re=533 时峰值 1.847。
- URL：https://doi.org/10.1016/j.icheatmasstransfer.2026.112861
- 判断：窗口内，未命中去重。相关性中。

### 候选7 · 多射流冲击微通道热沉加被动结构（CFD）
- 标题：CFD analysis of multi-jet impingement microchannel heat sink integrated with passive structures
- 作者：Jyoti Pandey; Mohd. Zahid Ansari; Shivanku Chauhan; Mangal Singh Lodhi
- 单位（OpenAlex 整篇串）：Department of Mechanical Engineering, Shri G S Institute of Technology and Sciences, Indore；MEMS and Microfluidics Lab, PDPM-IIITDM Jabalpur；R V Institute of Technology, Bijnor, Uttar Pradesh（均印度）
- 期刊：J. Therm. Anal. Calorim.；DOI 10.1007/s10973-026-16341-2；created / published 2026-10-13
- 摘要与数字：取不到
- URL：https://doi.org/10.1007/s10973-026-16341-2
- 判断：窗口内，未命中去重。仅标题级，相关性中（射流加微通道）。

### 候选8 · 圆弧桥针肋混合微通道热沉（热点）
- 标题：Localized hotspot mitigation using a hybrid microchannel heat sink with alternating-orientation arched-bridge pin-fins
- 作者：Xinglan Hou; Yongheng Yang
- 单位、摘要：取不到
- 期刊：Applied Thermal Engineering；DOI 10.1016/j.applthermaleng.2026.133571；created 2026-10-16
- URL：https://doi.org/10.1016/j.applthermaleng.2026.133571
- 判断：窗口内，未命中去重。仅标题级，相关性中。

### 候选9 · 低优先级，仅列标题（均只取到 Crossref 元数据，作者来自 Crossref，单位取不到）
- ATE 133591「A self-driven two-phase cooling method based on phase-change pressurization in porous media」：Rui Ma 等，国防科技大学（OpenAlex）。created 2026-10-14。10.1016/j.applthermaleng.2026.133591。**实验**，热源 600 / 300 °C，QGFF 10 g 填充使温控时间达 3500 s。自驱两相，非电子冷板量级，相关性弱。https://doi.org/10.1016/j.applthermaleng.2026.133591
- ICHMT 112850「Parametric study of pin fin structures for enhanced heat transfer in tesla valve microchannels」：Ping Liu; Qiang Ke; Jun Wu; Han Zhou; Zhiwen Wang; Yi Jin，created 2026-10-14，摘要取不到。https://doi.org/10.1016/j.icheatmasstransfer.2026.112850
- IJHFF 110749「cicada-wing-vein-inspired liquid cooling plate for lithium-ion battery」：Sen Zhan 等，created 2026-10-15，摘要取不到，电池冷板，相关性中。https://doi.org/10.1016/j.ijheatfluidflow.2026.110749
- IJTS 111417「Coupled convection–radiation heat transfer and optimization in microscale fin structures」（Heng Zhang 等，created 2026-10-14）和 IJTS 111432「Curvature-modulated slip effects … structured microchannels」（Yi Huang 等，created 2026-10-16）：仅标题，相关性弱。
- IJHMT 129692「Fast prediction of surface-temperature fields based on the thermal response function method」（Yongwang Gao 等，created 2026-10-13）：快速温度场预测，与 ROM 有方法学关联，摘要取不到，相关性弱到中。
- Eng. Res. Express「From Topology Optimisation to Topology-Informed Heat Sink Geometries」（Tekavit、Tezel、Kovan，Akdeniz University，created 2026-10-14，DOI 10.1088/2631-8695/aeb485）：8 种 AlSi10Mg 拓扑启发散热器**纯数值**，对比商用散热器最高温差 7.04–45.78 °C。**自承无网格无关性、无实验验证，风冷散热器非冷板**，相关性弱。https://doi.org/10.1088/2631-8695/aeb485
- SSRN 预印本 10.2139/ssrn.7596080「Lifecycle-Aware Topology Optimization of Liquid-cooled Fusion Reactor Divertors」（Samuel Schlicht，created 2026-10-12）：W/CuCrZr 偏滤器，q″=20 MW/m²，Δp=50 kPa，1000 h。聚变领域，**非电子散热**，相关性弱，仅作方法学参考。https://doi.org/10.2139/ssrn.7596080

## 三、本期未检出
- 窗口内无新的 arXiv 冷板、歧管微通道 MMC、两相沸腾冷板、生成式扩散模型冷板论文（arXiv API 对相关查询仅命中 2610.16716；2610.11108 Cova-PINN 为已报）。
- Crossref 期刊直扫未发现窗口内的歧管微通道（manifold）专题论文。ISSN 扫描只可靠覆盖到标题层面，建议 verifier 对 IJHMT 再补扫。
- 数据中心液冷方向，arXiv 本窗命中为电网和运营类（与冷板设计无关），不收。
