date: 2026-11-21
issue: 14
window: 2026-11-15 ~ 2026-11-21
last: 第 13 期 · 2026-11-14 (PR #12, merged 2026-11-14)
gates: 上期 PR 已合并（#12）；距上期 7 天 ≥ 5 → 两道跳期闸门均未命中
completed: [0, 1, 2, 3, 4]
step2_status: 三批核验已回（学术 4 条 + THERMINIC 3 条 + 产业全部）；第四批（CuBricks / 玻璃封装微流道）进行中
verified_pass: |
  学术：
    10.1109/tcpmt.2026.3751185   通过（created 11-13，上期挂账重试成功；头条）
    10.1016/j.ijheatmasstransfer.2026.129907 通过（created 11-17，浸没冷却功率电子）
    10.3390/mi17111351           通过（created 11-20，W-Cu 锻造 → 激光 bar 封装热路径）
    10.1109/therminic70452.2026.11779791 通过（created 11-19，方形针肋微通道热沉）
    10.1109/therminic70452.2026.11779794 待确认部分（created 11-19，多芯片功率模块两相微通道）
    10.1109/therminic70452.2026.11779775 待确认部分（created 11-19，集总参数模型负面结果）
  产业：
    MiTAC × ZutaCore PoC / Solenis × Vertiv / Arivor / ZTE / Aviemore / MES  六条通过
    CoolIT × Ecolab CHx 3000  待确认（已找到一手产品页，DCD 有两处错误）
    Nexalus × Renda Nova8     待确认（仅 DCD 转述）
    MarketsandMarkets 漏液检测 通过（须加口径限定）
verified_reject: |
  10.1109/tcpmt.2026.3754479（电子工艺设备侧、非芯片冷板，且有 SSRN 先行版）→ 从严否决，记 excluded
  10.54097/fdaate22（小出版商 + 摘要无电子散热字面 + 热阻拟合 R²=0.6229）→ 否决
  arXiv:2611.21707 EJBench（电池冷板 + LLM 评测基准，方法学价值弱）→ 否决
  ZutaCore × Munters Z₂O（一手全不可达，数字仅见检索摘要）→ 否决
  Frost & Sullivan 全球 HVAC 383.6 亿美元（口径非液冷、无数据中心细分）→ 否决
empty_angles: 冷板制造工艺的同行评审新论文（钎焊/skived/FSW/ECAM/LPBF）本期仍未检出——已扫过且为空
updated: 2026-11-21T15:03:56Z
