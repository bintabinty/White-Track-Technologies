num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
try:
    result=num1/num2
    print("result: ",result)
except ZeroDivisionError:
    print("ERROR: Division by zero is not allowed")
finally:
    print("Program completed")
try:
    age=int(input("Enter your age: "))
except ValueError:
    print("inalid input")
finally:
    print("program completed")

try:
    numbers = [10, 20, 30, 40, 50]   # Indexes: 0, 1, 2, 3, 4

    index = int(input("Enter the index (0-4): "))
    print("Element =", numbers[index])

except IndexError:
    print("Error: Index out of range! Please enter an index between 0 and 4.")

except ValueError:
    print("Error: Please enter a valid integer.")

finally:
    print("Program completed.")

