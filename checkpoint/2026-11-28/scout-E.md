# scout-E · 产业动态（原样回传，含第二轮）

## 结论
**窗口内（2026-11-22 ~ 11-28）未检出可确认的新增事实条，分析师数字也未检出。**
证据性质：搜索结果里没有任何一条落在窗口内。两轮的 `fetch_source.py` 取原文**全部被代理 403 拦截**
（"no rule or network setting allows this host"），被拦主机含 datacenterfrontier.com、daikin.eu、taiwannews.com.tw、
hpcwire.com、trendforce.com、globenewswire.com。**未取到任何一手正文，不能证明这七天确实没有稿件。**
scout 自评：「各 query 命中的最新条目都停在 11-17 前后，更像索引滞后，而不是窗口内确实没有稿件。」

## 两轮实际跑过的 query
第二轮（standard，各一次）：
1. `site:prnewswire.com liquid cooling data center November 2026`
2. `site:prnewswire.com cold plate OR "direct-to-chip" November 2026`
3. `site:prnewswire.com "coolant distribution unit" OR CDU data center November 26 2026`
4. `site:datacenterdynamics.com liquid cooling news November 2026`
5. `data center liquid cooling announcement "November 24, 2026" OR "November 25, 2026" OR "November 26, 2026"`
6. `immersion cooling OR two-phase cooling data center press release week November 23 2026`
7. `Vertiv OR nVent OR Boyd OR JetCool OR Accelsius OR Motivair November 2026 liquid cooling`
第一轮：`liquid cooling data center announcement November 2026`、`coolant distribution unit CDU launch press release November 2026`、
`direct-to-chip cold plate AI factory cooling acquisition expansion November 2026`、
`data center liquid cooling market forecast TrendForce penetration 2027`、
`liquid cooling press release "November 24, 2026" OR "November 25, 2026" OR "November 23, 2026" data center`
备注：`site:prnewswire.com` 过滤几乎未起作用，未返回任何窗口内 prnewswire 稿 → 无可取 URL，故第二轮未对 prnewswire 做取文。

## 检索摘要里出现的条目：全部窗口外，不作本期事实条
均仅来自检索摘要、未取一手正文，仅供去重核对。
- **Ecolab 集成液冷平台（SC26）**，摘要称 2026-11-16 —— 应即第 14 期已报的 CoolIT×Ecolab 条。摘要另称 Ecolab 全球高科技业务年增 >25%、2026 年年化销售额接近 15 亿美元（含 Ovivo 与 CoolIT），厂商口径、未核。https://www.hpcwire.com/off-the-wire/ecolab-introduces-integrated-liquid-cooling-platform-at-sc26/
- **nVent SC26**，摘要称 2026-11-16，称已部署超过 4 GW 液冷，厂商口径、未核。https://finviz.com/news/423571/nvent-features-expanded-liquid-cooling-and-power-portfolio-at-sc26
- **Delta SC26**，摘要称 2026-11-13，2.5 MW in-row L2L CDU、200 kW 4U in-rack CDU 与冷板 —— 去重清单已有
- **Acbel SC26 液冷供电**，仅 Webull 转载，窗口外、未取一手。https://www.webull.com/news/15934283034772480
- **Vertiv MegaMod HDX 新配置**，摘要称约 2026-11-14，窗口外、未核
- **AVC**，摘要称 11-10 财报，Q3 营收创纪录，并称占 NVIDIA GB200/GB300 冷板市场约 40–50% —— **二手转述的份额估计、来源未明确、窗口外，不建议用**
- **ZutaCore × Munters**（Z₂O 无水「芯片到屋顶」，摘要称 2026-11-16）、**Daikin 新 CDU**（摘要称 2026-11-02，400 kW~2.5 MW 来自 RefIndustry 转述）、**Panduit 液冷实验室**（摘要称 2026-11-17，仅聚合站 briefglance.com）、**Schneider/Motivair WCDU**（日期未确认）：**均窗口外**
- 更早：LiquidStack CDU 2.X、Carrier CDU（1.3–5 MW，日期未确认）
- **DCD 站内搜索没有返回任何 2026 年 11 月的液冷文章**

## 分析师 / 市场数字：窗口内未检出
窗口外者：TrendForce（2026-08-17，高端 AI 基础设施液冷渗透率 2026 约 53%、2027「接近 60%」，原页被拦、未核）；
Omdia（全球数据中心液冷 CAGR 25%、2028 年 168 亿美元，日期未确认、仅二手摘要、未见原页 → 不建议用）。

## 上期挂账四项：本期仍未取到一手稿（如实报「取不到」）
Ecolab CHx 3000 原稿 / Nexalus·Renda 一手稿 / TATSUTA 扩产一手稿 / Acuity 收购 Parameter Technologies 一手稿。

## scout 建议
本期若要补产业动态，需在能访问 prnewswire.com 搜索页或各公司 newsroom 的环境里按日期直接筛选。
