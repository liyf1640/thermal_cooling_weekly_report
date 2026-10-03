# 散热 / 冷板 相关学者名单

> 本页只收录散热 / 冷板相关学者。原跨研究线（玻璃保护膜、自愈合材料）条目已移除。
> 字段：姓名 / 单位 / 研究方向 / 已收录论文 / 备注。单位以原文核实为准，未核到的标"待确认"。

## 冷板仿真 / CFD / ML-for-simulation
| 姓名 | 单位 | 研究方向 | 已收录论文 | 备注 |
|---|---|---|---|---|
| Hongying Li（通讯作者） | **NTU 机械与航空航天工程学院**（读 arXiv PDF 致谢确认；合作者含 A*STAR IHPC 的 Chang Wei Kang、NVIDIA 的 Simon See、帝国理工 Heaney/Pain） | 神经-物理 CFD、湍流建模、可微分求解器 | **NeuralFVM**（Neural-physics FVM，湍流 k-ω，GPU 加速 19–46×；arXiv 2603.21869；作者逐位核）— **已收录第 4 期(08-23)** | "神经网络+CFD/湍流方法"已入每期检索角度 |
| Peng Zhang（张鹏，通讯作者） | **上海交通大学 制冷与低温研究所**（第6期 arXiv PDF 首页核；合作者 Zixu Han 同所） | 液冷板拓扑优化：分形几何 TO、场协同对流换热 TO | **FGTO**（arXiv 2603.26437）— 第2期(08-10)；**CTO 场协同+分形几何液冷板**（arXiv 2609.12344 / *Energy* 2026，DOI 10.1016/j.energy.2026.142364）— **第6期(09-16)** | 同一团队连续方法演进（面积→换热系数）；第2期所记职称/高被引身份未在第6期重核 |
| Xin Zhang、Fu-Yun Zhao 等 7 人团队（**通讯作者未核**） | **武汉大学 动力与机械学院**（Xin Zhang、Ji Zeng、Jiang-Hua Guo、Xian-Fei Liu、Fu-Yun Zhao）；**长江大学 石油工程学院**（Wei-Wei Wang）；**湖南工业大学 土木工程学院**（Fu-Yun Zhao 兼）；**Tomsk State University 对流传热传质实验室**（Mikhail A. Sheremet，俄罗斯）。单位据出版商向 Crossref 交存的原始机构串逐位核 | 液冷板拓扑演化 + 场协同解释（受限电池冷板 BTMS） | **受限电池液冷板拓扑演化与场协同解释**（DOI 10.1063/5.0348932，*Physics of Fluids* 38(9) 093616，在线 2026-09-24）— **第7期(09-26)** | 与上一行上海交大团队**无人员重合**，虽同用场协同框架但属独立工作；对象是**电池冷板非芯片冷板**。注：OpenAlex 给该团队误挂「Hubei University」，以出版商原串 Wuhan University 为准 |

| **Zhiyao Jiang**（第一）、Wei Xiao、Weiheng Li、**Bai Song**（**通讯作者未取到，待确认**） | **北京大学 工学院力学与工程科学系**（北京 100871）；Jiang / Xiao / Song 三人另兼 **微纳加工技术国家级重点实验室**。单位据 OpenAlex 的出版商原始机构串逐位核（Crossref affiliation 为空） | 嵌入式歧管微针肋（MPF）热沉三维数值研究；千瓦每平方厘米级芯片冷却 | **嵌入式 HU 型歧管微针肋热沉**（DOI 10.1016/j.ijheatmasstransfer.2026.129613，*IJHMT* Vol.273 文章号 129613，Crossref created 2026-09-28，在线先行）—— **第8期(10-03)** | 2000 W/cm² 下菱形截面针肋 ΔT_max 56 K / ΔP 28 kPa / COP>2000，相对常规微通道基准热与流同时更优。纯数值无实验；**COP 定义式原文未给**；摘要经 OpenAlex，ScienceDirect 因出口限制未直读复核 |
| **Yuwei Liu**（第一）、Jintao Liu、Wenwei Jiang、Yuanzhi Sun；**Jinghui Liang**；**Changhui Chen**（**通讯作者未取到，待确认**） | **中国矿业大学（北京）机电与信息工程学院**（北京 100083，前四人）；**北京海纳川汽车部件股份有限公司**（北京 100176，Liang）；**北汽动力总成有限公司**（北京 101100，Chen）。单位据 OpenAlex 的出版商原始机构串逐位核 | 微通道流-热双目标拓扑优化；场协同 + 㶲耗散 + 熵产三判据评价 | **场协同+㶲耗散+熵产三判据的微通道拓扑优化**（DOI 10.1016/j.applthermaleng.2026.133471，*ATE* Vol.308 文章号 133471，Crossref created 2026-09-30，在线先行）—— **第8期(10-03)** | **高校 + 北汽系两家企业的产学合作**；**本期唯一带实验验证**的拓扑优化条目。在所考察最高 Re 下压降相对 CSMC −31.54% / 相对 PSMC −30.09%，最高温升 −40.48% / −17.72%——**「最高 Re」具体值原文未给，不可读作全工况结论**。与第6期上海交大 Zixu Han/Peng Zhang 的 CTO（DOI 10.1016/j.energy.2026.142364）**作者与机构零重合，属独立工作** |
| **Ge Gao**（第一）、Guangze Li、Yuhui Wang、Liuyong Chang、Longfei Chen、**Feng Han**、**Pedro David Bravo-Mosquera**（**通讯作者未取到，待确认**） | **北京航空航天大学杭州国际创新研究院**（杭州 311115，前五人；Gao 兼**北航 航空科学与工程学院**；Li/Chang/Chen 兼**天目山实验室**）；**南京航空航天大学 能源与动力学院**（Han）；**圣保罗大学圣卡洛斯工程学院 航空工程系**（Bravo-Mosquera，**巴西**）。共 7 人 5 家机构，单位据出版商向 Crossref 交存的原始机构串逐位核 | 仿生（鲨鱼皮）翅片微通道热沉；Görtler 型二次流强化；realizable k–ε 高保真湍流仿真 | **仿鲨鱼皮翅片微通道热沉**（DOI 10.1063/5.0347413，*Physics of Fluids* 38(10) 105103，在线 2026-10-01，**已正式刊出**）—— **第8期(10-03)** | 相对同体积矩形翅片（限 5mm/8mm 两构型），流阻在所考察全部 Re 范围一致 −26~35%，Re>约 2130 后换热最大 +16%，PEC 峰值 +31%（原文措辞，PEC 通常为无量纲比值，本刊原样引用不换算）。纯数值无实验；**Re 区间与工质均未给**。注：机构串 "Hangzhou International Innovation Institute" 原文带 "Beihang University" 后缀，**不可拆成独立机构** |

## 冷板制造工艺
| 姓名 | 单位 | 研究方向 | 已收录论文 | 备注 |
|---|---|---|---|---|
| Mehmet Canberk Bacikoglu、Ulaş Yaman | **Aselsan Inc. 雷达与电子战系统**（Bacikoglu，土耳其安卡拉）；**中东技术大学 METU 机械工程系**（Yaman，兼 METU 焊接技术与无损检测中心）。单位据 Springer 文章页 citation_author_institution 核 | 铜冷板增材成形（M-FFF）与 SLM / FSW 工艺的性能对比 | **M-FFF 铜冷板性能评价**（DOI 10.1007/s00170-025-17246-4，*Int. J. Adv. Manuf. Technol.* 146(3) 1621–1628，在线 2026-01-20）— **第7期(09-26) 窗口外补记** | 本刊迄今第一篇把 **FSW 冷板作实测对照基准**的同行评审论文（见 [公司清单](companies.md) 缺口表 FSW 行）；第一作者属**工业界 Aselsan**，非 METU——按人名推断单位会写错 |

## 两相 / 直触芯片冷板实验
| 姓名 | 单位 | 研究方向 | 已收录论文 | 备注 |
|---|---|---|---|---|
| **Wookyoung Kim**（第一，**单位待确认**）、**Kyeonghui Hong**、**Jinsub Kim**、**Kong Hoon Lee**（**单位待确认**） | **韩国科学技术联合大学院大学（UST）**（Hong）；**韩国机械与材料研究院（KIMM）**（J. Kim）。**第一作者与末位作者单位取不到，标待确认——本刊不以同篇合作者单位代入推定** | 低 GWP 制冷剂两相直触芯片（D2C）针肋冷板；系统压力/约化压力对热阻构成的影响；无拟合常数热阻模型 | **系统压力对两相 D2C 针肋冷板热阻与泵功的影响**（DOI 10.2139/ssrn.7536705，**SSRN 预印本、未同行评审**，Crossref created 2026-09-28）—— **第8期(10-03)** | **实测**（高速摄影+测温）：铜冷板加热足迹 25.4×25.4 mm，R1233zd(E)/R1234ze(E)/R1234yf，入口 40 °C，45 W~标称 1 kW，0.152~2.235 kg/min，过冷度 1.8~39.9 K；COP 随过冷度约 +5~7 %/K（1.0 kg/min）；无拟合常数热阻模型在标称 1 kW 下精度 ±11%；3 kW/85 °C 推算允许过冷度约 19~27 K（**模型推算非实测**）。**摘要未给任何绝对热阻（K/W）与绝对泵功（W）值** |
| **Xingpu Feng**（第一）、Yiming Liang、**Sanli Liu**、**Yuqi Liu**、**Simon Maher**、**Min Chen** | **西交利物浦大学 School of Advanced Technology**（苏州 215123；Feng / Liang / Chen，Sanli Liu 兼）；**中国科学院沈阳自动化研究所**（沈阳 110169；Yuqi Liu，Sanli Liu 兼）；**英国利物浦大学 电气工程与电子系**（Maher） | MoE-PINN 微通道冷却场实时重建 | **MoE-PINN 微通道实时场重建**（DOI 10.1016/j.engappai.2026.115892，*Eng. Appl. of AI* Vol.182 文章号 115892，Crossref created 2026-08-08）—— 第7期(09-26) 挂账，**第8期(10-03) 补全单位并结清** | 三方合作（西交利物浦 + 中科院沈自所 + 英国利物浦）。**性能数字确认无法取得**：Crossref 列表路由（含 select=abstract）返回记录中不存在 abstract 字段（出版商从未交存摘要）、OpenAlex 摘要索引为空、ScienceDirect 受出口限制不可达。本刊不再追该篇数字 |

---
维护规则：新收录某散热/冷板学者论文 → 在对应研究线补/更新一行（含论文 + 出处），单位以原文核实。非散热主题（玻璃/自愈等）不在本频道清单收录。参见 [公司 / 企业清单](companies.md)。
