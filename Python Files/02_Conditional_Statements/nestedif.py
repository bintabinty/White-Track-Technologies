name=str(input("Enter students name: "))
marks = int(input("Enter marks: "))

if marks >= 40:          
    print("Result: Pass")

    if marks >= 90:
        print("Grade: A+")
    elif marks >= 80:
        print("Grade: A")
    elif marks >= 70:
        print("Grade: B")
    elif marks >= 60:
        print("Grade: C")
    else:
        print("Grade: D")

else:
    print("Result: Fail")
    print("Grade: F")

#check vowels in user input


#multiply of 7 & 5
num=int(input("Enter a number: "))
if(num%7==0):
    print(num,"is multiply of 7")
else:
    print(num,"not multiply of 7")


num1=int(input("Enter a number: "))
if(num1%5==0):
    print(num1,"is multiply of 5")
else:
    print(num1,"not multiply of 5")