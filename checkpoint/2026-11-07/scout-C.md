# Scout C（仿真方法）第 12 期回传

窗口 2026-10-25 ~ 2026-11-07。

## 特别指派：HAWFNO（10.1016/j.icheatmasstransfer.2026.112841）—— 摘要仍取不到，结论：仍不能上站
- 已试：OpenAlex 单篇端点（`abstract_inverted_index` 空）、Crossref（无 abstract 字段、作者 affiliation 为空）、
  `fetch_source.py`（只有题名/作者/容器）、doi.org（代理 403）、WebSearch（零命中）。ScienceDirect 不可达。
- Crossref created 2026-10-19，**本身也在本期窗口之前**。
- 作者（Crossref）：Hanyun Huang / Xiaobin Mu / Xiaokui Sang / Dongqi Zou / Yanxin Ren / Nana Duan。
  单位沿用上期已核的「西安交通大学 电气工程学院 + 中国电力科学研究院」，本次未能重新核到。
- **算例是否为电子冷却或冷板：无法判定。** 题名里的 "conjugate heat transfer" 与 "hot-spot" 不能当内容依据。
  按覆盖面闸门**应否决**。

## 窗内候选
arXiv 窗内检索（cold plate / heat sink / electronics cooling / microchannel / conjugate heat transfer / chip，
各自与 neural operator / surrogate / PINN / ROM / differentiable 组合，走 export.arxiv.org）：
**2026-10-20 之后无任何相关条目。** 以下候选全部来自 Crossref 按 created 检索。

### 候选 1 · 10.3176/proc.2026.4.08（created 2026-11-02）—— 有摘要，但领域存疑
"Additive manufacturing-aware topology optimization of cooling channels using a reduced-order cold plate model for electric machine water jackets"
- URL https://doi.org/10.3176/proc.2026.4.08 ；*Proceedings of the Estonian Academy of Sciences*
- 作者 Yang Zhang / Martin Sarap / Toomas Vaimann / Ants Kallaste；OpenAlex 全部标为 Tallinn University of Technology（Crossref 无单位，**待确认**）
- 方法：基于降阶冷板模型的密度法拓扑优化 + 制造性正则化；**二维算例**
- 关键数字：**摘要只有定性结论、无数值**。「更强正则化降低界面复杂度与流体面积占比，同时水力阻力上升、热性能下降」；
  「sharp-interface 重分析显示整体热响应吻合良好，但局部峰值温度与水力导度对密度法表示敏感」。
  ⚠️ 对照基准是**同一模型的 sharp-interface 重分析，属内部对照、不是对外比较**。
- 相关性：**存疑**——摘要明确写了 "reduced-order cold plate model"，但**应用对象是电机水套、不是电子芯片散热**；
  也不是 ML 方法，属降阶模型 + 拓扑优化。**请主编裁定。**
- 摘要经 Crossref 与 OpenAlex 双路核到。

### 候选 2 · 10.1016/j.energy.2026.142940（created 2026-10-27）—— 摘要未核
"A region-aware physics-informed deep neural network for temperature-field reconstruction and cooling optimization of electric-vehicle liquid-cooled SiC power modules"
- 作者 Youyou Gao / Xing Xu / Cong Liang / Heping Ling；OpenAlex：Jiangsu University（前三位）、BYD (China)（Heping Ling）；Crossref 无单位
- 关键数字：**未取到，摘要三路全缺**
- 相关性：题名直写液冷功率模块，强相关；但**摘要未核到，不满足闸门「摘要明确涉及」**。
  ⚠️ 另注：题名含 **electric-vehicle**，可能触及「电动汽车不在覆盖面」的边界。

### 候选 3 · 10.1016/j.applthermaleng.2026.133927（created 2026-11-07）—— 摘要未核
"Machine-learning-assisted co-design of diamond microchannel heat sink and packaging for IGBT reliability"
- 作者 Song Yang / Xinlong Zhao / Chenyu Shi / Wenbo Hu / Hongxing Wang；Crossref 与 OpenAlex 单位均空，待确认
- 关键数字：未取到，无摘要
- 相关性：电子散热对象明确（IGBT 微通道热沉），但很可能是 ML 驱动的设计优化、不一定是仿真方法学；**仅凭题名，存疑**

## 检索中见到但不回传
- 10.1016/j.icheatmasstransfer.2026.112891（热传导神经算子的共形不确定性带）：两路无摘要，题名无电子/冷板，通用类，不收
- 10.1016/j.icheatmasstransfer.2026.112954（干燥过程 PINN）：非电子散热，不收
- 10.1063/5.0356861（圆柱绕流热流 PINN）：通用算例，不收
- 10.1016/j.applthermaleng.2026.133826（螺旋肋微通道热沉性能预测与多目标优化）：题名涉 ML，但无摘要、无证据为仿真方法学，未深查
- arXiv 窗内无满足闸门的冷板/芯片类 ML-for-CFD 预印本。窗外见 "Generative Design for Direct-to-Chip Liquid Cooling for Data Centers"（2026-04-13）
  与 CFDTwin（2026-05-26，POD-NN 代理，涉 ANSYS Fluent），**均在窗外、未取全文、不回传**

## 未取到
Elsevier 摘要在所有可达通道都缺 → 候选 2、3 与 HAWFNO 均需 ScienceDirect 权限才能核摘要。
**按严格闸门，本期仅候选 1 有摘要原文可引证，且相关性存疑。**
