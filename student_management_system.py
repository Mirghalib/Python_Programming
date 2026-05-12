import os
while True:
    print("="*20+"Login","="*20)
    username = input("Username : ").strip()
    password = input("Password : ")
    if username == "admin" and password == "123456":
        print("Login Successfully!")
        break
    else:
        print("invalid username or password ")

print("="*20+"Admin Panel"+"*"*20)


while True:
    print("Press 1 : view data ")
    print("Press 2 : add data ")
    print("Press 3 : remove data ")
    print("Press 4 : update data ")
    print("Press 0 : exit data ")

    choice = int(input("Choice : "))
    match choice:
        case 0:
            break
        case 1:
            print("View all record ")
            try:
                with open("list_students.txt","r") as file:
                    count = 1
                    for record in file:
                        record = record.strip().split("||")
                        print("="*10,count,"="*10)
                        print("Name :"+record[0])
                        print("Age :"+record[1])
                        print("Eamil :"+record[2])
                        count+=1
            except FileNotFoundError:
                with open("list_students.txt","x") as file:
                    print("file created ")
            except Exception as e:
                print(e)
            input()
        case 2:
            print("Add record ")
            with open("list_students.txt","a") as file:
                name = input("Name : ").strip()
                email = input("Email : ").strip()
                age = input("Age : ").strip()
                file.write(f"{name}||{email}||{age}\n")
                print("added")
                input()
        case 3 :
            print("Remove record ")
            email = input("email : ")
            is_found = False
            with open("list_students.txt","r") as file:
                students_list = file.readlines()
                for student in  students_list:
                    record = student.strip().split("||")
                    if record[1] == email.strip():
                        students_list.remove(student)
                        print("record found ")
                        is_found = True
                        break
                if is_found:
                    with open("list_students.txt","w") as file:
                        file.writelines(students_list)
                        print("Record delete successfully")
                else:
                    print("Record is not found")

            input()
        case 4:
            # print("Update record ")
            # email = input("email : ")
            # is_found = False
            # with open("list_students.txt","r") as file:
            #     students_list = file.readlines()
            #     for student in  students_list:
            #         record = student.strip().split()
            #         if record[1] == email.strip():
            #             name = input("Enter Name : ")
            #             age = input("Enter age : ")
            #             email = input("Enter email : ")
            #             record[0] = name
            #             record[1] = age
            #             record[3] = email
            #         print(record)

            email = input("email : ").strip()
            is_found = False
            with open("list_students.txt","r") as file:
                students_list = file.readlines()
                for index, student in enumerate(students_list):
                    record = student.strip().split("||")
                    if record[1] == email:
                        name = input("Enter Name : ")
                        age = input("Enter age : ")
                        students_list[index]= f"{name}||{email}||{age}\n"
                        is_found = True
                        break
            if is_found:
                with open("list_students.txt","w") as file:
                        file.writelines(students_list)
                        print("Record Updated Successfully")
            else:
                print("Record not found")
            input()
        case _:
            print("Invalid choice ")
    os.system("cls")