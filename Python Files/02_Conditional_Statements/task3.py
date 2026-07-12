#1.Leap year

year = int(input("Enter year: "))

if year % 400 == 0:
    print("Leap Year")
else:
    print("Not Leap Year")

  #2. Largest among 4 numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a >= b and a >= c and a >= d:
    print("Largest =", a)
elif b >= c and b >= d:
    print("Largest =", b)
elif c >= d:
    print("Largest =", c)
else:
    print("Largest =", d)  

#3. Check uppercase / lowercase / digit / special character

ch = input("Enter a character: ")

if ch >= 'A' and ch <= 'Z':
    print("Uppercase")
elif ch >= 'a' and ch <= 'z':
    print("Lowercase")
elif ch >= '0' and ch <= '9':
    print("Digit")
else:
    print("Special Character")

#4. Electricity bill

units = int(input("Enter units: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

print("Bill =", bill)

#5. Triangle check + type
a = int(input("Enter side1: "))
b = int(input("Enter side2: "))
c = int(input("Enter side3: "))

if a + b > c and a + c > b and b + c > a:

    if a == b and b == c:
        print("Equilateral Triangle")

    elif a == b or b == c or a == c:
        print("Isosceles Triangle")

    else:
        print("Scalene Triangle")

else:
    print("Not a Triangle")

#6. Marks of 5 subjects + grade
m1 = int(input("Enter mark1: "))
m2 = int(input("Enter mark2: "))
m3 = int(input("Enter mark3: "))
m4 = int(input("Enter mark4: "))
m5 = int(input("Enter mark5: "))

total = m1 + m2 + m3 + m4 + m5
avg = total / 5

if m1 < 50 or m2 < 50 or m3 < 50 or m4 < 50 or m5 < 50:
    print("Fail")

elif avg > 90:
    print("Grade A")

elif avg >= 75:
    print("Grade B")

elif avg >= 50:
    print("Grade C")

else:
    print("Fail")

#7. Positive even / odd / negative / zero
num = int(input("Enter number: "))

if num == 0:
    print("Zero")

elif num > 0:

    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")

else:

    if num % 2 == 0:
        print("Negative Even")
    else:
        print("Negative Odd")

#.Login system

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":

    if password == "1234":
        print("Login Successful")

    else:
        print("Incorrect Password")

else:
    print("User Not Found")

#9. Voting / driving / senior citizen

age = int(input("Enter age: "))

if age >= 18:
    print("Eligible for voting")
else:
    print("Not eligible for voting")

if age >= 18:
    print("Eligible for driving license")
else:
    print("Not eligible for driving license")

if age >= 60:
    print("Eligible for senior citizen discount")
else:
    print("Not eligible for senior citizen discount")

#10. Mini ATM system

pin = int(input("Enter PIN: "))

balance = 5000

if pin == 1234:

    print("PIN Correct")

    amount = int(input("Enter withdrawal amount: "))

    if amount <= balance:
        balance = balance - amount
        print("Withdrawal successful")
        print("Balance =", balance)

    else:
        print("Insufficient Balance")

else:
    print("Wrong PIN")




