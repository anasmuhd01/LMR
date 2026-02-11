#----------PALINDROME-----------

# inp=input("enter a string: ")

# res=inp[::-1]
# if res == inp:
#     print("PALINDROME")
# else:
#     print("NOT PALINDROME")

# a=[1,2,3] #--> gloabl scope <--

# def fun():
#     global b #--> to make global scope of the local variable
#     print("from fun",a)
#     b=[1,2,3] #--> local scope <--
# fun()
# print(b)

# for i in a:
#     print(i)

# if True:
#     print(a)



for i in range(5,0,-1):
    for j in range(i):
        print(" ",end=" ")
    for k in range(1):
        print("*",end=" ")
    print()



