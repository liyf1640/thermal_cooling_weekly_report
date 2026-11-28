# scout-A · 冷板仿真与设计（原样回传）

扫描范围：Crossref 按 created 扫 IJHMT、ATE、ICHMT、IJTS、ECM、Exp. Therm. Fluid Sci. + 关键词全库查询（cold plate / microchannel heat sink / jet impingement / thermal resistance）；OpenAlex 取摘要与机构；**arXiv API 本次返回为空，arXiv 这一路本期未覆盖**。
所有 Elsevier 条目摘要均未从出版商页核，只有 OpenAlex 摘要或零摘要。作者单位多来自 OpenAlex（非出版商原串）。

## 一、窗内新增候选

### 候选 1 · 仿生分级冷板的伴随法优化与硅片实物制造
- 标题：In silico design and fabrication of biomorphic cold plates for chip cooling
- 作者/单位：Nikolaos Cavadias; Matei C. Ignuta-Ciuncanu; Ricardo Martinez-Botas。依 OpenAlex：Imperial College London（Ignuta-Ciuncanu 另挂 UC Berkeley）。出版商原串待确认。
- 日期：Crossref created 2026-11-26
- 关键数字：峰值基底温度 336.0 K → 325.6 K，相对 300 K 入口的温升降低 29%（基准：同流体体积分数、同入口条件、同功率图的直通道）；飞秒激光微加工硅片，面内尺寸复现偏差约 ±30 μm
- 相关性：强 —— 热点感知拓扑优化（FEniCS 伴随灵敏度），走完「优化→CAD→硅片制造」全链路
- 去重：新增
- 来源：https://doi.org/10.1016/j.icheatmasstransfer.2026.113204
- 核验状态：仅 OpenAlex 摘要，需核

### 候选 2 · 分块式歧管头 + TPMS 芯体两阶段拓扑优化
- 标题：Sequential partitioned design of heat sink headers and TPMS cores via two-stage topology optimization for enhanced thermo-fluid performance
- 作者/单位：Zhichao Men; Wenjiong Chen; Jilang Xiong; Yang Li。OpenAlex 仅给 Men、Chen 为 Dalian University of Technology，其余待确认
- 日期：created 2026-11-27 · 关键数字：**摘要零获取**
- 相关性：中（是否面向电子冷板需摘要确认）· 去重：新增（与已报「功能梯度 TPMS 热沉」不同篇，同题材）
- 来源：https://doi.org/10.1016/j.icheatmasstransfer.2026.113259

### 候选 3 · 嵌入近结微通道冷却的 GaN HEMT 电热联合表征
- 标题：Electrothermal co-characterization of high-power GaN HEMT with embedded near-junction microchannel cooling
- 作者：Yu He; Mengkai Jia; Shuhui Liang 等（Crossref 只列前三）；单位待确认（OpenAlex 无）
- 日期：created 2026-11-28 · 关键数字：**摘要零获取**
- 相关性：中（可能涉结温/热阻测量）· 来源：https://doi.org/10.1016/j.icheatmasstransfer.2026.113229

### 候选 4 · 金刚石歧管微通道不同通道构型对比
- 标题：Comparative study on heat dissipation performance of diamond manifold microchannels under different channel configurations
- 作者/单位：OpenAlex：Xuan Diao、Zheyu Fang、Xiaohu Wu，Hubei University（其余待确认）
- 日期：created 2026-11-22 · 关键数字：**摘要零获取** · 相关性：强（MMC）
- 来源：https://doi.org/10.1016/j.icheatmasstransfer.2026.113215

### 候选 5 · 带嵌入金属针肋的 LTCC 微通道热沉
- 标题：Enhanced Cooling Performance of LTCC Microchannel Heat Sink With Embedded Metal Pin Fins
- 作者/单位：Lili Zhang; Zhensong Li; Han Wang; Lili Cao。Crossref 机构串：School of Information and Communication Engineering, Beijing Information Science and Technology University, Beijing, China
- 日期：published-online 2026-11-27
- 关键数字：10/15/20 W 热负荷下中心最高温度分别降 23.55% / 19.78% / 17.18%（相对无针肋模型）；仿真与实验相对误差 1.15%–8.13%
- 相关性：中（热负荷量级小 ≤20 W）· 来源：https://doi.org/10.1002/jtse.70014

### 候选 6 · 针肋歧管微通道多目标优化（RSM + NSGA-II + TOPSIS）
- 标题：Multiobjective Optimization and Thermal–Hydraulic Performance of Pin-Finned Manifold Microchannel fo…（Crossref 标题截断，完整标题待确认）
- 作者/单位：Yitao Shi; Aili Zhang。Crossref 机构串：School of Mechanical and Equipment Engineering, Hebei University of Engineering, Handan, China；Key Laboratory of Intelligent Industrial Equipment Technology of Hebei Province
- 日期：published-online 2026-11-24
- 关键数字：加热面温度 61.05–86.88 °C、压降 2.24–2.57 kPa（Pareto 前沿）；TOPSIS 最优为加热面 62.75 °C、压降 < 2.40 kPa。**热流密度等基准条件摘要中未见，待核**
- 相关性：强 · 来源：https://doi.org/10.1002/htj.70429

### 候选 7 · 直触芯片蒸发冷却：液体输送层对流量失配与热性能的影响
- 标题：Direct-to-chip evaporative cooling: Effect of liquid delivery layer on flow maldistribution and thermal performance
- 作者/单位：Kidus Guye; Vivek V. Manepalli; Ayşenur Ateş; Samuel Lindsay Graham; Damena D. Agonafer。依 OpenAlex：University of Maryland, College Park
- 日期：created 2026-11-25
- 关键数字：LDL 高度 15 μm → 90 μm，流量失配降低 >40×（R-1336mzz(Z)，2 kW）、最高 32×（水，5 kW）；疏水面比亲水面基底温度高 22 °C（同热负荷）
- 相关性：强（中空微柱阵列两相蒸发式直触芯片冷板，实验+数值）
- 去重：新增（与已报「微柱阵列两相直触蒸发冷板回路网络+ML」可能同组/同技术线，非同篇，需判）
- 来源：https://doi.org/10.1016/j.applthermaleng.2026.134123

### 候选 8 · 开口梯形微通道加透气膜排汽的流动沸腾
- 类型：会议（IEEE CENCON 2026）· 标题：Flow boiling enhancement using a vapor venting membrane for high-power electronics cooling
- 作者/单位：Md Danish Eqbal; Manabendra Pathak; Mohd. Kaleem Khan。Crossref 机构串：Indian Institute of Technology Patna
- 日期：created 2026-11-25
- 关键数字：6 条开口梯形微通道；去离子水，过冷度 20 °C，质量流速 535 kg/m²s，热流密度 20–220 W/cm²。排汽后壁温降低、压降与壁温/压力波动受抑制。**摘要未给降幅数字**
- 相关性：中 · 来源：https://doi.org/10.1109/cencon70655.2026.11804424

### 候选 9 · 面向 AI 服务器的瞬态热管理（数据驱动优化 + 硬件在环验证）
- 标题：Transient thermal management of the high-heat-flux AI server: Data-driven optimization and hardware-in-the-loop validation
- 作者/单位：OpenAlex 前几位：Xingyang Niu（Beijing University of Technology；National Institute of Metrology）、Wei Zhang（National Institute of Metrology）、Fang Ye（BJUT）、Qingfei Shen（NIM）。出版商原串待确认
- 日期：created 2026-11-26 · 关键数字：**摘要零获取** · 相关性：弱~中
- 来源：https://doi.org/10.1016/j.ijheatmasstransfer.2026.129960

### 候选 10 · 间断肋与空腔微通道热-水力数值研究
- 标题：Numerical thermal-hydraulic study of microchannels with interrupted fins and cavities
- 作者/单位：OpenAlex：Kaihua Zhang; Kunyan Wang; Bilin Dong; Yue Wang（Henan Normal University）
- 日期：created 2026-11-26 · 关键数字：**摘要零获取** · 相关性：中
- 来源：https://doi.org/10.1016/j.applthermaleng.2026.134111

### 候选 11 · 全金刚石交错六边形针肋微通道热沉
- 标题：Investigation on an All-Diamond Staggered Hexagonal Pin-Fin Microchannel Heat Sink for High-Heat-Flu…（标题截断）
- 作者/单位：OpenAlex：Mingxue Li; Zhihao Zhang; Yufeng Zhang; Jiahui Luo（Harbin Institute of Technology）
- 日期：created 2026-11-24 · 关键数字：**摘要零获取** · 相关性：中
- 来源：https://doi.org/10.1016/j.energy.2026.143227

### 候选 12 · 液态金属三角肋-针肋复合多射流微通道数值分析
- 标题：Numerical analysis of heat transfer performance in liquid-metal triangular fin and pin fin composite multi-jet microchannel systems
- 作者：Chunquan Li; Rui Zhang; Yuling Shang（Crossref 只列前三）；单位待确认
- 日期：created 2026-11-28 · 关键数字：**摘要零获取** · 相关性：中
- 来源：https://doi.org/10.1016/j.ijthermalsci.2026.111516

### 候选 13 · 数据中心用固-固相变材料热沉的协同设计（边缘相关）
- 标题：Co-designed solid–solid PCM heat sinks for transient thermal management in data centers
- 作者/单位：Prashant Saini; Julian David Osorio; Munjal Purnkant Shah 等。依 OpenAlex：National Laboratory of the Rockies（其余待确认）
- 日期：created 2026-11-25
- 关键数字：OpenAlex 摘要前半只描述研究内容（脉冲热负荷下 SS-PCM 热沉的几何与材料协同设计），**未获取到数字结果**
- 相关性：弱（PCM 无源热沉，非液冷冷板）· 来源：https://doi.org/10.1016/j.ijheatmasstransfer.2026.129948

## 二、上期挂账 DOI 重试结果（created 均在 11-16~11-20，窗外）

### 候选 14 · 正弦中尺度通道冷板针肋的分离分析（OVHcloud × Reims）
- 类型：会议（THERMINIC 2026）· 标题：Why the Optimal Pin-Fin Geometry Depends on the Operating Point: A Separation-Based Analysis of Sinusoidal Meso-Channel Cold Plates
- 作者/单位（**Crossref 机构串**）：Mahdi Vahidi（OVHcloud / University of Reims Champagne-Ardenne）; Hadrien Bauduin（OVHcloud）; Michael Maalouly（OVHcloud）; Ali Chehade（OVHcloud）; Fabien Bogard（ITheMM, University of Reims Champagne-Ardenne）; Chadi Maalouf（ITheMM, University of Reims Champagne-Ardenne）
- 日期：Crossref created 2026-11-19（窗外）
- 关键数字：15 种构型，共轭传热 CFD；压降正比于瓶颈流速的 **2.10 次方**；流量 **0.4–0.8 L/min** 区间内，排名前六的构型**排序几乎完全反转**
- 相关性：强 · 来源：https://doi.org/10.1109/therminic70452.2026.11779811

### 候选 15 · SmartFins skived 热沉流动再分配（MegaCool）
- 类型：会议（THERMINIC 2026）· 标题：Enabling Flow Redistribution in Skived Heat Sinks for High-Power Density Computing: An End-to-End Case Study
- 作者/单位（**Crossref 机构串**）：Ine Vandebeek（MegaCool Technologies）; Lieven Vervecken（MegaCool Technologies）; Rui Vieira（MegaCool Technologies）
- 日期：created 2026-11-19（窗外）
- 关键数字：3 种设计实验测试；相对商用参考**热阻降低 47%**；背景热流密度 **>200 W/cm²**，热点接近 **600 W/cm²**
- 相关性：强（生成式设计 + 兼容铜 skived 制造的 CHT 验证冷板）· 来源：https://doi.org/10.1109/therminic70452.2026.11779752

### 候选 16 · LPBF 铜-石墨烯复合材料（弱相关）
- 标题：Laser Powder Bed Fusion of Copper-Graphene Metal Matrix Composites for Enhanced Heat Transfer
- 作者/单位：Wessel W. Wits; Hyunjong Lee; Leonore van Goor; Bernard Geurts; Davoud Jafari。Crossref 机构串：University of Twente（Wits 等四人另标 Mathematics and Computer Science）
- 日期：created 2026-11-19（窗外）· 关键数字：摘要仅称加入石墨烯可恢复 LPBF 过程损失的热导率，**未给具体数值**
- 相关性：弱 · 来源：https://doi.org/10.1109/therminic70452.2026.11779771

### 仍无摘要的挂账 DOI（标题+作者可核，摘要零获取，不得编摘要）
均 Elsevier，Crossref 与 OpenAlex 均无摘要，created 均在窗外：
- 10.1016/j.applthermaleng.2026.134045（created 11-19）拓扑优化小通道冷板+节流结构；Zeran Han; Jingkai Ma; Xiaohong Yan; Min Zeng; Ting Ma（Xi'an Jiaotong University，依 OpenAlex）
- 10.1016/j.energy.2026.143202（11-20）开放式微通道冷板 for AI 服务器；Bo Liu 等（Shandong University；Jinbo Li 为 Inspur (China)）
- 10.1016/j.ijheatmasstransfer.2026.129918（11-19）CuIO 涂层歧管微通道；Seungjae Lee 等（Chung-Ang / ETRI / Stanford / Hongik / Sungkyunkwan）
- 10.1016/j.ijheatmasstransfer.2026.129866（11-16）高功率芯片相变冷却结构设计；Shengxian Huang 等
- 10.1016/j.ijheatmasstransfer.2026.129924（11-17）超低压降微通道热沉；Anish Ojha 等（Institute of Chemical Technology）
- 10.1016/j.ijthermalsci.2026.111493（11-17）MicroChanNet；Jinfeng Zhao 等（Institute of Microelectronics, CAS）
- 10.1016/j.ijthermalsci.2026.111490（11-18）射频芯片 PCM+变截面微通道；Bo Xu; Ci Ao; Xin Wang; Zhenqian Chen（Southeast University）

## 三、窗内但判定不收或仅列名
- 10.1016/j.ijthermalsci.2026.111525（11-23）动力电池冷板，非电子/数据中心 → 不收
- 10.1016/j.icheatmasstransfer.2026.113092（11-25）微通道换热与压降综述，NIT Srinagar，摘要零获取 → 弱相关背景
- 10.1016/j.applthermaleng.2026.134127（11-24）服务器热环境 POD 快速预测，摘要零获取，偏机房气流 → 弱
- 10.1016/j.applthermaleng.2026.134169（11-27）Bi2Te3 热电制冷阵列多热点芯片热管理，非冷板 → 仅列名
- 10.1016/j.icheatmasstransfer.2026.113218（11-26）IGBT 模块结温估计方法综述，属电学法 → 仅列名
- 10.1016/j.icheatmasstransfer.2026.113167（11-24）mini 通道热沉入出口布置优化，Mustansiriyah University，摘要零获取，应用对象未知 → 不收
- 10.1080/01457632.2026.2762696（11-23）叠层双层微通道+Al2O3 纳米流体 CHT，National Cheng Kung University。数字：总流量 38.77 cm³/min、流量分配比 0.5 时叠层整体换热系数较单层最高提高 19.19%（纯水）→ 弱相关
- 10.1007/s00231-026-03827-w（11-26）表面粗糙度对微通道流动沸腾的影响，摘要零获取，是否面向电子散热未知 → 不收
- 10.1109/tpel.2026.3757968（11-26）风冷热沉质量体积与热阻数据驱动模型 → 风冷，不在冷板范围

## 四、本期未检出项
- **原位测量与表征**（in-situ thermal resistance / junction-to-coolant / 嵌入式传感器 / BLT / TIM BLT）：窗内**未检出明确的原位热阻/BLT 测量论文**（仅候选 3 GaN 电热表征待摘要确认、IGBT 结温综述仅列名）
- **arXiv**（physics.flu-dyn、cs.CE）：API 返回为空，本期**未覆盖**
- 生成式设计（扩散/GAN/VAE）：窗内仅见与冷板无关的 ATE 134061（窑炉燃烧）→ 不收
- 神经算子/代理模型：窗内仅见 IJHMT 129920（蒸汽发生器螺旋管，非冷板）→ 不收
- Energy Conversion & Management：窗内无相关条目
