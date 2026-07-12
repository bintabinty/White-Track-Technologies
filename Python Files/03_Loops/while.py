n=1
while n<=10:
    print(n)
    n+=1

#FACTORIAL
num=6
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)

#fibonnoci
n=10
a=0
b=1
for i in range(n):
    print(a, end=" ")
    c=a+b
    a=b
    b=c


num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if original == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")