# scout-E 回传 · 产业动态（原样存档）

窗口 2026-11-15 ~ 11-21。「PRN 搜索页」= `https://www.prnewswire.com/search/all/?keyword=` 列表页，ET 时间戳取自该页，
稿件 dateline 取自稿件页正文。**未去过/403 的通道**：ecolab.com、businesswire.com、hpcwire.com、datacenterfrontier.com、
energy.gov、arpa-e.energy.gov、intelligence.uptimeinstitute.com 均被代理 403，没取到原文。DCD `/en/news/` 只读前 3 页。
以下「稿内含液冷」均指已读正文确认。

## ① 事实条

### 1. CoolIT × Ecolab：CHx 3000 CDU（SC26）
- 一手稿**未取到**（Ecolab 官方稿在 BusinessWire / ecolab.com，均 403；HPCwire 转载页 403）。
- 二手（DCD，可读）：https://www.datacenterdynamics.com/en/news/coolit-ecolab-launch-3mw-cdu/
  页面署名日期 2026-11-18（Dan Swinhoe）——**这是 DCD 的日期，不是 Ecolab 稿的 ET 时间戳**。
- DCD 转述数字（厂商宣称）：3 MW；3 °C 趋近温差 ATD；支持 45 °C 暖水；单台最多 18 机架、190 kW/架；
  CDU 自身耗电 75 kW；含 Ecolab 3D TRASAR 冷却液监测；**Q1 2027 起发货**；Alfa Laval 提供换热器与流量部件。
- 同稿另提：同周 Ecolab × Siemens 合作（电力分配、自动化、数字孪生），虚拟孪生与 Dassault 合作开发——未取到一手。
- 未披露：价格、冷却液类型、换热器面积、Siemens 合作具体交付物。
- ⚠️ **3 °C ATD 只适用于 CHx 3000，不得与 Delta 或 Project Deschutes 的 ATD 混用。**

### 2. ZutaCore × Munters：Z₂O 无水两相芯片到屋顶架构（SC26）
- 一手稿 BusinessWire `…/20261116955324/en/ZutaCore-Unveils-ZO-at-SC26-Zero-HO-Near-Zero-Cooling-Energy` → **403，未读到正文与 ET 时间戳**。
- 仅检索摘要转述（**未核**）：建模 pPUE 1.03、WUE=0、625 kW IT 块、74% 年冷却能耗降低、
  首个服务器配置 ASRock Rack HGX B300、其他伙伴方案预计 2027 年上市。
- 🟢 **独立旁证（已读正文的一手稿）**：MiTAC PRN
  https://www.prnewswire.com/news-releases/mitac-computing-scales-agentic-ai-with-full-stack-infrastructure-at-sc26-302941327.html
  时间戳 Nov 16, 2026 22:15 ET（PRN 搜索页），dateline Nov. 16, 2026。
  原文数字：基于 **G4826Z5** 的**无水两相 DLC 概念验证（PoC）**，**TDP 超过 4,000 W**、**热流密度超过 250 W/cm²**、
  **年化 pPUE 1.03**——均厂商宣称、PoC 性质。
  ⚠️ 该 pPUE 1.03 与 Z₂O 的建模值数字相同但分属不同稿件，**须分开标注**。
- 未披露：Z₂O 一手稿全文、实测数据、价格。

### 3. Solenis × Vertiv：液冷流体管理合作
- 一手稿 https://www.prnewswire.com/news-releases/solenis-and-vertiv-partner-to-advance-liquid-cooling-management-for-ai-data-centers-302945426.html
- 时间戳 Nov 19, 2026 08:00 ET；dateline WILMINGTON, Del., Nov. 19, 2026。
- 原文数字：Solenis 服务全球**超过 500 个数据中心**；**稿内无性能数字**。
- 内容：流体健康（化学与监测）、OnGuard™ 水和乙二醇监测、Vertiv Next Predict 预测性维护。
- 未披露：商业条款、排他性、覆盖产品型号。一手，置信度高。非冷板硬件。

### 4. Panduit AI Cooling Lab
- 一手稿 https://www.prnewswire.com/news-releases/panduit-expands-data-center-innovation-with-new-ai-cooling-lab-302941280.html
- 时间戳 Nov 16, 2026 21:10 ET；dateline TINLEY PARK, Ill., Nov. 16, 2026。
- Thermal Lab 扩建并更名 AI Cooling Lab，展示 RDHx / 单相 DTC / 两相 DTC / 浸没四种路线。**原文无任何数字**。
- 未披露：面积、投资额、设备品牌与容量。相关性弱到中。（搜索聚合页写 11-17，以 PRN 稿 11-16 为准。）

### 5. Arivor Technologies（AEWIN 子公司）：两相 DLC 机架级方案（SC26）
- 一手稿 https://www.prnewswire.com/news-releases/arivor-technologies-highlights-two-phase-dlc-rack-scale-solution-for-high-density-ai-workloads-at-sc26-302941606.html
- 时间戳 Nov 17, 2026 08:00 ET；dateline CHICAGO, Nov. 17, 2026。
- 原文数字（厂商宣称）：机架级冷却能力**最高 200 kW**。
- 内容：智能 CDU（压力调节、汽液分离）、两相冷板（微结构）、不锈钢歧管、干断快接。
- 未披露：冷却剂种类、压降、芯片级热流密度、单卡 TDP 验证、客户。一手，置信度中高。

### 6. ZTE：1.5 MW 冷板式液冷 CDU
- 一手稿 https://www.prnewswire.com/news-releases/zte-powers-high-efficiency-aidc-with-robust-energy-infrastructure-302940311.html
- 时间戳 Nov 16, 2026 05:33 ET；dateline SHENZHEN, China, Nov. 16, 2026。多语种版本（11-17~11-18）系同稿翻译。
- 原文数字（厂商宣称）：单机 **1.5 MW**、可扩至 **2.4 MW**、配置 **2–5 个 CDU 柜**；控温 **±0.5 °C**、控压 **±0.05 bar**。
- ⚠️ 稿中 **PUE 1.15 对应 HVDC 配电加 32 °C 送风的整体方案，不是 CDU 指标**，别张冠李戴。
- 稿中称 Karakoram-01（巴基斯坦）采用冷板液冷。未披露：ATD、冷却液、发货时间、价格。一手，置信度中高。

### 7. Compal：Rubin HGX NVL8 机架级 DLC（SC26）
- 一手稿 https://www.prnewswire.com/news-releases/compal-unveils-rack-scale-liquid-cooling-solutions-powered-by-nvidia-at-sc26-302943215.html
- 时间戳 Nov 18, 2026 10:00 ET；dateline CHICAGO, Nov. 18, 2026。
- 原文数字：每机架最多 **9 台 OG231-2-L1 DLC 服务器**、共 **72 颗 Rubin GPU**（每台 8 颗）。
  ⚠️ 稿中 400 PF NVFP4、10× token 吞吐为 NVIDIA 口径转述，**与冷板无关，建议不引**。
- 只提「DLC、泄漏防护」，**无热学数字**。相关性弱。稿中无任何 Rubin 单芯片功耗（符合排除项）。

### 8. Aviemore：无密封磁耦合泵（CDU 用）
- 一手稿 https://www.prnewswire.com/news-releases/aviemore-launches-seal-less-magnetic-coupling-pump-platform-for-liquid-cooled-ai-data-centers-302939792.html
- 时间戳 Nov 16, 2026 12:00 ET；dateline CHICAGO, Nov. 16, 2026。
- 原文数字：输出功率 **0.10–5.0 kW**、直流母线 **12–800 V DC**；机架 CDU 泵 **0.10–2.0 kW**。
- ⚠️ 稿称当前机架 140 kW、240 kW 在后、600 kW 至 MW 级在规划、800 VDC 首批商用系统预计 2027 Q2 出货
  ——这些是**厂商背景叙述**，不当作事实引。
- 未披露：流量与扬程、寿命数据、客户。相关性中偏弱。一手，置信度高。

### 9. MES, Inc.：冷板平面度与表面粗糙度加工指引
- 性质：加工外包公司的技术指引稿，**营销属性重**，但含可引的工程数字。
- 一手稿 https://www.prnewswire.com/news-releases/as-ai-processor-packages-grow-mes-publishes-guidance-on-when-tighter-cold-plate-flatness-adds-cost-without-improving-cooling-302944112.html
- 时间戳 Nov 18, 2026 11:29 ET；dateline COLUMBUS, Ohio, Nov. 18, 2026。
- 原文数字（**厂商指引，非实验**）：30 mm 管芯上 0.025 mm 平面度 = 1/1,200，70 mm 管芯 = 1/2,800；
  TIM 厚度 25–75 µm、导热几 W/(m·K)、铜约 388 W/(m·K)；凹陷 0.040 mm 可使局部 TIM 最多多 40 µm；
  推荐表面粗糙度 **Ra 0.4–0.8 µm**；推荐工作规格 0.025 mm（跨管芯接触区），最终以热模型为准；
  公差自 0.025 mm 收紧到 0.015 mm 可能由精密 CNC 转为磨削或飞刀。
- 未披露：测试数据、热阻实测、样品量。相关性中、偏制造工程。一手，置信度中（工程建议性质）。

### 10. Phononic：Trinity Capital 1 亿美元债务融资
- 一手稿 https://www.prnewswire.com/news-releases/trinity-capital-inc-provides-100-million-in-debt-financing-to-accelerate-phononics-growth-and-manufacturing-expansion-for-ai-data-centers-302941276.html
  时间戳 Nov 17, 2026 08:00 ET。DCD 二手 https://www.datacenterdynamics.com/en/news/phononic-raises-100m-debt-facility-to-fund-solid-state-cooling-system/ （2026-11-19）。
- 原文数字：**US$100 million** 债务，用于产能扩张；DCD 称利率、期限、提款安排均未披露；客户为未具名美国超大规模厂商。
- ⚠️ **稿内不含液冷或冷板**：固态热电冷却，面向激光器、存储等局部器件，**不是冷板路线**。相关性弱。

### 11. Nexalus × Renda：Nova8 液冷 AI 服务器
- 一手稿**未取到**（PRN 搜索页未检出 Nexalus）。
- DCD `/en/news/` 列表页见标题「Nexalus and Renda launch liquid-cooled AI server for data center retrofit market」，
  日期 20 Nov 2026，副题「Features eight Nvidia Blackwell GPUs」，**未取到正文**。
- WebSearch 转述（**未核**，来自 Unite.ai 等）：4U、8 颗 96 GB RTX PRO 6000 Blackwell；**射流冲击冷板**；
  内部液冷回路经液对气换热器排热到室内空气；宣称吞吐最高 +20%、能效最高 +22%（**对比基线待确认**，转述方称未验证）。
- 相关性中。置信度低，需 verifier 复核。

### 12. 其他：已读、可弃或仅作背景
- **ASUS** Vera Rubin NVL72 出货与 SC26（Nov 17, 2026 01:30 ET；同稿另有 01:08 ET 条目）：仅提 NVL8 有 3U 混合冷却型号与 2U 全液冷型号，
  **无冷板热学数据**，相关性弱，可弃。
- **Midea** SC26 北美首秀（磁悬浮 CDU + 干冷器预制模块，Nov 20, 2026 06:53 ET，dateline CHICAGO）：
  属去重名单中的 Midea Building Technologies，且是整机预制与冷机侧、非冷板，**建议不回传**。
- **MSI**（11-16，DLC 1OU 2 节点，CPU TDP 最高 600 W）、**Acbel**（11-16，冷板或浸没液冷电源）：展会稿，相关性弱，未精读。
- **ValorC3**（11-18）：数据中心开发稿，不收。
- **Supermicro** Vera Rubin NVL72 + 1.8 MW 行内 CDU：StorageReview 页面日期 2026-09-25，**早于窗口**，不收。
- **Munters** 投资与产能：2026-11-11，早于窗口，不收。
- **Modexus Solutions（原 Modine）**：Nov 18 投资者日稿，会提液冷，未精读，不收。

### 本角度未检出的重点公司
Accelsius、JetCool、Boyd、LiquidStack、Iceotope、Submer、Asetek、Rittal、Legrand、Corintis、Cooler Master、
Schneider、Johnson Controls、Carrier —— PRN 搜索路径无窗口内稿件，WebSearch 亦未见 11-15 起新稿。
nVent、Motivair：PRN 搜索路径有命中，但均为 MarketsandMarkets / DC Market Insights 分析师稿提及，**非公司稿**。

## ② 分析师 / 市场数字
**以下均仅读到 PRN 搜索页片段，未读正文。**

| 机构 | 发布时间戳（ET，PRN 搜索页） | 数字 | 口径 | URL |
|---|---|---|---|---|
| MarketsandMarkets | Nov 17, 2026 10:01 | 数据中心漏液检测系统市场 2031 年 US$1.07 billion | 市场规模预测，仅漏液检测、非冷板 | https://www.prnewswire.com/news-releases/data-center-leak-detection-systems-market-worth-1-07-billion-by-2031--exclusive-report-by-marketsandmarkets-302942018.html |
| Frost & Sullivan | Nov 20, 2026 09:21 | 全球 HVAC 设备市场 2031 年 US$383.6 billion | 整体 HVAC，数据中心冷却仅为驱动因素 | 搜索页片段，未取单页 URL |

Wissen Research（Nov 11）在窗口外，且含被排除的 Daikin 欧洲 CDU 二手内容，**不收**。

## 定向检查结果
### 1. DOE COOLERCHIPS 1.5 与 Uptime 75% → **取不到，结案**
- COOLERCHIPS 1.5：`energy.gov` 与 `arpa-e.energy.gov` 均代理 403，一手页读不到。
  WebSearch 摘要（**二手，不作证据**）称 `energy.gov/node/4860068` 带 2026-08-26 日期、描述扩展测试验证 1 MW/机架的一二次侧回路；
  另有 `energy.gov/sites/default/files/2026-09/CX-271071.pdf`；另一文件称共 8 个小型研发项目。**均只证明 URL 存在，未取到一手原文。**
- Uptime 75%：可读到 2025 Cooling Systems Survey 资源页标题，样本 n=1,033，主题为 DLC 采用情况（仅少数运营商已部署）；
  `intelligence.uptimeinstitute.com` 403，**没读到任何 75% 数字**，检索摘要明确说未发现该数字。→ **75% 无一手证据，继续不用。**

### 2. 3C Datalec → **窗口内无新稿**
PRN 搜 `Datalec` 与 `3C liquid cooling`，最新仍为 2026-10-14 07:02 ET（英文合并稿）与 2026-10-15 02:56 ET（印尼文版）。

## 其他说明
上期已刊事件（Delta 800 VDC CDU、Frore、Daikin Applied、Chatsworth × ZutaCore、Vertiv RPP、3C Datalec 合并）
本期未发现新状态，均未重复回传。条目 1、2、11 是否算「新增」由主代理判断去重。
