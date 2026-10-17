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
