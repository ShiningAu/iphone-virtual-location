# Contributing / 贡献指南

感谢帮助改进文档、Windows 兼容性和恢复行为。

1. 阅读 README.md、AGENTS.md 和 docs/references.md。
2. 在 Python 3.12 环境安装 requirements-lock.txt，运行 `python -m unittest discover -s tests -v`。
3. 提交集中解决一个问题的改动；说明问题、修改、验证方式和剩余限制。
4. 如报告真机测试，说明手机机型、iOS 版本、Windows 版本、依赖版本及地图验证结果。省略 UDID、真实位置、配对记录和个人日志。
5. 将无设备测试与真机结果分开。不要以健康功能解锁、永久定位或所有版本兼容作为未经验证的宣传。
6. 引入外部代码时保留版权与许可证，更新 THIRD_PARTY_NOTICES.md。

Use clear commit messages such as `fix: keep tunnel responsive while waiting for input` or `docs: clarify restore verification`. Be respectful and focus review on reproducible behavior and evidence.
