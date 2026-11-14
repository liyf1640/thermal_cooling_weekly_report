# verified-academic（学术类逐位核验）· 第 13 期 · 窗 2026-11-08~11-14（判窗用 Crossref created）

**本期可达通道**：`api.crossref.org/works/<DOI>`、`api.openalex.org/works/https://doi.org/<DOI>`（**仅单篇端点**）、`export.arxiv.org`。
**不可达（CONNECT 403 / DNS 不解析）**：`www.mdpi.com`、`iopscience.iop.org`、`www.nature.com`、`www.researchsquare.com`、
`ieeexplore.ieee.org`、`api.semanticscholar.org`、`pub.orcid.org`、`doi.org` 跨域跳转目标；
OpenAlex `?search=` / `?filter=title.search:` **一律 429（重试 4 次）**。
→ 本期全部证据为出版商交存元数据，各条论文卡「备注」须写「出版商页面未能直读」（rules 第 15 条）。

## A1 · 10.3390/mi17111312 —— **通过**（两通道逐字一致，本期证据最硬）
- created `2026-11-12T10:07:08Z`；published-online 2026-11-12；**Micromachines 17(11), 1312**，journal-article（MDPI 正刊，同行评审）
- 标题 `In Situ Characterization of Local Thermal–Hydraulic Characteristics in a Liquid-Cooling Cold Plate for AI Servers Using an Embedded Flexible MEMS Microsensor`
- 作者序与单位原串（Crossref `affiliation[].name` 与 OpenAlex `raw_affiliation_strings` 完全相同）：
  1. Chi-Yuan Lee（`sequence: first`；OpenAlex 作 `Chi‐Yuan Lee`，连字符 U+2010，**按 Crossref 写 Chi-Yuan Lee**）
     — `Department of Mechanical Engineering, Yuan Ze Fuel Cell Center, Yuan Ze University, Taoyuan 32003, Taiwan`
  2. Kuo-Chung Lee — `CerTone Heat Solution Co., Ltd., Hsinchu 30305, Taiwan`
  3. Ying-Shuo Luo / 4. Wei-Ting Lin / 5. Chia-Te Hung — 同 1
  → 写「元智大学 机械工程系」（`Yuan Ze Fuel Cell Center` 属研究中心，不写）+「CerTone Heat Solution Co., Ltd.」
- 通讯作者：Crossref 无标注、OpenAlex 五位 `is_corresponding` **全 False** → **待确认**
- 数字（原文字面）：
  - `The sensing elements were fabricated on a 50-μm polyimide substrate and protected by a patterned PI 9320 layer.`
  - `Two microsensors were installed near the inlet and outlet of a commercial cold plate and evaluated at nominal coolant
    flow rates of 2–4 L/min.` —— **commercial cold plate**，摘要内**无型号无厂牌**
  - `The measured local temperature difference decreased from approximately 4.8 to 3.2 °C as the nominal flow rate increased,
    with a temperature difference of approximately 4.4 °C at 3 L/min.`
    → ⚠️ **这是进出口两点间的局部温差实测值，不是降温幅度**；基准＝名义流量 2→4 L/min 升高
  - `In a separate 120 h circulation test using a dedicated flow channel, all three sensing channels remained operational.`
    → ⚠️ **120 h 测试是用专用流道做的独立测试，不是在商用冷板上做的**
  - `The temperature, flow, and pressure sensitivities decreased by 7.2%, 5.4%, and 4.7%, respectively.`
    → 顺序＝温度/流量/压力，对照＝120 h 测试前
- 待确认：① 通讯作者；② 商用冷板厂牌/型号
- 失败通道：`www.mdpi.com/2072-666X/17/11/1312`（403，脚本与 curl 各一次）、`doi.org` 跳转目标同域被拒

## A2 · 10.1109/tcpmt.2026.3751096 —— **通过**
- **去重/规则检查**：该 DOI 在 `drafts/excluded-numbers.md` 第（八）节与 open-items 第 12 期有记载，但（八）节原文明确写
  「**因摘要三路全缺而未上站，不是数字有误、也不是被否决过**，下期若取到摘要可按既有规则正常收录」
  → **不构成 rules 第 25 条③的「已排除数字」禁用项**，取到摘要后可正常收录
- created `2026-11-06T20:13:09Z`（**落在上期窗口 → 前期漏收，按 rules 第 5 条如实写原始日期、不加补记标注**）
- IEEE TCPMT，`volume/issue: None`、`page: 1-1` → **Early Access**；issued 2026
- 标题 `A Network Model for Liquid Cooling in Data Center Servers utilizing an ML Model for Evaporative Chip Cooling`
- 作者：Kartik Upadhyay（`first`）/ Sumanta Acharya（`additional`），两位 Crossref `name: 'Illinois Institute of Technology'`
  （另有 `place: ['Chicago, IL, USA']` 按规则不写；无 department）；OpenAlex 原串同
- 通讯作者：两通道均未标注 → **待确认**
- 数字（原文字面）：
  - `With 97% predictive accuracy, the ML model predicted a 42% enhancement in heat transfer for a thermally optimized design.`
    → ⚠️ **97% 与 42% 同在一句内；42% 的对照基准摘要未写明**（只说 "for a thermally optimized design"），97% 的对照物亦未写明
    → **必须照抄原句，不得自行补基准**
  - `...a physics-informed CFD and data-driven ML modeling pathway with faster turn-around times
    (12 hours of CFD output in seconds) for evaluating and sizing DCEC systems...`
- **DCEC 全称（原文字面）**：`two-phase direct-to-chip evaporative cooling (DCEC)` → **scout/主代理此前漏了 two-phase，须补「两相」**
- 其他已核事实：`micropillar-array DCEC cold plates`；`High-fidelity CFD simulations, validated by measurements`；
  `surrogate DCEC ML model is integrated into a pumped two-phase closed-loop flow network model`；
  `determine server-level partial power usage effectiveness (pPUE) across a range of thermal loads`；
  `The computational models are validated using experiments performed on a benchtop DCEC setup`；
  回路含 `DCEC module, coolant distribution unit (condenser and flow-control devices), pumps, and fluid reservoir`
- **摘要中没有的（不得写）**：热流密度数值、工质名称（仅出现 `refrigerant flow rate` 一词）、pPUE 具体数值
- 待确认：① 通讯作者；② 42% / 97% 的对照基准；③ 热流密度 / 工质 / pPUE 数值
- 失败通道：IEEE Xplore 整域 403

## B1 · 10.1109/tcpmt.2026.3751185 —— **待确认（元数据通过，摘要零获取 → 不进正文）**
- created `2026-11-13T20:18:56Z`；IEEE TCPMT，`page: 1-1`、无卷期 → Early Access
- 标题 `Addressing Thermal Crosstalk in AI Chips and Heterogeneous Packages with Topology-Optimized Cold Plates`
- 作者序与单位原串（Crossref `affiliation[].name`）：
  1. Jaswanth Sai Bangaru Garu（first）— `University of California`
  2. Zubair Shaikh — `University of California`
  3. Taehwan Kim — `Samsung Electronics Co., Ltd`
  4. Jae Choon Kim — `Samsung Electronics Co., Ltd`
  5. Jaeho Lee — `University of California`
- ⚠️ **校区线索（出版商交存字段，非推定）**：三位 UC 作者 Crossref `place: ['Irvine, CA, USA']`，Samsung 两位 `['Hwasung, Republic of Korea']`。
  按 rules 第 2 条**不写城市/州省**，`name` 串里**没有校区** → 正文只能写到 `University of California`。
  另：三位 UC 作者有结构化 `department: ['Department of Mechanical and Aerospace Engineering']` → 按 2026-11-02 裁定**不采用**
- 通讯作者：无通道可取 → 待确认
- 摘要零获取 → **本条不得出现任何性能数字**
- 试过并失败：OpenAlex 单篇 **404**（复试仍 404）；OpenAlex `?search=` **429 ×4**；IEEE Xplore 整域 403
  （`doi.org` 跳转解析出 **文档号 11796570**，备作下期线索）；Semantic Scholar 403；
  arXiv `ti:"Thermal Crosstalk" AND ti:"Cold Plates"`、`all:"topology-optimized cold plates"` 各 0 条
- → **不进正文，记入 open-items**（元数据已核齐，下期 Xplore 可读时取摘要）

## B2 · 10.1016/j.ijheatmasstransfer.2026.129821 —— **否决**
- 理由：① 摘要三通道全缺 → **覆盖面无法核实**（不得从「介电液」推定电子散热，题名无 electronic/chip/cold plate）；
  ② 无可引数字；③ **第一作者姓名两通道冲突未解决**
- created `2026-11-10T14:51:28Z`；IJHMT **274, 129821**，published-print 2027-03
- ⚠️ 姓名冲突：Crossref `Fitsum H. Natnael`(first) / `Harsh Shah` / `Yangying Zhu`，**三位 affiliation 全空**；
  OpenAlex `Natnael F. Haile`(first, ORCID 0000-0002-7184-4222) / `Harsh Shah` / `Yangying Zhu`(**is_corresponding: True**)，
  三位原串均 `Department of Mechanical Engineering, University of California, Santa Barbara, 93106, CA, USA`
  → 第一作者姓氏 Natnael vs Haile **完全不同**，`pub.orcid.org` 403 无法裁决 → 记入跨期清单
- 将来收录时单位写「加州大学圣巴巴拉分校 机械工程系」（Santa Barbara 属校名组成部分）
- 失败通道：OpenAlex 单篇（有记录无摘要）、Crossref、arXiv 两检索式 0 条、ScienceDirect 403、ORCID 403

## C1 · 10.1016/j.enss.2026.100194 —— **通过（有 1 项关键待确认）**
- created `2026-11-10T08:21:24Z`；**Energy Storage and Saving，文章号 100194**，无卷期，published-print 2026-11
- 标题 `Nanofluidic ionic thermoelectric energy conversion integrated with a pin-fin based cold plate for electronic chip cooling`
- 作者序与单位（Crossref affiliation 五位全空 → OpenAlex 原串，五位**全同**）：
  Yongbo Dong(first) / Qiongyao Cui / Yu Qian / Ye Chen / **Qinlong Ren(last, `is_corresponding: True`)**
  原串 `Key Laboratory of Thermo-Fluid Science and Engineering of MOE, School of Energy and Power Engineering,
  Xi'an Jiaotong University, Xi'an, Shaanxi, 710049, China` → 写「西安交通大学 能源与动力工程学院」（MOE 重点实验室不写）
- 通讯作者：**Qinlong Ren**（交存 `is_corresponding: True`，可直接作已核结论）
- 数字（原文字面）：
  - `At an electronic heat flux of 7,000 W·m −2 , the pin-fin cold plate maintained the chip surface temperature at
    approximately 53.25 °C, while the NITEC system generated a power output density of 97.72 mW·m −2 .`
    → 7,000 W·m⁻² 确为原文字面、确系 "electronic heat flux"；**建议原样写 7,000 W·m⁻² 而非换算成 7 kW/m²**
  - `At an electrolyte concentration of 0.05 M, increasing the solution pH from 3 to 11 enhanced the maximum power output
    density from 52.09 to 118.83 mW·m −2 , representing the highest value observed in the present study.`
    → 118.83 为本研究观测最高值，基准＝同浓度下 pH 3
- NITEC 全称 `nanofluidic ionic thermoelectric energy conversion (NITEC)`
- ⚠️ **仿真 vs 实验**：摘要仅 `Numerical modeling and experiments were conducted to evaluate ...`
  → **未把任何单个数字归到仿真或实验** → 成稿只能写「数值模拟与实验并用、摘要未区分各数字归属」，**不得写成实测**
- 待确认：① 各数字属仿真还是实验；② 数字仅 OpenAlex 单通道（Crossref 未交存 abstract）

## C2 · 10.1088/2631-8695/aebd48 —— **通过（覆盖面在内，数字基准待确认）**
- created `2026-11-10T06:00:36Z`；published-online 2026-11-10、published-print 2026-11-01
- **刊名卷期（更正候选）**：**Engineering Research Express 8(21), 215527**（Crossref volume 8 / issue 21 / page 215527）
- 标题 `Thermo-hydraulic performance of a partitioned liquid cooling plate under highly non-uniform heat fluxes for space applications`
- 作者序与单位原串（两通道一致）：
  1. **Yinlin Li**(first) — `State Key Laboratory of Ultrafast Optical Science and Technology, Xi'an Institute of Optics and
     Precision Mechanics, Chinese Academy of Sciences` + `University of Chinese Academy of Sciences`
  2. Junjun Qin / 3. Yonglin Bai — 仅西安光机所串；4. Caixia Liu / 5. **Jiatao Wang**(last) — 西安光机所 + 国科大
  → 写「中国科学院西安光学精密机械研究所」+「中国科学院大学」（State Key Laboratory 不写）
  ⚠️ 姓名冲突：末位 Crossref `Jiatao Wang` vs OpenAlex `J.C. Wang` → **采 Crossref 全名**，差异记跨期清单
- 通讯作者：OpenAlex **五位 is_corresponding 全为 True**（IOP 交存伪影，不可能五人全通讯）→ **判不可用，标「待确认」，不点名**
- 数字（原文字面）：
  - `Numerical simulations indicate a substantial improvement in thermal stability, reducing the maximum temperature
    difference at the heat sink interface from 4.41 K to 1.50 K.`
    → **属数值仿真结果**；⚠️ **对照件摘要未写明** → 必须标待确认，不得补基准
  - `the serpentine structure was identified as the optimal configuration for high-heat-flux regions, as it enhances the
    convective heat transfer coefficient by inducing secondary flows and increasing fluid disturbance at the channel bends.`
    （对比对象为 trapezoidal channels：`evaluate the thermo-hydraulic responses of serpentine and trapezoidal channels`）
  - `Furthermore, an experimental platform was established to validate the numerical models, and the experimental data were
    in good agreement with the numerical predictions.` → **仅定性 good agreement，无偏差数字**
- **摘要中没有的（不得写）**：热流密度数值、工质、流量
- 覆盖面：`optoelectronic` ×2（`Space-borne optoelectronic systems`、`space-borne optoelectronic interfaces`）、`camera` ×1
  （`on-orbit replaceable space cameras`）、`cooling plate` ×2、**`chip` ×0、独立 `electronic` ×0**
  → 对象为空间相机光电器件液冷板，按 **2026-11-02「光电器件冷板在覆盖面内」裁定 → 在覆盖面内**，题名即 liquid cooling plate
- 待确认：① 4.41→1.50 K 的对照件；② 热流密度/工质/流量；③ 通讯作者；④ 末位作者姓名两通道不一致
- 失败通道：`iopscience.iop.org` 403

## C3 · 10.3390/surfaces9040094 —— **通过（证据完整）**
- created `2026-11-09T17:25:10Z`（published-online 2026-11-06，deposited 2026-11-13）；**Surfaces 9(4), 94**，正刊同行评审
- 标题 `Numerical Investigation of Flow and Thermal Performance of a Microchannel Array Jet Impingement Heat Sink with
  Porous-Skeleton Enhanced Surface Cooling: Experimental Validation and Parametric Analysis`
- 作者：**Jia-ao Dai**(first, `is_corresponding: True`) / **Xiaoshuo Liu**(last, False)，两位均
  `School of Information and Electronic Engineering, Shandong Technology and Business University, Yantai 264005, China`
  → 写「山东工商学院 信息与电子工程学院」
- 通讯作者：**Jia-ao Dai**（交存已标）
- 数字（原文字面，Crossref JATS 与 OpenAlex 逐字一致）：
  - `a porous skeleton of 0.15 mm thickness is embedded in the crossflow channel`（位置＝横流通道内）
  - `The validated model reveals that the optimal combination of jet velocity and porous filling ratio augments the heat
    transfer coefficient by approximately 15% and reduces the wall temperature by 18 °C relative to the configuration
    without the porous skeleton, with the flow resistance remaining within a practically acceptable range.`
    → **h +约 15%、壁温 −18 °C，对照基准明确＝无多孔骨架的同构型**；压降仅定性「在实际可接受范围内」，**无压降数字**
  - `A prototype of the MCJHS was fabricated and tested; the measured outlet velocity and liquid temperature agree well with
    the simulation results, with the deviations within the respective sensor accuracies, verifying the reliability of the
    numerical model.` → ⚠️ **无偏差百分比**；实测量只有**出口流速与液体温度**两项（**不是壁温、不是换热系数**）
  - 参数扫描 `covering jet velocity, porous filling thickness, and applied heat flux` → **具体区间未给**；
    评价指标 `maximum surface temperature, temperature uniformity, average heat transfer coefficient, and pressure drop` → **无绝对值**
- MCJHS 全称 `integrating array jet impingement with microchannel heat sinks (MCJHSs)`
- 覆盖面：`Electronic devices that dissipate high heat flux need compact cooling solutions...`、
  `for high-performance electronic thermal management`、`next-generation high-power electronic components` → **明确在闸门内**
- 待确认：① 射流速度/多孔填充率/热流密度区间；② 最大表面温度与压降绝对值
- 失败通道：`www.mdpi.com` 403

## C4 · 10.21203/rs.3.rs-11578799/v1 —— **通过（按预印本收）**
- created `2026-11-13T01:37:14Z`；posted 2026-11-13
- 出版状态 `type: posted-content` / `subtype: preprint`、`institution: Research Square`、**`group-title: In Review`**、CC BY 4.0
  → 即 Research Square「In Review」通道，**说明已投稿在审，但期刊名元数据未给**；另有 `accepted: 2026-10-31` 字段含义不明
  （平台受理日，**不得解读为期刊录用**）。正文按 rules 第 6 条写「Research Square 预印本（2026-11）、未同行评审」
- 标题 `Comparative Assessment of Micro-Scale Heat Exchangers Operating in Flow Boiling`
- 作者：**Ali H. Al-Zaidi**(first) — `University of Misan`；**Tassos G. Karayiannis**(last) — `Brunel University of London`
  （两串均无院系，不补写）
- 通讯作者：两通道均 False / 无标注 → **待确认**
- 数字（原文字面）：
  - `A dielectric HFE-7100 was used as the working fluid entering at 1 bar inlet pressure. The inlet subcooling was 5 K,
    the mass flux was varied between 100‒300 kg/m 2 s and the wall heat flux up to 0.324 MW/m 2 .`
  - 三构型：`two main categories, namely rectangular, multi-micro-channel and micro pin fin heat exchangers` +
    `A base benchmark design of a single micro-gap heat exchanger is also included.` + `The base area of all three designs is
    the same to allow direct comparison` → **单微间隙（基准件）/ 多微通道 / 微针肋，三者基底面积相同；具体尺寸摘要全无**
  - `The comparison of the heat transfer results indicated that the micro pin fin heat sink provided better thermal
    performance than the other geometries. In both the micro-gap and the multi-channels, the dryout region, which precedes
    the critical heat flux, was reached at lower wall heat flux values than in the pin heat sink. In addition, flow reversal
    and system instability were found to be suppressed in this design.`
  - 压降：`The pressure drop in the micro pin fin heat exchanger was higher, but it is worth noting that this is only a
    fraction of the total pressure drop and hence the pumping power of the thermal management system.` → **纯定性，零数字**
  - 终止判据 `until the exit vapour quality approached one or until near critical heat flux conditions were observed`；
    `A high-speed and high-resolution camera was used to visualise the flow boiling patterns.`
- 覆盖面：`The increasing demand to dissipate high heat fluxes from small areas in electronic equipment necessitated the move
  from air-cooled to liquid-cooled heat sinks...` → 在闸门内
- 待确认：① 三构型具体尺寸；② 压降数值；③ 通讯作者；④ 在审期刊名
- 失败通道：`www.researchsquare.com/article/rs-11578799/v1`（403 + DNS 不解析）

## C5 · 10.1115/fedsm2026-184041 —— **通过，但有一处口径错误必须改**
- created `2026-11-13T21:01:02Z`；published-online 2026-11-13；published-print/issued **2026-07-26（会期名义日期）**
- `type: proceedings-article`，ASME FEDSM2026，卷名 `Volume 1: Artificial Intelligence (AI) for Fluids; CFD Methods;
  CFD Applications; Biomedical and Bio-Inspired Fluid Mechanics`，**文章号 V001T03A012**。会议论文（非期刊刊文）
- 标题 `Machine Learning Applied for Instant Predictions of Spatial Temperature Variations in Heat Sinks for Computer Chip Cooling`
- 作者（按 Crossref 数组顺序）Ayush Jha / Reetu Thimmaiah / Isaac Perez-Raya，三位 `name` 均 `Rochester Institute of Technology , , ,`
  （`place: ['Rochester, New York, United States']`）→ 写「Rochester Institute of Technology（罗切斯特理工学院）」
  ⚠️ **ASME 交存缺陷：三位 sequence 全为 `additional`，无一位标 first** → **不写「第一作者/末位作者」字样**
- 通讯作者：Crossref 无标注、**OpenAlex 该 DOI 404**（复试仍 404）→ **待确认**
- 数字（原文字面）：
  - `Sometimes simulations can take over 5 minutes to solve, which limits real-time modeling capabilities.`
    → **「有时需 5 分钟以上」，不是固定耗时**
  - `Training took about 2 hours, and predictions took less than 0.05 seconds.`
  - ⚠️ **`Validation against theoretical results showed less than 1% error between the theoretical and simulated data.`**
    → **<1% 是「理论解 vs（OpenFOAM）仿真数据」之间的误差，不是 ML 预测精度** → **必须写成「OpenFOAM 仿真与理论解之差 <1%」**；
    摘要**没给 ML 预测的精度指标**
  - `Data for 25 different heights and 25 widths was used for training.`；`Geometries were generated parametrically in SOLIDWORKS`；
    `PyTorch was enabled with a fully connected neural network`；`Simulations were run in OpenFOAM using the chtMultiRegionFoam package`
  - ⚠️ `Both the chip and the heat sink are made of aluminum with a thermal conductivity of 400 W/m-K.`
    → **确为原文字面**（400 W/(m·K) 是铜的量级，铝约 200~240）→ 照原文引用并写明「作者给定的材料参数」，**不替作者改成铜、不静默修正**
  - `The operating conditions include a convective heat transfer coefficient of 125 W/m2-K and an ambient temperature of 40 °C.`
- 覆盖面：`The system studied includes a chip and a heat sink attached to it, with a base and N fins` + 对流边界条件 + 环境温度
  → **确为空冷翅片热沉，不是液冷冷板**；但对象明确是 chip、`Electronic cooling` → **在闸门内**，成稿须写清是空冷翅片热沉
- 待确认：① 通讯作者；② ML 预测自身精度；③ 翅片尺寸区间
- 失败通道：OpenAlex 单篇 404（两次）；ASME Digital Collection 未试（同属被拒域族）

## C6 · 10.1063/5.0359276 —— **通过（覆盖面：收，但须写明是均热板而非冷板）**
- created `2026-11-13T12:14:48Z`；published-online 2026-11-13、published-print 2026-11-01；**Physics of Fluids 38(11), 117416**，正刊
- 标题 `Numerical investigation of heat transfer enhancement of confined vapor chambers with wettability-modified surfaces by
  lattice Boltzmann method`
- 作者序与单位原串（Crossref）：Siyu Qin(first) / Yijia Liu / Siyu Chen / Jiacheng Yang / Zhaolin Gu / **Chun Yang** / Liwen Jin(last)
  - 除 Chun Yang 外六位：`School of Human Settlements and Civil Engineering, Xi'an Jiaotong University 1 , Xi'an 710049,`
    → 写「西安交通大学 人居环境与建筑工程学院」
  - Chun Yang：`School of Mechanical and Aerospace Engineering, Nanyang Technological University 2 , Singapore 639798,`
    → 写「南洋理工大学 机械与宇航工程学院」
- 通讯作者：Crossref 无标注、**OpenAlex 该 DOI 404**（复试仍 404）→ **待确认**（pubs.aip.org 按指示未再试）
- 数字（原文字面）：
  - `The effects of chamber height on bubble dynamics and thermal performance were examined for heights of 200, 150, and
    100 lattice units (l.u.).`
  - `The overall thermal resistance at 100 l.u. height is 1.9 times that at 200 l.u. height, while the boiling heat transfer
    coefficient decreases by 12.9%.` → 1.9 倍基准＝200 l.u.；12.9% 降幅在同一句内、基准未另写明
  - `The 120°–30° hybrid wettability surface (four regions) brings a 4.8-fold enhancement in thermal performance (quantified
    by reduction in overall thermal resistance) compared with the smooth surface, while the single-sided 120°–30° gradient
    wettability surface (four regions) achieves a 5.7-fold enhancement.`
    → **两者对照基准均为光滑表面**；**「提升」口径由原文括号界定＝以总热阻降幅衡量**（不是换热系数倍数）
  - 机理 `hydrophilic regions provide liquid replenishment, while hydrophobic regions promote bubble coalescence and re-nucleation`；
    设计参数 `contact angle difference, modification area, and gradient arrangement`
- ⚠️ **摘要无任何 l.u.→物理尺寸换算，无热流密度、无绝对温度/热阻值** → 相对量可引，绝对尺度不可引
- 覆盖面：首句 `The growing thermal management demands of artificial intelligence-driven data centers have drawn increasing
  attention to vapor chambers...`，末句 `...surface modification strategies in confined vapor chambers for electronic thermal
  management.` → **摘要内有「AI 数据中心」与「electronic thermal management」两处明确表述 → 闸门满足**；
  对象是**均热板而非液冷冷板** → 收，但正文须写明
- 待确认：① 通讯作者；② l.u. 对应物理腔高；③ 热流密度/绝对热阻；④ 数字仅 Crossref 单通道

## C7 · 10.1038/s44435-026-00023-4 —— **覆盖面否决**（元数据与数字全核到，留档备裁定）
- **否决理由（verifier 逐字复核）**：标题＋摘要全文关键词计数 `electron*` **0**、`chip` **0**、`CPU/GPU` **0**、`data cent*` **0**、
  `power device` **0**、`semiconductor` **0**、`cold plate` **0**、`device` **0**，连 `cooling` **0**（标题里只有 `liquid-cooled`）；
  应用场景唯一表述为 `high heat-flux thermal management`
  → 按覆盖面闸门「摘要须明确涉及冷板/芯片/功率半导体/电子散热」**不满足**；参照通用 TPMS 换热器、电机水套判例 → 不收
- **主代理裁定：从严否决，不进正文**；「微通道热沉（MCHS）本身是否即构成电子散热硬件」提请维护者裁定（记入 open-items）
- 以下为已核齐事实（裁定后可直接用）：
  - created `2026-11-11T06:18:01Z`；published-online 2026-11-11
  - **刊名（更正候选）**：**npj Thermal Science and Engineering**（**Science 单数**）**1(1)，文章号 21**
  - **标题（更正候选）**：`Numerical investigation of the thermal-hydraulic performance of liquid-cooled oblique-cut-fin
    microchannel heat sink configurations`
  - 作者（Crossref affiliation 空 → OpenAlex）：**Prasad Kangude**(first, `is_corresponding: True`) /
    **Anthony James Robinson**(last, False)，两位原串均
    `CONNECT Research Centre, Dunlop Oriel House, Trinity College Dublin, Dublin, Ireland` +
    `Department of Mechanical, Manufacturing & Biomedical Engineering, Trinity College Dublin, Dublin, Ireland`
    → 写「都柏林圣三一学院 机械、制造与生物医学工程系」（CONNECT 研究中心不写）
  - 数字（两通道逐字一致）：`Among them, PC_3_30° provides the best overall thermal-hydraulic performance, with PI values
    ranging from 1.30 to 1.54.`；`This configuration increases the convective heat transfer coefficient by up to 40% while
    reducing the pressure drop by up to 18%, despite having 5% less wetted area than the baseline.`（基准＝直肋基准件）；
    `PC_Base_30° produces the greatest convective heat transfer enhancement, with an average increase of approximately 66%,
    but incurs an average hydraulic penalty of approximately 55%`；构型集 `eight configurations, classified as symmetric (SC)
    and periodic (PC) at 30° and 60° oblique angles`；`PI` 为 `physics-based Performance Index`；
    **无热流密度、无绝对温度、无 Re 具体区间**
- 失败通道：`www.nature.com/articles/s44435-026-00023-4`（403 + DNS 不解析）；但 Crossref JATS 与 OpenAlex 重建摘要逐字一致

## C8 · 10.3389/fmech.2026.1965238 —— **通过（数字最丰富）**
- created `2026-11-12T06:37:28Z`；published-online 2026-11-12；**Frontiers in Mechanical Engineering 12，文章号 1965238**，正刊
- 标题 `Thermal–hydraulic performance of transverse ridge geometries in water-cooled microchannel heat sinks`
- 作者：**Joseph Marcello**(first, False) / **Sumith Yesudasan**(last, **`is_corresponding: True`**)，两位均
  `Mechanical and Industrial Engineering Department, University of New Haven`（`place: ['West Haven, CT, United States']` 不写）
  → 写「纽黑文大学 机械与工业工程系」
- 通讯作者：**Sumith Yesudasan**（交存已标）
- 数字（原文字面，Crossref 结构化摘要）：
  - `Ridge height ( e = 0.05–0.15 mm), pitch ( p s = 0.25–0.50 mm), and Reynolds number ( Re = 100–1000) were systematically
    varied, resulting in 135 ridged-channel simulations and five smooth-channel reference cases.`
  - `At Re = 1000, e = 0.15 mm, and p s = 0.40 mm, the smooth channel yielded a Nusselt number of 14.51, compared with 16.83,
    17.98, and 23.47 for the semicircular, rectangular, and triangular ridges, respectively. These values correspond to
    heat-transfer enhancements of 16.0%, 23.9%, and 61.8%.` → 基准＝同工况光滑通道
  - `The maximum TPF of 1.37 was achieved with triangular ridges at Re = 1000, e = 0.15 mm, and p s = 0.50 mm, which also
    yielded the highest Nusselt number of 24.01.`
  - `Triangular ridges provided the greatest thermal enhancement but incurred the highest pressure-drop penalty.` +
    Pareto：`rectangular ridges occupied much of the lower-pumping-power frontier, while triangular ridges provided superior
    heat-transfer enhancement at higher pumping demand` → **压降为定性描述，无百分比/绝对值**
  - `Two-dimensional conjugate heat-transfer simulations were performed using COMSOL Multiphysics to compare semicircular,
    triangular, and rectangular transverse ridges.`；对象 `a water-cooled copper microchannel` → **纯仿真，无实验验证**
- 覆盖面：首句 `Liquid-cooled microchannels offer an effective approach to removing high heat loads from compact electronic
  systems.` → 在摘要内且为开篇定位句，闸门满足；但**仅此一句泛指 compact electronic systems**，无具体芯片场景
  → 成稿不要写成针对某类芯片
- 待确认：① 压降量化值；② 热流密度/绝对壁温；③ 二维模型未经实验验证（技术局限）

## D 组
- **D1 · 10.1016/j.energy.2026.142969 → 否决**：摘要 Crossref/OpenAlex 双缺 → 覆盖面无法核实、无可引数字；
  题名无电子/芯片字样，不得据题名推定。created `2026-11-10T15:57:45Z`，Energy 文章号 142969。
  作者（10 位，OpenAlex）Yilin Zhong / Feilong Liu / Xiaohua Wu / Yuankai Yang / Yongshen Zhou / Zhaoyang Yan / Longsheng Lu /
  Shu Yang / Di Xing / **Yingxi Xie(last, is_corresponding: True)**；主体 `School of Mechanical & Automotive Engineering,
  South China University of Technology`（Xiaohua Wu 兼暨南大学 `School of Intelligent Systems Science and Engineering`）→ 元数据留档
- **D2 · 10.1016/j.rineng.2026.114145 → 否决**：摘要双缺；**两通道 affiliation 均空**（单位亦无从核）；
  题名 `high heat flux devices` 是否电子器件无法确认。created `2026-11-12T17:04:57Z`
- **D3 · 10.1016/j.rineng.2026.114102 → 通过（覆盖面在内，数字全核到）**
  created `2026-11-11T00:23:28Z`；Results in Engineering **文章号 114102**，published-print 2026-11，无卷期，正刊
  作者（Crossref 全空 → OpenAlex）：**Mehdi Barzegar**(first, False) / **Vali Kalantar**(middle, **is_corresponding: True**) /
  Mohammad Sefid(False) / Sina Soleimani(last, False)；前三位 `Department of Mechanical Engineering, Yazd University, Yazd, Iran`，
  Soleimani `Department of Computer Engineering, Yazd University` → 「亚兹德大学 机械工程系 / 计算机工程系」；
  **通讯作者为第二作者 Vali Kalantar（不是末位）**
  数字：`paraffin RT44HC ... aluminum pin-finned heat sinks`；`aspect ratios ranged from 1 to 4, while pin numbers varied from
  63 to 189 under heat fluxes of 1, 5, and 10 kW/m².`；`At 10 kW/m², the 63-pin configuration with AR = 4 achieved a maximum
  instantaneous base-temperature reduction of 8.1 K relative to AR = 1 and an enhancement ratio of 5.3.`（**基准＝同为 63 针的 AR=1**）；
  设定点 `set-point temperature (SPT) of 60 °C`；`At 1 kW/m², these parameters had little influence on temperature reduction,
  while reducing the enhancement ratio.`；RNN 用数值数据训练、**无精度指标**
  覆盖面：`passive thermal management of transient heat-generating electronic systems` → 在闸门内；
  但对象是 PCM 被动针肋热沉、非冷板，热流 1–10 kW/m² 偏低
  → **主代理裁定：本期不收（相关性最弱，避免凑数），元数据与数字留档**
- **D4 · 10.1016/j.icheatmasstransfer.2026.113079 → 否决**：摘要双缺 → 无法确认是否涉芯片级冷板
  （题名为数据中心**环路热虹吸**系统级能效与抗故障优化，更像机房级系统），无可引数字。created `2026-11-09T23:35:06Z`，ICHMT 181, 113079。
  ⚠️ 末位作者姓名两通道冲突：Crossref `Yit Jing Ee` vs OpenAlex `Jing Ee Yit`（已否决，仅记档）

## 建议进正文排序（verifier 建议）
1. A1（mi17111312）2. A2（tcpmt.3751096）3. C3（surfaces9040094）4. C1（enss.100194）5. C8（fmech.1965238）
6. C2（aebd48）7. C6（5.0359276）8. C5（fedsm2026-184041）9. C4（rs-11578799，预印本排最后）10. D3（相关性最弱，可不收）
**不进正文**：B1（摘要零获取，记 open-items）、B2 否决、C7 覆盖面否决、D1/D2/D4 否决

## verifier 结论：无需「更正」节
A2 与前期归档（excluded-numbers 第（八）节、open-items 第 12 期）对 created 2026-11-06、Early Access、
两位裸串 `Illinois Institute of Technology`、通讯作者取不到的记载**与本期独立复核完全一致**；
**本次核验未发现其他前期已刊内容与原文不符。**

## 需记入跨期清单的姓名/刊名差异
1. C7 刊名 **npj Thermal Science and Engineering**（Science 单数）1(1), 21；全名 Prasad Kangude / Anthony James Robinson
2. C5 的 <1% 误差口径＝理论解 vs 仿真数据（不是 ML 精度）
3. C2 卷期 Engineering Research Express 8(21), 215527；末位作者 Crossref `Jiatao Wang` vs OpenAlex `J.C. Wang` → 采 Crossref
4. B2 第一作者 Crossref `Fitsum H. Natnael` vs OpenAlex `Natnael F. Haile`（ORCID 0000-0002-7184-4222，ORCID 域不可达）
5. D4 末位作者 Crossref `Yit Jing Ee` vs OpenAlex `Jing Ee Yit`
