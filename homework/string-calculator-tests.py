import unittest

from string_calculator import Calculator


class TestCalculate(unittest.TestCase):
    def test_if_input_empty_calculator_return_zero(self): #if_input_empty_calculator_return_zero
        calculator = Calculator()

        res = calculator.add("")

        self.assertEqual(res, 0)


if __name__ == '__main__':
    unittest.main()
