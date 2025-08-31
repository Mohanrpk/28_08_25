# from operator import __not__


# class bank:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self._balance = balance

#     def deposit(self, amount):
#         self._balance += amount

#     def get_balance(self):
#         return self._balance

#     def withdraw(self, amount):
       
#         self._balance -= amount
#     def get_balance(self):
#         return self._balance

# account1 = bank(1234567890, 500)
# account1.deposit(200)
# account1.withdraw(800)
# print(f"Account Number: {account1.account_number}, Balance: {account1.get_balance()}")


# #Employee Management
# class RegularEmployee:
#     def __init__(self, name, salary, bonus):
#         self.name = name
#         self.salary = salary
#         self.bonus = bonus

#     def describe(self):
#         return(f"The employee {self.name} is a regular employee and has earned {self.salary + self.bonus}.")

# class ContractEmployee:
#     def __init__(self, name, rate_per_hour, hours_worked):
#         self.name = name
#         self.rate_per_hour = rate_per_hour
#         self.hours_worked = hours_worked
#     def describe(self):
#         return(f"The employee {self.name} is a contract employee and has earned {self.hours_worked * self.rate_per_hour}.")
# class Manager:
#     def __init__(self, name, salary, allowance):
#         self.name = name
#         self.salary = salary
#         self.allowance = allowance
#     def describe(self):
#         return(f"The employee {self.name} is a manager and has earned {self.salary +self.allowance}.")


# emp1 = RegularEmployee("Mohan", 50000, 5000)
# emp2 = ContractEmployee("Karthik", 100, 40)
# emp3 = Manager("Dhanwanth", 70000, 10000)

# print(emp1.describe())
# print(emp2.describe())
# print(emp3.describe())




class vehicle:
    def __init__(self, model, rental_rate):
        self.model = model
        self.rental_rate = rental_rate

    def calculate_rental(self, days):
        return self.rental_rate * days
    

    
class car(vehicle):
    def __init__(self, model, rental_rate):
        super().__init__(model, rental_rate)
    def calculate_rental(self, duration):
        return self.rental_rate * duration
    def describe(self):
        return f"{self.model} is a car with a rental rate of {self.rental_rate * 5} for 5 days."

class bike(vehicle):
    def __init__(self, model, rental_rate):
        super().__init__(model, rental_rate)
    def calculate_rental(self, duration):
        return self.rental_rate * duration
    def describe(self):
        return f"{self.model} is a bike with a rental rate of {self.rental_rate * 5} for 5 days."

class truck(vehicle):
    def __init__(self, model, rental_rate):
        super().__init__(model, rental_rate)
    def calculate_rental(self, duration):
        return self.rental_rate * duration
    def describe(self):
        return f"{self.model} is a truck with a rental rate of {self.rental_rate * 5} for 5 days."
    
model1 = car("Honda city", 2000)
model2 = bike("Royal Enfield", 1000)
model3 = truck("Ashok Leyland", 10000)
    
print(model1.describe())
print(model2.describe())
print(model3.describe())
