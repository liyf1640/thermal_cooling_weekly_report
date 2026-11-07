# 第 12 期 · 产业侧对抗式核验报告

全部 A / C 组稿件由 verifier 逐条自己重新取原文、**完整读到稿末**（不依赖 scout 结论）。B 组按可达性尽力追一手。
工具：`python -I scripts/fetch_source.py <URL>`。PR Newswire 稿件的**精确 ET 时间戳**另从 PRN 站内搜索结果页核到。
⚠️ **工具侧要点**：`curl` 直取 `www.datacenterdynamics.com` 会撞 Cloudflare "Just a moment..." 挑战（只回 ~5.8 KB 壳页，
加 `--compressed` 也一样）；**只有 `fetch_source.py`（urllib）能穿过**。下期别浪费时间在 curl 上。

## A1 · Chemours Faizeon —— 通过（1 处 scout 遗漏、1 处口径必须改写）
- 发布 **2026-11-02**（首发日）。dateline `WILMINGTON, Del. , Nov. 2, 2026 /PRNewswire/`；PRN 时间戳 **16:30 ET**
- URL https://www.prnewswire.com/news-releases/chemours-launches-faizeon-two-phase-liquid-cooling-solutions-for-ai-data-centers-302926843.html
- 主体 `The Chemours Company ("Chemours") (NYSE: CC )` ✓
- **产品分档（逐字）**：
  - Faizeon™ 100 "A low-pressure two-phase direct-to-chip fluid"
  - Faizeon™ 110 "...with an **intermediate boiling point** and **zero ozone depletion potential**"
  - Faizeon™ 200 "A **high-performance** two-phase direct-to-chip fluid—and **industry standard for medium pressure systems**"
  - Faizeon™ 220 "Chemours' **highest-performance** two-phase direct-to-chip fluid"
  - Faizeon™ 500 "A two-phase **immersion** cooling fluid, **formerly Opteon™ 2P50 dielectric fluid**"
  → **500 确为 Opteon™ 2P50 改名，字面坐实**。注意 **100 与 110 都是 low-pressure**；「中压」只对应 200，
  且 200 的 "industry standard for medium pressure systems" 是**厂商自我定位、不是第三方认定**
- **ODP**：原文 "zero ozone depletion potential" = **ODP 为零**（非 near-zero）✓
  🔴 **GWP：稿中完全没有任何 GWP 数字或表述**（已全文 grep）→ 不得写 GWP
- 🔴 **19 °C 原文逐字**：
  > "In independent third-party testing , a two-phase direct-to-chip system using Faizeon™ 200 fluid maintained a Graphics Processing
  > Unit (GPU) at **up to 19 degrees Celsius lower** than a **single-phase, water-based fluid**, while using a **lower coolant flow rate**."
  - "up to" **确为原文措辞**；**测试方稿里没有点名**，只写 "independent third-party testing"
  - **GPU 型号未给、基准功率未给、流量低多少没有数字**（只有定性 "lower coolant flow rate"）
  - 比较基准 = "a single-phase, water-based fluid"（单相水基液），**不是某具体产品**
  - 口径必须写成：**厂商转述的未具名第三方测试结果**，测试工况全部未披露
  - 🔴 **严禁把 ORNL 接到这个测试上**：19 °C 那段与伙伴名单是**两个互不相连的段落**，稿中没有任何一句把 ORNL
    （或名单上任何一家）指为测试执行方
- **合作方 7 家字面核准，但「角色」稿里一个字都没写**：
  > "These efforts include **engagements with** the **U.S. Department of Energy's Oak Ridge National Laboratory (ORNL)**,
  > **NTT DATA**, **2CRSi**, **DataVolt**, **Munters**, **Accelsius**, and **ZutaCore**."
  🔴 **唯一的关系词是 "engagements"（合作/接洽）**。客户 / 测试伙伴 / 联合开发，稿中一个都没说 → 不得给任一家派定角色
- **引语归属**：**Denise Dignam, President and CEO at Chemours**（⚠️ 职务是 **President and CEO**，scout 只写 CEO）：
  > "With our liquid cooling solutions, we are applying **more than 90 years of thermal management expertise** to help data centers
  > manage higher heat loads while improving performance and dramatically reducing energy and water demand."
- **用水**：原文 "Faizeon™-enabled systems **can nearly eliminate cooling-related water use**, **depending on system design and
  operating conditions**." → ⚠️ 两处 scout 不准：(a) 限定是**系统设计与运行工况**（scout 漏了后半）；
  (b) 对象是 **cooling-related water use（冷却相关用水）、不是全站用水**；且是 "can"（能够）、非既成
- **稿里没有的**：价格、产能、上市/供货时间、第三方测试报告链接、业务部门归属、PFAS 表述、GWP、沸点数值、压力数值。唯一外链 "Learn more at Faizeon.com"
- ⚠️ **确认稿内零冷板硬件内容**。全篇定位为 "dielectric fluids"（介电流体），面向两相 D2C 与两相浸没两种架构
  → **这是冷却液条目、不是冷板硬件条目**
- 其他可用（定性无数字）：相变传热机理；"Systems designed for Faizeon™ fluids **can reduce** the energy required for data center cooling"（无数字）；
  "Fluid circularity: ... engineered to support recovery, reprocessing, and reuse"
- boilerplate：约 5,700 员工、28 个生产基地、约 2,400 客户、约 110 个国家；三大业务 Thermal & Specialized Solutions / Titanium Technologies / Advanced Performance Materials
  🔴 稿中**未说** Faizeon 归哪个业务部门，不得推断
- 待确认项：无（第三方测试方身份属**稿方未披露**，不是取数失败）

## A2 · Vertiv SmartIT —— 通过
- 发布 **2026-10-26**（首发日），`COLUMBUS, Ohio , Oct. 26, 2026`；PRN 时间戳 **17:12 ET** ✓
- URL https://www.prnewswire.com/news-releases/vertiv-simplifies-high-density-ai-infrastructure-deployment-across-data-center-environments-302919919.html
- **产品名**：正式名 **"Vertiv™ SmartIT"**。副标题称 "platform"、正文称 "solution"，**两种说法同稿并存**，无更长全称 → 写「Vertiv™ SmartIT」最安全
- **架构基础**：`Based on NVIDIA MGX™ and OCP ORV3 architectures`；正文另处展开为 `NVIDIA MGX™ and Open Compute Project (OCP) ORV3 architectures` ✓
- **集成项原文**：
  > "integrates **rack infrastructure**, **DC power conversion and distribution**, **direct-to-chip liquid cooling**,
  > **in-rack cooling distribution** and **monitoring** in a factory-validated design."
  - ⚠️ scout 写「DC 配电」不全 —— 原文是 **"DC power conversion and distribution"**（DC **变换** + 配电）
  - 🔴 **"in-rack cooling distribution"：稿中全篇没有 "CDU" 三个字母**（已全文确认）→ **不得译注为「机架内 CDU」**，只能照字面写「机架内冷却分配」
- **支持平台**：`NVIDIA GB300 NVL72`、`NVIDIA Vera Rubin NVL72`、`NVIDIA DGX™ Rubin NVL8`、`NVIDIA HGX™ Rubin NVL8` ✓ 四个全核准
- 🔴 **供货口径原文**：**"The solution is available now for AI deployments globally."**
  → 不是 "generally available"、也不是 "shipping" → 只能写「**稿称现已可用于全球 AI 部署**」，**不得写成「已出货」「已量产」**
- **与 DGX GB300**：原文 "**Previously deployed with NVIDIA to support** the NVIDIA DGX™ GB300, the highest-performing,
  largest-scale AI system available for enterprises." → 是**已部署**、不是仅验证。（"highest-performing, largest-scale" 是稿中厂商形容词）
- **GTC Berlin**：原文 "Vertiv showcased a Vertiv™ SmartIT with a NVIDIA HGX™ Rubin NVL8 **demo unit** during NVIDIA GTC Berlin **in October**"
  → ⚠️ **只给月份，稿中无具体日期**，不得补日期
- Redfish / SNMP / Modbus ✓；引语 **Scott Armul, Chief Product and Technology Officer at Vertiv** ✓ 职务字面一致
- 🔴 **热/冷却性能数字：确认全篇为零。** 无机架功率 kW、无 CDU 容量、无冷板规格、无供液温度、无热捕获率。
  **整篇唯一的「数字」就是产品型号里的数字（GB300、NVL72、ORV3、NVL8）** → 纯架构/集成度条目
- 其他可用：集成漏液检测 + 自动响应 + 持续监测（"built into the solution from day one"）；可从单机架扩到多机架、阶段间无需重设计；
  适用棕地企业机房与 Class A 商业楼；配套 **Vertiv™ SmartRun**、**Vertiv™ rPDU**、**Vertiv™ Unify**；Vertiv™ Global Services 支持部署/调试/生命周期
- 稿里没有的：价格、客户名、出货量、订单、任何容量数字

## A3 · Modine FY2027 Q2 —— 通过（⑨ 的结论对本刊最重要）
- 发布 **2026-11-03**，`RACINE, Wis. , Nov. 3, 2026`；PRN 时间戳 **16:15 ET** ✓。主体 `Modine (NYSE: MOD )`，财季截至 **2026-09-30**
- URL https://www.prnewswire.com/news-releases/modine-reports-second-quarter-fiscal-2027-results-302928192.html
- **数据中心分部**（逐字核准）：
  > "Data Centers segment sales were **$439.7 million**, compared with **$225.0 million** one year ago, an increase of **95 percent**.
  > This increase was **primarily driven by higher sales to hyperscale customers in North America**."
- **分部毛利率**：
  > "The segment reported gross margin of **19.7 percent**, which was **470 basis points lower** than the prior year.
  > This decrease was **primarily due to higher material, component and tariff costs**."
  （分部另有：营业利润 $61.2M、+70%；调整后 EBITDA $67.6M、+66%）
- **公司总销售额** $994.4M、+$255.5M / **+35%**，上年同期 $738.9M ✓。整体毛利率 20.7%（降 160 bps）；调整后 EBITDA $136.2M（+31%）；
  净利 $30.3M（−32%，含 $29.5M 与分拆相关的法人重组所得税）；EPS $0.56（−33%）；调整后 EPS $1.35（+27%）
- **「订单与积压创纪录」归属**：**Neil D. Brinker, Modine President and Chief Executive Officer** 引语：
  > "Demand for our products remains very robust, highlighted by **record orders and backlog in our Data Centers segment** and
  > expanding opportunities to serve the data center cooling market within Commercial HVAC."
  🔴 **CEO 引语、无任何数值** → 必须写成「CEO 表述」，不得写成公司披露的数据
- **分拆**：Highlights 字面 "Completed the spin-off of Performance Technologies **on October 1**"；前瞻声明段全写 "**October 1, 2026**" → **有稿内出处** ✓
- **FY2027 指引**（表格 "Fiscal 2027 Current Outlook"）：Net Sales **$3.1 to $3.2 billion** ✓；Adjusted EBITDA **$470 to $500 million** ✓
  CEO 引语给增速：revenues "+**50 to 55 percent** from the prior year, **excluding Performance Technologies from both periods**"；
  调整后 EBITDA 增速 "**in excess of 50 percent**"，同样剔除 PT
  → ⚠️ **+50~55% 必须带「两期均剔除 Performance Technologies」**，否则是错的；且出自 CEO 引语。自第三财季起 PT 按**终止经营**列报
- **投资者日**：原文 "our upcoming **Analyst and Investor Day** on **November 18**"（出自 CEO 引语，未写年份）✓。另有 11-04 电话会
- ⑨ 🔴 **关键结论：稿中完全不区分液冷与风冷。**
  全文 33,271 字符 grep：`liquid` 的全部命中都是 "**liquidity**"（流动性），**没有一次是 "liquid cooling"**；
  `cold plate` / `CDU` / `coolant` / `immersion` / `air-cooled` **零命中**。分部披露只到 Data Centers / Commercial HVAC / Performance Technologies
  → **+95% 是数据中心分部整体销售额增速，绝对不能读作液冷增长、也不能读作冷板或 CDU 增长。必须在成稿里写死。**
  稿中与冷却沾边的措辞仅为定性：「data center cooling products」（现金流段）、「the data center cooling market within Commercial HVAC」（CEO 引语）
- 其他：六个月经营活动净现金流出 $57.1M；自由现金流 −$145.6M，主因「为扩大数据中心分部产能的资本支出上升」与「为支撑数据中心冷却产品需求增长而增加的库存」；
  总债务 $724.3M、现金 $150.6M、净债务 $573.7M；重组费用 $3.0M、分拆相关费用 $14.1M；已与多家战略供应商签长期协议锁定关键部件；全球员工 9,000+
- 稿里没有的：积压绝对值、客户名、液冷/风冷拆分、产品级容量或温度数字、数据中心分部产能数字

## A4 · Gradian Thermal Solutions Dayton 新厂 —— 通过（④ 翻案：780,000 确为稿中数字；② 补到关键背景）
- 发布 **2026-10-28**，`DAYTON, Minn. , Oct. 28, 2026`；PRN 时间戳 **08:00 ET** ✓
- URL https://www.prnewswire.com/news-releases/gradian-expands-manufacturing-footprint-with-new-500-000-square-foot-facility-in-dayton-minnesota-302921866.html
- ② 🔴 **公司全称与前身 —— 已补到一手出处**
  - 本稿主体字面 **"Gradian Thermal Solutions"**（SOURCE 行亦同）✓。本稿内**没有**母公司/前身信息
  - 顺 PRN 同源稿追到一手：**2026-08-19 09:15 ET** Gradian 稿字面：
    > "**Gradian Thermal Solutions**, which recently launched as the **unified parent brand of MAS HVAC, Daedex, DeepCoolAI and Ecochillers**"
    URL https://www.prnewswire.com/news-releases/ecochillers-brings-expanded-thermal-solutions-portfolio-to-the-gradian-platform-302854624.html
    同稿 boilerplate：「Through its combined capabilities across MAS HVAC, Daedex, DeepCoolAI, and Ecochillers, Gradian offers a
    comprehensive portfolio of liquid cooling, air handling, chiller, and modular HVAC solutions」；**CEO = John Schneider**
  → 首次收录可写「Gradian Thermal Solutions，系 MAS HVAC / Daedex / DeepCoolAI / Ecochillers 的统一母品牌（2026-08-19 一手稿）」
  ⚠️ 四家子品牌里**哪家做液冷，两份稿都没说**（"DeepCoolAI" 听着像，**不得推断**）
- ③ 新厂：**500,000** 平方英尺 ✓；投资 **approximately $60 million** ✓；"Production began at the facility **in June**, and Gradian
  **continues to ramp up capacity**" ✓ → ⚠️ 稿中只写 **"in June"、没写年份**（稿发于 2026-10，上下文为 2026 年 6 月）
- ④ 🔴 **780,000 是稿中数字，scout 顾虑解除**：
  > "Together with the company's **180,000**-square-foot Maple Grove, Minnesota facility and the **100,000**-square-foot facility in
  > Guadalajara, Mexico, the Dayton expansion brings Gradian's manufacturing footprint to **approximately 780,000 square feet**"
  → 三个数字全部稿中明写，780,000 带 "approximately"，且与 500+180+100 自洽。另：Maple Grove 是**总部**
- ⑤ 🔴 **员工口径**：
  > "The company also **expects to grow** its workforce from **approximately 150 employees** to **around 1,000 companywide**."
  → **口径是 companywide（全公司）、不是该厂**；**是预期（expects）、不是已完成**；**稿中无时间框架** —— 三点都必须标清
- ⑥ **产品线**："spans **liquid cooling, chillers, air handling, commissioning products, and prefabricated solutions**"
  → ⚠️ scout 漏了 **"commissioning products"**（调试类产品），五项应写全
  "The facility includes assembly lines, fabrication equipment, and an **end-of-line testing lab for our chiller product line**"
  → 出厂测试实验室**专属冷水机产品线** ✓。COO 引语提 "vertically integrated operating model"
- ⑦ 引语 **Jason Ulett, Chief Operating Officer of Gradian** ✓
- ⑧ 🔴 **液冷具体指向：确认稿中完全没说。** "liquid cooling" 仅作为产品组合的一个类目出现（正文一次、boilerplate 一次），
  **无冷板、无 CDU、无歧管、无任何液冷容量/温度/流量数字** → **只能作为「液冷相关产能扩张」收录，不得具体化到冷板或 CDU**
- 稿里没有的：客户名、营收、液冷产品细节、投产产能数字、分产品线产能、Dayton 新厂具体产线类型

## A5 · Vertiv 2026 Q3 —— 通过（但仅作财务信号，⑦ 结论决定收法）
- 发布 **2026-10-28**，PRN 时间戳 **05:55 ET** ✓。主体 `Vertiv Holdings Co (NYSE: VRT )`，季度截至 2026-09-30
- URL https://www.prnewswire.com/news-releases/vertiv-reports-strong-third-quarter-2026-with-net-sales-growth-of-61-organic-orders-growth-over-100-and-diluted-eps-growth-of-91-adjusted-diluted-eps-growth-of-78-raises-full-year-2026-guidance-across-all-key-metrics-302921936.html
- 净销售 $**4,313** million、+$1,637M、**+61%**；**55% organic** + **约 6% 来自并购** ✓
- 地区 `the Americas up 75% (66% organic), APAC up 50% (48% organic), and EMEA up 23% (19% organic)` ✓
- 🔴 **「有机订单 +100% 以上」的归属**：两处 —— (a) **稿件标题** "Organic Orders Growth over 100%"；(b) **CEO 引语**
  > "**Our more than 100% organic orders growth year over year** and our overall performance are clear testaments to that."
  > —— **Giordano Albertazzi, Vertiv's Chief Executive Officer**
  🔴 **正文数据段/表格中没有独立的订单数据行**（43,580 字符全文 grep：`orders` 仅命中该引语与风险因素段）
  → 成稿请写成「公司称 / CEO 称」
- 调整后经营利润率 **25.2%**、+290 bps ✓；调整后经营利润 $1,087M（+83%）；经营利润 $984M（+90%）
- 指引逐项核准：全年 Net sales **$14,450M–$14,850M** ✓、中值 **$14,650M** ✓、上调 **$650 million** ✓
  🔴 **Q4 指引 Net sales 原文字面就是 `$4,313M - $4,513M`** —— 与 Q3 实际 $4,313M **确实完全相同，不是 scout 抄错**；
  算术自洽：(4,313+4,513)/2 = 4,413，与 Highlights 的「Q4 中值 $4,413 million」一致 → 可照写，建议加括注说明
  其他：Q4 有机增长 49–51%；Q4 调整后经营利润 $1,118–1,158M、利润率 25.3–26.3%、调整后 EPS $2.22–2.28；
  全年有机增长 37–39%、调整后经营利润 $3,475–3,555M、利润率 23.5–24.5%、调整后 EPS $7.10–7.20、调整后自由现金流 $2,600–2,800M。
  摊薄 EPS $1.95（+91%）、调整后摊薄 EPS $2.21（+78%）；经营净现金 $794M（+64%）、调整后自由现金流 $652M（+50%）；流动性 **$6.2 billion**；全年资本开支约占营收 4.0%
- ⑦ 🔴 **结论：稿内没有任何液冷 / 冷板 / 分产品线的冷却数字。**
  全文 grep：`cooling` **只命中 boilerplate 一处**（"a portfolio of power, cooling and IT infrastructure solutions"）；
  `liquid cooling` / `cold plate` / `CDU` / `coolant` / `immersion` **零命中**。分部披露是**地区分部**，产品维度只拆到 "**Products**" 与 "**Services & spares**"
  → **纯合并财务条目** → 建议**不进「产业动态」正节的技术条**
- ⑧ 🔴 **稿中不披露 backlog 绝对值**（`backlog` 唯一命中在风险因素段）→ 已排除的「2025 年末 USD 15.0bn」**本稿无任何支持，确认无可乘之机**
- 第二条引语归属：**Dave Cote, Vertiv's Executive Chairman** —— ⚠️ 别把 Cote 的话记到 Albertazzi 头上
- **附带新排除项**：PRN 同名搜索里 **Oct 28, 2026, 14:37 ET** 有一篇《From Cooling to Backup Power, Data Center Demand Is Showing Up
  in Quarterly Results》，发稿主体是 **"Equity Insider"**（付费股评/荐股稿、非 Vertiv 发布）→ **不得当作一手稿或行业事实引用**

## A6 · Vertiv 完成收购 UIG —— 通过，但建议只进公司清单
- 发布 **2026-10-27**，`COLUMBUS, Ohio , Oct. 27, 2026`；PRN 时间戳 **06:30 ET** ✓
- URL https://www.prnewswire.com/news-releases/vertiv-completes-acquisition-of-utilityinnovation-group-302919810.html
- 🔴 **被收购法人全称**：`Utility Innovation Holdings, Inc., which operates as UtilityInnovation Group ("UIG")`；收购方是 Vertiv 全资子公司 **Vertiv Corporation**
- "for **approximately $1.45 billion** in **upfront cash**" ✓；"additional **contingent consideration of up to $1.15 billion** in cash
  based on achieving certain **EBITDA** targets over **12- and 24-month** periods" ✓；"approximately **13x expected UIG 2027 EBITDA**" ✓
  另有 "The EBITDA multiple is anticipated to be **significantly lower if the full earnout is paid**"；预计**完成后第一年**对调整后 EPS 增厚
- UIG 业务副标题字面 "**microgrid controls, onsite generation orchestration, microgrid-specific switchgear and behind-the-meter power
  architecture**" ✓；正文另处为 "microgrid controls, **onsite generation and energy storage orchestration**, and behind-the-meter power architecture"（多了储能编排）
  UIG：2020 年成立，总部北卡 Raleigh，欧洲总部爱尔兰都柏林，北卡与新泽西有制造
  顾问：J.P. Morgan Securities LLC（Vertiv 财务）、Buchanan Ingersoll & Rooney PC（Vertiv 法律）、Morgan Stanley & Co. LLC（UIG 财务）、Davis Polk & Wardwell LLP（UIG 法律）
- ④ 🔴 **与冷却的关系比 scout 说的更细**：稿中 "cooling" **出现了**，但**全部指 Vertiv 自己既有的组合**、不是 UIG 带来的能力：
  副标题 "**Extends Vertiv's power and cooling portfolio from grid interconnect to chip**"；正文结尾 "Vertiv's end-to-end portfolio of
  **power and thermal management** systems"；CEO 引语 "a coordinated solution, **from behind-the-meter power generation to chip**"
  → **UIG 本身零冷却/热管理技术**；稿中无液冷、无冷板、无 CDU、无任何热数字
  → **同意只记入公司清单、不进刊物正文。** 另该交易本刊**第 6 期已以「2026-09-02 宣布、待交割」收录**（companies.md 第 14 行），
  本期增量只有「已交割 + 约 13 倍 2027E EBITDA + 12/24 个月对价期」→ 增量有限，支持不进正文
- ⑤ **引语归属**：**Giordano Albertazzi, Vertiv CEO**；**Sidney Hinton, Founder and CEO of UIG**
  🔴 **「解决拖慢 AI 数据中心建设的电力瓶颈」这句是 UIG 的 Hinton 说的、不是 Vertiv 说的**

## B1 · nVent × AMD Helios 双后门 RDHx —— **部分翻案：待确认（可刊）**
- 可读 URL https://www.datacenterdynamics.com/en/product-news/nvent-and-amd-collaborate-on-cooling-for-amd-helios-rackscale-solution/
- 一手不可达已复核：`www.globenewswire.com`、`www.nvent.com`、`investors.nvent.com`、`www.stocktitan.net` 全部代理 **connect_rejected**；
  DCD 站内搜索 403；PRN 站内无 nVent/AMD 一手稿
- ① 🔴 **是否官方通稿全文转载 —— 判据与结论**
  页面结构（全文仅 3,597 字符，已完整读完）：
  `Home / Product News / The Compute, Storage & Networking Channel / **Sponsored** / <标题> / <副标题> / October 15, 2026 / **By** / **Press Release** / ...`
  - ✅ 有 **"Press Release" 署名**（DCD 把作者栏填为 "Press Release"）；✅ 版位明确标 **"Sponsored"**；✅ 文风为纯通稿体（"nVent and AMD **today announced**…"）
  - ❌ **无 boilerplate**（没有 "About nVent"、没有 "About AMD"）；❌ **无媒体联系人**；❌ **无 "NYSE: NVT" 字样**
    🔴 → **(NYSE: NVT) 不能从这个页面取证**
  → **结论：是厂商提供的通稿正文，经 DCD 以 "Press Release" 署名在赞助版位刊出，但不是完整通稿**（被裁掉公司简介段与媒体联系人）
  → **可以用**，但措辞必须是「**nVent 通稿正文，经 DataCenterDynamics 以 Press Release 署名于赞助（Sponsored）版位刊出**」，
  **不得写成「nVent 官方新闻稿」或「官方新闻稿全文转载」**。证据强度：**介于一手与二手之间，高于记者改写，低于公司 newsroom 原稿**
- ② **页面标注日期 October 15, 2026**。🔴 **这是 DCD 的刊出日、不能确定是首发日**。
  一条内证支持它晚于首发：正文写 "nVent **will unveil** a first look at the OCP Global Summit in San Jose, CA, **October 12 to 16, 2026**"
  —— 用**将来时**谈一个 10-12 已开幕的会期，说明文案成稿早于 10-12，而页面日期 10-15 已在会期中段
- ③ **首发日：🔴 未核。** GlobeNewswire 全站、nVent 官网与 IR、StockTitan 均被代理拒连；DCD 站内搜索 403；PRN 无此稿。
  scout 的 `gnwcq-2026-10-13` / "October 13, 2026 via GlobeNewswire" **来自检索结果页、未直读，verifier 亦无法确认**
  → **成稿请明确写「首发日未核，仅 DCD 刊出日 2026-10-15 可核」**，日期写 **2026-10-15**，**不要写 10-13**
- ④ 内容逐项核（全部核准，一处 scout 用词需改）：
  - nVent **rear door heat exchanger (RDHx)** 纳入 **AMD Helios Rackscale solution** ✓
  - Helios 平台组成 `AMD Instinct graphical processing units (GPUs), EPYC central processing units (CPUs), Pensando networking technologies, and the AMD ROCm open software stack` ✓
  - 🔴 原文字面「nVent's **DC-powered RDHx** is an **industry-first dual rear door**, designed for the **double-wide AMD Helios rack**.」
    → 这是**厂商宣称的「业内首款」**，必须标清口径
  - 🔴 **房间中性的原文是 "effectively room-neutral"、不是 "virtually room neutral"**（scout 猜错）。完整原句：
    「It **captures the heat that direct-to-chip liquid cooling leaves behind** and **returns cooled air to the space**, keeping the rack **effectively room-neutral**.」
  - 传感与调速「offers **intelligent cooling with no wasted watts**, integrated **air temperature, humidity sensors** and
    **differential pressure fan speed control**」✓（"no wasted watts" 是厂商宣传语、无数字支撑）
  - 「its **DC power** matches how next-generation AI racks are powered」；「allows customers to **start with a single rack and scale larger deployments over time**」
  - 展出「nVent will unveil a first look at the **OCP Global Summit in San Jose, CA, October 12 to 16, 2026**」；
    「will show the RDHx **for the first time on an Open Rack Wide (ORW) rack** alongside the **manifolds, bus bars, and power shelves** of a Helios deployment」；「Visit **Booth #A9** at OCP」✓
    ⚠️ 会期按本页字面是 **10-12 至 10-16**（与别处 10-12~15 不一致 —— **各稿按各自字面写，不要互相校正**）
  - 副标题「nVent will add **liquid and air cooling** solution to AMD rack-scale AI platform to create a fully integrated system for large AI workloads」
- ⑤ **引语归属（职务字面逐字核准）**：
  - **Eric Osborn, vice president and general manager of Data Solutions, Cooling & Power at nVent** ✓
  - **Ravi Pendekanti, corporate vice president of the Data Center Solutions Business Group at AMD**：
    「**The rack, not any single component within it, has now become the unit of deployment**; and compute, networking, software, power and cooling must operate as one system.」✓
  （页面上 Pendekanti 第一段引语缺收尾引号，属 DCD 排版缺陷，不影响归属）
- ⑥ 🔴 **确认稿中无热容量（kW）、无价格、无上市时间、无订单。** 全文唯一数字是 OCP 会期日期与 Booth #A9
- ⑦ 🔴 **排除项确认：页面里没有混入这两项。** "225–245 kW/机架" **零命中**；"RDHX Pro 78 kW @ 14 °C" **零命中** → 本证据页干净
- ⑧ **结论：可刊，判定「待确认」。** 待确认项：① 首发日期与首发渠道；② nVent 官方通稿全文；③ RDHx 热容量/上市时间/价格（**稿方未披露、非取数失败**）

## B2 · Nidec NIR3.0 3.2 MW 在排 CDU —— 待确认（证据强度只够二手记者报道）
- 可读 URL https://www.datacenterdynamics.com/en/news/nidec-anounces-32mw-in-row-cdu/
- 一手（mynewsdesk）不可达；另试 `www.nidec.com`（含 `/en/corporate/news/…`）→ 代理 **connect_rejected**；PRN 搜 "Nidec coolant distribution" → **0 条**。**一手完全追不到**
- ① 🔴 **性质判定：是记者报道、不是通稿转载。**
  页面结构 `Home / News / **The Data Center Cooling Channel** / <标题> / <副标题「New unit to enter mass production next year」> / October 27, 2026 / By **Dan Swinhoe**`
  - 署名是 **DCD 记者 Dan Swinhoe**（非 "Press Release"）；**无 "Sponsored" 标记**（与 B1 形成对照）；无 boilerplate、无媒体联系人；
    文风为第三人称报道体（"The company **recently officially announced**…"）
  → **DCD 自采/编译报道，证据等级明显低于 B1。全文仅 2,133 字符**
- ② DCD 页字面核到的事实（均为 DCD 转述 Nidec）：
  - 产品名 **"Nidec In-Row Coolant Distribution Unit, NIR3.0"** ✓
  - 「will deliver a **maximum cooling capacity of 3.2MW**」✓ —— **厂商标称最大值，工况未给**
  - 「with **full compatibility with the 800VDC** high-voltage direct current power standard」✓
  - 「Nidec aims to **begin mass production in the first half of 2027**」✓ —— 是**目标**（aims to）
  - ⚠️ DCD 写 "**recently** officially announced"，**原始发布日页面未给**
  - 🔴 **口径提醒**：「Supporting 800VDC **will reduce power conversion and transmission losses** compared to traditional AC or
    lower-voltage DC systems, **potentially helping improve PUE**」—— 这是 **DCD 记者的分析、不是 Nidec 的宣称**，
    不得归到 Nidec 头上，也不得作为产品性能
- ③ **OCP 2026 原型 / Booth #E63：🔴 未核，且 DCD 页里完全没有。** 全文无 "OCP"、无 "booth"、无 "prototype"
  → **「原型」与「Booth #E63」两项均不可写**
- ④ **趋近温差、流量、尺寸：DCD 页中全部没有**
- ⑤ **公司全称 Nidec Corporation**（"Japan's Nidec Corporation"），1973 年成立，旧名 **Nippon Densan Corporation**；
  DCD 另称该公司「also develops **in-rack and in-row CDUs and cold plates**」。🔴 具体事业部/子公司稿中未给，不得推断
- ⑥ **结论：待确认，倾向只作线索。** 最低标注要求：「据 DataCenterDynamics 2026-10-27 报道（记者 Dan Swinhoe，非通稿）：
  Nidec Corporation 公布在排式 CDU NIR3.0，**厂商标称**最大制冷量 3.2 MW、兼容 800 VDC，**目标** 2027 年上半年量产；
  工况、ATD、流量、尺寸均未披露，一手稿未取到。」

## B3 · 三条结案意见
- ① **Cooler Master 2,500 kW CDU —— 同意结案为「二手来源不可用」。** 本期再次实测 `www.coolermaster.com/en-global/news/` → HTTP 000 / 代理拒连，
  **连续三期不可达**。在没有一手稿能裁定哪个数字为真的情况下，**任何一个数字都不能写**。
  **建议把「990 GPM / 1,500 LPM / 2,500 kW / 2,500 MW / ATD 4–5 °C」整组数字写入排除清单**，避免下期有人只捡其中一个来用
- ② **Polar Data Centers 41 MW / 100 MW —— 同意本期不新写，但⚠️ 不要撤回第 11 期已有记录。**
  实测 `polardatacenters.com` → HTTP 000。
  🔴 **纠正这条挂账的前提**：`companies.md` 第 45 行显示，**41 MW / 可扩至 100 MW 是有一手出处的 —— 出自 Vertiv 2026-10-21 一手稿**，
  第 11 期已如实记为「**MW 口径（供电 / IT 负载 / 制冷容量）稿中未说明 → 待确认**」。
  所以不是「41/100 MW 未核」，而是「**其量纲口径未核**」，且已正确标注
  → **本期不新增 Polar 条目；第 11 期原记录维持不变、不需更正**；搜索里的「约 40 MW 初期、PUE 目标 1.12」**追不到一手，继续排除，
  且不得与 41/100 MW 并列或互相印证**
- ③ **Delta 800 VDC L2L CDU 的 ATD —— 建议从「挂账待补」改判为「原稿未披露，结案」。**
  实测 `www.deltaww.com/en-US/news` → HTTP 000。更关键：`companies.md` 第 42 行显示第 11 期已逐字核过那份 2026-10-15 一手稿，
  并明确记载「**ATD、供回水温度、尺寸、冗余等级稿中均未给**」。既然**一手稿本身就没有这个数**，这不是取数失败而是**稿方未披露**；
  继续当作可补的挂账挂下去，**会诱使后续周期去二手源凑数**
  → 保留第 11 期禁令：**SuperCDU-1500 与 GoCool 系列的 4–7.5 °C ATD 是别的型号，不得套用、不得并列、不得作为「同厂参考值」**；
  ATD 亦不可与第 10 期 LITEON × DCX 的「2.6 MW + ATD 3 °C + N+1」互相代入

## C1 · MarketsandMarkets CDU 市场 —— 通过（限「前瞻分析」节）
- 发布 **2026-10-26**，`DELRAY BEACH, Fla., Oct. 26, 2026`；PRN 时间戳 **06:59 ET** ✓
- URL https://www.prnewswire.com/news-releases/data-center-coolant-distribution-units-market-worth-10-02-billion-by-2033---exclusive-report-by-marketsandmarkets-302919164.html
- **市场规模（逐字）**：
  > "projected to grow from **USD 1.41 billion in 2026** to **USD 10.02 billion by 2033**, at a **CAGR of 32.3%** during the forecast period"
  预测期 = **2026–2033**（稿中 "CAGR (2026-2033): 32.3%" 明写）
- **四个百分比的口径各不相同，必须分别标**：
  | 数字 | 原文口径 |
  |---|---|
  | in-row CDU **54.3%** | "accounted for a share of 54.3% **in terms of value** in **2025**" —— 按**价值**、**2025 年**份额 |
  | 超大规模 **77.0%** | "accounted for the largest share of 77.0%, **in terms of value**, in **2025**" —— 按**价值**、**2025 年**份额 |
  | 直连芯片冷却 **34.3%** | "expected to register the highest CAGR of 34.3% **during the forecast period**" —— 🔴 **此条原文没有 "in terms of value" 限定**，只能写「预测期内最高 CAGR」，**不得自行补「按价值」** |
  | 北美 **33.1%** | "projected to grow at the highest CAGR of 33.1%, **in terms of value**, during the forecast period" —— 按**价值**、预测期 |
  → 两个份额是 **2025 年**基准，两个 CAGR 是 **2026–2033** 预测期。**不要把「按价值」统一加到四条上**
- **方法论与基准年：🔴 稿中未披露方法论。** 只给报告规格「Market Size Available for Years: **2021–2033**」「**200** market data Tables、**59** Figures、**263** Pages」。
  **没有任何 "base year" 字样**；基准年只能从份额数据是 2025、规模起点是 2026 推得 —— **属推断，不得写成稿中声明**
- ⑥ 🔴 **稿内转述的第三方事实 —— 全部不得采用，记入排除清单**：
  1. **Vertiv 350 kW 与 2.3 MW CDU**：「Vertiv, for example, has introduced **350 kW and 2.3 MW CDUs**…」—— M&M 转述的 Vertiv 产品规格。
     （本刊 companies.md 第 14 行已有经一手核过的 2.3 MW CoolChip 记录；**要用就用本刊自己核过的那份出处，不要引 M&M 这段**；
     **350 kW 一档本刊尚无一手出处**）
  2. **Uptime Institute 2025 调查「69% 受访者」**
  3. **Uptime Institute 2026 表述**（二手转述、无数字）
  4. **融资年表（整组）**：2020 年 2 笔共 **USD 166.2M**；2021 年 4 笔 **USD 64.6M**；2022 年 3 笔 **USD 86.7M**；2023 年 1 笔 **USD 17.0M**；2024 年 1 笔 **USD 20.0M** —— 来源未注
  5. **M&M 自家厂商评级**：「star players」= Schneider Electric、Vertiv Group Corp.、Delta Electronics, Inc.、nVent、DCX Liquid Cooling Systems；
     「startups and SMEs」= Nortek Air Solutions、Excool Ltd、LNEYA Thermo Refrigeration Co., Ltd. —— **分析师主观评级、非事实**
  6. **Key Players 的国别标注** —— M&M 标注，不作本刊公司国别依据
  7. 「CDUs are increasingly being deployed at the **hundreds-of-kilowatts-to-megawatt scale**」—— 无出处的定性量级描述
  8. 「In 2025, North America emerged as the leading…market」—— M&M 自家结论

# 汇总
**可进「产业动态」正节（3 条）**：A1 Chemours Faizeon（2026-11-02）、A2 Vertiv SmartIT（2026-10-26）、
B1 nVent × AMD Helios RDHx（**2026-10-15 DCD 刊出日；首发日未核**，本期翻案、判「待确认」可刊）
**可进正节但属需求侧财务信号（2 条，建议明示无冷却拆分）**：A3 Modine FY27 Q2（2026-11-03）、A4 Gradian Dayton 新厂（2026-10-28）
**只进公司清单、不进正文（2 条）**：A5 Vertiv 2026 Q3（2026-10-28，纯合并财务）、A6 Vertiv 完成收购 UIG（2026-10-27，电力侧）
**只进「前瞻分析」节（1 条）**：C1 MarketsandMarkets CDU 市场（2026-10-26）
**挂账 / 结案**：B2 Nidec NIR3.0（待确认，只作线索）、B3-① Cooler Master（结案，整组数字入排除清单）、
B3-② Polar 41/100 MW（本期不写，**第 11 期记录无需更正**）、B3-③ Delta ATD（建议改判「原稿未披露，结案」）
**对已归档周报的更正：无。**（verifier 另复核了 companies.md 中与本期相关的既有记录 —— Vertiv UIG（第 6 期）、
Vertiv 2.3 MW CoolChip（第 7 期）、nVent Blaine 扩产（第 5 期）、Delta 800 VDC L2L（第 11 期）、Polar 41/100 MW（第 11 期）
—— 均与可读原文一致，不需更正。）
**新增建议入排除清单**：C1 稿内 8 组转述内容；《From Cooling to Backup Power…》（PRN 2026-10-28 14:37 ET，主体 "Equity Insider"，付费股评稿）；
「nVent (NYSE: NVT)」不得标到 B1 的证据 URL 上
**复核后确认不可达**：`www.globenewswire.com`（含文章页）、`www.nvent.com`、`investors.nvent.com`、`www.stocktitan.net`、
`www.nidec.com`、`www.coolermaster.com`、`polardatacenters.com`、`www.deltaww.com` —— 均代理 connect_rejected；
`www.datacenterdynamics.com/en/search/` → 403（文章页本身可读）
⚠️ **工具提示**：`curl` 直取 DCD 文章页会被 Cloudflare 挑战拦住；**DCD 必须用 `scripts/fetch_source.py`**
