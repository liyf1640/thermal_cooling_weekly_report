# scout-B 回传 · 冷板制造工艺（原样存档）

窗口 2026-11-15 ~ 11-21，判窗用 Crossref `created`。

**结论：同行评审的冷板制造工艺论文（钎焊 / skived / FSW / ECAM / LPBF 冷板）本期未检出。**
有 2 条 THERMINIC 2026 会议论文勉强沾边，列为低置信度备选，两条都取不到摘要。

## 各入口实际查询与命中
### 1. Crossref works，`created` 窗口 + `query.bibliographic`，rows=8
（total 是相关度宽召回总数，不代表命中数）

| 关键词 | total | 窗口内与制造工艺 + 散热相关 |
|---|---|---|
| brazed cold plate | 554 | 0。靠前为 SSRN 冷板布局优化（ssrn.7693278，SSRN 不收）、brazed plate gas cooler（icheatmasstransfer.2026.113163，板式气冷器热力学，不涉工艺）、开放微通道热液优化（energy.2026.143202）、拓扑优化冷板流动均匀性（applthermaleng.2026.134045）。后两篇是热工/优化，不是制造工艺。 |
| skived fin | 84 | 1，即备选 1。其余为法语 "fin" 噪声。 |
| friction stir welding heat sink | 1239 | 0。均为 FSW 材料学或工艺、与散热无关（AA5052/6261 异种接头、ZE41 镁合金、泡沫铝）。ijhmt.2026.129934 是 FSW 的 CFD，不涉散热。 |
| diffusion bonding cold plate | 1181 | 0。msea.2026.151436（Cu-Cu 超低温扩散焊）、mssp.2026.111418（Cu/SiO2 混合键合）属材料/封装键合，无冷板依据。 |
| additive manufacturing cold plate | 1541 | 0。均为通用增材、材料或拓扑优化。 |
| laser powder bed fusion heat sink | 3113 | 1，即备选 2。其余为通用 LPBF 材料/粉末研究。 |
| micro-milling microchannel | 542 | 0。10.1007/978-981-95-5253-5_45-1 为 Springer 手册章节、不是工艺论文；SAE 2026-99-2516 是会聚-发散通道热工优化，不涉工艺。 |
| electrochemical additive manufacturing copper | 1683 | 0。无 ECAM / Fabric8Labs 相关新条目。 |
| manufacturing liquid cooling heat sink | 2674 | 0 个工艺类。ijhmt.2026.129924、tcpmt.2026.3754479 是热工设计，不是制造工艺。 |

### 2. arXiv（`export.arxiv.org`）：窗口内 0 条
- 查询一 `all:"cold plate"` AND (brazing / additive / friction stir / skived / powder bed / milling)，按投稿日降序：
  最新三条为 2024-08-25、2023-10-05、2012-10-13 → 窗口内零。（先遇 "Rate exceeded"，重试一次才拿到结果。）
- 查询二 `all:"heat sink"` AND (additive manufacturing / powder bed / skiving / friction stir)：最新一条 2025-01-10 → 窗口内零。
- ⚠️ 第三条 `electronics cooling AND fabrication` **被限流，未得到结果，未覆盖**。

### 3. Crossref 10.1109 前缀（ECTC / ITherm / THERMINIC / ESTC 等），窗口 + `query.bibliographic`，rows=6

| 关键词 | total | 说明 |
|---|---|---|
| cold plate | 19 | 与冷板制造无关（Heatspreading from a Small Source on a Thick Plate 是传热建模，其余噪声）。 |
| heat sink | 39 | 命中 **THERMINIC 2026 一批**：AI 几何优化、SLA 氧化铝陶瓷热沉、泡沫金属倾斜板热沉、螺栓接触热导建模，另有备选 1 和 2。 |
| liquid cooling | 56 | 浸没冷却、两相冷却，与制造工艺无关。 |
| thermal management electronics packaging | 1148 | 仅看前 6 条，均为 ESTC / THERMINIC 封装热管理，无冷板制造。 |

- 🟢 **整个窗口内没有 ECTC、ITherm、SEMI-THERM 的 DOI。10.1109 前缀下只有 THERMINIC 2026（created 2026-11-19 批量上线）、ESTC 2026、EPEPS 2026。**
- ⚠️ THERMINIC 论文 Crossref `published` 为 2026-09、`created` 为 2026-11-19 → **按 created 判窗属本期窗口内上线**。

### 4. InterPACK 挂账项：10.1115 前缀 429 条，0 条 `ipack2026-*`，**第 4 次复查仍零命中**

## 低置信度备选（均无摘要）
**备选 1 · skived 热沉流量再分配**
- Enabling Flow Redistribution in Skived Heat Sinks for High-Power Density Computing: An End-to-End Case Study
- THERMINIC 2026（32nd Int. Workshop on Thermal Investigations of ICs and Systems），proceedings-article，IEEE
- DOI 10.1109/therminic70452.2026.11779752；Crossref created **2026-11-19**（`published` 2026-09）
- 作者与单位（Crossref 原串）：Ine Vandebeek、Lieven Vervecken、Rui Vieira，均为 **MegaCool Technologies**
- 摘要未取到（Crossref 无 abstract，fetch_source 也只有元数据）。关键数字：无。
- 覆盖面依据：仅标题字面 "Skived Heat Sinks"、"High-Power Density Computing"
- 置信度中低：散热相关成立，但是否涉及 skiving 加工工艺还是只做流场再分配设计，**无摘要无法判断**；作者单位是企业，留意厂商稿倾向。
- 去重：skived 为已覆盖工艺，但此 DOI 不在已报清单，按新增处理。

**备选 2 · LPBF 铜-石墨烯复合材料强化传热**
- Laser Powder Bed Fusion of Copper-Graphene Metal Matrix Composites for Enhanced Heat Transfer
- 同上 THERMINIC 2026；DOI 10.1109/therminic70452.2026.11779771；created **2026-11-19**（`published` 2026-09）
- 作者与单位（Crossref 原串）：Wessel W. Wits、Hyunjong Lee、Leonore van Goor、Bernard Geurts，
  单位 "Mathematics and Computer Science University of Twente"；Davoud Jafari，单位 "University of Twente"
- 摘要未取到。关键数字：无。覆盖面依据：仅标题字面 "Enhanced Heat Transfer"
- 置信度低：偏材料/工艺，是否明确面向热沉或冷板未知 → **无摘要证实则建议丢弃**
- 去重：LPBF 为已覆盖工艺，但此 DOI 不在已报清单，按新增处理。

## 需说明的未覆盖项
- arXiv 第三条查询被限流，未得到结果。
- SEMI-THERM 未单独查前缀（10.1109 前缀窗口内没有任何 SEMI-THERM 条目）。
- **OpenAlex 单篇端点未使用**——理由是备选 1、2 的 Crossref 记录本身没有摘要。
  ⚠️（主代理注：此推理有误。本期 3751185 与 3754479 两条正是 Crossref 无摘要而 OpenAlex 单篇端点有，已令其回头补试。）

---

# scout-B 补充回传 · THERMINIC / ESTC 2026 整批 + OpenAlex 摘要 + arXiv 设计一路

**结论**
- 制造工艺角度本期仍无合格论文候选（无取到摘要的钎焊/skived/FSW/ECAM/LPBF 冷板论文）。
- THERMINIC 两条工艺相关条目（skived、LPBF Cu-Graphene）**OpenAlex 摘要均 null**，覆盖面无法证实，保持低置信度备选。
- THERMINIC 里有一批冷板/微通道/液冷设计与建模论文，**已取到摘要的见下**（属设计/仿真角度）。
- arXiv 设计一路重试后成功，窗口内只有 1 条冷板相关（2611.21707）。

## 任务 1：整批枚举
- 方法：Crossref `prefixes/10.1109/works`，created 窗口 11-15~11-21，`query.bibliographic=therminic estc thermal`，
  rows=100，offset 翻 0–2000 共 21 页，再按 DOI 含 `therminic` / `estc` 过滤。
- 结果：**THERMINIC 92 条、ESTC 182 条**（含 Front Matter / Author Index / Session Schedule 与会议根条目）。
  **该批 `created` 全部落在 2026-11-17（ESTC）与 2026-11-19（THERMINIC）。**
- ⚠️ 覆盖限制：这是相关度检索 + 翻页，**不是穷举**，不保证完整。
- DOI 后缀范围：THERMINIC `10.1109/therminic70452.2026.`11779729–11779819；ESTC `10.1109/estc68880.2026.`11778931–11779409。

### THERMINIC 2026 中与冷板/液冷/微通道/热沉/功率器件散热相关的条目（DOI 后缀）
11779729 Vapor Chamber 热传导数值模型对比 ｜ 11779730 四面体点阵芯层层流热水力 ｜ 11779731 倾斜板热沉 + 泡沫金属翅 + PCM ｜
11779733 石墨烯增强热沉 ｜ 11779736 IGBT 模块参数化 MOR ｜ 11779739 竖向流动沸腾的进出口与通道设计 ｜
11779742 混合浸没冷却服务器的上区局部取热与热分层控制 ｜ 11779745 AI 驱动非参数几何优化热沉 ｜
11779746 厚板上小热源的热扩展 ｜ 11779750 SLA 制氧化铝陶瓷热沉（宽禁带器件）｜ 11779752 skived 热沉流量再分配 ｜
11779754 半导体开关热建模的参数化 MOR 验证 ｜ 11779756 两种递增密度热沉的流动沸腾不稳定性实验对比 ｜
11779760 铝-氨热管用于大功率电子冷却 ｜ 11779765 底面冷却封装的结-壳热阻测量方法 ｜
11779768 CuBricks：功率半导体的竖向介电浸没冷却 ｜ 11779769 小型嵌入式 MOSFET 半桥功率模块的流动沸腾冷却 ｜
11779771 LPBF 铜-石墨烯 MMC ｜ 11779772 数据中心服务器空气放大器冷却能力试验台 ｜ 11779773 SiC 功率模块热 ROM ｜
11779774 向全直接液冷服务器架构过渡的热水力实验 ｜ 11779775 直接冷却功率模块扩展热阻的集总参数模型实验验证 ｜
11779776 热磁脉动热管「冷却兼发电」｜ 11779785 顶面冷却功率器件 TIM 间隙垫的热-机耦合表征 ｜
11779787 小型化环路热管热水力分析 ｜ 11779788 HPC 封装翘曲致热性能退化实验 ｜
11779791 方形针肋微通道热沉热水力数值研究 ｜ 11779794 多芯片功率模块两相微通道冷却瞬态 CFD ｜
11779804 螺栓连接电子封装-热沉接触热导的空间变化建模 ｜ 11779806 两相方案不同冷却概念的冷却行为评估 ｜
11779807 PCM 集成热沉集总参数建模 + 实验验证 ｜ 11779808 超临界 CO2 作热扩展器工质 ｜
11779810 新型包封 HPC 封装的工艺实现与验证 ｜ 11779811 最优针肋几何为何依赖工况点：正弦针肋的分离分析 ｜
11779817 不锈钢热虹吸与脉动热管热性能对比

### ESTC 2026（182 条）里与散热相关的
11778937 封装级非均匀加热下热扩展原位研究（chiplet 架构 / TIM / CUF；作者 Resonac + imec，Crossref 原串）｜
11778957 功率电子模块热-机械 FEM 的数值稳定 ROM 加速 ｜ 11778975 直接接触铜柱 + 单片集成微流道玻璃封装 ｜
11779245 TIM 厚度对分立功率封装电热行为的影响 ｜ 11779285 领域定制 CNN 加速先进封装热原型 ｜
11779390 WaLTIS 晶圆级热界面叠层（近结热管理）｜ 11779286 小过孔高散热 PCB 严苛热循环可靠性 ｜
11779351 完整 chiplet 封装热机可靠性的降阶建模
其余主要是键合、烧结、玻璃基板、RDL、可靠性，与冷板无关。**以上多数未逐条读摘要，仅凭标题，属「标题级线索」。**

**整批里没有任何一条标题明示钎焊 / FSW / ECAM / 扩散焊 / 微铣削冷板。**
与制造工艺沾边的仅 11779752（skived）、11779771（LPBF Cu-Graphene）、11779750（SLA 氧化铝陶瓷热沉）。

## 任务 2：OpenAlex 单篇端点取摘要（逐条试，间隔 3 s，全部 HTTP 成功）

### 🟢 取到摘要
**(a) 10.1109/therminic70452.2026.11779791 · Thermo-Hydraulic Performance of Microchannel Heat Sinks with Square Pin-Fin Geometries: A Numerical Investigation**
- 作者与单位（OpenAlex `raw_affiliation_strings`，**只读到前 7 位**）：
  Ashraf Morsi（Alexandria University, Egypt）；Mohammed Abdel Razzaq（Texas Institute for Electronics, UT Austin, USA）；
  Youssef Khalid（Cairo University, Egypt）；Mohamed Naser（Alexandria University）；
  Mohamed Atif Elkholy（Menoufia University, Egypt）；Ibrahim Osama Elhagali（POWERlab, EPFL, Switzerland）；
  Osama M. Maklad（School of Engineering, University of Greenwich, UK）
- 关键数字（摘要）：三维 CFD，多入口微通道热沉，工质 **25% 丙二醇水溶液（PG25）**；
  **五入口 + 方形针肋基准工况 HTC 26,452 W/(m²·K)、压降 128.5 Pa、泵功 0.001646 mW/mm²**；
  **新型设计 Novel 1 HTC 41,975 W/(m²·K)，比基准提高 40.2%**，泵功显著增加；**孔洞 + 长宽比修改的设计 HTC 提高 5.1%**。
- 覆盖面字面依据：摘要结尾 "provide guidelines for the design of high-performance microchannel **cold plates**"
- 性质：纯数值设计，**不属制造工艺**，属设计/仿真角度。Crossref created 2026-11-19。

**(b) 10.1109/therminic70452.2026.11779794 · Transient CFD Modelling of Two-Phase Microchannel Cooling in a Multi-Chip Power Module**
- 作者与单位（OpenAlex 原串）：Sadegh Sadeghi（Aalborg University, Denmark）；Amir Sajjad Bahman（Aalborg University, Denmark）
- 关键数字（摘要）：三芯片功率模块，**每芯片 190 W**，亚冷 **R134a** 流经矩形微通道；
  **沸腾起始约 0.04 s**；运行 **0.15 s** 后**两相热阻 0.055 K/W、单相 0.09 K/W**；
  **压降 6.2 → 6.5 kPa**；**出口液温 22.4 °C（两相）对 23.2 °C（单相）**。
- 覆盖面依据：摘要 "two-phase microchannel cooling in a multi-chip power module"。纯 CFD。Crossref created 2026-11-19。

**(c) 10.1109/therminic70452.2026.11779775 · Experimental Validation of a Lumped Parameter Thermal Model for Spreading Resistance in Direct-Cooled Power…**
- 作者与单位：**未读取**（仅取了摘要）。
- 关键数字（摘要）：液冷铜热沉，局部热源代表功率半导体裸片；模型能复现定性趋势，
  但**仿真与实测偏差最大达 3 倍**，作者结论为该模型**不足以定量预测热阻**。
- 覆盖面依据：摘要 "liquid-cooled copper heat sink subjected to a localized heat source representative for a power semiconductor die"
- 性质：**负面结果**，对冷板建模有直接参考价值。

**(d) 10.1109/estc68880.2026.11778957**（功率电子模块热-机械 ROM 加速）
- 摘要前 1100 字符：RK-BSOAR（有理 Krylov 子空间块二阶 Arnoldi）做 MIMO 降阶，面向功率循环下热-机械耦合。
  **只读到方法描述、没有性能数字**，摘要后半截断未再取。覆盖面：与冷板关系弱（无冷板设计内容）。

### 取不到（`abstract_inverted_index` 为 null，HTTP 成功）
11779752（skived，MegaCool）｜ 11779771（LPBF 铜-石墨烯，Twente）｜
11779745（AI 非参数几何优化热沉；⚠️ **Crossref 元数据未核实单位，Synopsys 之说待确认**）｜
11779773（SiC 功率模块热 ROM）｜ 11779736（IGBT 参数化 MOR）｜ 11779774（全直接液冷服务器架构实验）｜
11779769（嵌入式 MOSFET 半桥流动沸腾）｜ 11779730（四面体点阵芯层）｜ 11779733（石墨烯增强热沉）
**其余条目未逐条试 OpenAlex（时间与 token 所限）。**
skived 与 LPBF 两条无摘要、不能用标题推内容 → **建议不收**。

## 任务 3：arXiv 设计一路（重试后成功）
7 个组合均跑通（先遇 "Rate exceeded"，等 10 s 重试成功），按投稿日降序取 6 条：

| 查询 | 窗口内命中 | 最新一条投稿日（窗外） |
|---|---|---|
| `all:"cold plate"` | **1 条：2611.21707（2026-11-16）** | — |
| `all:"microchannel heat sink"` | 0 | 2026-10-12（2610.16716，**已报**） |
| `all:"manifold microchannel"` | 0 | 2026-11-07（2611.10666） |
| `all:"jet impingement" AND all:chip` | 0 | 2023-10-18 |
| `all:"topology optimization" AND all:"heat sink"` | 0 | 2026-07-30（2607.28534） |
| `all:"two-phase" AND all:"cold plate"` | 0（返回空） | — |
| `all:"electronics cooling"` | 0 | 2026-11-10（2611.14363） |
未加 `cat:` 分类过滤。窗口内唯一候选即 **arXiv:2611.21707（EJBench）**，与 scout C 所报同一条。

## 其他
- InterPACK `ipack2026-*` 第 4 次复查零命中（10.1115 前缀 429 条全是 pvp2026-*，另 1 条 1.4072771 与散热无关）。
- 上轮 Crossref 工艺关键词与 arXiv 工艺词扫描结论不变：**钎焊 / skived / FSW / 扩散焊冷板 / ECAM / LPBF 冷板 / 微铣削
  均无窗口内、能证实与散热相关的同行评审论文。**
