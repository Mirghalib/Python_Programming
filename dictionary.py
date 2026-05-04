students = {
    "student_01":{
        "name" : "Ghalib",
        "Age" : 20,
        "Semester" : "1st",
        "Score":{
            "Programming" : 88,
            "Information Security" : 78,
            "Data Stucture" : 99
        }
    }
}

obtain = students["student_01"]["Score"].values()
average = sum(obtain) / len(obtain)

if average <=100 and average >=90:
    Grade = 'A+'
elif average >=80:
    Grade = 'A'
elif average >=70:
    Grade = 'B'
elif average >=60:
    Grade = 'C'
elif average >=50:
    Grade = 'D'
else:
    Grade = 'F'

students["student_01"]["Average"] = average
students["student_01"]["Grade"] = Grade

print(students)