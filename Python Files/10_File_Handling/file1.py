import os
print("========== FILE WRITE ==========")

file = open("student.txt", "w")
file.write("Name : Sreerag\n")
file.write("Name : Binty\n")
file.write("Name : Terrance\n")
file.close()

print("========== FILE READ ==========")

file = open("student.txt", "r")
print(file.readline())
print(file.read())
print("File read succesfully")
file.close()

print("========== FILE UPDATE ==========")

file = open("student.txt", "r")
newfile = file.read()
file.close()

updateddata=newfile.replace("Binty","Jees")
file=open("student.txt","w")
file.write(updateddata)
print("File updated succesfully")
file.close()

print("\n========== FILE RENAME ==========")
os.rename("student.txt","students.txt")
print("file renamed succesfully")

print("=========FILE REMOVE=======")
os.remove("students.txt")
print("file deleted succesfully")


