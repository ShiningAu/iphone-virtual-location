# 故障排查

## 电脑找不到手机

确认 USB 线支持数据、手机已解锁且已信任电脑。运行 `scripts/devices.ps1`。若 USB 服务不可访问，确认 Apple Devices / iTunes 与驱动正常；工具依赖本地 USB 通信服务，沙箱还可能限制本机 socket 连接。授权失败不等于手机未连接。

不要把完整设备列表直接贴到公开 Issue；其中可能含设备名称和 UDID。

## 开发者模式或开发者镜像不可用

先确认在手机上已开启开发者模式并完成重启确认。当天环境已有可用开发者服务；本仓库不会自动切换手机隐私设置或下载、挂载镜像。镜像或隧道报错请按 [上游故障排查](https://doronz88.github.io/pymobiledevice3/guides/troubleshooting/) 处理，不要把未验证的报错当成定位成功。

## 地图不更新

保持 USB 和启动窗口运行，点击地图定位箭头。必要时在手机上关闭定位服务，等 10 秒后重开，再检查。网络开关不是本案例的必要前提，也不是健康功能解锁的保证。

## 显示 Trying again over a no-root userspace tunnel

在本例 iOS 27.0.1 环境中，这是工具切换到开发者隧道的提示，本身不代表失败；仍需观察后续错误和手机地图。

## 恢复命令成功，但地图仍是模拟位置

先在启动窗口按 Enter，确保持续模拟已经结束；再运行 `scripts/restore.ps1`。重新检查地图。若仍未恢复，重启 iPhone。本案例通过用户重启和地图反馈确认恢复；不要只依据退出码宣称恢复完成。

## 健康功能仍提示地区不可用

这是当天实际观察到的结果。地图坐标变化不证明地区资格已改变。本仓库只提供虚拟位置，不提供健康功能解锁，亦不自动回答健康问答。

## PowerShell 拒绝运行脚本

可直接使用 README 中的 Python 命令执行入口。安装时依次运行 `py -m venv .venv` 和 `.\.venv\Scripts\python.exe -m pip install -r requirements-lock.txt`。本项目不修改电脑执行策略。
