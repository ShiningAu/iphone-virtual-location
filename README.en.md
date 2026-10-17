# iPhone Virtual Location

A small **Windows USB iPhone location simulator** built on [pymobiledevice3](https://github.com/doronz88/pymobiledevice3). Includes a documented device case, reproducible setup, location presets, restore guidance, and instructions for **Codex and Claude Code**.

[中文说明](README.md) · [Detailed usage guide](docs/usage.en.md) · [Architecture](docs/architecture.md) · [Sources and attribution](docs/references.md) · [AI-assisted reproduction](docs/reproduce-with-ai.md)

## What was verified

On 2026-10-17, a Windows host with Python 3.12 and pymobiledevice3 11.33.1 sent Hong Kong and New York coordinates to an iPhone 15 Pro running iOS 27.0.1 over USB. The user confirmed the changed blue dot in Apple Maps. The user also confirmed real location recovery after stopping simulation and restarting the phone.

The tested method did **not** unlock region-restricted Apple Watch or AirPods health features. This is a developer location simulator, not a health-feature activation tool. The newly organized wrapper was checked automatically without starting another device session; it is not claimed to have undergone a new end-to-end hardware test.

## Quick start

Requirements: Windows, Python 3.12 recommended, Apple Devices or iTunes USB support, a data-capable USB cable, an unlocked and trusted iPhone with Developer Mode enabled. The case used an already working developer-services environment; fresh driver/image setup was not separately validated.

**Before sending coordinates**, enable Developer Mode in Settings → Privacy & Security → Developer Mode. Follow the restart prompt, unlock the phone, confirm enabling Developer Mode, and reconnect USB if needed. If the option is missing, consult the prerequisites and troubleshooting guidance before starting.

```powershell
.\scripts\setup.ps1
.\scripts\start.ps1
```

The default preset is New York, Manhattan (`40.7128, -74.0060`).

### Phone steps after sending coordinates

1. Keep USB connected and the computer session running. Do not press Enter yet.
2. Open Apple Maps, tap the location arrow, and verify the target city's blue dot.
3. If it has not updated, open Settings → Privacy & Security → Location Services, turn it off for **ten seconds**, turn it back on, and check Maps again.
4. If needed, optionally turn off Wi-Fi, Cellular Data and Location Services briefly, wait about ten seconds, turn Location Services back on and restore the previous network settings, then check Maps. See the [detailed English guide](docs/usage.en.md) for the complete sequence.

**Developer Mode is a prerequisite; disabling networking is optional troubleshooting.** The case did not establish that a network toggle was required or could unlock regional features. Do not leave Location Services disabled. Sending coordinates is not uploading phone files.

```powershell
# Another public demonstration location
.\scripts\start.ps1 -Preset hong-kong

# Custom coordinates
.\.venv\Scripts\python.exe .\src\iphone_location.py start --lat 40.7128 --lon -74.0060
```

## Restore

Press **Enter** in the active session to request a clear. If needed, run `.\scripts\restore.ps1` after stopping the active session. Verify real location in Maps. If the phone still shows the simulated position, restart it and verify again. A successful command exit is not proof of restored physical location.

## Development

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

See `AGENTS.md`, `CLAUDE.md`, and `CONTRIBUTING.md` before changing the project. Never commit `.state/`, `.venv/`, pairing records, private keys, real device identifiers, or personal logs. Public preset coordinates are examples, not the user's actual location.

No MFi keys, CarKit/iAP2 implementation, Bluetooth pairing, or AnyGo cloud authentication are used. GPL-3.0; third-party dependencies retain their own licenses. Codex and Claude Code are independent tools, and this project does not imply their endorsement.

## Citation and reuse

Cite the repository URL and the version or commit you actually used. [CITATION.cff](CITATION.cff) provides machine-readable metadata. Preserve the applicable licenses and upstream copyright notices when reusing or distributing code; attribution links alone do not replace license requirements. The core device implementation is pymobiledevice3. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) and the [source inventory](docs/references.md) for the boundary between the actual dependency, this project's wrapper, and evaluated alternatives.
