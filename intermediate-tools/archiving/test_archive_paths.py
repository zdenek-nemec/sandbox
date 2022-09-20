import logging
import os.path
import socket
import unittest

from parameterized import parameterized

from archive_paths import ArchivePaths
from archive_target import ArchiveTarget

INTERMEDIATE = ["avl4688t", "avl4658t", "avl4713p", "avl4715p"]


class TestInit(unittest.TestCase):
    def test_default(self):
        archive_paths = ArchivePaths()
        self.assertEqual(socket.gethostname(), archive_paths._host)
        if socket.gethostname() in INTERMEDIATE:
            self.assertEqual(False, archive_paths._test)
        else:
            self.assertEqual(True, archive_paths._test)

    def test_test_true(self):
        archive_paths = ArchivePaths(True)
        self.assertEqual(True, archive_paths._test)

    def test_test_false(self):
        archive_paths = ArchivePaths(False)
        if socket.gethostname() in INTERMEDIATE:
            self.assertEqual(False, archive_paths._test)
        else:
            self.assertEqual(True, archive_paths._test)


class TestGetPath(unittest.TestCase):
    @parameterized.expand([
        [True, "potato", ArchiveTarget.PATH_MEDIATION, "./tests/mediation"],
        [True, "potato", ArchiveTarget.PATH_TEMPORARY, "./tests/temp"],
        [True, "potato", ArchiveTarget.PATH_LOGS, "./tests/archive_logs"],
        [True, "potato", ArchiveTarget.PATH_ORIGINALS, "./tests/originals"],
        [True, "potato", ArchiveTarget.PATH_TAR, "./tests/tar_archives"]
    ])
    def test_local(self, test, host, target, expected_path):
        archive_paths = ArchivePaths(test)
        archive_paths._host = host
        self.assertEqual(os.path.abspath(expected_path), archive_paths.get_path(target))

    @parameterized.expand([
        [True, "avl4688t", ArchiveTarget.PATH_MEDIATION, "./tests/mediation"],
        [True, "avl4688t", ArchiveTarget.PATH_TEMPORARY, "./tests/temp"],
        [True, "avl4688t", ArchiveTarget.PATH_LOGS, "./tests/archive_logs"],
        [True, "avl4688t", ArchiveTarget.PATH_ORIGINALS, "./tests/originals"],
        [True, "avl4688t", ArchiveTarget.PATH_TAR, "./tests/tar_archives"],
        [False, "avl4688t", ArchiveTarget.PATH_MEDIATION, "/appl/dcs/data01/ARCHIVE"],
        [False, "avl4688t", ArchiveTarget.PATH_TEMPORARY, "/appl/dcs/data01/ARCHIVE/ARCHIVE_STORAGE/temp"],
        [False, "avl4688t", ArchiveTarget.PATH_LOGS, "/appl/dcs/data01/ARCHIVE/ARCHIVE_STORAGE/archive_logs"],
        [False, "avl4688t", ArchiveTarget.PATH_ORIGINALS, "/appl/dcs/data01/ARCHIVE/ARCHIVE_STORAGE/originals"],
        [False, "avl4688t", ArchiveTarget.PATH_TAR, "/appl/dcs/data01/ARCHIVE/ARCHIVE_STORAGE/tar_archives"],
        [True, "avl4713p", ArchiveTarget.PATH_MEDIATION, "./tests/mediation"],
        [True, "avl4713p", ArchiveTarget.PATH_TEMPORARY, "./tests/temp"],
        [True, "avl4713p", ArchiveTarget.PATH_LOGS, "./tests/archive_logs"],
        [True, "avl4713p", ArchiveTarget.PATH_ORIGINALS, "./tests/originals"],
        [True, "avl4713p", ArchiveTarget.PATH_TAR, "./tests/tar_archives"],
        [False, "avl4713p", ArchiveTarget.PATH_MEDIATION, "/appl/dcs/data01/tmp/OC-12871/arch01"],
        [False, "avl4713p", ArchiveTarget.PATH_TEMPORARY, "/appl/dcs/data01/tmp/OC-12871/temp"],
        [False, "avl4713p", ArchiveTarget.PATH_LOGS, "/appl/dcs/data01/tmp/OC-12871/archive_logs"],
        [False, "avl4713p", ArchiveTarget.PATH_ORIGINALS, "/appl/dcs/data01/tmp/OC-12871/originals"],
        [False, "avl4713p", ArchiveTarget.PATH_TAR, "/appl/dcs/data01/tmp/OC-12871/tar_archives"],
        [True, "avl4715p", ArchiveTarget.PATH_MEDIATION, "./tests/mediation"],
        [True, "avl4715p", ArchiveTarget.PATH_TEMPORARY, "./tests/temp"],
        [True, "avl4715p", ArchiveTarget.PATH_LOGS, "./tests/archive_logs"],
        [True, "avl4715p", ArchiveTarget.PATH_ORIGINALS, "./tests/originals"],
        [True, "avl4715p", ArchiveTarget.PATH_TAR, "./tests/tar_archives"],
        [False, "avl4715p", ArchiveTarget.PATH_MEDIATION, "/appl/dcs/arch01"],
        [False, "avl4715p", ArchiveTarget.PATH_TEMPORARY, "/appl/dcs/arch01/ARCHIVE_STORAGE/temp"],
        [False, "avl4715p", ArchiveTarget.PATH_LOGS, "/appl/dcs/arch01/ARCHIVE_STORAGE/archive_logs"],
        [False, "avl4715p", ArchiveTarget.PATH_ORIGINALS, "/appl/dcs/data01/ARCHIVE/originals"],
        [False, "avl4715p", ArchiveTarget.PATH_TAR, "/appl/mediation/med_backup"]
    ])
    def test_intermediate(self, test, host, target, expected_path):
        archive_paths = ArchivePaths()
        archive_paths._host = host
        archive_paths._test = test
        self.assertEqual(os.path.abspath(expected_path), archive_paths.get_path(target))

    def test_unknown_host_exception(self):
        logging.disable()
        archive_paths = ArchivePaths()
        archive_paths._test = False
        archive_paths._host = "potato"
        with self.assertRaises(KeyError):
            archive_paths.get_path(ArchiveTarget.PATH_MEDIATION)


class TestValidate(unittest.TestCase):
    def test_valid(self):
        archive_paths = ArchivePaths()
        archive_paths.validate(".")
        self.assertTrue(True)

    def test_invalid(self):
        archive_paths = ArchivePaths()
        with self.assertRaises(OSError):
            archive_paths.validate("/xxx/potato/xxx")


if __name__ == "__main__":
    unittest.main()
