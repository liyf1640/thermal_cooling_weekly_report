# verified-industry（产业类逐位核验）· 第 13 期 · 窗 2026-11-08~11-14

8 条事实条 + A1 全部取 PRNewswire 原稿核（fetch_source.py）。**scout 记的 9 个 ET 时间戳与 9 个 dateline 全部与原稿一致。**
实质问题 4 处：F1 的 3,000 W 归属稿内自相矛盾；F6 标准号 scout 记错；F8 漏「两相」；F5 新发现稿内单机容量自相矛盾。

## F1 · Delta SC26「From-Grid-to-Chip」—— 待确认（仅 3,000 W 一项）· **建议进正文，排第 1**
- dateline `CHICAGO , Nov. 11, 2026 /PRNewswire/`；列表 `Nov 11, 2026, 09:00 ET`（一致）
- 主体 `SOURCE Delta Electronics (Americas)`；母公司 `Delta Electronics, Inc. (TWSE: 2308)`（**台交所，不是 NYSE**）
- 展会 `McCormick Place in Chicago, Illinois from November 17 to 19, 2026`，展位 `#1443`
- 全部数字均为**厂商宣称**，原文字面：
  - `the 800 VDC 2.5 MW In-Row Liquid-to-Liquid Coolant Distribution Unit (L2L CDU), equipped featuring three 800 VDC 25 kW
    hot-swappable pumps in a 3+0 configuration designed to support zero-downtime operation, with a flow rate of up to 3,850 LPM
    and 60 psi of pressure at the operating point.`（`equipped featuring` 原文如此 sic）
  - `the Project Deschutes Open In-Row CDU, which delivers up to 2 MW of cooling at a 3°C approach temperature`
  - `the Google OCP Project Brazos rack-mounted liquid-to-air CDU, delivering up to 60 kW per rack through a self-contained, closed-loop design`
  - `its latest 4U In-Rack Coolant Distribution Unit (CDU), delivering up to 200 kW of cooling capacity`
  - `its Vertical Power Delivery (VPD) Double-Sided Cooling Solution for Open Adapter Card (OAC) architectures, supporting cooling
    for up to 3,000 W of computing components and 500 W of power components within a slim 40 mm cold plate profile,
    with heat flux exceeding 170 W/cm².`
  - `its next-generation fan wall solution, featuring 450 mm EC blowers, ...` ⚠️ 原文是 **EC blowers（鼓风机）**，不是「EC 风扇」
  - `next-generation cooling technologies that feature advanced thermal interface materials and micro-channel lid structures`
  - `its hot-swappable SSD cold plate solution with a modular design for stacked SSDs`
- ⚠️ **3,000 W 归属稿内自相矛盾**（两段原文）：
  - 导语：`... the ultra-thin multi-channel flow Power Shelf Embedded Cold Plate **for the optimum cooling of up to 3,000W in computing components**.`
  - 细节段：Power Shelf Embedded Cold Plate 的描述**无任何数字**，且服务 `space-constrained power systems`（电源系统）；
    3,000 W 出现在 VPD 那句里，与 500 W / 40 mm / >170 W/cm² 同句、后三项全稿仅此一处只能属 VPD
  - verifier 判定：**归属待确认**；给两个方案 (a) 整个不用 / (b) 写在 VPD 名下 + 必须注明稿内归属不一致
  - **主代理裁定：采 (b)** —— 3,000 W 写在 VPD 的规格组内（细节段同句不可分割），**备注里写明导语把同一 3,000 W 挂在
    Power Shelf Embedded Cold Plate 名下、稿内归属不一致**；Power Shelf Embedded Cold Plate 只写「首发、稿中未给容量数字」
- 稿中明确未给（逐句确认不存在）：800 VDC 2.5 MW L2L CDU 的 **ATD / 趋近温差**（3 °C 只属 Project Deschutes，**严禁代入**）、
  供回水温度、尺寸占地、冗余等级（除 `3+0` 外无 N+1/N+2）、效率、压降曲线；全稿无价格、无上市时间、无出货量、无客户名
- ⚠️ `800 VDC` 修饰的是 **CDU 的供电输入**（`800 VDC-powered`），不是冷却侧
- URL https://www.prnewswire.com/news-releases/delta-unveils-from-grid-to-chip-cooling-innovations-for-ai-infrastructure-and-for-new-800-vdc-400-vdc-architectures-at-sc26-302935999.html

## F2 · Gates ThermalCool 2100SS 泵 —— 通过 · **建议进正文，排第 3**
- dateline `DENVER , Nov. 12, 2026`；列表 `Nov 12, 2026, 16:30 ET`（一致）
- `Gates Industrial Corporation Ltd. (NYSE: GTES )`；`SOURCE Gates Corporation`；发言人 `Rebekah Headley, general manager of data centers at Gates`
- 厂商宣称，原文字面：
  - `High performance in a compact footprint: Up to 200 L/min flow at 3 bar in a 4U-compatible design.`
  - `Self-cooling architecture: Built for enclosed CDUs with limited airflow or high ambient temperatures, the motor is uniquely
    designed to be electrically dry and actively liquid-cooled by the coolant the pump already circulates, with no separate
    cooling circuit or fan required.`（**「无需独立冷却回路或风扇」这半句务必保留**）
  - `Stainless steel construction, OCP-compliant wetted materials, IP55 protection and a rated 50,000-hour pump life`
  - `parallel operation and N+1 redundancy ... CANBUS and MODBUS communication support integration with CDU monitoring and control systems.`
  - `The Gates ThermalCool 2100SS Pump is expected to be available globally in early 2027.` → **按 rules 第 9 条写成预告**
  - 客户：`in response to requirements from a leading CDU manufacturer, working as an engineering partner` —— 未具名
- ⚠️ **稿中无 "first" 字样，不得写「首款」。** 稿内口径均为「新增 / 扩展」：
  `adding a new, purpose-built active coolant circulation solution alongside its fluid conveyance and connection technologies`；
  `complementing its portfolio of hoses, UQDs, fittings and engineered assemblies`
- 稿中未给：扬程曲线、效率、输入功率、电压、噪声、转速、重量、尺寸（仅 4U 兼容）、价格、产能、客户名
- URL https://www.prnewswire.com/news-releases/gates-introduces-compact-thermalcool-2100ss-pump-to-expand-data-center-portfolio-302937904.html

## F3 · Frore Systems LiquidJet CES 奖 —— 待确认（部分）· **建议进正文，排第 4**
- dateline `SAN JOSE, Calif. , Nov. 11, 2026`；列表 `Nov 11, 2026, 09:26 ET`（一致）
- 奖项（第三方事实，可写）：`The Consumer Technology Association today announced that Frore Systems has been named a
  CES Innovation Awards ® honoree in the **Enterprise Tech** category for LiquidJet ® , its direct-to-chip advanced liquid
  coldplate designed for AI data centers. The **CES Innovation Awards 2027 program** received a record number of submissions
  – nearly 4,000. This is the fourth consecutive CES Innovation Award ...`
  —— 级别是 **honoree**（不是 Best of Innovation）；`CES 2027 takes place Jan. 6-9 in Las Vegas.`
- 厂商宣称数字（原文字面）：
  `LiquidJet enables GPUs to run up to 12°C cooler, providing up to 25% more AI Tokens per Watt with a seamless upgrade,
  and can manage hotspot power density of 670 W/cm².`
  `With integrated diamond spreaders embedded in the coldplate base, LiquidJet Diamond enables GPUs to run up to 22°C cooler,
  providing up to 35% more AI Tokens per Watt, and can manage hotspot power density of 770 W/cm².`
- ⚠️ **对比基线稿中完全没有**。全稿唯一可能暗示是 `Legacy coldplates rely on outdated skived 2D microchannel manufacturing`，
  但该句**与 12/22 °C 无任何连接** → 用这两个数字必须写「厂商宣称……（稿中未给对比基线）」，**严禁补「相对风冷」「相对常规冷板」**
- ⚠️ 原文是 `hotspot power density`（**热点功率密度**），不是 heat flux → **不可与 F1 Delta 的 `heat flux exceeding 170 W/cm²` 并列比较**
- ⚠️ 「Unicorn / 独角兽」：稿中确有（标题 + `the Silicon Valley unicorn`），但**无估值、无融资轮次、无投资方、无第三方来源** → **不采用**
- ⚠️ **量产 / 出货时间稿中没有**；`integrated into products from major OEMs` 是 About 段对公司全部技术（含 AirJet）的笼统表述，
  **不能当 LiquidJet 已出货的证据**。制造：`manufacturing operations in Taiwan`
- 白皮书（须注明是 Frore 自家分析）：`By optimizing the full thermal stack and running AI chips cooler, the research finds
  data centers could produce **over 40% more AI tokens** from the same electricity.`
- scout 漏记、建议整组不用：`roughly **20% less** energy and water ... around **26% less** with LiquidJet Diamond`；
  CEO 引语 `Every **100 megawatts** ... can do the work of roughly **135 megawatts** ... three data centers can do the work of four.`；
  产品线 `LiquidJet ® Nexus, a lightweight integrated coldplate system that integrates multiple LiquidJets and eliminates all
  hoses, connectors and manifolds enabling ½U compute trays.`
- URL https://www.prnewswire.com/news-releases/ai-cooling-unicorn-frore-systems-wins-ces-innovation-award-for-sustainable-ai-cooling-302936581.html

## F4 · Daikin Applied D60-W —— 通过 · **建议进正文，排第 2**
- dateline `MINNEAPOLIS , Nov. 10, 2026`；列表 `Nov 10, 2026, 09:00 ET`（一致）
- 正式名 `Reference Architecture D60-W Water-Cooled Chillers with Dry Coolers`
- **92% / 8% 的口径原文（勿改写成「热负荷」，稿中无 heat load 字样）**：
  `D60-W supports a **60 MW IT load** across **six deployable units**. **Liquid cooling handles 92% of the load and air cooling
  handles the remaining 8%.** The design runs two temperature loops. A high-temperature liquid loop serves the coolant
  distribution units (CDUs) and a dedicated low-temperature loop serves the air-cooling rack containment units, improving
  overall plant efficiency.`
- `D60-W is built around Daikin Applied's oil-free Magnitude® WME magnetic bearing centrifugal chillers, with capacities up to 10 MW.`
  （原文是「容量最高 10 MW」，未明说「单机」→ 写「机型容量最高 10 MW」）
- `dry coolers carry the cooling load for most of the year in suitable climates, with chillers supporting the operation during the hottest days.`
- `D60-W switches between dry cooling, hybrid cooling and full mechanical cooling based on outdoor conditions. In dry cooling mode,
  the chiller compressors are off. In hybrid mode, waterside economizers precool the return water and the chillers handle the remaining load.`
- `Heat rejection relies on dry coolers instead of evaporative cooling towers, which **eliminates cooling-tower make-up water**
  and supports low water usage effectiveness (WUE).` —— ⚠️ **WUE 只有 low 这个形容词，无任何数值**
- 机架侧：`D60-W's racks are primarily liquid cooled via CDUs, while the DDC Solutions S-Series rack containment units (RCUs)
  capture the remaining heat at the rack and move it directly to the low-temperature loop`（稿带脚注引 ddcsolutions.com 规格）
- 另有 `RideThrough®` / `RapidRestore®` 冷机技术；`iDCM` 监控层统一协调 RCU / CDU / 冷机 / 干冷器
- **未发布产品（rules 第 9 条）**：`The Daikin Applied CDU and data center dry cooler are **currently under development,
  with availability targeted for the second half of 2027**.`
- NVIDIA 相关表述**全稿仅 1 处**：`a 60-megawatt (MW) cooling blueprint for AI factories **based on the NVIDIA DSX AI Factory
  Platform with NVIDIA Vera Rubin NVL72**.` → **稿中无任何 NVIDIA 冷板规格、无 TDP、无单机架功率、无流量水温要求**
- 稿中未给：CDU 容量、供回水温度、趋近温差、流量、PUE/WUE 数值、每个 deployable unit 的 MW、价格、首个落地项目、客户名
- 发言人 `Yu Nishiwaki, president and CEO of Daikin Applied`；`Karim Shalash, director of Data Center Solutions`
- URL https://www.prnewswire.com/news-releases/daikin-applied-introduces-60-mw-ai-factory-cooling-reference-architecture-302934188.html

## F5 · Armada + Johnson Controls 都柏林 —— 待确认（部分）· **verifier 与主代理均判：不收**
- dateline `DUBLIN , Nov. 11, 2026`；列表 `Nov 11, 2026, 03:00 ET`（一致）
- 302935706 = 302935710 **确认为同一稿重复发布**（同标题、同 ET 时间戳，正文逐段一致，10,438 vs 10,422 字符差异仅页尾署名区）；
  另有德语版 `Nov 12, 2026, 01:29 ET`、法语版 `Nov 11, 12:53 ET`、西语版 `Nov 11, 09:58 ET` → **算一个事件**
- 核到：`spanning **90,000 square feet** ... supported by **approximately 700** Johnson Controls engineers, technicians and other skilled workers`；
  Gilbert AZ `continuous production is expected to begin in early 2027 across up to 400,000 square feet, supporting more than 500 jobs`；
  `Further manufacturing expansion is planned at a Johnson Controls site in Edmonton, Canada.`
- ⚠️ 500 MW 口径：`Armada and Johnson Controls are targeting **at least 500 MW of capacity in 2027**` ——
  **稿中未定义 capacity 是制造产能、交付容量还是部署 IT 容量 → 不得写成「产能」或「IT 容量」**
- ⚠️ 首台口径：原文是 `the first **Dublin-built** Leviathan` / `**Europe's first** Leviathan`，**不是全球首台**
- ⚠️ **新发现：稿内单机容量三处自相矛盾** → 任何「每台 MW」数字都不得写：
  正文 `Fossefall has placed an initial order for **five** Leviathan modular data centers totaling **more than 9 MW**`（折算约 1.8 MW/台）；
  About 段 `to **10 MW Leviathans**`；正文又称 `a multi-megawatt-scale modular data center`
- ⚠️ **全稿 `liquid cooling` / `cold plate` / `direct-to-chip` 零命中**；散热内容仅一句无数字的产品组合罗列：
  `The Johnson Controls thermal portfolio spans the end-to-end thermal chain, including **coolant distribution units, chillers,
  and building controls**, and supports high-density compute with **zero-water cooling technologies** ...`（零水冷却亦无 WUE 数值）
- → **本期不收**（散热信息量≈0 + 两处口径矛盾）
- URL https://www.prnewswire.com/news-releases/armada-and-johnson-controls-launch-galleon-forge-two-in-dublin-bringing-sovereign-ai-infrastructure-production-to-europe-302935710.html

## F6 · Infinium EDGE ETV100 NSF 认证 —— 通过（含一处 scout 记错的更正）· **建议短条**
- dateline `SACRAMENTO, Calif. , Nov. 9, 2026`；列表 `Nov 09, 2026, 07:00 ET`（一致）
- ⚠️ **更正 scout：标准号不是「NSF/ANSI 537」，原文是 `NSF Certification Guideline 537`；全稿无 ANSI 字样**
  `NSF International has registered Infinium EDGE ETV100™ Immersion Fluid in **Category HT1** for heat transfer applications
  where incidental food contact may occur, and certified it PFAS-Free under **NSF Certification Guideline 537**, confirming
  that ETV100 is not PFAS chemistry.`
- HT1 的准确含义：`fluids that may come into **incidental contact** with food. To earn it, NSF reviews the fluid's formulation
  and labeling against applicable U.S. FDA regulations (21 CFR).` → **是「可能偶发接触食品」，中文慎用「食品级」**
- 化学：`a **synthetic hydrocarbon fluid** produced through Infinium's **Fischer-Tropsch** process, with **no fluorinated
  compounds by design**`；路线 `proprietary **single-phase** immersion cooling technology`（单相，稿中明示）
- **scout 漏记的唯一定量指标**：`NSF verified it against defined requirements: **no more than 50 ppm total organic fluorine**
  and no intentionally added PFAS, PFAS additives, post-consumer recycled content or PFAS from manufacturing contamination.`
- 应用：`powers Infinium Edge's immersion cooling systems, including **Vector ONE™** modules deployed through the ... EdgeSites™ program`
- 证书：`Certificate C0911923-01`（Sacramento, CA）/ `C0911930-01`（Corpus Christi, TX）/ `Registration No. 174592`，可于 nsfwhitebook.org 复核
- 企业自述（宣称，须标）：`Infinium Edge is the **only North American producer** of Fischer-Tropsch immersion fluids`
- **热物性 / 介电数值：稿中完全没有**（无导热、黏度、比热、闪点、沸点、介电常数、击穿电压、兼容性）；唯一数字是 50 ppm
- URL https://www.prnewswire.com/news-releases/infinium-edge-etv100-immersion-fluid-earns-nsf-pfas-free-certification-and-ht1-registration-as-food-safe-302932662.html

## F7 · Vertiv PowerStation 3100 RPP —— 通过 · **建议短条（本期唯一「电气侧为液冷漏液做设计」的一手证据）**
- dateline `COLUMBUS, Ohio , Nov. 13, 2026`；列表 `Nov 13, 2026, 08:30 ET`（一致）
- `Vertiv Holdings Co. (NYSE: VRT )`；发言人 `Kyle Keeper, Senior Vice President of Vertiv's Power Business Unit`
- `supports **600 A, 800 A, 1,000 A, and 1,200 A** configurations on a single hardware platform, providing **three to five times
  the capacity** of traditional panelboard-based RPPs.`（3–5 倍为厂商宣称，基准是 `traditional panelboard-based RPPs`）
- `power densities **exceeding 100 kW**`；`The solution is **available now in North America**.`
- scout 漏记：`Delivered as a complete, **UL-891 listed** assembly`；`custom busbar architecture with molded case circuit breakers (MCCBs)`；
  `switch between **60 A, 100 A and 150 A** trip-unit ratings within the same circuit breaker frame`
- ⚠️ **液冷联动点原句（主语是设施方的检漏系统，Vertiv 提供的是断路器分励跳闸）**：
  `**Liquid cooling leak isolation:** Each branch circuit breaker includes an integrated remote shunt trip, enabling
  **the facility's leak detection system** to isolate power to an individual rack the moment a leak is detected, without
  shutting down adjacent racks or the entire pod. ... The shunt trip accessory is embedded within the breaker, adding no
  additional footprint.`
  背景句：`adoption of direct liquid cooling has created a need to isolate power to an individual rack if a coolant leak is
  detected. Traditional remote power panels were not designed for these demands.`
  → **不要写成「Vertiv 的漏液检测系统」**
- 稿中未给：价格、交期、短路耐受/分断电流数值（仅定性）、尺寸、效率
- URL https://www.prnewswire.com/news-releases/vertiv-introduces-high-density-remote-power-panel-for-next-generation-ai-data-centers-302938962.html

## F8 · Chatsworth Products SC26 —— 通过（含 scout 漏记的关键限定词）· **建议短条**
- dateline `SIMI VALLEY, Calif. , Nov. 10, 2026`；列表 `Nov 10, 2026, 09:00 ET`（一致）
- `Chatsworth Products, Inc. (CPI)`；发言人 `Sam Rodriguez, Senior Product Manager, Cabinets, Containment and Industrial Solutions`
- ⚠️ **scout 漏了「two-phase（两相）」**。正文专节（最完整，用这句）：
  `CPI will also showcase **ZutaCore® HyperCool® waterless two-phase direct-to-chip liquid cooling integrated into CPI's
  ZetaFrame® Cabinet System**.` → **必须写「无水两相直触芯片液冷」**，漏掉「两相」会写错 ZutaCore 的技术路线
  （副标题与文末两处措辞省略了 two-phase，三处不一致）
- ORV3：`CPI's OCP Open Rack V3 (ORV3)`；`carries the **OCP Accepted®** designation`；
  `Available in standard and customer-specific **44OU and 48OU** ORV3 and High-Power Rack (HPR) configurations, the solution
  supports **21-inch** Open Rack equipment, with optional support for **19-inch** EIA equipment.`
- 预览（未发布，rules 第 9 条）：`CPI will also preview its **CoolStream™ Rear Door Heat Exchanger (RDHx)**, designed to bring
  liquid-assisted cooling to the rack level.`；另有 `The upcoming **eConnect® PDUs with 480V Input**`
- ⚠️ 电气侧确有数字：`Optional **48V DC power shelf** solutions range from **18 kW to 33 kW**, while compatible **busbars range
  from 350 A to 2500 A**`；但 **CoolStream RDHx 与 ZutaCore 集成方案均无任何容量 / 热流密度 / 流量 / 水温 / 压降数字**
- 展会 `SC26, taking place **November 15–20, 2026** ... During the exhibition, **November 17–19**`；`Booth #4203`
- URL https://www.prnewswire.com/news-releases/chatsworth-products-showcases-rack-power-and-cooling-solutions-for-ai-and-hpc-at-sc26-302932153.html

## 专项挂账结论
1. **Delta 800 VDC L2L CDU 规格表 / 产品页 → 稿方未披露 + 产品页不可达。**
   `www.deltaww.com/.../Coolant-Distribution-Unit-CDU/ALL` → 403（**连续第二期**）；备用域 `www.delta-americas.com` 根路径与产品页均 403
   → ATD / 供回水温度 / 尺寸 / 冗余等级本期不得补任何数值；挂回 open-items
2. **Daikin 欧洲站 CDU 稿 → 否决，不得引用任何数字。**
   `www.daikin.eu`（带/不带 www，fetch_source）403；WebFetch 同 URL `getaddrinfo ENOTFOUND`（**该域在会话网络白名单外**）；
   `www.daikin.com/press/2026/` 403；DCD 搜索路径 403、`/en/news/cooling/` 404、`/en/news/` 列表只到 11-13 且无 Daikin CDU 条目
   → 真实稿日、400 kW~2.5 MW 容量区间、订单开放日（2026-11-01 vs 2027-11-01 冲突）**三项全部未核**
   ⚠️ **唯一找到的旁证恰是不可用的二手源**：A1（Wissen 稿）里有一段
   `In **October 2026**, Daikin Industries, Ltd. of Japan introduced a new line of coolant distribution units for AI data centers,
   with single units reaching **2.5 MW**, and showed them at an industry congress in **Cannes**. The range starts at **400 kW**,
   up to **ten** units can run together under one control system ...`
   —— 市场研究公司 PR 里的二手汇编，且稿期写作 October 2026 与 scout 听说的 11-02 不符 → **一律不作证据**
   → **本期只写经核的 F4 一侧**（Daikin Applied 自家 CDU 与干冷器仍在开发、目标 2027 下半年）；
   **不得把欧洲侧与美国侧并列、不得写「欧洲已上市而美国仍在开发」**
3. **3C Datalec 是否另发产品稿 → 本期无新稿。** PRNewswire 两次搜索（Datalec / 3C Datalec）最新稿仍为 2026-10-14/15 合并公告本身
   → 按 rules 第 12 条本期不提

## A1 · Wissen Research 数据中心冷却市场 —— 通过（仅核心三数字 + 口径可用）
- dateline `SHERIDAN, Wyo. , Nov. 11, 2026`；列表 `Nov 11, 2026, 13:44 ET`（一致）；`SOURCE Wissen Research LLC`
- 核心数字原文：`The global data center cooling market is valued at **USD 19.5 billion in 2026** and is projected to reach
  **USD 42 billion by 2031**, growing at a **CAGR of 16.5%** over the forecast period (**2026–2031**)`（FAQ 复述一致）
- **口径原句（稿中有明确定义，确认是整体冷却市场、不是仅液冷）**：
  `The data center cooling market covers the equipment, systems, and services used to regulate temperatures, remove heat, and
  maintain suitable operating conditions within data center facilities. It includes hardware and services for **air conditioning,
  chilling units, cooling towers, liquid cooling systems, economizer systems, control systems, and other components, deployed in
  room-based and row/rack-based configurations across hyperscale, enterprise, and colocation data centers. General data center
  infrastructure, IT hardware, and power distribution equipment are excluded.**`
- ⚠️ DOE COOLERCHIPS 1.5（1 MW/机架、称 2026-08-26 公布）与 Uptime 2025 调查 75%、ICEF 95% —— **均为 Wissen 对第三方的转述、
  本刊未取一手源 → 本期不引用**（挂回 open-items 另期去核 DOE / Uptime 一手）
- ⚠️ 厂商规格汇编**已确认是 Wissen 对各厂商公开规格的转述、不是其测算**（上文句式 `Suppliers are building out the hardware:`，
  无测算无方法无出处链接）→ **Vertiv CoolLoop 80 kW/机架、Boyd ROL2300 2.3 MW、JCI Silent-Aire 500 kW~>10 MW、
  Carrier CDU 1.3~5 MW 一律不引用**（本次最大误引风险点）
- 机构自述：`Wissen Research is a global market intelligence and consulting firm specializing in **healthcare, life sciences,
  technology, and emerging industries**`；地址 `Gould St, Ste R, Sheridan, WY 82801`；署名 `Mayur Jain, Research Expert`
- verifier 的证据强度提示（**按 rules 第 8 条不写进刊物**）：主业自述为医疗/生命科学；稿中无方法学说明；
  Sheridan WY 地址为业界常见注册代理地址；同机构同期在 PRN 密集发布跨行业报告稿
- URL https://www.prnewswire.com/news-releases/data-center-cooling-market-to-reach-us-42-bn-by-2031--growing-at-16-5-cagr-as-ai-racks-push-cooling-from-air-to-liquid-wissen-research-302936853.html

## 不得引用的数字清单（本期硬禁止）
1. Delta「3,000 W 计算部件」在**不加稿内归属矛盾说明**的情况下使用
2. 把 Project Deschutes 的 3 °C 趋近温差代入 800 VDC 2.5 MW L2L CDU
3. Frore 的 12 / 22 °C、+25% / +35% 在**不注明「稿中未给对比基线」**的情况下使用；严禁补「相对风冷」「相对常规冷板」
4. Frore「独角兽 / unicorn」及任何估值表述
5. Frore 的 20% / 26% 省能耗与水、100 MW≈135 MW、「三座顶四座」
6. Armada / JCI「10 MW Leviathan」与任何每台 MW 折算值
7. Armada / JCI「500 MW capacity」写成「产能」或「IT 容量」
8. Daikin 欧洲 CDU 的 400 kW~2.5 MW、「可十台联控」、订单开放日、稿日 2026-11-02
9. A1 转述的厂商规格：Vertiv CoolLoop 80 kW/机架、Boyd ROL2300 2.3 MW 与「支持 >10 个 NVL72 机架」、
   JCI Silent-Aire 500 kW~>10 MW、Carrier CDU 1.3~5 MW
10. A1 转述的第三方调研数字：DOE COOLERCHIPS 1.5、Uptime 75% / 35% / 22%、ICEF 95%、CBRE 9,432 MW 等整组、JLL 35 GW / 64%、
    印度 375→1,500 MW、Carrier Fort Worth、Schneider 班加罗尔
11. Chatsworth 的 18–33 kW 48V DC 电源托架、350–2500 A 母排**与散热容量混写**
12. Vertiv「3–5 倍」不标「厂商宣称」与基准

## 通道实测（供下期沿用）
| 通道 | 结果 |
|---|---|
| `www.prnewswire.com` 稿件页（fetch_source.py） | ✅ 9 篇全部正常，含完整正文与 dateline |
| `www.prnewswire.com/search/all/?keyword=…`（fetch_source.py） | ✅ **可取精确 ET 时间戳**，输出极省 token（500–2,600 字符）；比 `/search/news/?keyword=` 更准 |
| `www.daikin.eu`（带/不带 www） | ❌ fetch_source 403；WebFetch `getaddrinfo ENOTFOUND`（**域在白名单外，需维护者加白**） |
| `www.daikin.com/press/2026/` | ❌ 403 |
| `www.deltaww.com` / `www.delta-americas.com` | ❌ 均 403（deltaww 连续第二期） |
| `www.datacenterdynamics.com/en/news/`（fetch_source.py） | ✅ 列表页可读 |
| `www.datacenterdynamics.com/en/search/?q=…` | ❌ 403（**搜索路径被挡，与稿件页/列表页不同**） |
| `www.datacenterdynamics.com/en/news/cooling/` | ❌ 404（路径不存在） |
| businesswire / globenewswire | 未尝试（白名单外） |

## verifier 结论
- **无需进「更正」节**：未发现前期已归档周报内容与原文不符之处（Daikin、Delta 800 VDC CDU、Frore LiquidJet 均本期首次核验；
  3C Datalec 合并稿为 10 月事件、本期无新稿、不涉更正）
- `drafts/reported-index.md` 与 `drafts/open-items.md` 中检索 "daikin" **零命中** → F4 与专项 2 均非重复报道
- 建议挂回 open-items 三项：① Delta 800 VDC CDU 四参数（稿方未披露 + 两域连续 403）；
  ② Daikin 欧洲 CDU 稿（需加白 daikin.eu）；③ DOE COOLERCHIPS 1.5 与 Uptime 2025 调查的一手源
