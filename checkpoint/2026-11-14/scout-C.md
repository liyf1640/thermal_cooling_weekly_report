# scout-C（仿真方法）· 第 13 期 · 窗 2026-11-08~11-14

**本期未检出。** 没有候选通过覆盖面闸门。

已扫的源：
- arXiv API（export.arxiv.org，按 submittedDate 限窗）。关键词：heat sink、cold plate、conjugate heat transfer、microchannel、
  liquid cooling、data center cooling、heat transfer 与 neural/surrogate/operator/ROM/differentiable/GPU 的组合、
  neural operator 全量、temperature field、thermal management、PINN+heat
- Crossref（按 created 限窗）。查询：cold plate / heat sink / microchannel 的 neural surrogate 与 ML、
  PINN conjugate heat transfer、chip thermal GPU
- WebSearch 无窗内新命中
- 未能扫到的源：ScienceDirect 403；CMAME / JCP / IJHMT / ATE 未逐刊查，仅经 Crossref 关键词覆盖
  （Crossref 对 "physics-informed surrogate heat sink" 一类查询覆盖不全，有漏检可能）
- 已核去重清单，窗内无命中，未回传主代理列出的已处理项

被排除的近邻命中（均未过闸，不建议收）：
1. arXiv:2611.16341 SUMNO（Spatially Unrolled Multigrid Neural Operator for Fluid Flow Surrogates），v1 2026-11-12，预印本。
   摘要只有 "fluid flow fields"，四个流动基准，无传热/温度场，未提冷板或芯片 → 纯流体算例，排除
2. arXiv:2611.12424 PINN 小数据对比（H-PINN），v1 2026-11-09。算例为热方程与两相渗流，无冷板/芯片/电子散热语境 → 排除
3. arXiv:2611.11716 "Rapid Heat Removal from Chip Cores: Near-Junction Active Cooling of Power Transistors via Electron
   Entropy Transport and Spatial Decoupling"，v1 2026-11-09。属器件物理/新型冷却概念，不是仿真方法，未取摘要核；
   可转其他角度当线索
4. 10.1016/j.compfluid.2026.107342 GPU 加速混合简化格子 Boltzmann 求解器（湍流热流）。作者 Kiran Sivadas、Kameswararao Anupindi。
   Crossref 无摘要，无冷板/电子散热依据 → 相关性弱，不收
5. 10.53365/nrfhh.4472 圆管湍流 Nu 与摩擦因数的混合 ML-CFD 框架。算例为光滑圆管；摘要自称「将进行」仿真、性能声明待完成 → 不收
6. 10.1016/j.rineng.2026.114102（PCM 椭圆针肋热沉）、10.1038/s44435-026-00023-4（斜切肋微通道数值）、
   10.3390/surfaces9040094（微通道阵列射流冲击热沉）：均为常规 CFD 参数研究，不属仿真方法角度；冷板相关，已转 A/B 评估
7. 10.1016/j.measurement.2026.123850 功率驱动器件退化建模（PINN）→ 属寿命退化，非传热建模，排除
