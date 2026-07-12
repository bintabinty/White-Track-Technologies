# 1. Write a program to perform all arithmetic operations on two numbers.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Modulus:", num1 % num2)

# 2. Check whether a number is odd or even using operators.

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# 3. Calculate simple interest using principal, rate, and time.

p = float(input("Enter principal amount: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

si = (p * r * t) / 100

print("Simple Interest =", si)

# 4. Check whether a person is eligible to vote based on age.

age = int(input("Enter age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")

# 5. Increase an employee’s salary by 10% using assignment operators.

salary = float(input("Enter salary: "))
salary += salary * 0.10
print("Updated Salary =", salary)

# 6. Check if a student passed all subjects using logical operators.

m1 = int(input("Enter mark1: "))
m2 = int(input("Enter mark2: "))
m3 = int(input("Enter mark3: "))

if m1 >= 40 and m2 >= 40 and m3 >= 40:
    print("Passed all subjects")
else:
    print("Failed")

# 7. Find the largest among three numbers using comparison operators.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("Largest =", a)
elif b > c:
    print("Largest =", b)
else:
    print("Largest =", c)


# 8. Create an ATM withdrawal system and update balance after withdrawal.

balance = 10000
withdraw = float(input("Enter withdrawal amount: "))

if withdraw <= balance:
    balance -= withdraw
    print("Withdrawal successful")
    print("Remaining Balance =", balance)
else:
    print("Insufficient balance")

# 9. Check whether a username exists in a list using membership operators.
users = ["binty", "rahul", "anu"]
name = input("Enter username: ")
if name in users:
    print("Username exists")
else:
    print("Username not found")

# 10. Calculate BMI and determine the health category.
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height ** 2)

print("BMI =", bmi)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")

# 11. Create an electricity bill calculator based on units consumed.

units = int(input("Enter units consumed: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = units * 7
else:
    bill = units * 10

print("Electricity Bill =", bill)

# 12. Check loan eligibility using age, salary, and employment status.

age = int(input("Enter age: "))
salary = float(input("Enter salary: "))
job = input("Are you employed? (yes/no): ")

if age >= 21 and salary >= 25000 and job == "yes":
    print("Eligible for loan")
else:
    print("Not eligible")

# 13. Compare two strings and determine whether they are equal.

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if str1 == str2:
    print("Strings are equal")
else:
    print("Strings are not equal")

# 14. Check whether a character exists in a given string.

text = input("Enter a string: ")
char = input("Enter a character: ")

if char in text:
    print("Character exists")
else:
    print("Character not found")

# 15. Compare two lists using == and is operators.

list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(list1 == list2)   # Checks values
print(list1 is list2)   # Checks memory location


# 16. Calculate shopping discount based on purchase amount.

amount = float(input("Enter purchase amount: "))

if amount >= 5000:
    discount = amount * 0.20
elif amount >= 2000:
    discount = amount * 0.10
else:
    discount = 0

final_amount = amount - discount

print("Discount =", discount)
print("Final Amount =", final_amount)

# 17. Perform bitwise operations (&, |, ^, <<, >>) on two numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("AND =", a & b)
print("OR =", a | b)
print("XOR =", a ^ b)
print("Left Shift =", a << 1)
print("Right Shift =", a >> 1)

# 18. Update mobile balance after recharge using assignment operators.

balance = 100

recharge = int(input("Enter recharge amount: "))

balance += recharge

print("Updated Balance =", balance)

# 19. Check employee bonus eligibility using experience and salary conditions.

experience = int(input("Enter years of experience: "))
salary = float(input("Enter salary: "))

if experience >= 5 and salary < 50000:
    print("Eligible for bonus")
else:
    print("Not eligible")


# 20. Build a mini calculator to perform arithmetic operations based on user input.

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print("Result =", num1 + num2)
elif operator == "-":
    print("Result =", num1 - num2)
elif operator == "*":
    print("Result =", num1 * num2)
elif operator == "/":
    print("Result =", num1 / num2)
else:
    print("Invalid operator")