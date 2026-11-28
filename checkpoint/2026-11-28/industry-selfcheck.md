# 产业侧 · 主代理自查（scout E 两轮均报「窗口内空」，经复核不成立）

## 关键发现：prnewswire.com 本会话**可达**（HTTP 200），scout E 未实际尝试
scout E 两轮共 12 条 WebSearch，结论「窗口内未检出」，并自述 `fetch_source.py` 全被代理 403 拦。
主代理直连复核：
- `https://www.prnewswire.com/news-releases/news-releases-list/` → **HTTP 200**
- `https://www.datacenterdynamics.com/en/news/` → HTTP 403（确实不可达）
- `https://www.businesswire.com/` → 连接失败
- `www.se.com`、`stocktitan.net` → 代理 connect_rejected 403

→ **PRN 可达**。主代理自行扫 PRN 搜索页 18 个关键词（liquid cooling / cold plate / coolant distribution unit /
data center cooling / immersion cooling / direct-to-chip / CDU / two-phase cooling / thermal management data center /
AI data center cooling / heat sink / rack cooling / Vertiv / nVent / Boyd thermal / JetCool / Accelsius / Motivair /
LiquidStack / CoolIT / Asetek / Chilldyne / ZutaCore / Fabric8Labs），共解析 ~430 条稿件卡（标题+日期+URL），
筛出发布日落在 **2026-11-22 ~ 11-28** 的条目如下。

## 窗口内 PRN 条目（逐条判定）

### ✅ 收录 · Midea Building Technologies 于 Big 5 Global 2026 展 AIDC 冷却（2026-11-26，一手 PRN，全文已直读 4,524 字符）
URL：https://www.prnewswire.com/news-releases/midea-showcases-full-stack-aidc-cooling-and-commercial-hvac-solutions-built-for-extreme-climates-at-big-5-global-2026-302950365.html
dateline：DUBAI, UAE, Nov. 26, 2026；展会 Big 5 Global 2026 于 **11 月 26 日**在 Dubai World Trade Centre 闭幕。
**AIDC 相关（厂商标称，原文引证）**：
- 「air-liquid converged」架构，可对冷源、CDU、风墙作动态分配以适应不同机架密度
- **AirBoost 变频风冷螺杆冷水机组**：环境温度最高 **55 °C** 可连续运行；出水温度范围 **5–35 °C**；
  工质 **R1234ze(E)**（低 GWP）；断电后快速恢复 **120 秒内**
- 其风冷侧**稀土铝合金微通道换热器**通过 **9,000 小时**盐雾测试，可选 TCP 与 E-coating 防护
- **高效双源风墙**使自然冷却时间延长**最多 28%**
- **MagBoost 冷水机组**：磁悬浮 + 永磁同步电机、无油无摩擦，称全生命周期成本降至传统机组的**不到一半**；
  通过 AHRI 与 CE 认证；可作 AIDC 的水冷/风冷核心冷源
- 服务网络：备件中心覆盖 **34 国**（当日达）、**29 国 193 个**本地服务点
**⚠️ 去重要点**：稿中「Midea CDU 业界领先 **2.6 MW**」**第 8 期已报**（第 8 期记为「工业级 CDU 标称 2.6 MW @ 3 K 温差」，
Data Centre World Asia 2026，2026-10-02 一手稿）→ **本期不复述该数字**，无实质进展。
**⚠️ 另注**：本稿大部分内容为商用 HVAC（ProFit Rooftop、V8 VRF）—— **不在本刊覆盖面，不写**。
**⚠️ 全部数字为厂商标称、无第三方实测。**
**⚠️ 同源另一场（窗口外）**：Midea 于 **DCW Middle East 2026**（阿布扎比，11-18 闭幕）另有一稿 → 窗口外，不收。

### ❌ 不收 · Fluidstack Blackbird 400 MW 模块化数据中心（2026-11-24，一手 PRN，全文已直读）
URL：https://www.prnewswire.com/news-releases/fluidstack-launches-modular-400-mw-data-center-products-designed-to-be-built-in-six-months-302949865.html
理由：**冷却技术含量近乎为零**。全文涉冷却仅一句——Compute Module 为「承载电力、冷却与布线的自支撑吊顶结构，
内置热通道封闭（HAC）」；**无液冷、无冷板、无 CDU、无供液温度或冷却容量**。HAC 属风冷气流封闭。
其数字（400 MW、单区 10+ MW 起、6 个月建成对行业 18–24 个月、Glendale 工厂 110 万 ft²、1,250 个岗位、
35 kV 进 480/415 V 出）均属数据中心建造与配电，不属本刊散热主线 → 按 rules 第 14 条不凑数。

### ❌ 不收 · IT Availability LLC「仅浸没式」数据中心构想（2026-11-23，一手 PRN，全文已直读）
URL：https://www.prnewswire.com/news-releases/it-availability-llc-proposes-new-immersion-only-data-center-model-to-address-community-infrastructure-concerns-302947848.html
理由：**是概念倡议、非产品**。稿件自带免责——配图注明「Conceptual rendering ... **Not an operating facility**」，
且「Proposed design elements remain subject to detailed engineering, permitting, commercial analysis, and
site-specific evaluation. **Final specifications and performance metrics would be established during subsequent
development phases**」。全稿唯一数字是建筑面积「不足 30,000 ft²」，**无任何散热性能指标** → 不收。

### ❌ 不收 · 其余窗口内 PRN 条目
- `302951672`（11-27）Arrvel 无风扇工业面板 PC —— 边缘工业 PC 产品，非数据中心/冷板
- `302948915`（11-24）CIMI 高密度氧化铝陶瓷管/板/棒材 —— 元件供应商目录式发布，按 rules 第 4 条不作来源
- `302948074`（11-23）ZTE 高效 AI 数据中心能源基础设施（德文版）—— **第 14 期已报同一条英文稿，属译文重发**
- `302951019`（11-26）/ `302950314`（11-25）EVE Energy AIDC 储能 —— 电力侧 BESS，非冷却
- `302949391`（11-24）Global Growth Insights「数据中心市场 2035 年 2,842.7 亿美元、CAGR 4.09%」—— 全文已直读，
  **通篇无冷却专项数字**（冷却仅泛泛提及）→ 不进「前瞻分析」节，按 rules 第 12、14 条不凑数
- `302949781`（11-24）HVAC 季检提示（HelloNation 软文）、`302947170` EcoFlow、`302946790` REDMAGIC、
  `302950755` Baffin 工靴、`302950213`/`302949169`/`302947970` 建材与均质机市场报告、`302946943` 燃气轮机市场 —— 全不相关
- 按公司名扫 12 家冷却厂商（Vertiv / nVent / Boyd / JetCool / Accelsius / Motivair / LiquidStack / CoolIT /
  Asetek / Chilldyne / ZutaCore / Fabric8Labs）：**窗口内零条**

## 一条未能落实的线索（转挂账，不入本期正文）
extended WebSearch 提示 **Schneider Electric 2026-11-26 在意大利 Conselve 工厂将先进液冷产能翻倍、
并建实验室使冷却系统测试能力增至三倍**。
**本期不收**，理由：① 一手源 `www.se.com` 与转述页 `stocktitan.net` **均被代理 403 拦**；
② 第二次定向检索（含「Conselve」字样）**零命中支持该说法**，连 Conselve 都未出现；
③ 检索工具自述其摘要部分仅据标题、未读正文。
→ 按 rules 第 1、3、4 条**不予采用**，转入 `drafts/open-items.md` 待下期在 se.com 可达时重核。

## 其余窗口外、仅供去重核对（本期一律不收）
nVent SC26（11-16，含 OCP 兼容 L2A CDU 与 2.3 MW 模块化 CDU）、Ecolab/CoolIT CHx 3000（11-16，第 14 期已报）、
ZutaCore × Munters Z₂O（11-16）、Daikin CDU（11-02，400 kW~2.5 MW）、Panduit 液冷实验室（11-17）、
Cooler Master OCP 2.5 MW CDU（10 月）、Acbel SC26（11-17 前后）、Vertiv MegaMod HDX（约 11-14）、
AVC 财报（11-10，含「占 NVIDIA GB200/GB300 冷板市场约 40–50%」的**二手份额估计，来源未明，不得引用**）。
