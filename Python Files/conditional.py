#Largest of 3 numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if (a>=b) and (a >= c):
   print("The largest number is", a)
elif (b >= a) and (b >= c):
    print("The largest number is", b)
else:
    print("The largest number is", c)

#Vote Eligiblity check

age=int(input("Enter your age"))
if age >= 18:
        print("Eligible for voting")
else:
        print("Not eligible for voting")

#check if a number is positive or negative

num=int(input("Enter a number"))
if num > 0:
     print("The number is positive")
else:
     print("The number is negative")

#to check if ayear is leap year or nor

year=int(input("Enter a year"))
if year % 4 ==0:
     print(year," is leap year")
else:
     print(year," is not leap year")

#calculator using operators and conditional statements

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