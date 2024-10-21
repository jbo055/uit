class Account:
    def __init__(self, cust_id, account_no, balance: int = 0, interest: int = 5):
        self._cust_id = cust_id
        self._account_no = account_no
        self._balance = balance
        self._interest = interest
        self._transactions = []
    
    def __str__(self) -> str:
        return (f'Customer id = {self._cust_id}\n'
                f'Account no = {self._account_no}\n'
                f'Balance = {self._balance}\n'
                f'Interest = {self._interest}\n')
    
    @property
    def cust_id(self) -> int:
        return self._cust_id
    
    @property
    def account_no(self) -> int:
        return self._account_no
    
    @property
    def balance(self) -> int:
        return self._balance
    
    @property
    def interest(self) -> int:
        return self._interest

    def deposit(self, amount: float) -> float:
        if amount > 0:
            self._balance += amount
            self._transactions.append(Transaction(amount))
        return self._balance
    
    def withdraw(self, amount: float) -> float:
        if amount > 0 and self._balance >= amount:
            self._balance -= amount
            self._transactions.append(Transaction(-amount))
        return self._balance
    
    
    
    def showTransactions(self):
        for transaction in self._transactions:
            print(transaction)
    
from datetime import datetime

class Transaction:
    def __init__(self, amount: float):
        self._amount = amount
        self._time = self._getTimeAsString()

    def _getTimeAsString(self) -> str:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    @property
    def time(self) -> str:
        return self._time
    
    @property
    def amount(self) -> float:
        return self._amount
    
    def __str__(self) -> str:
        return (f'Transaction timestamp: {self._time}, amount: {self._amount}')
    


# Testkode
account1 = Account(1, 1000, 50000, 7)
print(account1)
account1.deposit(500)
print(f'New balance after deposit: {account1.balance}')
account1.withdraw(1000)
print(f'New balance after withdrawal: {account1.balance}')
account1.showTransactions()