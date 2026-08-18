import unittest
from money import Dollar

class TestMoney(unittest.TestCase):
    def test_multiplication(self):
        five = Dollar(5)
        five.times(2)
        # $5 * 2 = $10 であることを期待する
        self.assertEqual(10, five.amount)

if __name__ == '__main__':
    unittest.main()
