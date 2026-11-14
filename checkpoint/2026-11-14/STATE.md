# STATE · 第 13 期

- date: 2026-11-14
- issue: 13
- window: 2026-11-08 ~ 2026-11-14（上期 2026-11-07 之后）
- completed: [0, 1, 2, 3]
- updated: 2026-11-14T14:47:18Z

## 断点续跑检查结论（2026-11-14）

- LAST = 第 12 期 · 2026-11-07（PR #11，已于 2026-11-11 合并）
- 无 open 状态 briefing/* PR → 闸门一（上期 PR 未合并）未命中
- 今天 − LAST = 7 天 ≥ 5 → 闸门二（不足 5 天）未命中
- 无 wip/briefing-2026-11-14、无 briefing/2026-11-14 PR → 全新开跑
- 遗留：origin/wip/briefing-2026-11-07 未被第 12 期清理（日期不晚于 LAST，不影响续跑判断）→ 记入流程备注

## 本期必做的上期「下期动作」

1. OpenAlex 单篇端点重试摘要：10.1016/j.ijthermalsci.2026.111477、10.1016/j.ijheatmasstransfer.2026.129813、
   10.1016/j.ijheatmasstransfer.2026.129793、10.1109/tcpmt.2026.3751096（优先前两条）
2. 第 11 期六条 + ATE 133678 的摘要：若止损规则未定，再提一次止损请求（维护者尚未裁定）
3. ipack2026-* 再查一次（InterPACK 2026 会期 10-26~10-29 已结束）
4. AIP 两条（10.1063/5.0355126、10.1063/5.0350893）唯一未试通道 pubs.aip.org
5. 3C（与 Datalec 合并）若另发产品稿则核一次
6. fetch_source.py 改进建议原样重提（created / sequence / is_corresponding）

## 取数通道备忘（第 12 期实测）

- 可读：api.crossref.org、api.openalex.org（单篇端点，~3s 间隔）、export.arxiv.org、arxiv.org/pdf、doi.org、
  www.prnewswire.com、www.datacenterdynamics.com（须带 www + 必须用 fetch_source.py，curl 撞 Cloudflare）
- 不可读：ScienceDirect 整域 403、SSRN 全文 403、OpenAlex 批量 filter 429
- 判窗一律用 Crossref `created`
