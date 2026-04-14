class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance
        print(balance)
    def deposit(self, amount):
        self._balance +=amount
        
        return print(self._balance)
    def withdraw(self, amount):
        if amount >self._balance:
            print("insufficeint funds")
        else:
            self._balance -=amount
            
            return print(self._balance)
class SavingsAccount(BankAccount):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate =interest_rate
    def apply_interest_rate(self):
        self._balance +=self._balance *self.interest_rate
        return self._balance
savingmoney =BankAccount(0)
interest_Rate = SavingsAccount(1000, 0.05)
amount_in_bank = savingmoney.deposit(1000)
amount_in_bank = savingmoney.withdraw(500)
amount_in_bank = interest_Rate.apply_interest_rate()