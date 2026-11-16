# PYTHON QUESTIONS SET 1 - PART B
# Basic Python Pattern Programming
# All ten programs run sequentially.

# 1. Right-Angled Triangle
print('\n1. Right-Angled Triangle')
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print('*', end='')
    print()

# 2. Inverted Right-Angled Triangle
print('\n2. Inverted Right-Angled Triangle')
n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print('*', end='')
    print()

# 3. Square Pattern
print('\n3. Square Pattern')
n = 5
for i in range(n):
    for j in range(n):
        print('*', end='')
    print()

# 4. Left-Sided Triangle
print('\n4. Left-Sided Triangle')
n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print()

# 5. Inverted Left-Sided Triangle
print('\n5. Inverted Left-Sided Triangle')
n = 5
for i in range(n, 0, -1):
    for j in range(n - i):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print()

# 6. Pyramid Pattern
print('\n6. Pyramid Pattern')
n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(' ', end='')
    for j in range(2 * i - 1):
        print('*', end='')
    print()

# 7. Inverted Pyramid
print('\n7. Inverted Pyramid')
n = 5
for i in range(n, 0, -1):
    for j in range(n - i):
        print(' ', end='')
    for j in range(2 * i - 1):
        print('*', end='')
    print()

# 8. Diamond Pattern (7 rows, as in the question paper)
print('\n8. Diamond Pattern')
n = 4
# Upper pyramid
for i in range(1, n + 1):
    for j in range(n - i):
        print(' ', end='')
    for j in range(2 * i - 1):
        print('*', end='')
    print()
# Lower inverted pyramid
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(' ', end='')
    for j in range(2 * i - 1):
        print('*', end='')
    print()

# 9. Hollow Square
print('\n9. Hollow Square')
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print(' * ', end=" ")
        else:
            print('  ', end="  ")
    print()

# 10. Hollow Right Triangle
print('\n10. Hollow Right Triangle')
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print('*', end='')
        else:
            print(' ', end='')
    print()
