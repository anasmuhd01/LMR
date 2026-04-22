limit =5
# for i in range ( 1,limit+1):
#     for j in range(6,i,-1):
#         print("*",end=" ")
#     print()


for i in range(limit+1):
    for j in range(i):
        print(i,end=" ")
    print()