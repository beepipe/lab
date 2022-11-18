import unittest
from account import *

class MyTestCase(unittest.TestCase):

    delta_value = 0.001

    def setUp(self):
        self.account1 = Account('test1')

    def tearDown(self):
        del self.account1

    def test_init(self):
        self.assertEqual(self.account1.get_name(), 'test1')
        self.assertEqual(self.account1.get_balance(), 0)


    def test_deposit(self):
        self.assertEqual(self.account1.deposit(1000), True)
        self.assertEqual(self.account1.deposit(-1000), False)
        self.assertEqual(self.account1.deposit(1000.45), True)
        self.assertEqual(self.account1.deposit(-1000.30), False)

        self.assertRaises(TypeError, self.account1.deposit, 'string')


    def test_withdraw(self):
        self.assertEqual(self.account1.withdraw(1000), False)
        self.assertEqual(self.account1.withdraw(-1000), False)
        self.assertEqual(self.account1.withdraw(1000.45), False)
        self.assertEqual(self.account1.withdraw(-1000.30), False)

        self.assertRaises(TypeError, self.account1.withdraw, 'string')


if __name__ == '__main__':
    unittest.main()