# scout-B（冷板制造工艺）· 第 13 期 · 窗 2026-11-08~11-14

**结论：本角度未检出窗口内新增（过闸门者为零）。** 仅 1 条边缘疑似，scout 建议否决。

## 唯一疑似边缘命中（边缘，建议否决）
- 标题：Vacuum brazing of binder jetting structures for the assembly of complex internal channels and gyroid lattices
- DOI 10.21203/rs.3.rs-11305335/v1 ; https://doi.org/10.21203/rs.3.rs-11305335/v1
- Crossref created 2026-11-12T06:33:49Z（posted 2026-11-12）
- Research Square 预印本（posted-content，未同行评审），无卷期
- 摘要未给具体数值。工艺：金属 binder jetting 子部件 + 真空炉钎焊；填充金属 Ni 基合金 / 活性钎料 / 纯铜；
  试样为管-管接头与 gyroid 点阵立方体-板，仅做宏观分析（"characterized by macroscopic analysis"）
- 作者 Bernaitz Arregi / Garbiñe Atxaga / Isaac Dávila（均 Tecnalia Research & Innovation Foundation）
- 闸门依据：**摘要全文不含 cold plate / heat sink / electronics / cooling 字样**；最相关句为
  "design and manufacture of advanced structures with complex internal channels and gyroid architectures"
- 否决理由：通用 BJ 增材件的钎焊连接，不是冷板 / 热沉的制造；且为预印本

## InterPACK 2026（ipack2026-*）专查：仍零命中（第 3 次）
- prefix 10.1115、created 2026-11-01~11-14 共 382 条，offset 0/100/200/300 全部拉取；DOI 或标题含 ipack 的 0 条
- 该前缀新上线的只有 msec2026-*（created 2026-11-04，窗外）、fedsm2026-*（created 2026-11-13）与零星期刊文章
- query.bibliographic "IPACK2026" / "InterPACK 2026"（created ≥ 2026-11-01）无 ASME 命中
- 顺带发现（不属本角度，可转交 A/C 参考）：**fedsm2026-184041**
  *Machine Learning Applied for Instant Predictions of Spatial Temperature Variations in Heat Sinks for Computer Chip Cooling*（created 2026-11-13）

## 窗口内扫到但被闸门挡掉（均不是冷板制造工艺；其中数条属 A 角度，已转交）
- 10.1016/j.rineng.2026.114156（电池冷板流道设计与歧管分析，纯设计 + 电池）
- 10.1016/j.applthermaleng.2026.133878（仿蜘蛛网流道液冷板多目标优化，设计）
- 10.1016/j.ijthermalsci.2026.111441（鲨鱼鳍针肋电池冷板，设计）
- 10.3390/mi17111312（AI 服务器液冷冷板局部热工水力原位表征，测试非制造）
- 10.1016/j.enss.2026.100194（针肋冷板集成离子热电，设计）
- 10.1088/2631-8695/aebd48（分区液冷板，设计）
- 10.1016/j.applthermaleng.2026.133956（可弯曲铜平板振荡热管，热管非冷板）
- 10.1038/s44435-026-00023-4、10.3389/fmech.2026.1965238、10.1007/s12206-026-1049-4（微通道热沉数值/设计）
- 10.1016/j.trpro.2026.08.040（AM 换热器文献计量综述，created 2026-11-13，通用换热器，建议否决）
- FSW 类（Welding in the World / Welding International / engproc）：通用焊接冶金或钢材 → 排除
- LPBF / SLM 类（addma.2026.105429、rs.3.rs-11366783）：通用粉床工艺，无冷板/热沉 → 排除
- 网页检索只返回厂商页（Radian Thermal、CoolIT 技术简报、Wakefield），无 2026-11 新闻 → 不收
- arXiv API（cold plate + fabrication/brazing/additive/bonding，按提交日降序）返回为空

## 跑过的全部检索式（证明空窗是真空窗）
Crossref 全局 works，filter=from-created-date:2026-11-08,until-created-date:2026-11-14，query.bibliographic 逐条：
cold plate brazing / heat sink brazing / vacuum brazing cold plate / skived fin heat sink /
friction stir welding cold plate liquid cooling / electrochemical additive manufacturing copper heat sink /
laser powder bed fusion cold plate / additively manufactured heat sink / selective laser melting microchannel heat sink /
diffusion bonding microchannel heat exchanger / micro-milling microchannel heat sink / micro pin fin fabrication heat sink /
microneedle fin heat sink machining / 3D printed liquid cold plate copper / manufacturing process liquid cooling plate electronics /
additive manufacturing cold plate data center / copper cold plate manufacturing / microchannel cold plate fabrication bonding /
ITherm 2026 cold plate / ECTC 2026 microchannel cooling / IPACK2026 / InterPACK 2026
另：prefixes/10.1115 created 2026-11-01~11-14 四页共 382 条本地过滤；
WebSearch "cold plate additive manufacturing OR brazing OR skived fin manufacturing November 2026"；
export.arxiv.org all:"cold plate" AND (fabrication OR brazing OR "additive manufacturing" OR bonding)。

## 局限
ScienceDirect / SSRN 页面不可达，Elsevier 刊物只能凭标题与 Crossref 元数据判断；窗口内 Elsevier 刊物里
没有题名指向制造工艺的冷板 / 热沉论文。
