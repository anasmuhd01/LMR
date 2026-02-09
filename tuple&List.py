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

#list methods

# a=[1,2,3]
# a.append(5)
# a.clear()
# a=[4,5,6,4,4,]
# b = a.copy()
# print(b)
# x =a.count(4)
# print(x)
# a=[1,2,3]
# b=[12,23]
# a.extend(b)
# print(a)

# a=[11,9,4,25]
#a.pop() #--> last item will poped 
# x=a.pop(1) #-->will pop the item at index 1 
# print(x) #--> will return poped item 
# print(a) 

# a=[44,55,23,11]
# # a.remove(44) #--> will remove the item 44 no return data

# a.sort()
# a.reverse()
# print(a)

# a=[1,2,3]
# b=a
# print(id(a))
# b.append(4)
# print(id(b))

# print(a)
# print(b)

# a=[1,2,3]
# b=a.copy()
# print(id(a))
# b.append(4)
# print(id(b))

# print(a)
# print(b)


#type converting tuple to list and to tuple again

# a=(1,2,3,4)
# # a[3]="kiwi" not possible due to immutability

# b=list(a)
# b[3]="kiwi"
# print(b)

# a=tuple(b)
# print(a)

# size = int(input("enter limit"))
# a =[]

# for i in range(size):
    
#     elements= input("enter elements :")
#     a.append(elements)
# print(a)
    
# main=[12,31,4,16,109,82,77,133,241,1092]
# odd=[]
# even=[]
# for i in main:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# odd.sort()
# even.sort()
# print("odd list --> ", odd)
# print("even list --> ", even)

sum=0
main=[12,31,4,16,109,82,77,133,241,1092,1]

# for i in main:
#     sum+=i
# print(sum)
#--> to print largest number

# print(main[0])
# print(main[0+1])
# larg=main[0]
# for i in main:
#     if larg<i:
#         larg=i
# print(larg)


#--> to print smallest number
# small=main[0]
# for i in main:
#     if small>i:
#         small=i
# print(small)
 
# --> to print without repeatation     
# a=[1,2,1,1,2,1,4,5,6,1,3,4,5,6]
# b=[]
# for i in a:
#     if i in b:
#         continue
#     else:
#         b.append(i)
# print(b)

        

# b=set(a)
# print(b)



