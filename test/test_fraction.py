import unittest
from fractions_app.math import Fraction


class TestFraction(unittest.TestCase):
    def test_fraction_initializing(self):
        Fraction(5, 7)
        Fraction(1, 2, 3)
        Fraction(0, 2, 3)
        Fraction(-1, 2, 3)
        Fraction(-6, 2, -3)

        with self.assertRaises(ValueError):
            Fraction(1.2, 5)
        with self.assertRaises(ValueError):
            Fraction(6, 0)
        with self.assertRaises(ValueError):
            Fraction(2, 5, "2")
        with self.assertRaises(ValueError):
            Fraction(9, 5, None)
        with self.assertRaises(ValueError):
            Fraction(0, -2, -3)
        with self.assertRaises(ValueError):
            Fraction(0, -2, 3)

    def test_fraction_reducing(self):
        fraction = Fraction(12, 3).reduce()
        self.assertEqual(fraction, Fraction(4, 1))

        fraction = Fraction(6, 12).reduce()
        self.assertEqual(fraction, Fraction(1, 2))

        fraction = Fraction(7, 5).reduce()
        self.assertEqual(fraction, Fraction(7, 5))

        fraction = Fraction(9, 4).reduce()
        self.assertEqual(fraction, Fraction(9, 4))

        fraction = Fraction(0, 3, 1).reduce()
        self.assertEqual(fraction, Fraction(0, 1))

        fraction = Fraction(2, 2, 2).reduce()
        self.assertEqual(fraction, Fraction(1, 1, 2))

    def test_fraction_convertion_to_improper_fraction(self):
        fraction = Fraction(2, 8).to_improper_fraction()
        self.assertEqual(fraction, Fraction(2, 8))

        fraction = Fraction(6, 9, 1).to_improper_fraction()
        self.assertEqual(fraction, Fraction(15, 9))

        fraction = Fraction(0, 5, 1).to_improper_fraction()
        self.assertEqual(fraction, Fraction(5, 5))

        fraction = Fraction(4, 2, 1).to_improper_fraction()
        self.assertEqual(fraction, Fraction(6, 2))

    def test_fraction_convertion_to_proper_fraction(self):
        fraction = Fraction(2, 6).to_proper_fraction()
        self.assertEqual(fraction, Fraction(2, 6))

        fraction = Fraction(0, 6).to_proper_fraction()
        self.assertEqual(fraction, Fraction(0, 6))

        fraction = Fraction(1, 6).to_proper_fraction()
        self.assertEqual(fraction, Fraction(1, 6))

        fraction = Fraction(6, 1).to_proper_fraction()
        self.assertEqual(fraction, Fraction(1, 1, 6))

        fraction = Fraction(60, 8).to_proper_fraction()
        self.assertEqual(fraction, Fraction(4, 8, 7))

        fraction = Fraction(-15, 8).to_proper_fraction()
        self.assertEqual(fraction, Fraction(7, 8, -1))
