# Python Pattern Printing Questions - Set 2
# All 10 programs execute sequentially.

# 1. Binary Pattern
print("\n1. Binary Pattern")
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j % 2, end="")
    print()

# 2. Alphabet Pattern
print("\n2. Alphabet Pattern")
n = 5
for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    # The question paper explicitly shows ABCDA in the third row.
    if i == 3:
        print("ABCDA")
    else:
        for j in range(i):
            print(chr(65 + j), end="")
        for j in range(i - 2, -1, -1):
            print(chr(65 + j), end="")
        print()
# For the regular symmetric pattern, remove the special case above
# and use the two alphabet loops for every row (third row: ABCBA).

# 3. Number Palindrome Pattern (centered)
print("\n3. Number Palindrome Pattern")
n = 5
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(i, 0, -1):
        print(j, end="")
    for j in range(2, i + 1):
        print(j, end="")
    print()

# 4. Number Pattern
print("\n4. Number Pattern")
rows = 4
cols = 3
for i in range(1, rows + 1):
    for j in range(cols):
        print(i + j * rows, end="\t")
    print()

# 5. Right-Angled Number Triangle
print("\n5. Right-Angled Number Triangle")
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# 6. Inverted Number Triangle
print("\n6. Inverted Number Triangle")
n = 5
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# 7. Floyd's Triangle
print("\n7. Floyd's Triangle")
n = 5
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" " if i >= 4 else "")
        num += 1
    print()

# 8. Alphabet Triangle
print("\n8. Alphabet Triangle")
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end="")
    print()

# 9. Number Palindrome Triangle (left-aligned)
print("\n9. Number Palindrome Triangle")
n = 5
for i in range(1, n + 1):
    for j in range(i, 0, -1):
        print(j, end="")
    for j in range(2, i + 1):
        print(j, end="")
    print()

# 10. Continuous Alphabet Pattern
print("\n10. Continuous Alphabet Pattern")
n = 5
letter = 65  # ASCII value of A
for i in range(1, n + 1):
    for j in range(i):
        print(chr(letter), end="")
        letter += 1
    print()
