# Scout B（冷板制造工艺）第 12 期回传

**结论：钎焊 / skived / FSW 三项本期仍未检出窗口内、对象为冷板/热沉的同行评审新文。**
整个角度只有 2 条弱/边缘候选。判窗均用 Crossref `created`。未扫新闻检索（只扫 Crossref）。

## InterPACK 2026 会后 DOI 复查
- `api.crossref.org/prefixes/10.1115/works`，created 2026-10-25~11-07 共 294 条，只翻了前 100 条，其中**无 `ipack2026-*`**。
  同期出现的 ASME 新前缀为 `msec2026-*`（MSEC2026，created 2026-11-04）与 `drivn2026-*`（DRIVN，created 2026-10-29）。
- 10.1115 前缀下 query 带 IPACK2026：0 命中。
- 全库 query "InterPACK electronic packaging thermal" + 窗口过滤：16 条，无一为 InterPACK 论文。
- 直取 `10.1115/ipack2026-fm1` / `ipack2026-fm2` / `ipack2026-170001`：Crossref 均 404。
- **结论：InterPACK 2026 会后论文 DOI 截至 2026-11-07 仍零命中。** MSEC2026、DRIVN2026 已分别于 11-04、10-29 上线，InterPACK 可能滞后，下期可再查。
- 未覆盖：会议程序页与 ASME Digital Collection 本次未试；ITherm / ECTC / SEMI-THERM 未专门扫，仅通用 query 间接覆盖、窗口内未见。

## 候选（均弱相关）
1. **10.3176/proc.2026.4.08**（created 2026-11-02）"AM-aware topology optimization of cooling channels using a reduced-order cold plate model for electric machine water jackets"
   - 对象是**电机水冷夹套**，用降阶冷板模型做拓扑优化；偏设计、不是制造工艺，只是考虑了增材可制造性正则化。
   - 摘要只有定性结论：正则化越强→界面复杂度与流体面积分数越低、水力阻力越高、热性能越差；锐界面重分析显示全局热响应吻合良好。**无任何工艺参数或数值。**
   - 作者 Yang Zhang / Martin Sarap / Toomas Vaimann / Ants Kallaste（*Proceedings of the Estonian Academy of Sciences*）。单位 Crossref 无。全文未读。
2. **10.1007/s40964-026-02044-5**（created 2026-11-05）"The effect of sintering hold-time on heat transfer relevant properties of 3D-printed copper and bronze samples produced by bound powder extrusion"
   - 粘结粉末挤出（BPE，即 M-FFF 类）打印铜/青铜后脱脂烧结。**对象是试样、不是冷板或热沉**；立意服务传热行业。
   - 摘要数字：铜失重约 8%、烧结保温加长后收缩 12–30%、孔隙率 25–45%、热导率 40–70 W/mK（约为实体铜的 6–20%）；
     青铜失重约 10%、收缩 20–40%、孔隙率 27–45%、热导率 2–9 W/m（原文单位如此）；硬度为实体件的 30–50%；表面粗糙度明显高于减材加工。
   - 作者 Roy Urwin / Bradley D. Bock（*Progress in Additive Manufacturing*）。单位 Crossref 无。
   - 相关性：弱。热导率仅实体铜 6–20%，对冷板意义有限，可作「M-FFF 铜热沉现状」的负面数据点。

## 已读但不建议回传
- **10.1109/wipdaeurope69886.2026.11747072**（热管辅助 skived 翅片强制风冷，Zhejiang Univ；Xinglan Hou / Yongheng Yang；会议）：
  对象是 skived 翅片散热器，但 Crossref 只给到出版月份 2026-09，**created 日期未取到**；摘要缺失，无法判断是否含制造参数，设计向。**留给调用方决定是否核。**
- 10.3390/en19215111（PLA / PLA+Cu 增材壳管换热器）：非冷板非热沉，热导率仅 0.243→0.422 W/m·K，不相关。
- **10.1016/j.ijthermalsci.2026.111477**（AI 数据中心两相微通道冷板，created 2026-11-03）：纯设计/热工，**归角度 A**。
- FSW 命中（铝合金地铁车顶板、黄铜、高熵合金综述、TWB）：全是焊接冶金，按上期教训丢弃。
- 钎焊命中（CoCrFeNi 扩散钎焊、轻合金超声焊钎综述）：焊接冶金，丢弃。
- LPBF / SLM / 铜增材命中：多为工艺监测、ML、材料类，无冷板对象。
- 微铣削 / 扩散焊 / skived / 真空钎焊 query：命中全是微通道热沉的数值或设计论文，无制造细节，已被角度 A 覆盖。

## 没取到的
- 窗口内未再检出第 11 期 SSRN 7656294 一类的新增材冷板文章。
- LPBF / SLM 类 query 总命中数很大（数千），只取了前 8 条排序结果，可能遗漏排在后面的相关条目。
