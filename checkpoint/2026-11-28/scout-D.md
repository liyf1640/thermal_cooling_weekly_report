# scout-D · 英文期刊 in-press / online-first 专项（原样回传）

判窗用 Crossref created。**所有 Elsevier 条目的 published-online 字段 Crossref 均为空，故只能写「无」。**
方法：Crossref journals 端点按 created 筛 11 个刊（0017-9310、1359-4311、0196-8904、1290-0729、0735-1933、0142-727X、1948-5085、0360-5442、2214-157X、0306-2619、2072-666X），再逐条取 Crossref/OpenAlex 单篇。
TCPMT（1557-9972）窗内 0 条；Applied Energy、ECM、IJHFF、Case Stud. Therm. Eng. 标题筛后无相关条目。
**Crossref 的 Elsevier 作者列表无单位字段 → 一律「待确认」。** 已对去重清单查过，下列条目均不在其中。

## A. 摘要已取到（OpenAlex 或 Crossref），可核内容

### 候选 1 · 生物形(biomorphic)冷板：伴随法拓扑优化 + 飞秒激光硅片制造
- 刊：Int. Commun. Heat Mass Transfer · 标题：In silico design and fabrication of biomorphic cold plates for chip cooling
- 作者：Nikolaos Cavadias; Matei C. Ignuta-Ciuncanu; Ricardo F. Martinez-Botas；**单位待确认**
- 内容：FEniCS 伴随灵敏度梯度优化，在非均匀芯片功率图、固定流体体积下得到分级分支网络；转 CAD 后在硅上飞秒激光加工
- 关键数字（OpenAlex 摘要）：对比同流体分数直通道，峰值底面温度 **336.0 K → 325.6 K**（入口 300 K，**温升降 29%**）；制造面内尺寸复现约 **±30 μm**
- DOI：10.1016/j.icheatmasstransfer.2026.113204 · https://doi.org/10.1016/j.icheatmasstransfer.2026.113204
- Crossref created **2026-11-26**；published-online 无 · 摘要途径：OpenAlex（Crossref 无）
- 相关性：强（冷板拓扑优化 + 实物制造）· 去重：新增

### 候选 2 · 直接芯片蒸发冷却：液体分配层对流量不均的影响
- 刊：Applied Thermal Engineering · 标题：Direct-to-chip evaporative cooling: Effect of liquid delivery layer on flow maldistribution and thermal performance
- 作者：Kidus Guye; Vivek V. Manepalli; Ayşenur Ateş; Samuel Graham; Damena Agonafer；**单位待确认**
- 内容：空心微柱阵列蒸发冷却（DCEC）+ 液体分配层（LDL），实验加数值
- 关键数字（摘要）：疏水表面比亲水表面在同热负荷下基底温度高 **22 °C**；LDL 高度 **15→90 μm**，流量不均降低：R-1336mzz(Z) **2 kW** 时 **>40×**，水 **5 kW** 时最高 **32×**
- DOI：10.1016/j.applthermaleng.2026.134123 · Crossref created **2026-11-25**；published-online 无 · 摘要途径：OpenAlex
- 相关性：强（芯片级两相冷却）· 去重：新增

### 候选 3 · 固-固相变材料(PCM)散热器：数据中心瞬态热管理（数值）
- 刊：Int. J. Heat Mass Transfer · 标题：Co-designed solid–solid PCM heat sinks for transient thermal management in data centers
- 作者：Prashant Saini; Julian D. Osorio; Munjal P. Shah；**单位待确认**
- 关键数字（摘要）：固定 PCM 质量 **60 g**；风车形棱柱翅片应用型指标 **TPI 0.914**，基线针翅 **0.391**；**14/14 双面板构型**相对基线针翅峰值源温降约 **23 K**、恢复时间缩短约 **79%**
- DOI：10.1016/j.ijheatmasstransfer.2026.129948 · created **2026-11-25**；published-online 无 · 摘要途径：OpenAlex
- 相关性：中（被动 PCM 散热器，非液冷冷板；纯数值）· 去重：新增

### 候选 4 · LTCC 微通道散热器嵌金属针翅
- 刊：J. Thermal Science and Engineering Applications（ASME 刊，Wiley 平台）· 标题：Enhanced Cooling Performance of LTCC Microchannel Heat Sink With Embedded Metal Pin Fins
- 作者：Lili Zhang; Zhensong Li; Han Wang; Lili Cao; 其余作者待确认
- 单位（**Crossref 出版商原串**）：Beijing Information Science and Technology University 信息与通信工程学院
- 关键数字（摘要）：10/15/20 W 热负荷下中心最高温度分别降 **23.55% / 19.78% / 17.18%**（对比无针翅模型）；仿真与实验相对误差 **1.15%–8.13%**；压降代价小
- DOI：10.1002/jtse.70014 · created **2026-11-27**；**published-online 2026-11-27** · 摘要途径：Crossref abstract
- 相关性：强（电子微通道散热，仿真+实验）。注：此刊虽 ASME 刊但出版商为 Wiley，印本刊期状态待核 · 去重：新增

### 候选 5 · 双面水冷 SiC 功率模块：ANN-NSGA-II 代理优化
- 刊：Micromachines（MDPI）· 标题：Surrogate-Assisted Multi-Physics Optimization of a Double-Sided Water-Cooled SiC Power Module Using a Neural Network and a Genetic Algorithm
- 作者：Shuhua Liao; Jiuyang Tang; Liming Che; 其余待确认
- 单位（**Crossref 出版商原串**）：Fudan University, College of Intelligent Robotics and Advanced Manufacturing（上海）; Research Institute of Fudan University in Ningbo
- 关键数字（摘要）：6 个几何参数、4 个目标（最高结温、动态电流不均衡、杂散电感、等效热容）；**总优化算力降低 >20 倍**；最优解经高保真多物理场仿真复核
- DOI：10.3390/mi17121371 · created **2026-11-25**；**published-online 2026-11-25** · 摘要途径：Crossref abstract + OpenAlex
- 相关性：中（偏电热协同；**摘要无具体结温数值**）· 去重：新增

## B. 标题+作者可核、摘要零获取（Crossref 与 OpenAlex 均无；未推断内容）
均为 Elsevier，摘要途径：未取到。URL 均为 https://doi.org/<DOI>。published-online 均无。
- 6 · IJHMT 10.1016/j.ijheatmasstransfer.2026.129960（created 2026-11-26）· Transient thermal management of the high-heat-flux AI server: Data-driven optimization and hardware-in-the-loop validation · Xingyang Niu; Wei Zhang; Fang Ye; Qingfei Shen; Hang Guo · 强（标题字面 AI 服务器）
- 7 · ICHMT 10.1016/j.icheatmasstransfer.2026.113229（created 2026-11-28）· Electrothermal co-characterization of high-power GaN HEMT with embedded near-junction microchannel cooling · Yu He; Mengkai Jia; Shuhui Liang; Xiaoji Ding; Weiqiang Niu; Qiang Li; Jiaqi Li · 强
- 8 · ICHMT 10.1016/j.icheatmasstransfer.2026.113215（created 2026-11-22）· Comparative study on heat dissipation performance of diamond manifold microchannels under different channel configurations · Xuan Diao; Zheyu Fang; Xiaohu Wu · 强
- 9 · ICHMT 10.1016/j.icheatmasstransfer.2026.113259（created 2026-11-27）· Sequential partitioned design of heat sink headers and TPMS cores via two-stage topology optimization for enhanced thermo-fluid performance · Zhichao Men; Wenjiong Chen; Jilang Xiong; Yang Li · 中强
- 10 · ICHMT 10.1016/j.icheatmasstransfer.2026.113167（created 2026-11-24）· Thermo-hydraulic performance of mini-channel heat sinks with integrated optimization of inlet–outlet configuration, outlet positioning, and inclined bypass channels · Baqer J. Jaber; Sara Y. Sultan; Noor Ahmed Ammar; Basim Freegah · 中（应用领域标题未写电子）
- 11 · Energy 10.1016/j.energy.2026.143227（created 2026-11-24）· Investigation on an All-Diamond Staggered Hexagonal Pin-Fin Microchannel Heat Sink for High-Heat-Flux Cooling · Mingxue Li; Zhihao Zhang; Yufeng Zhang; Jiahui Luo · 强
- 12 · ATE 10.1016/j.applthermaleng.2026.134111（created 2026-11-26）· Numerical thermal-hydraulic study of microchannels with interrupted fins and cavities · Kaihua Zhang; Kunyan Wang; Bilin Dong; Yi Wang; Xiaohu Wu · 中
- 13 · ATE 10.1016/j.applthermaleng.2026.134152（created 2026-11-27）· Deep reinforcement learning-based multi-objective thermal management for single-phase liquid immersion cooling of high-power charging modules · Haoran Wu; Jinwang Liu; Yu Zhang; Kuibin Huang; Jiaqi Zhao; Lei Dong · 中（浸没冷却，对象为充电模块）
- 14 · ATE 10.1016/j.applthermaleng.2026.134169（created 2026-11-27）· Data-driven operating strategy design of Bi2Te3-based thermoelectric cooler arrays for efficient multi-hotspot chip thermal management · Hangyu Zhang; Xianhua Nie; Xinyi Zhang; Xuan Yao; Shuai Deng; Li Zhao · 中（芯片热点，TEC 非冷板）
- 15 · ATE 10.1016/j.applthermaleng.2026.134127（created 2026-11-24）· Rapid prediction and performance evaluation of server thermal environment across multiple operating conditions based on POD and deep neural networks · Qingqing Liu; Li Wu; Shuangquan Shao · 弱-中
- 16 · IJTS 10.1016/j.ijthermalsci.2026.111516（created 2026-11-28）· Numerical analysis of heat transfer performance in liquid-metal triangular fin and pin fin composite multi-jet microchannel systems · Chunquan Li; Rui Zhang; Yuling Shang; Wenluo Huang; Xinghang Li; Yufeng Liang · 中
- 17 · ICHMT 10.1016/j.icheatmasstransfer.2026.113218（created 2026-11-26）· A review of research methods for junction temperature estimation of IGBT power modules · Li Zhuangzhuang; Zheng Zhaolei · 中（综述）
- 弱相关 / 仅列备查（只核到标题，摘要未取到）：IJHMT 129930（蒸汽腔滴状凝结，11-22）；IJHMT 129899（微小通道电场调控沸腾转变，11-22）；IJTS 111525（动力电池液冷板，11-23）；ICHMT 113239（锂电池液冷板拓扑优化，11-26）；ICHMT 113092（微通道换热压降综述，11-25）；ICHMT 113228（时间条件代理模型，11-26，是否涉冷板待确认）；ATE 134142（超临界 CO₂ 微通道，11-26）

## C. 上期挂账 15 条重试结果：摘要全部仍未出现
Crossref 与 OpenAlex 均无摘要，未推断内容。created 均早于本窗（10-17 ~ 11-19），按窗口规则本期不算新增。
- ATE 134045（created 11-19）· 拓扑优化小通道冷板+节流结构的流量均匀性与两相稳定性实验 · Zeran Han; Jingkai Ma; Xiaohong Yan; Min Zeng; Ting Ma
- Energy 143202（11-20）· 开放式微通道冷板用于 AI 服务器单相浸没冷却 · Bo Liu; Daoguang Yu; Yifei Liu; Man Wang; Jinbo Li; Dakuo Shi; Gongming Xin
- IJHMT 129918（11-19）· CuIO 涂层歧管微通道高热流电子冷却分层热流体建模 · Seungjae Lee; Daeyoung Kong; Jaewon Hwang; Minsoo Kang; Sangyeon Pak; Jungwan Cho; Hyoungsoon Lee
- IJHMT 129866（11-16）· 高功率芯片相变冷却的流动沸腾强化与泵功降低结构设计 · Shengxian Huang 等 9 人
- IJHMT 129924（11-17）· 超低压降微通道热沉、芯片级均温 · Anish Ojha; Aniket Saha; R.A. Thanush; Vaibhav Nayak; Pyarimohan Dehury
- IJTS 111493（11-17）· MicroChanNet · Jinfeng Zhao 等 11 人
- IJTS 111490（11-18）· 射频芯片脉冲热负荷 PCM + 变截面微通道热沉 · Bo Xu; Ci Ao; Xin Wang; Zhenqian Chen
- IJTS 111477（11-03）· 面向 AI 数据中心 GPU 的两相微通道冷板系统：CHF 约束下 GPU-HBM 协同热管理 · Fengzhao Ni 等 11 人
- IJHMT 129813（11-04）· 嵌入式微流道冷却从毫米级放大到厘米级芯片 · Wei Xiao; Zhiyao Jiang; Weiheng Li; Bai Song
- IJHMT 129793（11-02）· 高功率薄片激光器歧管微射流冲击冷却 · Wang Chenjie 等 7 人（含 Tao Wen-Quan）
- ATE 133678（10-17）· 激光设备制冷剂冷板的数据高效多目标结构优化与设计空间探索 · Qingwen Gui 等 5 人
- ICHMT 112877（10-20）· TPMS 微通道热沉拓扑驱动流动特性与热工水力协同 · Yi Li 等 5 人
- ICHMT 112866（10-19）· 正弦针肋内嵌分段同轴屏蔽 TSV 的微通道热沉强化 · Qi Liu 等 5 人
- ICHMT 112885（10-19）· 微通道热沉新型翅片设计与布局 · Hussain Sallar; Muhammad Irfan; Muhammad Mahabat Khan
- IJHFF 110759（10-20）· 液态金属微通道冷板在 CPU 冷却中的热控性能 · De-Xin Zhang; Lai-Shun Yang; Kai Xie

## D. 覆盖说明
- TCPMT 窗内 0 条（Crossref 返回 0；IEEE 条目可能入库滞后，下期可再查）
- Applied Energy、ECM、ECM:X、IJHFF、Case Stud. Therm. Eng. 标题筛后无相关新条目
- **标题筛基于正则，Elsevier 刊标题不含关键词的条目可能漏检**
- 本次未使用 scripts/fetch_source.py，直接用 Crossref/OpenAlex 单篇接口
