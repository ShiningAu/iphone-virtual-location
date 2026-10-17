# Claude Code project guide

Follow [AGENTS.md](AGENTS.md), the repository's shared agent instructions.

Project: iPhone Virtual Location / iPhone虚拟位置. Windows, USB, pymobiledevice3, DVT location simulation.

Start with README.md and docs/reproduce-with-ai.md. Read docs/references.md for upstream attribution. Do not start a device location session during code review or setup unless the user explicitly requests it.

Verification command: `python -m unittest discover -s tests -v` in an environment with the pinned dependencies. No phone is needed for those tests.
