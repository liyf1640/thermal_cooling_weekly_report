# scout-B · 冷板制造工艺（原样回传）

本期角度 B（冷板制造工艺）：**窗口内（2026-09-27 ~ 2026-10-03）未检出新增候选**。

扫描范围：
- 用 WebSearch 查了英文 query 7 条，覆盖钎焊冷板、FSW 冷板、skived 翅片、LPBF 微通道热沉、扩散焊微通道冷板、微铣削微通道热沉、ECAM 铜热沉。另有 2 条查 InterPACK 2026 和增材冷板 arXiv。
- 用 fetch_source.py 核了 3 条命中，发表日期全部在窗口外，不回传。

窗口外命中（均不建议收录）：
1. 10.3390/pr14101503《Investigations into Microchannel-Controlled Copper–Copper Temperature Gradient Bonding》（Processes）。
   - Crossref published 2026-05-07，窗口外。
   - 作者为西南大学（Southwest University, Chongqing）电子工程学院与人工智能学院，共 4 人，原文单位串已取到。
   - 内容是用芯片背面微流道控温做 Cu-Cu 温度梯度键合，摘要称有限元仿真得到键合面温差 >100 °C。
   - 微流道是键合的控温手段，不是冷板成形。判定为关键词误匹配。
2. 10.1002/adem.202502052《Laser Powder Bed Fusion of Copper–Tungsten Composites for Heat Sink Applications in High-Power Electronics》（Advanced Engineering Materials）。
   - Crossref published 2026-02-21，窗口外。
   - 作者来自 Fraunhofer UMSICHT 与慕尼黑工业大学（TUM）。
   - 摘要称 Cu/W 复合材料（20 vol% W）相对密度 99.4%，热导率 300.1 W/(m·K)，为纯铜的 76.1%，CTE 13.3e-6 /K，比纯铜低 23.1%。
   - 真研究 LPBF 工艺参数，但对象是材料和热沉演示件，不是冷板流道成形，相关性中偏弱。窗口外约 7 个月，不建议收录。
3. 10.1007/s00542-026-06137-7《A review of fabrication methods for microchannel heat sinks in electronic device cooling systems》（Microsystem Technologies）。
   - Crossref published 2026-08-12，窗口外。
   - 作者共 5 人（Zolpakar 等），Crossref 无单位，未取到。
   - 与已报「MCHS 制造三阶段综述」主题重叠，不收。

专项确认：
- InterPACK 2026 召开日期为 2026-10-26~29，地点 Mission Valley, CA。截至 10-03 未检到论文公开，如实说明。scout 未核对 ASME 会议集页面，只凭检索结果和会期判断。
- ECTC / ITherm 2026 上期已扫完，本期未重复扫。
- 钎焊、skived 翅片、FSW 三项长期缺口本期**仍无同行评审论文**。命中的只有厂商页面（Lori Thermal 的钎焊与 skived 页面、Stirweld 的 FSW 冷板页面、Coolmosa）和专利（US 11872650 / 12151302 FSW 冷板，US 12484185 增材冷板，US 11679445 超声增材冷板预制翅片）。
  - 按规则不作候选（rules 第 4 条：营销落地页、专利、供应商目录不作论文来源）。
  - 供清单归档参考（需核验后才写入 companies.md「擅长企业」列）：Stirweld 做 FSW 冷板，Lori Thermal 做钎焊和 skived 冷板。
- 增材方向的命中均已在去重清单中。
