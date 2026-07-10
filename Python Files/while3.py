#amstrong number

num=153
original=num
sum=0
while(num>0):
    digit = num % 10
    sum= sum+(digit**3)
    num //= 10

if original == sum:
    print("Amstrong  Number")
else:
    print("Not a Amstrong Number")

    