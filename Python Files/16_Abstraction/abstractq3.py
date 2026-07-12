from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):

    def __init__(self, salary):
        self.salary = salary

    def calculate_salary(self):
        print("Full Time Salary =", self.salary)

class PartTimeEmployee(Employee):

    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate

    def calculate_salary(self):
        print("Part Time Salary =", self.hours * self.rate)

f = FullTimeEmployee(50000)
f.calculate_salary()

p = PartTimeEmployee(40, 500)
p.calculate_salary()