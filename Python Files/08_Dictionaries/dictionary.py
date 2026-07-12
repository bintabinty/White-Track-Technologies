# 1. Create a dictionary to store a student's name, age, and course
student = {
    "name": "Binty",
    "age": 22,
    "course": "BCom"
}


#Print all keys in a dictionary.
print(student.keys())

# 3. Print all values in a dictionary
print("\nValues:")
print(student.values())

# 4. Access the value of a specific key
print("\nCourse:")
print(student["course"])

# 5. Add a new key-value pair to a dictionary
student["city"] = "Kottayam"
print("\nAfter adding city:")
print(student)

# 7. Remove a key from a dictionary
student.pop("city")
print("\nAfter removing city:")
print(student)

# 8. Find the length of a dictionary
print("\nLength of dictionary:")
print(len(student))

# 9. Check if a key exists in a dictionary
if "name" in student:
    print("\nKey 'name' exists.")
else:
    print("\nKey 'name' does not exist.")


# 10. Clear all items from a dictionary
student.clear()
print("\nAfter clearing dictionary:")
print(student)