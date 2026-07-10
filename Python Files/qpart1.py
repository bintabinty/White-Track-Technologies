#Write a program to add two numbers.
a=10
b=20
sum=a+b
print("sum is ",sum)

#Find the sum, difference, product, and quotient of two numbers.
a1=5
b1=3
print("sum =",a+b)
print("diffrence= ",a-b)
print("product= ",a*b)
print("qutient= ",a/b)

#Check whether a number is even or odd using operators.
a2=56
if a2%2==0:
    print("Even")
else:
    print("odd")

#Find the largest of two numbers using comparison operators.
a3=78
b3=91
if a3>=b3:
    print("the largest is ",a3)
else:
    print("largest is  ",b3)

 #Swap two numbers without using a temporary variable.
n1=67
n2=56
n1,n2=n2,n1

print(n2)
print(n1)

#Find the remainder when one number is divided by another.
a4=13
b4=10
c=a4%b4
print("remainder= ",c)

#Check whether a number is divisible by both 3 and 5.
n3=int(input("enter a number"))
if n3%3==0 and n3%5==0:
    print("divisible by 3 and 5")
else:
    print("not divisble")

#Calculate the square and cube of a number.
n4=int(input("enter a number"))
print("square = ",n4*n4)
print("cube = ",n4*n4*n4)

#Check whether two numbers are equal
n5=int(input("enter first number"))
n6=int(input("enter second number"))
if n5==n6:
    print("equal")
else:
    print("not equal")

#Find the average of three numbers.
n7=int(input("enter 1st number"))
n8=int(input("enter 2nd number"))
n9=int(input("enter 3rd number"))
total=n7+n8+n9
avg=total/3
print("average is ",avg)