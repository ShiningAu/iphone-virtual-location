# 用 Codex 或 Claude Code 复现 / AI-assisted reproduction

本项目允许编码助手帮助理解和部署定位工具；不是在复现或训练 Codex、Claude 模型。手机定位操作需要设备所有者明确授权。

## 给编码助手的提示词

```text
请在 Windows 上部署当前仓库 iphone-virtual-location。
先阅读 AGENTS.md、README.md、docs/architecture.md 和 docs/references.md。
使用 Python 3.12，在项目 .venv 中安装 requirements-lock.txt，运行测试。
不要上传或展示配对记录、私钥、UDID、真实位置或个人日志。
不要自动修改手机隐私设置，也不要声称能解除健康功能的地区限制。
先完成软件环境检查，等待我明确授权后再启动手机定位。
```

环境准备完成后，由设备所有者发出下一条指令：

```text
这是我自己的手机，已通过 USB 连接、解锁并开启开发者模式。
请启动 new-york 预设并保持会话，指导我在 Apple 地图确认蓝点。
我说停止后，请结束会话、请求清除，再让我确认真实位置恢复。
```

## 操作边界

- 通过手机地图实际确认模拟位置，不能把终端输出当作地图验收。
- 关闭定位服务 10 秒后重开是本次用到的刷新步骤，不保证所有设备都需要或都有效。
- 重连后重新建立会话；本工具不提供后台自动重连服务。
- 结束时先按 Enter 或结束活动会话，再请求恢复。真实位置未恢复时，重启手机后确认。
- 不要把一次设备成功扩大为全部 iPhone/iOS 版本兼容。

English prompt:

```text
Read AGENTS.md and the README. Set up the pinned Python environment on Windows,
run the tests, and explain any prerequisites. Do not change my phone's location
until I explicitly ask. Keep pairing data and identifiers local. When authorized,
start the new-york preset, ask me to verify Apple Maps, and request a clear on stop.
Never claim the tool unlocks health features or that an exit code proves restoration.
```
