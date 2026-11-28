# 第 15 期 · 逐位核验结果（两名 verifier 回传 + 主代理对补扫 4 条的 Crossref 交叉核）

## 全局裁定
- **判窗一律用 Crossref `created`。** 本期再次实测：**OpenAlex `created_date` 系统性比 Crossref `created` 晚约 1 天**
  （THERMINIC 四条 11-20/24/26 对 Crossref 11-19/23/25；补扫四条 11-27/28 对 Crossref 11-26/27）→ 补入 open-items 作佐证。
- **THERMINIC 2026 会期统一为 2026-09-16 ~ 09-18，Berlin, Germany**（Crossref `event` 字段四条字面一致）。
  ⚠️ scout 回传里的「会议日期 2026-09-01」**是伪数据** —— 系 OpenAlex 把 `published-print: 2026-09` 归一成 `publication_date: 2026-09-01` 的产物，**全文禁用**。
- **摘要来源**：本期绝大多数条目 Crossref 无 `abstract`，摘要唯一来源是 **OpenAlex `abstract_inverted_index` 还原**。
  独立第二源本期全部取不到：`ieeexplore.ieee.org`、`www.mdpi.com`、`onlinelibrary.wiley.com`、`www.sciencedirect.com`、
  `journal.ksmpe.or.kr`、`koreascience.kr`、`api.semanticscholar.org`、`doaj.org` 均被出口代理拒绝。
  可达者仅 `api.crossref.org` 与 `api.openalex.org`。
- **通讯作者**：Crossref 交存普遍无 corresponding 标记；凡 OpenAlex `is_corresponding=true` 的按 rules 第 2 条作已核结论，否则「待确认」。
- **姓名一律采 Crossref 出版商交存串**（延续第 14 期先例），不采 OpenAlex 归一 `display_name`。

---

## A 组 · 窗口内期刊候选（verifier 1）

### ① 10.1016/j.icheatmasstransfer.2026.113204 —— **通过**
标题：In silico design and fabrication of biomorphic cold plates for chip cooling
- 作者/单位（OpenAlex `raw_affiliation_strings`，删邮编国别后）：
  Nikolaos Cavadias（Department of Mechanical Engineering, Imperial College London）；
  **Matei C. Ignuta-Ciuncanu（通讯作者，已核，中间位）**（Department of Nuclear Engineering, University of California, Berkeley；Dyson School of Design Engineering, Imperial College London）；
  Ricardo F. Martinez-Botas（Department of Mechanical Engineering, Imperial College London）
  原串：`Department of Mechanical Engineering, Imperial College London, SW7 2AZ, UK` / `Department of Nuclear Engineering, University of California, Berkeley, CA, USA` + `Dyson School of Design Engineering, Imperial College London, SW7 2AZ, UK`
  ⚠️ scout A 误称 Imperial / UC Berkeley 是「OpenAlex 归一名」——**出版商原串本身就这么写且带院系**。
  ⚠️ 通讯作者是**中间位**，成稿勿按末位惯例标注。
- 日期：Crossref created **2026-11-26T17:38:11Z**（窗口内）；无 published-online；published-print 2027-01（不作依据）。卷期已定 Vol. 182, 113204。
- 数字（逐句核）：峰值基底温度 **336.0 K → 325.6 K**（原句 "reduces the peak base temperature from 336.0 K to 325.6 K"）；
  **29%** 的口径是「**相对 300 K 入口之上温升**的降幅」（原句 "corresponding to a 29% reduction in temperature rise above the 300 K inlet"；36.0 K → 25.6 K 自洽）；
  **±30 μm** 带限定词 **coarse（粗尺度）in-plane** 与 approximately（原句 "with coarse in-plane dimensions reproduced within approximately ±30 μm"）。
  对照基准原句 "Against a straight-channel benchmark of identical fluid fraction, inlet condition and power map" → 候选表述正确。
  求解器 "an open-source finite-element implementation with adjoint sensitivities (FEniCS)"。
  实物侧 "fabricated in silicon by femtosecond laser micromachining. Microscopy confirms transfer of the principal trunks, secondary branches and hotspot terminations to the physical die"。
- **无热实验**；压降/泵功/热流密度/芯片功率绝对值摘要均无。

### ② 10.1016/j.applthermaleng.2026.134123 —— **待确认（口径）**
标题：Direct-to-chip evaporative cooling: Effect of liquid delivery layer on flow maldistribution and thermal performance
- 作者（Crossref 交存名）：Kidus Guye、Vivek V. Manepalli、Ayşenur Ateş、Samuel Graham、**Damena Agonafer（通讯作者，已核）**
  五位同一原串 `Mechanical Engineering, University of Maryland, College Park, MD, United States of America`
  → 主代理裁定：**写「Mechanical Engineering, University of Maryland, College Park」**（College Park 系该校校区名、属机构名一部分，与第 14 期「加州大学原串未写明校区」的记法一致；仅删 `MD, United States of America`）。
- 日期：Crossref created **2026-11-25T13:20:29Z**（窗口内）；published-print 2026-12（不作依据）。卷期已定 Vol. 311, 134123。
- 数字：**22 °C** 系**实测**（原句 "thermal measurements indicate a 22 °C higher substrate temperature compared to hydrophilic surfaces at the same heat load"）；
  LDL 高度 **15 μm → 90 μm**；**>40×**（R-1336mzz(Z)，2 kW）与**最高 32×**（水，5 kW）系**数值结果**（原句前缀 "Numerical results further demonstrate"）。
  ⚠️ **待确认**：(a) 摘要**从未定义 "liquid maldistribution" 的量化指标**；(b) "at 2 kW / 5 kW" 原文**未写 heat load 字样**，不得替补。
- 热阻/热流密度/结温绝对值：摘要均无。
- 🔴 **必须披露的时效问题**：同名同摘要的 **SSRN 预印本 `10.2139/ssrn.6535751`，Crossref created 2026-04-07**，摘要逐字一致
  → 内容自 2026 年 4 月已公开，本周只是期刊正式版上线。**成稿必须注明**，否则会把半年前的结果当本周新结果。
- 去重：与第 13 期 DCEC 一文（`10.1109/tcpmt.2026.3751096`，伊利诺伊理工 Upadhyay/Acharya）**非同篇**，机构与内容均不同。

### ③ 10.1002/jtse.70014 —— **待确认（百分比无绝对值）**
标题：Enhanced Cooling Performance of LTCC Microchannel Heat Sink With Embedded Metal Pin Fins
- 作者（Crossref，**共 4 位即全名单**）：Lili Zhang、Zhensong Li、Han Wang、**Lili Cao（通讯作者，已核，第 4 位）**
  四位同原串 `School of Information and Communication Engineering Beijing Information Science and Technology University  Beijing China`
  → 写「School of Information and Communication Engineering, Beijing Information Science and Technology University」（删 Beijing China）。
  ⚠️ 勿用 OpenAlex 归一名 "Beijing Information Science & Technology University"（带 &）。
  ⚠️ scout 称「其余待确认」可销——交存只有 4 位。
- 日期：Crossref created **2026-11-27T09:52:52Z**、**published-online 2026-11-27**（均在窗口内）。
  Wiley assertion：received 2026-08-07、accepted 2026-10-21、published 2026-11-27；**无卷期无页码，仅文章号 e70014（Early View）**。
- 刊物归属（已核）：Crossref publisher = Wiley，DOI 前缀 10.1002，ISSN 1948-5085/1948-5093；`doi.org` 重定向落地 **asme.onlinelibrary.wiley.com**
  → **ASME 刊、Wiley 出版/托管**。⚠️ OpenAlex 显示 host "ASM International"（ASM ≠ ASME）**是归一错误，勿采用**。
- 数字：10/15/20 W 下中心最高温度降 **23.55% / 19.78% / 17.18%**，基准 = **无针肋模型**（原句核实）；仿真与实验相对误差 **1.15%–8.13%**。
  ⚠️ **摘要内无任何绝对温度值**，百分比取自绝对温度还是温升**原文未界定** → 23.55% 无法还原成 K/°C。压降仅定性 "minimal pressure drop penalty"。

### ④ 10.1002/htj.70429 —— **待确认（工况基准缺失）**
完整标题（Crossref）：Multiobjective Optimization and Thermal–Hydraulic Performance of Pin-Finned Manifold Microchannel **for Flow Boiling**
  ⚠️ 后缀 "for Flow Boiling" 是关键限定（两相），scout 的截断标题会让读者误以为是单相优化。
- 作者（Crossref，**共 2 位即全名单**）：**Yitao Shi（通讯作者，已核）**、Aili Zhang
  原串 `School of Mechanical and Equipment Engineering Hebei University of Engineering  Handan China`（Shi 另挂河北省级重点实验室
  `Key Laboratory of Intelligent Industrial Equipment Technology of Hebei Province` → **按规则 3 整条删去**）→ 写「School of Mechanical and Equipment Engineering, Hebei University of Engineering」。
- 日期：Crossref created **2026-11-24T13:10:57Z**、**published-online 2026-11-24**（窗口内）。无卷期，文章号 htj.70429（Early View）。
- 数字：Pareto 前沿上加热面温度 **61.05–86.88 °C**、压降 **2.24–2.57 kPa**；TOPSIS 最优解加热面 **62.75 °C**、压降 **低于 2.40 kPa**（原文 "below"）。
  设计变量三个：fin height、fin spacing、inclination angle；方法 = 流固耦合数值 + RSM + NSGA-II + TOPSIS。
  定性结论（引用勿写反）：**翅片高度增加使加热面温度显著升高**，压降呈相反趋势；倾角对加热面温度存在峰值。
  ⚠️ **确认缺失**：热流密度、热源功率、流量/质量流密度、入口温度压力、工质牌号、通道尺寸**全无**；**无实验**（通篇仅 "a fluid–solid coupled numerical model"）。

### ⑤ 10.3390/mi17121371 —— **待确认（无绝对值，MDPI 不可达）**
标题：Surrogate-Assisted Multi-Physics Optimization of a Double-Sided Water-Cooled SiC Power Module Using a Neural Network and a Genetic Algorithm
- 作者（Crossref，**共 5 位即全名单**）：Shuhua Liao、Jiuyang Tang、Liming Che、Qiuming Wang、**Guangyin Lei（通讯作者，已核，末位）**
  五位同两条原串 `College of Intelligent Robotics and Advanced Manufacturing, Fudan University, Shanghai 200438, China` +
  `Research Institute of Fudan University in Ningbo, Ningbo 315336, China`（删邮编城市）
  （OpenAlex 把第 3 位显示为中文「车黎明」，以 Crossref 交存的 **Liming Che** 为准。）
- 日期：Crossref created **2026-11-25T15:28:46Z**、published-online 2026-11-25（窗口内）。卷期齐全 Micromachines **17(12), 1371**，CC-BY 4.0。
- 数字：**6 个几何参数**（具体哪 6 个摘要未列）；**4 个冲突的电热目标**（最高结温、动态电流不均衡、杂散电感、等效热容）；
  **总寻优算力降低 >20 倍**，被比对象核清 = **direct finite-element optimization（直接有限元寻优）**，量纲为 "total optimization computational cost"，**无绝对机时**。
  ⚠️ **摘要内无任何结温/热阻/电感绝对值**（逐句确认）。作者自述**热串扰参数强非线性、拟合精度低**（原文自认局限，可引）。
  最优解的「再验证」是高保真多物理场仿真，**不是实测**。
- `www.mdpi.com` 本期不可达（代理 403 + DNS 不解析），全文未能补。

### ⑥ 10.1016/j.ijheatmasstransfer.2026.129948 —— **通过**
标题：Co-designed solid–solid PCM heat sinks for transient thermal management in data centers
- **裁定：摘要里确有这些数字 —— scout D 正确，scout A 的「未获取到数字结果」系取数不全**（OpenAlex 还原摘要约 500 词，数字集中在中后段）。
- 作者（Crossref 交存名）：**Prashant Saini（通讯作者，已核）**、**Julian D. Osorio（亦为通讯作者，已核 —— 本文两位 corresponding）**、Munjal P. Shah
  原串 `Center for Energy Conversion & Storage Systems, National Laboratory of the Rockies, Golden, CO 80401, United States` /
  `Building Technologies and Science Center, National Laboratory of the Rockies, Golden, CO 80401, United States`
  → 三位均写 **National Laboratory of the Rockies**（按规则 3 删中心名与 Golden, CO 80401, United States）。
  ⚠️ **澄清**：scout A 担心该名是归一产物 —— **不是**，它写在 Elsevier 交存原串里；OpenAlex ROR `https://ror.org/036266993` 主名亦为该名，
  `display_name_alternatives` 含 "National Renewable Energy Laboratory"（同址 Golden, CO 80401）。
  **主代理裁定：成稿只写原串名，不加注「原 NREL」**（该别名出自 ROR 记录、非论文原文，按 rules 第 2 条不作推定）；ROR 别名记入跨期清单备查。
- 日期：Crossref created **2026-11-25T13:52:45Z**（窗口内）；published-print 2027-04（不作依据）。卷期已定 Vol. 275, 129948，CC-BY 4.0。
- 数字：**PCM 质量恒定 60 g**（⚠️ 限定在**几何对比**部分）；风车形棱柱翅片 **应用导向权重下 TPI 0.914** 对基线针翅 **0.391**（⚠️ 必须带「应用导向权重」限定，原文另有 equal 权重一套）；
  **14/14 双面板构型**相对 **baseline pin fin** 使峰值源温降**约 23 K**、恢复时间缩短**约 79%**（两数字原文均带 approximately）。
  **TPI = thermal performance index**，由 6 项指标（源温抑制、固-固相变分数、最大储能、汇侧排热、恢复时间、潜热贡献）归一化加权合成，两套权重；
  **具体权重数值与归一化方式摘要未给**。
  ⚠️ **「14/14」含义摘要未定义**，verifier 的「28 块板按源/汇侧各 14 分配」只是推断，**成稿勿当事实陈述**。
  其他已核数字（备选）：等能量加载下峰值局部源表面温度 **371.34 K（恒定均匀）→ 374.92 K（Workload 均匀）→ 388.01 K（Workload 热点）**；
  两时变工况最大源温差 **4.29 → 21.36 K**、面积加权温度标准差 **0.97 → 5.01 K**；另一组 **100 W** 评估中热输入自 **40 cm² 集中到 4 cm²**、
  局部热流 **2.5 → 25 W/cm²**、峰值面均源温 **385.73 → 475.19 K**；六板构型应用导向指数 **0.049**、28-simple **0.845**、28-perforated **0.850**；
  PEG 相变窗口 **330–340 K**；**4% 石墨烯**强化 PEG 在以排热为先时最优；Mn 层状钙钛矿在基线工况下质量归一 TPI 最高；翅片材料中铜给出最低源温与最快排热、石墨在综合质量归一指标最高。
- **纯数值**，校核方式为 "validated against published pin-fin and spiral-fin configurations"（**对照文献数据，无自测实验**）。

**verifier 1 汇总**：6 条全部在窗口内（created 11-24 / 11-25×3 / 11-26 / 11-27），**无一条应否决**，与前 14 期无重复。
**对前期周报的更正：本次核验范围内未发现第 1–14 期与原文不符之处。**

---

## B 组 · 会议与制造工艺候选（verifier 2）

### ① 10.1109/therminic70452.2026.11779811 —— **通过**（窗外补收）
标题：Why the Optimal Pin-Fin Geometry Depends on the Operating Point: A Separation-Based Analysis of Sinusoidal Meso-Channel Cold Plates
- 作者/单位（Crossref 原串 → 按规则 3/4 删改后）：
  Mahdi Vahidi（**OVHcloud / University of Reims Champagne-Ardenne**）、Hadrien Bauduin（OVHcloud）、Michael Maalouly（OVHcloud）、
  Ali Chehade（OVHcloud）、Fabien Bogard（University of Reims Champagne-Ardenne）、Chadi Maalouf（University of Reims Champagne-Ardenne）
  删改依据：作者 5/6 的 `ITheMM` 出现在 `name` 原串 → **按规则 3（不写下属实验室）删**；作者 1 的 `ITheMM` 与各人 `R&D Cooling dept.`
  出现在 **`department` 字段** → **按规则 4 本就不补写**；`place`（Croix / Reims, France）按规则 3 删。
  **`OVHcloud` 字面两源一致确认**（Crossref `name` 与 OpenAlex 原串 `OVHcloud, Croix, France`）→ **「云服务商自己发冷板论文」判断成立**。
  六位姓名三源完全一致。**通讯作者：待确认**（两源均无标记）。
- 日期：Crossref created **2026-11-19T20:27:21Z**；published-online **null**；published-print 2026-09（会期月份，不判窗）；
  会期 **2026-09-16~09-18, Berlin, Germany** → **窗口外，按前期漏收补收、如实写 11-19**。
- 数字：**15 种构型**（原句 "Fifteen configurations are **simulated** in a water-cooled meso-channel using conjugate heat transfer computations" → **全部仿真，非实验**）；
  **压降 ∝ 瓶颈流速的 2.10 次方**（原句 "the pressure drop is shown to scale with the bottleneck velocity raised to the power 2.10"）；
  **0.4–0.8 L/min 区间内前六名排序几乎完全反转**（原句 "between 0.4 and 0.8 liters per minute the ordering of the six highest-ranked configurations is almost exactly reversed, and each end of the range renders a different geometry inadmissible through the opposing constraint"）。
  ⚠️ **「几乎完全反转」是纯定性表述** —— 摘要无 Spearman 系数、无任何量化反转指标（`Spearman`/`correlation`/`rank coefficient` 全未出现）→ **成稿不得暗示有量化指标**。
  可引细节：工质为水；几何 "manufacturable in two passes of a single milling cutter"（**单把铣刀两刀可加工**）；分离点沿针肋周长按 `normalized arc length` 提取；四个几何参数 "act through distinct and separable mechanisms"。
- 待确认：通讯作者；**无实验**（摘要无 experiment/measured/test bench 任一词）；**热阻/温度/热流密度/芯片功率绝对值全无**（仅 "trade-off between thermal resistance and pumping penalty" 定性）；**meso-channel 尺度定义未给**；2.10 的拟合区间、R²、不确定度未给。

### ② 10.1109/therminic70452.2026.11779752 —— **通过**（窗外补收）
标题：Enabling Flow Redistribution in Skived Heat Sinks for High-Power Density Computing: An End-to-End Case Study
- 🔴 **两 scout 矛盾裁定：scout A 正确、scout B 错误。** `MegaCool Technologies` **两源都有且字面一致**：
  Crossref `author[].affiliation[0].name` = `MegaCool Technologies`（三位全部），`place` = `Rotselaar, Belgium`，无 `department`；
  OpenAlex `raw_affiliation_strings` = `MegaCool Technologies, Rotselaar, Belgium`（三位全部）。
  scout B 的「OpenAlex 未给出任何单位」系查了归一字段而非 `raw_affiliation_strings`（该 work 的机构未被归一匹配，但原串在）。
  → **「skived 翅片」工艺的「擅长企业」缺口可用本条填上**，机构名按原串写 `MegaCool Technologies`（规则 3：企业写机构名即可）。
- 作者：Ine Vandebeek、Lieven Vervecken、Rui Vieira（均 MegaCool Technologies）。姓名三源一致。**通讯作者：待确认**。
- 日期：Crossref created **2026-11-19T20:22:03Z**；会期 2026-09-16~09-18, Berlin → **窗口外，补收**。
- 数字：**3 种设计的实验测试**（原句 "We validate this approach through a conjugate heat transfer simulation framework, complemented by experimental testing of three distinct designs." → **仿真框架为主 + 3 个设计实验为补充**）；
  **相对一款商用参考件热阻降低 47%**（原句 "the optimized designs achieve a 47% reduction in thermal resistance compared to a commercially available reference"）。
  ⚠️ **基准未具名** → 成稿只能写「相对某一款商用参考件」，**不得点名任何厂商/型号**。
  ⚠️ **47% 的口径未分辨：摘要只说 "Our results"，未说明是实测还是 CHT 仿真** → 必须标注。
  ⚠️ **口径归属纠正**：**>200 W/cm² 封装热流与接近 600 W/cm² 局部热点是行业趋势的背景陈述**（原句 "The rapid expansion of high-performance
  computing and AI accelerators has driven package-level heat fluxes beyond 200 W/cm2, with localized hotspots approaching 600 W/cm2."）
  → **不是本文实测工况**，成稿必须保留「行业背景」定语。
  **SmartFins = 作者自命名的方法框架**（原句 "This paper introduces the SmartFins framework"），摘要未表述为已上市产品。
  「生成式设计」原文用词 = **"high-volume, subtractive-aware generative design"**（面向减材工艺、量产导向），另有 "monolithic copper manufacturing"。
  ⚠️ **绝对热阻/流量/压降摘要零数字** → 不得出现在成稿。
  技术动因（可引）：常规基于线性 skived 微翅结构的冷板 "frequently limited by thermal boundary layer development and suboptimal coolant distribution"；增材路线 "remains constrained by high costs and limited production scalability"。
- 技术局限：参照件未具名不可复现；实测/仿真口径未分；仅 3 个设计进入实验；无压降泵功数字 → 无法判断是否以压降换热阻；三位作者同属一家企业，**企业自测自评、无第三方复现**。

### ③ 10.1109/therminic70452.2026.11779771 —— **仅可作线索（零可引数字，已确认）**
标题：Laser Powder Bed Fusion of Copper-Graphene Metal Matrix Composites for Enhanced Heat Transfer
- 作者/单位（Crossref 原串，**院系写在 `name` 里、非 `department` 字段** → 按规则 4 后半句**可以写**）：
  Wessel W. Wits、Hyunjong Lee、Leonore van Goor、**Bernard Geurts**（四位：Mathematics and Computer Science, University of Twente）；
  Davoud Jafari（University of Twente）。`place` = Enschede, The Netherlands（删）。
  🔴 **姓名更正**：交存串与 OpenAlex `raw_author_name` 均为 **`Bernard Geurts`**；`Bernard J. Geurts` 只是 OpenAlex 归一 `display_name`
  → 按第 14 期先例**采交存串**，scout A 所报须更正。**通讯作者：待确认**。
- 日期：Crossref created **2026-11-19T20:23:10Z**；会期同上 → 窗口外，补收。
- **数字复核：确认为零。** 摘要全文无石墨烯质量分数、无致密度数值、无热导率数值、无 LPBF 工艺参数、无基线值。
  唯一可引定性结论：**「加入石墨烯可恢复纯铜 LPBF 过程中损失的热导率」**；且**是实验研究**（"investigated experimentally"）；粉末制备为 **mechanical mixing**。
  ⚠️ 措辞上限：「恢复」的是 LPBF 工艺损失的那部分热导率，**并非超过纯铜本体** → 成稿不得写成「超过纯铜」。

### ④ 10.1109/therminic70452.2026.11779750 —— **仅可作线索（零可引数字）+ 🔴 单位须更正**
标题：Experimental and Numerical Investigation of an SLA-Manufactured Alumina Ceramic Heat Sink for Wide-Bandgap Power Modules
- 🔴 **单位更正（最重要的一处出入）**：scout B 报「六位均 `Institut Catholique d'Arts et Métiers`」—— **两源都查不到这个字符串**。
  出版商交存原串是 **`Icam School of Engineering`**（三种变体：`Icam School of Engineering, Univ. De Toulouse` / `Icam School of Engineering` / `Icam School of Engineering, Univ Toulouse`），
  Crossref `name` 与 OpenAlex 原串字面一致。→ 按铁律 2，**只能写 `Icam School of Engineering`，不得写 `Institut Catholique d'Arts et Métiers`（属自行扩写）**。
  单位串的大小写与缩写不一致（`Univ. De Toulouse` / `Univ Toulouse`）**是出版商原样，不统一、不扩写成 `Université de Toulouse`**。
- 作者共 **9 位**：Lucie Teulet、Jean-Pierre Fradin、Ahmad Batikh、Alexandre Marie、Benjamin Périé、Virgile Puel（Icam School of Engineering，部分另挂 Univ. De Toulouse）；
  Emmanuel Marcault、Lucile Mage（**CEA**）；**Patrick Tounsi**（原串 `LAAS-CNRS, Univ. De Toulouse`）。
  🔴 **姓名更正**：交存串与 OpenAlex `raw_author_name` 均为 **`Patrick Tounsi`**；`P. Tounsi` 只是 OpenAlex `display_name` → scout B 所报须更正。
  **`LAAS` 处置**：主代理裁定按规则 3 删实验室名 → 写 **CNRS, Univ. De Toulouse**。**通讯作者：九位全待确认**。
- 日期：Crossref created **2026-11-19T20:13:57Z**；会期同上 → 窗口外，补收。
- **数字复核：确认为零。** 热阻值无、压降值无、流量区间无（仅 "the investigated range of flow rates"）、功率/热流密度无、偏差百分比无。
  可引定性：材料 **氧化铝 Al₂O₃**；工艺 **SLA**；原文自称 **"a first experimental and numerical comparison"**；仿真工具 **ANSYS Fluent**；
  **有专用试验台实测**（"experimentally characterized on a dedicated test bench"）；
  关键句 "the numerical model accurately predicts the thermal resistance and pressure drop over the investigated range of flow rates, with trends consistent with the experimental observations. The remaining discrepancies are mainly attributed to manufacturing tolerances, uncertainties in material properties and experimental measurements, and modelling assumptions."

### ⑤ 10.14775/ksmpe.2026.25.11.165 —— **通过**（窗口内）
标题：Weight Reduction and Thermal Performance Validation of a Multi-channel Cooling Plate Using Additive Manufacturing
刊：Journal of the Korean Society of Manufacturing Process Engineers，ISSN 2288-0771，Vol. 25, No. 11, pp. 165–176。
- 🔴 **作者栏裁定：`Hanwha Systems` 确系单位被误交存进作者栏，真实作者为 3 位。**
  证据：Crossref `author` 第 1 个条目是 **`{"name": "Hanwha Systems", "sequence": "first", "affiliation": [], "role": [author]}`**
  —— **机构型条目（只有 `name`、无 `given`/`family`）**；而第 2 个条目 `Hyun-Woo Jeong` 的 `sequence` **也是 `first`**（一个作者列表两个 `first`，交存错误的典型指纹）。
  OpenAlex 原样继承把它解析成作者实体，**同时把 `Hanwha Systems` 作为另外三人的 `raw_affiliation_strings`**。
  → **真实作者 3 位**：Hyun-Woo Jeong、Se-Jin Yoon、**Jae-Hun Heo（通讯作者，已核；OpenAlex `is_corresponding=true`，三人中唯一）**，均 **Hanwha Systems**。
  ⚠️ **成稿不得把 `Hanwha Systems` 列为作者**，也不得写成「四位作者」。
  ⚠️ Crossref 的 `affiliation` 数组四条全空，单位串只在 OpenAlex 原串与上述误交存条目里 → **备注须注明证据链**。
- 日期：Crossref created **2026-11-23T04:29:26Z**（**窗口内**）；`published-online` **null**；published-print/published/issued 均为 **2026-11-30**
  —— **该日期尚在未来，成稿切勿当作发表日**。
- 数字：最高温度比**传统（减材）制造模型**低 **1.0 °C**（原句核实）；质量 **5.3 kg → 4.4 kg**，原文字面 **16.9%**。
  **验算裁定**：(5.3−4.4)/5.3 = 16.98% ≈ 17.0%，**原文写 16.9%（截断）** → **照原文写 16.9%，不得自行改成 17.0%**。
  ⚠️ 原文该句英文有笔误（"reduced the weight reduction from..."），中文转述按「质量由 5.3 kg 降至 4.4 kg」写。
  **有实验验证**（"Numerical analysis and experimental validation demonstrated..."），但**工况一个数字都没给**。
  工艺：`laser powder bed fusion (L-PBF)` 与 `selective laser sintering (SLS)` **两者并列出现，但各自做了什么、SLS 用于金属还是非金属，摘要完全未说**
  → **待确认，禁止二选一**。结构：`integrated manifold structure and internal lattice structures`，**晶格类型/单胞尺寸/通道数均未给**。
  **应用对象**：原文两处 —— 动因 `thermal stability in increasingly prevalent high-heat-flux weapon systems`，结论 `cooling systems for high-power electronic equipment`。
  **覆盖面裁定（主代理）**：原文自己把落点收在「**大功率电子设备**」且是冷板/热点抑制问题 → **在本刊「电子散热」覆盖面内**；
  但须如实标注应用语境是**武器系统**，**具体载荷原文未指明**（不得自行指定，也不得写成「数据中心」）。
- 出版商页面不可达：`journal.ksmpe.or.kr`、`koreascience.kr` 均被代理拒绝。

### ⑥ 10.1109/cencon70655.2026.11804424 —— **仅可作线索（无降幅数字）**（窗口内）
标题：Flow boiling enhancement using a vapor venting membrane for high-power electronics cooling
会议：2026 IEEE Conference on Energy Conversion (CENCON)，会期 **2026-10-26~10-27, Putrajaya, Malaysia**（Crossref `event`）。
- 作者：**Md Danish Eqbal**、Manabendra Pathak、**Mohd. Kaleem Khan**（均 **Indian Institute of Technology Patna**）。
  **院系处置**：`Department of Mechanical Engineering` 只出现在 Crossref **结构化 `department` 字段**、OpenAlex 原串里没有
  → **按规则 4 不补写**（与上面 ③ 相反的处理，是规则 4 的直接结果，不是不一致）。
  姓名采交存串（OpenAlex display 为 `Md. Danish Eqbal` / `Mohd.Kaleem Khan`，标点有差）。**通讯作者：待确认**。
- 日期：Crossref created **2026-11-25T20:28:47Z**（**窗口内**）；published-print 2026-10（会期月份，不判窗）。
- 数字（**均为实验工况**，原句 "The experimental investigation is carried out at..."）：
  **6 条开口梯形微通道**；**去离子水**；**过冷度 20 °C**；**质量流速 535 kg/m²s**（单一取值）；**热流密度 20–220 W/cm²**。
  ⚠️ **降幅数字确认为零**：原文 "reduces wall temperatures compared to the conventional open microchannel (OTM) configuration without venting.
  Furthermore, the venting membrane effectively suppresses pressure drop, wall temperature fluctuations, and pressure fluctuations."
  —— **全是定性动词，无百分比、K、kPa 任何数值**。基准 = **同构的不带排汽膜的开口梯形微通道（OTM）**。
  技术要点：膜材 **PTFE**，位于开口通道**上方**，吸引汽塞并自通道顶面排出；设计目标 "mitigate flow instabilities without inducing additional pressure drop"。
  ⚠️ 立论前提「开口通道相对同水力直径闭式通道换热更好、流动不稳定性更低」**是文献综述口径，不是本文实测对比**，成稿勿张冠李戴。
- 本条印证「IEEE 摘要约 8 天后进 OpenAlex」的经验，且**更快**：created 11-25、11-28 已可取摘要。

---

## C 组 · 主代理补扫 4 条（Crossref 交叉核；详见 supplementary-sweep.md）
对 4 条补扫条目作 Crossref 复核，**修正了 OpenAlex 的 3 个日期与 2 个姓名**：

| DOI | Crossref created（判窗用） | OpenAlex created（晚 1 天，不用） | 判定 |
|---|---|---|---|
| `10.1109/ted.2026.3751611` | **2026-11-26T20:15:32Z** | 11-27 | 通过（窗内） |
| `10.1002/htj.70430` | **2026-11-25T18:00:18Z**（published-online 11-25） | 11-26 | 通过（窗内） |
| `10.32604/fhmt.2026.093483` | **2026-11-27T08:15:12Z** | 11-28 | 通过（窗内） |
| `10.1109/tpel.2026.3758090` | **2026-11-26T20:03:21Z** | 11-27 | 通过（窗内） |

- `ted.2026.3751611`：五位作者 Crossref `name` 均 `Huazhong University of Science and Technology`、`place` = `Wuhan, China`（删）、无 `department`
  → **华中科技大学**（原串无院系）。**通讯作者：两源均无标记 → 待确认。** Crossref 无 abstract，摘要取自 OpenAlex。page 1-7，无卷期。
- `htj.70430`：🔴 **姓名更正** —— Crossref 交存为 **`Hongqiang Ma`**，OpenAlex display 为 `H.X. Ma` → **采交存串 Hongqiang Ma**。
  单位原串（删城市后）：Lei Zhao / Cuiwei Liu = `College of Pipeline and Civil Engineering China University of Petroleum (East China)`；
  Xiaosong Cheng / Hongqiang Ma / Yulong Yang / Wei Cui = `School of Civil Engineering and Architecture East China Jiaotong University`
  （Hongqiang Ma 另挂 `Key Laboratory of Safety and Resilience of Civil Engineering in Mountain Area` → **按规则 3 删**）；
  Jiajun Wang = `School of Energy and Environment Southeast University`。
  **通讯作者三位已核**（OpenAlex `is_corresponding=true`）：**Xiaosong Cheng、Hongqiang Ma、Cuiwei Liu**。
  Crossref **有 abstract**（唯一一条），与 OpenAlex 还原一致。无卷期，文章号 htj.70430（Early View）。
- `fhmt.2026.093483`：🔴 **姓名更正** —— Crossref 交存第三位为 **`Yingying Zhang`**，OpenAlex 为 `Zhang Ying-yin` → **采交存串 Yingying Zhang**。
  ⚠️ **Crossref 完全未交存 affiliation**（四位全 `(none)`）→ 单位只能取 OpenAlex `raw_affiliation_strings`：
  Zhendong Li / Yu Wang / Yingying Zhang = `College of Urban Construction, Nanjing Tech University`（删 Nanjing, China）；
  Xiaolei Yuan = `Department of Civil Engineering, School of Energy Systems, LUT University`（删 Lahti, Finland）。
  **此事须写进备注。** **通讯作者 Yu Wang 已核**（OpenAlex `is_corresponding=true`）。volume 0 / issue 0 / page 1-10 → **尚无正式卷期**。
- `tpel.2026.3758090`：七位作者 Crossref `name` 均 `McMaster University`、`place` = `Hamilton, ON, Canada`（删）、无 `department`
  → **McMaster University**（原串无院系）。**通讯作者：两源均无标记 → 待确认。** page 1-15，无卷期。

---

## 本期不收 / 否决一览
- `10.1109/indin68935.2026.11802527`（两相浸没冷却高密度功率电子，UTS，created 11-27）：**摘要零获取** → 不编摘要，不收
- `10.1016/j.icheatmasstransfer.2026.113208`（狭缝射流冲击恒热流壁面 LBM，南方科技大学，created 11-26）：摘要零获取 + 标题为**通用射流冲击**算例、无芯片/冷板字面 → 按 2026-11-02 覆盖面裁定**不收**
- 电池热管理类（`10.1016/j.ijthermalsci.2026.111525`、`10.1080/01457632.2026.2762692`、`10.1016/j.icheatmasstransfer.2026.113239`、`10.1615/heattransres.2026065341`）：非电子/数据中心 → 不收
- arXiv `2611.32047`（Raspberry Pi 5 随机森林 + PCM 铜泡沫）：复核确认摘要**无液冷/冷板字样** → 不收
- 通用神经算子/PINN 七条（CoMNO 2611.32274、FMSNO 2611.30341、SPARK 2611.31834 等）：无电子散热字面 → 按裁定不收
- 大批 Elsevier in-press 标题级条目（**摘要零获取**，含上期挂账 15 条全部重试仍 null）：**一律不进正文**，转 open-items 与 excluded-numbers 第（八）类

## 本期角度覆盖缺口（进 PR 正文，不进刊物）
- **arXiv 整体未覆盖到窗口尾部**：scout C 实测 arXiv API 最大可见提交日为 **2026-11-25**（`submittedDate:[202611260000 TO 202611282359]` 返回 totalResults=0），
  11-26~11-28 三天**取不到、非「检了没有」**；scout A 的 arXiv 查询返回为空、scout B 的 arXiv 查询无可读结果 → **本期 arXiv 仅覆盖至 11-25**。
- **原位测量与表征**（2026-11-26 维护者增补的角度 A 要点：原位热阻、junction-to-coolant、嵌入式传感器、TIM BLT）：**窗口内未检出明确条目**。
- **InterPACK 2026 会后 DOI**：第 **5** 次零命中（ASME 前缀 10.1115 在 11-22~11-28 窗内仅 2 条，无 ipack）。
- **产业侧**：PRN 窗口内仅 1 条可收（Midea）；DCD、businesswire、globenewswire、se.com、ecolab.com 等均不可达。
