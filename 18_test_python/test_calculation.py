# test_calculation.py
import unittest
from calculation import add, divide, subtract, multiply

class TestCalculation(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15) # add(10,5)と15が等しい場合OK
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(20, 30), -10)

    def test_multiply(self):
        self.assertEqual(multiply(1, 1), 1)
        self.assertEqual(multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(divide(10, 4), 2.5)
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()
