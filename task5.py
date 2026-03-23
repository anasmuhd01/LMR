#1
# for i in range(1,21):
#     if i %3 ==0 or i%5==0:
#         print(i)

#2
# for i in range(1,10):
#     if i % 4 ==0:
#         break
#     print(i)

#3
# word=input("Enter a word: ")
# print(f"reversed: {word[::-1]}")

#4
# num=int(input("enter a number: "))
# temp=num
# n_of_digits=len(str(num))
# sum=0
# while num>0:
#     mod=num%10
#     sum+=mod**n_of_digits
#     num//=10
# if temp==sum:
#     print("ARMSTRONG NUMBER")
# else:
#     print("NOT ARMSTRONG")

#5
# ran=int(input("Enter range:"))

# for i in range(1,ran+1):
#     if ran<2:
#         print(i)
#     flag=0
#     for j in range(2,i):
#         if i % j ==0:
#             flag=1
#             break
#     if flag==1:
#         print(i)

#6
# import re
# pas=input("Enter password:")
# pat=r"[a-zA-Z1-9!@#$%^&*._]{8,}"
# res=re.findall(pat,pas)
# if res:
#     print("VALID PASSWORD! ")
# else:
#     print("PASSWORD INVALID! ")

#7
# num=int(input("Enter a number"))
# sum=0
# for i in range(1,num):
#     if num%i==0:
#         sum+=i

# if num==sum:
#     print("perfect number:")
# else:
#     print("not perfect number:")
    
#8

# from itertools import permutations
# og_clctn=[1,2,3]
# print(list(permutations(og_clctn)))


#9
# num=123
# count=0
# while num>0:
#     num//=10
#     count+=1
# print(count)

#10
n="192 168 255 251"
res=n.split(" ")
last=int(res[-1])

for i in range(4):
    res[-1]=str(last+i)
    print(" ".join(res))