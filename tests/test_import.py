import importlib
import unittest


class TestImport(unittest.TestCase):
    def test_import_qt_helpers(self):
        # Pure-Python modules that do not need a display or network.
        for name in ('qt_helpers', 'atlasview'):
            with self.subTest(module=name):
                importlib.import_module(name)
