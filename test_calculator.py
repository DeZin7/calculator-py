import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(10, 5), 15)
        self.assertRaises(TypeError, self.calculator.add, 10, "5")
        self.assertRaises(TypeError, self.calculator.add, "10", 5)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(10, 5), 2)
        self.assertEqual(self.calculator.divide(-10, 5), -2)
        self.assertEqual(self.calculator.divide(10, -5), -2)
        self.assertRaises(TypeError, self.calculator.divide, 10, "5")
        self.assertRaises(TypeError, self.calculator.divide, "10", 5)
        self.assertRaises(ZeroDivisionError, self.calculator.divide, 10, 0)

if __name__ == "__main__":
    unittest.main()