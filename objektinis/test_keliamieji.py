import unittest

from objektinis.keliamieji import Keliamieji


class KeliamiejiCase(unittest.TestCase):
    def setUp(self):
        self.keliamieji = Keliamieji()

    def test_tikrinti(self):
        self.assertFalse(self.keliamieji.tikrinti(2023))
        self.assertTrue(self.keliamieji.tikrinti(2020))
        self.assertFalse(self.keliamieji.tikrinti(2100))
        self.assertTrue(self.keliamieji.tikrinti(2000))

    def test_diapazonas(self):
        self.assertEqual(self.keliamieji.diapazonas(2000, 2021), [2000, 2004, 2008, 2012, 2016, 2020])
        self.assertEqual(self.keliamieji.diapazonas(1990, 2001), [1992, 1996, 2000])


if __name__ == '__main__':
    unittest.main()
