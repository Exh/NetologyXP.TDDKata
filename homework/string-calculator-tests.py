import unittest

from string_calculator import Calculator


class TestCalculate(unittest.TestCase):
    def test_if_input_empty_calculator_return_zero(self):
        calculator = Calculator()

        res = calculator.add("")

        self.assertEqual(res, 0)

    def test_if_input_single_number_calculator_return_number(self):
        calculator = Calculator()

        res = calculator.add("17")

        self.assertEqual(res, 17)

    def test_if_input_two_comma_separate_single_numbers_calculator_return_their_sum(self):
        calculator = Calculator()

        res = calculator.add("1,4")

        self.assertEqual(res, 5)

    def test_if_input_two_comma_separate_any_numbers_calculator_return_their_sum(self):
        calculator = Calculator()

        res = calculator.add("456, 111")

        self.assertEqual(res, 567)

    def test_if_input_any_amount_comma_separate_numbers_calculator_return_their_sum(self):
        calculator = Calculator()

        res = calculator.add("123,23,11,9,7")

        self.assertEqual(res, 123+23+11+9+7)

if __name__ == '__main__':
    unittest.main()
