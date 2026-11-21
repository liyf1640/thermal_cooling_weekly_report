# scout-B 回传 · 冷板制造工艺（原样存档）

窗口 2026-11-15 ~ 11-21，判窗用 Crossref `created`。

**结论：同行评审的冷板制造工艺论文（钎焊 / skived / FSW / ECAM / LPBF 冷板）本期未检出。**
有 2 条 THERMINIC 2026 会议论文勉强沾边，列为低置信度备选，两条都取不到摘要。

## 各入口实际查询与命中
### 1. Crossref works，`created` 窗口 + `query.bibliographic`，rows=8
（total 是相关度宽召回总数，不代表命中数）

| 关键词 | total | 窗口内与制造工艺 + 散热相关 |
|---|---|---|
| brazed cold plate | 554 | 0。靠前为 SSRN 冷板布局优化（ssrn.7693278，SSRN 不收）、brazed plate gas cooler（icheatmasstransfer.2026.113163，板式气冷器热力学，不涉工艺）、开放微通道热液优化（energy.2026.143202）、拓扑优化冷板流动均匀性（applthermaleng.2026.134045）。后两篇是热工/优化，不是制造工艺。 |
| skived fin | 84 | 1，即备选 1。其余为法语 "fin" 噪声。 |
| friction stir welding heat sink | 1239 | 0。均为 FSW 材料学或工艺、与散热无关（AA5052/6261 异种接头、ZE41 镁合金、泡沫铝）。ijhmt.2026.129934 是 FSW 的 CFD，不涉散热。 |
| diffusion bonding cold plate | 1181 | 0。msea.2026.151436（Cu-Cu 超低温扩散焊）、mssp.2026.111418（Cu/SiO2 混合键合）属材料/封装键合，无冷板依据。 |
| additive manufacturing cold plate | 1541 | 0。均为通用增材、材料或拓扑优化。 |
| laser powder bed fusion heat sink | 3113 | 1，即备选 2。其余为通用 LPBF 材料/粉末研究。 |
| micro-milling microchannel | 542 | 0。10.1007/978-981-95-5253-5_45-1 为 Springer 手册章节、不是工艺论文；SAE 2026-99-2516 是会聚-发散通道热工优化，不涉工艺。 |
| electrochemical additive manufacturing copper | 1683 | 0。无 ECAM / Fabric8Labs 相关新条目。 |
| manufacturing liquid cooling heat sink | 2674 | 0 个工艺类。ijhmt.2026.129924、tcpmt.2026.3754479 是热工设计，不是制造工艺。 |

### 2. arXiv（`export.arxiv.org`）：窗口内 0 条
- 查询一 `all:"cold plate"` AND (brazing / additive / friction stir / skived / powder bed / milling)，按投稿日降序：
  最新三条为 2024-08-25、2023-10-05、2012-10-13 → 窗口内零。（先遇 "Rate exceeded"，重试一次才拿到结果。）
- 查询二 `all:"heat sink"` AND (additive manufacturing / powder bed / skiving / friction stir)：最新一条 2025-01-10 → 窗口内零。
- ⚠️ 第三条 `electronics cooling AND fabrication` **被限流，未得到结果，未覆盖**。

### 3. Crossref 10.1109 前缀（ECTC / ITherm / THERMINIC / ESTC 等），窗口 + `query.bibliographic`，rows=6

| 关键词 | total | 说明 |
|---|---|---|
| cold plate | 19 | 与冷板制造无关（Heatspreading from a Small Source on a Thick Plate 是传热建模，其余噪声）。 |
| heat sink | 39 | 命中 **THERMINIC 2026 一批**：AI 几何优化、SLA 氧化铝陶瓷热沉、泡沫金属倾斜板热沉、螺栓接触热导建模，另有备选 1 和 2。 |
| liquid cooling | 56 | 浸没冷却、两相冷却，与制造工艺无关。 |
| thermal management electronics packaging | 1148 | 仅看前 6 条，均为 ESTC / THERMINIC 封装热管理，无冷板制造。 |

- 🟢 **整个窗口内没有 ECTC、ITherm、SEMI-THERM 的 DOI。10.1109 前缀下只有 THERMINIC 2026（created 2026-11-19 批量上线）、ESTC 2026、EPEPS 2026。**
- ⚠️ THERMINIC 论文 Crossref `published` 为 2026-09、`created` 为 2026-11-19 → **按 created 判窗属本期窗口内上线**。

### 4. InterPACK 挂账项：10.1115 前缀 429 条，0 条 `ipack2026-*`，**第 4 次复查仍零命中**

## 低置信度备选（均无摘要）
**备选 1 · skived 热沉流量再分配**
- Enabling Flow Redistribution in Skived Heat Sinks for High-Power Density Computing: An End-to-End Case Study
- THERMINIC 2026（32nd Int. Workshop on Thermal Investigations of ICs and Systems），proceedings-article，IEEE
- DOI 10.1109/therminic70452.2026.11779752；Crossref created **2026-11-19**（`published` 2026-09）
- 作者与单位（Crossref 原串）：Ine Vandebeek、Lieven Vervecken、Rui Vieira，均为 **MegaCool Technologies**
- 摘要未取到（Crossref 无 abstract，fetch_source 也只有元数据）。关键数字：无。
- 覆盖面依据：仅标题字面 "Skived Heat Sinks"、"High-Power Density Computing"
- 置信度中低：散热相关成立，但是否涉及 skiving 加工工艺还是只做流场再分配设计，**无摘要无法判断**；作者单位是企业，留意厂商稿倾向。
- 去重：skived 为已覆盖工艺，但此 DOI 不在已报清单，按新增处理。

**备选 2 · LPBF 铜-石墨烯复合材料强化传热**
- Laser Powder Bed Fusion of Copper-Graphene Metal Matrix Composites for Enhanced Heat Transfer
- 同上 THERMINIC 2026；DOI 10.1109/therminic70452.2026.11779771；created **2026-11-19**（`published` 2026-09）
- 作者与单位（Crossref 原串）：Wessel W. Wits、Hyunjong Lee、Leonore van Goor、Bernard Geurts，
  单位 "Mathematics and Computer Science University of Twente"；Davoud Jafari，单位 "University of Twente"
- 摘要未取到。关键数字：无。覆盖面依据：仅标题字面 "Enhanced Heat Transfer"
- 置信度低：偏材料/工艺，是否明确面向热沉或冷板未知 → **无摘要证实则建议丢弃**
- 去重：LPBF 为已覆盖工艺，但此 DOI 不在已报清单，按新增处理。

## 需说明的未覆盖项
- arXiv 第三条查询被限流，未得到结果。
- SEMI-THERM 未单独查前缀（10.1109 前缀窗口内没有任何 SEMI-THERM 条目）。
- **OpenAlex 单篇端点未使用**——理由是备选 1、2 的 Crossref 记录本身没有摘要。
  ⚠️（主代理注：此推理有误。本期 3751185 与 3754479 两条正是 Crossref 无摘要而 OpenAlex 单篇端点有，已令其回头补试。）
