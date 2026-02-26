import re


# st="apple is red"
# pat=r"\ba.*e\b"
# res=re.search(pat, st)
# print(res)
# print(res.span())
# print(res.group())

st="red apple is round"
pat=r"\br\S*d\b"
# res=re.findall(pat, st)
# print(res)

# # res=re.split(r"\s",st)
# res=re.split(" ",st)
# print(res)

# res=re.sub("red","orange",st)
# print(res)

# res=re.match("red",st)
res=re.match(pat,st)
print(res)