import unittest

from string_calculator import Calculator
from string_calculator import NegativesNotAllowed

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

    def test_if_input_any_amount_newline_separate_numbers_calculator_return_their_sum(self):
        calculator = Calculator()

        res = calculator.add("123\n23\n11\n9\n7")

        self.assertEqual(res, 123+23+11+9+7)

    def test_if_input_any_amount_mixed_separate_numbers_calculator_return_their_sum(self):
        calculator = Calculator()

        res = calculator.add("123,23\n11,9\n7")

        self.assertEqual(res, 123+23+11+9+7)

    def test_if_input_any_amount_custom_hash_separate_numbers_calculator_return_their_sum(self):
        calculator = Calculator('#')

        res = calculator.add("123#23#11#9#7")

        self.assertEqual(res, 123+23+11+9+7)

    def test_if_input_contain_custom_one_symbol_separator_in_beginning_string_it_used_for_separate_numbers(self):
        calculator = Calculator()

        res = calculator.add("//;\n1;2")

        self.assertEqual(res, 1+2)

    def test_if_input_contains_of_any_negative_number_exception_is_thrown(self):
        calculator = Calculator()
        negatives = False

        try:
            calculator.add("//;\n1;-2")
        except NegativesNotAllowed:
            negatives = True

        self.assertEqual(negatives, True)

if __name__ == '__main__':
    unittest.main()
