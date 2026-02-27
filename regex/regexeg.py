import re


# st="apple is red"
# pat=r"\ba.*e\b"
# res=re.search(pat, st)
# print(res)
# print(res.span())
# print(res.group())

# st="red apple is round"
# pat=r"\br\S*d\b"
# res=re.findall(pat, st)
# print(res)

# # res=re.split(r"\s",st)
# res=re.split(" ",st)
# print(res)

# res=re.sub("red","orange",st)
# print(res)

# res=re.match("red",st)
# res=re.match(pat,st)
# print(res)

# example="red at apple is round attt atatat"
# pattern=r"(at)+"
# res=re.findall(pattern,example)
# print(res)

# txt="2026-02-26"
# m=re.search(r"(\d{4})-(\d{2})-(\d{2})",txt)
# print(m)
# print(m.group(1))
# print(m.group(2))
# print(m.group(3))

#wap a program to validate a given mobile number using regex

# phone_no=input("enter number: ")

# pattern=r"^[7-9][0-9]{9}$"
# res=re.findall(pattern,phone_no)
# if res:
#     print("valid phone number: ")
# else:
#     print("invalid phone number:")

#Wap to check if a given email id is valid or not

test="sss@gmail.com"
pattern=r"^[a-z0-9]+[@][a-z]{3,}$"
res=re.findall(pattern,test)
print(res)