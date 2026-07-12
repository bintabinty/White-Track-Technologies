num=[i * i for i in range(5)]
print(num)

evennos=[a for a in range(20) if a%2==0]
print(evennos)

oddnos=[a for a in range(20) if a%2!=0]
print(oddnos)

num1=["Even" if a&2==0 else "Odd" for a in range(20)]
print(num1)

num2=[a for a in range(20) if a%2==0 if a%3!=0]
print(num2)


num3=[a for a in range(20) if a%2==0 and a%3!=0]
print(num3)