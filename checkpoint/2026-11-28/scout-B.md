# scout-B · 冷板制造工艺（原样回传）

总体结论：窗口内严格新增的强相关候选只有 1 条（候选 1）。缺口三项（钎焊/skived/FSW）窗口内无擅长企业或冷板专论新文。

## 一、窗口外、但摘要已重试取到的 THERMINIC 三条（created 2026-11-19，第 14 期未报）

### 补 1 · skived 热沉 SmartFins 流动再分配（缺口项：skived）
- 标题：Enabling Flow Redistribution in Skived Heat Sinks for High-Power Density Computing: An End-to-End Case Study
- 作者/单位：Ine Vandebeek；Lieven Vervecken；Rui Vieira。OpenAlex 未给任何单位 → 单位待确认。
- 内容：SmartFins 框架把「按热流分布优化的流动再分配」与「面向减材的生成式设计」结合，保留整块铜的减材 skived 制造路线。CHT 仿真 + 3 个设计的实验验证。摘要未点名企业。
- 关键数字（摘要）：封装热流 >200 W/cm²，局部热点接近 600 W/cm²；优化设计相对一款商用参考件热阻降低 47%。
- URL：https://doi.org/10.1109/therminic70452.2026.11779752
- 日期：Crossref created 2026-11-19；会议日期 2026-09-01
- 摘要途径：OpenAlex 单篇 DOI 端点，摘要完整
- 相关性：强（skived 冷板，缺口项）。可能的「skived 擅长企业」线索，但未能核实。

### 补 2 · LPBF 铜-石墨烯复合材料
- 标题：Laser Powder Bed Fusion of Copper-Graphene Metal Matrix Composites for Enhanced Heat Transfer
- 作者/单位：Wessel W. Wits、Hyunjong Lee、Leonore van Goor、Bernard J. Geurts、Davoud Jafari，均为 University of Twente（OpenAlex）
- 内容：机械混合制 Cu-Gr 复合粉 + LPBF；研究石墨烯与工艺参数对组织、致密度、热导率的影响
- 关键数字：**摘要无定量数字**。定性结论：加入石墨烯可恢复纯铜 LPBF 过程中损失的热导率
- URL：https://doi.org/10.1109/therminic70452.2026.11779771
- 日期：created 2026-11-19
- 相关性：中（材料层面，不是冷板整件）

### 补 3 · SLA 氧化铝陶瓷热沉
- 标题：Experimental and Numerical Investigation of an SLA-Manufactured Alumina Ceramic Heat Sink for Wide-Bandgap Power Modules
- 作者/单位：Lucie Teulet、Jean-Pierre Fradin、Ahmad Batikh、Alexandre Marie、Benjamin Périé、Virgile Puel（均 Institut Catholique d'Arts et Métiers）；Emmanuel Marcault、Lucile Mage（CEA）；P. Tounsi（CNRS / LAAS / Université de Toulouse）
- 内容：首次对 SLA 增材氧化铝陶瓷热沉做热工与水力实验，并与 ANSYS Fluent 仿真对比
- 关键数字：**摘要无定量数字**；仿真对热阻与压降趋势吻合，偏差归因于制造公差、材料属性、测量不确定度
- URL：https://doi.org/10.1109/therminic70452.2026.11779750
- 日期：created 2026-11-19
- 相关性：中

## 二、窗口内候选

### 候选 1 · 增材制造多通道冷板减重（LPBF + SLS，集成歧管 + 晶格）
- 标题：Weight Reduction and Thermal Performance Validation of a Multi-channel Cooling Plate Using Additive Manufacturing
- 作者/单位：Hanwha Systems（OpenAlex 与 Crossref 均把它列在作者栏，**疑似单位被误解析**）；Hyun-Woo Jeong；Se-Jin Yoon；Jae-Hun Heo。各人单位待确认。
- 内容：为高热流武器系统设计轻量冷板，用 L-PBF 与 SLS 制造集成歧管加内部晶格结构，并与传统减材制造对比
- 关键数字（摘要）：最高温度比传统制造模型低 1.0 °C；质量 5.3 kg → 4.4 kg，降幅 16.9%
- 刊/日期：Journal of the Korean Society of Manufacturing Process Engineers；Crossref created 2026-11-23（published 2026-11-30 为期次日期，不作判窗依据）
- URL：https://doi.org/10.14775/ksmpe.2026.25.11.165
- 摘要途径：OpenAlex 英文摘要（fetch_source 与 Crossref 均无）
- 相关性：强。注：降温仅 1.0 °C，价值主要在减重；SLS 用于金属还是其他材料摘要未说，需核。
- 核验状态：仅摘要（未读全文）

### 候选 2 · 金刚石/铜复合热沉板纳秒激光加工
- 标题：Material removal characteristics of diamond/Cu composite heat sink plate in nanosecond pulsed laser machining
- 作者/单位：Jia-wan Peng（Guangdong University of Technology；Guangdong Mechanical & Electrical Polytechnic）；Fenglin Zhang、Jian Zheng、Guo-Tao Pan（Guangdong University of Technology）；Xiao-yi Pan（China Nonferrous Metal Mining）；Yu-Mei Zhou（Guangdong Polytechnic Normal University）。OpenAlex 单位解析可能有误。
- 内容：**只有标题。摘要零获取**（Crossref、OpenAlex 均 null，ScienceDirect 不可达）
- 刊/日期：Optics & Laser Technology；created 2026-11-23
- URL：https://doi.org/10.1016/j.optlastec.2026.117107
- 相关性：弱到中（热沉基板材料加工，非冷板结构制造）

## 三、窗口内扫到但建议不收
- 10.21203/rs.3.rs-11206118/v1：W/CuCrZr 高熵合金钎料钎焊，Research Square 预印本，created 11-23。1000 °C 保温 20 min，剪切强度 247 MPa。Anhui Polytechnic University 等。属聚变面向等离子体部件，与电子冷板关联弱 + 未评审。
- 10.1002/jtse.70014：LTCC 微通道热沉 + 嵌入金属针肋（Wiley，created 11-27）→ 工艺角度弱，转角度 D。
- 10.1016/j.icheatmasstransfer.2026.113259：热沉集流腔 + TPMS 芯体两阶段拓扑优化，created 11-27，摘要零获取，属优化角度。
- 10.1016/j.ijthermalsci.2026.111525、10.1080/01457632.2026.2762692：电池冷板流道/设计优化，非制造工艺。

## 四、缺口三项与扫描范围
- 钎焊 / skived / FSW：窗口内 Crossref 无冷板专论新文；FSW 命中全是通用焊接材料论文。
- 厂商侧仅存量营销页、无窗口内新闻：Stirweld（FSW 设备）、Wakefield Thermal、Eaton、Radian Thermal（skived 微翅冷板）、Wieland —— 营销落地页，不作候选。
  Stirweld 有一篇厂商文章「Copper cold plates: which joining process to prioritize among FSW, vacuum brazing, and laser?」（https://stirweld.com/?p=267315），无日期、非窗口内一手新闻，仅线索。
- 扫描源：Crossref created 过滤（11-22~11-28）下 10 组英文 query（cold plate / brazing / skived / FSW / AM / LPBF / diffusion bonding / ECAM / micro-milling）+ 2 次 WebSearch。
- arXiv API 无可读结果 → arXiv 方向本期未检出，不能排除漏检。
- ITherm / ECTC / SEMI-THERM / InterPACK / ESTC 窗口内无新条目；THERMINIC 的 IEEE 条目 created 在 11-19，不在窗口内。
