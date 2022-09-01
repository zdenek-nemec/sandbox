import logging
import os.path
import socket
import unittest

from parameterized import parameterized

from archive_paths import ArchivePaths
from archive_target import ArchiveTarget


class TestInit(unittest.TestCase):
    def test_default(self):
        archive_paths = ArchivePaths()
        self.assertEqual(False, archive_paths._is_live)
        self.assertEqual(socket.gethostname(), archive_paths._host)
        self.assertEqual(list, type(archive_paths._valid_hosts))
        self.assertEqual(True, "avl4658t" in archive_paths._valid_hosts)

    def test_is_live_true(self):
        archive_paths = ArchivePaths(True)
        self.assertEqual(True, archive_paths._is_live)

    def test_is_live_false(self):
        archive_paths = ArchivePaths(False)
        self.assertEqual(False, archive_paths._is_live)


class TestIsLive(unittest.TestCase):
    def test_true(self):
        archive_paths = ArchivePaths()
        archive_paths._is_live = True
        self.assertEqual(True, archive_paths.is_live())

    def test_false(self):
        archive_paths = ArchivePaths()
        archive_paths._is_live = False
        self.assertEqual(False, archive_paths.is_live())


class TestIsHostValid(unittest.TestCase):
    def test_true(self):
        archive_paths = ArchivePaths()
        archive_paths._host = "potato"
        archive_paths._valid_hosts = ["potato"]
        self.assertEqual(True, archive_paths.is_host_valid())

    def test_false(self):
        archive_paths = ArchivePaths()
        archive_paths._host = "potato"
        archive_paths._valid_hosts = []
        self.assertEqual(False, archive_paths.is_host_valid())


class TestGetHost(unittest.TestCase):
    def test_get_host(self):
        archive_paths = ArchivePaths()
        self.assertEqual(socket.gethostname(), archive_paths.get_host())


class TestGetPath(unittest.TestCase):
    @parameterized.expand([
        [True, "avl4658t", ArchiveTarget.MED,
         "/appl/dcs/data01/tmp/OC-12871/med_archive"],
        [True, "N007510", ArchiveTarget.MED,
         "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/med_archive"],
        [True, "avl4658t", ArchiveTarget.TAR,
         "/appl/dcs/data01/tmp/OC-12871/tar_archive"],
        [True, "N007510", ArchiveTarget.TAR,
         "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/tar_archive"],
        [True, "avl4658t", ArchiveTarget.NAS,
         "/appl/dcs/data01/tmp/OC-12871/nas_archive"],
        [True, "N007510", ArchiveTarget.NAS,
         "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/nas_archive"],
        [True, "avl4658t", ArchiveTarget.OPS,
         "/appl/dcs/data01/tmp/OC-12871/ops_archive"],
        [True, "N007510", ArchiveTarget.OPS,
         "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/ops_archive"],
        [True, "avl4658t", ArchiveTarget.LOG,
         "/appl/dcs/data01/tmp/OC-12871/log_archive"],
        [True, "N007510", ArchiveTarget.LOG,
         "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/log_archive"],
        [False, "avl4658t", ArchiveTarget.MED,
         "/appl/dcs/data01/tmp/OC-12871/tests/med_archive"],
        [False, "N007510", ArchiveTarget.MED,
         "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/med_archive"],
        [False, "avl4658t", ArchiveTarget.TAR,
         "/appl/dcs/data01/tmp/OC-12871/tests/tar_archive"],
        [False, "N007510", ArchiveTarget.TAR,
         "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/tar_archive"],
        [False, "avl4658t", ArchiveTarget.NAS,
         "/appl/dcs/data01/tmp/OC-12871/tests/nas_archive"],
        [False, "N007510", ArchiveTarget.NAS,
         "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/nas_archive"],
        [False, "avl4658t", ArchiveTarget.OPS,
         "/appl/dcs/data01/tmp/OC-12871/tests/ops_archive"],
        [False, "N007510", ArchiveTarget.OPS,
         "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/ops_archive"],
        [False, "avl4658t", ArchiveTarget.LOG,
         "/appl/dcs/data01/tmp/OC-12871/tests/log_archive"],
        [False, "N007510", ArchiveTarget.LOG,
         "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/log_archive"]
    ])
    def test_existing_path(self, live, host, target, expected_path):
        archive_paths = ArchivePaths(is_live=live)
        archive_paths._host = host
        self.assertEqual(os.path.normpath(expected_path), archive_paths.get_path(target))

    def test_unknown_host(self):
        logging.disable()
        archive_paths = ArchivePaths()
        archive_paths._host = "potato"
        self.assertRaises(KeyError, archive_paths.get_path, ArchiveTarget.MED)


if __name__ == "__main__":
    unittest.main()
