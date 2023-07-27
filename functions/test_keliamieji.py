import unittest

from keliamieji_metai import ar_keliamieji

class KeliamiejiTest(unittest.TestCase):

    def test_ar_keliamieji(self):
        rezultatas = ar_keliamieji(2100)
        lukestis = "Nekeliamieji"
        self.assertEqual(lukestis, rezultatas)
        self.assertEqual("Keliamieji", ar_keliamieji(2020))
        self.assertEqual("Nekeliamieji", ar_keliamieji(2021))
        self.assertEqual("Keliamieji", ar_keliamieji(2000))
