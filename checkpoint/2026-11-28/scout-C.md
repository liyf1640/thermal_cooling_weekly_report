# scout-C · 仿真方法（原样回传，含补扫）

窗口 2026-11-22 ~ 11-28。**窗口内没有检出直接做「冷板内对流换热 + ML/神经算子」的新增论文。**
扫描方式：arXiv Atom API 按 submittedDate 限定，两组关键词，共约 125 条标题；未单独扫 Crossref、未做 WebSearch。

## arXiv 尾部三天（11-26 ~ 11-28）：取不到，非「检了没有」
- `submittedDate:[202611260000 TO 202611282359]` → totalResults **0**
- 放宽到 `[202611250000 TO 202611302359]` → 1391 条，按提交时间降序，最新一条为 **2026-11-25T18:59:59Z**（2611.34945）
- 结论：**API 当前最大可见提交日是 11-25**；11-25 19:00Z 之后无任何论文入库。
- → **arXiv 覆盖本期截至 11-25**，11-26~11-28 三天未覆盖（索引滞后，不能排除漏检）。

## 候选 1 · MicroChanNet（上期挂账，摘要仍零获取）
- 标题：Fast multi-layer thermal prediction for microchannel-cooled 3D ICs: MicroChanNet
- 作者：Jinfeng Zhao; Zihan Ke; Zhenjie Yao; Xiaoning Ma; Kunlong An; Hao He; He Cao; Jianyun Liu; Zeyu Sun; Zhiqiang Li; Qinzhi Xu（Crossref）
- 单位：OpenAlex 机构匹配给 Chinese Academy of Sciences / Institute of Microelectronics / UCAS —— **非从原文读到，建议标「待确认」**
- 日期：Crossref created 2026-11-17（**窗外**）；OpenAlex publication_date 2026-11-17；Crossref published 2027-03 为期卷日期，不作依据
- 关键数字：**无。OpenAlex `abstract_inverted_index` 仍为 null，摘要零获取，未编造**
- 相关性：强（仅据标题）· 来源：https://doi.org/10.1016/j.ijthermalsci.2026.111493

## 候选 2 · 神经算子加速声子 BTE-Fourier 双向耦合（硅鳍阵列）
- 标题：Neural-operator acceleration of bidirectional phonon Boltzmann-Fourier coupling for multiscale heat transport in silicon fin arrays
- 作者：Ruthwik Chivukula; Khemraj Shukla; George Em Karniadakis。单位待确认（arXiv 元数据无单位）
- 日期：2026-11-23
- 关键数字（原文摘要）：DeepONet 替代鳍内声子 BTE 求解，与基底 Fourier 模型做 Schwarz 迭代耦合（带 Aitken 松弛）；100 根硅鳍 3D 理想阵列，留出开关工况下与直接 BTE-Fourier 参考相比**最大温差 0.3 K、热流相对差 0.6%**；耦合代理约 **50 s** 对直接耦合 **2 h 28 min**，约 **180 倍**加速（不含一次性基底分解）
- 相关性：**弱** —— 涉半导体器件局部发热与硅鳍热扩散，**无对流、无冷板**，摘要不含电子冷却字样 → 按「相关方法（线索）」处理
- 来源：https://arxiv.org/abs/2611.31542（arXiv:2611.31542）· 核验状态：已用 fetch_source 取原文摘要核

## 候选 3 · CycleWalker：2.5D/3D IC 周期热分析随机游走求解器
- 标题：Walk the Cycle: An Efficient Stochastic Solver for Periodic Thermal Analysis of 2.5D/3D ICs
- 作者：Shengnan Cai; Qibo Xue; Tianshu Hou; Tianxiang Zhu; Zixiao Wang; Yibo Lin; Runsheng Wang; Bei Yu。单位待确认
- 日期：2026-11-24
- 关键数字：周期性 2.5D/3D IC 基准上，同等精度下相对瞬态随机游走求解器**最高加速 75.85 倍**；方法为周期残差随机游走 + Russian roulette 缩短历史，构建带 TSV 的热图
- 相关性：**弱** —— 芯片级导热求解，无冷板、无对流，也不是 ML
- 来源：https://arxiv.org/abs/2611.32082 · 核验状态：已核摘要

## 候选 4 · 随机森林预测的 PCM 铜泡沫混合散热器（Raspberry Pi 5）
- 标题：Machine-Learning-Assisted Hybrid Cooling of a Raspberry Pi 5
- 作者：Abdallah Ghazal; Fazal Hameed; Elshafey Elshafey; Mohammad Awadallah; Alhasan Emam。单位待确认
- 日期：2026-11-24
- 关键数字：随机森林回归预测 CPU 温度用于自适应风扇控制；约 99% CPU 负载下峰值 CPU 温度比 PCM-铜泡沫被动方案低约 **9 °C**、比商用主动散热器低约 **6 °C**
- 相关性：**弱** —— 属电子散热但是实验+控制、非高保真建模；**复核确认摘要中无液冷或冷板字样**（仅 PCM 石蜡、铜泡沫、自适应风扇、商用主动散热器）→ **本期不收**
- 来源：https://arxiv.org/abs/2611.32047 · 核验状态：已核摘要

## 上期挂账两条 OpenAlex 重试（均仍零摘要）
- `10.1016/j.ijthermalsci.2026.111493`（MicroChanNet）：`abstract_inverted_index` 仍 null
- `10.1016/j.ijthermalsci.2026.111490`：标题 Synergistic thermal management of radio frequency chips under pulsed heat loads using phase change materials and variable aspect ratio microchannel heat sink；作者 Bo Xu; Ci Ao; Xin Wang; Zhenqian Chen；OpenAlex 机构匹配 Southeast University（**建议标待确认**）；publication_date 2026-11-18，Crossref 另有 2027-03 期卷日期（不作依据）；`abstract_inverted_index` **仍 null**。该文属实验/数值研究，不属 C 角度 ML 范畴
- 两条均**不是窗口内新增**（11-17 / 11-18 早于 11-22），也**无可引用关键数字** → 只能作标题级线索

## 已看过但不收（标题命中通用神经算子/PINN，无电子散热字面关联，按 2026-11-02 裁定）
CoMNO（2611.32274）、FMSNO（2611.30341）、SPARK（2611.31834）、物理信息 FNO 浮式风机尾流重建（2611.31789）、涡脱落 PINN（2611.33489）、元求解器多智能体（2611.31611）、PDE 求解器输出验证（2611.31211）。
HAWFNO（10.1016/j.icheatmasstransfer.2026.112841）本期未再检索。
