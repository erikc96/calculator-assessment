import unittest
from .calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_sequence(self):
        # Check initial state
        self.assertEqual(self.calc.current, 0)

        # Test 2
        self.assertEqual(self.calc.input('2+45'), 2)

        # Test =
        self.assertEqual(self.calc.input('='), 47)

        # Test *3=
        self.assertEqual(self.calc.input('*3='), 141)

        # Test -8+12=
        self.assertEqual(self.calc.input('-8+12='), 145)

        # Test c
        self.assertEqual(self.calc.input('c'), 0)

if __name__ == '__main__':
    unittest.main()
