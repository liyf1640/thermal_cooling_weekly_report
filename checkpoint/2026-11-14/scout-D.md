# scout-D（英文期刊 in-press / online-first）· 第 13 期 · 窗 2026-11-08~11-14

方法：Crossref prefix 10.1016 / 10.1115 / 10.1109 / 10.1063，`from-created-date:2026-11-08,until-created-date:2026-11-14` + 16 组关键词，
共约 855 条 DOI，标题粗筛后人工挑选（个别 query 429 已重试补扫）。已按 reported-index 与 11 个已处理 DOI 去重。
注意：Crossref 对这些条目基本不给 `published-online`（除 PoF / FEDSM 外均为 None）。

### 候选 1 · 针肋冷板 + 纳流体离子热电
- Nanofluidic ionic thermoelectric energy conversion integrated with a pin-fin based cold plate for electronic chip cooling
- DOI 10.1016/j.enss.2026.100194 ; created [[2026,11,10]]（OpenAlex created_date 2026-11-11）
- published-online 无；published-print [[2026,11]]（仅月份名义值）
- Energy Storage and Saving，文章号 100194，无卷号。**刊名不在清单内，由调用方决定是否收**
- 作者 Yongbo Dong / Qiongyao Cui / Yu Qian / Ye Chen / Qinlong Ren（单位待确认）
- 数字（OpenAlex 摘要字面）：电子热流 7,000 W·m⁻² 时芯片表面温度约 53.25 °C，NITEC 输出功率密度 97.72 mW·m⁻²；
  电解质 0.05 M、pH 3→11 时最大功率密度 52.09→118.83 mW·m⁻²
- 闸门依据："integrated with a pin-fin-based cold plate for simultaneous electronic-chip cooling and waste-heat harvesting"
- ⚠️ 热流仅 7 kW/m²，量级很低，成稿时需注明

### 候选 2 · 拓扑优化冷板抑制 AI 芯片 / 异构封装热串扰
- Addressing Thermal Crosstalk in AI Chips and Heterogeneous Packages with Topology-Optimized Cold Plates
- DOI 10.1109/tcpmt.2026.3751185 ; created [[2026,11,13]] ; IEEE TCPMT，Early Access，无卷期
- 作者（Crossref）Jaswanth Sai Bangaru Garu（University of California）/ Zubair Shaikh（University of California）/
  Taehwan Kim（Samsung Electronics Co., Ltd）/ Jae Choon Kim（Samsung Electronics Co., Ltd）/ Jaeho Lee（University of California）
  —— **UC 具体校区待确认**
- 摘要未取到：已试 Crossref（无 abstract）、OpenAlex 单篇（404）、fetch_source、Semantic Scholar（403）
- 相关性强；**需 verifier 从 IEEE Xplore 复核摘要**

### 候选 3 · 介电液微通道流动沸腾的微结构控制输运
- Microstructure-controlled transport regimes in dielectric-fluid microchannel flow boiling
- DOI 10.1016/j.ijheatmasstransfer.2026.129821 ; created [[2026,11,10]] ; IJHMT vol 274 / 129821（published-print [[2027,3]] 名义值）
- 作者 Fitsum H. Natnael / Harsh Shah / Yangying Zhu（单位待确认）
- 摘要未取到（Crossref、OpenAlex、fetch_source 均试过）；是否明确涉及电子冷却未核

### 候选 4 · 压电多射流阵列复合强化冷却表面
- Design and Thermo-Fluid Performance Optimization of a Hybrid-Enhanced Cooling Surface with a Piezoelectric Multi-Jet Array
- DOI 10.1016/j.energy.2026.142969 ; created [[2026,11,10]]（OpenAlex 2026-11-11）; Energy，文章号 142969
- 作者 Yilin Zhong / Xiaohua Wu / Feilong Liu / Yuankai Yang / Yongshen Zhou / Zhaoyang Yan / Longsheng Lu / Shu Yang / Di Xing / Yingxi Xie
- 摘要未取到；标题未体现电子散热，**不过闸门则丢弃**

### 候选 5 · PCM 椭圆针肋热沉 + RNN 代理
- Transient Heat Transfer in Phase Change Material Heat Sinks With Elliptical Pin Fins: Numerical Investigation and Recurrent Neural Network Prediction
- DOI 10.1016/j.rineng.2026.114102 ; created [[2026,11,11]] ; Results in Engineering，文章号 114102（刊名不在清单内）
- 作者 Mehdi Barzegar / Vali Kalantar / Mohammad Sefid / Sina Soleimani（单位待确认）
- 数字（OpenAlex 摘要字面）：RT44HC 石蜡 + 铝针肋，椭圆纵横比 1–4、针数 63–189，热流 1/5/10 kW/m²；
  10 kW/m²、63 针、AR=4 相对 AR=1 最大瞬时基底温降 8.1 K，强化比 5.3；设定点温度 60 °C
- 闸门依据："passive thermal management of transient heat-generating electronic systems"
- 相关性弱到中（PCM 被动热沉，非液冷冷板），scout 建议降级为备选

### 候选 6 · ML 实时预测芯片散热翅片温度场（ASME FEDSM2026）
- 10.1115/fedsm2026-184041 ; created [[2026,11,13]]；published-online [[2026,11,13]]；published-print [[2026,7,26]]（会期名义日期）
- 文章号 V001T03A012；作者 Ayush Jha / Reetu Thimmaiah / Isaac Perez-Raya（单位待确认）
- 数字：铝热沉 k=400 W/m-K、h=125 W/m²-K、环境 40 °C；25 翅高 × 25 翅宽训练；常规仿真「can take over 5 minutes」；
  摘要后半被截断，最终精度数字未读到
- 相关性弱（空冷翅片 + 固定 h，非冷板）

### 候选 7 · 受限均热板润湿性改性的格子 Boltzmann 研究
- Numerical investigation of heat transfer enhancement of confined vapor chambers with wettability-modified surfaces by lattice Boltzmann method
- DOI 10.1063/5.0359276 ; created [[2026,11,13]]；published-online [[2026,11,13]]；published-print [[2026,11,1]]（名义值）
- Physics of Fluids vol 38，文章号 117416
- 作者 Siyu Qin / Yijia Liu / Siyu Chen / Jiacheng Yang / Zhaolin Gu / Chun Yang / Liwen Jin（单位待确认）
- 数字（Crossref 摘要字面）：腔高 200/150/100 l.u.；降至 100 l.u. 时总热阻为 200 l.u. 的 1.9 倍、沸腾换热系数下降 12.9%；
  120°–30° 混合润湿表面（四区）热性能提升 4.8 倍；单侧 120°–30° 梯度润湿（四区）提升 5.7 倍（均以总热阻降低计，对比光滑表面）
- 闸门依据："thermal management demands of artificial intelligence-driven data centers have drawn increasing attention to vapor chambers"
- 相关性中（均热板而非液冷冷板，属电子散热）；**l.u. 为格子单位，非物理尺寸**

### 候选 8 · 混合纳流体射流冲击冷却高热流器件
- Exploratory numerical insights of surface and through-thickness thermal response of high heat flux devices deploying innovative hybrid nanofluid impingement cooling technique
- DOI 10.1016/j.rineng.2026.114145 ; created [[2026,11,12]]（OpenAlex 2026-11-13）; Results in Engineering
- 作者 Muhammad Asim / Sheheryar Khan / Farooq Riaz Siddiqui / Hussain Sallar / Fahid Riaz
- 摘要未取到；"high heat flux devices" 是否指电子器件未核；相关性弱

### 本角度已检出但不收
- 10.1016/j.tsep.2026.105002（Crossref created 2026-11-11，但 OpenAlex created_date 2026-09-16，**又一个两日期不一致判例**）；
  摘要未提电子冷却 → 丢弃
- 电池冷板类：10.1016/j.applthermaleng.2026.133878、10.1016/j.ijthermalsci.2026.111441、10.1016/j.rineng.2026.114156 → 不收
- 10.1016/j.icheatmasstransfer.2026.113079（数据中心环路热虹吸，created 2026-11-09）：摘要未取到，是否涉芯片级冷板不确定
- 其余为 PV 热沉、燃气轮机/火箭冷却、池沸腾表面（129819、129861）等 → 不收

### 未覆盖 / 未检出
- 10.1115 期刊（JEP / JHMT）窗口内未检出冷板类条目，只有 FEDSM 会议文；10.1063 的 APL 未检出相关条目
- 10.1016 下 ATE / ICHMT / IJHFF / IJTS / ECM 窗口内除去重清单已列 DOI 外未再检出强相关新增
- 标题粗筛只靠关键词，标题不含这些词的条目可能漏检
