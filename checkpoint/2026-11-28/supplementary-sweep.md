# 主代理补扫 · 跨出版商 Crossref 全库关键词检索（scout D 自述正则标题筛可能漏检，故补）

方法：`api.crossref.org/works?query.bibliographic=<kw>&filter=from-created-date:2026-11-22,until-created-date:2026-11-28`，
6 组关键词（cold plate / microchannel heat sink / chip cooling / electronics cooling / liquid cooling chip / jet impingement cooling），
再以正则筛标题。**此举补出 4 条 scout 五路全未报的条目**，其中 3 条摘要完整、可成稿。
漏检原因：scout D 按「刊 ISSN 清单」扫，而这 4 条分别出自 **IEEE TED、Wiley Heat Transfer、Frontiers in Heat and Mass Transfer、IEEE INDIN** —— 均不在其 11 刊清单内。

## ✅ 新增 1 · DPC 陶瓷微通道液冷基板（高功率 LED 模块）
- DOI `10.1109/ted.2026.3751611` · IEEE Transactions on Electron Devices
- 标题：Highly Integrated Microchannel Liquid-Cooling Ceramic Substrate for Enhanced Thermal Management of High-Power LED Module
- 作者/单位（**OpenAlex raw_affiliation_strings，五位同串**）：Xianxing Ju（第一）、Qing Wang、Yongjie Ding、Yang Peng、Mingxiang Chen（末位）—— 原串均为 `Huazhong University of Science and Technology, Wuhan, China`（按规则删 Wuhan, China → **华中科技大学**，原串无院系）
- 通讯作者：`is_corresponding` **五位全 false** → **待确认**
- created **2026-11-27** ✓ 窗口内（OpenAlex PUBDATE 2026-01-01 为刊期名义日期，不作依据）
- 摘要途径：OpenAlex 单篇端点，**摘要完整**
- 关键数字（摘要原文）：传统被动散热难以满足陶瓷基板上 **>100 W/cm²** 的散热需求；MCHS 外形 **20×20×2 mm³**，矩形直通道阵列、截面 **600×600 μm²**、**9 条并行通道**；多芯片 LED 模块在 **3 A** 下热流密度 **216.20 W/cm²**，最高温度自 **158 °C 降至 83.3 °C**，光输出功率**提升 47.82%**；对照为**商用蛇形 MCHS 模块（S-MCHS）与主动风冷模块**；仿真与实验吻合良好
- **工艺要点（本条同时属制造工艺角度）**：**直接镀铜（DPC）**陶瓷基板 + **图形化电镀铜**把铜微通道与陶瓷基板结合，盖板与微通道热沉经**钎料键合气密封装**；原文指出**常规减材工艺**做铜微通道与陶瓷基板的**兼容性差、集成度低、可靠性不足**
- 覆盖面：高功率 LED 属光电器件 → 按 **2026-11-02 维护者裁定**（激光设备等光电/电子器件冷板在覆盖面内）**在覆盖面内**
- 相关性：**强**（冷板结构 + 制造工艺 + 实测三者齐备）

## ✅ 新增 2 · 两相浸没冷却数据中心的翅片式热沉沸腾特性
- DOI `10.1002/htj.70430` · Heat Transfer（Wiley）
- 标题：Performance Analysis of the Finned Heat Sinks Used in the Immersion Cooling System of Data Center
- 作者/单位（**OpenAlex raw**）：Lei Zhao（第一，`College of Pipeline and Civil Engineering China University of Petroleum (East China) Qingdao China`）、
  Xiaosong Cheng（**通讯**，`School of Civil Engineering and Architecture East China Jiaotong University Nanchang China`）、
  H.X. Ma（**通讯**，原串含 `Key Laboratory of Safety and Resilience of Civil Engineering in Mountain Area` + `School of Civil Engineering and Architecture East China Jiaotong University` → **按规则 3 删实验室**）、
  Yulong Yang、Wei Cui（同华东交通大学土木建筑学院）、Jiajun Wang（`School of Energy and Environment Southeast University Nanjing China`）、
  Cuiwei Liu（末位，**通讯**，中国石油大学（华东））
- 通讯作者：**三位 `is_corresponding=true`**（Xiaosong Cheng、H.X. Ma、Cuiwei Liu）→ 已核
- created **2026-11-26** ✓；OpenAlex PUBDATE **2026-11-25**
- 摘要途径：OpenAlex，**摘要完整**
- 关键数字（摘要原文）：两相浸没液冷系统（TPICS）翅片热沉沸腾模型，仿真与文献实验数据对比**相对误差在 ±15% 内**；
  **低功率**工况下最高翅片温度 **49.3 °C**（出现在侧向 **z = 65 mm**），**仅比冷却液沸点高 0.3 °C**，自然对流即可满足 CPU 散热需求；
  **高功率**工况下最高翅片温度 **54.6 °C**（出现在翅根）；汽相体积分数分布显示**上部翅片两侧几乎无沸腾换热**；
  据此提出**圆弧段（circular segment）翅片**构型，相对矩形翅片使峰值温度**降 2.8 K**、材料用量**降 27.3%**
- 相关性：**强**（数据中心两相浸没冷却）

## ✅ 新增 3 · 面向高密度 AI 数据中心的浸没-射流复合冷却
- DOI `10.32604/fhmt.2026.093483` · Frontiers in Heat and Mass Transfer
- 标题：Immersion Jet Cooling for High-Density AI Data Centers: From Structural Optimization to Dimensionless Modeling
- 作者/单位（**OpenAlex raw**）：Zhendong Li（第一，`College of Urban Construction, Nanjing Tech University, Nanjing, China`）、
  Yu Wang（**通讯**，同上）、Zhang Ying-yin（同上）、Xiaolei Yuan（末位，`Department of Civil Engineering, School of Energy Systems, LUT University, Lahti, Finland`）
- 通讯作者：Yu Wang `is_corresponding=true` → 已核
- created **2026-11-28** ✓（即本期期号日期当天）
- 摘要途径：OpenAlex，**摘要完整**
- 关键数字（摘要原文）：工质为氟化液 **DA-325**；优化对象是**完整 2U AI 服务器**（**2 CPU + 8 GPU + 18 个二级元件**）；
  相对**纯浸没冷却**，浸没-射流使 **CPU 峰值温度降 12.83%**（**79.74 °C → 69.51 °C**），
  面平均换热系数自 **105.4 升至 155.6 W/(m²·K)**，**提升 47.6%**；
  正交试验 + 极差与方差分析得**射流管径为统计上最显著参数**，最优几何组合 **L = 8 mm、D = 12 mm、N = 50 mm、d = 6 mm**；
  低黏度 DA-325 在同等热负荷下优于 **FC-40、矿物油、硅油**，**最多低 13 °C**；入口温度与芯片温度近似线性正相关，射流速度呈饱和型非线性收益；
  最后给出含 **Re、Pr、Eu 与几何系数 α** 的无量纲 Nu 关联式，**预测误差在 ±13% 内**
- 相关性：**强**（AI 数据中心、射流+浸没）

## ✅ 新增 4 · SiC 多芯片功率模块的广义 Fourier 级数热模型
- DOI `10.1109/tpel.2026.3758090` · IEEE Transactions on Power Electronics
- 标题：A Generalized Fourier-Series Thermal Model for Chip- and Layer-Wise Temperature Distribution in SiC Multi-Chip Power Modules
- 作者/单位（**OpenAlex raw，七位同串**）：Linke Zhou（第一）、Di Wang、Manar Emira、Jiaming An、Yulei Wang、Chang Liu、Ali Emadi（末位）
  —— 原串均为 `McMaster University, Hamilton, ON, Canada`（删 Hamilton, ON, Canada → **McMaster University**，原串无院系）
- 通讯作者：七位全 false → **待确认**
- created **2026-11-27** ✓
- 摘要途径：OpenAlex，**摘要完整**
- 关键数字（摘要原文）：基于**模态投影**的框架实现相邻层间系数传递，把解析热建模**推广到非等截面**（突破传统等截面假设）；
  对流换热系数 **h** 的影响机制从数学与传热两个角度分析，**真实冷却边界由 CFD 提取**并给出实用 h 区间；
  在一只**商用 10 芯片 SiC MCPM** 上经仿真与实验验证，覆盖不同流量、**功率损耗至 1080 W**、**峰值结温超过 150 °C**
- 相关性：**中强**（属 C 角度「仿真方法」：解析热模型 + CFD 提取的真实冷却边界，摘要明确涉芯片与冷却边界 → 过覆盖面闸门）

## ❌ 补扫到但不收
- `10.1109/indin68935.2026.11802527`（created 2026-11-27）Experimental and Numerical Investigation of Two-Phase Immersion Cooling for High-Density Power Electronics；
  Jeyaganesh Devaraj / J.C. Ji / Yam Prasad Siwakoti，原串均 `University of Technology Sydney`；
  **`abstract_inverted_index` 为 null，摘要零获取** → 按铁律不编摘要，**仅可作标题级线索**
- `10.1016/j.icheatmasstransfer.2026.113208`（created 2026-11-26）热分数步格子 Boltzmann 模型，受限狭缝射流冲击恒热流壁面；
  南方科技大学（通讯 Xiang Li、Peng Yu）；**摘要零获取**，且标题为**通用射流冲击恒热流壁面**算例、无芯片/冷板字面
  → 按 2026-11-02 覆盖面裁定**不收**
- `10.3390/electronics15235508` 面向下一代 AI 数据中心的电力电子（800 VDC 转型）—— 电力侧，非冷却
- `10.1615/heattransres.2026065341` 锂电池包波纹小通道冷板、`10.1080/01457632.2026.2762692` LiFePO₄ 冷板、
  `10.1016/j.icheatmasstransfer.2026.113239` 锂电池液冷板拓扑优化 —— **电池热管理，非电子/数据中心**，不收
- `10.32604/fhmt.2026.094166` 菱形扰流纳米流体微通道 —— 通用纳米流体强化，弱相关，不收
- `10.1007/s00231-026-03827-w` 表面粗糙度对微通道流动沸腾的影响 —— 摘要零获取、是否面向电子散热未知，不收
