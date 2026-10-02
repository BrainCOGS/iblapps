# iblapps
IBL related applications that rely on unsupported libraries such as pyqt5.  See package README files for more details.

## Development (BrainCOGS fork)

```bash
uv sync
uv tool install prek
prek install
prek run --all-files
QT_QPA_PLATFORM=offscreen uv run pytest
```

`tests/test_alignment_qc_gui.py` needs the IBL test Alyx server; set `IBLAPPS_ALYX_TESTS=1` to run it.
