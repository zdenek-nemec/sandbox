import os.path
import socket
import unittest

from parameterized import parameterized

from archive_paths import ArchivePaths
from archive_target import ArchiveTarget


class TestInit(unittest.TestCase):
    def test_default(self):
        archive = ArchivePaths()
        self.assertEqual(False, archive._is_live)
        self.assertEqual(socket.gethostname(), archive._host)

    def test_is_live_true(self):
        archive = ArchivePaths(True)
        self.assertEqual(True, archive._is_live)

    def test_is_live_false(self):
        archive = ArchivePaths(False)
        self.assertEqual(False, archive._is_live)


class TestIsLive(unittest.TestCase):
    def test_true(self):
        archive = ArchivePaths()
        archive._is_live = True
        self.assertEqual(True, archive.is_live())

    def test_false(self):
        archive = ArchivePaths()
        archive._is_live = False
        self.assertEqual(False, archive.is_live())


class TestGetPath(unittest.TestCase):
    @parameterized.expand([
        [True, "avl4658t", ArchiveTarget.MEDIATION,
         "/appl/dcs/data01/tmp/OC-12871/mediation_archive"],
        [True, "N007510", ArchiveTarget.MEDIATION,
         "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target1_mediation"],
        [True, "avl4658t", ArchiveTarget.TAR,
         "/appl/dcs/data01/tmp/OC-12871/tar_archive"],
        [True, "N007510", ArchiveTarget.TAR,
         "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target2_tar"],
        [True, "avl4658t", ArchiveTarget.NAS,
         "/appl/dcs/data01/tmp/OC-12871/nas_archive"],
        [True, "N007510", ArchiveTarget.NAS,
         "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target3_nas"],
        [True, "avl4658t", ArchiveTarget.OPS,
         "/appl/dcs/data01/tmp/OC-12871/ops_archive"],
        [True, "N007510", ArchiveTarget.OPS,
         "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target4_ops"],
        [False, "avl4658t", ArchiveTarget.MEDIATION,
         "/appl/dcs/data01/tmp/OC-12871/tests/target1_mediation"],
        [False, "N007510", ArchiveTarget.MEDIATION,
         "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target1_mediation"],
        [False, "avl4658t", ArchiveTarget.TAR,
         "/appl/dcs/data01/tmp/OC-12871/tests/target2_tar"],
        [False, "N007510", ArchiveTarget.TAR,
         "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target2_tar"],
        [False, "avl4658t", ArchiveTarget.NAS,
         "/appl/dcs/data01/tmp/OC-12871/tests/target3_nas"],
        [False, "N007510", ArchiveTarget.NAS,
         "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target3_nas"],
        [False, "avl4658t", ArchiveTarget.OPS,
         "/appl/dcs/data01/tmp/OC-12871/tests/target4_ops"],
        [False, "N007510", ArchiveTarget.OPS,
         "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target4_ops"]
    ])
    def test_live_mediation(self, live, host, target, expected_path):
        archive = ArchivePaths(is_live=live)
        archive._host = host
        self.assertEqual(os.path.normpath(expected_path), archive.get_path(target))


if __name__ == "__main__":
    unittest.main()
