
# Letter A
print("Letter A")
for i in range(7):
    for j in range(7):
        if (i == 0 and j == 3) or \
           (i == 1 and (j == 2 or j == 4)) or \
           (i == 2 and (j == 1 or j == 5)) or \
           (i == 3 and j >= 1 and j <= 5) or \
           (i > 3 and (j == 1 or j == 5)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Letter B
print("\nLetter B")
for i in range(7):
    for j in range(5):
        if j == 0 or ((i == 0 or i == 3 or i == 6) and j < 4) or \
           (j == 4 and i != 0 and i != 3 and i != 6):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Letter C
print("\nLetter C")
for i in range(7):
    for j in range(5):
        if ((i == 0 or i == 6) and j > 0) or j == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Letter D
print("\nLetter D")
for i in range(7):
    for j in range(5):
        if j == 0 or ((i == 0 or i == 6) and j < 4) or \
           (j == 4 and i > 0 and i < 6):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Letter E
print("\nLetter E")
for i in range(7):
    for j in range(5):
        if i == 0 or i == 3 or i == 6 or j == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Letter F
print("\nLetter F")
for i in range(7):
    for j in range(5):
        if i == 0 or i == 3 or j == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Letter G
print("\nLetter G")
for i in range(7):
    for j in range(5):
        if (((i == 0 or i == 6) and j > 0) or j == 0 or
            (i == 3 and j >= 2) or (j == 4 and i >= 3)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Letter H
print("\nLetter H")
for i in range(7):
    for j in range(5):
        if j == 0 or j == 4 or i == 3:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Letter I
print("\nLetter I")
for i in range(7):
    for j in range(5):
        if i == 0 or i == 6 or j == 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Letter J
print("\nLetter J")
for i in range(7):
    for j in range(5):
        if i == 0 or j == 2 or (i == 6 and j < 3) or \
           (j == 0 and i >= 4):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Letter K
print("\nLetter K")
for i in range(7):
    for j in range(5):
        if j == 0 or i + j == 4 or i - j == 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Letter L
print("\nLetter L")
for i in range(7):
    for j in range(5):
        if j == 0 or i == 6:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Letter M
print("\nLetter M")
for i in range(7):
    for j in range(7):
        if j == 0 or j == 6 or \
           (i == j and i < 4) or (i + j == 6 and i < 4):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Letter N
print("\nLetter N")
for i in range(7):
    for j in range(7):
        if j == 0 or j == 6 or i == j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Letter O
print("\nLetter O")
for i in range(7):
    for j in range(5):
        if ((i == 0 or i == 6) and j > 0 and j < 4) or \
           ((j == 0 or j == 4) and i > 0 and i < 6):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Letter P
print("\nLetter P")
for i in range(7):
    for j in range(5):
        if j == 0 or ((i == 0 or i == 3) and j < 4) or \
           (j == 4 and i > 0 and i < 3):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Letter Q
print("\nLetter Q")
for i in range(7):
    for j in range(5):
        if (((i == 0 or i == 5) and j > 0 and j < 4) or
            ((j == 0 or j == 4) and i > 0 and i < 5) or
            (i == j and i >= 4)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Letter R
print("\nLetter R")
for i in range(7):
    for j in range(5):
        if j == 0 or ((i == 0 or i == 3) and j < 4) or \
           (j == 4 and i > 0 and i < 3) or (i - j == 1 and i > 3):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Letter S
print("\nLetter S")
for i in range(7):
    for j in range(5):
        if i == 0 or i == 3 or i == 6 or \
           (j == 0 and i < 3) or (j == 4 and i > 3):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Letter T
print("\nLetter T")
for i in range(7):
    for j in range(5):
        if i == 0 or j == 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Letter U
print("\nLetter U")
for i in range(7):
    for j in range(5):
        if ((j == 0 or j == 4) and i < 6) or \
           (i == 6 and j > 0 and j < 4):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Letter V
print("\nLetter V")
for i in range(7):
    for j in range(7):
        if ((j == 0 or j == 6) and i < 4) or \
           (i == 4 and (j == 1 or j == 5)) or \
           (i == 5 and (j == 2 or j == 4)) or \
           (i == 6 and j == 3):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Letter W
print("\nLetter W")
for i in range(7):
    for j in range(7):
        if j == 0 or j == 6 or \
           (i == 4 and (j == 1 or j == 5)) or \
           (i == 5 and (j == 2 or j == 4)) or \
           (i == 6 and j == 3):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Letter X
print("\nLetter X")
for i in range(7):
    for j in range(7):
        if i == j or i + j == 6:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Letter Y
print("\nLetter Y")
for i in range(7):
    for j in range(7):
        if (i == j and i < 4) or \
           (i + j == 6 and i < 4) or \
           (i >= 3 and j == 3):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Letter Z
print("\nLetter Z")
for i in range(7):
    for j in range(7):
        if i == 0 or i == 6 or i + j == 6:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
