# verified.md · 第 9 期逐位核验回传（三组 verifier 原样汇总）

## 会话出口限制（三组一致，影响所有条目的证据层级）
可用：`api.crossref.org`、`api.openalex.org`、`export.arxiv.org`、`www.prnewswire.com`、`www.coolitsystems.com`。
被代理 403 / ENOTFOUND：ScienceDirect、api.elsevier.com、nature.com、api.semanticscholar.org、Europe PMC、
unpaywall、colab.ws、ouci、fatcat、opencompute.org、archive.org/web.archive.org、GlobeNewswire、BusinessWire、
uokik.gov.pl、Bing/DuckDuckGo、sanjose.org/sjconvention.org、LITEON/DCX/nVent/Supermicro 官网。
**Crossref 单条路由不支持 `?select=abstract`（返回 parameter-not-allowed）——上期笔记里这条写法要改。**
**OpenAlex 免费额度在第 2 组末段耗尽（429，$0 remaining，resets midnight UTC）。**
故本期 Elsevier 条目的单位与摘要多为 **OpenAlex 出版商交存元数据单一路径**，未经出版商页面二次复核。

---

# 第 1 组

## 1 · 10.1016/j.applthermaleng.2026.133509 —— 通过（可含论文卡）
标题：Optimization and thermal-hydraulic performance investigation of hierarchical-tapered manifold microchannel cold plate for chip cooling
作者（OpenAlex raw_affiliation_strings；Crossref affiliation 空）：
- Xiaoyu Zhou（first）→ School of Mechanical and Automotive Engineering, South China University of Technology, Guangzhou 510640, China
- Minqiang Pan → 同上；**is_corresponding=true（非末位）；单一路径待复核**
- Qinglin Xie → 同上
日期：created 2026-10-07 / published-online null / published-print 2026-11 → **窗口内**
载体：ATE Vol. 308 文章号 133509，issue null → **在线先行**，journal-article，同行评审已接收
数字（原文）：最优参数 manifold hierarchical length ratio of 1、manifold inlet-to-outlet area ratio of 1/2、
microchannel width 0.268 mm、microchannel height 3.73 mm、manifold height 5.70 mm；
"the absolute PEC value of HTMMC is 1.383"；"the deviation between surrogate-model prediction and CFD simulation is only 0.4%"；
"The PEC ratio of the optimized HTMMC is **1.203–1.401** relative to the **initial HTMMC prototype** and
**1.678–1.849** relative to the **TMC prototype**"（TMC 原文称代表 "mainstream chip-cooling schemes"）；
方法链 single-factor → Plackett-Burman screening → Box-Behnken RSM；"demonstrated by both experimental tests and numerical simulations"
局限：摘要无热流密度/温升/压降/泵功绝对值；PEC 定义式未给；PEC 区间对应的扫描变量范围未给（不得写成「全流量范围」）；
无热机械评估；通讯作者单一路径

## 2 · 10.1016/j.applthermaleng.2026.133538 —— 通过（可含论文卡）
标题：Topology-optimized microchannel cooling for heterogeneous logic-HBM heat sources: thermal-hydraulic optimization and thermo-mechanical assessment
作者：
- Siping Gao（first）→ State Key Laboratory of Micro-nano Engineering Science, School of Mechanical Engineering, Shanghai Jiao Tong University, Shanghai 200240, China
- Meihong Zhao → 同上
- Boxiang Wang → **2020 X-Lab, Shanghai Institute of Microsystem and Information Technology, Chinese Academy of Sciences, Shanghai 200050, China**
- Shuai Gong → 同上海交大；**is_corresponding=true（末位）；单一路径待复核**
日期：created 2026-10-07 / online null / print 2026-11 → 窗口内；ATE Vol. 308 文章号 133538，在线先行
数字（原文）："Compared with the straight microchannel baseline, the optimized layouts reduce **maximum thermal resistance by ∼30%**,
cut **pumping power by 57%**."（基准=直微通道；是最大**热阻**不是温升；∼ 号须保留）；
"a **70% reduction in maximum thermally induced von Mises stress (from 35.59 to 10.75 MPa)**"；
对象 heterogeneous 2.5D packages、logic-HBM 非均匀热源；2D 拓扑优化结果重构为 3D；
稳健性（无数字）"under varying flow conditions and logic power ratios … retain their cooling advantages beyond the nominal design point"
局限：**纯数值无实验**（CFD + thermo-mechanical simulations）；名义工况流量与热流未给；2D→3D 重构保真度未评估；
应力为仿真值；工质未给

## 3 · 10.1016/j.ijheatmasstransfer.2026.129709 —— 通过（须严格分离仿真数与实验数）
标题：Thermal and hydraulic optimization and experimental validation of a water-cooled heat sink for high-power semiconductor devices
作者（五位同校不同平台，按原始串分列）：
- Hengji Wu（first）→ Jiangsu Industrial Technology Engineering Center for Environmental and Meteorological Integrated Chip System, Nanjing University of Information Science and Technology, Nanjing, 210044, China
- Jie Yang → 上述 + Jiangsu Collaborative Innovation Center on Atmospheric Environment and Equipment Technology, NUIST；**is_corresponding=true（第二作者，非末位）；单一路径**
- Yuebo Chen / Jiaye Zhou → 同 Chip System 工程中心
- Qingquan Liu → 两串同 Jie Yang
中文：南京信息工程大学
日期：created 2026-10-06 / online null / print 2027-02 → 窗口内；IJHMT Vol. 273 文章号 129709，在线先行
数字（原文，仿真/实验已分离）：
构型 parallel double U-shaped channels + regionally distributed micro-protrusions；
"a channel width ratio of 4:5 provides the most uniform temperature distribution"；
"the 45° inclined configuration (Model #3) achieved the highest PEC of 1.306"；
"the horizontal configuration (Model #2) exhibited a high PEC of 1.257, a **3.3 K lower maximum temperature**, and only a
**0.22 kPa higher pressure drop** than Model #3"（基准均为 Model #3）；
【CFD】"Compared with the smooth-channel baseline, the optimal configuration (Model #7) reduces the maximum semiconductor device
temperature by **approximately 27.3 K** under a heat flux of **80 W/cm²** while maintaining the pressure drop **below 15.3 kPa**"；
【实验】"Experimental validation conducted at a heat flux of **16 W/cm²** and an inlet coolant velocity of **0.5 m/s** showed close
agreement with the numerical predictions, yielding a **mean absolute error of 2.77 K** and a **correlation coefficient of 0.99**."；
【实验对照】"under identical operating conditions, the proposed liquid-cooled heat sink reduced both the maximum and average device
temperatures by **approximately 10 K** compared with a **conventional air-cooled heat sink**"
局限：**头条 27.3 K @ 80 W/cm² 是 CFD，实验只做到 16 W/cm²（仿真工况的五分之一）、单一流速 0.5 m/s**；
量级 80 W/cm² 级功率半导体，**与第 8 期 2000 W/cm² 芯片级不可同台比较**；PEC 与温度均匀性定义式未给；
Model #1–#7 几何定义未给；进口温度与流量绝对值未给

## 4 · 10.1038/s41928-026-01724-y —— **通过但无性能数字（只能作线索条，不得发论文卡）**
标题：Horizontal-up microfluidics for embedded chip cooling with a dielectric fluid
作者（OpenAlex raw；nature.com 403 无法复核）：
- Wei Xiao（first）、Zhihu Wu、Zhiyao Jiang、Yuxi Wang、Bai Song（**is_corresponding=true**）
  → "National Key Laboratory of Advanced Micro and Nano Manufacture Technology, Peking University, Beijing, China"
    + "School of Mechanics and Engineering Science, Peking University, Beijing, China"
- Wei Wang → 上述实验室 + **"School of Integrated Circuits, Peking University"**（集成电路学院，与其余五人不同）
**机构名注意**：原始串 "National Key Laboratory of Advanced Micro and Nano Manufacture Technology"；
OpenAlex `institutions` 映射成 "National Key Laboratory of Science and Technology on Micro/Nano Fabrication" —— **映射名与原始串不一致，按原始串为准**
日期：created 2026-10-07 / published-online 2026-10-07 / print 无 → 窗口内
Crossref assertion 评审链：Received 8 October 2025 / Accepted 11 September 2026 / First Online 7 October 2026；reference-count 49
载体：Nature Electronics，volume/issue/page/article-number **全为 null** → AOP，尚无卷期；OA closed，无任何仓储副本
栏目标签（Article/Letter）**未取到，待确认**；可确证为同行评审原始研究稿
摘要与性能数字：**四路径全空/全封，全部无法取得**（OpenAlex abstract_inverted_index null；Crossref 无 abstract；
S2 403/ENOTFOUND；EPMC 403；nature.com 与 PDF 403；unpaywall 403；arXiv `all:"horizontal-up microfluidics"` 0 命中、
`au:"Bai Song" AND abs:"dielectric"` 6 条均旧作）
与第 8 期 10.1016/j.ijheatmasstransfer.2026.129613 的关系：**两篇独立论文，非同一工作的版本重复**——
不同 DOI/刊/标题；作者名单不同（本条多 Zhihu Wu、Yuxi Wang、Wei Wang，少 Weiheng Li；一作由 Zhiyao Jiang 换成 Wei Xiao）；
Nature 稿 Received 2025-10-08，时间线独立。
**同源线索但未证实**：第 8 期那篇构型写作 "HU-type manifold"，本条标题是 "Horizontal-up microfluidics"，
**"HU" 极可能即 "horizontal-up" 缩写，但 129613 原文从未展开 HU 含义，本条摘要取不到 → 只能写「待确认」**。
差别（基于两条已核原文可比项）：129613 明确是 "comprehensive 3D numerical investigation"（纯数值）；本条是否含实验无法确认。
129613 摘要**通篇未给工质名**（复核确认第 8 期「工质未给」记法正确）；本条标题明写 dielectric fluid（标题级事实可用，
但具体介电工质名取不到，不得填）。**129613 的 2000 W/cm² / 56 K / 28 kPa / COP>2000 不得挪用到本条。**

## 第 1 组提出的第 8 期更正项
1. **机构中文名**：第 8 期第 1 条写「微纳加工技术国家级重点实验室」，但出版商原始串为
   "National Key Laboratory of Advanced Micro and Nano Manufacture Technology"（**先进微纳制造技术国家重点实验室**）。
   第 8 期用的是 OpenAlex **映射名**（Science and Technology on Micro/Nano Fabrication），与原始串不符 → **需更正**。
   另：第 8 期把 Weiheng Li 与其他三人的兼职关系写法**复核无误**（Weiheng Li 只有一串）。
2. **通讯作者可补**：第 8 期第 1 条写「通讯作者未取到，待确认」，OpenAlex 对 129613 明确给出 is_corresponding=true → **Bai Song**。
3. 第 8 期第 1 条英文标题可补录为 "Embedded micro-pin-fin heat sink with 3D manifold for cooling high-power electronics"。
4. **第 8 期性能数字复核：全部与原文一致**（2000 W/cm²、ΔT_max 56 K、ΔP 28 kPa、COP>2000、背景热流 "beyond 1 kW cm⁻²"、
   相对常规微通道基准热与流同时更优、顺排/错排圆形针肋对照组、H_cav 固定下增大 H_f 抑制旁通泄漏、间距非对称交叉耦合）——无需更正。

---

# 第 2 组

## 1 · 10.1016/bs.aiht.2026.09.001 —— **待确认（部分）；不足以填增材工艺缺口**
标题：Metal additive manufacturing enables monolithic copper cold plate development with sinusoidal microchannels for direct-to-chip cooling
作者 10 人（Crossref 与 OpenAlex 顺序一致）+ 原始串：
1 Saptarshi Joshi / 2 Behnood Bazmi / 3 Woo Young Park / 4 Daniel Farhat / 5 Evgeny Shatskiy / 6 Omar M. Zaki
  → "Department of Mechanical Science and Engineering, University of Illinois, Urbana, IL, United States"
7 Scott Green / 8 Dakota Black → **"3D Systems, Inc., 333 Three D Systems Circle, Rock Hill, SC, United States"**
9 William P. King → 上述 + "Materials Research Laboratory, University of Illinois, Urbana, IL"
10 **Nenad Miljkovic → raw_affiliation_strings 为空数组 → 单位待确认**（不得按同篇合作者代入）
通讯作者：取不到。原始串写 "University of Illinois, Urbana, IL"，**非** "at Urbana-Champaign" 全称
日期：created 2026-10-08 / online None / print [[2026]]（仅年份）/ deposited 2026-10-09 → **窗口内**
载体（问题 a）：Crossref **type = book-chapter**，container-title Advances in Heat Transfer，**volume/page/issue 全 None**，
Elsevier，PII S0065271726000225，reference-count 75；OpenAlex source.type = "book series"，issn_l 0065-2717。
横向对照同系列 2026 章节普遍无 volume → **Elsevier 书系（ISSN 0065-2717）的一章，不是期刊论文；无卷号页码**。
**同行评审状态无法核实** → 成稿不得写「同行评审论文」，写「Elsevier 书系章节，评审方式未披露」。
与第 1 期 10.1016/j.xcrp.2026.103272 的关系（问题 b）：**同组新工作，非改写非综述复述**，三条依据：
① 前作标题 "Ultra-high-performance cold plate development through topology optimization and electrochemical additive manufacturing"
（Cell Reports Physical Science，type=article，pubdate 2026-05-01），技术路线不同（前作 TO+**ECAM**；本章 **metal AM + 正弦微通道**）；
② 作者交集 5/10（Bazmi、Shatskiy、Woo Young Park、King、Miljkovic），本章新增一作 Joshi、Farhat、Zaki 与 **3D Systems 两位工业作者**，
前作工业方是 **Fabric8Labs（San Diego, CA 92121）**，本章无 Fabric8Labs 作者 → **工业伙伴整体更换**；
③ 本章 75 条参考文献中**把前作当参考文献引用**。
工艺与制造实测数据（问题 c）：**全部无法取得**（Crossref/OpenAlex 均无摘要；arXiv `all:"monolithic copper cold plate"` 0 命中）。
致密度、表面粗糙度、翅片最小特征尺寸、耐压、热阻、压降 —— 一个数字都没有。
唯一**间接线索（明确标为推断，不可写成事实）**：75 条参考文献密集出现 LPBF 纯铜文献、LPBF 通道粗糙度、X 射线 CT 尺寸计量、
单样本不确定度分析与 nvidia-smi 功率测量，加 3D Systems（LPBF/DMP 设备商）共同署名 → 很可能是纯铜 LPBF + 含实测与 CT 表征的原始工作。
待确认：Miljkovic 单位、通讯作者、卷页、评审方式、章节性质（原始研究 vs 综述）、增材工艺类型、全部数字。
**结论：若指望它填增材工艺归档缺口 —— 填不上。只能作一行提示，不要展开技术描述。**

## 2 · 10.1016/j.applthermaleng.2026.133504 —— 通过（但是**空气外流场景，非液冷冷板**）
标题：Integrated shroud designs for enhanced thermal and hydraulic performance in 3D manifold heatsinks subjected to external flow
作者 + 原始串：
1 Wenguang Zhao → School of Engineering, **Trinity College Dublin**, Dublin, Ireland —— **is_corresponding=true**
2 Gearóid Farrell → 同上
3 **Shailesh Narayan Joshi**（OpenAlex 全名；Crossref 作 Shailesh N. Joshi）→ **"Toyota Research Institute of North America, Ann Arbor, USA"** —— **is_corresponding=true**
4 Ercan M. Dede → 同上
5 Tim Persoons → Trinity College Dublin
**原始串为 "Toyota Research Institute of North America"（含 of），照原始串写**
日期：created 2026-10-08 / online None / print 2026-11 → 窗口内；ATE vol 308 文章号 133504，在线先行
数字（原文；**全部为 CFD，非实测**，用 "previously validated three-dimensional CFD framework"）：
比较 `60 shroud configurations`，对象 converging–diverging (CONDIV) manifold heatsink，置于 wall-bounded test section；
参数空间 `Five profiles, three placements, and four lengths from 0.25 L to 1 L`；速度 `5–40 m/s`，
`Reynolds numbers of 12,900–102,800 based on the heatsink unit length L`；
**At 9.68 m/s**，构型 **N4412-TS-1L**（full-length, two-sided shroud, NACA 4412 profile）：
`increases internal ingestion by 34.2%`、`heat flux by 7.5%`、`reducing external drag by 18.6%`、`local wake-deficit index by 7.4%`；
`a 23.2% reduction in the full-domain static-pressure difference yields a 40.0% increase in the coefficient of performance (COP)
within the same test section`；
对照 CP-CS-1L：`a larger heat-flux gain of 17.9%` 但 `raises the full-domain pressure difference by 57.3%`；
跨速度 `N4412-TS-1L maintains COP improvements of 33.8%–41.6% across the tested velocity range`
**基准待确认**：摘要未明示上述百分比的参照对象（无罩基准 vs 其他 shroud 构型）
局限：纯 CFD；单一 wall-bounded 测试段，COP 增益明确限定 `within the same test section`；**空气外流风冷侧气动罩，不是液冷冷板**

## 3 · 10.1016/j.icheatmasstransfer.2026.112500 —— 通过（**作者名单必须补第 9 位，且他是通讯作者**）
标题：Exploring capillary limits of copper wire mesh manifold for area scaling of capillary-driven two-phase coolers
作者 **9 人**（Crossref 与 OpenAlex 两路径一致）+ 原始串：
1 Heungdong Kwon → Dept. of Mechanical Engineering, **Stanford University**, Stanford, CA 94305 + School of Mechanical Engineering, **Kyung Hee University**, Yongin 17104, Republic of Korea
2 Roman Giglio → Dept. of Mechanical and Aerospace Engineering, **University of California, Merced**, CA 95343
3 Daeyoung Kong → Advanced Materials and Components Research Division, **Electronics and Telecommunications Research Institute (ETRI)**, Daejeon 34129 + Stanford
4 Muhammad Shattique → Dept. of Aeronautical Engineering, **Military Institute of Science and Technology**, Mirpur Cantonment, Dhaka 1216, Bangladesh + 同校 Biomedical Engineering + UC Merced Materials and Biomaterials Science and Engineering
5 Hyoungsoon Lee → School of Mechanical Engineering, **Chung-Ang University**, Seoul 06974
6 James W. Palko → UC Merced
7 Ercan M. Dede → Electronics Research Department, **Toyota Research Institute of North America**, MI 48105
8 Mehdi Asheghi → Stanford
9 **Kenneth E. Goodson → Stanford —— is_corresponding=true（候选原本漏列此人）**
日期：created 2026-10-07 / online None / print 2026-11 → 窗口内；ICHMT vol 180 文章号 112500，在线先行
数字（原文；**作者实验实测**，有高速摄像证据描述）：
背景引述（**非本文测量，属文献/行业口径**）：`Data-center cooling represents 30–40% of the total data-center facility energy consumption`；
结构 `a silicon pin array coated with a copper inverse opal (CIO) wick and copper wire-mesh (CWM) 3D manifold`，
`decoupling liquid feeding and vapor extraction`；
三组工况（加热面积 : manifold 覆盖面积）case A 5×5 : 5×5 mm²、case B 10×10 : 10×10 mm²、Case C 5×5 : 10×10 mm²；
`For all cases, A, B, and C, we achieved critical heat fluxes (CHF) of ≈ 220 and ≈ 440 W cm⁻² at heated-area mass fluxes of
5 and 10 g/min/cm², respectively, with full mass flow utilization for phase change.`；
`When excess fluid is supplied to the CWM 3D manifold, for cases A and C, slightly higher CHF level of ≈ 550 W cm⁻² is achieved.`
（高速摄像见 liquid-vapor phase front，说明有未完全汽化的过量液体）；
`for case B (10 × 10 mm² : 10 × 10 mm²), the CHF value is pinned at ≈ 440 W cm⁻²` → 归因 CWM 3D manifold
`operates near its capillary limit`、`viscous pressure drop is highly non-linear for higher mass flow rates`；
`At the most efficient operating point, the coolers achieved two-phase heat transfer coefficients, HTC₂-φ ranging from
0.4 to 0.5 MW m⁻² °C⁻¹ for cases A and B.`
**CHF 值均带 ≈，不得去掉约等号、不得换算单位**
局限：面积仅到 10×10 mm²，更大面积受毛细极限钳制（case B 被 pin 在 ≈440）；≈550 是**过量供液**下取得、非自持毛细工况；
摘要未给压降绝对值、工质、过热度、热阻；HTC 仅给「最高效工作点」区间

## 4 · 10.1016/j.icheatmasstransfer.2026.112814 —— **待确认（摘要与单位全空，建议本期不作实质条目）**
标题：Encoded corrugation design for flow redistribution and thermohydraulic performance enhancement in parallel microchannels
作者 4 人 Yili Zhou / Ping Xu / Jie Xing / Shuguang Yao；**单位全部待确认**（Crossref affiliation 空；
OpenAlex raw_affiliation_strings 四位**全部返回空数组**，该响应在额度耗尽前正常返回，属真空值）；**通讯作者取不到**
日期：created 2026-10-09 → 窗口内；ICHMT vol 180 文章号 112814，在线先行
**摘要四路径以上全空 → 无任何性能数字可引**。不否决，但写进周报等于一条空壳

## 5 · 10.1016/j.ijheatmasstransfer.2026.129693 —— 通过（标题完整，无截断）
标题（两路径字串相同）：Influence of regional artificial cavity layouts on flow boiling in micro heat sinks with stepwise-decreasing pin-fin heights
（标题版用连字符 stepwise-decreasing，摘要正文写 stepwise decreasing；引用以标题版为准）
作者 + 原始串：
1 Fatih Atci → Dept. of Mechanical Engineering, **Karadeniz Technical University**, Trabzon, 61080, Türkiye
2 **Burak Markal → 同 Karadeniz Technical University —— is_corresponding=true**
3 Alperen Evcimen → Dept. of Mechanical Engineering, **Recep Tayyip Erdogan University**, Rize, 53100, Türkiye
日期：created **2026-10-04**（窗口左边界当日，在窗内）/ online None / print 2027-02 → 窗口内；IJHMT vol 273 文章号 129693，在线先行
数字（原文；**作者实验实测**）：
四个热沉（均 stepwise decreasing fin heights）：DPFH-1D（仅下游有 microcavities）、DPFH-2D（中游+下游）、DPFH-3D（全区）、
**DPFH（无 microcavities，原文 `used as reference case`）**；
工况 `heat fluxes (212 – 462 kW m⁻²)`、`mass fluxes (151 and 222 kg m⁻² s⁻¹)`、`approximately constant inlet temperature (≈77 °C)`；
`DPFH-1D provided the best overall thermal performance and the highest two-phase heat-transfer coefficients, although DPFH-3D
yielded slightly lower wall-superheat values at the two highest heating powers.`；
`The maximum heat-transfer-coefficient enhancements of DPFH-1D reached **286.2% and 528.4%** at **151 and 222 kg m⁻² s⁻¹**, respectively.`
—— **该句未明示对照对象；摘要另处声明 DPFH（无腔）为 reference case，故基准极可能是 DPFH，但属推断**；
`Despite producing the highest pressure drop, DPFH-1D's PEC value remained above 1 throughout dataset, with a **maximum of 3.49**.`；
机理 `Downstream microcavities most effectively promoted capillary liquid retention and surface rewetting, whereas upstream and
middle microcavities provided limited additional benefits at low and moderate heat loads.`
局限：热流只到 **462 kW m⁻²（≈46 W cm⁻²，远低于 AI 芯片量级）**；仅两个质量流密度点；入口温度固定 ≈77 °C（单一过冷度）；
DPFH-1D 代价是最高压降；工质未给

## 6 · 10.1016/j.applthermaleng.2026.133318 —— 通过（全仿真/代理模型，无实验）
标题：Thermo-hydraulic optimization and rapid temperature field prediction for high heat flux density microchannel heat sinks based on multitask artificial neural networks
作者 6 人，原始串**完全相同**：`Guilin University of Electronic Technology, No. 1 Jinji Road, Qixing District, Guilin, 541004, the Guangxi Zhuang Autonomous Region, China`
1 Chunquan Li / 2 **Wenluo Huang（corr）** / 3 **Yuling Shang（corr）** / 4 **Hongyan Huang（corr）** / 5 Rui Zhang / 6 Yufeng Liang
—— **OpenAlex 标了三位 corresponding，成稿若只写一位会失准，建议写「通讯作者（元数据标注三位）」或省略**
日期：created 2026-10-08 / online None / print 2026-11 → 窗口内；ATE vol 308 文章号 133318，在线先行
数字（原文）：对象 `a three-zone non-uniform staggered pin-fin microchannel heat sink`；
框架 MTL-ANN + `proper orthogonal decomposition (POD)` + NSGA-II；
`Twelve geometric parameters in the inlet, middle, and outlet regions are selected as design variables`；
数据集由 `Latin hypercube sampling and conjugate heat-transfer CFD simulations` 生成；
`CFD validation of seven optimized designs shows that the maximum prediction error of the surrogate model is **below 5.4%**.`（基准=自家 CFD，非实验）；
`At a Reynolds number (Re) of **402**, the All-Balance optimal design achieves a peak performance evaluation criterion (PEC) of **1.34**`；
`The first **10 POD modes capture 99.95%** of the total temperature fluctuation energy, with an average temperature-field
reconstruction error **below 1.64%**.`；
`the surrogate model reduces the single prediction time to **less than 2 s** … corresponding to an approximately **4500-fold
improvement in computational efficiency**`（基准 = `Compared with conventional CFD`）
**4500 倍是计算效率，不是散热性能提升**
局限：无实验验证，误差口径均以自家 CFD 为真值；PEC 1.34 仅在 Re=402 单点；
**标题含 "high heat flux density" 但摘要未给任何热流密度数值** → 「高热流」程度无出处；CFD 基准单次耗时未给

## 第 2 组跨条目提醒
1. 本组 6 条**没有一条**能提供增材工艺实测数据；候选 1 原本被寄望填缺口，核后填不上。
   **本期「增材工艺归档」缺口仍然空着，不要用候选 1 顶上。**
2. 候选 2、6 全为数值结果；候选 3、5 为实验 —— 成稿每条必须标口径，不得混排。
3. 所有 published-print 均晚于 created，按判窗规则以 created 入窗；正文给日期建议写
   「created 2026-10-xx（在线先行；印本刊期 20xx-xx）」，避免读者误以为是未来期刊文章。
4. **与已归档周报的冲突：未发现第 1–8 期已报内容与原文不符之处。** 顺手核到第 1 期对应的 10.1016/j.xcrp.2026.103272
   准确标题为 "Ultra-high-performance cold plate development through topology optimization and electrochemical additive manufacturing"，
   18 位作者，UIUC + Fabric8Labs（San Diego, CA 92121），摘要数字 `up to 32% lower thermal resistance at a fixed flow rate`、
   `up to 68% lower pressure drop at equal thermal resistance compared with pin fin designs`、
   `only 1.1% of total data center energy use for cooling`（带 "under the stated assumptions" 限定）。

---

# 第 3 组

## A1 · arXiv:2610.11108 Cova-PINN —— 通过（预印本，未同行评审）
标题：Cova-PINN: Cross-Domain Conservation Physics-Informed Neural Network for Fluid-Solid Conjugate Heat Transfer in Complex Geometries
作者 + 单位（**已读 PDF 首页，非推断**；路径 `curl -sL https://arxiv.org/pdf/2610.11108v1` → `pdftotext -f 1 -l 1`）：
`Weizheng Zhang*¹, Xunjie Xie*¹, Hao Pan², and Lin Lu¹`；脚注 `* These authors contributed equally.` / `1 Shandong University` / `2 Tsinghua University`
→ Weizheng Zhang、Xunjie Xie、Lin Lu = **山东大学**；Hao Pan = **清华大学**；Zhang 与 Xie 同等贡献
日期：submitted 2026-10-08T02:28:18Z，**v1 仅一版** → 窗口内
载体：arXiv 预印本，**未同行评审**；primary cs.LG，cross-list physics.flu-dyn；
**Atom 无 arxiv:comment、无 journal_ref、无 DOI → 不存在任何「投稿/在审/已接收」声明，成稿不得写投了什么**
数字（原文）：摘要 "Relative to the closest baseline, **MUSA-PINN-CHT**, Cova-PINN reduces average outlet-temperature and
device-level closure errors across the four TPMS topologies by **37.7% and 60.2%**, respectively, while also improving
full-field and heat-duty accuracy, with consistent gains on DualMS."
结论节完整四项："Relative to MUSA-PINN-CHT, it reduces average **field, outlet, heat-duty, and closure** errors across four TPMS
topologies by **28.6%, 37.7%, 44.8%, and 60.2%**, respectively. On the more complex DualMS exchanger, the corresponding
reductions are **19.9%, 68.1%, 71.6%, and 73.6%**."
算例对象：`four triply periodic minimal surface (TPMS) heat exchangers and a geometrically distinct DualMS design`
→ **是 TPMS 换热器，不是冷板**
**加速比：没有，且方向相反。** 附录 Table 11 `End-to-end wall-clock cost under a common 10,000-update schedule. All runs use one
NVIDIA A40 GPU.`：E-MPINN 20.43 h、RoPINN-CHT 27.87 h、CoPINN-CHT 21.85 h、**MUSA-PINN-CHT 32.76 h**、
**Cova-PINN flow 5,000 updates 25.12 h + thermal 5,000 updates 16.18 h = 41.30 h** → **只能写训练成本增加，绝不可写加速**
局限（原文 Limitations）：`steady, constant-property CHT with temperature-independent flow fields; transient transport and
temperature-dependent flow–thermal feedback remain outside its scope. Local-control-volume and paired-wall quadrature also
increase training cost.` 另：流场网络沿用并冻结 MUSA-PINN 的两个 flow networks

## A2 · 10.1016/j.icheatmasstransfer.2026.112739 —— 通过（单位 OpenAlex 单源）
标题：Physics-informed neural networks for thermal spreading of multilayer multichip power modules
**作者人数裁定：10 人**（Crossref message.author 顺序）：1 Yonghun Kim · 2 Changhyeon Yoon · 3 Haeun Lee · 4 Seonu Bae ·
5 Nana Kang · 6 Changwoo Han · 7 Dongmin Shin · 8 Jungwan Cho · 9 Sooyoung Lee · 10 Hyoungsoon Lee
→ **scout 的 8 人名单漏了 Sooyoung Lee 与 Hyoungsoon Lee**（OpenAlex authorships 有重复条目与韩文名「한창우」，属数据瑕疵）
单位（OpenAlex raw）：School of Mechanical Engineering, **Chung-Ang University**, Seoul 06974（Yonghun Kim、Changhyeon Yoon、
Haeun Lee、Sooyoung Lee、Hyoungsoon Lee）；Department of Intelligent Energy and Industry, **Chung-Ang University**（Seonu Bae、Nana Kang）；
Research & Development Division, **Hyundai Motor Group**, Hwaseong 18280（Nana Kang 双挂、Changwoo Han、Dongmin Shin）；
School of Mechanical Engineering, **Sungkyunkwan University**, Suwon 16419（Jungwan Cho）
日期：created 2026-10-05 / published-online 字段空 / print 2026-11 → 窗口内；ICHMT Vol 180 文章号 112739，已刊出；PII S0735193326022608
数字（原文）：`The PINN achieves prediction errors **below 2.4%** for **single-source validation** and **below 2.0%** for a
realistic **seven-layer, multi-source power module**`；
`the complete **PINN-GP** workflow **reduced the estimated design-exploration time from approximately 15,000 to 200 h**
compared with **sequential FVM evaluation**`（注意 "**estimated**"，是估算不是实测墙钟）；
`achieving **up to 4.1% reduction in thermal spreading resistance**`
基准：误差基准为 FVM 解；对象为多层多热源功率模块稳态热扩散；**摘要未提任何实验验证**
待确认：单位与摘要均 OpenAlex 单源（Crossref affiliation 与 abstract 皆空）

## A3 · 10.1016/j.icheatmasstransfer.2026.112748 —— 通过（单位 OpenAlex 单源）
标题：A physics-constrained surrogate for subcooled flow boiling in low-GWP immersion cooling microchannels: FiLM conditioning and gradient-balanced training
作者 2 人：1 Jaeseon Lee · 2 Yujin Kim；单位（两人同）：
`Innovative Thermal Engineering Laboratory, Department of Mechanical Engineering, **Ulsan National Institute of Science and
Technology (UNIST)**, 50 UNIST Rd., Ulsan 44919, Republic of Korea`
日期：created 2026-10-07 → 窗口内；ICHMT Vol 180 文章号 112748，已刊出
数字（原文）：工质 **R1233zd(E)**，**micro-finned** 通道，浸没冷却；研究量为 **ONB（onset of nucleate boiling）**闭合关系的可微代理；
**训练数据来源须标明**：`trained on **correlation-generated** data over **81 operating scenarios**` —— **由关联式生成，不是实验数据**；
消融 `with fixed weights the energy residual absorbs **99.2%** of the parameter gradient and the RMSE degrades by **67%**`；
主结果 `Across all 81 scenarios the **median wall-temperature RMSE is 0.52 K** against **2.37 K** for a fully specified
**Sato–Matsumura baseline**`；`**ONB classification reaches an F1 score of 99.4%** against a **64.1% majority baseline**`；
`the onset location is recovered to a **mean absolute error of 0.15 mm**`；
泛化 `Leaving out an entire operating level, the constrained model is more accurate than an otherwise identical data-driven
network in **all four cases**, by more than the seed spread in **three**.`；
**反例（必须保留）** `It is **not uniformly more robust: beyond the trained pressure range it is 17 K worse**, so
**input clamping is mandatory**.`；
推理 `Inference costs **0.64 ms on a CPU** for a **five-member ensemble**.`；
对外部实验的核对 `Against **published R1233zd(E) measurements** the ONB criterion reproduces the **onset superheat to 1.30 K**.`；
局限（摘要自述）`The formulation has **no dry-out model and over-predicts once dry-out begins**.`
口径：训练与评估基准均为关联式生成数据，仅 1.30 K 一项对照**已发表的**实验测量 → **不得写成实验验证的冷却性能**

## A4 · 10.1063/5.0333304 —— **通过但无性能数字**（刊出版摘要零数字；另有 3 月预印本）
标题：Swirl flow in microchannels: Patterned slip walls enhance heat transport
**完整摘要两源一致、未截断**，结尾 "...enhancing the performance of microfluidic heat-transfer devices."
**摘要内不含任何数字**：无换热增强幅度、**无 Nu**、无 Re 区间、无滑移区布置参数。泵功只有定性表述：
`appropriately arranged slip/no-slip regions can **induce swirl without geometric perturbations or increased pumping power**,
ultimately **improving heat transfer efficiency at fixed volumetric flow rate**`；`a simple, **energy-neutral** strategy`；
适用范围 `under conditions relevant to **laminar** microchannel cooling`
→ **成稿不得给任何刊出版本的性能百分数**，只能写定性结论 + 工况限定
作者 + 单位（Crossref affiliation 与 OpenAlex raw 一致；国名在刊出串中被截断，国别由 2026-03 预印本首页补全，非推断）：
1 L. G. Chej / 2 M. F. Carusela（OpenAlex 作 M. Florencia Carusela）/ 3 A. G. Monastra —— 均双挂
`Laboratory of Modeling and Computational Simulation, Instituto de Ciencias, **Universidad Nacional de General Sarmiento**,
Los Polvorines, Buenos Aires CP1613` + `**National Scientific and Technical Research Council (CONICET)**, Ciudad Autónoma de
Buenos Aires C1425FQB`；预印本首页写明 **Argentina**，通讯邮箱 lchej@campus.ungs.edu.ar
4 J. Harting → `**Helmholtz-Institut Erlangen-Nürnberg für Erneuerbare Energien (IET-2), Forschungszentrum Jülich**,
Cauerstraße 1, 91058 Erlangen` + `**Friedrich-Alexander-Universität Erlangen-Nürnberg**`；预印本写明 **Germany**
5 P. Malgaretti（OpenAlex 作 Paolo Malgaretti）→ HI ERN (IET-2), Forschungszentrum Jülich, Erlangen, **Germany**
日期：created 2026-10-07 / **published-online 2026-10-07**（→ 窗口内）/ **published-print 2026-10-01、issued 2026-10-01
（名义印刷日早于 online，按铁律不作判窗依据）**
载体：**已正式刊出，卷期齐备 Physics of Fluids Vol 38, Issue 10, article 102005**（非在线先行），同行评审期刊论文
**⚠️ 同一工作有更早预印本：arXiv:2603.09607v1，2026-03-10T12:50:00Z**，题 "Swirl flow in microchannels: patterned slip walls
enhance heat transport"，同 5 位作者，**摘要与刊出版几乎逐字相同（亦无数字）**。
→ **本期窗口内的「新进展」只是正式刊出，科学内容自 3 月即公开；成稿若写「新成果」须明示此点。**
预印本里的数字（**仅供背景，不可当作 PoF 刊出数字引用**，来源 arXiv 2603.09607v1 2026-03）：
方形管 w=5×10⁻⁴ m、L=50w；工质 75% 乙二醇/水混合物；驱动压降 ΔP **0.3–10 kPa**；**Re<50**、Pe>300；
底壁 Th=35 °C、入口 Tc=15 °C、其余三壁绝热；滑移条纹数 n=25/50/100/200（每壁）、条纹角 θ=25°/45°/65°；
最佳 n=200、θ=45°，相对标准全无滑移通道、同体积流量下排热量最大提升 "up to ∼45%"；涡量—热流呈指数 1/2 幂律；格子 Boltzmann 模拟；
**全文无 Nusselt 数**（grep "nusselt" 0 命中）
→ verifier **建议本期不写 45%**，按「通过但无性能数字」处理
待确认：PoF 刊出正文未读（仅摘要），刊出版是否沿用 45%、是否新增 Nu/Re 数据未核；作者国名由预印本补全

## B5 · CoolIT "The Next Gen AI CDU" 页 —— **页面事实通过；但「窗口内新页」这一定性不成立/高度可疑**
可达性：两个 URL 均 HTTP 200、内容相同，正文 822 字符。
**canonical 为第三个地址**：`<link rel="canonical" href="https://www.coolitsystems.com/resources/news/the-next-gen-ai-cdu/" />`，og:url 同 → **建议引用 canonical**
日期来源（meta 字段名原样）：`<meta property="article:published_time" content="2026-10-07T08:00:20-06:00" />`；
`article:modified_time` 2026-10-07T09:11:51-06:00；`og:updated_time` 同 → scout 的 2026-10-07T08:00 -06:00 **核准**
**且不止 meta：页面有可见 dateline** `OCTOBER 7, 2026 | News`；新闻索引 `/news/` 首条亦显示 "The Next Gen AI CDU — OCTOBER 7, 2026"
WordPress REST 二次确认：`/wp-json/wp/v2/news?include[]=6514` → date 2026-10-07T08:00:20、date_gmt 2026-10-07T14:00:20、
modified 2026-10-07T09:11:51、slug the-next-gen-ai-cdu
**⚠️ 关键反面证据**：该文章 **WordPress post ID = 6514**，而 CoolIT news 类目里 2026-07-02 的帖子 ID 为 6553、2026-07-28 为 6605、
8–9 月的为 7375/7415/7681/7770/7797/7878。WP 自增 ID 与创建时间单调相关 → **ID 6514 说明该帖对象在 2026 年 6 月底/7 月初即已创建，
远早于其现在显示的 10-07 发布日**。结合第 8 期已记载的 2026-08-17 预告页内容，**本页实质相同**（仅多出 "The Wait is Almost Over." 一句）。
→ **这极可能是同一预告页被改日期/重新发布，而不是窗口内的新发布。周报不得写成「CoolIT 本期发布新页/有新进展」。**
无法 100% 判定是「改日期」还是「同文另发」（CoolIT 未提供 8-17 版独立 URL，archive.org 本会话 403，无法快照比对）
引文逐字核验：**准确**。`The Wait is Almost Over.`（后接两个零宽字符 U+200B，引用时忽略）；
`More cooling capacity to scale AI compute with speed, reliability, and global support is just around the corner. Get a first
look at CoolIT's next-generation CDU for high-density AI infrastructure at OCP Global Summit (Booth E19). Complete the form
below to book a meeting with our team and reserve your exclusive preview.`（CoolIT's 用弯引号 &#8217;）
**容量数字 / 型号名 / 发货日期：全部为「无」。** 整页 HTML（83,689 B）检索：
`[0-9.,]*\s*(MW|kW|megawatt|kilowatt)` → **0 命中**；`CHx*`、`OMNI*` → 0 命中；
`available/availability/shipping/ships/launch/general availability` → 0 命中；
正文含数字片段仅 `OCTOBER 7, 2026`、`Booth E19`、`© 2026 CoolIT Systems`
**"1 MW" 或任何 MW 数字：无（全页 0 命中）→ 第 8 期撤回「1MW+」的结论不需回滚**
`Booth E19` 与 `OCP Global Summit` 是原文（Booth E19 出现 1 次）；**原文未写 2026 年份、未写会期日期、未写展区城市**
引语归属：**CoolIT Systems 官网新闻页，未署个人、无具名发言人、非新闻稿体**
前瞻（未发布）：产品本体、容量、型号、规格、上市时间**全部未发布**

## B6 · OCP Global Summit 2026 会期 —— **否决 scout 的「官方口径」定性；日期本身待确认**
**opencompute.org 官方页本会话完全不可达**（summit/global-summit、events、首页全部 403；WebFetch ENOTFOUND）。
替代路径全数失败：web.archive.org/archive.org、r.jina.ai、Bing、DuckDuckGo、translate.goog、businesswire、sanjose.org、sjconvention.org
PR Newswire 上 **Open Compute Project Foundation 自家最新稿为 2026-04-29（Barcelona，EMEA Summit）**，窗口内及之后无 OCPF 官方稿
给出 2026 Global Summit 会期 → **拿不到一手官方日期**
**可达渠道只有厂商稿，且互相矛盾**：
- AcBel Polytech（PRN，2026-10-08 14:00 ET）：`at OCP Global Summit 2026, **taking place October 13–15 in San Jose, California**`，
  稿内另有 `October 13–15, 2026  Venue: San Jose Convention Center, San Jose`、Booth F3
- AEWIN（PRN，2026-10-06 10:00 ET）：`Visit AEWIN at OCP Global Summit 2026, **October 12–15**, at Booth #D9`（德/西文版同为 12.–15.）
裁定：
- 「2026-10-12 ~ 10-15」**不能作为官方会期写入周报**（只与 AEWIN 稿一致，与 AcBel 稿冲突，官方页未核）
- 「**San Jose McEnery Convention Center**」**未在任何取到的源中出现**；最接近的是 AcBel 稿的 "San Jose Convention Center"（厂商口径）
  → **不要写 McEnery**
- 已按要求未采用 CoolIT 活动页的笔误日期（"October 12 - July 15, 2026"）
**本刊真正需要的结论仍然安全**：无论 10/12–15 还是 10/13–15，会期均完整落在本期窗口（截至 2026-10-10）之后 →
「CoolIT 新一代 CDU 的首展在本期窗口之后」**可以写**。
建议表述：「OCP Global Summit 2026 于 10 月中旬在美国加州 San Jose 举行（官方页本会话不可达；可达的厂商新闻稿口径为
10 月 12–15 日与 10 月 13–15 日两种，日期待确认），即在本期窗口之后。」
待确认：官方会期起止日（12 日是否为 tutorial/预备日**纯属推测，未核，不得写**）、官方场馆全名

## B 附 · LITEON × DCX 交割
**可达渠道核查结果：窗口（2026-10-04~10-10）内无任何交割/获批/延期公告。**
- PR Newswire `keyword=LITEON` → "Displaying Results 1-14 of 14"，相关最新一条为 **Sep 03, 2026, 05:18 ET**
  「LITEON Announces Strategic Investment in Liquid Cooling Technology Company DCX」（原文 "TAIPEI, Sept. 3, 2026 /PRNewswire/ --
  LITEON Technology (2301.TW) today announced a strategic investment in DCX POLSKA Sp. z o.o. (\"DCX Liquid Cooling Systems\"),
  a Warsaw, Poland-based provider…"）。**10 月无 LITEON 稿**
- `keyword="DCX Liquid Cooling"` → 7 条，最新相关者同为 Sep 03；其余为 MarketsandMarkets 等市场报告中的厂商名单
  （**第三方分析师口径，不可作为交割证据**）
不可达（已尝试并失败 → 无法穷尽）：GlobeNewswire、BusinessWire、波兰 UOKiK、archive.org、Bing/DuckDuckGo；
LITEON/DCX 官网与台交所 MOPS 按指示未再硬撞
判定：**窗口内无新状态可核，且渠道受限无法穷尽核查**

## 第 3 组给维护者的跨期事项
1. 第 8 期对 CoolIT 预告页的描述本身没错，但本期须说明该预告页发布日期已被改至/重发为 2026-10-07、内容实质未变、仍无规格；
   WP post ID 6514 证明它不是一篇全新文章。**建议不进「更正」节（第 8 期无错），在产业节内就地说明**，避免读者误以为 CoolIT 有新进展。
2. 第 8 期撤回「1MW+」的处置经复核仍然正确：10-07 版页面全页无任何 MW/kW 数字。
3. 最易出错两处：候选 A2 作者人数（8 → **10**）；OCP 会期（**不要**写 10/12–15 为官方、**不要**写 McEnery）。
