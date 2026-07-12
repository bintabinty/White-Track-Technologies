#Print numbers from 10 to 1.

num=10
for i in range(1,num+1):
    print(num)
    num-=1

#Print odd numbers from 1 to 50.
print("Odd numbers between 1 and 50")
for i in range(1,50,2):
    print(i)

#Find the sum of numbers from 1 to 100.
num =100
sum=0
for i in range(1,num+1):
    sum+=i
print("sum of numbers from 1 to 100 ",sum)

#Print the multiplication table of any number entered by the user.

num1=int(input("Enter any number "))
for i in range(1,11):
   print(num1, "x", i, "=", num1 * i)

# Count digits in a number

num = int(input("Enter a number: "))

count = 0

while num > 0:
    num = num // 10
    count += 1

print("Number of digits =", count)