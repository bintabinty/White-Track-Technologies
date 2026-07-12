# Student Management System

from abc import ABC, abstractmethod

# Abstract Class
class StudentDetails(ABC):
    @abstractmethod
    def display(self):
        pass

# Child Class
class Student(StudentDetails):
    def __init__(self, student_id, name, m1, m2, m3):
        self.__student_id = student_id
        self.__name = name
        self.__mark1 = m1
        self.__mark2 = m2
        self.__mark3 = m3

    def get_id(self):
        return self.__student_id

    def calculate_total(self, m1, m2, m3):
        total = m1 + m2 + m3
        return total

    def calculate_average(self, total):
        average = total / 3
        return average

    def display_grade(self, average):
        if average >= 90:
            return "A"
        elif average >= 75:
            return "B"
        elif average >= 50:
            return "C"
        else:
            return "Fail"

    def display(self):
        total = self.calculate_total(self.__mark1, self.__mark2, self.__mark3)
        average = self.calculate_average(total)
        grade = self.display_grade(average)

        print("\nStudent ID :", self.__student_id)
        print("Name       :", self.__name)
        print("Total      :", total)
        print("Average    :", average)
        print("Grade      :", grade)


students = []

# Add Student
def add_student():
    sid = int(input("Enter Student ID: "))
    name = input("Enter Name: ")
    m1 = int(input("Enter Mark 1: "))
    m2 = int(input("Enter Mark 2: "))
    m3 = int(input("Enter Mark 3: "))

    obj = Student(sid, name, m1, m2, m3)
    students.append(obj)

    print("Student Added Successfully!")

# View All Students
def view_students():
    if len(students) == 0:
        print("No student records found.")
    else:
        for s in students:
            s.display()

# Search Student
def search_student():
    sid = int(input("Enter Student ID: "))

    found = False

    for s in students:
        if s.get_id() == sid:
            print("Student Found")
            s.display()
            found = True
            break

    if found == False:
        print("Student Not Found")

# Main Menu
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by ID")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Try Again.")