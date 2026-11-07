# 第 12 期 学术侧 对抗式核验报告

证据通道：Crossref 单篇端点取 `created`/作者/`affiliation`/卷期；OpenAlex 单篇端点取 `raw_affiliation_strings`/`is_corresponding`/
`abstract_inverted_index`（verifier 自行反演，未照抄 scout 转述）。
**本会话新增不可达域名（与既往记录不符，须记档）**：`www.mdpi.com`（connect_rejected + DNS 不解析）、`kirj.ee`（connect_rejected）、
`link.springer.com` → 303 到 `idp.springer.com`（DNS 不解析）。**故 MDPI 全文、爱沙尼亚科学院 PDF、Springer 文章页本期均读不到。**

## A1 · 10.2139/ssrn.7670126 —— 通过（2 项待确认须随稿标注）
- 完整标题：`Orientation-dependent flow boiling in rigid-tail micro-pillar array channels: Thermal-hydraulic performance and bubble transport mechanisms`
- 作者顺序（Crossref）：Zheng Weng(first) / Shuaihua Ma / Zheng Li / Yuang Jiang / Mei Lin / Qiuwang Wang
- 单位：Crossref 六位全为空数组。OpenAlex raw：Mei Lin、Qiuwang Wang → `Xi'an Jiaotong University (XJTU), Xi'an, China`；
  **Zheng Weng / Shuaihua Ma / Zheng Li / Yuang Jiang → 空数组 → 待确认**（SSRN 全文域名不可达，不以同篇合作者单位代入）
  上站写法：Mei Lin、Qiuwang Wang → **西安交通大学**（原串无院系）；其余四位标「单位待确认」
- 通讯作者：**Mei Lin**（`is_corresponding=True`，唯一）
- `created` **2026-10-25T16:17:10Z** → 窗内。`posted-content`，Elsevier BV 托管 SSRN **预印本（未同行评审）**，`posted` 只到年份 2026
- 数字（全部命中原文）：
  - 原文 `Compared with the horizontal configuration, the vertical channel generally exhibits lower wall temperatures, higher HTC, and lower pressure drop. At a representative condition, for example, the average wall temperature falls by 1.49 K and the total pressure drop by 20.2%`
    → **基准 = 水平（0°）配置**；⚠️ **「representative condition」的质量流速与热流摘要完全未给** → 成稿只能写「某一代表性工况下」
  - 原文 `at low mass flux, the thermal-hydraulic performance factor at 90° reaches approximately 4.5 times that at 0°`
    → **「约（approximately）」确为原文措辞**；⚠️「低质量流速」具体数值未给 → 待确认
  - 工质 **PFO-50**、方位 **0°/45°/90°** ✅；**修正 Froude 数**确有引入（`characterize the competition between buoyancy and imposed-flow inertia`），
    且原文称**压降收益与该竞争的相关性比 HTC 提升更一致**
  - 可用定性（scout 未报）：垂直运行使**气泡脱离尺寸减小、脱离频率升高、尾板附近滞气时间缩短**，支持「连续剪切 continuous-shearing」机制
- **实验**（`This study experimentally investigates`；含高速气泡追踪、壁温/HTC/压降测量）
- **与姊妹篇 129752 不构成重复报道**：① 129752（`...flexible tails`，created 2026-10-19，IJHMT 273/129752）**从未上站**（仅见 open-items 挂账）；
  ② 两篇非同一文的两个版本：作者名单不同（129752 为 Shuaihua Ma 第一，含 Lei Xie、Wenxiao Chu，无 Zheng Li / Yuang Jiang）、
  对象不同（**flexible tails 柔性尾板 vs rigid-tail 刚性尾板**）、自变量不同（129752 无方位角研究）、载体不同（期刊 vs SSRN 预印本）
- 未取到：四位作者单位、代表工况角点、「低质量流速」数值

## A2 · 10.1016/j.ecmx.2026.102444 —— 通过（1 项口径须照原文含糊写）
- 完整标题：`Comparative thermo-hydraulic assessment of monolithic, hierarchical, hybrid, and functionally graded TPMS heat sinks: Flow reorganization and hotspot mitigation for high-heat-flux applications`
- 作者两位同串：Dame Alemayehu Efa、Dejene Alemayehu Ifa →
  `School of Mechanical Engineering, Institute of Technology, Wallaga University, P.O. Box 395, Nekemte, Ethiopia`
  **校名字面经核为 `Wallaga University`**（非 Wollega/Wollaga）。上站：**Wallaga University 机械工程学院**（埃塞俄比亚）；
  **无通行中译，建议保留英文校名**，不自造「瓦拉加大学」
- 通讯作者：**Dame Alemayehu Efa**（`is_corresponding=True`）
- `created` **2026-11-03T17:13:11Z** → 窗内。*ECM: X* **vol 32, 文章号 102444**，`published` 2026-12（判窗不用）；OA gold
- **覆盖面硬证据**：摘要**第一句**即 `High-power electronics require heat sinks with excellent thermal–hydraulic performance.` → 明确电子散热，覆盖面成立
- 数字（全部命中）：
  - FG-H 由 **Lidinoid、Split-P、Diamond 沿壁面法向、背离热源方向依次堆叠**，**恒定孔隙率 82.2%**
  - 三个对照基线：**monolithic Diamond (M−D)**、**hierarchical nested Diamond (H-ND)**、**heterogeneous hybrid (H-H)**
  - **三维共轭传热仿真**、**经验证的 SST k–ω**、**Re 2,000–16,000**、**128 个采样面**
  - **Re=10,000：Nu=31.93（最高）、压降 236 Pa（最低）、PEC=1.75（最优）**，口径为 `compared with the other baseline designs`
  - **相对 M−D 基线**：水力损失**少 52.80%**、冷却性能**好 14.3%**、**平均场协同因子 2.61 倍**、熵**减 6.43%**、温度不均匀性**降 71.4%**（原文 `than the M−D baseline`）
  - ⚠️ **「14.3% better cooling performance」的物理量摘要未给** → 只能照原文含糊写，**不得解释成换热系数或温降**
  - 性能总排序 **FG-H > H-H > M−D > H-ND**
- **纯 CFD**：摘要只称湍流模型 `validated`，**未提作者自建实验台、未说明验证对象** → 写「仿真（湍流模型经验证，验证对象摘要未给）」，不可写「有实验验证」
- 未取到：全文；摘要为 **OpenAlex 单通道**（Crossref 无 `abstract` 键），无第二通道交叉验证

## A3 · 10.3390/mi17111225 —— 待确认（74.5% 基准读不到）＋ 建议线索条、不作论文卡
- 完整标题：`Coupled Multiphysics Optimization of Ball Grid Array with Microchannel Heat Dissipation`
- 完整作者 5 位：Yuqing Dong / Gang Nan / Zhihui Xie / Zhuoqun Lu / **Yanlin Ge**
- 单位原串（Crossref）：Dong、Nan、Xie → `College of Power Engineering, Naval University of Engineering, Wuhan 430033, China`；
  Zhuoqun Lu → 同上 ＋ `School of Energy and Electromechanic Engineering, Hunan University of Humanities, Science and Technology, Loudi 417000, China`；
  Yanlin Ge → `Institute of Thermal Science and Power Engineering, Wuhan Institute of Technology` ＋ `School of Mechanical & Electrical Engineering, Wuhan Institute of Technology, Wuhan 430205, China`
  上站：海军工程大学 动力工程学院；Lu 另 Hunan University of Humanities, Science and Technology 能源与机电工程学院；Ge → 武汉工程大学 机械与电气工程学院
- 通讯作者：**Zhihui Xie 与 Yanlin Ge**（两位 `is_corresponding=True`）
- `created` **2026-10-26T04:07:18Z** → 窗内。*Micromachines* **17(11), 1225**，`published` 2026-10-25
- 数字：
  - **7.8 K** ✅ 但口径须正：原文 `the difference between the maximum and minimum values of the maximum temperature is 7.8 K`
    —— 是**全部算例中「最高温度」这一指标的极大值与极小值之差**，**不是某两方案的温差**
  - **5.88×10⁻³ mm** ✅ 同理为最大变形指标的极大值与极小值之差
  - **74.5%** ⚠️ **待确认**：原文仅 `with a maximum reduction ratio of 74.5%`，**降低的是什么量、相对什么基准摘要未交代**。
    verifier 的自洽推算（挂在最大变形上）**属推算、不是原文出处 → 不得上站**。MDPI 全文不可达 → **该数字本期不可用**
  - 「矩形环形布局最优」→ 原文措辞**内部不一致**：摘要前段 `rectangular-ambulatory type`、结论句 `rectangular-loop layout`；另两类为 `array` 与 `staggered`。
    结论成立：`the rectangular-ambulatory type consistently yields the lowest maximum temperature and maximum deformation for all long/short half-axis ratios`
  - 构造理论 ✅；设计变量 = 焊点长短半轴比 + BGA 布局，约束 = 焊点总数与总体积
  - 其他可用：三种布局下最高温度随长短半轴比单调上升、最大变形单调下降；权重比 7:3 时存在最优长短半轴比；权重比变化不改变最优布局
- **纯数值**，无实验
- **覆盖面存疑偏弱 → 线索条**：摘要自述 `To investigate and improve the thermo-mechanical performance of BGA solder joints under steady-state conditions,
  a thermo-mechanical coupling model of a BGA packaging chip **under microchannel-forced liquid cooling** is established`
  —— 微通道强制液冷是**给定边界条件**，优化对象是**焊点形状与布局**；摘要**无任何一句以微通道冷却结构本身为研究对象**（无通道几何、无流量/压降、无冷板优化）

## A4 · 10.1063/5.0353789 —— **否决（覆盖面外）**
- 完整标题：`Flow dynamics mechanisms and thermal hydraulic performance evaluation of triply periodic minimal surface (TPMS) heat exchangers`
- 完整作者 5 位（无遗漏）：Zhenwei Zhang / Qinghai Zhao / Yunyi Ma / Hangyu Sun / Yu Chen
- 单位：五位同串 `College of Mechanical and Electrical Engineering, Qingdao University, Qingdao 266071`；Zhao 另有国家工程研究中心（按规则不写）
  → 上站（若收）**青岛大学 机电工程学院**
- 通讯作者：**Qinghai Zhao**；`created` **2026-11-02T09:26:02Z**（= published-online），*Physics of Fluids* **38, 115101**
- 数字（均命中，留档）：5 种 TPMS（Primitive/IWP/Gyroid/Diamond/FRD）对比**传统 PCHE**、同几何尺寸、**孔隙率 70%**、**Re 500–3000**、
  CFD + **增材样件实验验证**；**Re=500 时 FRD 总换热量 +69%、总传热系数 +78%（基准 = 传统 PCHE）**；归一化压降 **IWP 8.6 Pa/W ～ FRD 34.3 Pa/W**
- 🔴 **否决理由**：摘要中涉及电子散热的文字**只有末句应用展望**，逐字引证：
  `These findings clarify the topology-flow-thermal relationship of TPMS HX and provide physical guidance for the design of compact
  liquid-cooling systems, particularly for applications such as electronic cooling and battery thermal management.`
  对象是**通用换热器**，基准是 **PCHE**，工况以 Re 表征，**无热流密度、无芯片/热源设定、无电子算例** → 属「展望里泛提一句」，按闸门不计入覆盖面

## A5 · 10.1016/j.ijheatmasstransfer.2026.129770 —— 通过（定性卡，摘要无任何性能量值）
- 完整标题：`Flow boiling behavior of R1233zd(E) in embedded silicon microchannel heat sinks: Flow visualization, heat transfer and pressure drop`
- 作者（以 Crossref 为准）：Huigang Wang / Thanh Hoang Phan / Chirag R. Kharangate（OpenAlex 作 Thanh-Hoang Phan）
- 单位：Crossref 三位全空；OpenAlex raw 三位**同串** `Department of Mechanical and Aerospace Engineering, Case Western Reserve University, 10900 Euclid Avenue, Cleveland, OH, 44106, USA`
  → 上站 **凯斯西储大学 机械与航空航天工程系**
- 通讯作者：**Chirag R. Kharangate**（`is_corresponding=True`）
- `created` **2026-10-27T23:31:55Z** → 窗内。IJHMT **273, 129770**。
  （注：OpenAlex `created_date` 为 2026-08-27，比 Crossref 早两个月 —— 又一例 OpenAlex 日期不可用于判窗）
- 摘要已补全，逐条核：
  - **4 个硅微通道热沉，通道宽 100/150/200/300 µm，深恒为 100 µm**
  - 手段：**红外热像测壁温 + 高速可视化 + 结合流体压力温度算局部 HTC**
  - **泡状/塞状/环状（bubbly, slug, annular）**流型
  - `Increasing heat flux promotes an earlier onset of nucleate boiling (ONB), enlarges the boiling region, and accelerates the transition of flow regimes`
  - `In contrast, increasing mass flux delays boiling inception and shifts the boiling region downstream` —— **两个自变量方向相反，成稿勿合并**
  - **压力驱动闪蒸**原文为 `Pressure-driven flashing is observed under high mass flux conditions and gradually weakens with increasing heat flux
    and is replaced by nucleate boiling` —— scout 漏了后半句，**须补**
  - `only a minor influence on the average heat transfer coefficient under two phase conditions, whereas the pressure drop increases
    significantly with increasing mass flux and channel width`
  - 另：局部 HTC 高度依赖热流；质量流速与通道宽度主要影响 **ONB 位置**与局部 HTC 分布
  - 覆盖面明确：`providing valuable experimental guidance for the design and optimization of microchannel heat sinks for **two-phase electronics cooling**`，开篇亦为 `high-power electronic devices`
- **实验**（`flow boiling experiments are conducted`）
- **可引用量值：除通道几何外，摘要无任何性能量值** —— 无 W/cm²、无 kW/(m²·K)、无 kPa、无质量流速数值 → 只能作定性/机理条
- 未取到：全文量值区间；摘要为 OpenAlex 单通道

## A6 · 10.1109/tcpmt.2026.3742181 —— 通过（⚠️ 标题须改、1 条事实须改、通讯作者待确认）
- 🔴 **完整标题（字面，必须用这一版）**：
  `Dynamic startup characteristics of a dual-evaporator cooling loop for electronic thermal management with unequal heat load`
  （Crossref 与 OpenAlex 完全一致。scout 版本缺 `Dynamic`、`Start-up`→`startup`、`electronics`→`electronic`，且**整段漏掉 `with unequal heat load`**）
- 作者：Ruixue Yang(first) / Chengcheng Fan / Zhiheng Zhu / Chengbin Zhang
- 单位：Crossref 四位均为 `{"name":"Southeast University","place":["Nanjing, PR China"],"department":["School Of Energy And Environment"]}`；
  OpenAlex raw 四位均为裸串 `Southeast University`。按 2026-11-02 裁定 **`department` 不采用** → 上站写**东南大学**，不写院系
- 通讯作者：**取不到 → 待确认**（OpenAlex 四位 `is_corresponding` 复核仍全 False）
- `created` **2026-10-12T19:09:11Z** → **在本期窗口之外**，但该条**从未上站**（仅 open-items 挂账两期），
  按维护者裁定**可直接收入、如实写 2026-10-12、不加补记标注**。载体：IEEE TCPMT **Early Access**（无卷号，`page`="1-1"）
- 摘要要点（verifier 独立反演复核）：
  - 实验研究**双蒸发器泵驱两相冷却回路**在**不等热负荷**下的**动态启动特性**
  - 建立**基于热负荷分配的启动工况图（startup regime map）**，识别**同步/异步/耦合（synchronous, asynchronous, coupled）**三种模式，随两蒸发器热负荷差增大依次出现
  - **同步**：两蒸发器均呈 **twice-rise overshoot**，**上游蒸发器达稳态略有延迟**
  - **异步**：高负荷蒸发器 twice-rise overshoot、低负荷蒸发器**渐进（gradual）**启动
  - **耦合**：达峰温后两蒸发器壁温呈**两步下降（two-step descending response）**，表明进入**两相不稳定区**
  - 🔴 **须更正的一条**：原文 `the steady-state temperature difference between the two evaporators increases with total heat flux
    **in the synchronous and asynchronous modes**, whereas it decreases in the coupled mode` —— **同步「和异步」两种模式下都随总热流增大**。
    scout 只写了同步，**漏了异步，成稿必须补**
  - 定位：`multi-source electronic systems` / `high-heat-flux electronics` → 覆盖面内
- **实验**（`This study experimentally investigates`）；**确认全篇摘要零数值**（无热流、功率、温度、流量）→ 只能作定性/机理条
- 未取到：通讯作者、任何量值

## B1 · 10.3176/proc.2026.4.08 —— **否决（覆盖面外）**，verifier 独立判断与主编倾向一致
- 完整标题：`Additive manufacturing-aware topology optimization of cooling channels using a reduced-order cold plate model for electric machine water jackets`
- 作者四位同串 `Department of Electrical Power Engineering and Mechatronics, Tallinn University of Technology, Ehitajate tee 5, 19086 Tallinn, Estonia`
- 通讯作者取不到；`created` 2026-11-02，*Proc. Estonian Acad. Sci.* 2026 年第 4 期 **pp. 346–352**，OA gold
- ① **摘要里芯片/电子器件/功率半导体/数据中心字样：一个都没有。** 涉及应用对象的只有第一句：
  `Integrated liquid cooling jackets are widely used in the thermal management of **high-power-density motors**, but traditional designs
  rely on parametric channel layouts, failing to fully utilize the geometric degrees of freedom offered by additive manufacturing (AM).`
- ② **「cold plate model」是建模方法、不是物理对象**：原文 `topology optimization framework **based on** a reduced-order cold plate model`，
  即借用冷板式（二维薄板）降阶模型去算**电机水套**的流道拓扑；标题后缀明确物理对象是电机水冷套；算例是**二维**
- ③ 作者所属为**电力工程与机电系**，非热科学系（辅助证据）
- **否决理由**：物理对象为电机水冷套，与「数据中心/电子散热冷板」覆盖面不符，摘要零电子/芯片/半导体/数据中心字样。
  与既有判例一致（可比第 11 期否决的 Dual-Cooling-Media Cold Plate **for Electric Vehicles**）
- 保留意见（不改变否决）：方法本身与冷板拓扑优化同源，如需可在跨期方法清单留一行线索，**不进正文**
- 数字：**摘要无任何数值**
- 未取到：全文 PDF（`kirj.ee` connect_rejected）

## B2 · 10.1007/s40964-026-02044-5 —— 待确认（可作制造工艺线索条），数字已全核，**原文有一处单位错印**
- 完整标题：`The effect of sintering hold-time on heat transfer relevant properties of 3D-printed copper and bronze samples produced by bound powder extrusion`
- 单位：Crossref 两位全空；OpenAlex raw 两位**同串** `Clean Energy Research Group, Department of Mechanical and Aeronautical Engineering, University of Pretoria, Pretoria, South Africa`
  → 上站 **比勒陀利亚大学 机械与航空工程系**（南非）。按规则不写研究组与城市
  ⚠️ **Springer 文章页本会话不可达**（`link.springer.com` 303 → `idp.springer.com` DNS 不解析），第 7 期用过的 `citation_author_institution` 元标签法**本期走不通**；
  单位证据为 OpenAlex raw 串（规则 2 允许的通道），**但非出版商页面直取** → 建议随稿注明证据通道
- 通讯作者：**Bradley D. Bock**（`is_corresponding=True`）
- `created` **2026-11-05** → 窗内。*Progress in Additive Manufacturing*，`published` 2026-11-05，在线先发（无卷期）。**已同行评审**
- 数字（Crossref 交存完整摘要，逐字对照）：
  - 铜：**失重约 8%**（`lose about 8% of its mass during manufacturing`）；**随烧结保温时间延长收缩 12–30%**
  - 青铜：**失重约 10%**、**收缩 20–40%**
  - 孔隙率与热导率均为烧结时间的函数：铜 **25–45%** 与 **40–70 W/mK**；青铜 **27–45%** 与 **2–9 W/m**
  - ⚠️ **单位核准：原文就印作 `2–9 W/m`（缺 K）**，同句铜写作 `40–70 W/mK` → **这是出版商摘要的错印，不是转抄错误**。
    成稿若引用建议写「2–9 W/(m·K)（原文摘要印作 W/m，K 缺失）」或只引铜的 40–70 W/(m·K)
  - 🔴 **「6–20%」归属须更正**：原文 `... and 2–9 W/m for bronze, **which represents between 6 and 20% of the respective solid metals' thermal conductivity**`
    —— `respective solid metals`（复数）表明是**对铜与青铜合并给出的口径**，**不能写成「约为实体铜的 6–20%」**。
    （旁证：40–70 对实体铜约 400 W/(m·K) 为 10–17.5%；2–9 对实体青铜约 60 W/(m·K) 为 3–15%，均不单独等于 6–20%。）
  - **硬度为对应实体件的 30–50%**；**表面粗糙度显著高于传统减材加工样件**；孔隙成因为气体积聚导致的分层与脱脂留下的空洞；
    **比热容与实体件相近**（差异疑由碳杂质引起）；粗糙度与硬度在样件上**不均匀**
- **实验（材料表征）**
- **覆盖面：对象不符（试样、非冷板/热沉）→ 不作论文卡；建议作制造工艺线索条**。理由：① 摘要**无任何冷板/热沉/芯片/电子器件**字样；
  ② 但首句自述面向换热行业（`Bound Powder Extrusion (BPE) is in principle an excellent opportunity for the heat transfer industry as
  high thermal conductivity metals can be manufactured with relative ease and at low cost`），且 **BPE ≈ M-FFF 已在本刊工艺清单里**
  （第 7 期归档过 M-FFF 铜冷板论文 10.1007/s00170-025-17246-4）；③ 它给出的正是该工艺路线**当前铜件热导率只有实体金属 6–20% 这一硬约束**
- 未取到：Springer 文章页原始机构串与 Accepted 日期

## B3 · 10.1109/wipdaeurope69886.2026.11747072 —— **通过（有数字有基准）**，本期最大意外：**摘要取到了**
- ① **`created` = 2026-11-02T20:18:16Z**（`deposited` 2026-11-03）→ **在本期窗口内！** scout 只看到 `issued` = 2026-09（会期月份）。
  会议：**2026 IEEE Workshop on Wide Bandgap Power Devices and Applications in Europe (WiPDA Europe)**，2026-09-20～22，丹麦 Aalborg，**pp. 171–176**。**已同行评审（会议论文）**
- ② 完整标题：`Heat-Pipe-Assisted Skived-Fin Forced-Air Cooling Design for High-Power Converters`
- ③ 作者 Xinglan Hou(first) / Yongheng Yang；Crossref `affiliation[].name` 两位均为裸串 `Zhejiang University`（place: Hangzhou, China），
  OpenAlex raw 同 → 上站**浙江大学**（**无院系，不补写**）
- 通讯作者：取不到（两位 `is_corresponding` 全 False）→ 待确认
- ④ 摘要经 OpenAlex 单篇端点取到（Crossref 无 `abstract` 键）。数字 + 基准：
  - 对象：**460 kW 三电平中点钳位（NPC）光伏变换器**，含 **3 个 SiC MOSFET boost 模块（直流侧）+ 3 个 IGBT NPC 模块（网侧）**，**共用一只强制风冷散热器**
  - **30 根热管**埋入散热器基板，**位置与长度按两排模块布置和模块级损耗分布定制**
  - 方法：**ANSYS Icepak 三维共轭流-热模型**；模块损耗按所研究的 **DPWM** 策略计算后作为**稳态热源**施加
  - **基准明确 = baseline skived-fin heat sink（未加热管的 skived 翅片散热器）**，原句：
    `Compared with the baseline skived-fin heat sink, the proposed design reduces the maximum module temperature from 114.8 to 93.9 °C
    and the average module temperature is lowered from 105.0 to 90.5 °C. The maximum temperature difference among the six modules
    decreases from 19.8 to 6.9 °C, corresponding to a 65.2% reduction in thermal nonuniformity.`
  - 机理：定制热管布局**增强横向扩热**、抑制模块损耗不均引起的热失衡
- **纯仿真（ANSYS Icepak 稳态）**，摘要**未提任何实验或样机测试**
- ⑤ **工艺判定：研究的不是 skived 翅片的制造工艺本身**，而是以 skived 翅片散热器为平台/基准做热设计。
  skived-fin 仅出现在方案名与基准名两处，**无任何铲齿/切削工艺参数**（翅厚、翅距、加工方式、刀具、良率、成本）
  → **不能填 companies.md 里 skived 翅片的「擅长企业」列**，**不足以结清「工艺本身的论文」缺口**；
  但是**第 4 期 DIOJIC 之后第二条带 skived-fin 定量性能基准的文献**，可作该缺口行的第二条性能对照出处
- ⑥ **这是强制风冷（air-cooled heat sink + 嵌入热管）、不是液冷冷板**；场景是**光伏变换器（功率半导体模块）**、不是数据中心 → 属**电力电子散热**
- 未取到：通讯作者；摘要为 **OpenAlex 单通道**（Xplore 不可达，Crossref 未交存），**数字无第二通道交叉验证**
  → 若把 114.8/93.9/65.2% 写进正文，建议随稿注明证据通道

## C 组 · 抢救结果：**四条摘要全部三路全缺**（Crossref 无 `abstract` 键 + OpenAlex `abstract_inverted_index` 为 null + arXiv 无同名预印本）
arXiv 新路子本期无收获，5 个检索式全部 total=0 或无关：`all:"Scaling up embedded microfluidic cooling"`(0)、`au:Song_Bai AND abs:microfluidic`(0)、
`all:"CHF-constrained"`(0)、`au:"Bai Song" AND cat:physics.app-ph`（5 条全为热物性/近场热输运/FDTR，**无微流控冷却**）、
`all:"microfluidic cooling" AND all:"chips"`（3 条全为 2024 年及更早他人工作）。**结论：Bai Song 组这篇没有 arXiv 版。**

1. **10.1016/j.ijthermalsci.2026.111477** —— 待确认（摘要三路全缺）
   `A two-phase microchannel cold plate system for AI data center GPUs: CHF-constrained GPU-HBM co-thermal management`；
   `created` **2026-11-03T10:41:29Z**，*IJTS* **233, 111477**。
   ⚠️ **作者名须以 Crossref（出版商）为准，scout 与 OpenAlex 各有错**：Crossref 11 位 = Fengzhao Ni / Shihuan Zhang / Haoran Li / Yonghai Zhang /
   **Xiang Ma** / Xiaoping Yang / **Jinjia Wei** / Gang Qu / Peng Liang / Yun Zhu / Shouqing Li
   （OpenAlex 把 Xiang Ma 作 "X Y Ma"、把 Jinjia Wei 作 "Jie Wei"，**均不可用**）。
   单位（OpenAlex raw）：Ni / Shihuan Zhang / Yonghai Zhang / Ma / Yang / Wei → 西安交通大学（原串含国家重点实验室 + `School of Chemical
   Engineering and Technology`）→ 上站**西安交通大学 化学工程与技术学院**；Haoran Li、Shouqing Li → `China United Network Communications Co., Ltd, Shaanxi Branch`；
   Gang Qu、Yun Zhu → 同公司宁夏分公司；Peng Liang → `China United Network Communications Group Co., Ltd`（**中国联通，产学合作**）。
   通讯作者：**Shihuan Zhang 与 Yonghai Zhang**。注：**Jinjia Wei 是第 7 位，非第一或通讯作者**。
   标题层面最贴本刊主线，**但摘要与全部数字取不到**。
2. **10.1016/j.ijheatmasstransfer.2026.129813** —— 待确认（摘要三路全缺，arXiv 亦无）
   `Scaling up embedded microfluidic cooling from millimeter to centimeter-sized chips`；`created` **2026-11-04T19:07:27Z**，IJHMT **274, 129813**。
   作者 Wei Xiao / Zhiyao Jiang / Weiheng Li / **Bai Song（通讯，`is_corresponding=True`）**；四位同串
   `National Key Laboratory of Advanced Micro and Nano Manufacture Technology, Peking University` + `School of Mechanics and Engineering Science, Peking University`
   → 上站**北京大学 力学与工程科学系**。题材完全对口，**无摘要无数字**。
3. **10.1016/j.ijheatmasstransfer.2026.129793** —— 待确认（摘要三路全缺）
   `Research on manifold micro-jet impingement cooling technology for high-power thin-disk lasers`；`created` **2026-11-02T04:58:12Z**，IJHMT **274, 129793**。
   ⚠️ **Crossref 把姓名装反了**（`given`=姓），正确顺序取 OpenAlex display name：
   **Chenjie Wang / Guangwen Jiang / Sen Yang / Saile Zhang / Qin Lei / Tianqi Zou / Wen-Quan Tao**。
   单位：Chenjie Wang → 西安交通大学 能源与动力工程学院 ＋ 中国科学院西安光学精密机械研究所；Jiang/Sen Yang/Saile Zhang/Qin Lei/Tianqi Zou → 中科院西安光机所；
   **Wen-Quan Tao（通讯，`is_corresponding=True`）** → 西安交大能源与动力工程学院。激光器冷板在覆盖面内，**但无摘要无数字**。
4. **10.1109/tcpmt.2026.3751096** —— 待确认（摘要三路全缺）
   `A Network Model for Liquid Cooling in Data Center Servers utilizing an ML Model for Evaporative Chip Cooling`；
   `created` **2026-11-06T20:13:09Z**（窗口最后一天内），IEEE TCPMT **Early Access**。
   作者 Kartik Upadhyay / Sumanta Acharya，Crossref 两位均裸串 `Illinois Institute of Technology`（Chicago, IL, USA）→ 上站 **Illinois Institute of Technology**（无院系）。
   通讯作者取不到。题材对口，**无摘要无数字**。

# 汇总
**够论文卡（有数字 + 有基准 + 覆盖面内）—— 3 条**：A1 SSRN 7670126、A2 ECM-X 102444、B3 WiPDA 11747072（但风冷 + 仿真 + 光伏变换器，相关性待主编裁定）
**够定性/机理条（覆盖面内但摘要零性能量值）—— 2 条**：A5 IJHMT 129770、A6 TCPMT 3742181
**只够线索条 —— 6 条**：A3 mi17111225（74.5% 不可用）、B2 s40964（制造工艺）、C 组四条（一个数字都不能写）
**否决 —— 2 条**：A4 10.1063/5.0353789（覆盖面外）、B1 10.3176/proc.2026.4.08（覆盖面外）
**前期已刊内容的事实错误：本期未发现**（A6 与 129752 均从未上站，不入「更正」节）
