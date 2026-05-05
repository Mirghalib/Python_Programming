# students = {
#     "student_01":{
#         "name" : "Ghalib",
#         "Age" : 20,
#         "Semester" : "1st",
#         "Score":{
#             "Programming" : 88,
#             "Information Security" : 78,
#             "Data Stucture" : 99
#         }
#     },
#     "student_02":{
#         "name" : "Qamar",
#         "Age" : 22,
#         "Semester" : "1st",
#         "Score":{
#             "Programming" : 38,
#             "Information Security" : 18,
#             "Data Stucture" : 39
#         }
#     }
# }

# obtain = students["student_01"]["Score"].values()
# average = sum(obtain) / len(obtain)


# obtain_2 = students["student_02"]["Score"].values()
# average_2 = sum(obtain_2) / len(obtain_2)

# if average or average_2 <=100 and average or average_2 >=90:
#     Grade = 'A+'
# elif average or average_2 >=80:
#     Grade = 'A'
# elif average or average_2 >=70:
#     Grade = 'B'
# elif average or average_2 >=60:
#     Grade = 'C'
# elif average or average_2 >=50:
#     Grade = 'D'
# else:
#     Grade = 'F'

# students["student_01"]["Average"] = average
# students["student_01"]["Grade"] = Grade

# students["student_02"]["Average"] = average_2
# students["student_02"]["Grade"] = Grade

# print(students)
# print(students["student_01"])
# print(students["student_02"])



# students = {
#     "student_01": {
#         "name": "Ghalib",
#         "Age": 20,
#         "Semester": "1st",
#         "Score": {
#             "Programming": 88,
#             "Information Security": 78,
#             "Data Structure": 99
#         }
#     },
#     "student_02": {
#         "name": "Qamar",
#         "Age": 22,
#         "Semester": "1st",
#         "Score": {
#             "Programming": 38,
#             "Information Security": 18,
#             "Data Structure": 39
#         }
#     }
# }

# # Loop through each student
# for student_id, data in students.items():
    
#     scores = data["Score"].values()
#     average = sum(scores) / len(scores)
    
#     # Assign grade correctly
#     if 90 <= average <= 100:
#         grade = 'A+'
#     elif average >= 80:
#         grade = 'A'
#     elif average >= 70:
#         grade = 'B'
#     elif average >= 60:
#         grade = 'C'
#     elif average >= 50:
#         grade = 'D'
#     else:
#         grade = 'F'
    
#     # Store results
#     data["Average"] = round(average, 2)
#     data["Grade"] = grade

# print(students)