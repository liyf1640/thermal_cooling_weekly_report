# scout-D 回传 · 英文期刊 in-press / online-first 专项（原样存档）

窗口 2026-11-15~21，一律以 Crossref `created` 判窗。方法：对 IJHMT、ATE、ICHMT、IJTS、ECM、IJHFF、TSEP、CSITE、
TCPMT、Applied Energy、Energy、Micromachines、Energies 用 Crossref 按 created 窗口批量拉取，再按主题词筛，
对入选条目逐篇调 /works/<DOI> 取作者与单位。Frontiers in Mech. Eng.（ISSN 2297-3079）未查；
用的两个 ASME ISSN（2377-5496、2332-0451）均 404，故 J. Electronic Packaging、J. Heat & Mass Transfer 未扫到。
Nature 系刊域名不可达，未扫。

**全局警示（印本名义日期陷阱）**：下列 Elsevier 条目 `published-print` 全是未来刊期名义日期，不能判窗：
IJHMT 129781 等为 2027-03；IJTS 为 2027-03；ATE / ICHMT / TSEP / CSITE 为 2026-12。它们 `created` 都落在窗内。

**摘要说明**：Elsevier 条目 Crossref 与 OpenAlex 均无摘要，均为「摘要零获取」，未重试。除标注外覆盖面依据只有标题字面。

**定向重试**：10.1109/tcpmt.2026.3751185 摘要取到（候选 1）。
**去重核对**：以下候选均不在已报清单，也不在「反复失败」清单。

## 候选 1 · 拓扑优化冷板抑制 AI 芯片热串扰（定向重试成功，建议收）
- Addressing Thermal Crosstalk in AI Chips and Heterogeneous Packages with Topology-Optimized Cold Plates
- IEEE TCPMT, 10.1109/tcpmt.2026.3751185（Xplore 文档号 11796570）
- created 2026-11-13T20:18:56Z（**窗外，早于 11-15**；OpenAlex created_date 2026-11-14）；无 published-online；
  published-print [2026] 名义；page 1-1、无 volume → Early Access。**判窗在窗外，是否收由调用方定夺。**
- 作者/单位（Crossref 原串）：Jaswanth Sai Bangaru Garu [University of California]；Zubair Shaikh [University of California]；
  Taehwan Kim [Samsung Electronics Co., Ltd]；Jae Choon Kim [Samsung Electronics Co., Ltd]；Jaeho Lee [University of California]
- 摘要（OpenAlex 单篇端点取到）：热流体拓扑优化框架，设计冷板以最小化 ASIC 与 HBM 之间的热串扰。
  ASIC 功率 300 W、固体体积分数 0.6、恒定泵功下，ASIC 约 90 °C，HBM 约 43 °C，热串扰 0.075 °C/W，
  约为同条件常规平行通道冷板的 1/3。另研究固体体积分数、流向、多 HBM 配置的影响。
- 覆盖面依据：摘要字面 "direct-to-chip liquid cooling with cold plates"
- 置信度：高

## 候选 2 · 拓扑优化小通道冷板 + 节流结构，流量均匀性与两相稳定性实验
- Experimental investigation of flow uniformity and two-phase flow stability in a topology-optimized minichannel cold plate with integrated throttling structures
- ATE 311, 10.1016/j.applthermaleng.2026.134045；created 2026-11-19T13:30:20Z；print 2026-12 名义；vol 311, page 134045
- 作者（无单位）：Zeran Han; Jingkai Ma; Xiaohong Yan; Min Zeng; Ting Ma ｜ 摘要零获取 ｜ 覆盖面：标题 "cold plate" ｜ 中高

## 候选 3 · 开放式微通道冷板用于 AI 服务器单相浸没冷却
- Thermal–Hydraulic Characterization and Multi-Objective Optimization of an Open Microchannel Cold Plate for Single-Phase Immersion Cooling of AI Servers
- Energy, 10.1016/j.energy.2026.143202；created 2026-11-20T07:50:07Z；print 2026-11 名义；vol 缺, page 143202（in press）
- 作者（无单位）：Bo Liu; Daoguang Yu; Yifei Liu; Man Wang; Jinbo Li; Dakuo Shi; Gongming Xin ｜ 摘要零获取 ｜ 覆盖面：标题 "Cold Plate … AI Servers" ｜ 中高

## 候选 4 · 歧管微通道（CuIO 涂层）高热流电子冷却，分层热流体建模
- Hierarchical thermo-fluid modeling framework of CuIO-coated manifold microchannels for high-heat-flux electronics cooling
- IJHMT, 10.1016/j.ijheatmasstransfer.2026.129918；created 2026-11-19T05:22:02Z；print 2026-11 名义；vol 缺, page 129918（in press）
- 作者（无单位）：Seungjae Lee; Daeyoung Kong; Jaewon Hwang; Minsoo Kang; Sangyeon Pak; Jungwan Cho; Hyoungsoon Lee
  ｜ 摘要零获取 ｜ 覆盖面：标题 "high-heat-flux electronics cooling" ｜ 中高

## 候选 5 · 功率电子直接浸没冷却
- Direct immersion cooling for thermal management of power electronics
- IJHMT 274, 10.1016/j.ijheatmasstransfer.2026.129907；created 2026-11-17T17:29:40Z；print 2027-03 名义；vol 274, page 129907
- 作者（无单位）：Hrushikesh B. Jadhav; Al-Thaddeus Avestruz; Solomon Adera ｜ 摘要零获取 ｜ 覆盖面：标题 "power electronics" ｜ 中高

## 候选 6 · 高功率芯片相变冷却结构设计（降泵功）
- Structural design for enhanced flow boiling and reduced pump power in phase change cooling of high power chips
- IJHMT 274, 10.1016/j.ijheatmasstransfer.2026.129866；created 2026-11-16T18:05:12Z；print 2027-03 名义；vol 274, page 129866
- 作者（无单位）：Shengxian Huang; Xin Chen; Shensen Feng; Shaoning Zhang; Jinya Liu; Ying Wang; Eddie Yin Kwee Ng; Pei Zhang; Shifeng Lin
  ｜ 摘要零获取 ｜ 覆盖面：标题 "high power chips" ｜ 中高

## 候选 7 · 超低压降微通道热沉，芯片级均温
- Ultra-low pressure drop microchannel heat sink with novel geometry for uniform temperature in chip level cooling
- IJHMT 274, 10.1016/j.ijheatmasstransfer.2026.129924；created 2026-11-17T02:12:05Z；print 2027-03 名义；vol 274, page 129924
- 作者（无单位）：Anish Ojha; Aniket Saha; R.A. Thanush; Vaibhav Nayak; Pyarimohan Dehury ｜ 摘要零获取 ｜ 覆盖面：标题 "chip level cooling" ｜ 中高

## 候选 8 · 微通道流动沸腾相变数值模型实验验证（Garimella/Weibel 组）
- Experimental validation of a saturated-interface-volume phase change model for numerical simulation of microchannel flow boiling
- IJHMT 274, 10.1016/j.ijheatmasstransfer.2026.129781；created 2026-11-16T21:56:58Z；print 2027-03 名义；vol 274, page 129781
- 作者（无单位）：Shantanu Datar; Zhe Yan; Justin A. Weibel; Suresh V. Garimella; Zhenhai Pan; Todd A. Kingston
  ｜ 摘要零获取 ｜ 覆盖面：仅标题 "microchannel flow boiling"，未显式提及电子，相关性中等 ｜ 中

## 候选 9 · Tesla 阀诱导两相混合，微通道流动沸腾（HFE-7100）
- The impact of spatial two-phase mixing induced by Tesla valve structure on microchannel flow boiling using HFE-7100
- IJHMT 274, 10.1016/j.ijheatmasstransfer.2026.129908；created 2026-11-17T17:29:40Z；print 2027-03 名义；vol 274, page 129908
- 作者（无单位）：Jingwei Han; Wenming Li ｜ 摘要零获取 ｜ 覆盖面：仅标题，电子冷却指向不明确 ｜ 中低

## 候选 10 · 冲击射流双层微通道热沉，知识迁移强化学习多目标设计
- Multi-objective design of impinging-jet double-layer microchannel heat sinks using knowledge-transfer reinforcement learning
- ATE 310, 10.1016/j.applthermaleng.2026.134020；created 2026-11-17T17:33:17Z；print 2026-12 名义；vol 310, page 134020
- 作者（无单位）：Xingran Li; Yichen Wang; Chenhan Lian; Ruiyao Xiao; Ziyu Li; Yixin Chen; Zhiyu Yang ｜ 摘要零获取 ｜ 覆盖面：标题 "microchannel heat sinks" ｜ 中

## 候选 11 · 多层振荡热扩展器，航空高功率电子冷却
- Performance characteristics of multi-layer oscillating heat spreader for potential aerospace applications of high-power electronics cooling
- ATE 310, 10.1016/j.applthermaleng.2026.134044；created 2026-11-18T19:23:19Z；print 2026-12 名义；vol 310, page 134044
- 作者（无单位）：Jian Qu; Guoqing Zhou; Ziang Li; Chengbin Zhang; Xiangdong Liu; Peng Cheng
  ｜ 摘要零获取 ｜ 覆盖面：标题 "high-power electronics cooling"（非冷板，属热扩展/均热板类） ｜ 中

## 候选 12 · 微通道流动沸腾阶跃热负荷瞬态特性（主动蒸汽注入）
- Experimental investigation of transient characteristics of microchannel flow boiling under step heat loads using active vapor injection
- ATE 310, 10.1016/j.applthermaleng.2026.134001；created 2026-11-16T13:51:13Z；print 2026-12 名义；vol 310, page 134001
- 作者（无单位）：Yaning Guo; Ke Xue; Xiusen Wang; Bo Zhang; Xiangji Guo ｜ 摘要零获取 ｜ 覆盖面：仅标题，未显式提及电子 ｜ 中低

## 候选 13 · 双蒸发器两相冷却系统最优流量（非均匀热负荷）
- Experimental investigation of the optimal operating flow rate of a dual-evaporator two-phase cooling system under non-uniform heat loads
- ICHMT 181, 10.1016/j.icheatmasstransfer.2026.113131；created 2026-11-19T11:51:27Z；print 2026-12 名义；vol 181, page 113131
- 作者（无单位）：Jinjie Bai; Siyong Yu; Zhiheng Zhu; Qile Shi; Zilong Deng ｜ 摘要零获取 ｜ 覆盖面：电子指向未证实 ｜ 中低

## 候选 14 · 单喷嘴冲击射流 + 多孔平板，非均匀热流
- Experimental study of heat transfer of single jet impingement on a perforated flat plate for non-uniform heat flux boundary condition
- ICHMT 181, 10.1016/j.icheatmasstransfer.2026.113153；created 2026-11-19T04:52:08Z；print 2026-12 名义；vol 181, page 113153
- 作者（无单位）：H.I. Shaikh; S. Siddapureddy; S.V. Prabhu ｜ 摘要零获取 ｜ 覆盖面：仅标题，电子指向不明 ｜ 中低

## 候选 15 · 3D IC 微通道冷却多层热预测网络 MicroChanNet
- Fast multi-layer thermal prediction for microchannel-cooled 3D ICs: MicroChanNet
- IJTS 233, 10.1016/j.ijthermalsci.2026.111493；created 2026-11-17T22:06:52Z；print 2027-03 名义；vol 233, page 111493
- 作者（无单位）：Jinfeng Zhao; Zihan Ke; Zhenjie Yao; Xiaoning Ma; Kunlong An; Hao He; He Cao; Jianyun Liu; Zeyu Sun; Zhiqiang Li; Qinzhi Xu
  ｜ 摘要零获取 ｜ 覆盖面：标题 "microchannel-cooled 3D ICs"，代理模型方向 ｜ 中高

## 候选 16 · 射频芯片脉冲热负荷：PCM + 变截面微通道热沉
- Synergistic thermal management of radio frequency chips under pulsed heat loads using phase change materials and variable aspect ratio microchannel heat sink
- IJTS 233, 10.1016/j.ijthermalsci.2026.111490；created 2026-11-18T17:21:08Z；print 2027-03 名义；vol 233, page 111490
- 作者（无单位）：Bo Xu; Ci Ao; Xin Wang; Zhenqian Chen ｜ 摘要零获取 ｜ 覆盖面：标题 "radio frequency chips … microchannel heat sink" ｜ 中高

## 候选 17 · SLM 圆通道热沉内部复合强化结构
- Thermohydraulic investigation of selective laser melted circular channel heat sinks with internal compound enhancement structures
- IJTS 233, 10.1016/j.ijthermalsci.2026.111505；created 2026-11-18T08:17:30Z；print 2027-03 名义；vol 233, page 111505
- 作者（无单位）：Yuliang Huo; Guibin Lou; Tao Yu; Hongwei Chen; Lida Shen ｜ 摘要零获取 ｜ 覆盖面：标题 "heat sinks"，电子指向未证实 ｜ 中

## 候选 18 · 2.5D chiplet 跨拓扑热预测 Transformer
- A mask-aware Transformer framework for cross-topological thermal prediction in 2.5D chiplet systems
- CSITE 88, 10.1016/j.csite.2026.108746；created 2026-11-21T11:18:16Z；print 2026-12 名义；vol 88, page 108746
- 作者（无单位）：Fengshuo Liu; Xiaoyu Liang; Ning Xu; Qingjia Chi; Xiaonan Zhang; Shiyi Fu; Dongfeng Cao
  ｜ 摘要零获取 ｜ 覆盖面：标题 "2.5D chiplet systems"，冷板关联弱 ｜ 中

## 候选 19 · 机房-机架-服务器-芯片多尺度热响应建模（风冷数据中心）
- A multiscale modeling framework for room-rack-server-chip thermal response in air-cooled data center cooling systems
- CSITE 88, 10.1016/j.csite.2026.108735；created 2026-11-19T01:13:18Z；print 2026-12 名义；vol 88, page 108735
- 作者（无单位）：Yu-Qing Tang; Zhi-Huan Zhou; Hong-Liang Du; Wen-Zhen Fang; Wen-Quan Tao
  ｜ 摘要零获取 ｜ 覆盖面：标题 "data center … chip"，但为风冷，冷板相关性弱 ｜ 中

## 候选 20 · IEEE TCPMT Early Access：双径向多入口小通道热沉 + DES 纳米冷却液
- A Biradial Multiple Entry Mini-channel Heat Sink for Processing Electronic Materials with an Organic Deep Eutectic Solvent (DES) Based Nano-coolant
- IEEE TCPMT, 10.1109/tcpmt.2026.3754479；created 2026-11-16T20:04:47Z；print [2026] 名义；page 1-1、无 volume（Early Access）
- 作者/单位（Crossref 原串）：Sujatha Selvamurugan [Indian Institute of Technology Madras]；Mannem S V Sayi Teja Reddy [IIT Madras]；
  Badal Modi [Lam Research Bangalore]；Dhairyashil Desai [Lam Research Bangalore]；Dhiman Chatterjee [IIT Madras]；
  Pyarimohan Dehury [Institute of Chemical Technology–IndianOil Odisha Campus]；Sarit K Das [IIT Madras]
- 摘要零获取（Crossref 无摘要，**OpenAlex 未试**）｜ 覆盖面：标题指向半导体工艺设备冷却，非芯片散热本身 ｜ 中

## 候选 21 · W-Cu 热沉锻造致半导体激光 bar 封装局部热阻（MDPI，摘要已取到）
- Forging-Induced Microstructural Heterogeneity and Localized Thermal Resistance in W–Cu Heat Sinks for High-Power Semiconductor Laser Bar Packaging
- Micromachines 17(11), 1351, 10.3390/mi17111351；created 2026-11-20T10:30:54Z；published-online 2026-11-20；无 print
- 作者/单位（Crossref 原串）：Guofeng Yang, Jin Zhang, Chi Hu, Yao Li, Shenjiang Wu，
  均为 School of Opto-Electronic Engineering, Xi'an Technological University, Xi'an 710021, China
- 摘要（Crossref，前 900 字符）：单向锻造 70W–30Cu，体热导率变化小于 5%，但封装激光 bar 在相同注入电流下输出功率降低约 20%。
  机理为锻造引入表面凹坑、Cu 网络局部软化与界面损伤，抬高 die-attach 热路径的接触与收缩热阻。
  另有一个有效热导率 2 W m⁻¹ K⁻¹ 的示意性有限差分热模型。
- 覆盖面依据：摘要字面 "high-power semiconductor laser bar packages … heat path"。属热沉材料/热扩展，非冷板 ｜ 中高（摘要后半截断）

## 已查但不收（主题弱或仅边缘）
10.1016/j.ijheatmasstransfer.2026.129905（点热源热超材料，通用）；10.1016/j.ijthermalsci.2026.111478（圆柱电池包液冷）；
10.1016/j.icheatmasstransfer.2026.113140（浸没式电池）；113139（sCO2 微通道，应用不明）；113189（纳米流体微通道 ML）；
113176（流动沸腾结垢，通用）；113187（锯齿微通道沸腾，应用不明）；113129（热虹吸环路换热器）；
10.1016/j.tsep.2026.105010（双面 V 肋微通道热沉，应用不明）；104981（pump-cooler 肋片热沉，应用不明）；
10.1016/j.enconman.2026.122398（蜂窝夹层承载散热一体化拓扑优化，应用不明）；122376（SMR 热电联供超算数据中心，能源系统）；
10.1016/j.energy.2026.142977（数据中心综合能源系统）；10.1016/j.apenergy.2026.129281（数据中心 MPC）；129288（能源-水关系）；
10.1016/j.ijheatfluidflow.2026.110795（加热微通道内柔性悬臂板流固耦合，应用不明）；
10.1109/tcpmt.2026.3755873（井下电子 PCB 可靠性，非散热）；10.3390/en19225582（EV 电池 TIM 综述）。

**强度排序**：候选 1（窗外，需调用方定夺）、2、3、4、5、6、7、15、16 最强。全部 Elsevier 条目摘要零获取。
**通道备注**：Crossref 对 ASME ISSN `2377-5496`、`2332-0451` 返回 404，J. Electronic Packaging 与 J. Heat & Mass Transfer 本栏未扫到；
Frontiers in Mech. Eng.（2297-3079）未查。
