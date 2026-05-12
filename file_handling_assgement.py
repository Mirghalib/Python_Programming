# print("Task 01")
# with open("students.txt","a") as f:
#     for x in range(5):
#         names = input("Enter Name : ")
#         f.write(names + "\n")
# print("Data COmplete Successfully!")
# f.close()


# # print("Task 02")
# count = 0
# with open("students.txt","r") as f:
#     for line in f:
#         names = line.strip()
#         print(names)
#         count +=1
#     print(f"There are {count} names in students.txt")



# # print("Task 03")
# with open("students.txt","a") as f:
#     for x in range(2):
#         names = input("Enter Name : ")
#         f.write(names + "\n")
# print("Data COmplete Successfully!")



# task 4
# Number_list = []
# with open("numbers.txt","a") as f:
#     for x in range(5):
#         numbers = int(input("Enter Number : "))
#         f.write(str(numbers)+",")
#         Number_list.append(numbers)
#     obtain = sum( Number_list)
#     average = obtain / len( Number_list)
#     print(f"Your obtain marks is  {obtain} and your Average is {average}")







# with open("stud.txt","a") as f:
#     for x in range(5):
#         names = input("Enter Name : ")
#         f.write(names + "\n")
#print("Complete Data Successfully!")




# # task 5
# with open("students.txt","r") as f:
#     names = f.read()
#     print(names)
# with open("students_backup.txt","w") as f:
#     f.write(names)
# print("data has been backed up successfully.")


# # task 6
# with open("story.txt","r") as f:
#     file = f.read()



with open("Numbers.txt","w") as file:
    list_numbers = []
    for x in range(5):
        numbers = input("Enter a Number : ")
        file.write(numbers+",")
        list_numbers.append(numbers)

with open("Numbers.txt","r") as file:
    print(file.read(numbers))
