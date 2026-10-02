"""Pytest configuration.

``test_alignment_qc_gui.py`` talks to the IBL test Alyx server at import time, so
it is only collected when ``IBLAPPS_ALYX_TESTS=1`` is set.
"""

import os

collect_ignore = []
if os.environ.get('IBLAPPS_ALYX_TESTS') != '1':
    collect_ignore.append('test_alignment_qc_gui.py')
