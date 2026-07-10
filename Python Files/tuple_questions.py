#1. Create a tuple of 5 student names and print all the names using a loop.
students = ("Anu", "Rahul", "Meera", "Akhil", "Neha")
for name in students:
    print(name)

#2. Create a tuple of numbers and find the total sum of all elements.
numbers = (10, 20, 30, 40, 50)
total = 0
for i in numbers:
    total = total + i
print("Total Sum =", total)

#3. Create a tuple of 10 numbers and find the largest number without using max().
numbers = (12, 45, 67, 23, 89, 34, 10, 99, 56, 78)
largest = numbers[0]
for i in numbers:
    if i > largest:
        largest = i
print("Largest Number =", largest)

#4. Create a tuple of 10 numbers and find the smallest number without using min().
numbers = (12, 45, 67, 23, 89, 34, 10, 99, 56, 78)
smallest = numbers[0]
for i in numbers:
    if i < smallest:
        smallest = i
print("Smallest Number =", smallest)

#5. Create a tuple of fruits and count how many times a specific fruit appears in the tuple.
fruits = ("Apple", "Orange", "Mango", "Apple", "Grapes", "Apple")
fruit = input("Enter fruit name: ")
count = 0
for i in fruits:
    if i == fruit:
        count = count + 1
print(fruit, "appears", count, "times")
#6. Take a value from the user and check whether it exists in a tuple.
numbers = (10, 20, 30, 40, 50)
value = int(input("Enter a number: "))
if value in numbers:
    print("Value exists in the tuple")
else:
    print("Value does not exist")

#7. Create a tuple of marks and calculate the average mark of all students.
marks = (85, 90, 78, 88, 92)
total = 0
for i in marks:
    total = total + i
average = total / len(marks)
print("Average Mark =", average)

#8. Create a tuple of city names and print the cities in reverse order.
cities = ("Delhi", "Mumbai", "Kochi", "Chennai", "Bangalore")
for i in cities[::-1]:
    print(i)
#9. Create two tuples and combine them into a single tuple.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = tuple1 + tuple2
print("Combined Tuple =", result)

#10. Create a tuple of numbers and count the number of even and odd elements present in it.
numbers = (10, 15, 20, 25, 30, 35, 40, 45)
even = 0
odd = 0
for i in numbers:
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print("Even Numbers =", even)
print("Odd Numbers =", odd)