for name in range(10):
    print("Hello binty")

#print 1 to 10
for i in range(11):
    print(i)

#to print even
for i in range(0,11,2):
   print(i)

#print 1 to 10
for i in range(1,11):
    print(i)

#3 multiply
for i in range(1,11):
    print("3 x", i, "=", i * 3)

#multiply of 2
for i in range(1, 11):
    print("2 x", i, "=", i * 2)

text=str(input("Enter text"))
count=0
for ch in text:
    if ch.lower() in "aeiou":
        count+=1
print("total vowels ",count)
    
