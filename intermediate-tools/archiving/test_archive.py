import os.path
import socket
import unittest

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
    def test_avl4658t_live_mediation(self):
        archive = Archive(is_live=True)
        archive._host = "avl4658t"
        self.assertEqual(os.path.normpath("/appl/dcs/data01/tmp/OC-12871/mediation_archive"),
                         archive.get_path(ArchiveTarget.MEDIATION))


if __name__ == "__main__":
    unittest.main()
