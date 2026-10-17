# Third-party notices

This project depends on [pymobiledevice3](https://github.com/doronz88/pymobiledevice3), pinned to version 11.33.1 for the documented case. pymobiledevice3 is distributed under GNU GPL v3; its authors retain their copyrights. Consult its own license and notices for full terms.

The project uses pymobiledevice3's Python APIs and CLI registration. It does not vendor its package, dependencies, Apple developer images, authentication certificates, private keys, pairing records, or Apple software.

The wrapper was written during the documented user/Codex session with reference to the installed upstream CLI and service APIs. The initial local experiment changed the dependency's blocking terminal wait; the distributed wrapper uses a process-local registered callback instead. The USB/device protocol stack is upstream work, not an original protocol implementation by this project.

DiPlay and PlayPort were read as background for an alternative accessory-authentication route; their code, APK assets, certificates and private keys were not imported. Other evaluated projects are listed in docs/references.md. The GPL license text is the standard license document, copied from the dependency's packaged license for inclusion here.

The included GPL-3.0 LICENSE covers this project's source. Dependency packages retain their respective licenses. The dependency lock is a version snapshot, not a bundled binary distribution or a hash-verified lock.

Apple, iPhone, Windows, and iAnyGo are trademarks of their respective owners. This is an independent project, not affiliated with Apple or Tenorshare.
