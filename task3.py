# import string
import re
# s= string.digits
# print(s)
# one="1"
# for i in s:
#     if one in i:
#         print(True)
strin="a_123"
pat="^[_a-zA-z][a-zA-z0-9]{1,}$"
res=re.findall(pat, strin)
print(res)

var=input("enter string ")
print(var.isidentifier())

pat = "^[a-zA-z0-9]"
