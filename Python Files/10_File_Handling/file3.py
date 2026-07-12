import os

with open("student.txt", "w") as file:
    file.write("Register Number : 121\n")
    file.write("Student Name    : Binty\n")
    file.write("Department      : MCA\n")
    file.write("Year            : 1\n")

print("Student record added successfully.")


# ---------- READ ----------
with open("student.txt", "r") as file:
    print("\nStudent Details")
    print(file.read())

# ---------- UPDATE ----------
with open("student.txt", "r") as file:
    data = file.read()

updated_data = data.replace("MCA", "AI & ML")

with open("student.txt", "w") as file:
    file.write(updated_data)

print("\nDepartment Updated Successfully.")

# ---------- READ AFTER UPDATE ----------
with open("student.txt", "r") as file:
    print(file.read())

# ---------- DELETE FILE ----------
os.remove("student.txt")
print("\nFile Deleted Successfully.")

