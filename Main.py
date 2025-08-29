class bank:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance

    def withdraw(self, amount):
       
        self._balance -= amount
    def get_balance(self):
        return self._balance

account1 = bank(1234567890, 500)
account1.deposit(200)
account1.withdraw(800)
print(f"Account Number: {account1.account_number}, Balance: {account1.get_balance()}")


#Employee Management
class RegularEmployee:
    def __init__(self, name, salary, bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def describe(self):
        return(f"The employee {self.name} is a regular employee and has earned {self.salary + self.bonus}.")

class ContractEmployee:
    def __init__(self, name, rate_per_hour, hours_worked):
        self.name = name
        self.rate_per_hour = rate_per_hour
        self.hours_worked = hours_worked
    def describe(self):
        return(f"The employee {self.name} is a contract employee and has earned {self.hours_worked * self.rate_per_hour}.")
class Manager:
    def __init__(self, name, salary, allowance):
        self.name = name
        self.salary = salary
        self.allowance = allowance
    def describe(self):
        return(f"The employee {self.name} is a manager and has earned {self.salary +self.allowance}.")


emp1 = RegularEmployee("Mohan", 50000, 5000)
emp2 = ContractEmployee("Karthik", 100, 40)
emp3 = Manager("Dhanwanth", 70000, 10000)

print(emp1.describe())
print(emp2.describe())
print(emp3.describe())




