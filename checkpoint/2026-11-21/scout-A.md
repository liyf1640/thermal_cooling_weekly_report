# scout-A 回传 · 冷板仿真与设计（原样存档）

窗口 2026-11-15 ~ 11-21。扫过：Crossref `from-created-date:2026-11-15,until-created-date:2026-11-21`，8 条检索式
（cold plate、microchannel heat sink、manifold microchannel、topology optimization heat sink、jet impingement chip、
liquid cooling data center、two-phase cold plate、heat sink electronics）+ OpenAlex 单篇 DOI 查询。
- ⚠️ **arXiv：`export.arxiv.org` 每条查询都回 "Rate exceeded" 或空输出 → 本期 arXiv 一路未完成，
  arXiv 候选为零是「未扫到」而非「不存在」。**
- 未运行 WebSearch。

## 定向重试：10.1109/tcpmt.2026.3751185 —— **摘要已取到**（高优先）
- 方法：OpenAlex 单篇端点现已带 `abstract_inverted_index`；Crossref 仍无摘要；Xplore 文档 11796570 不可达（HTTP 000）。
- Addressing Thermal Crosstalk in AI Chips and Heterogeneous Packages with Topology-Optimized Cold Plates
- IEEE TCPMT Early Access；Crossref created **2026-11-13**（上期窗口）
- 作者与单位（OpenAlex `raw_author_name` / `raw_affiliation_strings`）：
  - Jaswanth Sai Bangaru Garu：University of California, Irvine, CA, USA
  - Zubair Shaikh：University of California, Irvine, CA, USA
  - Taehwan Kim：Samsung Electronics Co., Ltd, Hwasung, Republic of Korea
  - Jae Choon Kim：Samsung Electronics Co., Ltd, Hwasung, Republic of Korea
  - Jaeho Lee：University of California, Irvine, CA, USA
  （⚠️ 主代理注：Crossref `name` 原串为裸 `University of California`、`place` 为 `Irvine, CA, USA`；
   第 13 期已裁定**不得推定为欧文分校**，按 rules 第 2 条不写城市/州省 → 正文只写到 University of California。）
- 摘要关键数字：冷板热流体拓扑优化以最小化 ASIC 与 HBM 间热串扰；**ASIC 功率 300 W**；
  固体体积分数 **0.6** 的拓扑优化冷板在**恒定泵功**下使 ASIC 维持约 **90 °C**、HBM 约 **43 °C**；
  **热串扰 0.075 °C/W，约为同条件常规平行通道冷板的 1/3**；另研究固体体积分数、流向、多 HBM 构型，
  并报告热点冷却、泵功需求与串扰之间的取舍。
- 置信度高。**不是「第 3 次失败」——第 3 次尝试取到了。**

## 候选（Crossref created 在 11-15~11-21 内，均未命中去重清单）
Elsevier 第 1~6 条摘要未在 Crossref / OpenAlex 交存；标题与作者单位为真，但**冷却相关性判断只能靠标题**。

**1. 10.54097/fdaate22**（created 2026-11-21；`published` 2026-11-20）
- Multi-Objective Optimization of Manifold Microchannel Heat Sink Structures Using a Gaussian Process Surrogate and NSGA-II
- *Academic Journal of Applied Sciences*（Darcy & Roy Press，**小出版商**）
- 作者（Crossref）：Weifu Huang；Wenyan Xue（均 The College of Mechanical and Energy Engineering, Guangdong Ocean University, Yangjiang, China）
- **摘要已取到**。关键数字：压降半经验拟合 **R² = 0.8994**、热阻拟合 **R² = 0.6229**（偏低）；
  高斯过程回归对比两种树集成，再用 NSGA-II + TOPSIS；选定构型为**无针肋、深度比 4.48、四排**，
  压降为热阻最优解的 **36.4%**，代价是热阻多 **4.4%**；在 100 个随机权重向量中的 **71 个**下仍最优。
- 覆盖面：摘要写 "manifold microchannel heat sink"，但**未字面提 chip 或 electronics**，且小样本方法学。相关性中。
- 置信度中（摘要已读，但**刊物层级低**）。

**2. 10.1016/j.ijheatmasstransfer.2026.129918**（created 2026-11-19；OpenAlex 11-20）
- Hierarchical thermo-fluid modeling framework of CuIO-coated manifold microchannels for high-heat-flux electronics cooling
- 作者（OpenAlex raw）：Seungjae Lee、Jaewon Hwang、Hyoungsoon Lee（School of Mechanical Engineering, Chung-Ang University, Seoul）；
  Daeyoung Kong（Department of Mechanical Engineering, Stanford University；另 Low-Carbon Integrated Technology Creative Research Section, ETRI, Daejeon）；
  Minsoo Kang（RF/Power Components Research Section, ETRI）；Sangyeon Pak（School of Electronic and Electrical Engineering, Hongik University）；
  Jungwan Cho（School of Mechanical Engineering, Sungkyunkwan University）
- **摘要未取到。** 覆盖面：标题含 "manifold microchannels … electronics cooling" + "modeling framework"，契合强。无数字。

**3. 10.1016/j.applthermaleng.2026.134045**（Crossref created 2026-11-19）
- Experimental investigation of flow uniformity and two-phase flow stability in a topology-optimized minichannel cold plate with integrated throttling structures
- 作者：Zeran Han；Jingkai Ma；Min Zeng；Ting Ma（Key Laboratory of Thermo-Fluid Science & Engineering, Xi'an Jiaotong University）；
  Xiaohong Yan（School of Chemical Engineering, Xi'an Jiaotong University）
- **摘要未取到。** 覆盖面：标题含 "cold plate" 且为拓扑优化，契合强；**面向电子还是电池未证实**。
- ⚠️ 日期存疑：该 DOI 的 OpenAlex `created_date` 为 **2026-08-13**，与 Crossref 冲突，需复核 `created`。

**4. 10.1016/j.energy.2026.143202**（created 2026-11-20；OpenAlex 11-21）
- Thermal–Hydraulic Characterization and Multi-Objective Optimization of an Open Microchannel Cold Plate for Single-Phase Immersion Cooling of AI Servers
- 作者（OpenAlex raw）：Bo Liu、Yifei Liu、Man Wang、Gongming Xin（School of Nuclear Science, Energy and Power Engineering, Shandong University, Jinan）；
  Daoguang Yu（Logistics Support Department, Shandong University, Jinan）；Jinbo Li（Inspur Electronic Information Industry Co., Ltd., Jinan）；
  Dakuo Shi（Shandong Dongyue Polymer Material Co., Ltd., Zibo）
- **摘要未取到。** 覆盖面：标题含 "cold plate"、"AI servers"、"multi-objective optimization"，契合强。无数字。

**5. 10.1016/j.ijheatmasstransfer.2026.129924**（created 2026-11-17）
- Ultra-low pressure drop microchannel heat sink with novel geometry for uniform temperature in chip level cooling
- 作者：Anish Ojha；Aniket Saha；R.A. Thanush；Vaibhav Nayak（Department of Chemical Engineering, Institute of Chemical Technology - IndianOil Odisha Campus, Bhubaneswar, India）；
  Pyarimohan Dehury（Department of Energy Engineering, 同校区）
- **摘要未取到。** 覆盖面：标题含 "chip level cooling"、"microchannel heat sink"，契合强。

**6. 10.1016/j.applthermaleng.2026.134020**（created 2026-11-17；OpenAlex 11-18）
- Multi-objective design of impinging-jet double-layer microchannel heat sinks using knowledge-transfer reinforcement learning
- 作者（OpenAlex raw）：Xingran Li、Yichen Wang、Chenhan Lian、Ziyu Li、Yixin Chen（Key Laboratory of Thermo-Fluid Science and Engineering of MOE, Xi'an Jiaotong University）；
  Ruiyao Xiao（School of International Trade and Economics, University of International Business and Economics, Beijing）；
  Zhiyu Yang（The First Clinical College, Chongqing Medical University）
- **摘要未取到。** 覆盖面：标题只给方法与器件，**未写 chip 或 electronics**，需按闸门核摘要。相关性中。

**7. 10.1016/j.cma.2026.119578**（created 2026-11-20；OpenAlex 11-21）
- Multiscale topology optimization with non-uniform unit cell mapping for spatially-varying pitch pin-fin heat sink design
- *Computer Methods in Applied Mechanics and Engineering*（Crossref 印本日期 2027-02）
- 作者（OpenAlex raw）：Yonghwa Ji、Jaewook Lee（Department of Mechanical and Robotics Engineering, GIST, Gwangju）；
  **Ercan M. Dede**（Electronics Research Department, Toyota Research Institute of North America, Ann Arbor, MI, USA）
- **摘要未取到。** 覆盖面：针肋热沉拓扑优化 + 电子研究部门合著者。相关性中，**需摘要确认电子/芯片语境**。

**8. 10.1109/tcpmt.2026.3754479**（Crossref created 2026-11-16）
- A Biradial Multiple Entry Mini-channel Heat Sink for Processing Electronic Materials with an Organic Deep Eutectic Solvent (DES) Based Nano-coolant
- 作者（Crossref 与 OpenAlex）：Sujatha Selvamurugan；Mannem S V Sayi Teja Reddy；Dhiman Chatterjee；Sarit K Das（Indian Institute of Technology Madras）；
  Badal Modi；Dhairyashil Desai（Lam Research Bangalore）；Pyarimohan Dehury（Institute of Chemical Technology–IndianOil Odisha Campus, Bhubaneswar）
- **摘要已取到**（与 scout D 增量一致）：双径向多入口多出口小通道热沉、**水力直径 2 mm**，DES + hBN 纳米冷却液；
  冷却液工作范围 **−12 °C 至沸点 151.9 °C**（常压）；实验**底板温度保持 40 °C 以下**，与计算吻合；
  对比螺旋小通道热沉所需泵压更低、温度均匀性更好，**无百分比数字**。
- 覆盖面：面向 "advanced electronics processing" 的高热流冷却 → **是电子工艺设备，不是芯片冷板**。相关性中。
- ⚠️ 日期存疑：OpenAlex `created_date` 为 **2026-07-07**，与 Crossref 11-16 冲突，需复核。

## 窗口内见到但未取、不建议收（仅标题）
10.1016/j.ijheatmasstransfer.2026.129908（Tesla 阀两相混合）、10.1016/j.applthermaleng.2026.134001（阶跃热负荷瞬态沸腾）、
10.1016/j.ijheatmasstransfer.2026.129781（饱和界面体积相变模型，方法相关性弱到中）、
10.1016/j.icheatmasstransfer.2026.113153（单射流多孔平板）、10.1016/j.tsep.2026.104981（pump-cooler 肋片热沉）、
10.1016/j.ijthermalsci.2026.111490（RF 芯片 PCM + 热沉，PCM 为主、弱）、
10.1016/j.ijheatmasstransfer.2026.129907（功率电子直接浸没冷却，浸没非冷板）、
10.1016/j.csite.2026.108735（风冷数据中心多尺度模型，非液冷）。

## 覆盖面外 / 仅电池，已排除
10.1016/j.est.2026.125867（电池液冷板拓扑生成 + 代理优化）、10.3390/eng7110648（光伏冷板）、
10.1016/j.enconman.2026.122398（蜂窝夹层）、10.1007/s12217-026-10308-6（更正通知）。

## 前期窗口（11-15 之前）
本轮过滤器限定在新窗口内，**未尝试前期漏收回捞**。
