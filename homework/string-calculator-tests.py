import unittest

from string_calculator import Calculator


class TestCalculate(unittest.TestCase):
    def test_if_input_empty_calculator_return_zero(self):
        calculator = Calculator()

        res = calculator.add("")

        self.assertEqual(res, 0)

    def test_if_input_1_calculator_return_1(self):
        calculator = Calculator()

        res = calculator.add("1")

        self.assertEqual(res, 1)

if __name__ == '__main__':
    unittest.main()