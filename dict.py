subjects = ["Math", "English", "Computer"]
marks = (85, 90, 95)
student = {
    "name": "Asad",
    "age": 20,
    "subjects": subjects,
    "marks": marks
}

print("Student Name:", student["name"])
print("Age:", student["age"])
print("Subjects:", student["subjects"])
print("Marks:", student["marks"])

print("First Subject:", student["subjects"][0])
print("First Mark:", student["marks"][0])