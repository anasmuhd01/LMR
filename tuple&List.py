# tup=(1,2,3)
# print(type(tup))

# tup1=(1)
# print(type(tup1)) #--> will return int type <class 'int'>

# tup1=(1,) #--> this is how tuple should be declared
# print(type(tup1))

# tuple concatination
#a=(1,2,3)
#b=(4,5,6)
#c=a+b
#print(c)

#PACKING AND UNPACKING IN TUPLE

# tup2=(1,2,3,"apple") #--> Packiing 
# (p,q,r,w)=tup2 #--> Unpacking

# print(p)
# print(q)
# print(r)
# print(w)

# for i in range(len(tup2)):
#     print(i)  
'''
i --> will return index of tuple elements
a[i] --> will return elements
'''
# for i in tup2:
#     print(i)

# tup=(1,2,1,22,1,4,"apple",2,3,"apple")
# res = tup.count(1)
# print(res) #--> will return the cont of 1 im tup

# res=tup.index("apple")
# print(res)

# res=tup.index("apple",7) #--> will take the index after 7
# print(res)

# res=tup.index("a") #ValueError: tuple.index(x): x not in tuple
# print(res)

#------------------LIST-----------------------------------
# a=[1,2,3]
# print(type(a))

'''
operations like "tuple concatination" 
and tuple "packing&unpacking" is same
'''
# a=[1,2,3] #--> PACKING
# [p,q,r]=a  #--> UNPACKING
#----list concatination----
# a=[1,2,3]
# b=[4,5,6]
# c=b+a
# print(c)