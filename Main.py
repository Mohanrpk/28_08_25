class bank:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New balance: {self.balance}")
        else:
            print("Enter valid amount")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}. New balance: {self.balance}")

account1 = bank(1234567890, 500)
account1.deposit(200)
account1.withdraw(800)

class savings_account(bank):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Interest added: {interest}. New balance: {self.balance}")
savings1 = savings_account(9876543210, 500, 5)
savings1.add_interest()

