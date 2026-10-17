# 来源、参考与致谢 / Sources and attribution

## 实际使用的核心项目

**[doronz88/pymobiledevice3](https://github.com/doronz88/pymobiledevice3)** — 本项目唯一直接调用的设备通信实现。使用 11.33.1 的 USBMux、配对/设备通信、userspace 开发者隧道和 DVT LocationSimulation。许可为 GPL v3；核心协议实现属于上游作者。本项目只提供 Windows 启动封装、异步等待与退出清除、案例说明和复现约定。

上游参考：[CLI 示例](https://github.com/doronz88/pymobiledevice3/blob/master/docs/guides/cli-recipes.md)、[故障排查](https://doronz88.github.io/pymobiledevice3/guides/troubleshooting/)、[DVT 模拟定位源码](https://github.com/doronz88/pymobiledevice3/blob/master/pymobiledevice3/services/dvt/instruments/location_simulation.py)。网页内容会更新，实际复现依赖以 requirements.txt 和 requirements-lock.txt 为准。

## 调研过但未集成的项目

| 项目 | 本次用途 | 未集成原因或边界 |
| --- | --- | --- |
| [youcci/playport](https://github.com/youcci/playport) | 了解另一种 CarPlay / MFi / iAP2 路线 | 现成接收端面向 Mac，未移植、未调用其实现 |
| [shihabal3amri/DiPlay](https://github.com/shihabal3amri/DiPlay) | 核对 Android 车机项目的用途 | 未提取 APK、证书或私钥，未集成代码 |
| [davesc63/GeoPort](https://github.com/davesc63/GeoPort) | 寻找 Windows 定位工具 | 仅调研，没有运行或集成 |
| [asdmoment/SimLocation](https://github.com/asdmoment/SimLocation) | 了解 pymobiledevice3 跨平台定位工具 | 仅调研，没有复制或集成源码 |
| [keezxc1223/locwarp](https://github.com/keezxc1223/locwarp) | 核对 Windows 定位应用与公开兼容性反馈 | 仅调研，没有运行或集成 |
| [PShiw/airpods-hearing-aid-enabler](https://github.com/PShiw/airpods-hearing-aid-enabler) | 了解助听功能地区案例 | 其设备和方法不同，未实施，不能证明本项目能解锁 |
| [imReker 的 Watch 功能 Gist](https://gist.github.com/imReker/fba069c6cae7407509863b0ed78da2a7) | 对比社区报告的蓝牙定位路线 | 未替换健康配置文件，未集成其 plist |

## 产品与健康文档

- [iAnyGo 官方连接说明](https://www.tenorshare.com/guide/ianygo-connection-tutorial.html)：用于说明产品存在蓝牙模式，不能据此断言其专有认证实现。
- [Apple 高血压通知说明](https://support.apple.com/en-us/117296)、[Apple AirPods 助听说明](https://support.apple.com/zh-cn/120992)：用于核对功能边界。本仓库不提供医学判断或地区解锁。

## 编写过程与原创范围

项目通过用户与 Codex 的协作整理，包含 AI 辅助编写的封装与文档。提供 CLAUDE.md 是为了让 Claude Code 用户方便复现，不代表 Claude 参与过当天设备测试，也不代表任何厂商为本项目背书。仓库没有包含聊天全文、账号数据或私有认证材料。
