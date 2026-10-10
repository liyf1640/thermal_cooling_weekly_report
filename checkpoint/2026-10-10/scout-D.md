# scout-D · 英文期刊 in-press / online-first（原样回传）

方法：Crossref `from-created-date:2026-10-04,until-created-date:2026-10-10` 按刊 ISSN 全量拉取。
窗口内条数：IJHMT 39、ATE 73、ECM 26、IJTS 23、ICHMT 51、Physics of Fluids 123、TCPMT 10。
fetch_source.py 对 Elsevier 条目只返回标题/作者/刊名，**不含摘要**。

通用说明：
- Elsevier 条目在 Crossref 里 **published-online 为空**，只有 created 与 published-print；上线日只能以 created 为准。
- Elsevier 的 published-print 是 in-press 阶段预分配的未来卷期名义日期，**不能当上线日**（ATE 2026-11、IJHMT 2027-02）。
- 所有 Elsevier 条目都「无印本刊期」，只有卷号与文章号，无页码。作者为 Crossref 所示，单位均未核。
- **未检出**：ASME JEP（ISSN 1043-7398 / 1528-9044）与 ASME J. Heat Mass Transfer（2832-8450 / 2832-8469）
  在 Crossref 窗口内返回 0 条，**只试了这几个 ISSN；可能是交存延迟或 ISSN 没对上，不等于该刊本周无新文**。
- ECM 窗口内 26 条，无一条与冷板或电子散热相关。

## 强相关
1. ATE | Optimization and thermal-hydraulic performance investigation of hierarchical-tapered manifold microchannel cold plate for chip cooling
   - Xiaoyu Zhou; Minqiang Pan; Qinglin Xie（未核）| vol 308 文章号 133509，无印本刊期
   - 10.1016/j.applthermaleng.2026.133509 | created 2026-10-07 / online 无 / print 2026-11（名义）| 无摘要 | **强**
2. ATE | Topology-optimized microchannel cooling for heterogeneous logic-HBM heat sources: thermal-hydraulic optimization and thermo-mechanical assessment
   - Siping Gao; Meihong Zhao; Boxiang Wang; Shuai Gong（未核）| vol 308 文章号 133538
   - 10.1016/j.applthermaleng.2026.133538 | created 2026-10-07 / online 无 / print 2026-11 | 无摘要 | **强**
3. ATE | Integrated shroud designs for enhanced thermal and hydraulic performance in 3D manifold heatsinks subjected to external flow
   - Wenguang Zhao; Gearóid Farrell; Shailesh N. Joshi; Ercan M. Dede; Tim Persoons（未核）| vol 308 文章号 133504
   - 10.1016/j.applthermaleng.2026.133504 | created 2026-10-08 | 无摘要 | **中到强**（3D 歧管散热器，外流风冷场景）
4. ATE | Thermo-hydraulic optimization and rapid temperature field prediction for high heat flux density microchannel heat sinks based on multitask artificial neural networks
   - Chunquan Li; Wenluo Huang; Yuling Shang; Hongyan Huang; Rui Zhang; Yufeng Liang（未核）| vol 308 文章号 133318
   - 10.1016/j.applthermaleng.2026.133318 | created 2026-10-08 | 无摘要 | **强**
5. IJHMT | Thermal and hydraulic optimization and experimental validation of a water-cooled heat sink for high-power semiconductor devices
   - Hengji Wu; Jie Yang; Yuebo Chen; Jiaye Zhou; Qingquan Liu（未核）| vol 273 文章号 129709
   - 10.1016/j.ijheatmasstransfer.2026.129709 | created 2026-10-06 / print 2027-02 | 无摘要 | **强**（含实验验证）
6. IJHMT | Influence of regional artificial cavity layouts on flow boiling in micro heat sinks with stepwise-decreasing pin-fin heights
   - Fatih Atci; Burak Markal; Alperen Evcimen（未核）| vol 273 文章号 129693
   - 10.1016/j.ijheatmasstransfer.2026.129693 | created 2026-10-04 / print 2027-02 | 无摘要 | **中到强**
7. ATE | Research on the performance and optimization of single-phase immersion liquid cooling systems for high-TDP multi-GPU servers
   - Huifan Zheng; Kejing Zhang; Guoji Tian; Mengwei Guo; Qiang Luo（未核）| vol 308 文章号 133387
   - 10.1016/j.applthermaleng.2026.133387 | created 2026-10-06 | 无摘要 | **中**（浸没式非 D2C 冷板）
8. ICHMT | Exploring capillary limits of copper wire mesh manifold for area scaling of capillary-driven two-phase coolers
   - Heungdong Kwon; Roman Giglio; Daeyoung Kong; Muhammad Shattique; Hyoungsoon Lee; James W. Palko; Ercan M. Dede; Mehdi Asheghi（未核）| vol 180 文章号 112500
   - 10.1016/j.icheatmasstransfer.2026.112500 | created 2026-10-07 | 无摘要 | **中**
9. ICHMT | Encoded corrugation design for flow redistribution and thermohydraulic performance enhancement in parallel microchannels
   - Yili Zhou; Ping Xu; Jie Xing; Shuguang Yao（未核）| vol 180 文章号 112814
   - 10.1016/j.icheatmasstransfer.2026.112814 | created 2026-10-09 | 无摘要 | **强到中**
10. ICHMT | A physics-constrained surrogate for subcooled flow boiling in low-GWP immersion cooling microchannels: FiLM conditioning and gradient-balanced training
    - Jaeseon Lee; Yujin Kim（未核）| vol 180 文章号 112748
    - 10.1016/j.icheatmasstransfer.2026.112748 | created 2026-10-07 | 无摘要 | **中**
11. ICHMT | Physics-informed neural networks for thermal spreading of multilayer multichip power modules
    - Yonghun Kim 等 8 人（未核）| vol 180 文章号 112739
    - 10.1016/j.icheatmasstransfer.2026.112739 | created 2026-10-05 | 无摘要 | **中**

## 弱相关（电子散热但偏离冷板主线）
- ICHMT 112799 脉动射流冲击针肋平板 LES+实验（Yousefi-Lafouraki 等）created 2026-10-08，中
- ICHMT 112791 超紧凑环翅离子风泵（Chuan Li 等）created 2026-10-06，弱（非液冷）
- ICHMT 112808 ML 辅助轴流风扇叶片优化（Rujie Shi 等）created 2026-10-08，弱（风冷）
- ATE 133521 机械泵驱动两相回路中蓄液器与微通道蒸发器的压力耦合（Jieni Wang 等）created 2026-10-05，中
- ATE 133430 四合一功率电子变换器功率模块均温（Manar Emira 等）created 2026-10-09，弱到中
- ATE 133443 2.5D 金属点阵强化 PCM 热沉瞬态 ON/OFF 评价（Bhatti 等）created 2026-10-06，弱
- IJTS 111382 双层微通道热沉上层针肋阵列（Anurag Maheswari 等）vol 232，created 2026-10-05 / print 2027-02，中
- IJTS 111413 多自由表面三角形射流冲击局部换热实验（Date 等）vol 233，created 2026-10-10 / print 2027-03，弱
- IJTS 111388 射流阵列自适应优化（Yunhao Bao; Shuangquan Shao）created 2026-10-06；IJTS 111396 扩散缝射流+交错针肋（Tianli Dong 等）created 2026-10-09；print 均 2027-03；弱
- TCPMT（Early Access，无卷期）10.1109/tcpmt.2026.3740646 空间变功率图 3D IC 解析热建模（Qiuchen Zhang; Xiaoyi Wu）created 2026-10-06，弱到中；
  10.1109/tcpmt.2026.3740761 3D 叠片边界热导映射灵敏度（Thi Kim Tuyen Le 等）created 2026-10-06，弱
- Physics of Fluids（**有摘要**）10.1063/5.0333304 Swirl flow in microchannels: Patterned slip walls enhance heat transport
  （L. G. Chej; M. F. Carusela; A. G. Monastra; J. Harting; P. Malgaretti）vol 38 iss 10 文章号 102005，
  created 2026-10-07 / published-online 2026-10-07 / **published-print 2026-10-01（名义日早于 online，正是本栏要防的情形）**；
  摘要要点「Microchannel heat sinks are widely used for thermal management in high-power electronics…」
  「appropriately arranged slip/no-slip regions can induce swirl without geometric perturbations or increased pumping po[wer]…」
  （摘要在 1200 字处被截断，无具体数字）；相关性 中
- Physics of Fluids 10.1063/5.0346595 各向异性润湿条抑制冲击两相流不稳定性（Zhicheng Yuan 等）created/online 2026-10-05 / print 2026-10-01；T 形微通道气水撞击界面稳定性，OpenFOAM，无传热数字；弱

未列入：ECM 全部条目；IJHMT/ATE 中的电池浸没冷却、热管、换热器、透平冷却等。
