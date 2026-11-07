# Scout A（冷板仿真与设计）第 12 期回传

## 第一轮：六条指派（第三次重试摘要）—— 全部仍取不到
做法：每条各取 OpenAlex 单篇端点 + Crossref /works/<DOI>；两路摘要字段均空
（OpenAlex `abstract_inverted_index` 空、Crossref 无 `abstract` 键）。112877 与 129752 另跑 fetch_source.py，同样只有元数据。
未从标题措辞推内容。六条均无任何性能数字。

1. 10.1016/j.icheatmasstransfer.2026.112877 — created 2026-10-20T13:53:00Z
   "Unraveling topology-driven flow characteristics and thermal-hydraulic synergy in TPMS microchannel heat sinks for chip cooling"
   作者 Yi Li / Yuanle Zhang / Jianhong Zhou / Qiang Li / Xuemei Chen；OpenAlex 归一名 Nanjing University of Science and Technology（五位）；Crossref 无单位。
   未取到：摘要、全部性能数字。
2. 10.1016/j.icheatmasstransfer.2026.112866 — created 2026-10-19T10:20:51Z
   "Thermo-hydraulic enhancement of microchannel heat sinks using segmented coaxial-shielded TSVs integrated into sinusoidal-featured pin-fins for 3D IC cooling"
   作者 Qi Liu / Xia Xiao / Zhouxu Luo / Shengyan Lin / Jiannan Zhou；OpenAlex 归一名 Tianjin University（五位）。
   未取到：摘要、全部性能数字。
3. 10.1016/j.ijheatfluidflow.2026.110759 — created 2026-10-20T13:45:37Z
   "Thermal control performance of liquid-metal based microchannel cold plate in CPU cooling application"
   作者 De-Xin Zhang / Lai-Shun Yang / Kai Xie；OpenAlex 归一名 Shandong Huayu University of Technology + Shandong University of Science and Technology。
   未取到：摘要、全部性能数字。
4. 10.1016/j.ijheatmasstransfer.2026.129752 — created 2026-10-19T10:50:58Z
   "Experimental study on subcooled boiling flow of PFO-50 in pillar-array microchannel with flexible tails"
   作者 Shuaihua Ma / Zheng Weng / Lei Xie / Mei Lin / Wenxiao Chu / Qiuwang Wang；单位再试仍取不到（两路 institutions 均空）→ 待确认。
   印本期名义日期 2027-02（不作依据）。未取到：摘要、单位、全部性能数字。
5. 10.1016/j.icheatmasstransfer.2026.112885 — created 2026-10-19T10:20:51Z
   "Novel fin design and layout patterns for superior hydrothermal performance of microchannel heat sink"
   作者 Hussain Sallar / Muhammad Irfan / Muhammad Mahabat Khan；OpenAlex 归一名 Capital University of Science and Technology（三位）。
   未取到：摘要、全部性能数字。
6. 10.1016/j.applthermaleng.2026.133678 — created 2026-10-17T05:15:13Z
   作者 Qingwen Gui / Youwei He / Jiangshuo Cui / Yong Chen / Chaochao Zhou；OpenAlex 归一名 University of South China（五位），与已结清的南华大学一致。
   未取到：摘要、全部性能数字。

## 第一轮 arXiv 扫描
按提交日倒序查 cold plate / microchannel / heat sink，限 physics.flu-dyn + cs.CE，取最近 30 条。
窗口内（11-03）仅 arXiv:2611.04288（Knudsen 泵，氢气，与冷板无关）；10-18 的 2610.25433 为电动流体色散，无关。
其余为已报或窗口之前（2610.16716 已报、2609.21639 已报、2607.12473 属 7 月）。
→ **arXiv 窗口内零命中。**

## 第一轮未做（已派回补做）
Crossref 按 `created` 过滤的选题检索一条未跑；本回传仅覆盖「六条指派 + arXiv 两类」。

---

# Scout A 第二轮（Crossref 按 `created` 过滤的选题检索）—— 核心产出

## 方法
端点 `api.crossref.org/works?query.bibliographic=<kw>&filter=from-created-date:2026-10-25,until-created-date:2026-11-07&rows=50`。
跑了指派的 16 条 query，另加 data center cooling / GPU liquid cooling / direct-to-chip cooling / immersion cooling / vapor chamber 共 5 条。
（chip cooling、electronics cooling liquid、two-phase cold plate 三条首次报错，已重跑成功。）
摘要：OpenAlex 单篇端点（3 s 间隔）+ Crossref `abstract` 键，共取 28 篇。
单位：全部用 Crossref `author[].affiliation[].name` 或 OpenAlex `raw_affiliation_strings` **原串**，未用归一机构名。
候选均不在去重清单内。

## 一、窗口内**取到摘要**的候选

**C1. 10.1016/j.ijheatmasstransfer.2026.129770**（created 2026-10-27）
- "Flow boiling behavior of R1233zd(E) in embedded silicon microchannel heat sinks: Flow visualization, heat tran…"（Crossref 层截断，全称待核）
- 作者 Huigang Wang / Thanh Hoang Phan / Chirag R. Kharangate
- **单位原串**：Department of Mechanical and Aerospace Engineering, **Case Western Reserve University**, 10900 Euclid Avenue, Cleveland, OH, 44106, USA
- 内容：R1233zd(E) 在 4 个硅微通道热沉（宽 100/150/200/300 µm、深 100 µm）做流动沸腾实验，红外测壁温 + 高速可视化
- 已取结论（定性）：识别泡状/塞状/环状流；热流升高使 ONB 提前；高质量流速使沸腾起始延后，并在高质量流速下观察到压力驱动闪蒸；
  平均两相 HTC 受质量流速与通道宽度影响小，压降随二者显著上升
- ⚠️ **摘要中未读到具体 W/cm² 或 kW/(m²·K) 数值**；摘要末句之后内容未取到

**C2. 10.3176/proc.2026.4.08**（created 2026-11-02）
- "Additive manufacturing-aware topology optimization of cooling channels using a reduced-order cold plate mo…"（截断）
- *Proceedings of the Estonian Academy of Sciences*
- 作者 Yang Zhang / Martin Sarap / Toomas Vaimann / Ants Kallaste
- **单位原串**：Department of Electrical Power Engineering and Mechatronics, **Tallinn University of Technology**, Ehitajate tee 5, 19086 Tallinn, Estonia
- 内容：基于降阶冷板模型的 AM 感知拓扑优化，**2D 算例**，研究可制造性正则化对通道拓扑与热水力性能的影响
- 数字：**摘要为定性结论、无数值**。正则化越强→界面复杂度与流体面积分数越小、水力阻力上升、热性能下降；
  尖锐界面复核显示全局热响应吻合良好，局部峰值温度与水力导纳对密度法表征敏感
- ⚠️ **应用对象是电机集成液冷套、不是芯片冷板。电机冷却是否在覆盖面内须裁定。**

**C3. 10.2139/ssrn.7670126**（created 2026-10-25，**SSRN 预印本**）
- "Orientation-dependent flow boiling in rigid-tail micro-pillar array channels: Thermal-hydraulic performance an…"（截断）
- 作者 Zheng Weng / Shuaihua Ma / Zheng Li / Yuang Jiang / Mei Lin / Qiuwang Wang
- **单位原串**：OpenAlex 仅 Mei Lin 与 Qiuwang Wang 给出 "Xi'an Jiaotong University (XJTU), Xi'an, China"，**其余四位为空**
- 内容：亚冷 **PFO-50** 在**刚性尾板微柱阵列通道**中，在 **0° / 45° / 90°** 三个方位做流动沸腾实验
- **数字**：相对水平放置，垂直通道平均壁温**降 1.49 K**、总压降**降 20.2%**（代表工况）；
  低质量流速下 90° 的热水力性能因子约为 0° 的 **4.5 倍**；引入修正 Froude 数
- ⚠️ **与第 11 期挂账的 10.1016/j.ijheatmasstransfer.2026.129752（柔性尾板）属同一课题组、同一系列姊妹篇**
- 去重清单里有 ssrn.7536705 与 7656294，**无 7670126**

**C4. 10.1016/j.ecmx.2026.102444**（created 2026-11-03，*Energy Conversion and Management: X*）
- "Comparative thermo-hydraulic assessment of monolithic, hierarchical, hybrid, and functionally graded T…"（TPMS 之后截断）
- 作者 Dame Alemayehu Efa / Dejene Alemayehu Ifa
- **单位原串**：School of Mechanical Engineering, Institute of Technology, **Wallaga University**, P.O. Box 395, Nekemte, Ethiopia
- 内容：面向**高功率电子**的功能梯度混合 TPMS 热沉（Lidinoid / Split-P / Diamond 沿壁面法向堆叠，**孔隙率 82.2%**），
  3D 共轭传热 CFD，**SST k–ω**，**Re 2,000–16,000**
- **数字**：Re=10,000 时 FG-H 的 **Nu=31.93**、压降 **236 Pa**、**PEC=1.75**；
  **相对单一 Diamond 基线**：水力损失**减 52.80%**、冷却性能**好 14.3%**、熵**减 6.43%**、温度不均匀性**降 71.4%**
- ⚠️ 纯 CFD，摘要未提实验验证

**C5. 10.1063/5.0353789**（created 2026-11-02，*Physics of Fluids*）
- "Flow dynamics mechanisms and thermal hydraulic performance evaluation of triply periodic minimal surface (TPMS)…"（截断）
- 作者 Zhenwei Zhang / Qinghai Zhao / Yunyi Ma / Hangyu Sun / 其余未读（待确认）
- **单位原串**：College of Mechanical and Electrical Engineering, **Qingdao University**, Qingdao 266071（Zhao 另有
  National Engineering Research Center for Intelligent Electrical Vehicle Power System, Qingdao University）
- 内容：5 种 TPMS 换热器（Primitive / IWP / Gyroid / Diamond / FRD）对比传统 PCHE，**70% 孔隙率**，**Re 500–3000**，CFD + 增材样件实验验证
- **数字**：Re=500 时 **FRD 总换热量 +69%、总传热系数 +78%**；归一化压降 **IWP 8.6 Pa/W 至 FRD 34.3 Pa/W**
- ⚠️ 与冷板相关性**弱到中**：对象是换热器，**摘要提到电子冷却与电池热管理**，须裁定

**C6. 10.3390/mi17111225**（created 2026-10-26，*Micromachines*）
- "Coupled Multiphysics Optimization of Ball Grid Array with Microchannel Heat Dissipation"
- 作者 Yuqing Dong / Gang Nan / Zhihui Xie / Zhuoqun Lu / 其余待确认
- **单位原串（Crossref）**：College of Power Engineering, **Naval University of Engineering**, Wuhan 430033, China
  （Zhuoqun Lu 另有 School of Energy and Electromechanic Engineering, **Hunan University of Humanities, Science and Technology**…）
- 内容：微通道强制液冷下 **BGA 芯片封装**的热-力耦合，结合构造理论优化焊点形状与布局
- **数字**：最高温差值 **7.8 K**、最大变形差 **5.88×10⁻³ mm**、最大降低比 **74.5%**；矩形环形布局最优
- ⚠️ 相关性**中到弱**，重点在**焊点**而非冷板

## 二、窗口内标题对口、**摘要取不到**的候选（单位原串如下）
| DOI（created） | 标题（Crossref 层，部分截断） | 作者 | 单位原串 |
|---|---|---|---|
| 10.1016/j.ijthermalsci.2026.111477（11-03） | A two-phase microchannel cold plate system for AI data center GPUs: CHF-constrained GPU-HBM co-thermal managem… | Fengzhao Ni; Shihuan Zhang; Haoran Li; Yonghai Zhang; Xiang Ma; Xiaoping Yang; Jinjia Wei; Gang Qu; Peng Liang; Yun Zhu; Shouqing Li | Ni、Zhang：State Key Laboratory of Fluorine & Nitrogen Chemicals, School of Chemical Engineering and Technology, **Xi'an Jiaotong University**, Xi'an, Shaanxi, 710049；Haoran Li：**China United Network Communications Co., Ltd, Shaanxi Branch**；其余未读 |
| 10.1016/j.icheatmasstransfer.2026.113013（11-02） | Enhancement of flow boiling heat transfer in an injection manifold microchannel heat sink based on multi-objec… | Zhiguo Tang; Yanping Dong; Tianyu Li; Yuelong Xu; Yan Li; Jianping Cheng | School of Mechanical Engineering, **Hefei University of Technology**, Hefei |
| 10.1016/j.icheatmasstransfer.2026.113058（11-06） | Numerical investigation and multi-objective optimization of nozzle-jet impingement manifold minichannels for l… | Xiao Cheng; Yuheng Ma; Huiying Wu; Haidong Liu; Liu Liu; Jianjun Zhao | 待确认（两路皆空） |
| 10.1016/j.icheatmasstransfer.2026.113015（11-02） | Thermal-hydraulic performance of an arched pin-fin microchannel heat sink for local hotspot management: Synerg… | Kaihua Zhang; Yi Wang; Kunyan Wang; Bilin Dong; Xiaohu Wu | Henan Key Laboratory of Infrared Spectrum Measures and Applications, School of Optoelectronic Engineering, **Henan Normal University**, Xinxiang 453007 |
| 10.1016/j.icheatmasstransfer.2026.113051（11-06） | Impingement, rib structures, and flow configuration effects on the thermo-hydraulic performance of a combined… | Hind Mahmood; Basim Freegah | Mech. Eng. Dep., Eng. College of **Mustansiriyah University**, Baghdad, Iraq |
| 10.1016/j.icheatmasstransfer.2026.113069（11-07） | Numerical study on hydrothermal performance of a microchannel cooling plate integrating triangular ribs, cylin… | Fan Li; Chunyan Jiang; Tongyong Zhang; Dahai Zhang; Qingguo Fei | 待确认 |
| 10.1016/j.applthermaleng.2026.133927（11-07） | Machine-learning-assisted co-design of diamond microchannel heat sink and packaging for IGBT reliability | Song Yang; Xinlong Zhao; Chenyu Shi; Wenbo Hu; Hongxing Wang | 待确认 |
| 10.1016/j.applthermaleng.2026.133947（11-06） | Physics-guided graph neural networks for prediction and optimization of diamond microchannel heat sinks under… | Jiacheng Han; Linwei Cao; Jingrui Wan; Jinlong Ma; Xiaobing Luo | 待确认 |
| 10.1016/j.applthermaleng.2026.133826（10-27） | Segmented variable hydraulic diameter spiral rib microchannel heat sink performance synergistic prediction and… | Yaoxuan Guo; Chuan Ma; Jiajia Liu; Tiankui Li; Dehao Kong; Qi Lan | Guo/Ma/Kong：College of Mechanical science and Engineering, **Northeast Petroleum University**；Jiajia Liu：**Daqing Oilfield Tianyu Engineering Design Co., Ltd**；Tiankui Li：Special Equipment Emergency Response Department；Lan 未读 |
| 10.1016/j.applthermaleng.2026.133804（10-28） | Interpretable machine learning enabled multi-objective design optimization of fractal-like microchannel heat sin… | Jingbei Bai; Yaojun Li; Pincheng Xiang; Min Chen | Department of Engineering Mechanics, **Tsinghua University**, Beijing, 100084 |
| 10.1016/j.ijheatmasstransfer.2026.129793（11-02） | Research on manifold micro-jet impingement cooling technology for high-power thin-disk lasers | Wang Chenjie; Jiang Guangwen; Yang Sen; Zhang Saile; Qin Lei; Zou Tianqi; Tao Wen-Quan | Wang Chenjie：School of Energy and Power Engineering, Key Laboratory of Thermo-Fluid Science and Engineering of Ministry of Education, **Xi'an Jiaotong University**, Xi'an 710049；并 **Space Technology Department, Xi'an Institute of Optics and Precision Mechanics, Chinese Academy of Sciences**, Xi'an 710119；Jiang Guangwen 同第二单位；其余未读 |
| 10.1016/j.ijheatmasstransfer.2026.129805（10-28） | Experimental study on flow boiling heat transfer in microchannels with heterogeneous wettability modified by f… | Xiao Cheng; Shanshan Pan; Liu Liu; Yongqin Wang; Peng Liu; Haidong Liu | College of Physics and New Energy, **Chongqing University of Technology**, Chongqing 401135；并 The Joint Graduate Training Base … **Chongqing Research Institute of Harbin Institute of Technology**（前两位确认，其余未读） |
| 10.1016/j.icheatmasstransfer.2026.112941（10-26） | Inverse Marangoni effect enhances thermal performance in self-driven microchannel heat sink with self-rewettin… | Yu-Bin Dai; Yi-Tao Shen; Bao-Yu Yang; Hua Chen; Wen-Long Cheng | Dai/Shen/Chen：Department of Thermal Science and Energy Engineering, **University of Science and Technology of China**, Hefei 230027；Baoyu Yang：**Shanghai Institute of Technical Physics, CAS**, Shanghai 200083；Cheng 未读 |
| 10.1016/j.icheatmasstransfer.2026.112935（10-26） | Synergistic thermo-hydraulic enhancement and temperature uniformity in wave microchannel heat sinks using fan-… | Yuanping Yu; Jing Sun; Yujiao Zhang; Qing Cheng | School of Energy Science and Engineering, **Nanjing Tech University**, Nanjing 211816 |
| 10.1016/j.applthermaleng.2026.133954（11-06） | Experimental study on flow boiling characteristics in variable cross-section porous minichannels with trapezoi… | Huiqing Shang; Guodong Xia; Lei Xu; Wenbin Zhou; Jiahui Tang | 待确认 |
| 10.1016/j.energy.2026.142970（10-27） | Flow boiling in microchannels with progressive cross-sectional expansion: Effects on vapor migration and therm… | Qingjie Zhao; Jiaxuan Ma; Shuo Cui; Jiabo Zhang; Kang Tu; Dawei Tang | School of Energy and Power Engineering, **Dalian University of Technology**, Dalian 116023 |
| 10.1109/tcpmt.2026.3751096（11-06） | A Network Model for Liquid Cooling in Data Center Servers utilizing an ML Model for Evaporative Chip Cooling | Kartik Upadhyay; Sumanta Acharya | **Illinois Institute of Technology**（Crossref 原串） |
| 10.1016/j.ijthermalsci.2026.111453（10-26） | Jet-assisted single-phase immersion liquid cooling for heterogeneous chiplet packages: parametric CFD study on… | Hye Won Kim; Jeong-Heon Shin | Department of Mechanical & System Design Engineering, **Hongik University**, 94 Wausan-ro, Seoul, Mapo-gu, 04066, Republic of Korea |
| 10.1007/s12217-026-10301-z（11-03） | Computational Analysis of Thermal-Fluid Performance in Microchannel Liquid Cooling Plates | Muhammad Shahryar; Muhammad Fahadyar | Shahryar：Department of Mechanical Engineering, **University of Engineering and Technology, Lahore** 54890, Pakistan；并 School of Energy and Power Engineering, **Xi'an Jiaotong University**；Fahadyar 为 Lahore 那一家 |
| 10.1016/j.ijheatfluidflow.2026.110766（10-25） | Coupled slip-cavity effects on flow and heat transfer in microchannel heat sinks for aerospace electronics coo… | Yi Huang; Chaozhi Liang; Xingcong Zhan; Weidong Fang; Xiaojie Zhuang; Qiaoling Kong; Haiwang Li | National Key Laboratory of Science and Technology On Aero-Engine Aero-Thermodynamics, Research Institute of Aero-Engine, **Beihang University**, Beijing 100191 |

补充：111477 标题层面最贴合本刊主线但摘要取不到；110766 场景是**航空**电子、覆盖面存疑；111453 是**浸没式**而非冷板、边缘对口。

## 三、窗口内对口度较低、未取摘要
10.54254/2755-2721/2026.38315、10.3390/fluids11110276、10.3390/en19215079、10.1007/s13369-026-11719-8、
10.1007/s11630-026-2384-6、10.1140/epjp/s13360-026-08486-8、10.1002/htj.70403（微通道热沉被动强化综述）、
10.1007/s44562-026-00003-8（硅基微通道制造综述，含芯片冷却）、10.1016/j.applthermaleng.2026.133796、10.1177/09544089261502680（空气+PCM，非液冷）。

## 四、已见并排除
电池包冷板 10.2139/ssrn.7674864、10.2139/ssrn.7674328；电机/发动机冷却 10.1016/j.icheatmasstransfer.2026.112929（发动机冷板拓扑优化）、
10.1109/icem68283.2026.11757550（牵引电机直接液冷）；光伏冷却 10.1016/j.rineng.2026.114005 等；辐射冷却类。

## 五、顺带确认：133678 英文标题原文
**"Data-efficient multi-objective structural optimization and design space exploration of refrigerant-based cold plate for laser device"**
（Crossref `title` 与 OpenAlex `title` 两处字面一致。）

## 六、本轮未覆盖
取不到摘要的条目未退回原文页（ScienceDirect 不可达）；未重跑 arXiv；未逐刊 ISSN 扫描；未做厂商/新闻/会议面。
