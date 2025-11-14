class BankAccount:
    def __init__(self, name, balance, interest_rate):
        self.name = name
        self.balance = balance
        self.interest_rate = interest_rate

    def withdraw(self, name, amount):
        if name != self.name:
            print('You are not authorized for this account.')
            return None
        if self.balance < amount:
            print(f"Insufficient fund for withdrawal of ${amount}.")
            return 0
        else:
            self.balance -= amount
            return amount
        
    def show_balance(self):
        print(f"Account balance is ${self.balance}.")

    def deposit(self, amount):
        self.balance += amount

    def year_end_processing(self):
        self.balance *= (1 + self.interest_rate)

    def transfer_to(self, other, amount):
        if other.balance < amount:
            print('Insufficient funds for transfer.')
        else:
            other.balance += amount
            self.balance -= amount

class MinimumAccount(BankAccount):
    def __init__(self, name, balance):
        super().__init__(name, balance, 0.1)
    
    def year_end_processing(self):
        if self.balance <= 1000:
            if self.balance <= 20:
                self.balance = 0
            else:
                self.balance -= 20
        super().year_end_processing()