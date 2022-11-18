import pytest
from account import *

class Test:

    def setup_method(self):
        self.account1 = Account('test1')

    def teardown_method(self):
        del self.account1

    def test_init(self):
        assert self.account1.get_name() == 'test1'
        assert self.account1.get_balance() == 0

    def test_deposit(self):
        assert self.account1.deposit(1000) == True
        assert self.account1.get_balance() == 1000
        assert self.account1.deposit(-1000) == False
        assert self.account1.get_balance() == 1000
        assert self.account1.deposit(1000.45) == True
        assert self.account1.get_balance() == pytest.approx(2000.45, abs=0.001)
        assert self.account1.deposit(0) == False
        assert self.account1.get_balance() == pytest.approx(2000.45, abs=0.001)

    def test_withdraw(self):
        assert self.account1.withdraw(1000) == False
        assert self.account1.get_balance() == 0
        assert self.account1.withdraw(0) == False
        assert self.account1.get_balance() == 0
        self.account1.deposit(5000)
        assert self.account1.withdraw(1000.45) == True
        assert self.account1.get_balance() == pytest.approx(3999.55, abs=0.001)
        assert self.account1.withdraw(-1000) == False
        assert self.account1.get_balance() == pytest.approx(3999.55, abs=0.001)



