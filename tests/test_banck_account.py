import os
import unittest
from unittest.mock import patch
from src.bank_account import  BankAccount
from src.exceptions import WithdrawalTimeRestrictionError


class BankAccountTests(unittest.TestCase):

    # setUp is a helper to no duplicated the code
    def setUp(self) -> None:
        self.account = BankAccount(balance=1000, log_file="transaction_log.txt")

    def tearDown(self) -> None:
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)
    
    # funcionalidad dentro del test por eso no lleva test_
    def _count_lines(self, filename):
        with open(filename, "r") as f:
            return len(f.readlines())


    def test_deposit(self):
        # account = BankAccount(balance=1000)
        new_balance = self.account.deposit(500)
        # assert new_balance == 1500 este assert es el nativo de python
        self.assertEqual(new_balance, 1500, "El balance no es igual") # este assert es de unittest

    def test_withdraw(self):
        # account = BankAccount(balance=1000)
        new_balance = self.account.withdraw(200)
        # assert new_balance == 800
        self.assertEqual(new_balance, 800, "El balance no es igual")

    def test_get_balance(self):
        # account = BankAccount(balance=1000)
        # assert self.account.get_balance() == 1000
        self.assertEqual(self.account.get_balance(), 1000)

    def test_check_transfer_amount(self):
        if self.account.get_balance() > 200:
            pass
        else:
            raise ValueError('No disponde del monto necesario')

    def test_transfer_with_enough_balance(self):
        assert self.account.transfer(800) == 200

    def test_transfer_not_enough_balance(self):
        with self.assertRaises(ValueError):
            self.account.transfer(5000)

    def test_transaction_log(self):
        self.account.deposit(500)
        # assert os.path.exists("transaction_log.txt")
        self.assertTrue(os.path.exists("transaction_log.txt"))
    
    def test_count_transactions(self):
        assert self._count_lines(self.account.log_file) == 1
        self.account.deposit(500)
        assert self._count_lines(self.account.log_file) == 2

    def test_transfer_log_amount_smaller_than_balance(self):
        result = self.account.transfer_log(2000)
    
    def test_transfer_log_amount_greater_than_balance(self):
        result = self.account.transfer_log(800)

    # recuerda que el uso de patch como decorador nos envia el parametro que por convenio es muck + lo modificado
    @patch("src.bank_account.datetime")
    def test_withdraw_during_bussines_hours(self, muck_datetime):
        muck_datetime.now.return_value.hour = 8
        new_balance = self.account.withdraw(100)
        self.assertEqual(new_balance, 900)

    
    @patch("src.bank_account.datetime")
    def test_withdraw_disallow_before_bussines_hours(self, muck_datetime):
        muck_datetime.now.return_value.hour = 20
        with self.assertRaises(WithdrawalTimeRestrictionError):
            new_balance = self.account.withdraw(100)


    def test_deposit_some_amounts(self):
        test_cases = [
            {"amount": 100, "expected": 1100},
            {"amount": 3000, "expected": 4000},
            {"amount": 4500, "expected": 5500},
            {"amount": 6000, "expected": 7000},
        ]
        for case in test_cases:
            with self.subTest(case=case):
                self.account = BankAccount(balance=1000, log_file="transactions.py")
                new_balance = self.account.deposit(case["amount"])
                self.assertEqual(new_balance, case["expected"])