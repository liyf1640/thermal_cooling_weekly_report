# verified-industry.md · 第 8 期产业动态逐位核验

## 0. 取源环境硬限制
403 / EGRESS_BLOCKED 域名（部分）：globenewswire.com、liquidstack.com、tranetechnologies.com、lg.com、
lgnewsroom.com、liteon.com、mops.twse.com.tw、opencompute.org、it-online.co.za、channelpostmea.com、
telecompaper.com、sec.gov、web.archive.org、datacenterfrontier.com、以及 nvent/boyd/1-act/jetcool/
accelsius/chilldyne/motivair/asetek/deltaww/supermicro/wiwynn/fabric8labs/tdk/ecolab/nvidia.com 官网。
**实际能取到原文的只有 5 个域**：www.vertiv.com、www.coolitsystems.com、www.prnewswire.com、
blogs.nvidia.com、www.datacenterdynamics.com（仅文章/tag 页）。
> 复用技巧：Vertiv 新闻稿列表是 Angular 前端，需 POST
> `https://www.vertiv.com/api-lang/{en|en-GB}/searchAboutResults/searchNews`，
> body `{"query":"","facetGroups":[],"sortBy":"1","pageNumber":0,"newsType":"4593","fromNewsRelease":true,"parentId":"4599"}`。

---

## 1 · LiquidStack CDU 2.X —— 待确认（仅二手；数字须标「媒体转述厂商标称」）
**一手稿取不到**：GlobeNewswire 该 URL、liquidstack.com、tranetechnologies.com、Trane IR、SEC EDGAR 全被拦。
PR Newswire 全库搜 LiquidStack(8 条)/Trane Technologies(45 条) **均无此稿**（走 GlobeNewswire 独家分发）。
→ **唯一可读出处是 DCD 二手**：https://www.datacenterdynamics.com/en/news/trane-liquidstack-launch-new-25mw-cdu/
（署名 Dan Swinhoe，页面日期 September 30, 2026）

**DCD 原文直引**：
> "Able to offer 2.5MW of cooling capacity at 4°C (39.2°F) ATD, with 3,750 lpm at 3.5 bar of available head
> pressure, LiquidStack said the CDU 2.X features an ultra-low-harmonics VFD architecture designed to address
> harmonic distortion at the source... The CDU features flexible configuration options, including control valve,
> power-feed, and redundancy options, with dual-feed A/B and automatic transfer switch options. The CDU offers
> approach temperatures and facility inlet temperatures up to 45°C (113 °F)."

- **2.5 MW @ 4 °C ATD** ✅ 厂商标称。**原文两者绑定，不可拆开写「2.5MW」不带工况**
- **3,750 lpm @ 3.5 bar available head pressure** ✅ 厂商标称
- 超低谐波 VFD 架构 ✅ 厂商标称，无量化指标
- 双路 A/B + ATS ✅ 厂商标称，属**配置选项不是标配**
- 设施进水温度最高 45 °C ⚠️ **原文句子本身是病句**（45 °C 同时挂在 approach 与 facility inlet 上，而 approach 45 °C
  物理上讲不通，前句已给 4 °C ATD）。合理读法是「设施进水温度最高 45 °C」但**属 verifier 推断，非原文明确表述**
- **「端排与机架旁两种部署」❌ DCD 全文无此表述，零出处 → 删除**
- "architecture-agnostic" ✅ DCD 原文 "described as an 'architecture-agnostic coolant distribution unit'"（DCD 自己加引号标为转述厂商用词）

**预购/出货** ✅ 原文直引："The LiquidStack CDU 2.X is available for pre-order now, with shipments beginning in
the second quarter of 2027." DCD 副标题 "Shipping of new unit to start in Q2 2027" → **确认尚未发货**

**引语归属** ✅ 原文："said Scott Smith, general manager of LiquidStack, Trane Technologies."

**与 DSX Ready / GigaModular 的关系 —— 结论：无证据覆盖，禁止混写**
- NVIDIA 一手稿（blogs.nvidia.com，PUBLISHED_META 2026-09-21T18:00:07Z，全文 4524 字已读完）原文仅：
  > "At launch, DSX Ready includes qualified BESS solutions Hitachi Energy, LG Energy Solution and Tesla, and
  > qualified CDU solutions from LG Electronics, LiquidStack and Vertiv."
  **只点公司名，通篇不出现任何 CDU 型号名、不出现任何容量数字（MW/kW 一个都没有）** → 复核第 7 期判断**正确**
- DCD 的 CDU 2.X 报道**完全没提 DSX Ready / NVIDIA 资质**
- GigaModular：DCD LiquidStack tag 页显示 "LiquidStack launches modular CDU able to offer 10MW..." **03 Jun 2025**
  → 与 CDU 2.X 是两条不同条目、容量不同（10 MW vs 2.5 MW）→ **不是同一产品**
- → **DSX Ready 是否覆盖 CDU 2.X：无证据。不得写「DSX Ready 的 CDU 2.X」或暗示两者相连**
- **额外口径（重要）**：NVIDIA 原文 BESS = "partners run the required qualification tests and submit supporting
  data for NVIDIA review and approval"；**CDU = "the path uses the CDU self-qualification suite..."（自我认证）**。
  另有免责 "Passing qualification does not replace site-level engineering or imply site-level stability."

**日期**：直接证据只有 GlobeNewswire URL 路径 `/news-release/2026/09/29/3370788/`（页面本身取不到）；
DCD 页面日期 2026-09-30，正文 "this week announced" → **取 9-29 或 9-30 都在窗口内**
**「Yotta 2026（爱尔兰）」❌ 完全无出处** —— DCD 全文不含 "Yotta"、不含 "Ireland" → **删除**

---

## 2 · Vertiv 扩建斯洛伐克 Nové Mesto nad Váhom —— **通过（一手已核）**
**一手稿找到**（EMEA 区域稿，不在 en-us 列表里，经 en-GB 列表 API 取出）：
https://www.vertiv.com/en-emea/about/news-and-events/news-releases/2026/vertiv-strengthens-emea-power-and-cooling-manufacturing-capacity-to-help-customers-reduce-time-to-token-and-accelerate-ai-deployment/
官方标题（与媒体标题不同，用官方的）："Vertiv strengthens EMEA power and cooling manufacturing capacity to
help customers reduce time-to-token and accelerate AI deployment"

**官方日期 2026-09-28 → 窗口内**，三重依据：列表 API `eventDateUtc = 2026-09-28T03:10:54Z`；页面显示 "28/9/26"；
正文 dateline "Nové Mesto nad Váhom, Slovakia [Sept. 28, 2026] –"。
→ it-online 标 9-28 正确；channelpostmea 标 9-30 是转载日期非发稿日。

**22,000 m² 原文**：
> "Over the next 18 to 24 months, Vertiv plans to add approximately 22,000 square meters of new manufacturing
> space at the Nové Mesto nad Váhom campus."
→ **plans to add / approximately**，前瞻性计划（稿末有 forward-looking statements 免责段），**不是已建成**

**明确包含液冷 ✅ 原文**：
> "The expansion will increase production capacity for power, switchgear, and thermal management technologies,
> including advanced liquid cooling and power solutions designed for high-density AI and high-performance
> computing applications."

**岗位原文**：
> "The project is also expected to create hundreds of new employment opportunities between 2027 to 2029 across
> manufacturing, engineering, operations, supply chain, quality, technical, and leadership functions."

**引语归属（scout 未给）**：**Paul Ryan, president of Vertiv in EMEA**；**Chris Hales, VP operations EMEA, Vertiv**。
背景句："following recent expansion initiatives across its manufacturing facilities in Ireland, Italy, Croatia,
Malaysia, Mexico, and the United States."

---

## 3 · LG DSX Ready CDU 容量 2.5 还是 2.6 MW —— **待确认（触发人工裁定，verifier 未代为裁定）**
**scout 给的 lg.com 页面正文取不到**（代理 status 明确记录 `www.lg.com:443 → gateway answered 403 to CONNECT`）；
lgnewsroom.com / newsroom.lge.com / live.lge.co.kr / web.archive.org 同样被拦
→ **无法核对该页标题与 slug 的不一致，也无法确认正文容量**

**但取到 LG Electronics 自家发布的两篇一手稿（PR Newswire 分发，稿末 "FONTE LG Electronics Brasil"），
均在窗口内、共 4 处、全部写 2,6 MW**：

(A) https://www.prnewswire.com/br/comunicados-para-a-imprensa/lg-electronics-se-torna-parceira-preferencial-da-nvidia-em-solucoes-de-energia-e-resfriamento-302893005.html
dateline "SÃO PAULO, Sept. 29, 2026 /PRNewswire/"
> "A Unidade de Distribuição de Fluido de Resfriamento (CDU) de **2,6 megawatts (MW)** da LG foi recentemente
> qualificada como NVIDIA DSX Ready CDU, e a CDU de 2,6 MW possui atualmente a maior capacidade de resfriamento
> entre as soluções qualificadas como NVIDIA DSX Ready CDU.¹ A LG também concluiu a qualificação de
> infraestrutura dos modelos de 600 kW e 1 MW..."
脚注 ¹ "Com base nas informações exibidas no marketplace da NVIDIA no momento da consulta."
→ **「容量最大」是厂商标称 + 自限定脚注，不可去掉脚注直接陈述**
另："Até o final deste ano, a LG planeja buscar a qualificação da NVIDIA para seu modelo de CDU de 4,0 MW"

(B) https://www.prnewswire.com/br/comunicados-para-a-imprensa/lg-electronics-apresenta-solucoes-chip-to-chiller-para-resfriamento-de-data-centers-de-ia-na-data-center-world-asia-2026-302893329.html
dateline "SÃO PAULO, 29 de setembro de 2026"
> "As CDUs de 1 megawatt (MW), **2,6 megawatts (MW)** e 600 quilowatts (kW) da LG concluíram a qualificação de
> infraestrutura da NVIDIA neste ano... Além disso, a CDU de **2,6 megawatts (MW)** da LG foi qualificada como
> NVIDIA DSX Ready CDU..."

→ **LG 自家稿明确区分两档**：NVIDIA「AI 基础设施资质」= 600 kW / 1 MW / 2.6 MW 三档；
**「DSX Ready CDU」= 仅 2.6 MW 一档**

**标题与 slug 不一致能否澄清：不能**（lg.com 读不到）。
**NVIDIA 侧复核**：DSX Ready 发布稿全文无任何 CDU 容量数字、无任何型号名 → 第 7 期该判断**正确**。

**供人工裁定的事实摆列**：
- 第 7 期依据：Seoul Economic Daily（韩媒，**二手**），2026-09-22，称 2.5 MW。本期无法复核该韩媒原文（域名不可达）
- 本期新证据：**LG Electronics 自家新闻稿（一手，2026-09-29，PR Newswire，葡语本地化版；英文全球版在 lg.com 不可达）×2 篇共 4 处，均为 2.6 MW**
- scout 所称 lg.com「slug 写 2-5-megawatt、标题写 2.6-Megawatt」verifier **无法独立验证**，仅能确认 scout 给的 URL 里 slug 确含 `2-5-megawatt`
- 更正依据强度：**一手（LG 自己）胜过二手（韩媒）**；但英文全球原稿未读到，仍留一分不确定

---

## 4 · CoolIT 新一代 CDU —— **否决（窗口内无一手发布稿）；并查出 scout 一处事实错误**
**预告页复核 ✅ 确实没有任何揭晓日期。**
https://www.coolitsystems.com/resources/news/the-next-gen-ai-cdu/ （一手，PUBLISHED_META 2026-08-17T08:00:20-06:00，
全文仅 876 字符，**已整页读完**）。正文**全文**：
> "Get ready for CoolIT's next-gen CDU for the AI era / The Wait is Almost Over. / More cooling capacity to scale
> AI compute with speed, reliability, and global support is just around the corner. Get a first look at CoolIT's
> next-generation CDU for high-density AI infrastructure at OCP Global Summit (Booth E19). Complete the form
> below to book a meeting with our team and reserve your exclusive preview."
→ 无日期、无规格、无容量数字。

### ⚠️⚠️ 关键发现：scout 的「面向 1MW+ 超密 AI 机架」这句话，该页上不存在
该页**没有任何「1MW」、没有任何数字容量表述**。唯一与容量相关的措辞是定性的 "More cooling capacity"，
唯一与密度相关的是 "high-density AI infrastructure"。**属 scout 捏造/串稿，须在成稿前剔除。**
> **主流程注**：但「1MW+」这个数字**已经出现在第 5、6、7 期正文与 companies.md 里**（第 5 期：「面向 1MW+ 超密 AI 机架」）。
> 若该页从未有此数字，则属**撤回已发布数字**（rules 第 20 条 (b)）→ **必须停下等维护者裁定，本期不自行撤回。**

**窗口内 CoolIT 官网确无新一代 CDU 发布稿 ✅**（官网新闻索引第 1 页已整页读完）：
窗口 9-27~10-03 内**只有一条** News「DCF Tours: Inside CoolIT, Where AI Liquid Cooling Goes to Scale」
**SEPTEMBER 28, 2026** —— 这是 Data Center Frontier 的**媒体探访报道转载**，不是 CoolIT 发布稿、与新 CDU 无关。
邻近条目：Blog 9-24、9-21、9-14、News 9-2、8-31、8-17（预告页）、Blog 7-28、Press Release 7-2。
**窗口内 "Press Releases" 类目零条。**

**OCP Global Summit 2026 日期：核到 October 12–15, 2026，San Jose McEnery Convention Center —— 但不是 OCP 一手。**
opencompute.org 被拦。退到两个**互相独立的参展商第一方声明**且吻合：
- SUNON 自家稿（PR Newswire，2026-09-29）："Event: OCP Global Summit 2026 / **Date: October 12–15, 2026** /
  Venue: **San Jose McEnery Convention Center**, San Jose, California, USA / SUNON Booth: A19"
- Vertiv 官网活动页（一手）："**Oct 12 - 15, 2026** • San Jose, California, USA — OCP Global Summit 2026"
- 旁证：Compal 自家稿（2026-09-29，dateline SAN JOSE, Calif.）
→ 第 7 期正因二手日期出错撤回过一次，**此日期应标「未核到主办方一手」**

---

## 5 · LITEON × DCX 交割 —— **原稿数字通过；窗口内无新进展 → 本期不构成新事实条**
**原稿措辞复核 ✅ 完全一致**（liteon.com 被拦，退到 PR Newswire 上 LITEON 自己发布的同一篇稿，
稿末 "SOURCE LITEON Technology"，一手等效）：
https://www.prnewswire.com/news-releases/liteon-announces-strategic-investment-in-liquid-cooling-technology-company-dcx-302868836.html
dateline "TAIPEI, Sept. 3, 2026"，全文 5167 字符已整篇读完。原文直引：
> "Upon closing of the transaction, LITEON will hold approximately 25% equity ownership in DCX Liquid Cooling
> Systems with a total transaction value of approximately US$176 million."
→ 「upon closing」「约 25%」「约 US$176 million」**逐字核到**

**是否给出预计交割时点 ✅ 复核确认——未给。** 全篇逐字读完**不含任何** closing date / expected to close /
季度或年份的交割时点表述，也无监管批准条件表述。**第 7 期判断正确。**

**窗口内有无交割/批准/延期公告：未检出，但证据等级有限。**
- PR Newswire 全库搜 LITEON(14 条)/DCX(16 条)：最新均为 2026-09-03 本稿，其后无 LITEON 自家稿
- DCD Liteon tag 页：仅 "04 Sep 2026 Taiwan-based Liteon purchases 25 percent stake in Polish liquid cooling firm, DCX" 一条，无后续
- **台湾证交所 MOPS 被拦，未能查重大讯息；liteon.com 亦被拦** → 结论建立在「两条可达渠道未见」，**不是对 MOPS 的穷尽核查**

---

## 6 · scout 漏掉的窗口内一手稿 —— 检出 6 条
**未检出（限于 PR Newswire + 可达官网，各家自有官网全部被拦，故「未检出」≠「不存在」）**：
NVIDIA（窗口内 blogs.nvidia.com 无散热稿）、CoolIT、Ecolab、nVent（最新 9-02）、Boyd、ACT、JetCool（最新 7-09）、
Accelsius、Chilldyne、Motivair、Asetek（最新 6-09）、Delta（窗口内仅 9-29 自动驾驶稿）、
Supermicro（最新 9-23，窗口外）、Wiwynn、Fabric8Labs（最新 6-10）、TDK。

### 6.1【建议入刊·强】LG Electronics 美国首座冷水机组工厂（弗吉尼亚）—— 2026-10-01，窗口内
https://www.prnewswire.com/news-releases/lg-electronics-establishes-first-us-factory-to-produce-chillers-for-ai-data-center-cooling-302895464.html
dateline "WINDSOR, Va., Oct. 1, 2026"
- "the new **350,000-square-foot** state-of-the-art facility, on a **43-acre** site in Isle of Wight County, will
  produce **air-cooled chillers** for AIDCs, with **production scheduled to begin in the first half of 2027**"（厂商标称，未建成）
- "**more than 150 new jobs**" —— 出自**弗吉尼亚州长 Abigail Spanberger** 引语（**政府方口径，非 LG 自述**）
- "The company plans to invest a total of **KRW 150 billion**"（覆盖美国新厂 + 韩国 Pyeongtaek、Changwon 两厂，厂商标称）
- 韩国侧："expanding its air-cooled chiller production lines in Pyeongtaek and Changwon... adopting a conveyor-based production system"
- 引语人：Don Kwack（President & CEO, LG Electronics North America）、Chris Ahn（President, LG Electronics USA's
  Air Conditioning Technology division）、Carrie Chenery（Virginia Secretary of Commerce and Trade）
- **第三方机构数字（Omdia，分析师估计，非实测）**："global data center capacity is projected to grow from
  **226 GW in 2026 to 420 GW in 2030**, an increase of **194 GW**, with **60 percent** of the additional capacity
  expected to be concentrated in North America"

### 6.2【建议入刊·强，与第 3 条联动】LG 成为 NVIDIA NPN「Power and Cooling Solutions 优选合作伙伴」—— 2026-09-29
见第 3 条 (A)。核心：加入 NVIDIA Partner Network 为 Preferred Partner；2.6 MW CDU 过 DSX Ready；
600 kW / 1 MW 过 AI 基础设施资质；年内计划送 4.0 MW。引语：**James Lee, presidente da LG ES Company**。

### 6.3【可入刊】LG "Chip-to-Chiller" 于 Data Centre World Asia 2026 展出 —— 2026-09-29
见第 3 条 (B)。DCWA 2026 = 9/29–9/30，Marina Bay Sands Expo & Convention Center, Singapore；
展位面积「为 2025 年的三倍以上」（厂商标称）；展品含预制 hydronic 模块、无油磁悬浮离心空冷冷水机、
NVIDIA 认证 CDU、浸没冷却、Fan Wall Unit、DCCM。

### 6.4【可入刊，谨慎】Midea Building Technologies 于 DCWA 2026 发布「电冷超融合」—— dateline SINGAPORE, Oct. 2, 2026，窗口内
https://www.prnewswire.com/in/news-releases/midea-showcases-breakthrough-cooling-technologies-for-high-density-ai-data-centers-at-data-center-world-asia-2026-302893929.html
**全部厂商标称、无第三方实测**：
- Magnetic CDU："reduces equipment footprint by **up to 70%**... supports a **PUE below 1.2** under suitable operating conditions"
- 空冷磁悬浮离心机："delivers a **COP of up to 5.4**"
- **Industrial-Grade CDU："2.6 MW cooling capacity at a 3K temperature difference"**（**与 LG 的 2.6 MW 是不同厂商的不同产品，别串**）
- Gui'an Midea Cloud Data Center（与 Keppel 合作）："up to **7,654 hours** of annual free cooling and a stable **PUE below 1.2**"
- 规模："193 local service sites across 29 countries, and spare parts centers in 34 countries"

### 6.5【可入刊】Castrol 发布 "Castrol CORE" —— dateline SINGAPORE, Sept. 29, 2026，窗口内
https://www.prnewswire.com/news-releases/castrol-launches-castrol-core-an-integrated-thermal-management-offer-for-data-centres-302889530.html
从产品型转服务/整合型（设计+部署+启动+运维）；"cooling technologies, which have been tested and validated with
leading chip and hardware manufacturers **including NVIDIA and Intel**"（**厂商标称，稿中未给任何验证数据**）；
实验室在英/美/德/中；服务网络 "more than 150 countries"；中国完成一个 PoC。
引语：**Peter Huang, Global President of Data Centre and Thermal Management at Castrol**。

### 6.6【可入刊，边缘】MagPro（南京思普科技，CIGU × EPG 合资）AeroLev 1850 —— dateline SINGAPORE, Sept. 28, 2026，窗口内
https://www.prnewswire.com/news-releases/magpro-launches-aerolev-1850-to-advance-water-smart-cooling-for-ai-data-centers-302892313.html
**全部厂商标称**：1.85 MW 级、45 °C-ready 空冷磁悬浮；压缩机 "isentropic efficiency of up to 87%"；
专利冷凝器 "subcooling of more than 3°C"；"up to **40%** higher overall energy efficiency and up to **8%** lower
failure rates compared with **conventional oil-lubricated compressors**, and up to **10%** lower maintenance costs
compared with **conventional chillers**"（**三个相对量基准不同，务必分别标注基准**）；
"can supply chilled water at temperatures up to 45°C"；">6,000-square-meter production base and two air-cooled
laboratories, supporting testing of air-cooled units up to 2,000 kW"。

### 判为弱相关 / 不建议入刊
- Compal 于 OCP 展 NVIDIA AI Factory 基础设施（2026-09-29，一手）—— 仅定性，**无任何具体数字**
- SUNON "Build to Chill" OCP 展前稿（2026-09-29，一手）—— 纯展前预告，**无规格数字**，仅对确认 OCP 日期有用
- Modine 完成 Performance Technologies 分拆并与 Gentherm 合并（2026-10-01，一手）—— 分拆的是**车用**热管理，
  不是数据中心冷却（Airedale）业务，与本刊主题无关

---

## 汇总：含「厂商标称」数字的条目（触发 rules 第 20 条 (d)）
- LiquidStack CDU 2.X：2.5 MW@4 °C ATD、3,750 lpm@3.5 bar、45 °C 进水、Q2 2027 出货 —— **厂商标称 + 二手转述，双重降级**
- Vertiv：22,000 m²、18–24 个月、数百岗位/2027–2029 —— 厂商标称（前瞻性计划）
- LG：2.6 MW、600 kW / 1 MW / 4.0 MW、「DSX Ready 中容量最大」—— 厂商标称；后者**带自限定脚注，不可去掉**
- LG 弗吉尼亚：350,000 ft²、43 acre、H1 2027、KRW 1500 亿 —— 厂商标称；**150+ 岗位是州长口径**；
  **226→420 GW / +194 GW / 60% 是 Omdia 分析师估计** —— 三种口径须分开标
- Midea / Castrol / MagPro —— 全部厂商标称
- LITEON：25%、US$176M —— 公司公告（非产品性能，口径较硬）
- NVIDIA DSX Ready：**CDU 类别为厂商「自我认证（self-qualification suite）」**，与 BESS 的「NVIDIA review and
  approval」不同；另有免责「通过资质不替代站点级工程、不意味站点级稳定性」
