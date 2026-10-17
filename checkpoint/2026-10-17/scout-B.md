# scout B · 冷板制造工艺（原样回传）

窗口 2026-10-11~10-17，按 Crossref created。

**总体结论：钎焊 / skived / FSW / 扩散焊 / LPBF / ECAM / M-FFF 本期均未检出窗口内、与冷板直接相关的同行评审新论文。**

扫描方式：Crossref `query.bibliographic` + created 窗口过滤，共约 20 条 query。覆盖 brazed cold plate、skived fin、FSW cold plate、diffusion bonding microchannel、LPBF heat sink、ECAM copper、additively manufactured cold plate、M-FFF、vapor chamber sintered、micro-milling microchannel、embedded silicon microchannel、ITherm / SEMI-THERM / ECTC / InterPACK 等。FSW、brazing 的命中全是焊接冶金或电池冷板拓扑设计，与冷板制造无关。ITherm 和 "microchannel cold plate manufacturing" 两条 query 返回非 JSON，已换 query 重试。另做一条网页检索：命中只有厂商稿、招聘页、市场报告和专利，按规矩全部不收。

## 候选（弱相关，建议不入稿）

### 候选 1 · 空气辅助激光-微铣削复合工艺加工 100 µm 微通道
- 标题原文: Air-induced laser-assisted sequential micro-milling process for precise microchannel fabrication
- 作者原文串: Ashish Kumar Sahu (Indian Institute of Technology); Raju Prasad Mahto (Sardar Vallabhbhai National Institute of Technology); Sunil Jha (Indian Institute of Technology)
- 出处: Proc. IMechE Part L: J. Materials: Design and Applications（SAGE）
- DOI: 10.1177/14644207261496271，created/published 2026-10-12
- 内容与关键数字（摘要原文）:
  - 先激光铣削、再刀具微铣削，加工 100 µm 微通道。
  - 与常规微铣削相比，切削力降低 15–25%，刀具磨损和毛刺也降低 15–25%。
  - 进给从 40 增至 60 mm/min 时，毛刺从 37 µm 增至 59 µm。
  - 主轴 20000 rpm 时，表面粗糙度 0.6 µm，毛刺 20 µm。
- 相关性: 弱。摘要未提散热器、冷板或热工测试，工件材料摘要未写，未读全文。只能算微通道加工方法学，不是冷板论文。
- URL: https://doi.org/10.1177/14644207261496271
- 可信度: 同行评审；机构只有简称式字符串，无国别，不推定。

### 候选 2 · 拓扑优化形貌转 AlSi10Mg 增材散热器几何的数值比较
- 标题原文: From Topology Optimisation to Topology-Informed Heat Sink Geometries: Comparative Steady-State Thermal Assessment of AlSi10Mg Configurations
- 作者原文串: Gülsüm Tekavit (Akdeniz Universitesi); Tugce Tezel (Akdeniz University); Volkan Kovan (Akdeniz University)
- 出处: Engineering Research Express（IOP）
- DOI: 10.1088/2631-8695/aeb485，created/published 2026-10-14
- 内容与关键数字:
  - 纯数值，没有实验，也没有网格无关性验证（摘要自述）。
  - 8 种构型与商用散热器比较，最高温差 7.04–45.78 °C。最优构型 HS-8 与商用品相差约 7 °C。
  - 各构型未按质量和表面积归一化。
- 相关性: 弱。是风冷散热器，不是冷板，也没有增材工艺数据。
- URL: https://doi.org/10.1088/2631-8695/aeb485
- 可信度: 同行评审，但方法学薄弱，不建议入稿。

## 其他窗口内命中（均为设计 / 数值类，不属本角度，仅列 DOI 供角度 A / C 参考）
- 10.1016/j.icheatmasstransfer.2026.112881（rib-interconnected MCHS 数值，2026-10-16）
- 10.1016/j.applthermaleng.2026.133571（混合微通道热点缓解，2026-10-16）
- 10.1016/j.applthermaleng.2026.133678（制冷剂冷板结构优化，2026-10-17）
- 10.1016/j.ijheatfluidflow.2026.110749（蝉翅脉启发液冷，2026-10-15）
- 10.1016/j.jmrt.2026.10.111（梯度菱形结构散热器，2026-10-12。作者：Yingnan Sun; Yaoxian Zhang; Yuan Gao; Zhonghua Li，单位 Crossref 未带）
- 10.1002/ceat.70327（烧结铜纤维微通道散热器，电池冷却，2026-10-15）
- 以上均未核制造工艺，未读全文。

## 上期挂账处理

**1. InterPACK 2026（10-26~29，San Diego）**
- 无论文 DOI 上线。Crossref 中 10.1115 前缀下 `ipack2026-*` 零命中；直取 `10.1115/ipack2026-fm1` 返回 404。10.1115 前缀 9 月以来只见 SSDM2026 等其他会议。
- 会议程序页（interpack.secure-platform.com 日程页）被代理 403，未能核对；ASME 官网 `asmedigitalcollection.asme.org` 域名无法解析。
- 能确认的只有会期、地点，以及 CFP 的 9 个 track（含 Data Center、Heterogeneous Integration）。来源：https://event.asme.org/InterPACK/Program/Call-for-Papers
- 结论：论文 DOI 与公开程序均未取到。建议下期会后复查。

**2. 微铣削 microchannel heat sink**
- 本期已补扫成功。唯一相关命中即上面的候选 1，与散热器的关联很弱。
- 没有「微铣削加工微通道散热器 + 热工实测」的论文。

**3. ASME JEP / JHMT 的 ISSN**
- ASME Digital Collection 官网本环境不可达（域名无法解析），未能按 Online First 页面核对。改用 Crossref 的 journals 端点核 ISSN。
- Journal of Electronic Packaging：print 1043-7398，electronic 1528-9044，Crossref 标题匹配，ISSN 无误。
- ASME Journal of Heat and Mass Transfer：print 2832-8450，electronic 2832-8469，同样匹配。
- 另核了 JTSEA：print 1948-5085，electronic 1948-5093。
- 三刊在窗口内 created 均为 0 条。JEP 最新 Crossref 记录 created 为 2026-09-25（10.1115/1.4072719）。JHMT 最新为 2026-09-17，JTSEA 为 2026-09-11。
- 结论：**上期的 ISSN 没填错。0 条属实**，是 ASME 这几刊在 Crossref 的登记滞后（最近一次登记离窗口约 3–4 周）。
- 局限：ASME 官网的 Online First 页面里可能有尚未登记 DOI 的稿件，Crossref 看不到，本环境无法核。
- 顺带看到 JEP 在 2026-08 的两条（均窗口外，未核全文）：10.1115/1.4072567（Experimental Evaluation of Cooling Loop Configurations for Server-Level Direct-t…）、10.1115/1.4072591（Physics-of-Failure Approach for Reliability Analysis of Liquid-Cooled Data Cente…）

**4. 金属增材一体铜冷板章节补数据（DOI 10.1016/bs.aiht.2026.09.001）**
- 标题：Metal additive manufacturing enables monolithic copper cold plate development with sinusoidal microchannels for direct-to-chip cooling。出处 Advances in Heat Transfer（Elsevier），Crossref created 2026-10-08，book-chapter。
- 作者与单位（OpenAlex raw_affiliation，出版商交存层）：
  - Saptarshi Joshi、Behnood Bazmi、Woo Young Park、Daniel Farhat、Evgeny Shatskiy、Omar M. Zaki — Department of Mechanical Science and Engineering, University of Illinois, Urbana, IL, United States
  - Scott Green、Dakota Black — 3D Systems, Inc., Rock Hill, SC, United States
  - William P. King — 同上 Illinois 机械系，另有 Materials Research Laboratory, University of Illinois, Urbana, IL
  - Nenad Miljkovic（OpenAlex 标 is_corresponding=True）— 机构字段为空
- Miljkovic 单位：Crossref 和 OpenAlex 均无。**成稿须写「待确认」**，不推定。
- 通讯作者：仅此一条来自 OpenAlex 的标记，Crossref 无此字段，全文未取到，需 verifier 复核。
- 工艺类型、致密度、粗糙度、热工数据：均未取到（Crossref 与 OpenAlex 都没有摘要；ScienceDirect 被代理 403）。作者含 3D Systems，可能是 LPBF 铜工艺，**但这只是推测，不能写入成稿**。
- URL: https://doi.org/10.1016/bs.aiht.2026.09.001
