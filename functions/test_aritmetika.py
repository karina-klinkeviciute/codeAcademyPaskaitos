import unittest

from aritmetika import *

class AritmetikaTest(unittest.TestCase):

    def test_sudetis(self):
        rezultatas = sudetis(1, 2)
        lukestis = 3
        self.assertEqual(lukestis, rezultatas)

        self.assertEqual(sudetis(-5, 5), 0)
        self.assertEqual(sudetis(3000000, 4000000), 7000000)

    def test_atimtis(self):
        self.assertEqual(atimtis(5, 2), 3)
        self.assertEqual(atimtis(2, 5), -3)
        self.assertEqual(atimtis(900000, 1), 899999)

    def test_daugyba(self):
        self.assertEqual(daugyba(2, 2), 4)
        self.assertEqual(daugyba(-5, -5), 25)
        self.assertEqual(daugyba(100, 1000), 100000)

    def test_dalyba(self):
        self.assertEqual(dalyba(8, 2), 4)
        self.assertEqual(dalyba(5, 2), 2.5)
        self.assertEqual(dalyba(10, -2), -5)

    def test_dalyba_klaidos(self):
        # vienas budas patikrinimui, ar metama klaida
        self.assertRaises(ZeroDivisionError, dalyba, 10, 0)
        # antras budas patikrinimui, ar metama klaida
        with self.assertRaises(ZeroDivisionError):
            dalyba(10, 0)
