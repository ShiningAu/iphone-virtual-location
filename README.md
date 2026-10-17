# iPhone虚拟位置

**iPhone Virtual Location** — 在 Windows 上通过 USB 为自己的 iPhone 设置模拟位置，并保留可复查的操作记录。

仓库名：`iphone-virtual-location`。基于开源 [pymobiledevice3](https://github.com/doronz88/pymobiledevice3)，无需 iAnyGo 订阅、蓝牙配对或 AnyGo 云端认证。它是开发者模拟定位工具，**不承诺解锁健康功能或其他地区限制**。

[English](README.en.md) · [Codex / Claude 复现指南](docs/reproduce-with-ai.md) · [项目来源](docs/references.md) · [贡献指南](CONTRIBUTING.md)

适用检索词：iPhone 虚拟定位、Windows USB 定位、iOS location simulation、pymobiledevice3、DVT、Codex、Claude Code。这里的 AI 说明用于协助部署和复现本项目，不包含模型训练或模型复现。

## 已验证结果

2026-10-17，在 Windows、Python 3.12、pymobiledevice3 11.33.1、iPhone 15 Pro / iOS 27.0.1 的组合上：

- 成功通过 USB 发送香港中环与美国纽约坐标，用户在 Apple 地图确认蓝点改变。
- 断开、重新连接手机后，可再次发送坐标。
- 清除模拟定位后，地图可能仍显示模拟位置；本次通过重启 iPhone，用户确认真实位置恢复。
- Watch 高血压通知和 AirPods 助听的地区限制**没有解除**。

以上来自一次真实使用会话，不代表其他机型、系统版本都已通过测试。详见 [案例记录](docs/case-study-2026-10-17.md)。本仓库的新启动封装通过本地自动检查，未在本次整理时重新启动手机定位。

## 使用前准备

1. Windows 电脑，推荐 Python 3.12，确保命令行可以使用 `py`。
2. 安装 Apple Devices 或 iTunes，提供 iPhone USB 驱动与设备通信服务。
3. 使用能传输数据的 USB 线，解锁手机，并在手机上确认“信任此电脑”。
4. 在 iPhone“设置 → 隐私与安全性 → 开发者模式”手动开启开发者模式，并按提示重启和确认。
5. 初次使用建议只连接一台 iPhone。

当天使用了电脑上已经存在的 USB 通信环境，未单独验证“全新 Windows 安装 Apple Devices 后”的完整初始化流程。开发者镜像或配对状态缺失时，先看 [故障排查](docs/troubleshooting.md)。

## 快速开始

下载或克隆仓库，在项目根目录打开 PowerShell：

```powershell
# 首次安装
.\scripts\setup.ps1

# 开始模拟纽约曼哈顿
.\scripts\start.ps1

# 或使用香港中环预设
.\scripts\start.ps1 -Preset hong-kong
```

如果 Python 不在 PATH，可向安装脚本提供 Python 可执行文件路径：

```powershell
.\scripts\setup.ps1 -Python 'C:\path\to\python.exe'
```

保持 USB 连接和启动窗口运行。看到坐标发送成功后，在 iPhone 打开 Apple 地图并点定位箭头核实。若蓝点没有更新，可以在手机设置中关闭定位服务，等待 10 秒后重开，再检查地图。当天测试中不需要先切换网络；切换网络也不代表能够解除地区限制。

## 自定义位置与设备选择

```powershell
# 自定义经纬度；纬度在前，经度在后
.\.venv\Scripts\python.exe .\src\iphone_location.py start --lat 40.7128 --lon -74.0060

# 查看 USB 设备（只在本地输出，可能包含设备名称和标识）
.\scripts\devices.ps1

# 多台设备时明确指定本地查询到的 UDID；不要把实际 UDID 提交到仓库
.\scripts\start.ps1 -Udid '<your-device-udid>'
```

可编辑 `config/locations.json` 添加预设；其中坐标均为公共演示地点，不是实际住址或行踪。

## 停止和恢复真实位置

1. 在启动窗口按 **Enter**。本封装会在退出前请求清除模拟定位。
2. 若窗口异常退出或无法确认是否清除，可另行执行：

   ```powershell
   .\scripts\restore.ps1
   ```

3. 在 Apple 地图点定位箭头确认真实位置。**命令返回成功不等于已确认真实位置恢复。**
4. 如果仍显示模拟位置，重启 iPhone，再检查地图；本次案例实际通过该步骤恢复。

先结束模拟会话，再执行独立恢复脚本。强制关闭窗口、断线或进程崩溃时，自动清除不保证送达。

## 项目结构

```text
iphone-virtual-location/
├── config/locations.json             # 公共地点预设
├── docs/                            # 案例、技术路线、故障排查
├── scripts/                         # Windows 安装、启动、设备查看、恢复
├── src/iphone_location.py            # Python 入口和异步会话封装
├── tests/test_location.py            # 参数和会话退出逻辑检查
├── AGENTS.md                         # Codex 等编码代理的项目约定
├── CLAUDE.md                         # Claude Code 的项目入口
├── requirements.txt                 # 核心依赖版本
├── requirements-lock.txt            # 当天 Windows 环境依赖快照
├── LICENSE
└── THIRD_PARTY_NOTICES.md
```

`.venv/` 和 `.state/` 只保留在本机，并由 `.gitignore` 排除。不要上传配对记录、私钥、真实设备标识、个人日志或手机截图。

## 检查与维护

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

依赖固定到当天版本。升级后需重新核实 CLI 接口、隧道连接、模拟位置与恢复行为。支持范围以实测为准。

技术说明见 [架构](docs/architecture.md)。本项目采用 GPL-3.0；依赖的许可与来源见 [第三方说明](THIRD_PARTY_NOTICES.md)。
