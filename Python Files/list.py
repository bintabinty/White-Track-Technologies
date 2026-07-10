#Create a list of 5 student names and print each name using a loop.
name=['Anu','Allen','Nitha','Neena','Divya']
for i in name:
    print(i)

#Create a list of 5 numbers and find the sum of all elements.
num=[20,30,60,10,40]
sum=0
for i in num:
    sum+=i
print("sum= ",sum)

#Create a list of fruits and print the total number of fruits in the list.
# Create a list of fruits and print the total number of fruits in the list

fruit = ['Apple', 'Grapes', 'Orange', 'Pineapple', 'Pear']
count = 0
for i in fruit:
    count += 1
print("Total number of fruits:", count)

#Take a number from the user and check whether it exists in a list of numbers.
n=int(input("Enter anumber "))
numbers=[45,89,90,23,36]
if n in numbers:
    print("Number exists")
else:
    print("not exists")

#Create a list of colors and add a new color entered by the user. Print the updated list.
colors=['yellow','blue','green','white']
new_color = input("Enter a color: ")
colors.append(new_color)
print("Updated list:", colors)
    
#Create a list of subjects and remove a subject entered by the user. Print the updated list.
subjects = ['Maths', 'Science', 'English', 'History', 'Computer']
sub = input("Enter a subject to remove: ")
if sub in subjects:
    subjects.remove(sub)
    print("Updated list:", subjects)
else:
    print("Subject not found")

#Create a list of numbers and find the largest number without using max().
numbers = [45, 12, 78, 23, 90, 56]
largest = numbers[0]
for i in numbers:
    if i > largest:
        largest = i
print("Largest number:", largest)

#Create a list of numbers and count how many even and odd numbers are present.
num_list = [10, 15, 22, 33, 40, 57, 68]
even_count = 0
odd_count = 0
for i in num_list:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)

#Create a list of city names and print the list in reverse order without using reverse().
cities = ['Delhi', 'Mumbai', 'Chennai', 'Kochi', 'Bangalore']
for i in range(len(cities)-1, -1, -1):
    print(cities[i])

#Create a list of marks and calculate the average mark of all students.
marks=[85,92,76,6,75]
total=0
mark_count=0
for i in marks:
    tota+=i
    mark_count+=1
average=total/mark_count
print("Average mark:", average)


