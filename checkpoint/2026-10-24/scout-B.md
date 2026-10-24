# scout-B 回传（冷板制造工艺）· 原样存档

角度 B（冷板制造工艺）：**严格判据下本期未检出**。下面只有 1 条边缘候选，由调用方决定收不收。

## 边缘候选（建议最多放「预印本速览」，不单立制造节）
### 候选 1 · SLM 增材制冷剂冷板（2 kW 激光切割设备）
- 类型: 论文（SSRN 预印本，未经同行评审）
- 标题原文: Design and evaluation of an additively manufactured refrigerant-based cold plate for a 2kW laser cutting device
- 作者: Youwei He; Zihan Chen; Jincheng Wang; Huihui Li; Yong Chen; Tianshi Wang; Lihua Wei; Yang Liu; Bo Li; Chaochao Zhou（Crossref 无单位信息，单位待确认）
- DOI: 10.2139/ssrn.7656294，Crossref created 2026-10-22
- URL: https://doi.org/10.2139/ssrn.7656294
- 要点（来自 fetch_source.py 取到的摘要，全文未读）:
  - 工艺: AlSi10Mg 粉末 SLM，双层蛇形微通道加 BCC 点阵。
  - 仿真: 三维共轭传热模型，混合多相加 Lee 蒸发冷凝模型。
  - 对比基准: 常规直翅片冷板，标称热负荷 2.7 kW。
  - 肋增强区最高表面温度: 33.07 °C 降至 30.98 °C。
  - 面积加权平均表面温度: 23.64 °C 降至 21.50 °C，代价是压降上升。
  - 质量: 2.281 kg 降至 2.106 kg，减 7.67%。
  - 实验室测试: 四个监测点温差约 2.5–3.0 °C，压降 0.27–0.29 MPa，与数值估算一致。
  - 整机测试: 稳定运行，光输出约 2.1 kW。
- 与冷板相关性: 中 —— 增材冷板且有实测。但重点是设计与热工评价，不是制造工艺本身，也没有工艺参数或致密度等制造数据。
- 去重: 新增（不在第 1、2、9 期清单内；与第 2 期「金属增材波纹翅片冷板」是不同工作）
- 核验状态: 已用 fetch_source.py 核元数据和摘要，未读全文

## 专项动作结果
1. InterPACK 2026: Crossref `10.1115` 前缀下，created >= 2026-10-01 且关键词 InterPACK 的命中只有 1 条，即 10.1115/1.4072766「Special Issue on InterPACK 2025」，不属 2026 年会。`ipack2026-*` 零命中，符合预期，未深挖。
2. 微铣削: 本期无新的微铣削加散热命中，10.1177/14644207261496271 未重复回传。

## 扫过的 Crossref query
所有 query 都加了 created 2026-10-18 至 10-24 的过滤，仅查 Crossref。
cold plate brazing / skived fin heat sink / friction stir welding cold plate / microchannel heat sink additive manufacturing / laser powder bed fusion heat sink / diffusion bonding microchannel / micro-milling microchannel heat sink / electrochemical additive manufacturing copper heat sink / liquid cold plate manufacturing / additively manufactured cold plate / selective laser melting heat exchanger electronics cooling / vacuum brazing aluminum cooling plate / ITherm 2026 / ECTC 2026 microchannel / micro pin fin fabrication silicon cooling / copper heat sink 3D printing

结论是上述 query 的命中基本都不是冷板或散热器的制造。
- 焊接冶金或材料类，与散热无关: FSW 的 AA7075–AZ31、背垫导热、Al/Cu 层压板；钎焊的 (VNbTaMoW)C 陶瓷接头；LPBF 的 CuCrZr/316L 界面、Cu-Cr-Zr 氧化、M2 钢。
- 纯设计、仿真或综述: manifold 微通道综述（Applied and Computational Engineering）、MCHS 被动强化综述（JTAC）、微针肋冷板数值研究（Heat Transfer Engineering）、液态金属微通道冷板 CPU 冷却（IJHFF）、电池 manifold 冷板拓扑优化（SSRN）。
- 会议集: GT2026 的 10.1115/gt2026-* 是涡轮机械，不相关。ITherm、ECTC 在窗口内无 DOI 命中。

## 未做或受限的部分
- 未用 OpenAlex。未访问被封域名。边缘候选以外的命中只看了 Crossref 标题，未取摘要。

PR 流程备注可写：「冷板制造角度扫 16 条 Crossref query（含 InterPACK 2026 前缀核查），无符合制造判据的条目，该节不出现」。
