import unittest
from fractions_app.math import Fraction


class TestFraction(unittest.TestCase):
    def test_fraction_adding(self):
        fraction_1 = Fraction(1, 5) + Fraction(2, 5)
        self.assertEqual(fraction_1, Fraction(3, 5))

        fraction_2 = Fraction(3, 7) + Fraction(2, 7)
        self.assertEqual(fraction_2, Fraction(5, 7))

        fraction_3 = Fraction(1, 3) + Fraction(1, 6)
        self.assertEqual(fraction_3, Fraction(3, 6))

        fraction_4 = Fraction(29, 30) + Fraction(44, 45)
        self.assertEqual(fraction_4, Fraction(175, 90))

        fraction_5 = Fraction(2, 3) + Fraction(1, 2, 1)
        self.assertEqual(fraction_5, Fraction(7, 6, 1))

        fraction_6 = Fraction(5, 6, 1) + Fraction(3, 8, 2)
        self.assertEqual(fraction_6, Fraction(29, 24, 3))

    def test_fraction_substracting(self):
        fraction_1 = Fraction(3, 5) - Fraction(1, 5)
        self.assertEqual(fraction_1, Fraction(2, 5))

        fraction_2 = Fraction(8, 41) - Fraction(5, 41)
        self.assertEqual(fraction_2, Fraction(3, 41))

        fraction_3 = Fraction(5, 6) - Fraction(1, 2)
        self.assertEqual(fraction_3, Fraction(2, 6))

        fraction_4 = Fraction(3, 10) - Fraction(1, 6)
        self.assertEqual(fraction_4, Fraction(4, 30))

        fraction_5 = Fraction(1, 2, 2) - Fraction(1, 3, 1)
        self.assertEqual(fraction_5, Fraction(1, 6, 1))

        fraction_6 = Fraction(1, 6, 3) - Fraction(3, 8, 1)
        self.assertEqual(fraction_6, Fraction(19, 24, 1))

        fraction_7 = Fraction(1, 6, 1) - Fraction(2, 3, 3)
        self.assertEqual(fraction_7, Fraction(3, 6, -2))

    def test_fraction_multiplicating(self):
        fraction_1 = Fraction(3, 7) * 2
        self.assertEqual(fraction_1, Fraction(6, 7))

        fraction_2 = Fraction(1, 2) * 4
        self.assertEqual(fraction_2, Fraction(4, 2))

        fraction_3 = Fraction(3, 7) * Fraction(2, 5)
        self.assertEqual(fraction_3, Fraction(6, 35))

        fraction_4 = Fraction(10, 9) * Fraction(3, 4)
        self.assertEqual(fraction_4, Fraction(30, 36))

        fraction_5 = Fraction(1, 2, 2) * Fraction(2, 3, 1)
        self.assertEqual(fraction_5, Fraction(25, 6))

        fraction_6 = Fraction(1, 3, 4) * 6
        self.assertEqual(fraction_6, Fraction(78, 3))

        fraction_7 = Fraction(1, 7, 2) * Fraction(3, 5)
        self.assertEqual(fraction_7, Fraction(45, 35))

    def test_fraction_dividing(self):
        fraction_1 = Fraction(3, 7) / 2
        self.assertEqual(fraction_1, Fraction(3, 14))

        fraction_2 = Fraction(6, 11) / 3
        self.assertEqual(fraction_2, Fraction(6, 33))

        fraction_3 = Fraction(7, 2).divide_by_number(2)
        self.assertEqual(fraction_3, Fraction(4, 7))

        fraction_4 = Fraction(4, 5).divide_by_number(2)
        self.assertEqual(fraction_4, Fraction(10, 4))

        fraction_5 = Fraction(3, 7) / Fraction(4, 5)
        self.assertEqual(fraction_5, Fraction(15, 28))

        fraction_6 = Fraction(6, 7) / Fraction(4, 7)
        self.assertEqual(fraction_6, Fraction(42, 28))

        fraction_7 = Fraction(1, 2, 1) / Fraction(2, 3, 2)
        self.assertEqual(fraction_7, Fraction(9, 16))

        fraction_8 = Fraction(1, 7, 2) / Fraction(3, 5)
        self.assertEqual(fraction_8, Fraction(75, 21))

    def test_fraction_reducing(self):
        fraction_1 = Fraction(4, 8).reduce()
        self.assertEqual(fraction_1, Fraction(1, 2))

        fraction_2 = Fraction(15, 40).reduce()
        self.assertEqual(fraction_2, Fraction(3, 8))

        fraction_3 = Fraction(126, 426).reduce()
        self.assertEqual(fraction_3, Fraction(21, 71))

        fraction_4 = Fraction(7, 9).reduce()
        self.assertEqual(fraction_4, Fraction(7, 9))
