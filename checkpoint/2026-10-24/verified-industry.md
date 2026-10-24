# 产业侧 + 分析师侧逐位核验结果（verifier 回传，原样存档）

全部 7 篇都从 www.prnewswire.com 一手稿**整篇读完**（fetch_source.py --limit 60000，落盘后逐行读）。**7 条全部不否决**，但有 4 处必须改写的口径/归属错误（I2「now shipping」、I4「US$400M」、I3 泵冗余、I1 口径），以及 1 处跨期口径分离（N1 vs 第 9 期）。

## I1 · Vertiv × NVIDIA × Dassault Systèmes × Polar Data Centers —— 通过（含 1 项待确认）
读完整篇 11,360/11,360 字符。dateline COLUMBUS, Ohio, **Oct. 21, 2026**（窗内）。SOURCE Vertiv Holdings Co。
标题原文 "Vertiv **Targets** Up to 30% More Cumulative AI Token Output…"——是「目标」不是已实现。
**四方角色（scout 漏了一家）**：Dassault Systèmes 是实体参与方（3DEXPERIENCE agentic platform 为配置/虚拟验证载体，副题载明）。
数字与脚注假设（全部为「建模」，稿末三条脚注）：
- 10×（30 天→3 天）："reduces the time from requirements to a configured and validated AI factory solution from approximately 30 days to three days, a 10x improvement"，冠以 "In the modeled scenario"。脚注 2："Modeled. Time to an initial integrated design, configured and validated in the digital twin: 3 days vs. a 30-day conventional design process. Results vary by project."
- 最多 50%（90 天→45 天）：冠以 "In the modeled scenario"。脚注 3："Modeled. On-site power and cooling deployment with Vertiv factory-built infrastructure: 45 days vs. a 90-day conventional on-site baseline. Results vary by project."
- 120 天→48 天、提前约 10 周："That can make productive AI capacity available about 10 weeks sooner"
- **最多 30% token**："generate up to 30% more cumulative token output within the first 12 months **with the same installed capacity**"。脚注 1："Modeled. First 12 months measured from **design kickoff**: **317 vs. 245 productive days** at equal installed capacity (3 + 45 vs. 30 + 90 days). Actual results will vary."
→ 30% 是 **Vertiv 自己的建模**，无第三方验证。成稿只用原话「最多 30%」并带「建模、同等装机容量、自设计启动起算 12 个月」三个限定。
**冷板/CDU/液冷的容量、流量、温度数字：稿中全无（逐词确认）。** 只有定性：SmartRun 是 "prefabricated overhead infrastructure system for high-density power distribution, liquid cooling, networking and containment"；Polar 段称帮助交付 "high-density, liquid-cooled capacity"。
引语归属：**Giordano Albertazzi, CEO of Vertiv**（含「Polar Data Centers is demonstrating…」一句，**是 Vertiv CEO 说的，不是 Polar**）；**Vladimir Troy, VP of AI Infrastructure at NVIDIA**；**Stéphane Sireau, VP, High-Tech Industry, Dassault Systèmes**；**Andy Hayes, CEO of Polar Data Centers**。另 Scott Armul（Vertiv CPTO）于 2026-10-22 作 expo-theater 赞助场次演讲；展位 #3055。
事实 vs 计划：事实=Polar "is applying"/"is using" 该模式于 Herøya 首期；Vertiv "is supplying" 预制电力与热模块、SmartRun、SmartMod，由 Unify 软件支持；正向 Hugging Face SimReady Central Library 贡献 SimReady OpenUSD 资产。计划="Vertiv and NVIDIA **plan to** demonstrate elements of the approach at NVIDIA GTC Berlin"。**无任何已完工/已投产表述**，稿末附 forward-looking statements 免责声明。
**待确认**：Polar 41 MW / 100 MW 的 MW 口径（原文仅 "the first 41 MW phase of its multiphase AI data center, scalable to 100 MW"，**未说明是场站供电、IT 负载还是制冷容量**）。polardatacenters.com / polardc.com / www.polardc.com 三域代理 403。
URL: https://www.prnewswire.com/news-releases/vertiv-targets-up-to-30-more-cumulative-ai-token-output-in-first-12-months-using-nvidia-dsx-polar-deploys-approach-at-norway-site-302915397.html

## I2 · Supermicro NVIDIA Vera CPU 机架 —— 通过（含 1 处必须改写）
读完整篇 9,251/9,251。dateline SAN JOSE, Calif., **Oct. 22, 2026**（窗内）。SOURCE Super Micro Computer, Inc.
**「now shipping」归属**：原文 "Complementary to the **now shipping** Supermicro NVIDIA Vera Rubin NVL72, the 100% liquid-cooled CPU rack can be used either standalone or alongside…" → **修饰的是 Vera Rubin NVL72，不是这台 Vera CPU 机架**。该机架自身成熟度在 "Availability" 节："The Supermicro NVIDIA Vera CPU rack is **available to quote now**." → **可询价，未称已出货、未给发货或上市时点、未给价格。**
**DLC-2 热学规格：稿中一个数字都没有（逐词确认）**。相关内容全为定性："Supermicro's **DLC-2** direct liquid cooling stack enables a **100% liquid-cooled** rack"；"The Vera CPU rack uses the **third-generation NVIDIA MGX** design, **part of the DLC-2 stack**"；与 NVL72 配对的可选设计含 "hot-aisle containment layouts, and **redundant in-row coolant distribution units (CDUs) and rear door heat exchangers from the DLC-2 stack**"（本篇唯一冷却设备清单，仍无容量数字）。Liang 引语另称 Vera CPU 产品线另有风冷 1U 与 2U 机型。
→ 无热捕获率、无冷板覆盖器件、无供液温度、无机架功率密度、无 kW。
算力数字：正文 "integrates **256 NVIDIA Vera CPUs**, delivering **22,528 cores** and **45,056 threads** and supporting **up to 22,500 concurrent agent sandboxes per rack**"。导语另处写 "22.5K sandboxes"（无 "up to"、非「每机架」）→ 用正文版。**22,500 沙箱的前提稿中完全未披露**（无每沙箱配额、无工作负载、无基准）。22,528/256 = 88 核/颗，线程为核数 2 倍，内部自洽。
供电（厂商口径，无数字）："customers can choose either a traditional AC feed to compute rack or an **800 VDC sidecar power rack**, which enables the use of **battery backup units (BBU) in place of a conventional UPS**"；收益表述 "helps free data center floor space, **can** improve end-to-end power conversion efficiency, and lowers CapEx and OpEx"。
引语：**Charles Liang, president and CEO of Supermicro**；**Chris Marriott, vice president of enterprise platforms at NVIDIA**。
其他背景（厂商口径无数字）：BlueField-4 DPU；原生支持 NVIDIA OpenShell Reference Architecture；NVIDIA Sentry 跑在 BlueField-4 上做带外监控、可 "quarantine an agent … in milliseconds"；支持单一团队做 site survey、设计、L11 与 L12 集成与测试、现场部署。
URL: https://www.prnewswire.com/news-releases/supermicro-introduces-the-nvidia-vera-cpu-rack-a-256-cpu-100-liquid-cooled-rack-scale-solution-complementing-the-nvidia-vera-rubin-platform-for-agentic-ai-at-scale-302916308.html

## I3 · Delta 800 VDC 液-液 CDU —— 通过（scout 漏掉整整一节热学规格）
读完整篇 6,615/6,615（scout 只读了约 1,500，把 CDU 流量、压力、泵配置和新冷板整段漏了）。
dateline FREMONT, Calif., **Oct. 15, 2026**（**落在第 10 期窗口 10-10~10-17 内，属上期漏收**）。SOURCE **Delta Electronics (Americas)**（母公司 Delta Electronics, Inc.，TWSE: 2308）。
L2L CDU 规格：导语 "the **new 800 VDC Liquid-to-Liquid CDU with up to 2.5 MW cooling capacity**"；正文 "the new **800 VDC 2.5 MW Liquid-to-Liquid Cooling Distribution Unit (L2L CDU)**"。
**泵与流量（scout 漏掉的关键段）**："The L2L CDU features **three hot-swappable pumps** to support **zero-downtime targets** – each with an integrated converter and control module. Together the pumps **(3+0)** deliver a **combined flow rate of up to 3,850 LPM** and **60 psi of pressure at the operating point**."
→ ⚠️ **泵配置是 3+0，不是 N+1 冗余**；可用性靠热插拔实现「零停机目标」。**不得写成「冗余泵」**（第 10 期 LITEON/DCX 是 "N+1 冗余泵"，两者不同，勿串）。
**稿中未给**：趋近温差（ATD）、供/回水温度、尺寸、重量、冗余等级、二次侧/一次侧分别流量、电气接口细节。
**其他液冷产品（scout 全漏）**：
- **新冷板（面向 NVIDIA Vera Rubin NVL72）**："a new cold plate designed for NVIDIA Vera Rubin NVL72. … The **micro-channel cold plate** combines **micro-channel structures and a multi-impinging flow design** to enhance heat transfer and reduce flow resistance. **Passive flow control** and **advanced metal bonding processes** support high cooling capacity and reliability." —— **纯定性，无热流密度、无热阻、无压降数字。**
- **5,000A 液冷母排**，面向 NVIDIA 第三代 MGX 机架。
- MGX 机架与歧管 "support cooling for high-density Vera Rubin platforms"；另有 DC Busway。
- 定位句："Delta's thermal management portfolio supports 800 VDC-based AI data centers with cooling **from row to chip**."
电力侧（口径已核）：800 VDC In-Row Power Rack = 六个 7RU 功率模块（每个 3RU 110 kW power shelf + 4RU 80 kW BBU），合计 **660 kW 输出 + 480 kW 备电**（6×110、6×80 自洽）；90 kW DC/DC Power Shelf 将 800 VDC 转 50 V、效率最高 98.5%；SST 将中压交流直转 800 VDC；HVDC PDB 转 54/12 VDC、最高 98% 效率、功率密度 1,000 W/in³、支持热插拔；IPS 智能功率平滑最高 98% 效率；另有不含 BBU 的紧凑 800 kW In-Row 与含 BBU 的 660 kW In-Row 两种配置。
**成熟度：展出（exhibited），非预购、非出货。** 全篇动词只有 "is highlighting"/"is showcasing"/"Delta also presented"。无上市时点、无价格、无预购、无出货或客户交付表述。场合 OCP Global Summit 2026；NVIDIA AI Factory MGX Ecosystem Ceremony 于 10 月 14 日；Delta 的 executive session 于 10 月 12 日已讲。
**与 NVIDIA 的关系（不得升格）**：原文 "is highlighting how its **collaboration with NVIDIA accelerates the development of** NVIDIA 800 VDC power and cooling solutions"；"**Alongside** the NVIDIA AI Factory MGX Ecosystem Ceremony on October 14, Delta is showcasing…"。**稿中没有「认证」「qualified」「certified」「DSX-Ready」任何字样。严禁写成「获 NVIDIA 认证」。**
引语：**Ted Shyy, Executive Vice President of Power Electronics Business, Delta Electronics**（唯一引语，发言场合为 NVIDIA AI Factory MGX Ecosystem Ceremony）。**本篇无 NVIDIA 方引语。** 10-12 session 两位出席者（非引语）：Ralf Pieper, Research and Design Director, Custom Design Business Unit, Delta Electronics（原文即 "Research and Design"）；Mike Tu, Principal Electrical Engineer, NVIDIA。
URL: https://www.prnewswire.com/news-releases/delta-highlights-collaboration-with-nvidia-in-advancing-energy-efficient-800-vdc-power-and-cooling-solutions-for-ai-data-centers-at-ocp-global-summit-2026-302909912.html

## I4 · 3C 与 Datalec 合并成立 3C Datalec —— 通过（含 1 处必须钉死的口径 + 1 项待确认）
读完整篇 8,495/8,495。dateline LONDON, **Oct. 14, 2026**（**同属第 10 期窗口内，上期漏收**）。SOURCE 3C Datalec。
标题原文 "3C Merges with Datalec to Create **US$400M+** Revenue Liquid Cooling and Data Centre Services Platform"（原文带 "+"）。
**US$400 million 是「预测」**：正文 "The combined business has **approximately 1,000 team members** and **forecasts 2026 revenue to be over US$400 million**, with offices and manufacturing facilities across Europe, the Middle East, Asia-Pacific and North America." → 公司自身对 2026 年的营收**预测**，非已实现、非经审计。成稿必须写「公司预测 2026 年营收超 4 亿美元（公司口径、预测值）」。
**Steve Walton**：前职 "3C, the liquid-cooling-led data centre infrastructure services company **founded by former CoolIT Systems CEO Steve Walton**"（出现两次）→ 确为 **CoolIT Systems** 前 CEO（公司全名含 Systems）。任职起止年份稿中未给。现职：引语署名 "Steve Walton, **CEO of 3C Datalec**"。其引语自述 "At CoolIT, we spent years preparing for this moment and became a global leader in liquid cooling."
**合并完成状态：稿中表述为已完成**。"3C … **has merged with** Datalec Precision Installations … to create 3C Datalec"；About 节 "**Formed in 2026 through the combination of** 3C … and Datalec Precision Installations, founded in London in 2012"；"Datalec's headquarters **will remain** in London, and its founding leadership team **will continue** in their executive roles within the enlarged group. **Financial terms were not disclosed.**" **无任何「待交割」字样。**
两家各自做什么：**3C** = "the **liquid-cooling-led data centre infrastructure services** company"（创立年份稿中未给）；**Datalec（Datalec Precision Installations）** = "the **London-based data centre engineering specialist** founded in **2012**"。合并后能力集合：liquid cooling、mechanical and electrical (M&E) engineering、ODM manufacturing、connectivity、facilities management；三支柱 **Create**（design and engineering）/ **Construct**（liquid cooling, M&E, ODM manufacturing and connectivity installation）/ **Care**（commissioning, operations, maintenance and FM）。
⚠️ **待确认：3C 在液冷链条上的具体环节（冷板？CDU？歧管？安装调试？）稿中从未说明。成稿勿把它写成冷板/CDU 制造商。**
客户与规模原文限定语："It works with **four of the five largest hyperscalers** and **over 25 colocation providers**, alongside **neoclouds and enterprise customers**, with **active projects in 16 countries totalling hundreds of megawatts (MW)**." → 五大云中的四家**未点名**；「数百 MW」对应**在执行项目（active projects）总量**、分布 16 国，**稿中未说明是液冷容量还是总 IT 容量**，亦非已交付量。
其他已核：未来 12 个月招 200 名工程师；新设施在 Warsaw, Poland / Calgary, Alberta / Austin, Texas（原文写到省州）；约 1,000 名员工（"approximately"）；内部大学 + 学徒制 + Leadership & Employee Equity Program (LEEP) 员工持股；新投资方 Longbow Capital、S2G Investments、Apogem Capital、QIC（"Backed by **new investment** from…"，**金额未披露**；稿中只有前三家有 About 节，QIC 无任何说明）。
引语归属（五条）：**Steve Walton, CEO of 3C Datalec**（"Rack densities have outgrown air, and liquid cooling is no longer optional…"）；**Danny Keeper, Group Director & Co-Founder of Datalec**；**Stuart Richmond, Group Director & Co-Founder of Datalec**；**Matthew Cunning, Director at Longbow Capital**（"**Steve** helped build a category leader in liquid cooling…" —— **投资方评价 Walton，不是 Walton 自述**）；**Bala Nagarajan, Managing Director at S2G Investments**。
URL: https://www.prnewswire.com/news-releases/3c-merges-with-datalec-to-create-us400m-revenue-liquid-cooling-and-data-centre-services-platform-302907856.html

## N1 · MarketsandMarkets「AI 数据中心液冷市场」—— 通过
读完整篇 12,750/12,750。dateline DELRAY BEACH, Fla., **Oct. 20, 2026**（窗内）。
- "projected to grow from **USD 3.52 billion in 2026** to **USD 20.39 billion in 2032**, at a **CAGR of 34.0%**"；数据块另列 Market Size Available for Years 2022-2032。
- "**Asia Pacific** is expected to register the **highest CAGR (35.2%)**"（增速最高，非份额最大）；另句 "**North America** is projected to register the **largest market share**"（scout 漏）。
- "**150 kW & above** segment is projected to grow at the **highest CAGR (78.0%)**" —— ⚠️ **该分段按什么划分稿中一字未提**，成稿只能写「稿中列为 '150 kW 及以上' 分段，划分维度未说明」。
- scout 漏的两条："The **hyperscale** segment … **highest CAGR (34.7%)**"；"The **solutions** segment will dominate the market during the forecast period."
- D2C「最大细分」口径：**按价值、覆盖整个预测期**（"largest share … during the forecast period **in terms of value**"）。另 "by data center type, the **hyperscale** segment … largest market share **in terms of volume**"——价值/体量两套口径并存，勿混。
- 「市场」范围稿中**未定义边界**。分段维度：component、cooling type（direct-to-chip / immersion）、data center type（hyperscale / colocation / enterprise）、region。报告 200 表 / 50 图 / 300 页，题名 "AI Data Center Liquid Cooling Market - Global Forecast to 2032"，报告 id 218744084。
- 稿中点名企业：Vertiv、Schneider Electric、Super Micro Computer、DCX Liquid Cooling System (Poland)、CoolIT Systems (Ecolab)；startups/SMEs Kollance、GIGA-BYTE、Teimmers。
⚠️ **稿中嵌入的一批第三方二手事实，本期一律不采用**（无一手出处、属 MnM 转述）：ZutaCore 2026-06 USD 100M C 轮；Iceotope 2026-05 USD 26M B 轮；Boyd Thermal 预测 2026 销售 USD 1.7bn（液冷 1.5bn）；CoolIT 未来 12 个月约 USD 550M；Vertiv CDU 产品线 70 kW–1,350 kW；Vertiv 2025 年末订单储备 USD 15.0bn（+109%，稿中自注覆盖全产品线）；M&A：Eaton 收 Boyd Thermal、Ecolab 收 CoolIT、Trane 收 LiquidStack。**其中 Eaton/Boyd、Ecolab/CoolIT 交割信息已被 excluded-numbers.md 排除，不得用这篇分析师稿去「补」。**
URL: https://www.prnewswire.com/news-releases/ai-data-center-liquid-cooling-market-worth-20-39-billion-by-2032---exclusive-report-by-marketsandmarkets-302913151.html

## N2 · MarketsandMarkets「数据中心浸没冷却液市场」—— 通过
读完整篇 14,852/14,852。dateline DELRAY BEACH, Fla., **Oct. 23, 2026**（窗内）。
- "projected to grow from **USD 0.23 billion in 2026** to **USD 1.06 billion by 2033**, at a **CAGR of 24.8%**"；数据块 2022–2033。
- "By technology, the **single-phase** cooling segment accounted for the **largest share of 83.0%, in terms of volume, in 2025**."（体量口径、2025 实际）
- "By type, the **synthetic fluids** segment accounted for a share of **57.0%, in terms of value, in 2025**."
- scout 漏的两条："**North America** … **highest CAGR of 26.6%, in terms of value**"；"By data center type, the **AI/ML data center** segment … **highest CAGR of 27.0%**"。
- 报告 277 表 / 61 图 / 254 页，"Global Forecast to 2033"，报告 id 255406797。star players：Shell、Chemours、Exxon Mobil、Lubrizol、Castrol。
- 稿中融资年表与 Uptime Institute 引用**建议不用**（无一手出处）。合成液段有病句 "synthetic fluids, such as AI/ML, HPC, and hyperscale data centers"，显系笔误，不要据此引申。
URL: https://www.prnewswire.com/news-releases/data-center-immersion-cooling-fluids-market-worth-1-06-billion-by-2033---exclusive-report-by-marketsandmarkets-302917911.html

## N3 · DC Market Insights「数据中心管道市场」—— 通过
读完整篇 14,287/14,287。dateline LONDON, **Oct. 22, 2026**（窗内）；稿中另标 Report Updated: Oct. 21, 2026。SOURCE DC Market Insights。
- **USD 1.17 billion in 2025**（base year）→ **USD 1.60 billion in 2026**（稿标 +37.12% YoY）→ **USD 3.36 billion in 2030** → **USD 4.50 billion by 2035**；**CAGR 14.42%（2025–2035）**，区间 low 11.00% / high 17.50%。另有 2020 年 USD 330.00 million。
- 液冷二次回路与机架分歧管：**USD 177.12M（2025，占 15.1%）→ USD 1,581.47M（2035），CAGR 24.47%**。
- **USD 190,000 / 70,000 per MW 口径（已钉死）**：Key Takeaways "Liquid-cooled AI halls require about **USD 190,000 of piping per new MW in 2025**, compared with roughly **USD 70,000 for an air-cooled chilled-water hall**."；专节 "A conventional air-cooled chilled-water hall needs about **USD 70,000 of pipe, fittings, valves and insulation per MW**. A liquid-cooled AI hall **adds a technology cooling system loop from the CDU toward each rack row**, lifting piping content to about **USD 190,000 per MW in 2025**."
  → **口径 = 管材/管件/阀门/保温的采购价值 ÷ 每新增 MW，2025 年价；不是建造总成本、不是冷却系统总造价。** MW = **新增 IT 容量 MW**（方法论节："builds the market bottom-up from **new IT capacity** by cooling architecture and piping content per MW … The 2025 model uses **12.0 GW of new IT capacity** … plus recurring spend on **116 GW of installed capacity**."）
  → 倍数 "**nearly 2.7 times** an air-cooled chilled-water hall"（原文给的，可直接引用）。
- 系统分段（2025 值/份额 → 2035 值/CAGR）：冷冻水与冷凝器回路 781.85M / 66.8% → 2,069.13M / 10.22%；液冷二次回路与机架分歧管 177.12M / 15.1% → 1,581.47M / 24.47%；热排放与乙二醇回路 199.78M / 17.1% → 669.95M / 12.86%；余热外输管道 11.70M / 1.0% → 180.02M / 31.44%。四项 2025 合计 1,170.45M，与总量自洽。
- 材料：不锈钢 206.51M → 1,222.79M（19.47%）；热塑 206.12M → 1,186.19M（19.13%）；碳钢与球墨铸铁 675.39M → 1,807.43M（10.34%）；铜 82.43M → 284.16M（13.17%）。
- 区域：北美 42.0%（USD 491.59M）、2035 约 USD 1.73B；亚太 15.91% CAGR；中东非 16.52% CAGR（最快）；美国 USD 442.43M（最大国家）、印度 20.70% CAGR。
- 集中度：前五大供应商约占 2025 年价值的 21%，"remains fragmented"。
- **情景假设（若引 4.50B 必须带）**：基准情景假设「年新增容量达 27 GW、到 2035 年新增 AI 容量的 88% 为液冷」；低情景（AI 容量推迟两年、钢材关税维持高位、液冷占比见顶约 70%）→ USD 3.32B / 11.00%；高情景 → USD 5.87B / 17.50%。
- 引语：**Amit Jain, Senior Consultant, ICT & Emerging Technologies, DC Market Insights, report author**（唯一一条）。
- 机构自我描述：About 节 "DC Market Insights is a **dedicated research and consulting firm**…"；但开头是报告销售句式 "The 'Data Center Piping Market…' report **has been added to the DC Market Insights offering**"，报告格式 PDF + Excel，并推销一批订阅数据工具；联系地址在印度 Pune。→ 写「研究与咨询机构（自述），本篇为其报告发布稿」，两重身份都在稿里。
⚠️ 稿中 "Recent Developments" 含一条与挂账相关的二手提及："In **October 2026**, **nVent and AMD demonstrated cooling for the AMD Helios rack, including manifold infrastructure**." —— DC Market Insights 的转述、非一手、只有月份无日期、无规格 → **不足以解除 nVent × AMD Helios 的否决**。同节另有 GF/NTT、GF LiquidCore、Vertiv 完成约 USD 1.0bn 收购 PurgeRite（2025-12）、Perma-Pipe FY2025、GF 2026 上半年订单翻倍 —— **均为二手转述，不采用。**
URL: https://www.prnewswire.com/news-releases/data-center-piping-market-to-reach-usd-4-50-billion-by-2035-as-liquid-cooled-ai-halls-push-piping-content-to-usd-190-000-per-mw---dc-market-insights-302916378.html

## 跨期一致性 / 去重核查
1. 7 条 URL 全部不在 drafts/reported-index.md，无重复报道。索引里的 marketsandmarkets.com/Market-Reports/data-center-liquid-cooling-market-84374345.html 是**另一份报告**。
2. ⚠️ **N1 与第 9 期的口径分离（铁律第 10 条须显式交代）**：第 9 期已刊 MnM「全球数据中心液冷市场 2026 年 40.7 亿美元 → 2033 年 276.5 亿美元，CAGR 31.5%，口径含 Solution + Services」（报告 id 84374345）。**N1 是不同报告**（*AI* Data Center Liquid Cooling Market，id 218744084）。两者**不是同一数列的更新**，N1 更小是因为只覆盖 AI 子集。成稿必须写明是「另一份 AI 专题报告」，**不得呈现为对 40.7 亿美元的修订**。第 9 期该条本身无错，**不需要进「更正」节**。
3. ⚠️ **I3 / I4 的「窗外」性质要写准**：第 10 期时间窗是 2026-10-10 ~ 2026-10-17，且该期已覆盖 OCP 会期（10-12~10-15）的 LITEON / CoolIT / UfiSpace 三条。Delta（10-15）与 3C Datalec（10-14）**落在上期窗口内、被上期漏收**。
4. ⚠️ **Delta CDU 与已刊两条 2.5~2.6 MW CDU 勿混**：第 10 期已刊 LITEON × DCX「最高 2.6 MW、趋近温差 3 °C、N+1 冗余泵」；索引另有 Trane/LiquidStack 2.5 MW CDU。Delta 是第三家、不同厂商，不构成重复，但 **Delta 是 3 泵 3+0 热插拔、稿中无 ATD**，与 LITEON 的「N+1 冗余 + ATD 3 °C」**不可互相代入**。
5. 未发现任何已刊出内容与原文不符 → 就本次核验范围而言**无需「更正」节**。

## 取数通道小结（供 PR 流程备注）
- www.prnewswire.com 全程可达稳定：7 篇一次取回、全部读到稿末（11,360 / 9,251 / 6,615 / 8,495 / 12,750 / 14,852 / 14,287 字符，无一条截断）。本次 4 处实质修正全部位于 scout 未读到的后半段——**长稿必须读到底**这一条已被验证。
- 代理 403（本次新增记录）：polardatacenters.com、polardc.com、www.polardc.com 三域 "Tunnel connection failed: 403 Forbidden" → Polar Herøya 的 41 MW / 100 MW 口径无法从二方一手源确认，判待确认。
- 按嘱未触碰的已知失败域：coolermaster.com、s22.q4cdn.com、businesswire.com、www.nvent.com、opencompute.org、trendforce.com、datacentremagazine.com、storagenewsletter.com、archive.org。
- 因通道受限未核完：仅 I1 的 MW 口径一项。三条挂账按嘱未重试。
