import unittest

from photo_gallery import PhotoGallery


class TestPhotoGallery(unittest.TestCase):
    def test_get_image_files(self):
        pg = PhotoGallery.__new__(PhotoGallery)
        pg.pics_folder = "./pics"
        self.assertEqual(type(pg.get_image_files()), list)


if __name__ == "__main__":
    unittest.main()
