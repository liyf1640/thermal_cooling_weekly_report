# scout-D 回传（英文期刊 in-press / online-first 专项）· 原样存档

**方法**：Crossref `filter=issn:...,from-created-date:2026-10-18,until-created-date:2026-10-24` 逐刊扫描。每刊总条数：IJHMT 18、ATE 85、ECM 22、IJTS 20、ICHMT 46、TCPMT 17、Physics of Fluids 95、IJHFF 10、Energy 105、CSITE 31。JEP 1、ASME J. HMT 0。按标题关键词筛选并剔除已报 DOI。**筛选只看标题，可能漏掉标题没写关键词的条目。**

**整体取到与取不到**：所有 Elsevier 条目，Crossref 与 fetch_source.py 都没有摘要，也没有单位（sciencedirect 不可达，OpenAlex 新条目多无摘要）。这些候选只有标题、作者、DOI、日期。Elsevier 条目的 `published-online` 在 Crossref 均为空。

## 一、两条专项重试挂账

**挂账 1 · DOI 10.1016/j.applthermaleng.2026.133678（首次报道）**
- Data-efficient multi-objective structural optimization and design space exploration of refrigerant-based cold plate for laser device
- ATE；`created` 2026-10-17T05:15:13Z；`published-online` 无；Crossref `published` 2026-11。**created 10-17 落在本窗口（10-18~10-24）之外。**
- 单位：OpenAlex 现已收录（上期 404）。五位作者 raw 串相同：「School of Mechanical Engineering, University of South China, Hengyang, 421001, China」（Qingwen Gui、Youwei He、Jiangshuo Cui、Yong Chen、Chaochao Zhou）。Crossref 五位仍全空。
- **通讯作者：Youwei He**（OpenAlex `is_corresponding=True`，仅此一位）。
- OpenAlex 关键词：cold plate、refrigerant cooling、multi-fidelity surrogate modeling、Bayesian optimization、SHAP、thermal-hydraulic performance、pressure drop、temperature deviation、high-power lasers。
- **推断**（非从原文读到）：仿真 + 代理模型优化研究，有无实验验证无法确定。
- **摘要、性能数字：取不到。** Crossref 无 abstract 键，OpenAlex 无 inverted index；Semantic Scholar 与 Elsevier API 403；WebSearch 无结果。

**挂账 2 · DOI 10.1109/tcpmt.2026.3742181（首次报道）**
- Dynamic startup characteristics of a dual-evaporator cooling loop for electronic thermal management with unequal heat load
- IEEE TCPMT；`created` 2026-10-12T19:09:11Z；`published-online` 无；Crossref `published` 2026。**created 10-12，窗口外。**
- 作者：Ruixue Yang、Chengcheng Fan、Zhiheng Zhu、Chengbin Zhang。
- **单位新发现**：Crossref JSON 里每位作者 affiliation 对象为 `{"name": "Southeast University", "place": ["Nanjing, PR China"], "department": ["School Of Energy And Environment"]}`，四位一致。fetch_source.py 只展示 name。**出版方交存的 name 确实是裸串，但交存里另有结构化 department 与 place 字段。是否采用 department 由调用方裁定；scout 未自行补写。** OpenAlex raw 串仍只有 Southeast University。
- 通讯作者：OpenAlex 四位 `is_corresponding` 均 False，取不到。
- **摘要、性能数字：取不到**（Crossref 无 abstract，含 unixsd XML 亦未见；OpenAlex 无摘要；IEEE 与 Semantic Scholar 不可达）。

## 二、ASME 侧
- `published-online` 过滤 10-18~10-24：JEP 命中 1 条 —— DOI 10.1115/1.4072766「Special Issue on InterPACK 2025」，created 2026-10-21、published-online 2026-10-21。**特刊前言/编辑性条目，不是研究论文，不建议收。** 上一条 JEP 为 10.1115/1.4072719（created 09-25、published-online 10-01）。
- ASME J. Heat and Mass Transfer：窗内 created 与 published-online 均 0 条。最新两条 10.1115/1.4072697（created 09-17、published-online 09-29）、10.1115/1.4072673（created 09-05、published-online 10-01）。
- asmedigitalcollection 官网不可达（通道限制）。
- TCPMT 窗内 17 条中 6 条过标题筛选，均非热管理（LPDDR 温度传感器漂移、D 波段倒装互连、TSV RLGC 建模，其余目次类）。无冷板或热沉候选。

## 三、窗内 created 的候选（均无单位、无摘要、无数字，需 verifier 复核）

**强相关（冷板 / 微通道热沉 / 芯片冷却）**

| # | 标题原文 | 作者（Crossref，无单位） | 刊 | DOI | created | Crossref published（印本名义） |
|---|---|---|---|---|---|---|
| 1 | Thermal control performance of liquid-metal based microchannel cold plate in CPU cooling application | De-Xin Zhang; Lai-Shun Yang; Kai Xie | IJHFF | 10.1016/j.ijheatfluidflow.2026.110759 | 2026-10-20 | 2026-12 |
| 2 | Numerical investigation on thermal-hydraulic performance of manifold jet-microchannel heat sink with shark-fin-shaped bionic sidewalls | Jie Zhong; Delin Shu; Lijun Liu; Gaoliang Liao; Feng Zhang | IJHFF | 10.1016/j.ijheatfluidflow.2026.110754 | 2026-10-19 | 2026-12 |
| 3 | Unraveling topology-driven flow characteristics and thermal-hydraulic synergy in TPMS microchannel heat sinks for chip cooling | Yi Li; Yuanle Zhang; Jianhong Zhou; Qiang Li; Xuemei Chen | ICHMT | 10.1016/j.icheatmasstransfer.2026.112877 | 2026-10-21 | 2026-11 |
| 4 | Thermo-hydraulic enhancement of microchannel heat sinks using segmented coaxial-shielded TSVs integrated into sinusoidal-featured pin-fins for 3D IC cooling | Qi Liu; Xia Xiao; Zhouxu Luo; Shengyan Lin; Jiannan Zhou | ICHMT | 10.1016/j.icheatmasstransfer.2026.112866 | 2026-10-19 | 2026-11 |
| 5 | Enhanced hotspot suppression and two-phase boiling performance in groove–tapered composite microchannels for high heat flux electronics | Guangping Wang; Yuling Zhai; Zhouhang Li; Hua Wang | IJTS | 10.1016/j.ijthermalsci.2026.111450 | 2026-10-22 | 2027-03 |
| 6 | Experimental study on subcooled boiling flow of PFO-50 in pillar-array microchannel with flexible tails | Shuaihua Ma; Zheng Weng; Lei Xie; Mei Lin; Wenxiao Chu; Qiuwang Wang | IJHMT | 10.1016/j.ijheatmasstransfer.2026.129752 | 2026-10-19 | 2027-02 |
| 7 | History-aware adaptive mesh refinement via latent-relevance dataset selection for thermal-fluid topology optimization | Yuguo Fu; Dong Chen; Melvan Tan Kian Hao; Lifei Ye; Lailai Zhu; Poh Seng Lee | IJHMT | 10.1016/j.ijheatmasstransfer.2026.129712 | 2026-10-21 | 2027-02 |
| 8 | Thermal-safety-constrained cooling energy optimization for data centers using a physics-informed graph surrogate model | Xinyao Wang 等 8 位 | Energy | 10.1016/j.energy.2026.142880 | 2026-10-21 | 2026-10 |
| 9 | Experimental characterization and modelling of a compact adsorption chiller prototype for data Centre cooling | Di Cicco; Alejandro Jose; Aprile Marcello; Mittelbach Walter; Freni Angelo | ATE | 10.1016/j.applthermaleng.2026.133754 | 2026-10-24 | 2026-11 |
| 10 | Thermo-economic analysis of depth-optimised hybrid seawater cooling for offshore data centres in the shallow Arabian Gulf | Farhat Mahmood; Sertac Bayhan; Tareq Al-Ansari | ATE | 10.1016/j.applthermaleng.2026.133740 | 2026-10-24 | 2026-11 |

相关性依据只来自标题。#7 与冷板的关联只能从标题推断。#8、#9、#10 是机房级冷却，不是芯片级冷板，相关性中等偏弱。

**中 / 弱相关**

| # | 标题原文 | 作者 | 刊 | DOI | created |
|---|---|---|---|---|---|
| 11 | Novel fin design and layout patterns for superior hydrothermal performance of microchannel heat sink | Hussain Sallar; Muhammad Irfan; Muhammad Mahabat Khan | ICHMT | 10.1016/j.icheatmasstransfer.2026.112885 | 2026-10-19 |
| 12 | A novel intelligent framework for thermal management design of power electronics systems | Biju Theruvil Sayed 等 10 位 | ICHMT | 10.1016/j.icheatmasstransfer.2026.112876 | 2026-10-22 |
| 13 | Numerical investigation of the thermo-hydraulic performance of a diatom-inspired pin-fin heat sink | Arjun M B 等 7 位 | IJTS | 10.1016/j.ijthermalsci.2026.111405 | 2026-10-22 |
| 14 | Coupled effects of fin structures and nanofluids on the thermal-hydraulic characteristics of mini plate-fin heat sinks | Ruitong Ding; Shentao Song; Jiang Pan | IJTS | 10.1016/j.ijthermalsci.2026.111447 | 2026-10-21 |
| 15 | Experimental investigation on flow boiling in leaf-inspired open microchannels | Wenhao Ma; Yingli Xue; Yi Ding; Li Jia; Liaofei Yin | IJHFF | 10.1016/j.ijheatfluidflow.2026.110762 | 2026-10-20 |
| 16 | Exploring suitable channel configurations of a microfluidic fuel cell stack for chip combined cooling and power applications | Ehtesham Ali 等 7 位 | ATE | 10.1016/j.applthermaleng.2026.133737 | 2026-10-20 |
| 17 | Percolation-based characterization of vapor network evolution during pool boiling of a highly wetting dielectric fluid | Ji-Hwan Park; Daeseong Jo | ATE | 10.1016/j.applthermaleng.2026.133714 | 2026-10-21 |
| 18 | Effects of conical structure geometry on boiling heat transfer in confined flat thermosyphon | Yijia Liu 等 8 位 | IJHMT | 10.1016/j.ijheatmasstransfer.2026.129772 | 2026-10-23 |
| 19 | Effects of nozzle exit size and edge shape on transient flash spray cooling performance of a millimeter-scale sweeping nozzle | Jiameng Tian 等 9 位 | IJHMT | 10.1016/j.ijheatmasstransfer.2026.129784 | 2026-10-21 |

**唯一在 Crossref 有单位的条目（AIP，窗内 online）**
- Dual-scale and hybrid micropillar architectures for enhanced boiling and capillary transport: A three-dimensional pore-scale study
- 作者：Majid Eshagh Nimvari；Michael J. Gibbons。单位原串：「Department of Mechanical, Manufacturing & Biomedical Engineering, Trinity College Dublin, The University of Dublin , D02 PN40 Dublin,」（Crossref 原串末尾即截断于逗号）。
- Physics of Fluids；DOI 10.1063/5.0355126；`created` 2026-10-22，`published-online` 2026-10-22（Crossref `published` 字段 2026-10-01）。
- 摘要要点（Crossref abstract，输出被截断、后半未读到）：3D 孔隙尺度 VOF 仿真；monopillar、bipillar、hybrid 三种微柱构型；热流 10~100 W/cm²；预测换热系数随热流从约 4.8 增至 8.9 W/cm²·K；hybrid 构型壁面过热更低、汽相波动更小；bipillar 渗透率显著高于 monopillar，但高热流下大孔易积汽。
- 相关性：中（高热流沸腾表面，纯仿真，非冷板）。去重：新增。

## 四、本窗未检出 / 未列入
- Energy Conversion & Management：22 条，标题筛选后无冷板或电子散热条目。
- Case Studies in Thermal Engineering：31 条，无相关候选。
- ASME JEP / J. HMT：无研究论文。TCPMT：无热管理论文。
- 已剔除 10-18 起窗内但属电池、建筑、燃气轮机叶片冷却、电动车热管理等范围外条目。
- 所有候选的摘要与性能数字、单位均需 verifier 取。当前环境对 sciencedirect、IEEE、Semantic Scholar、Elsevier API 均 403。
