# scout-D · 英文期刊 in-press / online-first 专项（原样回传）

窗口 2026-09-27 ~ 2026-10-03。

**方法**
- Crossref REST API `filter=from-created-date:2026-09-27,until-created-date:2026-10-03` 两路扫：
  - 第一路：10 个主题词 `query.bibliographic` 全库查询。
  - 第二路：按 ISSN 逐刊全量拉取 + 标题关键词筛选。IJHMT 33 条、ATE 63 条、ECM 15 条、IJTS 18 条、TCPMT 7 条。
- JEP（1043-7398）与 ASME J. Heat Mass Transfer（2832-8450）窗口内 Crossref 返回 0 条。未换 ISSN 复查，算「未检出」，不排除 ISSN 有误。
- **取不到摘要**。Crossref 无 abstract 字段，Elsevier 文章付费，fetch_source.py 只返回元数据。**下列候选全部只有标题级信息、无性能数字**。
- Elsevier 的 `published-online` 在 Crossref 中全部为空（None），判窗只能依据 `created`。`published-print` 都是未来刊期（2026-10 ~ 2027-02），即均处 in press 状态。

---

### 候选 1 · 嵌入式微针肋 + 3D 歧管散热器（高功率电子）
- Embedded micro-pin-fin heat sink with 3D manifold for cooling high-power electronics
- IJHMT；articles in press（印本刊期 2027-02）
- DOI 10.1016/j.ijheatmasstransfer.2026.129613
- created = `2026-09-28T10:31:05Z`；published-online = None；published-print = `[[2027,2]]` → **窗口内**
- Zhiyao Jiang; Wei Xiao; Weiheng Li; Bai Song；单位未取到
- 仅标题级，无摘要无数字（付费）
- 对象：芯片/高功率电子；相关性 **强**

### 候选 2 · SiC 功率模块液冷散热器多目标拓扑优化
- Multi-objective topology optimization of a liquid-cooled heat sink for electric vehicle SiC power modules considering thermal and hydraulic performance
- ATE；articles in press（印本 2026-11）
- DOI 10.1016/j.applthermaleng.2026.133472
- created = `2026-10-01T16:52:55Z`；published-online = None；published-print = `[[2026,11]]` → **窗口内**
- Youyou Gao; Xing Xu; Cong Liang; Heping Ling；单位未取到
- 仅标题级，无数字
- 对象：车用 SiC 功率模块；相关性 **强**。与已报「散热-流阻双目标拓扑优化液冷板」主题近，DOI 未命中，需核是否同一工作

### 候选 3 · 微通道拓扑优化（场协同 / 熵耗散 / 熵产）
- Topology optimization and heat-transfer enhancement mechanisms of microchannels based on field synergy, entransy dissipation, and entropy generation
- ATE；articles in press（印本 2026-11）
- DOI 10.1016/j.applthermaleng.2026.133471
- created = `2026-09-30T21:04:46Z`；published-online = None；published-print = `[[2026,11]]` → **窗口内**
- Yuwei Liu; Jintao Liu; Jinghui Liang; Wenwei Jiang; Yuanzhi Sun; Changhui Chen；单位未取到
- 仅标题级，无数字
- 对象：微通道散热器；相关性 **中到强**。与已报「场协同+分形 CTO」同属场协同路线，需查重

### 候选 4 · 3D 堆叠 IC 的冷板 + 侧歧管混合冷却
- Numerical Investigation of a Hybrid Cold-Plate and Side-Manifold Cooling Solution for 3D-Stacked Integrated Circuits Under Uniform and Non-Uniform Power Dissipation
- IEEE TCPMT；早期访问（状态未向出版商页核实）
- DOI 10.1109/tcpmt.2026.3739728
- created = `2026-10-02T19:05:03Z`；published-online = None；published-print = None（issued `[[2026]]`）→ **窗口内**
- Chukwudi Azubuike (Binghamton University); Mohammad Tradat (Binghamton University); Bahgat Sammakia (Binghamton University)（Crossref 机构串）
- 仅标题级，无数字
- 对象：3D 堆叠芯片冷板；相关性 **强**，单位已取到

### 候选 5 · 液冷储能电池系统的湍流 / 非等温拓扑冷板
- Turbulent and non-isothermal devised topology cooling plates for liquid-cooled energy storage battery system
- IJHMT；articles in press（印本 2027-02）
- DOI 10.1016/j.ijheatmasstransfer.2026.129665
- created = `2026-09-30T07:36:29Z`；published-online = None；published-print = `[[2027,2]]` → **窗口内**
- Xiang-Wei Lin; Meng-Lin Yu; Xin-Yi Lin; Yu-Tong Xie; Zhi-Fu Zhou; Liejin Guo；单位未取到
- 对象：储能电池；相关性 **中**

### 候选 6 · 液汽分离通路：选择性表面改性 + 射流冲击开放微通道
- Separated liquid-vapor pathways: a hybrid cooling strategy with selective surface modification and jet impingement in open microchannels for enhanced heat transfer
- IJTS；articles in press（印本 2027-02）
- DOI 10.1016/j.ijthermalsci.2026.111369
- created = `2026-10-02T00:16:23Z`；published-online = None；published-print = `[[2027,2]]` → **窗口内**
- Yuming Guo; Yifei Li; Yong Qin; Liang Zhao；单位未取到
- 对象：电子两相冷却；相关性 **中到强**

### 候选 7 · 先进 IC 封装热路径工程（疑综述）
- Thermal pathway engineering for advanced integrated-circuit packaging: from intrinsic properties to lifetime qualification
- ATE；articles in press（印本 2026-10）
- DOI 10.1016/j.applthermaleng.2026.133168
- created = `2026-09-28T19:23:49Z`；published-online = None；published-print = `[[2026,10]]` → **窗口内**
- Peisheng Liu; Feiyu Qiang; Jinlan Wang；单位未取到
- 「是否综述」为 scout 由标题推测，未核
- 相关性 **中**（偏材料与热界面）

### 候选 8 · 超薄大面积均热板双层吸液芯
- Bilayer Wicks Enable High-Performance Large-Area Ultra-Thin Vapor Chambers
- IEEE TCPMT；早期访问（未核）
- DOI 10.1109/tcpmt.2026.3739624
- created = `2026-10-01T19:07:01Z`；published-online = None；published-print = None（issued `[[2026]]`）→ **窗口内**
- Ying He (Shanghai Jiao Tong University); Ninghua Zhan (Otto von Guericke University); Shijie Liu (SJTU); Ran Holtzman (CSIC); Evangelos Tsotsas (Otto von Guericke University); Rui Wu (SJTU)
- 相关性 **弱到中**（非冷板，属均热/被动相变）

### 候选 9 · 径向挤压散热器烟囱设计（实验 + 神经网络）
- Optimization of chimney design for an extruded radial heat sink using experiments and neural network models
- IJHMT；articles in press（印本 2027-02）
- DOI 10.1016/j.ijheatmasstransfer.2026.129656
- created = `2026-10-02T03:55:32Z`；published-online = None；published-print = `[[2027,2]]` → **窗口内**
- Yedam Jo; Yong-Joo Kim; Soo-Bong Jung; Yoon-Jae Lee; Seung-Woo Lee; Yeon-Ju Jang; Chaewon Yun; Dong-Bin Kwak；单位未取到
- 相关性 **弱**（风冷，非液冷）

### 候选 10 · TSV 阵列热管理混合驱动建模
- A Hybrid-Driven Modeling Approach for Thermal Management of TSV Arrays in 3D ICs
- IEEE TCPMT；早期访问（未核）
- DOI 10.1109/tcpmt.2026.3739533
- created = `2026-10-01T19:03:53Z`；published-online = None；published-print = None（issued `[[2026]]`）→ **窗口内**
- Guangbao Shan; Zeyu Chen; Yanwen Zheng; Xiaohua Wu; Yingtang Yang（均 Xidian University，Crossref 机构串）
- 相关性 **弱**（芯片内建模，非冷板）

---

**其它窗口内但相关性低或偏题（仅列 DOI，未深查）**
- 电池/EV：ATE 133389（浸没式电池）、ATE 133372（U 形微热管阵列+液冷储能）、ATE 133336（往复冷却）、ATE 133412（EV 流场热管理综述）
- 其它：IJHMT 129660（微针肋+电场池沸腾）、ATE 133423（多孔结构沸腾 LBM）、IJTS 111376（射流冲击，非电子）、Heat Transfer Research 10.1615/heattransres.2026065327（数据中心冷却液综述，created 2026-10-01T15:35:34Z，不在目标刊清单内）
- ECM 窗口内 15 条无冷板/电子冷却相关条目

**目标刊覆盖结论**：IJHMT / ATE / IJTS / TCPMT 有候选；ECM 无；JEP 与 ASME JHMT 窗口内 0 条。
