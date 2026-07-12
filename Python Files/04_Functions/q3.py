#Write a function to return the factorial of a given number.
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
num=factorial(5)  
print(num)

#4. Write a function to return the reverse of a string
def reverse_string(text):
    return text[::-1]
word ="Hello world"
print(reverse_string(word))

#5.
def count_vowels(text1):
    count = 0
    vowels = "aeiouAEIOU"
    for i in text1:
        if i in vowels:
            count += 1
    return count

word1 ="THere"
print( count_vowels(word1))

#6. Write a function to return the sum of all elements in a list.
def sum_list(lst):
    total = 0
    for i in lst:
        total = total + i
    return total
my_list = [10, 20, 30, 40, 50]
print( sum_list(my_list))

#Write a function to return True if a number is prime, otherwise False
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(is_prime(13))

# 9. Function to return the grade based on marks
def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"
print(grade(82))

#10
def word_count(sentence):
    count = 1
    for char in sentence:
        if char == " ":
            count += 1
    return count
print(word_count("Python is easy to learn"))