# Instructions for coding agents

Read README.md, docs/architecture.md, docs/case-study-2026-10-17.md and docs/references.md before modifying this project.

- This is a Windows USB iPhone developer-location wrapper, not a health-feature unlocker.
- Preserve the difference between a successful API call, a user-confirmed map change, and confirmed restoration.
- Keep local runtime state in .state/ and dependencies in .venv/. Never commit pairing data, keys, UDIDs, real locations, personal logs, or screenshots.
- Use the pinned pymobiledevice3 version. Validate CLI dependency injection when updating it.
- Keep the userspace tunnel's event loop responsive. Do not call blocking input directly on that loop.
- Do not start, stop, or change an attached phone's simulated location solely to test code. Obtain the user's instruction for that device action first.
- Normal verification: `python -m unittest discover -s tests -v`. On Windows the asyncio tests need access to local sockets; report environment failures rather than labeling them device incompatibility.
- Do not change existing device sessions during installation or documentation work.
- Keep Chinese and English README claims consistent and cite actual source projects. Do not present evaluated alternatives as implemented dependencies.
- Tests without a phone cannot establish hardware compatibility. Record hardware verification separately.
