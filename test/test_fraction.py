import unittest
from fractions_app.math import Fraction, get_highest_common_divider


class TestFraction(unittest.TestCase):
    def test_fraction_adding(self):
        fraction_1 = Fraction(1, 5) + Fraction(2, 5)
        self.assertEqual(fraction_1, Fraction(15, 25))

        fraction_2 = Fraction(3, 7) + Fraction(2, 7)
        self.assertEqual(fraction_2, Fraction(35, 49))

        fraction_3 = Fraction(3, 5) + Fraction(5, 6)
        self.assertEqual(fraction_3, Fraction(43, 30))

        fraction_4 = Fraction(44, 45) + Fraction(29, 30)
        self.assertEqual(fraction_4, Fraction(2625, 1350))

        fraction_5 = Fraction(2, 3) + Fraction(1, 2, 1)
        self.assertEqual(fraction_5, Fraction(13, 6))

        fraction_6 = Fraction(5, 6, 1) + Fraction(3, 8, 2)
        self.assertEqual(fraction_6, Fraction(202, 48))

        fraction_7 = Fraction(5, 6) + 8
        self.assertEqual(fraction_7, Fraction(5, 6, 8))

        fraction_8 = Fraction(5, 2, 2) + 8
        self.assertEqual(fraction_8, Fraction(5, 2, 10))

    def test_fraction_substracting(self):
        fraction_1 = Fraction(3, 5) - Fraction(1, 5)
        self.assertEqual(fraction_1, Fraction(10, 25))

        fraction_2 = Fraction(5, 41) - Fraction(8, 41)
        self.assertEqual(fraction_2, Fraction(-123, 1681))

        fraction_3 = Fraction(5, 6) - Fraction(3, 5)
        self.assertEqual(fraction_3, Fraction(7, 30))

        fraction_4 = Fraction(4, 10) - Fraction(7, 9)
        self.assertEqual(fraction_4, Fraction(-34, 90))

        fraction_5 = Fraction(4, 9) - Fraction(4, 9)
        self.assertEqual(fraction_5, Fraction(0, 81))

        fraction_6 = Fraction(6, 13) - Fraction(6, 13)
        self.assertEqual(fraction_6, Fraction(0, 169))

        fraction_7 = Fraction(4, 7, 2) - Fraction(2, 3, 1)
        self.assertEqual(fraction_7, Fraction(19, 21))

        fraction_8 = Fraction(1, 6, 3) - Fraction(3, 8, 1)
        self.assertEqual(fraction_8, Fraction(86, 48))

        fraction_9 = Fraction(1, 6, 1) - Fraction(2, 3, 3)
        self.assertEqual(fraction_9, Fraction(-45, 18))

        fraction_10 = Fraction(5, 6) - 8
        self.assertEqual(fraction_10, Fraction(-43, 6))

        fraction_11 = Fraction(5, 6, 2) - 4
        self.assertEqual(fraction_11, Fraction(-7, 6))

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
        result = Fraction(-123, 1681).reduce()
        self.assertEqual(result, Fraction(-3, 41))

        fraction_1 = Fraction(4, 8).reduce()
        self.assertEqual(fraction_1, Fraction(1, 2))

        fraction_2 = Fraction(15, 40).reduce()
        self.assertEqual(fraction_2, Fraction(3, 8))

        result = Fraction(-45, 18).reduce()
        self.assertEqual(result, Fraction(-5, 2))

        fraction_4 = Fraction(1681, 123).reduce()
        self.assertEqual(fraction_4, Fraction(41, 3))

        fraction_5 = Fraction(0, 81).reduce()
        self.assertEqual(fraction_5, Fraction(0, 0))

        fraction_6 = Fraction(0, 169).reduce()
        self.assertEqual(fraction_6, Fraction(0, 0))

    def test_fraction_simplifing(self):
        result = Fraction(-123, 1681).simplify()
        self.assertEqual(result, Fraction(-3, 41))

        fraction_1 = Fraction(4, 8).simplify()
        self.assertEqual(fraction_1, Fraction(1, 2))

        fraction_2 = Fraction(15, 40).simplify()
        self.assertEqual(fraction_2, Fraction(3, 8))

        result = Fraction(-45, 18).simplify()
        self.assertEqual(result, Fraction(1, 2, -3))

        fraction_4 = Fraction(1681, 123).simplify()
        self.assertEqual(fraction_4, Fraction(2, 3, 13))

    def test_getting_common_divider(self):
        self.assertEqual(get_highest_common_divider(10, 9), 1)
        self.assertEqual(get_highest_common_divider(5, 9), 1)
        self.assertEqual(get_highest_common_divider(-45, 18), 9)
        self.assertEqual(get_highest_common_divider(15, 5), 5)

    def test_fraction_immutability(self):
        operand_1, operand_2 = Fraction(3, 7, 1), Fraction(4, 7, 2)

        operand_1_copy = operand_1.copy()
        operand_2_copy = operand_2.copy()

        self.assertIsNot(operand_1_copy, operand_1)
        self.assertIsNot(operand_2_copy, operand_2)
        res = operand_1_copy + operand_2_copy
        self.assertEqual(operand_1_copy, operand_1)
        self.assertEqual(operand_2_copy, operand_2)
        res = operand_1_copy - operand_2_copy
        self.assertEqual(operand_1_copy, operand_1)
        self.assertEqual(operand_2_copy, operand_2)
        res = operand_1_copy / operand_2_copy
        self.assertEqual(operand_1_copy, operand_1)
        self.assertEqual(operand_2_copy, operand_2)
        operand_1_copy.divide_by_number(4)
        self.assertEqual(operand_1_copy, operand_1)
        res = operand_1_copy * operand_2_copy
        self.assertEqual(operand_1_copy, operand_1)
        self.assertEqual(operand_2_copy, operand_2)

        operand_1_copy.reduce()
        self.assertEqual(operand_1_copy, operand_1)
        operand_1_copy.convert_to_improper_fraction()
        self.assertEqual(operand_1_copy, operand_1)
        operand_1_copy.simplify()
        self.assertEqual(operand_1_copy, operand_1)

    def test_fraction_converting(self):
        fraction_1 = Fraction(1, 2).convert_to_float()
        self.assertAlmostEqual(fraction_1, 0.5)
        fraction_2 = Fraction(3, 6).convert_to_float()
        self.assertAlmostEqual(fraction_2, 0.5)

        fraction_3 = Fraction(8, 5).convert_to_float()
        self.assertAlmostEqual(fraction_3, 1.6)
        fraction_4 = Fraction(18, 8).convert_to_float()
        self.assertAlmostEqual(fraction_4, 2.25)

        fraction_5 = Fraction(3, 8, 1).convert_to_float()
        self.assertAlmostEqual(fraction_5, 1.375)
        fraction_6 = Fraction(3, 5, 4).convert_to_float()
        self.assertAlmostEqual(fraction_6, 4.6)

    def test_fraction_logic_operators(self):
        fraction_1 = Fraction(9, 12)
        fraction_2 = Fraction(7, 12)
        self.assertFalse(fraction_1 < fraction_2)

        fraction_3 = Fraction(1, 2)
        fraction_4 = Fraction(8, 9)
        self.assertFalse(fraction_3 > fraction_4)

        fraction_5 = Fraction(7, 9, 1)
        fraction_6 = Fraction(6, 7)
        self.assertFalse(fraction_5 < fraction_6)
