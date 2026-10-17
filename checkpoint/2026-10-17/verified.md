# 逐位核验结果（第 10 期）

## 批次 1 · 学术强相关（4 条）

**取证通道说明（对四条都适用）**：Crossref REST 与 Crossref unixsd XML（`/transform`，已对 112861 实抓验证）**均未交存 affiliation、通讯作者标注、abstract**——四条 Crossref 记录里 `abstract` 键不存在、`person_name` 节点只有 given/surname。因此**单位 / 通讯作者 / 摘要全部取自 OpenAlex**（`raw_affiliation_strings`、`is_corresponding`、`abstract_inverted_index`）。ScienceDirect 与 linkinghub.elsevier.com 经代理 403，出版商页与 PDF 读不到；Semantic Scholar API 同样 403。

### 1 · 10.1016/j.icheatmasstransfer.2026.112802 —— 通过（含 1 处单位更正、1 项待确认）
- **完整标题**（Crossref 与 OpenAlex 一致，**未截断、无副标题**）：`Zoned topology optimization of double-sided liquid-cooled microchannel heat sinks for the thermal management of SiC IGBT modules` → scout 的「标题疑被截断」**不成立**，成稿不要加保留语。
- **作者**：Hanyang Xu / Yifan Wang / Wenchao Tian / Feiyang Li / Han Shen / Daowei Wu（逐位一致）
- **原始机构串 → 裁剪**：
  - Xu / Wang / Tian / Shen：`School of Electro-Mechanical Engineering, Xidian University, Xi'an 710071, China`（Xu、Tian、Shen 另带国家重点实验室串）→ **西安电子科技大学 机电工程学院**
  - **Feiyang Li：只有** `State Key Laboratory of Electromechanical Integrated Manufacturing of High-Performance Electronic Equipments, Xidian University` → 裁掉实验室后只剩 **西安电子科技大学**（**无学院一级**）
  - **Daowei Wu：只有** `National Key Laboratory of Integrated Circuits and Microsystems, China` → **国家集成电路与微系统重点实验室**（原串无大学/学院层级，**不得自行补大学名**）
  - ⚠️ **与 scout 不符**：scout 称「前五位西安电子科技大学机电工程学院」，实为**四位**（Xu/Wang/Tian/Shen），Li 仅西安电子科技大学。
- **通讯作者**：**Daowei Wu**（OpenAlex `is_corresponding: true`，其余五位 false）
- **日期**：`created` 2026-10-13T15:58:57Z（✓ 窗内）；`published-online` **字段不存在**；`published-print` 2026-11（不作判窗依据）。ICHMT vol.180 文号 112802，已刊出期刊论文。
- **性质**：摘要原文 `Numerical simulations were performed in ANSYS FLUENT` —— **纯仿真**，摘要通篇无实验、无样机。
- **数字（全部命中摘要）**：
  - `a 114–187% improvement in the overall thermal performance factor` ✓ —— **基准 scout 漏写**：原文明确 `relative to the conventional straight-channel MCHS`，成稿必须带基准
  - `TOPO_20 ... reduces the average IGBT model temperature by 3.62 K` ✓
  - `the average SiC junction temperature by 6.41 K` ✓
  - `the peak thermomechanical stress within the module package by 72.76 MPa` ✓（**绝对值，不是百分比**）
  - **TOPO_20 含义**＝`featuring a 20 mm-wide high-temperature core region`（scout 未写，建议补）
- **「分区」具体是哪几区（已核到）**：每个设计域划三个功能区 `an inlet zone, a high-temperature design domain, and an outlet design domain`——入口区管流量分配均匀性、高温设计域以最大降温为首要目标、出口设计域平衡整体散热与泵功。模块**两面各集成一个 MCHS**（双面液冷）。
- **待确认**：① 是否**完全**无实验——摘要未提，正文读不到（403），成稿写「摘要口径为纯 ANSYS Fluent 仿真」而非断言全文无实验；② Daowei Wu 的大学/学院层级（元数据本身缺失）。

### 2 · 10.1016/j.applthermaleng.2026.133314 —— 通过（含单位补全、措辞更正、1 项待确认）
- **完整标题**：`Two-stage cGAN-ridge surrogate for battery cold plate topology design` ✓
- **作者（Crossref 交存串顺序）**：Puneeth D. Shetty / Akhil Garg / **Nguyen Phi Long**（given `Nguyen Phi` + family `Long`；OpenAlex 显示名 `Phi Long Nguyen`，**成稿用 Crossref 交存形式**）/ Hai Hung Pham / Jonghoon Kim / Kexiang Wei
- **原始机构串 → 裁剪**：
  - Shetty：`Department of Mechanical Engineering, National Institute of Technology Calicut, Kerala, India` → **National Institute of Technology Calicut 机械工程系**
  - Garg：`Department of Chemistry and Materials Science, Advanced Materials Research Center, School of Science, Xi'an Jiaotong-Liverpool University, Suzhou` → **西交利物浦大学 理学院**（⚠️ scout 漏了学院一级；系别是化学与材料科学系，**不是工程学院**）
  - Nguyen Phi Long：`Center for Environmental Intelligence and College of Engineering & Computer Science, Vin University, Hanoi City` + `School of Electrical and Electronic Engineering, Hanoi University of Industry` → **Vin University 工程与计算机科学学院** + **Hanoi University of Industry 电气电子工程学院**（原串写作两词 `Vin University`，**按原串**）
  - Pham：同 Vin University 串 → **Vin University 工程与计算机科学学院**
  - Jonghoon Kim：`Energy Storage and Conversion Laboratory, Department of Electrical Engineering, Chungnam National University, Daejeon` → **忠南大学 电气工程系**
  - Kexiang Wei：`Hunan Provincial Key Laboratory of Vehicle Power and Transmission System, Hunan Institute of Engineering, Xiangtan` → **湖南工程学院**（原串无学院一级）
- **通讯作者**：**两位** —— **Akhil Garg** 与 **Jonghoon Kim**
- **日期**：`created` 2026-10-12T12:07:50Z（✓ 窗内）；`published-online` 不存在；`published-print` 2026-11。ATE vol.308 文号 133314。
- **性质**：**纯计算**；摘要明确 `Full CFD verification remains required for final design selection`。无硬件实验。
- **数字**：
  - `It produces 256 × 256 fields in about 35 ms` ✓ —— 原文是 **"about 35 ms"（约）**，且**摘要未给硬件平台**，成稿须写「约 35 ms（摘要未说明硬件）」
  - `On 71 holdout cases ... topology IoU of 0.704 and a temperature SSIM of 0.692` ✓
  - `Connectivity holds in 57 of 71 cases` ✓；`mean pressure monotonicity is 66.9%` ✓
  - `Ridge gives R²=0.311–0.607 and Spearman ρ=0.761–0.830 for the three temperature targets` ✓
  - 压降原文 `It does not predict pressure drop reliably (R² = −0.009, ρ = 0.069)` —— 数字 ✓，但 **scout 的「预测失败」属加重表述**，改为「**不可靠**」；`Pressure drop is therefore excluded from the automated score and is checked by CFD`
  - `The workflow is designed to send only 2–3 of 20 candidates to CFD verification` ✓；作者自述 `This reduction target has not yet been validated against a full-CFD ranking of all 20 candidates` ✓ **必须保留**
  - 另核到应写进局限：主评估口径 `geometry-grouped five-fold cross-validation, repeated over three seeds`；`tree-based models are promising offline alternatives, but they have not been deployed in the workflow`；`The method is a constraint-penalised surrogate, not a PDE-residual model`
- **待确认**：35 ms 的硬件/批大小口径。

### 3 · 10.1016/j.icheatmasstransfer.2026.112881 —— 通过（含单位规则更正、1 项基准待确认）
- **完整标题**：`Numerical study on thermo-hydraulic performance of rib-interconnected microchannel heat sink` ✓
- **作者**：Xiuxian Zou / **Hui Deng** / Leyong Jiang / Wangbing Yu / Xiaohu Wu —— 第二作者出版商交存英文名就是 **Hui Deng**（OpenAlex 的 `邓晖` 是作者档案显示名，**成稿用 Hui Deng**）
- **原始机构串 → 裁剪**：
  - Zou / Deng / Jiang / Yu：`School of Physics and Electronics, Hunan Normal University, Changsha` → **湖南师范大学 物理与电子学院**
  - Xiaohu Wu：`School of Integrated Circuits, Hubei University, Wuhan` + `Thermal Science Research Center, Shandong Institute of Advanced Technology, Jinan` → **湖北大学 集成电路学院** + **山东高等技术研究院**
  - ⚠️ **与 scout 不符**：scout 把 **Yangtze Laboratory** 列为单位之一；按「只写到大学/学院、不写实验室」规则 **Yangtze Laboratory 不进成稿**（出现在 Zou、Deng、Wu 三人原串里，性质是实验室）
- **通讯作者**：**两位** —— **Wangbing Yu** 与 **Xiaohu Wu**
- **日期**：`created` 2026-10-16T13:25:48Z（✓ 窗内，本期最晚一条）；`published-online` 不存在；`published-print` 2026-11。ICHMT vol.180 文号 112881。
- **性质**：`Numerical simulations are conducted` —— **纯数值**，摘要无实验。Re `92–829` ✓
- **数字**（原文两句相邻）：`At Re = 829, case 8 with triangular ribs reduces the maximum substrate temperature by 12.65 K, increases the heat transfer coefficient by 129.36%, and reduces temperature non-uniformity by 65.80% compared with the conventional MCHS. Its PEC reaches 1.99, while the maximum heat flux capacity reaches 132.01 W/cm2, representing an increase of 122.20%.`
  - 最高基底温度降 **12.65 K** ✓；传热系数升 **129.36%** ✓；温度不均匀度降 **65.80%** ✓；三项基准 = `compared with the conventional MCHS` ✓
  - **PEC 1.99** ✓；**132.01 W/cm²** 与 **提高 122.20%** 同源同句 ✓
  - **待确认（基准）**：122.20% 所在句**未重申基准**，「相对常规 MCHS」属上文语境承接的推断——成稿不要写成原文明示
- **构型细节**：在下游微通道侧壁引入**椭圆、矩形、三角三种肋**，相邻通道间设**互连通道（interconnectors, ICs）**；三角肋导流最优、经 ICs 的横流最强。
- **待确认**：① 122.20% 的基准是否正文明示；② case 8 的具体几何参数。

### 4 · 10.1016/j.icheatmasstransfer.2026.112861 —— **待确认（部分）**
主体（标题、作者、单位、日期、数字）全部核实，但两项关键定义摘要里没有、正文读不到，故不给「通过」。
- **完整标题**：`Effect of coupled ribs and cavities on the hydrothermal comprehensive performance of microchannels under constant fluid domain volume`（无副标题、未截断）
- **作者**：Wenling Liao / Zhengbiao Jing / Shuaimei Lian / Fenghao Chen / Ao Li / Yuhan Xu / Pingping Liu（七位，逐位一致）
- **原始机构串 → 裁剪**：Liao / Lian / Chen / Li / Xu / Liu 均 `School of Mechanical Engineering, Chengdu Technological University, Chengdu` → **成都工业学院 机械工程学院**；Jing `Chengdu Vocational & Technical College of Industry, Chengdu` → **成都工业职业技术学院**（原串无学院/系一级）。两校**不可混写**。
- **通讯作者**：**Pingping Liu**（末位）
- **日期**：`created` 2026-10-14T07:14:56Z（✓ 窗内）；`published-online` 不存在。ICHMT vol.180 文号 112861。
- **性质**：`Numerical simulations are performed assess the feasibility of this strategy`（原文有漏词）—— **纯仿真**
- **数字**：Re `355-1065` ✓；五种构型原文列全 `MC, MC-SRCP, MC-PRCS, MC-SRCS, and DLMC-SRCS` ✓；`DLMC-SRCS achieves an average η exceeding 1.8, with a peak of 1.847 at Re = 533` ✓（平均 η>1.8、峰值 1.847、Re=533 三项全对）；η 定义 `hydrothermal comprehensive performance (η)`＝**水热综合性能**；机理 `combined improvements in wall impingement and interlayer fluid mixing`
- ⚠️ **不要照抄的作者自夸**：`which represents a marked enhancement over previously reported results` —— **未给任何对比文献与数值**，属无基准定性宣称
- **待确认（不可补写）**：
  1. **DLMC-SRCS 全称取不到**——摘要只给代号，五个缩写全部未展开。成稿只能写代号并注「原文摘要未给缩写全称」。
  2. **「等流体域体积」约束仅有摘要级口径**：`a design strategy based on the principle of maintaining a constant fluid domain volume in microchannels`；究竟以哪个基准构型的体积为准、肋与腔如何配比以守恒体积，摘要未说明、正文读不到。
  3. 摘要有语法残缺（`performed assess`），交存文本未经编辑清理。

### 批次 1 总体风险提示
1. **单位与通讯作者全部只有 OpenAlex 一个来源**。四条 Crossref 交存（含 unixsd XML）都不含机构串、corresponding 标注、摘要（对 112861 抓原始 XML 逐字确认）。按本期规则 OpenAlex 可作已核结论，但**本批不存在第二个独立出版商来源可交叉验证**。
2. **摘要来源单一**，均为 OpenAlex 倒排索引还原；还原文本里公式被拆成散字符（如 `𝑅 2 = 0 . 3 1 1`），数值无歧义但不要原样粘贴摘要片段。
3. **scout 两处会误导读者的表述必须改**：112802「标题被截断」是误判；133314「压降预测失败」应为「不可靠」。另 112802「前五位均机电工程学院」与原串不符。
4. **基准缺失是本批最大的数字风险**：112802 的 114–187% 必须带「相对常规直通道 MCHS」；112881 的 122.20% 所在句未重申基准；112861 的「显著优于已报道结果」无任何对比数值，不得当可比结论写入。
5. **全部四条都是纯计算研究、零硬件实验**，且 112802 / 112881 / 112861 是同一期刊（ICHMT vol.180）同一周落地的微通道 CFD 参数研究。**112861 与 112881 主题高度同类**，建议合并为一条或明确区分创新点，否则显得注水。
6. **判窗**：四条 `published-online` 字段均不存在，全部按 `created`：112802=10-13、133314=10-12、112881=10-16、112861=10-14，均在窗内。
7. **去重**：四条 DOI 在 `docs/` 已归档周报中无任何命中。**未发现**前期已归档周报与原文不符之处，本批无需「更正」。

---

## 批次 2 · 学术（A 组已有数字复核 5 条 + B 组缺失补取 5 条）

**取证通道说明**：本次环境只有 `api.crossref.org`、`api.openalex.org`、`arxiv.org/export.arxiv.org` 可达。ScienceDirect / linkinghub.elsevier.com / api.elsevier.com / ieeexplore.ieee.org / Semantic Scholar 全部被出口代理拒绝（`connect_rejected` 403）。另：**OpenAlex 免费额度在核验中途用尽**（UTC 午夜重置），第 6、8 条的补缺只能等下期。

### A 组

### 1 · arXiv:2610.16716 —— 通过（**单位已补到**）
- **完整标题**：Versatile two-layer model for thermohydraulic prediction of microchannel heat sinks
- **作者原串**：`Chih-Hsiang Chen^a , Kentaro Yaji^{a,∗}`
- **原始机构串（从 PDF 首页脚注取到，scout 两次取不到的那项已解决）**：`a Department of Mechanical Engineering, Graduate School of Engineering, The University of Osaka, 2-1, Yamadaoka, Suita, Osaka, 565-0871, Japan`
  - 裁剪后：**大阪大学 工学研究科 机械工程系**（两位作者同一单位）
  - 用名注意：原串写 **"The University of Osaka"**（该校 2025 年起启用的英文新名），不是 "Osaka University"。
- **通讯作者**：**Kentaro Yaji**（`∗ Corresponding author`）
- **日期/版本**：v1 2026-10-12（Atom `PUBLISHED`=`UPDATED`=2026-10-12T12:50:37Z，仅 v1）。**预印本，无 DOI、无 journal-ref，未经同行评审**。窗内。
- **性质**：纯数值，无实验。
- **两个待答问题的回答**：
  1. **摘要里确实没有任何定量数字**——逐句核过，全为定性表述（"improved overall agreement"、"conservative screening guideline"）。
  2. **确认是降阶/低维物理模型、不是机器学习**——全文 `machine learning`/`neural network`/`deep learning`/`surrogate`/`data-driven` 命中数均为 **0**；关键词 `Reduced-dimensional modeling`，正文自称 `Physics-based reduced-dimensional modeling`。
- **正文（非摘要）可用数字，若写必须标注「出自正文表 5 / 第 4 节，非摘要」**：
  - 求解时间加速比：AR=0.2 → **19.6×**；AR=1.0 → **34.5×**；AR=5.0 → **170.5×**；正文表述 "speedups ranging from approximately 20 to 171"（基准＝三维共轭传热参考模型稳态求解时间，137/138/682 s vs 7/4/4 s）
  - AR=1.0 底面温差仅 **0.51 °C**，对照 Zeng and Lee 模型 **4.26 °C**、Yan et al. 模型 **7.36 °C**
  - 最大水力误差 **12.12%**
- **待确认**：无

### 2 · ATE 133601 —— 通过
- **完整标题**：Transpiration-inspired micromembrane-enabled ultrathin vapor chambers with suppressed flow evolution
- **作者原串（Crossref 逐位）**：Yuxi Wu / Guisheng Zou / Hang Yu / Kuan Zhao / Zhewen Xiong / Chengjie Du / Haishan Cao / Yahui Wang / Shaoning Mu / **Zhanwen A** / Jinpeng Huo / Lei Liu
  - ⚠️ **与 scout 不符（姓名写法）**：scout 写 "A Zhanwen"。Crossref 交存 `given="Zhanwen"`, `family="A"` → 正确写法 **"Zhanwen A"**；OpenAlex 的 "A Zhanwen" 是归一化产物。
- **原始机构串 → 裁剪**：
  - Wu / Zou / Yu / Du / Huo / Liu：`State Key Laboratory of Clean and Efficient Turbomachinery Power Equipment, Department of Mechanical Engineering, Tsinghua University` → **清华大学 机械工程系**
  - Xiong / Cao：`Key Laboratory for Thermal Science and Power Engineering of Ministry of Education, Department of Energy and Power Engineering, Tsinghua University` → **清华大学 能源与动力工程系**
  - Zhao / Zhanwen A：`School of Mechanical Engineering, Qinghai University, Xining` → **青海大学 机械工程学院**
  - Yahui Wang / Shaoning Mu：`S Lab, GIC, IDG, Lenovo (Beijing) Co., Ltd., Beijing` → **联想（北京）有限公司**（"S Lab, GIC, IDG" 为内部实验室/事业群，按规则不写）
- **通讯作者**：**Jinpeng Huo 与 Lei Liu**（双通讯，OpenAlex `is_corresponding` + `corresponding_author_ids` 两处一致）。口径：系 OpenAlex 从原文脚注解析，非 Crossref 交存字段，成稿可写「据原文标注」。
- **`created`** 2026-10-14T16:04:12Z ✅ 窗内；`published-online` **Crossref 无此字段**；`published-print` 2026-11。ATE Vol 308 文号 133601。
- **性质**：**机理部分为「原位观测 + 理论建模 + 数值仿真」三者组合**（原文 "A combination of in-situ observation, theoretical modeling, and numerical simulation reveals..."）；**UTVC 整机性能部分为实物实验**。⚠️ 口径要分开：**「干涸距离与热流约 2 倍提升」属机理结论，不可写成「实测 2 倍」**。
- **数字（全部坐实）**：
  - 内部吸液芯厚度受限 **≤ 0.1 mm**（scout 未提，可补）
  - "approximately a twofold increase in the dry-out distance and heat flux" → 约 2 倍 ✅
  - 0.41 mm 与 0.31 mm UTVC 支持 **7 W·cm⁻²**，最大扩散温差分别 **< 0.9 °C** 与 **< 1.2 °C**，**在严格抗重力（strict anti-gravity）工况下** ✅
  - "more than doubles the maximum heat load sustained by the **open-channel counterpart**" → 最大热负荷 > 开放微槽对照的 2 倍 ✅（基准＝开放微槽对照件，**非商用均热板**）
- **待确认**：无（仅姓名写法需改）

### 3 · ICHMT 112840 —— 通过
- **完整标题（scout 缺，此处补全）**：**Transient response and thermal safe operating area extension of dual-heat-source vapor chambers for high-performance laptops**
- **作者原串**：Jing Wang / Wentao Yan / Shuangfeng Wang
- **原始机构串**：三位同串 `Key Laboratory of Heat and Mass Transfer and Low-Carbon Conversion, Ministry of Education, School of Chemistry and Chemical Engineering, South China University of Technology, Guangzhou` → **华南理工大学 化学与化工学院**
- **通讯作者**：**Wentao Yan 与 Shuangfeng Wang**（双通讯）
- **`created`** 2026-10-13T15:58:57Z ✅ 窗内；`published-online` 无；ICHMT Vol 180 文号 112840。
- **性质**：实验（实物 DHS-VC，含启动瞬态与五次交变载荷循环实测）
- **数字 —— scout 的 7 个数字逐个坐实，无一处不符**：厚度 **3.0 mm**；120 W–120 W 高载下启动 **1051 s**，比**纯网芯（pure mesh-wick）对照件**在**整个工况矩阵**上短 **5.8%–31.1%**；等载 190 W–190 W（**合计 380 W**）稳态**最小总热阻 0.032 °C/W**；不等载 280 W–60 W 下**局部峰值热流 58.33 W/cm²**；**75 °C 安全工作区（SOA）面积比纯网芯对照扩大 26.0%**
- **scout 漏掉、建议补的限定语**：原文明确 **100 °C 物理极限所围的外包络线与纯网芯对照「基本相当」（essentially comparable）**——扩大的只是 75 °C 那条 SOA。另：五次交变循环中无局部毛细干涸导致的温度突跳。
- **待确认**：无

### 4 · ICHMT 112864 —— **待确认（部分）**
- **完整标题**：Pool boiling performance of gyroid-structured surfaces subject to R-1233zd(E) refrigerant
- **作者原串**：Mohsen Khandan Bakavoli / Wei-Han Huang / Chi-Chuan Wang
- **原始机构串 → 裁剪**：
  - **Bakavoli（第一作者）：取不到**。OpenAlex 该 authorship 的 `raw_affiliation_strings` 为空数组、`institutions` 为空；Crossref `author.affiliation` 为空。**绝不按「他是 Chi-Chuan Wang 的第一作者」推定为阳明交大**——成稿必须标「单位待确认」。
  - Wei-Han Huang：`Rayvatek, Miaoli County, 360, Taiwan` → **Rayvatek**（企业，无学院可写）
  - Chi-Chuan Wang：`Department of Mechanical Engineering, National Yang Ming Chiao Tung University, Hsinchu` → **国立阳明交通大学 机械工程系**
- **通讯作者**：Chi-Chuan Wang（单通讯）
- **`created`** 2026-10-15T13:38:48Z ✅ 窗内；`published-online` 无；ICHMT Vol 180 文号 112864。
- **性质**：实验（摘要首句即 "This experimental study"）
- **「582%」专项核查 —— 确实出自摘要原文，但 scout 的写法有重大误导风险**：
  - 原文逐字：`At low heat flux under increasing heat flux conditions and 1.5 bar saturation pressure, GL-1 and GL-1.2 achieved HTC enhancements of approximately 582% and 183%, respectively, compared with the smooth surface.` → 582% 对应 **GL-1（1 mm 单元）**，183% 对应 **GL-1.2（1.2 mm 单元）**
  - **基准**：`a well-polished copper surface having an average roughness of 0.025 μm`（抛光铜面 Ra 0.025 μm）——**刻意做光的低基准**
  - **工况**：仅限「**低热流** + **升热流分支** + **1.5 bar**」这一个角点
  - ⚠️ **摘要里同页还有三组明显低得多的数字，不一起写就是选择性引用**：同压力（1.5 bar）**降热流分支、最高热流**下增益降为 **105%（GL-1）/ 112%（GL-1.2）**；最高测试热流 **≈ 215 kW·m⁻²**、**2.5 bar** 下最大 HTC 增益 **85%（GL-1）/ 101%（GL-1.2）**
  - ⚠️ **作者自己给 582% 打了折扣**：原文 `The reason for this improvement lies not only in the lattice-structure-enhanced surface but also in the fabrication process.`——增益**部分来自增材制造的原始表面形貌（as-built 粗糙度）**，不能全部归因于 gyroid 拓扑。**这一句必须随 582% 一起出现。**
  - **结论**：582% 可写，但**必须三件套齐全**——(a) 限定「1.5 bar、低热流、升热流分支」；(b) 同时给出 85%/101% 的高热流端数字；(c) 注明作者将部分增益归因于增材表面而非 gyroid 结构本身。**只写 582% 不加限定 → 判为不可写。**
- **其他可补**：滞回行为——光滑面降热流时 HTC 更高，gyroid 面升热流时更优；饱和压力升高则升/降热流差异减小。测试压力 1.5 / 2.0 / 2.5 bar。
- **待确认（逐条）**：① Bakavoli 单位取不到；② **增材制造工艺类型取不到**——摘要只写 `additively manufactured`，可取元数据中**未出现 LPBF / SLM / DMLS / 电子束等任何具体工艺名**，成稿**不得**写「激光粉末床熔融/SLM」，只能写「增材制造（工艺类型未披露）」；③ gyroid 试件材质（是否铜）摘要未明示。

### 5 · IJHFF 110749 —— 通过（被截断的数字已补取）
- **完整标题（scout 缺，此处补全）**：**Thermal–hydraulic design and multi-objective optimisation of a cicada-wing-vein-inspired liquid cooling plate for lithium-ion battery thermal management**
- **作者原串**：Sen Zhan / Lei Yuan / Yonggang Liu / Shaojiang Dong / Junda Chen
- **原始机构串 → 裁剪**：
  - Sen Zhan（双聘）：`School of Mechatronics and Vehicle Engineering, Chongqing Jiaotong University` + `State Key Laboratory of Mechanical Transmission for Advanced Equipment, Chongqing University` → **重庆交通大学 机电与车辆工程学院** + **重庆大学**（第二串只给国家重点实验室，按规则不写实验室，故重庆大学**无学院可写**）
  - Lei Yuan / Shaojiang Dong / Junda Chen：**重庆交通大学 机电与车辆工程学院**
  - Yonggang Liu：**仅重庆大学**（原串只有国家重点实验室，无学院）
  - 注意：**只有 Zhan 和 Liu 挂重庆大学**，不是全员。
- **通讯作者**：**Sen Zhan**（第一作者兼通讯，单通讯）
- **`created`** 2026-10-15T01:30:14Z ✅ 窗内；`published-online` 无；`published-print` 2026-12；IJHFF Vol 122 文号 110749。
- **性质**：**纯数值/优化**（三构型 CFD 对比 + 正交设计 + 代理模型 + NSGA-II + 拓扑优化）。⚠️ **摘要全文未提任何实验验证** → 不可写「实测」。
- **数字**：
  - 参数优化板 **相对初始仿生板**：最高温降 **1.79%**、平均温降 **1.39%**、温度均匀性改善 **13.28%**、压降降 **29.85%** ✅ 四项全部坐实，基准＝"initial biomimetic plate"（初始仿生板）**而非矩形直通道板**
  - **scout 被截断的那组已补到（拓扑优化板，3.5 g/s）**：原文 `At a coolant mass-flow rate of 3.5 g/s, the resulting biomimetic topology-optimised plate reduced the maximum temperature, average temperature, and temperature standard deviation by 0.36 °C, 0.34 °C, and 0.09 °C, respectively, while decreasing the pressure drop by 49.39 Pa relative to the parameter-optimised plate.` → 拓扑优化板在 **3.5 g/s** 下相对**参数优化板**：最高温 **−0.36 °C**、平均温 **−0.34 °C**、温度标准差 **−0.09 °C**、压降 **−49.39 Pa**
  - ⚠️ **基准链必须写对（两级基准，极易写错）**：1.79%/1.39%/13.28%/29.85% 是「参数优化板 vs **初始仿生板**」；0.36/0.34/0.09 °C 与 49.39 Pa 是「拓扑优化板 vs **参数优化板**」。两组**不可相加**，也不可混同基准。
  - 另：三种构型为矩形、斜分支、多级仿生分支；优化变量为分支数、分支角、通道宽、通道高。
- **待确认**：无（实验验证一项为「原文未提」，不是「取不到」）

### B 组

### 6 · ATE 133678 —— **待确认（单位/摘要/数字全部取不到）**
- **完整标题**：Data-efficient multi-objective structural optimization and design space exploration of refrigerant-based cold plate for laser device
- **作者原串**：Qingwen Gui / Youwei He / Jiangshuo Cui / Yong Chen / Chaochao Zhou（5 位）
- **原始机构串**：**取不到**。Crossref 五位 `affiliation` 全空；**OpenAlex 该 DOI 返回 404（尚未收录，`created` 就是今天）**。
- **通讯作者**：**元数据为空**
- **`created`** 2026-10-17T05:15:13Z ✅ 窗内（最后一天）；`published-online` 无；ATE Vol 308 文号 133678；PII `S1359431126039876`
- **性质**：**取不到**（标题含 "data-efficient"、"design space exploration" 提示代理模型驱动的仿真优化，**但这是推测、不是原文证据，不可写**）
- **数字**：**一个都没有 → 本条数字不可写。**

### 7 · ATE 133571 —— 通过（**单位、摘要、数字全部补到**）
- **完整标题**：Localized hotspot mitigation using a hybrid microchannel heat sink with alternating-orientation arched-bridge pin-fins
- **作者原串**：Xinglan Hou / Yongheng Yang（2 位）
- **原始机构串**：两位同串 `College of Electrical Engineering, Zhejiang University, Hangzhou 310027, China` → **浙江大学 电气工程学院**（注意：是**电气**工程学院，不是机械/能源）
- **通讯作者**：**Yongheng Yang**（末位，单通讯）
- **`created`** 2026-10-16T02:52:18Z ✅ 窗内；`published-online` 无；ATE Vol 308 文号 133571。
- **性质**：**纯仿真**。原文 `Three-dimensional steady-state conjugate heat transfer simulations are conducted`。摘要无任何实验。
- **数字（全部为新补，scout 原本没有数字）**：
  - 设计名 **AO-ABPF**（交替取向拱桥形针肋混合微通道），对照两件：**SPMC**（直平行微通道）与 **HCP**（混合圆形针肋）
  - 中心针肋用**硅**时（AO-ABPF(Si)），在 **Re=200–1000** 区间优于 SPMC 与 HCP
  - **Re=200**：T_max,base 相对 **SPMC 降 22.7 K**、相对 **HCP 降 8.3 K**
  - **Re=400**：热阻 R_th 相对 **SPMC 降 53.1%**、相对 **HCP 降 28.0%**
  - **硅换金刚石**（AO-ABPF(Di)）：Re=200–1000 全区间 T_max,base 再降 **1.4–2.3 K**、R_th 再降 **6.8%–12.1%**，两者总泵功 P_total 差异在**约 1.2%** 以内
  - 针肋间隙 W_fingap 从 **0.100 → 0.250 mm**：AO-ABPF(Di) 的 T_max,base 与 R_th 几乎不变，分别维持在**约 320 K** 与 **0.34 K/W**；而 AO-ABPF(Si) 相应升高 **5.9 K** 与 **26.5%**
  - 热点热流 **q″_hs = 900 W/cm²** 时，AO-ABPF(Di) 相对 **AO-ABPF(Si)** 再降：T_max,base **18.9 K**、R_th **32.4%**、δT,hotspot **36.8%**、δT,base **34.5%**
  - ⚠️ **口径警告（务必随数字写）**：(1) 全部为仿真、无实测；(2) 金刚石针肋收益是**仿真里换材料属性**得到的，900 W/cm² 热点也是**设定的仿真边界条件**，不是器件实测能力；(3) 原文把场景框定为 "AI accelerators and data-center processors"，属**引言式动机表述**，不代表有 AI 芯片实物验证。
- **待确认**：无

### 8 · Energy 142688 —— **待确认（且先纠一个关键错判：不是数据中心，是电动汽车）**
- 🚨 **完整标题（截断部分补全，Crossref `title` 与 `assertion.articletitle` 双处一致）**：**Design and Performance Evaluation of a Chiller-Free Integrated Thermal Management System Based on a Dual-Cooling-Media Cold Plate for Electric Vehicles**
  → **应用场景是「电动汽车」，不是数据中心。** 若按数据中心选题收录属选题层面错误，须整条移出。
- **作者原串（scout 未给，此处补全，8 位）**：Haibo Chen / Hongyu Ma / Tianshi Zhang / Shichun Yang / Hui Fan / Jialin Su / Haizhen Huang / Shaokang Li
- **原始机构串**：**取不到**（Crossref 八位全空；OpenAlex 404，今日交存尚未收录）
- **通讯作者**：**元数据为空**
- **`created`** 2026-10-17T09:46:17Z ✅ 窗内（最后一天）；`published-online` 无；**无卷号**，文号 142688；PII `S0360544226027957`
- **数字**：**一个都没有 → 不可写。**

### 9 · IEEE TCPMT 3742181 —— **待确认（原始机构串已核实：出版方交存的就是裸校名）**
- **完整标题**：Dynamic startup characteristics of a dual-evaporator cooling loop for electronic thermal management with unequal heat load
- **作者原串**：Ruixue Yang / Chengcheng Fan / Zhiheng Zhu / Chengbin Zhang
- **原始机构串（关键结论）**：**Crossref `author[].affiliation[].name` 四位全为字符串 `Southeast University`，一字不多。** 即 scout 看到的 "Southeast University" **不是 OpenAlex 归一名，而是 IEEE 向 Crossref 交存的原始机构串本身**（IEEE 交存习惯只给裸机构名）。OpenAlex 的 `raw_affiliation_strings` 同样是 `Southeast University`，两处一致。
  - 裁剪后：**东南大学**（**院系取不到**——出版方根本没交存。成稿**不得**补「能源与环境学院」之类）
- **通讯作者**：**元数据为空**
- **`created`** 2026-10-12T19:09:11Z ✅ 窗内；`published-online` 无；`published-print` `[[2026]]`（仅年份）；**`page`="1-1"、无卷号 → 典型 Early Access**，Xplore 文档号 11733509
- **评审状态**：已被 IEEE TCPMT 接收、Early Access 上线，**尚未编入正式卷期**
- **数字**：**一个都没有 → 不可写。**（Crossref message 里没有 `abstract` 键，已 dump 全部 keys 确认；IEEE Xplore 域名本会话不可达）

### 10 · ICHMT 112814 —— **否决**
- **完整标题**：Encoded corrugation design for flow redistribution and thermohydraulic performance enhancement in parallel microchannels
- **作者原串**：Yili Zhou / Ping Xu / Jie Xing / Shuguang Yao
- **原始机构串**：**第三次取不到**（Crossref 四位全空；OpenAlex 虽已收录但四位 authorship 的 `raw_affiliation_strings` 与 `institutions` 均为空）
- **`created`**：**2026-10-09T16:53:42Z**（`deposited` 2026-10-12，`published-print` 2026-11）
- **否决理由（两条，任一即可）**：
  1. **落在时间窗外**：判窗依据 `created` = 2026-10-09，早于窗口起点 2026-10-11 两天。（`deposited` 10-12 在窗内，但按本刊规则判窗用 `created`。）
  2. **单位与摘要连续三期取不到**，无任何可核实的实质内容。
- **与前期档案的关系**：第 9 期 open-items 已记录「下期重试」。**本条此前从未上站，不存在已发布错误，无需进更正节**；既已确认永久落在窗外，建议把 open-items 的「下期重试」改为**结案**。

### 批次 2 总体风险提示
1. **「数字仍不可写」共 3 条**：ATE 133678（零数字/零单位/零通讯）、Energy 142688（零数字/零单位，**且场景实为电动汽车**）、TCPMT 3742181（零数字；单位只能写到「东南大学」，院系系出版方未交存）。
2. **数字可写但必须带限定语，裸写即判不可写 —— 1 条**：ICHMT 112864 的 **582%**（三件套缺一不可）；该条增材工艺类型原文未披露，不得补写。
3. **选题层面硬错误 —— 1 条**：Energy 142688 不是数据中心散热，是电动汽车整车热管理。
4. **单位「取不到」而绝不可推定 —— 3 处**：112864 的 Bakavoli（勿因其为 Chi-Chuan Wang 的第一作者就写成阳明交大）；133678 全部 5 位、142688 全部 8 位（OpenAlex 均 404，交存当天，下期大概率可补）；3742181 的院系。
5. **基准链写错的高风险点**：IJHFF 110749 两组数字是**两级不同基准**，不可相加混同。ICHMT 112840 同理：75 °C SOA 扩大 26.0% 成立，但 **100 °C 外包络与对照「基本相当」**，不能笼统说「安全工作区大幅扩大」。
6. **姓名写法更正**：ATE 133601 的 "A Zhanwen" 应按 Crossref 交存改为 **"Zhanwen A"**。
7. **仿真被读成实测的风险**：arXiv 2610.16716、IJHFF 110749、ATE 133571 **全为纯数值、无任何实验**；ATE 133601 需把「机理结论（原位观测+建模+仿真组合）」与「整机实测」分开表述。ATE 133571 的 900 W/cm² 与金刚石针肋收益尤其容易被当成器件实测能力。
8. **取证通道受限（基础设施层面，非核验疏漏）**：本会话仅 Crossref / OpenAlex / arXiv 可达；ScienceDirect、linkinghub、api.elsevier.com、IEEE Xplore、Semantic Scholar 均被出口代理 403 拒绝。**OpenAlex 免费日额度在核验中途耗尽**，故 133678、142688 两条的 404 无法再用标题检索复验。**建议下期开篇即重试 133678、142688、3742181 三条的单位与摘要**。
9. **工具改进建议（流程，不进刊物）**：建议把「原始机构串 + 摘要倒排重建」能力并入 `scripts/fetch_source.py`——现版脚本遇 Elsevier 只会打印 "Crossref carries no affiliation"，是本期多条单位连续取不到的直接原因。
