# scout-E 回传（产业动态）· 原样存档

角度 E 产业动态，第 11 期（窗口 2026-10-18 ~ 10-24）。所有「直读」均指用 fetch_source.py 取到 PR Newswire 原稿正文。

## 三条挂账结论
1. **Cooler Master 2,500 kW CDU：仍不可达，量级矛盾未解。** coolermaster.com 经 fetch_source 仍 403（只试了 en-global 产品页一次）；webull.com 与 s22.q4cdn.com 在 WebFetch 里 DNS 失败；PR Newswire 窗口内「Cooler Master」0 条。只拿到检索摘要且互相打架（990 GPM + 4–5 °C vs 产品页 1,500 LPM + 5 °C）；摘要另称同站 1.4 MW 型号也标 1,500 LPM / 5 °C（新线索，未核实）。**量级矛盾不能消解，数字仍不可写进刊物。** 可补记但未直读：Q4 2026 量产目标、功耗约 19.5 kW、设施侧供水 2–45 °C。
2. **nVent × AMD Helios 后门热交换器：发布日期已定位，原稿未能直读。** 官方稿 PDF 在 s22.q4cdn.com（nVent 投资者站 CDN），fetch_source 403、WebFetch DNS 失败 → 日期 **2026-10-13** 来自检索摘要、非直读。产品为 Helios 双宽机架的直流供电双后门，捕获 DLC 之后的剩余热量使机架对机房近热中性，门上带温湿度传感器与压差风扇控制。**检索摘要里没有容量数字。** StockWirex 称系展示品、未披露价格/容量/上市日期/订单，并称 Helios 约 225–245 kW/机架（第三方数字，未核实，不可用）。摘要里的 "RDHX Pro 78 kW @ 14 °C" 是另一款产品，勿混。来源：https://s22.q4cdn.com/268397047/files/doc_news/nVent-and-AMD-Collaborate-on-Cooling-for-AMD-Helios-Rackscale-Solution-2026.pdf
3. **OCP 场馆全名：opencompute.org 仍 403，按指示结案，不再挂账。**

## （一）事实条

### 窗口内（2026-10-18 ~ 10-24）
**F1. Vertiv × NVIDIA：AI 工厂预设计参考架构 + 工厂预制交付，Polar Data Centers 挪威部署**
- 公司：Vertiv、NVIDIA、Polar Data Centers、Dassault Systèmes。发布 2026-10-21，美国俄亥俄州 Columbus，称在 NVIDIA GTC Berlin 发布。
- 来源：https://www.prnewswire.com/news-releases/vertiv-targets-up-to-30-more-cumulative-ai-token-output-in-first-12-months-using-nvidia-dsx-polar-deploys-approach-at-norway-site-302915397.html
- 原文数字（厂商口径，且为建模场景）：配置验证约 30 天→3 天（10 倍）；基础设施部署约 90 天→45 天（最多 50%）；两段合计约 120 天→48 天，可提前约 10 周投产，12 个月内累计 token 产出最多多 30%（"under defined assumptions"）。Polar 挪威 Herøya 站首期 41 MW、可扩到 100 MW。Vertiv 供应预制电力与热模块、SmartRun 架空基础设施、SmartMod。
- 直读：是（约 5,500/11,360 字符，后半未读）。相关性：中（预制交付与仿真叙事，不是冷板硬件规格）。
- 去重：与已报「Vertiv CDU 获 NVIDIA DSX-Ready 认证」「NVIDIA DSX-Ready AI factory 博客」同属 DSX 主题，但系新稿新内容。

**F2. Supermicro NVIDIA Vera CPU 机架：256 颗 CPU，100% 液冷**
- 发布 2026-10-22，美国加州 San Jose。来源：https://www.prnewswire.com/news-releases/supermicro-introduces-the-nvidia-vera-cpu-rack-a-256-cpu-100-liquid-cooled-rack-scale-solution-complementing-the-nvidia-vera-rubin-platform-for-agentic-ai-at-scale-302916308.html
- 原文数字：每机架 256 颗 Vera CPU、22,528 核、45,056 线程，最多支持 22,500 个并发 agent 沙箱（厂商口径）；采用 Supermicro DLC-2 直接液冷与第三代 MGX 机架；供电可选交流馈电或 800 VDC 旁柜电源机架（带 BBU）；稿中称 Vera Rubin NVL72 "now shipping"。
- 直读：是（约 5,500/9,251 字符）。**没有冷却容量（kW）数字。** 相关性：弱到中。去重：新增。

**F3. 本窗口其他液冷相关 PRN 稿（仅标题级，未展开，建议不收）**
Sensata FL 系列超声波流量传感器（用于 CDU、冷水机组，最高 400 L/min；日期 10-20~10-22 不明，Business Wire 原稿未取）；Entuity（Park Place Technologies）AI 加速器与液冷监控 2026-10-22；RS × Omron 控制面板 2026-10-21；ASUS Rubin NVL8 开始出货 2026-10-21；Armada × NVIDIA DSX POD 2026-10-21。均与冷板关系弱或无，未读原稿。

### 窗外补记（需维护者裁定，原始日期已标）
**W1. Delta：800 VDC 液-液 CDU，最高 2.5 MW**
- 日期 **2026-10-15**，美国 Fremont。来源：https://www.prnewswire.com/news-releases/delta-highlights-collaboration-with-nvidia-in-advancing-energy-efficient-800-vdc-power-and-cooling-solutions-for-ai-data-centers-at-ocp-global-summit-2026-302909912.html
- 原文数字：展出 "new 800 VDC Liquid-to-Liquid CDU with up to 2.5 MW cooling capacity"（厂商口径）；同稿另有 800 VDC 660 kW in-row 电源机架（配 480 kW 备用电源）。
- 直读：是（前约 1,500 字符，只确认上述两句）。**没有流量或趋近温差。** 相关性：强。去重：新增。

**W2. 3C 与 Datalec 合并，成立 3C Datalec**
- 日期 **2026-10-14**，伦敦。3C 由前 CoolIT CEO Steve Walton 创立。来源：https://www.prnewswire.com/news-releases/3c-merges-with-datalec-to-create-us400m-revenue-liquid-cooling-and-data-centre-services-platform-302907856.html
- 原文数字：合并后约 1,000 人，2026 年**预测**营收超 US$400 million（公司口径）；未来 12 个月招 200 名工程师，新设施在波兰华沙、加拿大卡尔加里、美国奥斯汀；服务 5 大超大规模云中的 4 家、超过 25 家托管商；16 个国家在建项目合计数百 MW；新投资方 Longbow Capital、S2G Investments、Apogem Capital、QIC（金额未披露）。
- 直读：是（约 3,800 字符）。相关性：中（液冷服务集成商，非硬件）。去重：新增。

**W3. nVent × AMD Helios RDHx**：见挂账 2。日期 2026-10-13，未直读。
**W4. CoolIT "The Next Gen AI CDU"**：日期 2026-10-07，仅在 coolitsystems.com/news 列表看到标题与日期，未点进正文。
**W5. Ecolab 完成收购 CoolIT**：交割 2026-07-02、对价约 $4.75B、协议 2026-03-20 签署，来源为 SEC 10-Q 与转载的检索摘要，未直读。另称 Ecolab 计划 2026 年 11 月芝加哥 SC 大会发布合并的 3D TRASAR 冷却平台（前瞻，未核实）。窗外较久，仅作背景，不建议收。

## （二）分析师 / 市场数字（只能进「前瞻分析」节）
| # | 机构 | 发布日期 | 数字 | 口径 | URL | 直读 |
|---|---|---|---|---|---|---|
| A1 | MarketsandMarkets | 2026-10-20 | AI 数据中心液冷市场：2026 年 USD 3.52 bn，2032 年 USD 20.39 bn，CAGR 34.0%（2026–2032）。亚太 CAGR 最高 35.2%；150 kW 及以上分段 CAGR 78.0%；D2C 为最大细分 | 市场规模预测 | https://www.prnewswire.com/news-releases/ai-data-center-liquid-cooling-market-worth-20-39-billion-by-2032---exclusive-report-by-marketsandmarkets-302913151.html | 是 |
| A2 | MarketsandMarkets | 2026-10-23 | 数据中心浸没冷却液市场：2026 年 USD 0.23 bn，2033 年 USD 1.06 bn，CAGR 24.8%。2025 年单相占体量 83.0%；合成液占价值 57.0% | 市场规模预测 | https://www.prnewswire.com/news-releases/data-center-immersion-cooling-fluids-market-worth-1-06-billion-by-2033---exclusive-report-by-marketsandmarkets-302917911.html | 是 |
| A3 | DC Market Insights | 2026-10-22 | 数据中心管道市场：2025 年 USD 1.17 bn，2026 年 USD 1.60 bn，2035 年 USD 4.50 bn，CAGR 14.42%（2025–2035）。液冷二次回路与机架分歧管 2025 年 USD 177.12 M、2035 年 USD 1.58 bn，CAGR 24.47%。液冷 AI 机房管道约 USD 190,000/MW，对比风冷冷冻水机房约 USD 70,000/MW | 市场规模预测 + 单位 MW 管道价值 | https://www.prnewswire.com/news-releases/data-center-piping-market-to-reach-usd-4-50-billion-by-2035-as-liquid-cooled-ai-halls-push-piping-content-to-usd-190-000-per-mw---dc-market-insights-302916378.html | 是 |
| A4 | DC Market Insights | 2026-10-19 | 数据中心冷却塔市场到 2035 年 USD 2.44 bn | 市场规模预测 | https://www.prnewswire.com/news-releases/data-center-cooling-tower-market-to-reach-usd-2-44-billion-by-2035-as-water-rules-push-hybrid-and-adiabatic-coolers---dc-market-insights-302912946.html | **仅标题，未读正文** |
| A5（窗外） | TrendForce | **2026-08-17** | 标题称液冷在高端 AI 基础设施成为标配、2026 年渗透率预计 53% | 渗透率预测 | https://www.trendforce.com/presscenter/news/20260817-13183.html | 否，域名 403，仅标题 |

提示：A1–A3 是营销型报告稿，样本量与方法学未披露；A1 的 2026 年基数 USD 3.52 bn 与已排除的 Dell'Oro 数字是不同机构不同口径，不要对比或混用；未引用 Dell'Oro 组任何数字。
〔调用方注：A5 命中去重——TrendForce「2026 年 53%」已在第 5 期（2026-08-30）刊出，且本期窗外、未直读，不收。〕

## 本期未检出（已扫源）
- PR Newswire 关键词检索（liquid cooling、data center cooling、coolant distribution unit、direct-to-chip、immersion cooling、cold plate、CoolIT、Ecolab、Accelsius、JetCool、Motivair、Asetek、Boyd、nVent、Danfoss、Parker、LiquidStack、Chilldyne、Cooler Master、Vertiv、Delta、ACT、Wiwynn、LITEON 等），窗口内除上述外这些公司无自家发布的冷却相关稿。
- Danfoss 与 Parker 只命中无关稿。未检索 Stäubli（关键词含非 ASCII 使脚本报错）、HPE、Intel、AMD 官方稿、LG、Midea、Trane。
- 窗口内未检出并购交割与产能扩张。未取到 Business Wire 稿、datacentremagazine、storagenewsletter、digitimes（403 或不在 PRN 内）。
- 一条 WebSearch 摘要提到 Digitimes 10-22 两条访谈（TI 谈托盘级控制、Walrus Pump 称高容量 AI 冷却泵需求偏慢），未读正文，不建议收。
