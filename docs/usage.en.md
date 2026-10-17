# Detailed usage guide

[中文](usage.md) · [English README](../README.en.md)

“Send a location” means sending simulated coordinates from your computer to your own iPhone over USB. It does not mean uploading phone files or a backup.

## 1. Before sending coordinates

1. Prepare Windows with Python 3.12 and the Apple Devices or iTunes USB drivers. Run `scripts/setup.ps1` from the project root once to install the pinned dependencies.
2. Connect a data-capable USB cable, unlock the iPhone, and confirm **Trust This Computer** on the phone. The owner must handle passcodes and trust prompts.
3. **Enable Developer Mode before starting simulation**: Settings → Privacy & Security → Developer Mode → On. Follow the restart prompt, then unlock the phone and confirm enabling Developer Mode after it restarts.
4. Keep the phone connected, reconnecting USB after the restart if needed. Start with only one iPhone attached.
5. If Developer Mode is missing, or developer-image/tunnel setup fails, see [Troubleshooting](troubleshooting.md). The tool does not toggle phone privacy settings automatically. The case used an already working developer-services environment; clean-machine setup was not separately verified.

## 2. Send coordinates from Windows

Open PowerShell in the project root:

```powershell
# First-time setup; skip once installed
.\scripts\setup.ps1

# New York, Manhattan
.\scripts\start.ps1
```

After the `Sent coordinates` message and Enter prompt appear, **keep the terminal and USB connection open; do not press Enter yet**. Command completion does not prove that the phone is showing the location. Resolve any connection error before treating the operation as successful.

```powershell
# Hong Kong, Central
.\scripts\start.ps1 -Preset hong-kong

# Custom latitude and longitude
.\.venv\Scripts\python.exe .\src\iphone_location.py start --lat 40.7128 --lon -74.0060
```

## 3. Refresh and verify on the phone

1. Open Apple Maps and tap the current-location arrow. Check whether the blue dot is in the selected city.
2. If it has not updated, open Settings → Privacy & Security → Location Services. Turn Location Services off, **wait ten seconds**, and turn it back on.
3. Return to Maps and tap the location arrow again. This refresh was used in the successful case; it is not guaranteed to be necessary or effective on every device.
4. If the map still has not updated, you may try the optional network refresh below. Keep USB and the computer session running throughout.

### Optional network refresh

This is a troubleshooting option, **not a demonstrated requirement of this case**, and it is not a proven way to unlock regional features.

1. Temporarily turn off Wi-Fi in Settings → Wi-Fi.
2. Temporarily turn off Cellular Data in Settings → Cellular/Mobile Service.
3. Temporarily turn off Location Services in Settings → Privacy & Security.
4. Wait about ten seconds. Turn Location Services back on, and restore Wi-Fi and Cellular Data to their previous states.
5. Return to Maps and verify the blue dot. Briefly disabling networking may interrupt network activity; do not leave networking or Location Services disabled.

The location channel is USB and does not need Bluetooth pairing. Disabling networking does not itself change an IP address, and a changed map position does not prove regional eligibility in other apps.

## 4. During use and after reconnecting

- Keep the cable connected and the terminal running. After map verification, inspect the relevant behavior in your target app.
- Do not assume simulation survives unplugging or a computer restart. Reconnect, unlock, confirm trust if asked, and start a new session.
- Stop the previous session before switching presets to avoid competing simulations.
- Record “map verification succeeded” only after checking the blue dot on the phone.

## 5. Stop and verify real location

1. Press **Enter** in the active terminal to end simulation and request a clear.
2. If that terminal exited unexpectedly or clearing is uncertain, stop the original session, then run:

   ```powershell
   .\scripts\restore.ps1
   ```

3. Ensure Location Services is on and network settings are restored. Open Maps and tap the location arrow.
4. If the phone still shows the simulated location, **restart the iPhone**, unlock it, and check Maps again. In the documented case, the user confirmed real location after a restart.
5. A successful clear command does not prove restoration. If the position remains incorrect after a restart, stop testing and investigate.

## Checklist

| Stage | Verify |
| --- | --- |
| Before sending | Developer Mode enabled, phone unlocked/trusted, working data cable |
| After sending | Keep the computer session running; refresh Location Services for ten seconds if needed |
| Optional troubleshooting | Briefly disable and restore Wi-Fi, Cellular Data and Location Services; not a proven requirement |
| Success | User verifies the target city's blue dot in Maps |
| Finish | Stop, request clear, restore network/location settings, verify real position |

The method did not remove the health-feature region restrictions tested in this case. It is a location simulator, not a health-feature activation tool.
