# fruits = ["Apple","Banana","Orange"]
# for x in fruits:
#     print(x)


# fruits = ["Apple","Banana","Orange"]
# for x in fruits:
#     print(x.upper())


# x = 1
# for x in range(6):
#     print(x)


# for x in range(6):
#     for j in range(6):
#         print("*",end=" ")
#     print()


# for x in range(6):
#     for j in range(6):
#         print(j,end=" ")
#     print()


# for x in range(6):
#     for j in range(6):
#         print(x,end=" ")
#     print()

# for x in range(6):
#     for j in range(6):
#         print(f"{x}{j}",end=" ")
#     print()

# rows = 5
# for i in range(1, rows + 1):
#     print(' ' * (rows - i) + '*' * (2 * i - 1))

# rows = 5
# for i in range(rows, 0, -1):
#     print(' ' * (rows - i) + '*' * (2 * i - 1))


# i = 5
# for j in range(1,i+1):
#     print(" "*(i-j)," *"*j)



# i = 5
# for j in range(i,0,-1):
#     print(" "*(i-j)," *"*j)


num = 3
count = 0
for x in range(1,num+1):
    if num%x == 0:
        count +=1
if count == 2:
    print("Prime")
else:
    print("Not Prime")