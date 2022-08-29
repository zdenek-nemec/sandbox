import os.path
import socket
import unittest

from parameterized import parameterized

from archive import Archive
from archive import ArchiveTarget


class TestInit(unittest.TestCase):
    def test_default(self):
        archive = Archive()
        self.assertEqual(False, archive._is_live)
        self.assertEqual(socket.gethostname(), archive._host)

    def test_is_live_true(self):
        archive = Archive(True)
        self.assertEqual(True, archive._is_live)

    def test_is_live_false(self):
        archive = Archive(False)
        self.assertEqual(False, archive._is_live)


class TestIsLive(unittest.TestCase):
    def test_true(self):
        archive = Archive()
        archive._is_live = True
        self.assertEqual(True, archive.is_live())

    def test_false(self):
        archive = Archive()
        archive._is_live = False
        self.assertEqual(False, archive.is_live())


class TestGetPath(unittest.TestCase):
    @parameterized.expand([
        [True, "avl4658t", ArchiveTarget.MEDIATION, "/appl/dcs/data01/tmp/OC-12871/mediation_archive"],
        [True, "JISKRA", ArchiveTarget.MEDIATION, "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target1_mediation", ],
        [True, "N007510", ArchiveTarget.MEDIATION, "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target1_mediation"],
        [True, "avl4658t", ArchiveTarget.TAR, "/appl/dcs/data01/tmp/OC-12871/tar_archive"],
        [True, "JISKRA", ArchiveTarget.TAR, "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target2_tar", ],
        [True, "N007510", ArchiveTarget.TAR, "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target2_tar"],
        [True, "avl4658t", ArchiveTarget.NAS, "/appl/dcs/data01/tmp/OC-12871/nas_archive"],
        [True, "JISKRA", ArchiveTarget.NAS, "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target3_nas", ],
        [True, "N007510", ArchiveTarget.NAS, "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target3_nas"],
        [True, "avl4658t", ArchiveTarget.OPS, "/appl/dcs/data01/tmp/OC-12871/ops_archive"],
        [True, "JISKRA", ArchiveTarget.OPS, "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target4_ops", ],
        [True, "N007510", ArchiveTarget.OPS, "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target4_ops"],
        [False, "avl4658t", ArchiveTarget.MEDIATION, "/appl/dcs/data01/tmp/OC-12871/tests/target1_mediation"],
        [False, "JISKRA", ArchiveTarget.MEDIATION, "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target1_mediation", ],
        [False, "N007510", ArchiveTarget.MEDIATION, "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target1_mediation"],
        [False, "avl4658t", ArchiveTarget.TAR, "/appl/dcs/data01/tmp/OC-12871/tests/target2_tar"],
        [False, "JISKRA", ArchiveTarget.TAR, "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target2_tar", ],
        [False, "N007510", ArchiveTarget.TAR, "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target2_tar"],
        [False, "avl4658t", ArchiveTarget.NAS, "/appl/dcs/data01/tmp/OC-12871/tests/target3_nas"],
        [False, "JISKRA", ArchiveTarget.NAS, "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target3_nas", ],
        [False, "N007510", ArchiveTarget.NAS, "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target3_nas"],
        [False, "avl4658t", ArchiveTarget.OPS, "/appl/dcs/data01/tmp/OC-12871/tests/target4_ops"],
        [False, "JISKRA", ArchiveTarget.OPS, "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target4_ops", ],
        [False, "N007510", ArchiveTarget.OPS, "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target4_ops"]
    ])
    def test_live_mediation(self, live, host, target, expected_path):
        archive = Archive(is_live=live)
        archive._host = host
        self.assertEqual(
            os.path.normpath(expected_path),
            archive.get_path(target))


if __name__ == "__main__":
    unittest.main()
