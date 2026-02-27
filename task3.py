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
# print(res)



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
#give loop value by factorial
actual=[]
after_copy=[]
temp_list=[]
length= int(input("enter length of identifier: "))
for i in range(length):
    iden_char = input("enter characters: ")
    temp_list.append(iden_char)

pat="^[_a-zA-z][a-zA-z0-9]{1,}$"
for i in range(10):
    x= "".join(random.sample(temp_list,k=5))
    actual.append(x)
    
    res=re.findall(pat, x)
    after_copy.append(res)
print(actual)
print(after_copy)




# print(temp_list)

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

#-9
# number = int(input("Enter a number: "))
# for i in range(10):
#     print(f"{i+1} * {number} = {(i+1)*number}")

#-10
# a=5
# b=10

# a=a+b
# b=a-b
# a=a-b
# print(a)
# print(b)
