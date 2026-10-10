# 术语表

散热方案周报中常见的缩写与术语。随各期内容持续补充。

| 缩写 | 全称 | 说明 |
| --- | --- | --- |
| TO | Topology Optimization | 拓扑优化，用于生成高效流道 / 结构布局 |
| ECAM | Electrochemical Additive Manufacturing | 电化学增材制造，可室温成形纯铜复杂流道 |
| AM | Additive Manufacturing | 增材制造（3D 打印）总称 |
| LPBF | Laser Powder Bed Fusion | 激光粉末床熔融，金属 3D 打印工艺 |
| MCHS | Microchannel Heat Sink | 微通道散热器 |
| MLCP | Microchannel Liquid Cold Plate | 微通道液冷板 |
| MIMO | Multiple-Input Multiple-Output | （冷板语境）多进多出流道构型 |
| SISO | Single-Input Single-Output | 单进单出流道构型 |
| CDU | Coolant Distribution Unit | 冷却液分配单元 |
| TDP | Thermal Design Power | 热设计功耗 |
| PEC | Performance Evaluation Criterion | 综合换热性能评价指标 |
| CNC | Computer Numerical Control | 数控加工 |
| CTO | Convective heat transfer Topology Optimization | 对流换热拓扑优化：以场协同理论显式刻画换热系数的 TO（第 6 期） |
| D2C | Direct-to-Chip (liquid cooling) | 直触芯片液冷，冷板贴合芯片封装 |
| FSW | Friction Stir Welding | 搅拌摩擦焊，固相焊接冷板/盖板，热变形小 |
| CHT | Conjugate Heat Transfer | 共轭传热：固体导热与流体对流耦合求解 |
| PINN | Physics-Informed Neural Network | 物理信息神经网络，将控制方程残差并入损失函数 |
| BTMS | Battery Thermal Management System | 电池热管理系统；其液冷板热源为面状电芯，与芯片冷板工况不同（第 7 期） |
| Fc | Field Synergy Number | 场协同数：以速度场与温度场夹角刻画对流换热的协同程度（第 6/7 期） |
| M-FFF | Metal Fused Filament Fabrication | 金属熔融沉积成形：金属丝材挤出成形后脱脂烧结，可成形铜冷板（第 7 期） |
| BESS | Battery Energy Storage System | 电池储能系统；NVIDIA DSX Ready 首批两品类之一（另一为 CDU，第 7 期） |
| RDHx | Rear Door Heat Exchanger | 后门换热器，机柜门内置液-气换热盘管（第 7 期） |
| D2S | Direct-to-Silicon (liquid cooling) | 直触硅液冷：冷却液直接接触芯片背面微结构，跳过 TIM 与盖板（第 7 期） |
| MPF | Micro-Pin-Fin | 微针肋：冷板/热沉内的微尺度柱状扰流结构，截面可为圆形、菱形等（第 8 期） |
| ATD | Approach Temperature Difference | 趋近温差：CDU 一二次侧的进出口温差指标，CDU 制冷量必须连同 ATD 工况一起引用才有意义（第 8 期） |
| GWP | Global Warming Potential | 全球变暖潜能值；低 GWP 制冷剂如 R1233zd(E)、R1234ze(E)、R1234yf（第 8 期） |
| NPN | NVIDIA Partner Network | NVIDIA 合作伙伴网络；「电源与散热解决方案」为其品类之一（第 8 期） |
| 㶲耗散 | Entransy Dissipation | 传热能力耗散，用于刻画换热过程不可逆性的判据，常与场协同、熵产并用（第 8 期） |
| minichannel | Minichannel | 小通道：水力直径量级大于微通道（microchannel），二者非同义，不可混用（第 8 期） |
| HTMMC | Hierarchical-Tapered Manifold Microchannel (cold plate) | 分级渐缩歧管微通道冷板：歧管分级 + 流道渐缩的组合构型（第 9 期） |
| TMC | Traditional/straight MicroChannel | 常规直微通道，作为冷板构型寻优的对照基准（第 9 期） |
| HBM | High Bandwidth Memory | 高带宽存储；与逻辑芯片并置于 2.5D 封装内，形成非均匀热源（第 9 期） |
| CHF | Critical Heat Flux | 临界热流密度：两相冷却器失效前可承受的最大热流（第 9 期） |
| ONB | Onset of Nucleate Boiling | 核态沸腾起始：两相冷板裕量取法的关键位置量（第 9 期） |
| CIO | Copper Inverse Opal | 铜反蛋白石：多孔铜吸液芯结构，用于毛细驱动两相冷却（第 9 期） |
| CWM | Copper Wire Mesh | 铜丝网：充当三维歧管，把供液与排汽解耦（第 9 期） |
| POD | Proper Orthogonal Decomposition | 本征正交分解：把温度场压缩为少数模态，供代理模型快速重构（第 9 期） |
| MTL-ANN | Multi-Task Learning Artificial Neural Network | 多任务学习人工神经网络：一网同时输出多个目标与场量（第 9 期） |
| TPMS | Triply Periodic Minimal Surface | 三周期极小曲面：换热器常用的周期性曲面结构（第 9 期） |
| FVM | Finite Volume Method | 有限体积法：CFD 常用离散方法，常作代理模型误差的真值基准（第 9 期） |
| GP | Gaussian Process | 高斯过程：代理建模与寻优常用的概率回归方法（第 9 期） |
| AOP | Advance Online Publication | 在线先行发表：已接收上线但尚无卷期（第 9 期） |
