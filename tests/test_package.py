import importlib.util
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('checker', ROOT / 'scripts/check_package.py')
checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)


class PackageChecks(unittest.TestCase):
    def test_current_package(self):
        self.assertEqual(checker.check(ROOT), [])

    def test_detects_broken_nested_link(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            shutil.copytree(ROOT, root, dirs_exist_ok=True, ignore=shutil.ignore_patterns('.git', '__pycache__'))
            (root / 'references/eurogames/master.md').unlink()
            self.assertTrue(any('missing path' in e for e in checker.check(root)))

    def test_detects_duplicate_persona(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            shutil.copytree(ROOT, root, dirs_exist_ok=True, ignore=shutil.ignore_patterns('.git', '__pycache__'))
            path = next((root / 'data').glob('*.csv'))
            path.write_text(path.read_text().replace('\n380,', '\n379,'))
            self.assertTrue(any('unique IDs' in e for e in checker.check(root)))

    def test_path_cannot_escape_package(self):
        self.assertIn('escapes package', checker.local_target(ROOT, ROOT / 'SKILL.md', '../outside.md'))

    def test_external_url_is_not_fetched(self):
        self.assertIsNone(checker.local_target(ROOT, ROOT / 'SKILL.md', 'https://example.org/file.md'))

    def test_active_link_scheme_is_rejected(self):
        self.assertIn('unsupported link scheme', checker.local_target(ROOT, ROOT / 'SKILL.md', 'javascript:alert(1)'))


if __name__ == '__main__':
    unittest.main()
