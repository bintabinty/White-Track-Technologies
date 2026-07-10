#Write a function to return the product of all elements in a list.
def product_of_list(lst):
    product=1
    for i in lst:
        product=product*i
    return product
num_lst=[2,3,6]
print(product_of_list(num_lst))

#Write a function to return the largest digit in a number.
def largest_digit(num):
    largest=0
    while num>0:
        digit=num%10
        if digit>largest:
            largest=digit
        num=num//10

    return largest
print(largest_digit(58329))

#Write a function to return the smallest digit in a number.
def smallest_digit(num):
    smallest=0
    while num>0:
        digit=num%10
        if digit < smallest:
            smallest=digit
        num=num//10

    return smallest
print(smallest_digit(58329))

#Write a function to return the number of uppercase letters in a string
def count_uppercase(text):
    count = 0
    for char in text:
        if char.isupper():
            count+=1

    return count
print(count_uppercase("Hello WORLD"))

#Write a function to return the number of lowercase letters in a string.
def count_lowercase(text):
    count = 0
    for char in text:
        if char.islower():
            count+=1

    return count
print(count_lowercase("Hello WORLD"))

#Write a function to return the count of positive numbers in a list.
def count_positive(num1):
    count=0
    for i in num1:
        if i > 0:
            count+=1
    return count
positive_lst=[56,-9,-5,27,8,13]
print(count_positive(positive_lst))

#Write a function to return the count of negative numbers in a list.
def count_negative(num2):
    count=0
    for i in num2:
        if i < 0:
            count+=1
    return count
negative_lst=[56,-9,-5,27,8,13,-7,-1]
print(count_negative(negative_lst))

#Write a function to return the sum of all even numbers from 1 to N.
def sum_even(num3):
    total=0
    for i in range(1,num3+1):
        if i%2==0:
            total+=i
    return total
print(sum_even(10))

#Write a function to return the sum of all odd numbers from 1 to N.
def sum_odd(num4):
    total=0
    for i in range(1,num4+1):
        if i%2!=0:
            total+=i
    return total
print(sum_odd(10))

#Write a function to return a list without duplicate elements.
def remove_duplicates(num4):
    unique = []
    for i in num4:
        if i not in unique:
            unique.append(i)
    return unique
temp_list=[2,2,3,4,5,5,5,6,7,8,8,9,10]
print(remove_duplicates(temp_list))

#Function to return the Fibonacci series up to N terms
def fibonacci(num5):
    a = 0
    b = 1
    for i in range(num5):
        print(a,end=" ")
        c=a+b
        a=b
        b=c
print(fibonacci(10))

#Write a function to return all factors of a number.
def find_factors(num6):
    factors = []
    for i in range(1,num6+1):
        if num6%i==0:
         factors.append(i)
    return factors
print(find_factors(12))






