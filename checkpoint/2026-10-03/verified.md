# verified.md · 第 8 期逐位核验（学术部分）

## 取证环境（影响所有判定）
出口代理 403 拦截几乎所有出版商站点：sciencedirect.com、linkinghub.elsevier.com、papers.ssrn.com、
ieeexplore.ieee.org、pubs.aip.org、jffhmt.avestia.com、doaj.org、api.semanticscholar.org。
Crossref **单条 works 路由不支持 `select`**（返 400）；要用 select 必须走列表路由
`https://api.crossref.org/works?filter=doi:<DOI>&select=...`。

证据分三档：
- **A 档**：Crossref `/works/<DOI>` 的 abstract/author/affiliation —— 出版商自己 deposit，可当原文用。
- **B 档**：OpenAlex `abstract_inverted_index` 重建摘要 / `raw_affiliation_strings` —— **成稿必须注明来源与「未直读出版商页面」**。
- **C 档**：取不到 → 待确认 / 不可用，不猜。

---

## 【通过·可写论文卡】1 · 鲨鱼皮仿生翅片微通道热沉（A 档）
DOI 10.1063/5.0347413 · *Physics of Fluids* **Vol. 38, Iss. 10, 文章号 105103**
created 2026-10-01T08:35:06Z；published-online 2026-10-01；published-print 2026-10-01 → **窗口内，已正式刊出（非 in press）**

**7 位作者、5 家机构（Crossref 出版商自存 affiliation，逐位）**：
1. **Ge Gao**（第一）— 北京航空航天大学杭州国际创新研究院（Hangzhou International Innovation Institute, Beihang University, Hangzhou 311115）＋ 北航航空科学与工程学院（Beijing 100191）
2. **Guangze Li** — 北航杭州国际创新研究院 ＋ **天目山实验室**（Tianmushan Laboratory, 杭州余杭区 311115）
3. **Yuhui Wang** — 北航杭州国际创新研究院
4. **Liuyong Chang** — 北航杭州国际创新研究院 ＋ 天目山实验室
5. **Longfei Chen** — 北航杭州国际创新研究院 ＋ 天目山实验室
6. **Feng Han** — **南京航空航天大学 能源与动力学院**（Nanjing 210016）
7. **Pedro David Bravo-Mosquera** — **圣保罗大学圣卡洛斯工程学院 航空工程系**（University of São Paulo, São Carlos 13566-590，**巴西**）
> 纠 scout 两处：scout 漏了第 5 家机构（圣保罗大学）与第 7 位作者；"Hangzhou International Innovation Institute" 原文带 "Beihang University" 后缀，是北航杭州国际创新研究院，**不可拆开写成独立机构**。
> **通讯作者待确认**（Crossref 无 corresponding 标记，AIP 页 403）。

**数字（逐字出自 Crossref abstract）**：
- 流动阻力相对**同体积矩形翅片**基准，在**所考察的全部 Re 范围内**一致降低 **26–35%**（限定：**5 mm 与 8 mm 两种翅片构型**）
- **Re 超过约 2130** 时换热效率开始上升，最大增强 **16%**
- 相对矩形翅片 **PEC 峰值 31%**（原文 "rises to a peak value of 31%"）
- 机理：渐缩尾缘产生纵向涡，表现为典型 **Görtler 型二次流**；交错布置出现 **U 形温度梯度**
- 方法：**全尺寸 MCHS 湍流高保真数值仿真，realizable k–ε**

**待确认（不得补写）**：① Re 考察区间具体数值未给（只有 "Re>约 2130" 一个点）；② **工质未给**；
③ 热流密度、基准热阻、绝对温度值均无；④ "PEC 峰值 31%" 原文措辞含歧义（PEC 通常是无量纲比值而非百分比），
**按原文措辞原样引用**；⑤ **纯数值，摘要未提任何实验验证**；⑥ 通讯作者待确认。
证据：`https://api.crossref.org/works/10.1063/5.0347413`（AIP 自存）。pubs.aip.org 403。

---

## 【通过·可写论文卡】2 · 系统压力对两相 D2C 针肋冷板热阻与泵功的影响（A 档）
DOI 10.2139/ssrn.7536705 · Crossref `type = posted-content`，无 container-title / 无卷期页码
→ **SSRN 预印本，未经同行评审**。created 2026-09-28T13:47:12Z → **窗口内**

**作者**：Wookyoung Kim（第一）/ Kyeonghui Hong / Jinsub Kim / Kong Hoon Lee
**单位仅核到 2/4（B 档）**：Kyeonghui Hong — **University of Science and Technology (UST), Korea**；
Jinsub Kim — **韩国机械与材料研究院 KIMM**。
> **Wookyoung Kim 与 Kong Hoon Lee 单位取不到 → 待确认。不得因 KIMM/UST 就把第一作者与末位作者也写成 KIMM。**

**数字（逐字出自 Crossref abstract，实验测量）**：
- 工质 **R1233zd(E) / R1234ze(E) / R1234yf**（低 GWP）；**铜冷板，加热足迹 25.4 × 25.4 mm**；过冷流动沸腾
- 手段：**高速摄影 + 测温**（实验，非仿真）；入口温度 **40 °C**；系统压力与过冷度用储液器调节
- 输入功率 **45 W ~ 标称 1 kW**；质量流量 **0.152 ~ 2.235 kg/min**；过冷度 **1.8 ~ 39.9 K**
- 现象：即使出口按平衡含气率判为单相液的工况也已发生核态沸腾
- **标称 1 kW 下三种工质热阻均随过冷度增大而上升（定性）**；热阻分解后随约化压力升高对流项下降、部分抵消过冷项上升
- **COP（输入功率/泵功）在 1.0 kg/min 下随过冷度约以 5 ~ 7 %/K 上升**
- 提出**无拟合常数**简化热阻模型，**标称 1 kW 下预测实验热阻在 ±11% 内**；模型与实验一致显示饱和压力更高的工质热阻更低
- 对 **3 kW 微通道冷板模型、芯片温度上限 85 °C**，允许过冷度估为 **约 19 ~ 27 K**（随工质不同）

> **纠 scout**：摘要里**没有绝对热阻值（K/W）、也没有绝对泵功值（W）**。1 kW 下结论是定性方向性的；
> 定量只有 COP 的 **5–7 %/K** 与模型精度 **±11%**。**成稿不得凭空给 K/W 数字。**

**待确认**：① Wookyoung Kim、Kong Hoon Lee 单位；② 绝对热阻/泵功数值；③ 过冷度与压力的具体 range 对应；④ 是否已投期刊。
证据：`https://api.crossref.org/works/10.2139/ssrn.7536705`；`https://api.openalex.org/works/doi:10.2139/ssrn.7536705`。papers.ssrn.com 403。

---

## 【通过·可写论文卡】3 · 嵌入式 HU 型歧管 micro-pin-fin 热沉（摘要 B 档）
DOI 10.1016/j.ijheatmasstransfer.2026.129613 · IJHMT **Vol. 273, 文章号 129613**，PII S0017931026012895
created 2026-09-28T10:31:05Z → **窗口内**；published-print 2027-02 → **在线先行，纸刊排到 2027-02**

**作者/单位（OpenAlex raw_affiliation；Crossref affiliation 全空）**：
- **Zhiyao Jiang**（第一）— **北京大学 工学院力学与工程科学系**（Beijing 100871）＋ **微纳加工技术国家级重点实验室**
- **Wei Xiao** — 同上两家
- **Weiheng Li** — 北京大学力学与工程科学系
- **Bai Song** — 同第一作者两家
> 通讯作者取不到 → 待确认。**末位 Bai Song 可能是通讯但无出处，不要写。**

**数字（B 档，OpenAlex 重建摘要）**：
- 背景：芯片功率密度推动热流**超过 1 kW/cm²**
- 对象：**嵌入式 HU 型歧管 micro-pin-fin（MPF）热沉**，**三维数值研究**，分层三模型策略
- 趋势：增大 MPF 直径 → ΔT_max 下降、ΔP 上升；**固定 H_cav 时增大翅高 H_f 会压缩顶部间隙、抑制旁通泄漏、显著强化换热**
- 横向/纵向间距存在**非对称交叉耦合**；间距过大时流动绕流走低阻通道 + 尾迹，换热严重恶化
- **关键数字：热流 2000 W/cm² 下，菱形（diamond）截面 MPF 同时取得 ΔT_max = 56 K、ΔP = 28 kPa、COP > 2000**，
  **在热与流两方面同时优于常规微通道（MC）基准**
- 基准口径明确：常规微通道 MC 基线，以及同族 in-line / staggered 圆形 MPF 阵列

**待确认**：① 通讯作者；② **摘要与数字未能在 ScienceDirect 直读复核（403），成稿须注明来源为 OpenAlex**；
③ COP 定义式未给（**不要自行解释**）；④ 工质、泵功绝对值、MPF 具体尺寸区间未取到；⑤ 纯数值，摘要未提实验验证。
证据：`https://api.crossref.org/works/10.1016/j.ijheatmasstransfer.2026.129613`；`https://api.openalex.org/works/doi:10.1016/j.ijheatmasstransfer.2026.129613`。

---

## 【通过·可写论文卡】7 · 场协同+㶲耗散+熵产三位一体的微通道拓扑优化（摘要 B 档）
DOI 10.1016/j.applthermaleng.2026.133471 · ATE **Vol. 308, 文章号 133471**
created 2026-09-30T21:04:46Z → **窗口内**；published-print 2026-11

**查重结论（明确）**：与第 6 期已报 10.1016/j.energy.2026.142364（作者仅 2 人 **Zixu Han、Peng Zhang**，上海交大）
**作者零重合、机构零重合**；本文框架是 **场协同 + 㶲(entransy)耗散 + 熵产 三位一体评价**、对象是**微通道**，
142364 是 **场协同 + 分形几何**、对象是**液冷板**。→ **两项独立工作，既非同一工作、也无证据表明是同组后续。**

**作者/单位（OpenAlex raw_affiliation；Crossref affiliation 全空）—— 产学合作**：
1. **Yuwei Liu**（第一）— **中国矿业大学（北京）机电与信息工程学院**（Beijing 100083）
2. **Jintao Liu** — 同上
3. **Jinghui Liang** — **北京海纳川汽车部件股份有限公司**（Beijing 100176）
4. **Wenwei Jiang** — 中国矿业大学（北京）
5. **Yuanzhi Sun** — 中国矿业大学（北京）
6. **Changhui Chen** — **北汽动力总成有限公司**（Beijing 101100）

**数字（B 档，逐字）**：
- 双目标（强化换热 + 降低流阻）流-热拓扑优化模型，据 **Pareto 前沿 + 综合热工水力评价**选出 **TOMC** 构型
- 两个基准：**CSMC**（conventional straight microchannel 常规直微通道）与 **PSMC**（原文写作 pin-fin microchannel，缩写与词组不匹配，**原样引用并注「原文如此」**）
- **在所考察的最高 Reynolds 数下**：TOMC 压降相对 CSMC **−31.54%**、相对 PSMC **−30.09%**；
  最高温升相对 CSMC **−40.48%**、相对 PSMC **−17.72%**
- 验证：**三维共轭传热仿真 + 实验验证**（原文 "...and experimental validation are conducted"）→ **有实验验证**
- 机理：改善内部流量分配与**速度场-温度梯度场空间协同**，降低传热能力耗散与总熵产，总熵产以热贡献为主导

**待确认**：① **「最高 Reynolds 数」具体数值未给 —— 成稿必须保留「在所考察的最高 Re 下」这个限定词，不得省略**；
② 通讯作者；③ 工质、热流密度、绝对温度/压降值未取到；④ 摘要未在 ScienceDirect 直读复核，须标注来源。
证据：`https://api.crossref.org/works/10.1016/j.applthermaleng.2026.133471`；`https://api.openalex.org/works/doi:10.1016/j.applthermaleng.2026.133471`。

---

## 【待确认·只能进其他线索，零性能数字不得写卡】

### 4 · 3D 堆叠 IC 冷板 + 侧歧管混合冷却（IEEE TCPMT 早期访问）
DOI 10.1109/tcpmt.2026.3739728；created 2026-10-02T19:05:03Z → 窗口内
Crossref `page = "1-1"`、无卷无期、published-print 2026（仅年）→ **Early Access 确认成立**
作者/单位（Crossref，IEEE 自存，三位全部裸串 **Binghamton University**，scout 无误）：
**Chukwudi Azubuike**（第一）/ **Mohammad Tradat** / **Bahgat Sammakia**
> ⚠ OpenAlex 把第一作者记作 "**Chima** Azubuike"、第二作者 "Mohammad **I.** Tradat"。
> **以 IEEE 自存的 Crossref 为准写 Chukwudi Azubuike**；若用全名有顾虑可写 "C. Azubuike"。
**数字：零。** Crossref 无 abstract；OpenAlex abstract = none；IEEE Xplore 403。

### 5 · 径向歧管微通道热沉多目标拓扑设计（*Energy*）
DOI 10.1016/j.energy.2026.142527；文章号 142527；created 2026-10-02T15:24:46Z → 窗口内；published-print 2026-10
**查重：与第 6 期 142364 作者零重合、机构零重合、标题与对象不同 → 确认两项完全独立的工作。**
作者/单位（OpenAlex）：
1. **Hanwei Lv**（第一）— **长安大学** 汽车与电气工程学院 ＋ 陕西省交通新能源开发应用及汽车节能重点实验室（Xi'an 710018）
2. **Yasong Sun** — **同济大学**（上海地面交通工具空气动力与热环境模拟重点实验室，201804）＋ 西安先进交通动力重点实验室（长安大学）
3. **Zican Lin** / 4. **Xiaolong Chang** / 5. **Huquan Cao** — 长安大学（同 1）
6. **Yifan Wang** — **西安交通大学 能源与动力工程学院**（710049）
7. **Jing Ma** — 长安大学 汽车学院
**数字：零。**

### 6 · 非均匀高热流下嵌入式针肋微通道芯片冷却结构优化（ICHMT）
DOI 10.1016/j.icheatmasstransfer.2026.112696；ICHMT **Vol. 180, 文章号 112696**
created 2026-09-28T13:11:51Z → 窗口内；published-print 2026-11
作者（Crossref）：**Yangyu Deng**（第一）/ **Fei Xin** / **Qiang Lyu**
**单位：无（Crossref 空、OpenAlex raw_affiliation_strings = []）→ 一律待确认，坚决不猜。数字：零。**

### 13 · 超临界 CO₂ 蛇形微通道高热流电子冷却（*J. Supercritical Fluids*）
DOI 10.1016/j.supflu.2026.107166；文章号 107166，无卷期；created 2026-10-02T15:25:50Z → 窗口内；published-print 2026-10
作者/单位（OpenAlex，**本期 P4 唯一核全单位的一条**）：
1. **Saravana Kumar Tamilarasan**（第一）— **Vellore Institute of Technology (VIT) 机械工程学院，印度泰米尔纳德邦 Vellore 632014**
2. **Parthasarathy Rajesh Kanna** — 同上
相关性：标题**明确写 "for High Heat Flux Electronics"** → 主题相关性成立；但工质是**超临界 CO₂**、构型为蛇形微通道，
距本刊主线（数据中心 D2C 水/两相冷板）较远，属**方向性参考**。**数字：零。**

---

## 【否决】

### 9 · Advances in Direct-to-Chip Liquid Cooling Integration（ECTC 2026, Adeia）—— 否决：窗口外
依据四条互相印证：
1. **Crossref 自身发表日就是 5 月**：`published-print = [[2026,5]]`、`issued = [[2026,5]]`。
   `created = 2026-10-01T19:17:30Z`、`deposited = 2026-10-02T05:27:07Z` —— 这是 **DOI 登记/存档日，不是发表日**。
   本条**无 `published-online` 字段**，故「用 created/published-online 判窗」在此无可用 online 日期，只能看 issued。
2. **同论文集姊妹篇早在 6 月登记**：10.1109/ectc51846.2026.00092（第 7 期已报 TSMC）created = 2026-06-17、
   published-print = [[2026,5,26]]。同集内 created 相差近 4 个月 → **created 在此只反映 IEEE 分批补登节奏**。
3. **官方论文集 PDF 首页原文**（已下载，200 OK）：
   "2026 IEEE 76th Electronic Components and Technology Conference (ECTC 2026) / Orlando, Florida, USA / **26-29 May 2026**"。
4. **第 7 期已就 ECTC 2026 作出同样定性并写入正刊**（2026-09-26.md:29）。本期若按窗口内收录将与第 7 期口径自相矛盾。
**附带发现（元数据质量）**：Crossref 给本条页码 **579–584**，但官方目录里 579–584 页是
"Diamond-on-Chip Integration..."（Zeming Tao 等，579 页）与 "Low Warpage Double Side RDL..."（584 页）；
整份目录（至 2570 页）**grep 不到本标题**，也 grep 不到 Mirkarimi 的冷却类论文（Adeia 的 Laura Mirkarimi 只出现在
1327 页 "Reworkable Die-to-Wafer Hybrid Bonding Process"）。→ **页码与官方目录冲突、论文不在 POD 目录，元数据不可靠。**
作者（留档）：L.W. Mirkarimi 等 8 位全部 Adeia。**数字：零。**
→ **本期不提。** 若要提只能作「窗口外补记」——而那会触发 rules 第 20 条 (c)。

### 10 · 液汽分离通路 + 射流冲击开放微通道（IJTS 111369）—— 否决：相关性无法证实 + 零数字
DOI 10.1016/j.ijthermalsci.2026.111369；created 2026-10-02T00:16:23Z；published-print 2027-02
作者：Yuming Guo / Yifei Li / Yong Qin / Liang Zhao。**单位：无。数字：零。**
**「对象是否芯片/电子」：无法证实** —— 标题只说 "for enhanced heat transfer"，**无 chip / electronics 字样**；
*Int. J. Thermal Sciences* 为通用传热刊；摘要取不到，无法判断热源是否为模拟芯片。

### 11 · 歧管微通道三角侧壁沟槽流动沸腾（JFFHMT / Avestia）—— 否决：刊物层级 + 零证据
DOI 10.11159/jffhmt.2026.029；Vol. 13, pp. 319–328；created 2026-10-02T13:15:32Z；**published-online = [[2026]]（仅到年）**
作者（Crossref）：Pengyang Jin / Haocheng Wang / Yong Ren。**单位：无。数字：零。**
> ⚠ OpenAlex 把第一作者渲染成中文 "朋央 金"（且姓名顺序颠倒），与 Crossref 不一致 → 元数据可靠性差。
**刊物层级判定**：*Journal of Fluid Flow, Heat and Mass Transfer*，ISSN 2368-6111，Avestia Publishing（加拿大）。
OpenAlex source：`is_oa = true`、**`is_in_doaj = false`**、works_count **244**、cited_by_count 478、
**h_index 8**、**2yr_mean_citedness 0.719**。→ 极小众低影响力 OA 小刊，通常承接 Avestia 自家会议扩展稿。
同行评审政策声明**无法核到**（官网与 DOAJ 均 403）→ **不能断言掠夺性，但也无可核证据支持其为正常严格同行评审**。
按本刊标准**不足以作论文卡的证据层级**。

### 12 · 新月形针肋 vs 光滑**小通道**热沉流动沸腾对比（ICHMT 112763）—— 否决：证据最薄，留待下期
DOI 10.1016/j.icheatmasstransfer.2026.112763；ICHMT Vol. 180, 文章号 112763
created 2026-10-03T10:16:59Z（**就是期号当日**）；published-print 2026-11
> **纠 scout 的关键词错误**：原文是 "**smooth minichannel** heat sinks"（**小通道 minichannel**），
> **不是「光滑微通道 microchannel」**。两者水力直径量级不同，是实质差别。
作者：Fadi Alnaimat / Abdul Hanan / Bobby Mathew。**单位：无**（Crossref 空，**OpenAlex 尚未收录该 DOI，404**）。**数字：零。**
**「是否实验」无法证实** —— "comparative study" 既可指实验也可指仿真，摘要取不到。**不要写成「实验对比」。**
→ 建议本期不收，**留到下期待元数据补全后再核（下期仍属首次报道，不违反去重）**。

---

## 【上期挂账结清】14 · MoE-PINN（10.1016/j.engappai.2026.115892）
**性能数字确认取不到。** 三路均走完：
- Crossref 列表路由 + `select=abstract`（HTTP 200、total-results 1）→ **返回 item 里根本没有 `abstract` 键**，
  即**不是截断问题，是 Elsevier 从未向 Crossref deposit 该文摘要**。
- OpenAlex → 已收录，**`abstract_inverted_index` 为空**。
- ScienceDirect → 403。

**本次新取到的作者单位（上期此处空缺，可用于补全）**：
1. **Xingpu Feng**（第一，ORCID 0009-0008-6817-3836）— **西交利物浦大学 School of Advanced Technology**（苏州工业园区仁爱路 111 号，215123）
2. **Yiming Liang** — 西交利物浦大学
3. **Sanli Liu** — 西交利物浦大学 ＋ **中国科学院沈阳自动化研究所**（沈阳 110169）
4. **Yuqi Liu** — 中科院沈阳自动化研究所
5. **Simon Maher** — **英国利物浦大学 电气工程与电子系**（Liverpool L69 3GJ）
6. **Min Chen**（ORCID 0000-0002-3122-6788）— 西交利物浦大学
→ 三方合作：西交利物浦大学 + 中科院沈阳自动化所 + 英国利物浦大学。
created = 2026-08-08T18:44:30Z、EAAI Vol. 182, 文章号 115892、published-print 2026-10 → **远在本期窗口外**，第 7 期已报，不作新条目。

---

## 主流程对 verifier 建议的处置（重要）
verifier 建议把「DOI→条目映射错误」写进本期「更正」节。**主流程已独立核查并驳回该建议**：
- 10.1016/j.applthermaleng.2025.126360 在仓库里**只出现在第 4 期**（2026-08-23.md:33、37），
  且第 4 期**正确地**把它挂在「分布式进出口射流冲击冷板（DIOJIC-CP）」卡上。
- 第 3 期「散热-流阻双目标」卡（2026-08-16.md:34-40）**本来就没有 DOI**，来源写的是 comsol.com/paper/147032、
  团队为肖飞/刘晓龙（南航）—— 也是**正确的**。
→ **已发布期次没有任何错误，对读者无更正可言。** 张冠李戴发生在主流程写给 scout 的 prompt 里，
属 agent 自身运行问题，按 rules 第 24 条**只进 PR 正文「流程备注」，不进周报正文、不写「更正」节**。
