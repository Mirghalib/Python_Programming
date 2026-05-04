# has_license = input("Do have a license (yes/no) : ".lower())
# if has_license == "yes" or has_license == "y":
#     print("You Can Drive")
# elif has_license == "no" or has_license == "n":
#     age = int(input("Enter your Age : "))
#     if age >= 20:
#         print("Your are eligible for to apply for license ")
#     else:
#         print("You are underage to apply for license")
# else:
#     print("Invalid Value")
# print("The Program is End.......")

# num = int(input("Enter a Number : "))
# if num%2 == 0:
#     print(f"{num} is Even Number")
# elif num%2 != 0:
#     print(f"{num} is Odd Number")

# print("======= Welcome to Loan Aligiblity Checker System")
# user_name = input("Enter Your Name : ")
# user_age = int(input("Enter your Age : "))
# user_income = int(input("Enter your Income : "))
# user_credit_source = int(input("Enter your Credited Source : "))

# if user_age >= 25 and user_income >= 35000 and user_credit_source >= 10000:
#     print("Your are Eligiable for Our Loan")
# else:
#     print("Your are not Eligiable for Our loan")

# print("== Welcome to Loan Aligiblity Checker System for our loan scheme ==")
# user_name = input("Enter Your Name : ")
# user_age = int(input("Enter your Age : "))
# user_income = int(input("Enter your Income : "))
# user_credit_source = int(input("Enter your Credited Source : "))

# if user_age >= 25 and user_income >= 35000 and user_credit_source <= 10000:
#     print(f"=================== congratulations ====================\n    Mr {user_name} your age is valid.\n    Mr {user_name} your income is valid\n    Mr {user_name} your Credit Source is valid\n    Mr {user_name} your are eligible for our loan Scheme")
# elif user_age < 25:
#     print(f"Mr {user_name} your age is not valid for our laon scheme. Age must be above 25 years")
# elif user_income < 35000:
#     print(f"Mr {user_name} your income is not valid for our laon scheme. income must be above 35000 per month")
# elif user_age < 25:
#     print(f"Mr {user_credit_source } your Credit Source  is not valid for our laon scheme. Age must be less then 10000")
# print("\n============= Thank you for using our system =============")

# print("======= Grading System =======")
# user_score = int(input("      Enter your score : "))
# if user_score <=100 and user_score >=90:
#     grade = 'A+'
# elif user_score >=80:
#     grade = 'A'
# elif user_score >=70:
#     grade = 'B'
# elif user_score >=60:
#     grade = 'C'
# elif user_score >=50:
#     grade = 'D'
# elif user_score < 50:
#     grade = 'F'
# print(f"      Your Grade is {grade}")

# print("=====  Age Group Classification  =====")
# user_age = int(input("     Enter your age : "))
# if user_age < 2:
#     user = "Infant"
# elif user_age < 12:
#     user = "Child"
# elif user_age < 19:
#     user = "Teenager"
# elif user_age < 12:
#     user = "Adult"
# else:
#     user = "Senior"
# print(f"      You are a {user}")

print("===== Discount Calculator =====")
purchase_amount = int(input("Enter Your Purchase Amount : "))
if purchase_amount < 1000:
    discount = 0
elif purchase_amount >= 1000:
    discount = (5/100)*purchase_amount
elif purchase_amount >= 2000:
    discount = (10/100)*purchase_amount
elif purchase_amount >= 3000:
    discount = (15/100)*purchase_amount
elif purchase_amount >= 4000:
    discount = (20/100)*purchase_amount
Payable_amount = purchase_amount - discount
print(f"The Payable amount after discount is {Payable_amount}")



