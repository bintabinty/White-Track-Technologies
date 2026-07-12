#square for n 
n=5
for row in range(n):
    for col in range(n):
        print("*",end=" ")
    print()

#ight-angled triangle pattern using stars
n1 = 5

for i in range(1, n1 + 1):
    for j in range(i):
        print("*", end="")
    print()

#Print an Inverted Right-Angled Triangle Pattern
n2 = 5

for i in range(n2, 0, -1):
    for j in range(i):
        print("*", end="")
    print()


#Print a Number Triangle Pattern
n4 = 5

for i in range(1, n4 + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

#Print Floyd's Triangle
n5 = 4
num = 1

for i in range(1, n5 + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

#Print Same Number Repeated in Each Row
n6 = 5

for i in range(1, n6 + 1):
    for j in range(i):
        print(i, end="")
    print()

#9. Print an Alphabet Triangle Pattern
n7 = 5

for i in range(1, n7 + 1):
    for j in range(i):
        print(chr(65 + j), end="")
    print()
#pyramid
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)