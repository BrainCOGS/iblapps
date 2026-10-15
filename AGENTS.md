# iblapps (BrainCOGS fork)

BrainCOGS's fork of int-brain-lab/iblapps (PyQt5 apps for IBL sessions, mainly
the ephys alignment GUI), launched from RecordingProcessJobGUI. Python >= 3.10.

## Setup and tests

```bash
uv sync --locked
uv run pytest -q            # CI: Python 3.10 and 3.13 (needs libegl1/libgl1 on Linux)
```

Lint: `uvx prek run --all-files` (the same as CI's Lint workflow).

## Pins and gotchas

- Keep upstream files untouched where possible: only BrainCOGS-added files are
  formatted, so merging upstream stays easy. If an upstream merge brings back
  its `ci.yml`, delete it again.

## Agent workflow

- Errors reported in Slack: use the `bugfix-from-slack` skill (agent-tooling). The braincogs-claude-agent bot opens issues and PRs; commits and pushes are the user's.
- Commits end with one `Assisted-by: <Harness>:<model>` trailer per agent, e.g. `Assisted-by: ClaudeCode:claude-opus-5-5`. No AI co-authors, and no `Generated with` lines. `prek install` sets up the `ai-attribution` commit-msg hook (`.github/scripts/check_ai_attribution.py`, vendored from agent-tooling), and CI checks every commit of a PR.
- PRs target `master` on `BrainCOGS/iblapps`. Merge PRs the bot opened with **Rebase and merge**, not Squash: GitHub attributes a squash commit to the PR's opener.
- This is a fork. Always pass `-R BrainCOGS/iblapps` to `gh`, since plain `gh pr create` targets the upstream.
- Issues are turned off here; put the bug report sections in the PR body instead.
