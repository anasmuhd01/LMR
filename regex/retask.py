import re
st=input("enter name: ")
patter="^[A-Z][a-z]{3,}$"
res=re.match(patter,st)
if res:
    print("Valid name")
else:
    print("Invalid name")
