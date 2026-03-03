# import string
import re
import random

# var=input("enter string ")
# print(var.isidentifier())

# s= string.digits
# print(s)
# one="1"
# for i in s:
#     if one in i:
#         print(True)
# -1
# strin=input("Enter a identifier: ")
# pat="^[_a-zA-z][a-zA-z0-9]{1,}$"
# res=re.findall(pat, strin)
# if res:
#     print(res)
# else:
#     print("Not valid identifier:")



# -2
# password = input("enter password:")
# le=len(password)
# pat=r"[0-9]"
# res=re.findall(pat,password)
# if le>= 8 and res:
#     print("valid password")
# else:
#     print("not valid password")

# -3
# sum=0
# for i in range(3):
#     values =int(input(f"enter number {i+1} :"))
#     sum= sum+values
# print("sum =" ,sum)

# -4

from itertools import permutations
# length=int(input("Enter length of identifier: "))
arr=['a','b','c']
# for i in range(length):
#     ch=input("enter characters: ")
#     arr.append(ch)
# "".join(p) 
res=[p for p in permutations(arr)]
# for i in range(arr):
#     print(permutations(i))
print(res)

# identifier_lis=[]
# pat="^[_a-zA-z][a-zA-z0-9]{1,}$"
# for word in res:
#     if re.match(pat,word):
#         identifier_lis.append(word)
# print(identifier_lis)

#  --4
# user_input=[]
# length=int(input("Enter identifier length: "))
# for i in range(length):
#     a=input(f"Enter character {i+1} :")
#     user_input.append(a)

# final_res=[]
# def permutation(chars,current):
#     if len(chars)==0:
#         final_res.append(current)
#         return
#     for i in range(len(chars)):
#         reminder= chars[:i]+chars[i+1:]
#         permutation(reminder, current+chars[i])

# permutation(user_input,"")
# print(final_res)

# identifier_lis=[]
# pat="^[_a-zA-z][a-zA-z0-9]{1,}$"
# for word in final_res:
#     if re.match(pat,word):
#         identifier_lis.append(word)
    
# print(identifier_lis)


# -5 
# avg=0
# sum=0
# for i in range(5):
#     marks= int(input(f"Enter Mark {i+1}: "))
#     sum+= marks
#     avg = sum/5


# if avg >= 90:
#     print("A")
# elif avg >=70 and avg<90:
#     print("B")
# elif avg >=50 and avg <70:
#     print("C")
# elif avg >=30 and avg <50:
#     print("D")
# else:
#     print("Fail")

# -6 


# def calculations(val1,val2):
#     print(f"{val1} + {val2} = {val1 + val2 }")
#     print(f"{val1} - {val2} = {val1 - val2 }")
#     print(f"{val1} * {val2} = {val1 * val2 }")
#     print(f"{val1} / {val2} = {val1 / val2 }")
#     print(f"{val1} % {val2} = {val1 % val2 }")

# val1=int(input("Enter num 1: "))
# val2=int(input("Enter num 2: "))

# calculations(val1,val2)

# -7
# def comparison(val1,val2):
#     print(f"{val1} > {val2} = {val1 > val2 }")
#     print(f"{val1} < {val2} = {val1 < val2 }")
#     print(f"{val1} == {val2} = {val1 == val2 }")
#     print(f"{val1} >= {val2} = {val1 >= val2 }")
#     print(f"{val1} <= {val2} = {val1 <= val2 }")
    

# val1=int(input("Enter num 1: "))
# val2=int(input("Enter num 2: "))

# comparison(val1,val2)

# -8
# age=int(input("enter age: "))

# if age >= 18 and age<=120:
#     print("Eligble for voting: ")
# else:
#     print("Ineligble: ")

# -9
# number = int(input("Enter a number: "))
# for i in range(10):
#     print(f"{i+1} * {number} = {(i+1)*number}")

#-10
# a=25
# b=11
# print(a)
# print(b)
# print("after swaping")
# a=a+b
# b=a-b
# a=a-b
# print(a)
# print(b)
