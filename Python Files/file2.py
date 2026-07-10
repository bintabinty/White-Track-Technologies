import os
file=open("student.txt","w")
file.write("Register Number : 101\n")
file.write("Student Name    : Binty\n")
file.write("Department      : MCA\n")
file.write("Year            : 1\n")

file.write("Register Number : 102\n")
file.write("Student Name    : Anu\n")
file.write("Department      : IT\n")
file.write("Year            : 1\n")
file.close()

print("File created succesfully")

# ---------- READ ----------
file = open("student.txt", "r")
print("\nStudent Details")
print(file.read())
file.close()

# ---------- UPDATE ----------
file = open("student.txt", "r")
data = file.read()
file.close()

updated_data = data.replace("MCA", "AI & ML")

file = open("student.txt", "w")
file.write(updated_data)
file.close()

print("\nDepartment Updated Successfully.")

# ---------- READ AFTER UPDATE ----------
file = open("student.txt", "r")
print(file.read())
file.close()

# Delete Student
os.remove("student.txt")
print("\nFile Deleted Successfully.")


