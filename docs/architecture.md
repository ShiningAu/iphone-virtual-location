# 技术路线

```text
Windows 本地 Python 启动器
  → USBMux / 已配对的 USB 设备连接
  → iOS 开发者服务的 userspace 隧道
  → DVT LocationSimulation
  → iOS 为应用提供模拟位置
```

依赖版本为 pymobiledevice3 11.33.1。DVT 定位服务标识是 `com.apple.instruments.server.services.LocationSimulation`，设置坐标对应 `simulateLocationWithLatitude:longitude:`，清除对应 `stopLocationSimulation`。

本项目不改变卫星信号或手机实际物理位置。没有实现 MFi-v3、CarKit、iAP2 或 NMEA，没有提取 DiPlay 中的证书或私钥，也不请求 AnyGo 云端认证。

## 为什么保持异步事件循环

当天的初始调用使用 CLI 等待终端按键。检查本地依赖源码时发现等待逻辑是同步的，可能阻塞同一线程上的 userspace 隧道。改为 `await asyncio.to_thread(...)` 后保持事件循环可运行，用户随后确认地图位置改变。

这是一项与修复时间一致的观察，不是经过控制变量实验确认的唯一根因。本仓库通过替换进程内的 `set` 命令回调实现异步等待，不编辑依赖安装文件；退出时在 `finally` 请求清除。

## 状态、恢复与边界

- `.state/` 保存工具本地状态，可能包含配对数据，必须忽略。
- 按 Enter 正常退出会请求清除；中断、断线、强制终止时不能保证送达。
- DVT 命令成功只能说明通信调用完成；蓝点是否改变以及真实位置是否恢复，需要在手机地图验证。
- 地图与健康功能的地区判断不能视为同一件事。本次香港、纽约定位均未解除健康功能限制，具体地区判定机制未被逆向验证。
- iAnyGo 官方说明有蓝牙模式，但其专有协议未在本项目验证，不能声称它必然使用某种 MFi 或 iAP2 实现。

参考：[pymobiledevice3 源码](https://github.com/doronz88/pymobiledevice3)、[DVT CLI 使用示例](https://github.com/doronz88/pymobiledevice3/blob/master/docs/guides/cli-recipes.md)、[iAnyGo 官方连接说明](https://www.tenorshare.com/guide/ianygo-connection-tutorial.html)。
