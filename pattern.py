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


inp=int(input("enter limit: "))

for i in range(inp,0,-1):
    for j in range(i):
        print("* ",end="")
    print()