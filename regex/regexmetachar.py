import re


#--> []
st="the rain in spain_ 12"
st="a a attt"
# pat="[rain]" # take rain as single character 'r' 'a' 'i' 'n'
# pat="[a-zA-z _]" #from a to z A-Z space _

#--> \
# pat=r"\s" # space
# pat=r"\S" # without space

#--> .
# pat = "."

#--> ^starts with
# pat="^the"

#-->$ends with
# pat="12$"

#--> * zero or more
# pat="t*"   #['', '', '', '', '', 'ttt', '']
# pat="at*"    #['a', 'a', 'attt']

#--> + one or more
# pat= "at+"

#--> ? zero or one 
# pat="t?"   #['', '', '', '', '', 't', 't', 't', '']
# pat="tt?" #['tt', 't']
# pat ="at ?" #['at']

#--> {} exactly the specified number of occurences
# pat ="t{2}"
# pat ="t{0,3}"


# | either or
st="the rain in spain_ 12"
pat = "rain | spain"
res= re.findall(pat,st)


print(res) 