#Create a list containing numbers from 1 to 20.
num=[a for a in range(1,21)]
print(num)

#Create a list of squares from 1 to 10.
num1=[a * a for a in range(1,11)]
print(num1)

#Create a list of cubes from 1 to 10.
num2=[a * a * a for a in range(1,11)]
print(num2)


#Create a list of even numbers between 1 and 50.
num3=[a for a in range(1,51) if a%2==0]
print(num3)

#Create a list of odd numbers between 1 and 50.
num4=[a for a in range(1,51) if a%2!=0]
print(num4)

#Create a list containing numbers divisible by 5 from 1 to 100.
num5=[a for a in range(1,51) if a%5==0]
print(num5)

#Create a list containing numbers divisible by 3 and 7 from 1 to 100.
num6=[a for a in range(1,101) if a%3==0 and a%7==0]
print(num6)

#Create a list of multiples of 8 less than 100.
num7=[a for a in range(100) if a%8==0]
print(num7)

#Create a list containing the first 20 natural numbers.
num8=[a for a in range(1,21)]
print(num8)

#Create a list containing negative numbers from -1 to -20.
num9=[a for a in range(-1,-21,-1)]
print(num9)





