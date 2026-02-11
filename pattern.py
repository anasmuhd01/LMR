#print  given star pattern with user input
# for i in range(5):
#     for j in range(i+1):
#         print("* ",end="")
#     print()



# for i in range(5):
#     star=""
#     for j in range(i+1):
#         star+="* "
#     print(star)


# for i in range(5,0,-1):
#     star=""
#     for j in range(i):
#         star+="* "
#     print(star)


# inp=int(input("enter limit: "))

# for i in range(inp,0,-1):
#     for j in range(i):
#         print("* ",end="")
#     print()


# for i in range(5,0,-1):
#     for j in range(i):
#         print(j,end=" ")
#     print()

# for i in range(5,0,-1):
#     for j in range(i):
#         print("1 ",end="")
#     for k in range(i):
#         print("* ",end="")
#     print()

limit =5
# for i in range(1,limit+1):
#     for j in range(limit,i-1,-1):
#         print(" ",end=" ")
#     for k in range(i):
#         print("* ",end="  ")
#     print()


# for i in range(1,limit+1):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(limit,i-1,-1):
#         print("* ",end="  ")
#     print()

# ****----patten another method--------

# for i in range(1,limit+1):
#     for k in range(limit-i):
#         print("",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()

# for i in range(1,limit+1):
#     for k in range(i):
#         print("",end=" ")
#     for j in range(limit-i):
#         print("*",end=" ")
#     print()



# for i in range(5):
#     for j in range(i):
#         print(j+1,end=" ")
#     print()

# for i in range(5):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# num=1
# limit =4
# for i in range(1,limit+1):
#     for j in range(i):
#         print(num,end=" ")
#         num+=1
#     print()

limit =5
for i in range(1,limit+1):
    for k in range(limit-i):
        print("",end=" ")
    for j in range(i):
        print(i,end=" ")
    print()