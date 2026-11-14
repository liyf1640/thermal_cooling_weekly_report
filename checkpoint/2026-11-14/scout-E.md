# scout-E（产业动态）· 第 13 期 · 窗 2026-11-08~11-14

扫描范围：PRNewswire 站内搜索（liquid cooling / coolant distribution unit / direct-to-chip / immersion cooling / SC26 /
Datalec / NVIDIA Vera Rubin cooling）及命中稿件原文，全部用 fetch_source.py 取原文。
- 未能访问：businesswire、globenewswire（本会话网络白名单外，getaddrinfo ENOTFOUND）
- DCD `/en/cooling/` 返回 404，未取到列表页，DCD 角度本期基本空白
- 去重：以下全部 URL 已对照 reported-index 第四节，**均不在已报表内**；Chemours Faizeon（11-02）、Vertiv 10-26 稿等已报，已丢弃

## 一、事实条

### 候选 1 · Delta SC26「Grid-to-Chip」冷却展品（含上期挂账的 800 VDC L2L CDU）
- Delta Electronics（Americas），SC26（Chicago，11-17~19，展位 #1443）参展预告
- 日期 2026-11-11（正文 "CHICAGO, Nov. 11, 2026"；PRNewswire 列表 09:00 ET）
- 稿中数字（**均为厂商宣称**）：
  - **800 VDC 2.5 MW In-Row L2L CDU**：3 台 800 VDC 25 kW 热插拔泵，3+0 配置，"zero-downtime"，流量最高 3,850 LPM，工作点压力 60 psi
  - Project Deschutes Open In-Row CDU：最高 2 MW，趋近温差 3 °C
  - 4U In-Rack CDU：最高 200 kW
  - Google OCP Project Brazos 机架式液-气 CDU：最高 60 kW/机架，自包含闭环
  - Power Shelf Embedded Cold Plate（首发）：超薄多通道，稿中称用于「最高 3,000 W 的计算部件」
    ⚠️ 该表述在导语；细节段把 3,000 W 对应到 VPD 双面冷却方案，**导语与细节段归属有出入，建议 verifier 复核**
  - VPD 双面冷却方案（OAC 架构）：计算部件最高 3,000 W + 功率部件 500 W，40 mm 薄冷板，热流密度 >170 W/cm²
  - 热插拔 SSD 冷板；芯片级先进 TIM + 微通道盖板（micro-channel lid）；风冷 450 mm EC 风墙
- 稿中未给：800 VDC CDU 的 **ATD、供/回水温度、尺寸、冗余等级（除 3+0 泵配置外）**；无规格表、无产品页链接
- 来源 https://www.prnewswire.com/news-releases/delta-unveils-from-grid-to-chip-cooling-innovations-for-ai-infrastructure-and-for-new-800-vdc-400-vdc-architectures-at-sc26-302935999.html

### 候选 2 · Gates 发布 ThermalCool 2100SS 泵（CDU 用）
- Gates Industrial（NYSE: GTES），为机架式 CDU 推出紧凑 4U 兼容不锈钢泵（此前产品线有软管、UQD、接头）
- 日期 2026-11-12（正文 "DENVER, Nov. 12, 2026"；列表 16:30 ET）
- 稿中数字（**均为厂商宣称**）：最高 200 L/min @ 3 bar；4U 兼容；电机「电干式」由泵送冷却液主动冷却、无需独立回路或风扇；
  不锈钢结构、OCP 合规湿接触材料、IP55、额定寿命 50,000 小时；支持并联与 N+1 冗余；CANBUS / MODBUS；预计 2027 年初全球上市
- 稿中未给：终端 CDU 客户（仅称 "a leading CDU manufacturer"）、扬程曲线、功率、价格
- 来源 https://www.prnewswire.com/news-releases/gates-introduces-compact-thermalcool-2100ss-pump-to-expand-data-center-portfolio-302937904.html

### 候选 3 · Frore Systems LiquidJet 冷板获 CES 创新奖
- Frore Systems，直触芯片 LiquidJet 冷板入选 CES Innovation Awards 2027 企业科技类（奖项属第三方 CTA，数字为厂商自称）
- 日期 2026-11-11（正文 "SAN JOSE, Calif., Nov. 11, 2026"；列表 09:26 ET）
- 稿中数字（**均为厂商宣称**）：LiquidJet GPU 最多降温 12 °C、最多 +25% AI tokens/W、可处理热点热流密度 670 W/cm²；
  LiquidJet Diamond（嵌金刚石热扩展层）最多降 22 °C、最多 +35% tokens/W、770 W/cm²；
  白皮书 "Cooling Is the Next Revolution" 称全热栈优化可多产出 >40% tokens；工艺为把半导体工艺适配到金属晶圆
- 稿中未给：基准 GPU 型号、流量、压降、冷却液温度、测试条件、量产时间（「12 °C cooler」的对比基线未写）
- 来源 https://www.prnewswire.com/news-releases/ai-cooling-unicorn-frore-systems-wins-ces-innovation-award-for-sustainable-ai-cooling-302936581.html
- 说明：标题称 "Unicorn"，估值稿中未核，scout 未验证

### 候选 4 · Daikin Applied 60 MW AI 工厂冷却参考架构 D60-W
- Daikin Applied，基于 NVIDIA DSX AI Factory Platform 与 Vera Rubin NVL72 的 60 MW 冷却蓝图
- 日期 2026-11-10（正文 "MINNEAPOLIS, Nov. 10, 2026"；列表 09:00 ET）
- 稿中数字（**均为厂商宣称**）：60 MW IT 负荷、6 个可部署单元；液冷承担 92%、风冷 8%；
  双回路（高温液体回路接 CDU + 专用低温回路接风冷机架容纳单元）；磁悬浮无油离心冷水机 Magnitude WME 单机最大 10 MW；
  干冷器为主、最热天辅以冷水机、三模式切换（干冷/混合/全机械）；取消冷却塔补水；
  **Daikin Applied 自家 CDU 与干冷器「仍在开发中」，目标 2027 下半年上市**
- 稿中未给：CDU 容量、ATD、供回水温度、单机架流量、Vera Rubin NVL72 冷板或冷却液参数
- 来源 https://www.prnewswire.com/news-releases/daikin-applied-introduces-60-mw-ai-factory-cooling-reference-architecture-302934188.html

### 候选 5 · Armada + Johnson Controls：爱尔兰 Galleon Forge Two 量产
- 位于 JCI 都柏林厂内，开始连续生产 Leviathan 模块化数据中心
- 日期 2026-11-11（正文 "DUBLIN, Nov. 11, 2026"；列表 03:00 ET）
- 稿中数字（**均为厂商宣称**）：都柏林厂 90,000 平方英尺、约 700 名 JCI 工程师/技师；两家目标 2027 年至少 500 MW 产能；
  首台 Leviathan 发往挪威 Fossefall；Gilbert, Arizona 厂预计 2027 初投产、最多 400,000 平方英尺、>500 个岗位；
  计划在加拿大 Edmonton 的 JCI 厂址进一步扩产；JCI 热管理组合含 CDU、冷水机、楼控，称「零水冷却」
- 稿中未给：CDU 型号/容量/冷板规格、Leviathan 单模块 MW 数（仅称 "multi-megawatt-scale"）
- 与冷板相关性：弱到中（液冷落点只有一句话，主体是模块化数据中心制造）
- 来源 https://www.prnewswire.com/news-releases/armada-and-johnson-controls-launch-galleon-forge-two-in-dublin-bringing-sovereign-ai-infrastructure-production-to-europe-302935710.html
- 说明：同稿另有重复发布 ID 302935706，同事件，勿重复计

### 候选 6 · Infinium EDGE ETV100 浸没液获 NSF PFAS-Free 认证
- Infinium（Sacramento, CA），ETV100 获 NSF HT1 食品安全注册与 NSF/ANSI 537 导则下 PFAS-Free 认证
- 日期 2026-11-09（正文 "SACRAMENTO, Calif., Nov. 9, 2026"；列表 07:00 ET）
- 稿中数字：合成烃类流体，经 Fischer-Tropsch 工艺生产，无氟化合物；用于 Vector ONE 浸没模块
- 稿中未给：热物性（比热、导热、黏度、闪点）、介电强度、与冷板单相/两相的对比
- 相关性弱（浸没路线）
- 来源 https://www.prnewswire.com/news-releases/infinium-edge-etv100-immersion-fluid-earns-nsf-pfas-free-certification-and-ht1-registration-as-food-safe-302932662.html

### 候选 7（边缘）· Vertiv PowerStation 3100 RPP
- 高密度远程配电盘，每路分支断路器含集成远程分励脱扣，漏液检测系统可对单机架断电
- 日期 2026-11-13（正文 "COLUMBUS, Ohio, Nov. 13, 2026"；列表 08:30 ET）
- 稿中数字：600/800/1,000/1,200 A 配置；>100 kW 机架；北美现货
- 相关性弱（配电产品，仅「DLC 漏液隔离」一个联动点），scout 建议不入主栏
- 来源 https://www.prnewswire.com/news-releases/vertiv-introduces-high-density-remote-power-panel-for-next-generation-ai-data-centers-302938962.html

### 候选 8（边缘）· Chatsworth Products SC26 预告
- 日期 2026-11-10（列表 09:00 ET）；CPI 发布 OCP ORV3 机架，SC26 展示 ZutaCore HyperCool 无水直触芯片液冷集成进 ZetaFrame 机柜，
  另有 CoolStream 后门换热器（RDHx）早期预览；稿中未给液冷具体规格数字；相关性弱
- 来源 https://www.prnewswire.com/news-releases/chatsworth-products-showcases-rack-power-and-cooling-solutions-for-ai-and-hpc-at-sc26-302932153.html

### 其余命中、判定不收
- XNRGY（2026-11-09 07:00 ET）：10 月出货约 115 台冷水机 + 500 台空侧设备、共 >350 MW → 冷水机/风冷产能，非液冷
- Teadit 垫片稿：列表时间戳 Nov 13 14:13 ET，正文落款 "VADODARA, India, Nov. 14, 2026"，**两者不一致**；内容为密封件营销 → 不收
- Compal SC26（11-10）：仅列 OG430-2-L1（DLC HGX B300）与 OG231-2-L1（Rubin NVL8）型号，无冷却参数 → 不收
- Supermicro H15 AMD EPYC 9006 出货（11-11）：前段无液冷要点 → 不收
- LITEON electronica（11-11）：光互连 → 不收

## 二、三项专项挂账结论
1. **3C（Datalec 合并方）产品稿**：PRNewswire 搜 "Datalec" 仅命中 10-14 合并稿（及印尼语版 10-15），
   **本期未检出** 3C 产品稿，液冷链条具体环节仍无法确认
2. **Delta 800 VDC L2L CDU 规格**：见候选 1。本期稿给出 2.5 MW、3×25 kW 热插拔泵 3+0、3,850 LPM、60 psi，
   但**仍无 ATD、供回水温度、尺寸、冗余等级**，也未检出独立产品页或规格表（deltaww.com 本次未试，上期 403）
3. **NVIDIA DSX / Vera Rubin 冷板或 CDU 一手规格**：本期**未检出** NVIDIA 一手新披露。
   检索只得二手/转述（**未核，勿引用**）：有称单颗 Rubin GPU 最高 2,300 W、另有 1,800 W、3,600 W，归属 Rubin Ultra 或 NVL144 说法不一、互相矛盾。
   Daikin Applied D60-W 稿只引用 DSX / Vera Rubin NVL72 作设计基础，无冷板 TDP 或流量

## 三、分析师 / 市场规模数字（单独收集）
### A1 · Wissen Research：数据中心冷却市场
- Wissen Research，2026-11-11（列表 13:44 ET；正文 "SHERIDAN, Wyo., Nov. 11, 2026"）
- 数字：全球**数据中心冷却市场** 2026 年 "USD 19.5 billion"，2031 年 "USD 42 billion"，CAGR 16.5%（2026–2031）
- 口径：整个数据中心冷却市场（含风冷、液冷、混合、行/机架级），**不是仅液冷**
- 稿中并称 DOE COOLERCHIPS 1.5 计划（2026-08-26 公布）目标 1 MW/机架，并引用 Uptime 2025 调查：75% 运营商用周边风冷
- ⚠️ 稿中顺带罗列的 Boyd ROL2300 CDU 2.3 MW、Vertiv CoolLoop RDHx 80 kW/机架、JCI Silent-Aire CDU 500 kW 到 >10 MW、
  Carrier CDU 1.3~5 MW 等均为**二手汇编，不得当一手引用**
- 来源 https://www.prnewswire.com/news-releases/data-center-cooling-market-to-reach-us-42-bn-by-2031--growing-at-16-5-cagr-as-ai-racks-push-cooling-from-air-to-liquid-wissen-research-302936853.html

### A2 · 其他
- MarketsandMarkets 2026-11-13 Data Center Power Market（2031 年 USD 52.43 billion）与 Laminated Busbar（11-11）均非冷却 → 不入文
- 本窗口**未检出** TrendForce / Omdia / Dell'Oro / IDC / FactMR 的新液冷预测

## 四、早于本期窗口的线索（未取原文，**不得直接引用**）
- **Daikin 新 CDU**：仅检索页转述，称 Daikin（欧洲站新闻稿页）发布 400 kW~2.5 MW CDU，稿日约 2026-11-02，
  订单开放日各来源冲突（2027-11-01 / 2026-11-01），**须取 Daikin 原稿核**。可与候选 4「CDU 开发中、2027 下半年上市」交叉核对。
  URL（未核）https://www.daikin.eu/en_us/press-releases/daikin-ai-data-center-portfolio-expansion-new-coolant-distribution-unit.html
- **Cooler Master OCP 2026**（约 10 月中旬）：检索转述称 2.5 MW 液-液 in-row CDU、300 kW 液冷/风辅 CDU 已量产、
  30 kW 机架内液-气型目标 2026 Q4 量产。仅检索页，未取原文，日期待确认；coolermaster.com 此前 403
- **Trane / LiquidStack CDU 2.X**：检索页称 2026-10-12 发布，但 reported-index 已有同主题 DCD 链接 → 视为已报，丢弃

无可靠的窗口内并购 / 产能扩张 / 认证类液冷新闻（Ecolab-CoolIT、Eaton-Boyd、Vertiv-STL、Trane-LiquidStack 均为早前事件）。
