import unittest
from fractions_app.helper import (
    generate_mixed_fractions,
    generate_proper_fractions_with_unlike_denominators,
    generate_proper_fractions_with_like_denominators,
    generate_proper_fraction,
)


class TestFraction(unittest.TestCase):
    def test_fractions_with_like_denominators(self):
        for _ in range(100):
            fraction_1, fraction_2 = generate_proper_fractions_with_like_denominators()
            self.assertEqual(fraction_1.integer, 0)
            self.assertEqual(fraction_2.integer, 0)
            self.assertEqual(fraction_1.denominator, fraction_2.denominator)
            self.assertLessEqual(fraction_1.numerator, fraction_1.denominator)
            self.assertLessEqual(fraction_2.numerator, fraction_2.denominator)

    def test_fractions_with_unlike_denominators(self):
        for _ in range(100):
            (
                fraction_1,
                fraction_2,
            ) = generate_proper_fractions_with_unlike_denominators()
            self.assertEqual(fraction_1.integer, 0)
            self.assertEqual(fraction_2.integer, 0)
            self.assertNotEqual(fraction_1.denominator, fraction_2.denominator)
            self.assertLessEqual(fraction_1.numerator, fraction_1.denominator)
            self.assertLessEqual(fraction_2.numerator, fraction_2.denominator)

    def test_mixed_fractions(self):
        for _ in range(100):
            fraction_1, fraction_2 = generate_mixed_fractions()
            self.assertGreater(fraction_1.integer, 0)
            self.assertGreater(fraction_2.integer, 0)
            self.assertNotEqual(fraction_1.denominator, fraction_2.denominator)
            self.assertLessEqual(fraction_1.numerator, fraction_1.denominator)
            self.assertLessEqual(fraction_2.numerator, fraction_2.denominator)

    def test_proper_fraction_generator(self):
        for _ in range(100):
            fraction = generate_proper_fraction()
            self.assertLessEqual(fraction.numerator, fraction.denominator)
            self.assertEqual(fraction.integer, 0)
