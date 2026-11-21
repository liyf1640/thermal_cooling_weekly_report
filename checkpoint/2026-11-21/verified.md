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
