# PYTHON QUESTIONS SET 1 - PART A
# Run this file to execute all eight programs in order.

# 1. Factorial of a given number
print('\n1. Factorial')
n = int(input('Enter a number: '))
fact = 1
if n < 0:
    print('Factorial is not defined')
else:
    for i in range(1, n + 1):
        fact = fact * i
    print('Factorial =', fact)

# 2. Fibonacci series up to N terms
print('\n2. Fibonacci Series')
n = int(input('Enter number of terms: '))
a = 0
b = 1
for i in range(n):
    print(a, end=' ')
    c = a + b
    a = b
    b = c
print()

# 3. Armstrong number
print('\n3. Armstrong Number')
n = int(input('Enter a number: '))
temp = n
total = 0
power = len(str(n))
while temp > 0:
    digit = temp % 10
    total = total + digit ** power
    temp = temp // 10
if total == n:
    print('Armstrong Number')
else:
    print('Not an Armstrong Number')

# 4. Palindrome number
print('\n4. Palindrome Number')
n = int(input('Enter a number: '))
temp = n
reverse = 0
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10
if n == reverse:
    print('Palindrome Number')
else:
    print('Not a Palindrome Number')

# 5. Prime number
print('\n5. Prime Number')
n = int(input('Enter a number: '))
if n <= 1:
    print('Not a Prime Number')
else:
    for i in range(2, n):
        if n % i == 0:
            print('Not a Prime Number')
            break
    else:
        print('Prime Number')

# 6. Second largest number without sorting
print('\n6. Second Largest Number')
numbers = [10, 25, 40, 15, 30]
largest = max(numbers)
second = None
for i in numbers:
    if i != largest:
        if second is None or i > second:
            second = i
print('List:', numbers)
print('Largest Number:', largest)
print('Second Largest Number:', second)

# 7. Second smallest number
print('\n7. Second Smallest Number')
numbers = [10, 25, 40, 15, 30]
smallest = min(numbers)
second = None
for i in numbers:
    if i != smallest:
        if second is None or i < second:
            second = i
print('List:', numbers)
print('Smallest Number:', smallest)
print('Second Smallest Number:', second)

# 8. Move all zeros to the end of a list
print('\n8. Move Zeros to the End')
numbers = [0, 1, 0, 3, 12, 0, 5]
result = []
count = 0
for i in numbers:
    if i != 0:
        result.append(i)
    else:
        count = count + 1
for i in range(count):
    result.append(0)
print('Original List:', numbers)
print('Updated List:', result)
