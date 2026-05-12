# def my_functions(fruits):
#     for fruit in fruits:
#         print(fruit)

# my_fruits = ["Apple","Banana","Orange","Cherry"]
# # my_functions(my_fruits)


# def my_function(person):
#     print("\n============  Person Details  ============")
#     print("            Name    :    ",person["name"])
#     print("            Age     :    ",person["age"])
#     print("            Email   :    ",person["email"])
#     print("            Status  :    ",person["status"])
#     print("            Gender  :    ",person["gender"])
#     print("=="*21)

# person_dict = { "name":"Ghalib", 
#                "age":22,
#                "email": "ghalib@gmail.com",
#                "status":"Unmarried",
#                "gender":"Male"
#                }
# my_function(person_dict)

# sum = lambda a,b : a + b
# print(sum(5,4))


# def myfun(num):
#     return lambda a : a**num

# power_2 = myfun(2)
# power_3 = myfun(3)
# power_4 = myfun(4)
# power_5 = myfun(5)
# print("\n   ======= Power Function ========")
# print("          power 2   :  ",power_2(5))
# print("          power 3   :  ",power_3(5))
# print("          power 4   :  ",power_4(5))
# print("          power 5   :  ",power_5(5))
# print()


def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))