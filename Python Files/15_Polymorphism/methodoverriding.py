#1. Shape Area Calculation
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def area(self, length, breadth):
        print("Area of Rectangle =", length * breadth)

class Circle(Shape):
    def area(self, radius):
        print("Area of Circle =", 3.14 * radius * radius)

r = Rectangle()
c = Circle()

r.area(5, 4)
c.area(3)

#2. Student and Teacher Roles
class Student:
    def role(self):
        print("Student studies subjects")

class Teacher:
    def role(self):
        print("Teacher teaches students")

s = Student()
t = Teacher()

s.role()
t.role()

#3. Food Ordering System
class FoodItem:
    def calculate_price(self):
        pass

class Pizza(FoodItem):
    def calculate_price(self, qty):
        print("Pizza Bill =", qty * 200)

class Burger(FoodItem):
    def calculate_price(self, qty):
        print("Burger Bill =", qty * 120)

class Sandwich(FoodItem):
    def calculate_price(self, qty):
        print("Sandwich Bill =", qty * 80)

p = Pizza()
b = Burger()
s = Sandwich()

p.calculate_price(2)
b.calculate_price(3)
s.calculate_price(4)

#4. Employee Bonus Calculator
class Employee:
    def bonus(self):
        pass

class Manager(Employee):
    def bonus(self, salary):
        print("Manager Bonus =", salary * 0.20)

class Developer(Employee):
    def bonus(self, salary):
        print("Developer Bonus =", salary * 0.15)

class Tester(Employee):
    def bonus(self, salary):
        print("Tester Bonus =", salary * 0.10)

m = Manager()
d = Developer()
t = Tester()

salary = 50000

m.bonus(salary)
d.bonus(salary)
t.bonus(salary)

#5. Ticket Booking System
class Ticket:
    def price(self, distance):
        pass

class BusTicket(Ticket):
    def price(self, distance):
        print("Bus Fare =", distance * 2)

class TrainTicket(Ticket):
    def price(self, distance):
        print("Train Fare =", distance * 3)

class FlightTicket(Ticket):
    def price(self, distance):
        print("Flight Fare =", distance * 10)

b = BusTicket()
t = TrainTicket()
f = FlightTicket()

distance = 100

b.price(distance)
t.price(distance)
f.price(distance)