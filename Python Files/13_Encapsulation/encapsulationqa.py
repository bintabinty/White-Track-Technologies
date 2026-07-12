#1. Student Class
class Student:
    def __init__(self):
        self.__name = ""

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        print("Name:", self.__name)


obj = Student()
obj.set_name("Binty")
obj.get_name()

#2. Bank Account Class
class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        print("Balance:", self.__balance)


obj = BankAccount()
obj.deposit(5000)
obj.get_balance()

#3. Employee Class
class Employee:
    def __init__(self):
        self.__salary = 0

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        print("Salary:", self.__salary)


obj = Employee()
obj.set_salary(30000)
obj.get_salary()

#4. Car Class
class Car:
    def __init__(self):
        self.__speed = 0

    def set_speed(self, speed):
        self.__speed = speed

    def get_speed(self):
        print("Speed:", self.__speed, "km/h")


obj = Car()
obj.set_speed(80)
obj.get_speed()

#5. Password Manager Class
class PasswordManager:
    def __init__(self):
        self.__password = ""

    def set_password(self, password):
        self.__password = password

    def verify_password(self, password):
        if self.__password == password:
            print("Password Verified")
        else:
            print("Incorrect Password")


obj = PasswordManager()
obj.set_password("admin123")

obj.verify_password("admin123")
obj.verify_password("1234")

#6. Laptop Class
class Laptop:
    def __init__(self):
        self.__brand = ""

    def set_brand(self, brand):
        self.__brand = brand

    def get_brand(self):
        print("Brand:", self.__brand)


obj = Laptop()
obj.set_brand("Dell")
obj.get_brand()

#7. Book Class
class Book:
    def __init__(self):
        self.__title = ""

    def set_title(self, title):
        self.__title = title

    def get_title(self):
        print("Title:", self.__title)


obj = Book()
obj.set_title("Python Programming")
obj.get_title()

#8.Temperature Class
class Temperature:
    def __init__(self):
        self.__celsius = 0

    def set_temperature(self, celsius):
        self.__celsius = celsius

    def get_temperature(self):
        print("Temperature:", self.__celsius, "°C")


obj = Temperature()
obj.set_temperature(25)
obj.get_temperature()

#9.Movie Class
class Movie:
    def __init__(self):
        self.__rating = 0

    def set_rating(self, rating):
        self.__rating = rating

    def get_rating(self):
        print("Rating:", self.__rating)


obj = Movie()
obj.set_rating(4.5)
obj.get_rating()

#10.Patient Class
class Patient:
    def __init__(self):
        self.__patient_id = ""

    def set_patient_id(self, patient_id):
        self.__patient_id = patient_id

    def get_patient_id(self):
        print("Patient ID:", self.__patient_id)


obj = Patient()
obj.set_patient_id("P101")
obj.get_patient_id()