# 第 14 期 逐位核验存档

通道：`api.crossref.org/works/<DOI>` + `api.openalex.org/works/https://doi.org/<DOI>`（间隔 ≥3 s，无 429）。
原始 JSON 落盘于 scratchpad（cr1-4.json / oa1-4.json）。

---

## 学术侧 第一批（4 条，全部「通过」）

### 1 · `10.1109/tcpmt.2026.3751185` —— **通过**（本期头条）
- **Crossref `created`**：`2026-11-13T20:18:56Z`（与第 13 期记录完全一致）。`deposited` 2026-11-16T20:07:27Z；
  `published-print` `[[2026]]`（不作依据）；无 `published-online`。OpenAlex `created_date` 2026-11-14（仅对照）。
  ⚠️ **主代理注：11-13 早于本期窗口 11-15，属第 13 期挂账指定重试的前期漏收条目**
  → 按 rules 第 5 条**直接收入、如实写原始日期、不加补记标注**（2026-11-02 裁定）。
- container：*IEEE Transactions on Components, Packaging and Manufacturing Technology*，Early Access。标题逐字一致。
- **作者与 sequence（Crossref 为准）**：
  1 Jaswanth Sai Bangaru Garu（`first`）/ 2 Zubair Shaikh / 3 Taehwan Kim / 4 **Jae Choon Kim** / 5 Jaeho Lee（OpenAlex `last`）
  ⚠️ 作者 4 两通道人名不一致：Crossref `Jae Choon` vs OpenAlex `Jaechoon Kim` → **以 Crossref 为准写 Jae Choon Kim**。
- **通讯作者**：Crossref 无该字段；OpenAlex **五位全 false** → **取不到，不可点名**。
- **单位原串逐字**：
  - Crossref（三位 UC 作者三条相同）：`name` = **`University of California`**；`place` = `["Irvine, CA, USA"]`；
    `department` = `["Department of Mechanical and Aerospace Engineering"]`（按 2026-11-02 裁定**不采用**）
  - OpenAlex raw：`["University of California, Irvine, CA, USA"]`
  - Samsung 两位：Crossref `name` = **`Samsung Electronics Co., Ltd`**，`place` = `["Hwasung, Republic of Korea"]`
- **「Irvine 是校区名还是城市名」裁决**：Crossref 结构化三段式把 `Irvine` 放进 **`place`** 并与 `CA`（州）、`USA`（国）同串并列，
  而 `name` 串里**完全没有** `Irvine` → 按字段语义落在**城市槽位**。OpenAlex 扁平串无法区分。
  → **维持第 13 期裁定：不得推定为欧文分校，正文写 `University of California`。**
- **摘要数字逐项**（摘要**仅 OpenAlex 有**，Crossref `abstract: None`；前期 404 已解除）：
  - ASIC 功率 **300 W** ✅（`For an ASIC power of 300 W`）
  - 固体体积分数 **0.6** ✅（`with a solid volume fraction of 0.6`）
  - ASIC **约 90 °C** ✅（`keeps the ASIC at approximately 90 °C`）
  - HBM **43 °C** ⚠️ **口径微差**：原文 `and the HBM at 43 °C`，`approximately` 只修饰 90 °C
    → **43 °C 原文无「约」，不得写「约 43 °C」**
  - 热串扰 **0.075 °C/W** ✅
  - **约为常规平行通道冷板的 1/3** ✅ 基准须完整：`approximately one-third that of a conventional parallel-channel
    cold plate under the same conditions`（基准＝**同条件下的常规平行通道冷板**）
  - **恒定泵功** ✅（`under a constant pumping power`，与上述数字同句，是成立条件，**不可省**）
  - 覆盖面字面：首句确有 `advanced cooling technologies such as direct-to-chip liquid cooling with cold plates`
- **摘要未给（不得补写）**：热流密度、工质种类、通道与冷板几何尺寸、HBM 数量（只有定性 `multiple HBM configurations`）、
  泵功绝对值、温度上限具体值（只说 `within their temperature limits`）、常规冷板串扰绝对值（只给 1/3 相对量）。
- ⚠️ **口径归属**：摘要通篇为拓扑优化框架 + 算法 + 计算结果（`we present a thermofluidic topology optimization framework`／
  `Our algorithm`／`Our study explores…`），**全文无任何实验/样件/实测字样** → **只能写为仿真/优化结果，不得写「实测」**；
  「是否有实验验证」= **摘要未给**。

### 2 · `10.1016/j.ijheatmasstransfer.2026.129907` —— **通过**（单位缺口已补齐）
- **Crossref `created`**：`2026-11-17T17:29:40Z`（与前期记录一致，**在窗内**）。`published-print` `[[2027,3]]`（仅对照）。
  IJHMT **vol 274, article 129907**。标题逐字一致。
- **作者与 sequence**：1 Hrushikesh B. Jadhav（`first`，ORCID 0009-0003-2728-2562）/ 2 Al-Thaddeus Avestruz（ORCID 0000-0001-8961-0734）/
  3 Solomon Adera（OpenAlex `last`，ORCID 0000-0002-3249-301X）
- **单位 —— 前两轮缺口本轮取到**：Crossref `affiliation` 三位**全为空数组**（Elsevier 未交存）；OpenAlex raw 有，逐字：
  - Jadhav：`Energy Transport Lab (ETL), Department of Mechanical Engineering, University of Michigan, Ann Arbor, MI, United States`
  - Avestruz：`Department of Aerospace Engineering, University of Michigan, Ann Arbor, MI, United States`
    ⚠️ **原串如此写 Aerospace**，verifier 不作更正或推断
  - Adera：同 Jadhav
  - 按规则裁剪（删下属实验室 ETL、删城市州）：Jadhav / Adera = **University of Michigan 机械工程系**；
    Avestruz = **University of Michigan 航空航天工程系**
- **通讯作者**：OpenAlex `is_corresponding` = Jadhav false / Avestruz false / **Adera true**（非全 true 非全 false，无伪影特征）
  → **可点名 Solomon Adera 为通讯作者**。
- **摘要数字逐项**（仅 OpenAlex 有）：
  - 局部热流 `exceeds 1 kW/cm²` ✅ 但**是背景句**对功率电子器件的一般陈述，**不是本文实测值**
  - **h ≈ 1100 W/(m²·K)** ✅ ／ 对流空冷 **≈26 W/(m²·K)** ✅ ／ **43 倍** ✅（`a 43 × enhancement over convective air cooling`）
  - 近乎相同结温下浸没 **≈26 W** vs 对流空冷 **≈1.4 W** ✅（基准＝对流空冷）
  - **≈65% 经 drain tab / ≈35% 经塑封体** ✅ 原文均带「约」，且明说是**实验结果**（`our experiments show`）
  - 总热阻降约 **75%** ✅ 基准＝**自然空冷 natural air cooling**
  - 牵引逆变器结温安全上限 **≈150 °C** ✅ 语境为**EV 牵引逆变器的数值分析**，对照为 **forced air cooling**
  - ⚠️⚠️ **三个空冷基准互不相同，成稿绝不得混用/合并**：`convective air cooling`（h 与 26 W/1.4 W）、
    `natural air cooling`（−75% 热阻）、`forced air cooling`（牵引逆变器对照）
- ⚠️ **Icepak / Fluent 原文不一致已逐字确认「真的并存」**：
  第 1 处 `The experiments are compared with a conjugate heat transfer model that is developed using ANSYS Icepak.`
  第 2 处 `After earning credence by validating the ANSYS Fluent model prediction with experiments, we employed the
  numerical framework to analyze the thermal management of traction inverters in electric vehicles.`
  → 同一摘要不同句并存、指向同一个共轭传热模型，属**原文自身不一致**。
  建议**不点软件名**，或原样并列并标注原文不一致；**不得择一写死**。
- **覆盖面字面**：`ultra-high heat flux power electronics`；末句 `the thermal management of silicon power electronics`
  ⚠️ **本条是单相直接浸没冷却（两种介电流体）+ PCB 热扩散，不是冷板**（摘要无 cold plate / channel 字样），
  对象为**功率电子器件与 EV 牵引逆变器**，不是 AI 芯片/数据中心。
- **摘要未给**：两种介电流体的名称/型号、器件型号与封装类型、芯片面积、具体结温数值、流速与浸没槽尺寸、
  热阻绝对值、`1 kW/cm²` 是否在本文实验中达到（背景句而已）、牵引逆变器分析的功率等级。

### 3 · `10.1109/tcpmt.2026.3754479` —— **通过，但覆盖面与首发口径两项须由主代理裁**
- **日期冲突裁决**：Crossref `created` = **`2026-11-16T20:04:47Z`（在窗内）**；OpenAlex `created_date` = 2026-07-07。
  🟢 **差异原因已查明（本轮新发现）**：该 OpenAlex work（W7167481455）**合并了一个 SSRN 预印本版本**
  —— `locations` 含 `https://doi.org/10.2139/ssrn.7067699`（SSRN Electronic Journal，`version: submittedVersion`），
  另一处为 IEEE `publishedVersion`。即 OpenAlex 的 2026-07-07 是**SSRN 投稿版进入 OpenAlex 的时间**，不是 IEEE 版日期。
  ⚠️ ssrn.com 整域不可达，投稿日期本身无法直接核。
  → **IEEE 期刊版落在本期窗内可上；但首发并非本周**，同一工作已有约 2026-07 的 SSRN 投稿版。
- **作者与单位原串逐字（Crossref 七位）**：
  1 **Sujatha Selvamurugan**（`first`）— `Indian Institute of Technology Madras`，place `TN, India`，department `PhD Scholar`
  2 Mannem S V Sayi Teja Reddy — 同 IIT Madras，department `Graduate student`
  3 Badal Modi — `Lam Research Bangalore`（**无 place 字段**）
  4 Dhairyashil Desai — `Lam Research Bangalore`
  5 Dhiman Chatterjee — IIT Madras，place `TN, India`
  6 Pyarimohan Dehury — `Institute of Chemical Technology–IndianOil Odisha Campus`（⚠️ 连接符为 **en dash U+2013**），place `Bhubaneswar, India`
  7 Sarit K Das（OpenAlex `last`）— IIT Madras，place `Tamil Nadu, India`（⚠️ 写法与前几位的 `TN, India` 不同，原串如此）
  - 机构分布核实与候选一致：IIT Madras 四位、Lam Research Bangalore 两位、ICT–IndianOil Odisha Campus 一位
  - ⚠️ `department` 两条为 `PhD Scholar` / `Graduate student`——**根本不是院系（职位误填）**，双重理由不采用
  - ⚠️ 两通道人名不一致（以 Crossref 为准）：作者 2 `Mannem S V Sayi Teja Reddy` vs OpenAlex `Sayiteja Reddy Mannem`；
    作者 4 `Dhairyashil Desai` vs `Dhairyshil  Ramachandran Desai`；作者 7 `Sarit K Das` vs `Sarit K. Das`
- **通讯作者**：Crossref 无；OpenAlex **七位全 false** → **取不到，不可点名**。
- **摘要数字**：水力直径 **2 mm** ✅；**DES + hBN（六方氮化硼）** ✅；
  工作范围原文逐字 `with an operating range of -12 to a boiling point of 151.9 °C at atmospheric pressure, with thermal
  stability up to 151.9 °C` ⚠️ ① **原文 −12 后无单位**（°C 由同句推得）；② **沸点与热稳定上限原文给的是同一个数 151.9 °C**；
  实验**底板温度保持 40 °C 以下** ✅（`in strong agreement with computational predictions`）；
  与高性能螺旋小通道热沉相比**泵压更低 + 温度均匀性更好** ✅ **纯定性**
- **确认均未给**：泵压降低百分比、热流密度、流量/流速、加热功率、进出口数量、hBN 浓度、DES 具体组分、
  热导率提升数值、压降绝对值、GWP 数值。
- **覆盖面字面（原文逐字）**：
  首句 `Efficient thermal management in advanced electronics processing is challenged by the limited heat dissipation of
  conventional systems and the high global warming potentials (GWP) of standard fluorocarbon coolants.`
  末句 `This work provides a practical framework for designing eco-friendly, high-heat-flux cooling systems using
  engineered fluids in robust mini-channel architecture.`
  ⚠️ **摘要通篇无 chip / die / CPU / GPU / processor / package / cold plate 字样**；对象框定为 `advanced electronics processing`
  （题名亦为 `for Processing Electronic Materials`），作者含 **Lam Research**（半导体工艺设备）两位，
  实验指标是**底板温度 < 40 °C**（典型工艺台量级而非芯片结温）
  → verifier 判「**电子工艺（制造）设备侧的小通道热沉 + 环保工质，不是芯片冷板**」。

### 4 · `10.3390/mi17111351` —— **通过**（唯一硬约束：2 W/(m·K) 必须标为模型侧数值）
- **Crossref `created`**：`2026-11-20T10:30:54Z`（与前期一致，在窗内）；**`published-online` 2026-11-20**（MDPI 即时上线）；
  无 print。vol **17**, issue **11**, page **1351**。标题逐字一致。
- **作者与 sequence**：1 **Guofeng Yang**（`first`）/ 2 Jin Zhang / 3 Chi Hu / 4 Yao Li / 5 Shenjiang Wu（OpenAlex `last`）。两通道拼写一致。
- **单位原串逐字 —— 五位全同**：Crossref 五条 `affiliation[0].name` 均为
  `School of Opto-Electronic Engineering, Xi’an Technological University, Xi’an 710021, China`
  （⚠️ 撇号为全角右单引号 U+2019；无 place/department 子字段，整串都在 `name` 里）；OpenAlex raw 逐字相同。
  按规则（院系在原串里出现 → 可写；城市+邮编 `Xi’an 710021` → **必须删**）→ **西安工业大学 光电工程学院**
- **通讯作者**：Crossref 未交存（⚠️ 另注意 Crossref 把 CRediT 角色交存成五位各挂 14–15 个全同角色，属 MDPI 伪影，不可用）；
  OpenAlex = 前四位 false / **Wu true**（`corresponding_author_ids` 亦仅含一人）→ **可点名 Shenjiang Wu 为通讯作者**。
- **摘要数字**（Crossref 摘要全文已取到）：
  - `70W–30Cu` 单向锻造 ✅
  - 体热导率**变化 < 5%** ✅ 原文 `changes the bulk thermal conductivity by less than 5%`
    ⚠️ **原文是「变化」不是「下降」，不得写成「降低不足 5%」**
  - 同注入电流下封装激光 bar 输出功率**降约 20%** ✅
  - **有效热导率 2 W/(m·K)** —— 数字在原文，但口径须标注，见下
- ⚠️ **2 W/(m·K) 口径判断**：原句 `A combined analysis of thermal diffusivity, heat capacity, electrical conductivity,
  hardness, and an illustrative finite-difference thermal model shows that an effective conductivity of 2 W m−1 K−1
  raises the peak temperature, despite an unchanged bulk conductivity.`
  依据：① 句中明确列举的**实测量**是 thermal diffusivity / heat capacity / electrical conductivity / hardness，
  **有效热导率不在实测清单里**；② 该值由 `an illustrative finite-difference thermal model`（**示意性**有限差分模型）引出；
  ③ 句式为「模型 shows that 某有效热导率 raises the peak temperature」，读作模型输入/情景设定更自然。
  → **倾向判为模型侧设定/代入值，不能读作实测值**；但原文并未明文写 assumed / measured，**句法不足以 100% 断定**。
  **成稿硬约束**：要么写「示意性有限差分模型中取有效热导率 2 W/(m·K) 时峰值温度上升」，要么不写这个数；
  **绝不可写成「实测界面有效热导率仅 2 W/(m·K)」**。另：该句只说 `raises the peak temperature`，**没给温升量**。
- **摘要未给**：锻造前/后具体热导率数值、具体注入电流值、绝对输出功率值、热阻绝对值、峰值温度与温升数值、
  锻造工艺参数（变形量/温度/道次）、die-attach 材料与工艺、样品数量与尺寸、表面坑洞尺寸与硬度数值。
- 覆盖面字面：`heat spreaders in high-power semiconductor laser bar packages`、`device-level thermal management`、
  `die-attach heat path` → 对象是**高功率半导体激光 bar 封装的 W–Cu 热沉（材料 + 界面侧）**，不是液冷冷板，不涉数据中心。

## 第一批要点汇总
1. 4 条的 `created` 复核**全部与前期记录一致**，无一处需更正（11-13 / 11-17 / 11-16 / 11-20）。
2. **可点名的通讯作者只有 2 位**：#2 Solomon Adera、#4 Shenjiang Wu。**#1、#3 取不到，不可点名**。
3. #1 的 Irvine 维持第 13 期裁定 → 写 `University of California`。
4. #2 必须分清三个空冷基准；Icepak 与 Fluent 在摘要中确实并存。
5. #3 新发现 SSRN 投稿版先行（`10.2139/ssrn.7067699`，约 2026-07）。
6. #4 的 2 W/(m·K) 不可写成实测，且摘要未给温升量。
7. 须改口径的 scout 表述：#1「HBM 约 43 °C」→ 原文**无「约」**；#4「变化 < 5%」原文是 **changes（变化）**。
8. 覆盖面字面提示（verifier 不代判）：#2 浸没冷却非冷板、对象为功率电子/EV 逆变器；
   #3 摘要无任何 chip/cold plate 字样、对象为工艺设备侧；#4 为激光 bar 封装材料/界面侧。
   **只有 #1 是正经的芯片级冷板 + AI 芯片/异构封装。**
9. **重复报道核查**：`grep` 全仓未发现这 4 条出现在已刊各期正文；#1 仅见于 `drafts/excluded-numbers.md`（第八类，上期未上站）
   与 `drafts/open-items.md`（挂账）。**本轮摘要已取到，挂账条件解除，可结账上站。**

---

## 产业侧核验（A 待确认 / B-1 否决 / B-2 + C1–C5 通过 / D 待确认 / E1 通过 / E2 建议否决）

**两个最重要发现（成稿前必须处理）**
1. **A 条「支持 45 °C 暖水」属 DCD 误述** —— CoolIT 一手产品页写的是 **45 °C 环境空气**（IP54），不是暖水；
   「双换热器」一词一手页根本没有。
2. **ZTE 的 PUE 1.15 归属与候选描述不一致** —— 稿里有**两处不同的 1.15**，候选把它们混成了一句。

### A · CoolIT × Ecolab CHx 3000 CDU —— **待确认（降级为「一手产品页 + DCD 转述」双层标注）**
🟢 **新发现一手源 1**：`https://www.coolitsystems.com/resources/news/ecolab-unveils-first-of-its-kind-integrated-cooling-platform/`
  日期 NOVEMBER 16, 2026，`PUBLISHED_META: 2026-11-16T12:06:25-06:00`（= **2026-11-16 13:06 ET**）。
  ⚠️ 只是摘要桩，**正文仅一句，不含任何数字**。
🟢 **新发现一手源 2（关键）**：`https://www.coolitsystems.com/cdu-product/chx3000/`
  （经 `/cdu-product-sitemap.xml` 找到），**几乎所有规格数字都在这里一手坐实**。
❌ Ecolab 新闻稿原文 `www.ecolab.com/...` 403；`investor.ecolab.com` 403；`globenewswire.com` 403；`stocktitan.net` 403
❌ PRN 搜索 `Ecolab` 与 `CoolIT` 均无此稿（Ecolab 不走 PRN）

| 项 | 一手产品页原文 | DCD | 判定 |
|---|---|---|---|
| 3 MW | `3 MW cooling capacity at 3°C approach temperature difference (ATD)`；规格表 `Cooling Capacity 3 MW` | 同义 | **核实（一手）** |
| 3 °C ATD | 同上 | 同上 | **核实（一手）** |
| 75 kW 自耗 | 规格表 `Power Consumption 75 kW` | DCD 自己的话、无归属 | **核实（一手）** |
| 18 机架 / 190 kW/架 | 规格表 `Racks Managed: Supports up to 18x high-density AI racks per CDU (at 190 kW/rack)` | 「the company said …」 | **核实（一手）** |
| **45 °C 暖水** | ❌ **一手页无「暖水」**。原文 `white or grey space operation with an IP54 rating in up to 45°C ambient air` | `dual heat exchangers support 45°C (113 °F) warm-water operations` | **🔴 不符 —— DCD 误述** |
| **双换热器** | ❌ 一手页**完全没有**这个词 | DCD 有 | **仅 DCD** |
| Q1 2027 发货 | ❌ 一手页未提可用期 | `Units will be available to ship beginning Q1 2027`（DCD 自己的话） | **仅 DCD，一手未证** |
| Alfa Laval | ❌ 一手页未提 | `Ecolab also said it was working with Alfa Laval for its heat exchanger and flow components expertise` | **仅 DCD（DCD 标为 Ecolab 所说）** |
| 3D TRASAR | `featuring Ecolab's 3D TRASAR™ Technology for continuous coolant health monitoring built in` | 同义 | **核实（一手）** |
| 3D TRASAR 七参数清单 | ❌ 一手页只写 `continuous coolant monitoring`，**无参数清单** | DCD 列了 7 项 | **仅 DCD** |

🔴 **DCD 两处问题（成稿严禁沿用）**
1. **45 °C 暖水 = 误述**。一手是 **45 °C 环境空气**（IP54 白区/灰区）。⚠️ 一手页**自身也不一致**：
   引言段 `up to 45°C ambient air`，Features 段 `up to 50°C ambient operation`。
   → 若要提，只能写「厂商标称 IP54、可在最高 45 °C 环境空气下运行（同页另一处写 50 °C，口径不一）」，**绝不可写「支持 45 °C 暖水」**。
2. **单位换算错误**：DCD 把 3 °C 的**温差**换算成 `37.4 °F`。温差 3 °C = **5.4 °F**。**不要引用 DCD 的任何 °F 数值。**

**一手页上候选漏掉的数字（可用，均厂商标称）**：流量 **4,500 LPM**、压头 **50 PSI**；
支持 **NVIDIA Vera Rubin、AMD Helios**（DCD 漏了 AMD Helios）；**IP54**；内置 **ATS**；**N+1** 冗余泵/滤芯/传感器；
最多 **20 台 CDU** 群控；在 CoolIT **6 MW Liquid Lab™** 做出厂验证；定位语「支持 100 MW+ 数据中心」。
**归属**：全部性能数字均为厂商标称（CoolIT/Ecolab 自有页面），**无第三方实测**。
**Ecolab × Siemens / Dassault**：DCD 各一句顺带提及、无数字无一手无时间表 → **不值得单独成条**，最多一句带过并标「据 DCD」。

### B-1 · ZutaCore × Munters Z₂O —— **否决**
一手稿完全取不到：BusinessWire 403、`zutacore.com` / `www.zutacore.com` 403、`www.munters.com` 403、
`globenewswire.com` 403；PRN 搜 `ZutaCore` **无任何 Z₂O 英文稿**（命中 5 条全是 MiTAC 稿的多语种译本）。
→ **下列数字一律不得入稿**：pPUE 1.03（建模）、WUE=0、625 kW IT 块、74% 年冷却能耗降低、ASRock Rack HGX B300、伙伴方案 2027 上市。

### B-2 · MiTAC × ZutaCore 两相 DLC PoC —— **通过**
一手 PRN；**Nov 16, 2026 22:15 ET**（页面 HTML `22:15 ET`，`datePublished 2026-11-17T03:15:00Z`）；dateline `CHICAGO, Nov. 16, 2026` **一致**。
原文逐字（全文仅此一处）：
> `Advanced Liquid Cooling Rack: Partnering with ZutaCore, MiTAC exhibits a PoC integrating the G4826Z5 with
> Waterless Two-Phase Direct Liquid Cooling (DLC). Vaporizing dielectric fluid directly at the chip supports
> thermal design powers exceeding 4,000W and a heat flux over 250W/cm², enabling an annualized pPUE of 1.03.`
全部核实：PoC ✅（原文明写 `a PoC`）/ G4826Z5 ✅ / TDP 超 4,000 W ✅ / 热流密度超 250 W/cm² ✅ / 年化 pPUE 1.03 ✅
**归属**：全部厂商（MiTAC）宣称，自家稿，无第三方实测、无测试方法、无 pPUE 边界定义。
**确为 PoC 非量产**（SC26 展台 Booth 4615），**不得写成产品或已部署**。
另有一条 52U 液冷机架（12 台 G4826Z5 + 96 颗 AMD Instinct MI355X，宣称 `50% higher GPU density than conventional deployments`
—— 基线仅含糊的 `conventional deployments`，若用须原样标注）。
**稿中未披露**：PoC 用哪颗加速器、介质流体牌号、机架总功率、pPUE 测算边界、PoC 地点、量产计划、
**ZutaCore 产品名（稿中未出现 Z₂O）**。
⚠️ 该 1.03 与 Z₂O 检索摘要里的 1.03 **分属不同稿件，未合并、未互证**；Z₂O 条已否决，成稿不得出现「两处 1.03 互证」。

### C1 · Solenis × Vertiv —— **通过**
**Nov 19, 2026 08:00 ET**（搜索页 + 稿页 HTML + `2026-11-19T13:00:00Z` 三者一致）；dateline `WILMINGTON, Del., Nov. 19, 2026` 一致。
**「超过 500 个数据中心」核实**：原文 `Today, Solenis serves more than 500 data centers globally.`
⚠️ 该规模是**与 Chem-Aqua 合并后的全部数据中心客户**，稿中**未**说明其中多少是液冷站点 → **不得写成「500 个液冷数据中心」**。
**确认整篇零性能数字**：无温度、PUE、节能率、MTBF、腐蚀速率、合同金额与期限。
唯一量化内容是公司规模（Solenis 78 个生产基地、23,000+ 员工、160+ 国家；Vertiv 130+ 国家）。
OnGuard™ 原文两处：`OnGuard™ water and glycol monitoring systems`；
`Solenis OnGuard™ monitoring systems for continuous analysis and identification of potential challenges`。
Vertiv 原文：`Vertiv's cooling infrastructure, Next Predict predictive maintenance capabilities and global service scale`。
三大领域：`Fluid health` / `Operational insight` / `Lifecycle performance`（均定性）。
**未披露**：是否排他（稿中反而强调 `preserving customer choice and flexibility`）、金额、期限、起始时间、首批客户、是否涉冷板级别。

### C2 · Arivor Technologies（AEWIN 子公司）—— **通过**
**Nov 17, 2026 08:00 ET**；dateline `CHICAGO, Nov. 17, 2026` 一致。
**最高 200 kW 核实且确为厂商宣称**：`the solution provides rack-level cooling capacity of up to 200kW`，无第三方验证、无测试条件。
**母子公司关系稿中明说** ✅：`Arivor Technologies, a leading provider of two-phase direct liquid cooling solutions and a subsidiary of AEWIN Technologies`
（PRN 同源历史稿显示 AEWIN 属 Qisda Group，**本稿未提 Qisda**）。
四项技术原文一句列举：`an Intelligent CDU featuring pressure regulation and vapor-liquid separation design for dynamic
management; Next-Generation Two-Phase Cold Plates with optimized microstructures to enhance cooling efficiency;
High-Reliability Manifolds utilizes industrial-grade stainless steel and tuned flow guidance to enable consistent
refrigerant distribution; and Dry-Break Quick Release Connectors that help keep zero leakage and contamination during maintenance.`
⚠️ 歧管原文为「**工业级**不锈钢」；干断快接是「有助于保持零泄漏」的**定性宣称，不是实测泄漏率**。
两相原理原文：`uses a low-boiling-point coolant and phase-change mechanism to enhance heat transfer`。
CTO **C.E Liu** 引语中的 `reduced PUE` 为**定性，稿中未给任何 PUE 数值**。
**未披露**：冷却剂牌号/沸点、PUE 值、单芯片 TDP 上限、热流密度、CDU 容量、ATD、流量压降、上市时间与价格、客户部署、
200 kW 在何种进液温度/环境下达成。

### C3 · ZTE —— **通过（PUE 1.15 归属必须改写）**
**Nov 16, 2026 05:33 ET**；dateline `SHENZHEN, China, Nov. 16, 2026` 一致。
**CDU 数字全部核实**：
> `The CDU has a single-unit cooling capacity of 1.5 MW, expandable to 2.4 MW, with flexible configuration of 2–5 CDU cabinets.`
> `the 1500 kW liquid cooling CDU achieves precise temperature control of ±0.5°C and pressure control of ±0.05 bar`
±0.5 °C / ±0.05 bar **明确归属于 1500 kW 冷板液冷 CDU 本身**（全稿中唯一真正属于 CDU 的性能指标）。
另有未在候选中的 CDU 特性：`N+X redundant hot backup`、双路供电、7×24 不间断、健康指标与状态可视化。

🔴 **PUE 1.15 的真实归属 —— 稿中有两处不同的 1.15，候选把它们混成了一句**
- **第一处（通用方案级）**：`The combination of 800V high-voltage DC and the 1500 kW liquid cooling CDU outlines an
  efficient "inbound" and "outbound" channel for AIDC: … keeping PUE stably within 1.15.`
  → 归属 = **800 V HVDC + 1500 kW 液冷 CDU 的组合，不含 32 °C 送风**
- **第二处（具体案例级）**：`The Nanjing Binjiang Data Center … implemented a liquid-cooling integrated solution with a
  power density of up to 60 kW, adopting high-efficiency HVDC power distribution and busway, 32°C air supply, and group
  control optimization, achieving a PUE of only 1.15.`
  → 归属 = **南京滨江数据中心改造案例**（60 kW 功率密度，HVDC + 母线槽 + 32 °C 送风 + 群控优化）
**→ 成稿必须二选一或分开写，且无论哪一处都不能写成 CDU 单体指标。**
**Karakoram-01 核实**：`Karakoram-01, Pakistan's first and largest purpose-built, AI-ready data center campus … adopts
technologies such as cold plate liquid cooling, prefabricated power modules, and smart busway`
⚠️ 冷板液冷**仅为 `adopts technologies such as` 的列举之一**，稿中**未给**该项目的容量、PUE、机架密度、液冷覆盖比例、投产时间。
**归属**：整篇为 ZTE 自述的宣传/观点稿，非第三方评测。
**未披露**：CDU 的 ATD、流量、进出水温、换热形式、上市时间、价格、1.15 的测算边界与气候区、南京滨江液冷/风冷占比、
Karakoram-01 规模与冷板供应商、±0.5 °C 在何种负载与流量下达成。

### C4 · Aviemore Motion Technologies —— **通过**
**Nov 16, 2026 12:00 ET**；dateline `CHICAGO, Nov. 16, 2026` 一致。
规格全部核实（厂商宣称）：`The platform covers 0.10 to 5.0 kW of output across a 12 to 800 V DC bus range.`；
`Rack CDU Pumps: 0.10 to 2.0 kW, 12 to 800 V DC`；
候选漏掉的一行：`Row and Facility Pumps: 1.0 to 5.0 kW, 12 to 800 V DC, AC and DC drive, for row CDUs, coolant skids, and facility loops`
🔴 **140 kW / 240 kW / 600 kW–MW / 800 VDC Q2 2027 确认为「行业背景叙述」，不是该公司产品承诺**。原文：
> `AI racks draw 140 kW today. Racks of 240 kW are close behind and 600 kW to megawatt-class racks are in future
> planning. Power inside the rack is also moving from 54 VDC to 800 VDC, with the first commercial systems expected to
> ship in Q2 2027. … Aviemore built its platform for that paradigm shift.`
→ 这四句**全是 Aviemore 对行业走势的无出处断言**。「800 VDC 首批商用系统 2027 Q2 出货」指的是
**机架内 800 VDC 供电的行业首批商用系统，不是 Aviemore 泵的出货时间**。
**稿中完全没有给 Aviemore 自家泵的上市/出货时间。**
其他（厂商宣称）：团队共事 25+ 年；无槽电机已出货 `more than 15,000 motors with zero motor defects`
（⚠️ 这是其**无槽电机整体历史，不是本次这批泵**）；设计泵 20 年；**156,000 平方英尺** Radford, Virginia 工厂；
ISO 9001；`UL and Intertek certifiable on request`（**可认证，非已认证**）；`patent-pending`（**申请中，非已授权**）；
`The pumps can run dry during commissioning or a loss of prime`（定性，无时长）。
**未披露**：流量、扬程/压差、效率、转速、MTBF/寿命、噪声、湿端材料、兼容冷却液清单、价格、交期、自家泵出货时间、
任何客户/认证机构实测数据、专利号。

### C5 · MES, Inc. 冷板平面度与粗糙度指引 —— **通过（须标为「加工商工程指引、零实测数据」）**
**Nov 18, 2026 11:29 ET**；dateline `COLUMBUS, Ohio, Nov. 18, 2026`。
⚠️ 小矛盾：dateline 写 COLUMBUS, Ohio，但 About 段写 `Headquartered in Lewis Center, Ohio` → **写总部请用 Lewis Center**。
全部核实：
- `Holding 0.025 mm across a 30 mm die works out to 1 part in 1,200.` ✅
- `Across a 70 mm die, the same tolerance is 1 part in 2,800` ✅
- **换算校验**：0.025/30 = 1/1200.0 ✓；0.025/70 = 1/2800.0 ✓ → **确为纯几何换算，两数精确对得上**
- `TIM typically forms a layer 25 to 75 microns thick and conducts a few W/m•K, compared with about 388 W/m•K for copper.` ✅
- `A plate dished 0.040 mm can add up to 40 microns of TIM locally` ✅ 原文用 **dished（碟形）**、**can add up to（最多可增加）**，上限式非典型值
- `describes 0.4 to 0.8 µm Ra as a useful working range for many contact faces, depending on the TIM and contact
  pressure, and suggests specifying both Ra and Rz on critical die interfaces` ✅ ⚠️ 带两重限定 + 建议同时标 Ra 与 Rz
- `Moving a callout from 0.025 mm to 0.015 mm can shift the contact face from precision CNC machining to grinding or
  dedicated fly cutting, adding setup, fixturing and inspection costs.` ✅
**候选漏掉、建议补的一手数字**：
🟢 **钎焊态平面度 0.100–0.250 mm**：`As-brazed flatness commonly runs 0.100 to 0.250 mm because a vacuum braze cycle
can relieve residual stress and change the shape of the base.` 并建议 `machining the mounting face after brazing`
并把工序写成图纸工艺注记 —— **本稿最有工程价值的一条，候选没列**。
MES 推荐规格：`identifies 0.025 mm across the die contact footprint as a good working specification for most
direct-to-chip applications, with the final tolerance set by the thermal model`。
🔴 **关键定性判断**
1. **稿中完全没有任何实测/测试数据**：零实验、零测试件、零热阻/ΔT/W·cm⁻² 测量、零样本量、零对照组。
   唯一「验证」措辞是 `parts are verified by CMM at the source`（来料尺寸检验，**不是热性能测试**）。
2. **两类数字必须分开写**：
   - **通用工程换算/公开材料常数**：1/1,200 与 1/2,800、铜 ≈388 W/(m·K)、TIM 25–75 µm 与 `a few W/m·K`、钎焊态 0.100–0.250 mm
   - **MES 自己的推荐规格/判断**：0.025 mm 作为多数 direct-to-chip 应用的 `good working specification`、
     Ra 0.4–0.8 µm、同时标 Ra+Rz、焊后加工并写入工艺注记、0.015 mm 会导致工艺跃迁
   - **上限式估算**：0.040 mm 碟形 → 局部「最多」多 40 µm TIM（无推导、无测量）
3. **须标明**：MES 是**制造采购/供应链公司**（`manufacturing sourcing and supply chain company`），不是冷板设计方也不是实验室；
   本稿是**工程指引 + 营销稿**。两位发言人 Hiten Shah（President & CEO）、Brad Layne（Engineering Manager）均强调 `start with the thermal model`。
4. ⚠️ **标题陷阱**：稿末博客 URL 为 `.../why-a-tighter-flatness-spec-can-double-cold-plate-cost/`（「可使成本翻倍」），
   但**PRN 正文从未给出任何成本倍数或百分比**，只说 `Cost rises in steps` → **严禁从 URL 推出「成本翻倍」**。
**未披露**：成本倍数/金额、五种工艺的具体对比表（在稿外 blog）、TIM 牌号、接触压力数值、适用芯片/封装型号、客户名、Rz 推荐值。

### D · Nexalus × Renda Nova8 —— **待确认**
✅ DCD 稿件页 `https://www.datacenterdynamics.com/en/news/nexalus-and-renda-launch-liquid-cooled-ai-server-for-data-center-retrofit-market/`
  **November 20, 2026 / By Matthew Gooding**，副题 `Features eight Nvidia Blackwell GPUs`
❌ PRN 搜 `Nexalus` **No Results Found**；`www.nexalus.com` / `nexalus.com` / `www.renda.com` / `renda.tech` 均 403
→ **一手未取到**。DCD 明确称存在 `a statement from Nexalus and Renda`，但该联合声明原文不可达。

| 候选项 | DCD 原文 | 判定 |
|---|---|---|
| 4U | `is engineered as a single 4U server, with integrated CPUs, memory, storage, power, and cooling` | **核实（据 DCD）** |
| **8 颗 96 GB RTX PRO 6000 Blackwell** | DCD 只写 `built around eight Nvidia Blackwell GPUs` | **🔴 不符/稿中未给**。DCD **从未出现 "RTX PRO 6000" 或 "96 GB"** → **必须删**，或写「八颗 Nvidia Blackwell GPU（DCD 未给型号与显存）」 |
| 射流冲击冷板 | `Nexalus's jet cooling technology, which sees coolant squirted onto the liquid cooling cold plate, rather than running through channels` | **核实（据 DCD）**。用词为 `jet cooling technology`，**未用 "jet impingement"** |
| 单 4U 内冷却 CPU + 8 GPU 满功率 | `According to Nexalus, this enables the CPU and eight GPUs at full power to be cooled within a single 4U chassis` | **核实，厂商宣称** |
| **液对气换热器 / 排热到室内空气** | **🔴 DCD 稿中完全没有这句**。DCD 只写 `It fits a standard 19-inch rack in an existing air-cooled data center`，`operators can swap it in for current equipment without adding new piping or cooling infrastructure` | **核不到 → 严禁入稿**。只能写 DCD 原话 |
| 吞吐最高 +20% | `with up to 20 percent more AI token throughput` | **核实，厂商宣称**。⚠️ 原文是 **AI token 吞吐**，不是泛指「吞吐」 |
| 能效最高 +22% | `It says it can offer a 22 percent boost to energy efficiency when compared to a similar setup that is air-cooled` | **核实，厂商宣称** |

🔴 **基线**：+22% 基线**已核到** = `a similar setup that is air-cooled`；
**+20% AI token 吞吐 DCD 未单独给出基线**（`compared to…` 从句语法上只挂在 22% 那一项）。
→ 22% 标注「厂商宣称，相对一套类似配置的风冷方案（据 DCD）」；**20% 只能标注「厂商宣称，DCD 未就该项单独给出基线」**。
两项都是 `up to（最高）`，不是典型值。
其他（据 DCD）：Nexalus 总部 **Cork, Ireland**；Renda 位于 **UK**；Nexalus CEO **Kenneth O'Mahony**；
Renda 方 **Ian "8Pack" Parry**；两家称 F1 经验用于 Nova8 开发；Nexalus 已与 **HPE** 合作、HPE 在其系统中采用 Nexalus 液冷技术。
⚠️ DCD 自身用词不一致：导语称 `a new liquid-cooled rack`，下文又明确是 `a single 4U server` → **按「4U 服务器」写**。

### E1 · MarketsandMarkets 数据中心漏液检测系统市场 —— **通过（口径须加限定）**
一手稿件页已读正文（非搜索片段）。**Nov 17, 2026 10:01 ET**；dateline `DELRAY BEACH, Fla., Nov. 17, 2026` 一致。
> `the Data Center Leak Detection Systems Market is projected to grow from USD 0.63 billion in 2026 to USD 1.07
> billion by 2031, at a CAGR of 11.3% during the forecast period.`
口径 = **市场规模预测** ✅；**基年已给** ✅（2025 = USD 0.58 bn；2026 = USD 0.63 bn；2031 = USD 1.07 bn）；
**CAGR 11.3%（2026–2031）** ✅；预测区间 2026–2031（历史回溯至 2021）。
🔴 **是否限定在液冷场景？—— 否，明确不限定，必须加限定说明**：
> `leaks from chilled water pipes, condensate lines, cooling distribution units, and coolant circulation systems`
> `both conventional air-cooled facilities with water-based cooling infrastructure and facilities adopting liquid cooling`
→ 液冷是**增长驱动因素之一，不是市场边界**。
**成稿必须写明：该数字覆盖风冷设施的水系统 + 液冷设施，不可当作「液冷漏液检测市场」引用。**
**未披露**：地区/细分的 2031 绝对值、报告价格、方法论、**1.07 bn 中液冷相关占比（本刊最想要的拆分，稿中没有）**。

### E2 · Frost & Sullivan 全球 HVAC 设备市场 US$383.6 bn —— **建议否决（不该进本刊）**
一手 URL 已找到并读取；**Nov 20, 2026 09:21 ET**；dateline `LONDON, Nov. 20, 2026`。
数字核实：`projected to reach $383.6 billion by 2031, expanding at a CAGR of 7.0% from 2025`（*Frost Radar™: HVAC Equipment, 2026*）
⚠️ **基年 2025 的绝对值稿中未给**。
🔴 否决理由：① 标的是**全球 HVAC 设备市场**（建筑暖通：热泵、低 GWP 制冷剂、建筑电气化、区域供冷、IoT 楼控）；
② **全文零次出现 liquid cooling / cold plate / direct-to-chip / immersion / CDU / PUE**（逐字读完 5,777 字符确认）；
③「数据中心冷却」仅为三个**定性**增长机会之一，**无任何数据中心细分的规模、占比或 CAGR**；
④ 与本刊液冷/冷板数字**量级差 2–3 个数量级且口径完全不同，并列必然误导**；
⑤ 实质是 Frost Radar™ 榜单推广（10 家入选全为传统暖通巨头，**无一家液冷/冷板专业厂商**）。
→ **整条否决，不入「前瞻分析」节，也不入正文。**

## 产业侧汇总判定
| 条目 | 判定 | 一手？ | 精确 ET / dateline |
|---|---|---|---|
| A CoolIT × Ecolab CHx 3000 | **待确认** | 规格有一手产品页；新闻稿一手不可达 | CoolIT 新闻页 2026-11-16 13:06 ET；DCD 2026-11-18 |
| B-1 ZutaCore × Munters Z₂O | **否决** | 无 | — |
| B-2 MiTAC × ZutaCore PoC | **通过** | 是（PRN） | Nov 16 22:15 ET / CHICAGO, Nov. 16 ✓ |
| C1 Solenis × Vertiv | **通过** | 是 | Nov 19 08:00 ET / WILMINGTON, Del. ✓ |
| C2 Arivor（AEWIN 子公司） | **通过** | 是 | Nov 17 08:00 ET / CHICAGO ✓ |
| C3 ZTE | **通过**（PUE 归属须改写） | 是 | Nov 16 05:33 ET / SHENZHEN ✓ |
| C4 Aviemore | **通过** | 是 | Nov 16 12:00 ET / CHICAGO ✓ |
| C5 MES, Inc. | **通过**（须标零实测） | 是 | Nov 18 11:29 ET / COLUMBUS, Ohio ✓ |
| D Nexalus × Renda Nova8 | **待确认** | 无（仅 DCD） | DCD 2026-11-20, Matthew Gooding |
| E1 MarketsandMarkets 漏液检测 | **通过**（加口径限定） | 是 | Nov 17 10:01 ET / DELRAY BEACH, Fla. ✓ |
| E2 Frost & Sullivan HVAC | **建议否决** | 是（口径不合本刊） | Nov 20 09:21 ET / LONDON ✓ |

**所有 PRN 条目的列表时间戳与稿内 dateline 均一致，本期无上期那类时间戳冲突。**

**成稿前必须落实的 6 条**
1. A：删「45 °C 暖水」「双换热器」；改为「IP54，最高 45 °C 环境空气（同页另处写 50 °C）」。不引 DCD 的 37.4 °F。
2. A：Q1 2027 发货、Alfa Laval、3D TRASAR 七参数 → 标「据 DCD」。
3. B-1 整条删除（含 pPUE 1.03、WUE 0、625 kW、74%、ASRock HGX B300、2027 上市）。
4. C3：PUE 1.15 按两处分开写，均不得写成 CDU 单体指标。
5. C5：标明「制造采购公司的工程指引稿，无任何实测数据」；不得出现「成本翻倍」。
6. D：删 RTX PRO 6000 / 96 GB 与「液对气换热器」；20% 写成「AI token 吞吐」且注明「DCD 未单独给基线」，
   22% 注明基线为「类似配置的风冷方案」。

**失败通道（供下期更新通道表）**：`www.businesswire.com`、`zutacore.com` / `www.zutacore.com`、`www.munters.com`、
`www.nexalus.com` / `nexalus.com`、`www.renda.com`、`renda.tech`、`www.globenewswire.com`、`www.ecolab.com`、
`investor.ecolab.com`、`www.stocktitan.net`、`coolitsystems.com`（**无 www 403，带 www 正常**）—— 均 `Tunnel connection failed: 403`。
**新增可用通道**：✅ `www.coolitsystems.com`（含 `/sitemap_index.xml`、`/cdu-product-sitemap.xml`，有一手产品规格页，价值高）；
✅ PRN 稿页原始 HTML 中 `grep -oE '[0-9]{1,2}:[0-9]{2} ET|datePublished'` 可直接取精确 ET 时间戳，比搜索页更可靠；
✅ 用 `python3 -I` + 与 fetch_source 相同 UA 直取 DCD 列表页 HTML 可提取 slug（curl 仍撞 Cloudflare）。
