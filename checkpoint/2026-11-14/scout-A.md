# scout-A（冷板仿真与设计）· 第 13 期 · 窗 2026-11-08~11-14

扫过的源：Crossref created 过滤（10 组英文 query）、arXiv API（4 组 query，窗口内 v1 为 0 条）、OpenAlex 单篇端点补摘要。
已对 reported-index 与 11 个「只缺摘要」DOI 查重，以下均不在其中。边缘（created 11-05~11-07）未检出。

## 过闸门、摘要已取到

### 候选 1 · 冷板 + 纳流体离子热电（芯片冷却 + 余热发电）
- Nanofluidic ionic thermoelectric energy conversion integrated with a pin-fin based cold plate for electronic chip cooling
- DOI 10.1016/j.enss.2026.100194 ; https://doi.org/10.1016/j.enss.2026.100194
- created 2026-11-10 ; Energy Storage and Saving（2026-11，卷期号未取到）
- 数字：电子热流密度 7,000 W·m⁻² 时针肋冷板将芯片表面温度维持在约 53.25 °C，NITEC 输出功率密度 97.72 mW·m⁻²；
  电解液 0.05 M、pH 3→11 时最大输出功率密度 52.09→118.83 mW·m⁻²
- 作者 Yongbo Dong / Qiongyao Cui / Yu Qian / Ye Chen / Qinlong Ren（Crossref 无单位，待确认）
- 闸门依据："...integrated with a pin-fin-based cold plate for simultaneous electronic-chip cooling and waste-heat harvesting."
- 摘要经 OpenAlex 单篇端点取得（Crossref 无）。备注：做的是热电转换系统，冷板只是载体，相关性中

### 候选 2 · 微通道阵列射流冲击 + 多孔骨架热沉（含样机验证）
- Numerical Investigation of Flow and Thermal Performance of a Microchannel Array Jet Impingement Heat Sink with Porous-Skeleton Enhanced Surface Cooling: Experimental Validation and Parametric Analysis
- DOI 10.3390/surfaces9040094 ; created 2026-11-09（Crossref published 2026-11-06）; Surfaces（MDPI）9(4)
- 数字：摘要只有定性结论与参数范围；多孔骨架厚 0.15 mm；样机实测出口流速、液温与仿真吻合，偏差在传感器精度内
- 作者 Jia-ao Dai / Xiaoshuo Liu（Shandong Technology and Business University, School of Information and Electronic Engineering）
- 闸门依据："...integrating array jet impingement with microchannel heat sinks (MCJHSs) for high-performance electronic thermal management..."
- 摘要末尾被截断

### 候选 3 · 面向空间光电系统的分区液冷板（含实验验证）
- Thermo-hydraulic performance of a partitioned liquid cooling plate under highly non-uniform heat fluxes for space applications
- DOI 10.1088/2631-8695/aebd48 ; created 2026-11-10（published 2026-11-01）; Engineering Research Express
- 数字：热沉界面最大温差从 4.41 K 降到 1.50 K；蛇形流道为高热流区最优；实验平台验证数值模型
- 作者 Yinlin Li / Junjun Qin / Yonglin Bai / Caixia Liu / Jiatao Wang（中科院西安光机所等）
- 闸门依据："Space-borne optoelectronic systems operating in extreme orbital thermal environments face significant challenges
  due to localized high heat fluxes and strict temperature uniformity requirements."
- 备注：对象是空间相机光电器件，算「光电/电子器件冷板」；航天应用，由主代理裁定

### 候选 4 · 横向肋条微通道热沉 CFD（COMSOL）
- Thermal–hydraulic performance of transverse ridge geometries in water-cooled microchannel heat sinks
- DOI 10.3389/fmech.2026.1965238 ; created 2026-11-12 ; Frontiers in Mechanical Engineering
- 数字：2D 共轭传热，135 个肋条通道算例 + 5 个光滑参考；肋高 e=0.05–0.15 mm，节距 0.25–0.50 mm，Re=100–1000；
  结果段在 fetch 输出中被截断，增益数字未取到
- 作者 Joseph Marcello / Sumith Yesudasan（University of New Haven, Mechanical and Industrial Engineering Department）
- 闸门依据（偏弱，引言泛提一句）："Liquid-cooled microchannels offer an effective approach to removing high heat loads from compact electronic systems."

### 候选 5 · 面向芯片散热的热沉温度场 ML 实时预测（ASME FEDSM 会议）
- Machine Learning Applied for Instant Predictions of Spatial Temperature Variations in Heat Sinks for Computer Chip Cooling
- DOI 10.1115/fedsm2026-184041 ; created 2026-11-13（published 2026-07-26 为会期名义日期）
- ASME FEDSM2026，Volume 1: Artificial Intelligence (AI) for Fluids; CFD Methods; …
- 数字：OpenFOAM chtMultiRegionFoam 作训练数据，与理论解误差 <1%；训练约 2 小时；预测耗时数字在截断处未取到
- 作者 Ayush Jha / Reetu Thimmaiah / Isaac Perez-Raya（Rochester Institute of Technology）
- 备注：对象是 chip + 铝翅片空冷热沉（h=125 W/m²K），不是液冷冷板；方法是全连接网络代理，相关性弱到中

### 候选 6 · AI 服务器冷板的嵌入式柔性 MEMS 微传感器原位表征（实验，非仿真）
- In Situ Characterization of Local Thermal–Hydraulic Characteristics in a Liquid-Cooling Cold Plate for AI Servers Using an Embedded Flexible MEMS Microsensor
- DOI 10.3390/mi17111312 ; created 2026-11-12 ; Micromachines（MDPI）
- 数字：商用冷板，流量 2–4 L/min；进出口局部温差由约 4.8 降到 3.2 °C，3 L/min 时约 4.4 °C；
  120 h 循环测试后温度/流量/压力灵敏度分别下降 7.2%、5.4%、4.7%
- 作者 Chi-Yuan Lee / Kuo-Chung Lee / Ying-Shuo Luo / Wei-Ting Lin / Chia-Te Hung
  （Yuan Ze University 机械工程系；Kuo-Chung Lee 为 CerTone Heat Solution Co., Ltd., Hsinchu）
- 备注：属监测/传感，不是设计优化，主代理可另归节

### 候选 7 · 微间隙 / 多微通道 / 微针肋沸腾对比（HFE-7100，实验）
- Comparative Assessment of Micro-Scale Heat Exchangers Operating in Flow Boiling
- DOI 10.21203/rs.3.rs-11578799/v1 ; created 2026-11-13 ; Research Square 预印本，未经同行评审
- 数字：工质 HFE-7100，入口 1 bar、过冷度 5 K，质量流速 100–300 kg/m²s，壁面热流最高 0.324 MW/m²；
  微针肋热沉性能最好且抑制流动反向与不稳定；针肋压降较高
- 作者 Ali H. Al-Zaidi（University of Misan）/ Tassos G. Karayiannis（Brunel University of London）
- 闸门依据："The increasing demand to dissipate high heat fluxes from small areas in electronic equipment necessitated
  the move from air-cooled to liquid-cooled heat sinks and now to heat sinks operating in flow boiling."

## 摘要未取到、需 verifier 复核（fetch_source/Crossref、OpenAlex 单篇均无；ScienceDirect 403）
- 候选 8 · Microstructure-controlled transport regimes in dielectric-fluid microchannel flow boiling
  DOI 10.1016/j.ijheatmasstransfer.2026.129821，created 2026-11-10，IJHMT（Crossref 记 2027-03 期）
  作者 Fitsum H. Natnael / Harsh Shah / Yangying Zhu（单位待确认）
- 候选 9 · Design and Thermo-Fluid Performance Optimization of a Hybrid-Enhanced Cooling Surface with a Piezoelectric Multi-Jet Array
  DOI 10.1016/j.energy.2026.142969，created 2026-11-10，Energy
  作者 Yilin Zhong / Feilong Liu / Xiaohua Wu / Yuankai Yang / Yongshen Zhou / Zhaoyang Yan / Longsheng Lu / Shu Yang / Di Xing / Yingxi Xie
- 候选 10 · Exploratory numerical insights of surface and through-thickness thermal response of high heat flux devices
  deploying innovative hybrid nanofluid impingement cooling technique
  DOI 10.1016/j.rineng.2026.114145，created 2026-11-12，Results in Engineering
  作者 Muhammad Asim / Sheheryar Khan / Farooq Riaz Siddiqui / Hussain Sallar / Fahid Riaz

## 摘要已取到或可判断、但未过闸门（scout 建议不收）
- 10.1038/s44435-026-00023-4（npj Thermal Sci. Eng.，created 2026-11-11）Kangude & Robinson，oblique-cut-fin 微通道热沉 CHT 仿真。
  数字：PC_3_30° 的 PI = 1.30–1.54，换热系数最高 +40%，压降最多 −18%。摘要只写 "high heat-flux thermal management"，
  无 electronic / chip 字样，按从严口径不过闸门；若主代理放宽可作强相关设计类候选
- 10.1016/j.applthermaleng.2026.133878（created 2026-11-10）仿蜘蛛网流道液冷板，标题明示电池热管理 → 不过闸门
- 10.1016/j.ijthermalsci.2026.111441（created 2026-11-12）鲨鱼鳍针肋冷板，标题明示电池 → 不过闸门
- 10.1016/j.tsep.2026.105002（created 2026-11-11）自由表面射流 + 混合纳米流体 CFD-ML 代理，摘要无电子散热表述 → 不过闸门
- 10.1007/s12206-026-1049-4（JMST，created 2026-11-12）纳米流体微通道热沉翅片 CFD，无摘要、无电子散热依据 → 未收
- 10.1007/s11630-026-2378-4（J. Thermal Sci.，created 2026-11-09）热电翅片热沉，无摘要；标题含 electronic devices
  但属热电/空冷热沉，不是冷板 → 未收
- 10.1016/j.rineng.2026.114156（created 2026-11-12）制冷剂直冷电池冷板 → 电池，不收

## 其他说明
- arXiv 窗口内（v1 在 2026-11-08~11-14）未检出冷板/微通道/共轭传热类新稿
- 未找到窗口内的生成式设计（扩散/GAN/VAE）、拓扑优化、歧管微通道（MMC）新条目；结论只基于 Crossref 关键词检索，
  Elsevier 刊覆盖受限于无摘要
