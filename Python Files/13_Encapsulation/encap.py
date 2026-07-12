class BankAccount:
    def __init__(self):
        self.__balance=1000
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        self.__balance-=amount
    def show_balance(self):
        print("balance ",self.__balance)
obj= BankAccount()
obj.deposit(1000)
obj.withdraw(500)
obj.show_balance()

#1. Employee Salary Management
class Employee:
    def __init__(self):
        self.__salary = 20000
    def increase_salary(self, amount):
        self.__salary += amount
    def decrease_salary(self, amount):
        self.__salary -= amount
    def show_salary(self):
        print("Salary:", self.__salary)

obj = Employee()
obj.increase_salary(5000)
obj.decrease_salary(2000)
obj.show_salary()

#2. Student Marks
class Student:
    def __init__(self):
        self.__marks = 0
    def add_marks(self, mark):
        self.__marks += mark
    def deduct_marks(self, mark):
        self.__marks -= mark
    def show_marks(self):
        print("Marks:", self.__marks)
obj = Student()
obj.add_marks(80)
obj.deduct_marks(10)
obj.show_marks()

#3. Mobile Battery

class Mobile:
    def __init__(self):
        self.__battery = 100

    def charge(self, percent):
        self.__battery += percent

    def use(self, percent):
        self.__battery -= percent

    def show_battery(self):
        print("Battery:", self.__battery, "%")


obj = Mobile()
obj.use(30)
obj.charge(10)
obj.show_battery()

#4. Product Stock
class Product:
    def __init__(self):
        self.__stock = 50

    def add_stock(self, quantity):
        self.__stock += quantity

    def sell_stock(self, quantity):
        self.__stock -= quantity

    def show_stock(self):
        print("Available Stock:", self.__stock)


obj = Product()
obj.add_stock(20)
obj.sell_stock(10)
obj.show_stock()

#5. Water Tank
class WaterTank:
    def __init__(self):
        self.__water_level = 100

    def fill(self, liters):
        self.__water_level += liters

    def use(self, liters):
        self.__water_level -= liters

    def show_level(self):
        print("Water Level:", self.__water_level, "liters")


obj = WaterTank()
obj.fill(50)
obj.use(30)
obj.show_level()

