#Write a function to return the square of a number.
def square(n):
    return n*n
num=square(3)
print(num)
#Write a function to return the cube of a number
def cube(n1):
    return n1*n1*n1
num1=cube(3)
print(num1)

#Write a function to return the sum of digits of a number.
def sum_of_digit(n2):
    sum=0
    while n2>0:
        digit=n2%10
        sum=sum+digit
        n2=n2//10
    return sum
result=sum_of_digit(636)
print(result)

# Function to return the smallest number in a list
def smallest_number(numbers):
    smallest = numbers[0]

    for i in numbers:
        if i < smallest:
            smallest = i

    return smallest

print(smallest_number([10, 5, 20, 3, 15]))

# Write a function to return the multiplication table of a number as a list.
def multiply(n3):
    table = []

    for i in range(1, 11):
        table.append(n3 * i)
    return table
print(multiply(5))

#Write a function to return all even numbers from a list
def even_numbers(n4):
     even=[]
     
     for i in n4:
         if i%2==0:
             even.append(i)
     return even
print(even_numbers([10, 15, 20, 25, 30]))
         

# Function to return the average of numbers in a list
def average(n5):
    total = 0

    for i in n5:
        total += i
    return total / len(n5)
print(average([10, 20, 30, 40, 50]))
