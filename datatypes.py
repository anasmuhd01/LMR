# a=0
# a=-10
# a=""
# a="apple"
# a=" "
# a=None 
# b=bool(a)
# print(b)


# a = '''apple 
# is red '''

# print(a)

# a="apple is red"
# print(a)

# # a[6]="o"
# # TypeError: 'str' object does not support item assignment

# print(a[6]) 

# a= "apple is red"

# for i in range(len(a)):
#     print(a[i])

# for i in a:
#     print(i)

# count=0
# nm = input("Enter a string ")
# # for i in nm:
# #     if i == 'a' or i =='e' or i =='i' or i=='o' or i=='u':
# #         # print(i)
# #         count+=1
# # print(count)

# # using MEMBERSHIP OPERATOR  
# for i in nm:
#     if i in 'aeiouAEIOU':
#         # print(i)
#         count+=1

# print(count)

# a = "c::\file\bin\ti"
# print(a)

# a = "c::\\file\\bin\\ti"
# print(a)

'''r is used in order to reduce string length from
using " escpe characters " , instead of \\ " r  " can be 
used'''

# a = r"c::\file\bin\ti"
# print(a)

'''STRING FORMATING
    using formating method-- .format()
    {}--> is called placeholder
'''

# name = input("enter name: ")
# number = input("enter number")

# string_formating="{},you have {} messages--".format(name,number)
# print(string_formating)

'''
USING FSTRING METHOD
'''
# str_a=f"{name} you have {number} message"
# print(str_a)

a="apple is red"
b="A"
c=" "
d=['a','b','c']
# for i in range(len(a)):
#     if a[i] == " ":
#         print()
#     print(a[i],end="")

# for i in a:
#     if i == " ":
#         print()
#         continue
#     print(i,end="")

# print(a.replace("apple","strawbery"))
# print(a.isalpha())
# print(a.find('z'))
# print(a.index('z'))
# print(a.strip(' a'))
# print(a.swapcase())
# print(a.upper())
# print(b.casefold())
# print(b.endswith('a'))
# print(c.isspace())
# x='_'
# print(x.join(d))
# print(a.count('a'))

# x={'val1':1,'val2':2}
# y='_'
# print(y.join(x))

# x='   apple is red    '
# print(x.strip())



