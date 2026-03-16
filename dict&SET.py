a={"name":"ajith","place":"calicut","age":20}
# print(a)

# print(a["name"])

# a["name"]= "sam"
# print(a)

# a["phone"]=910123345678
# print(a)

# for i in a:
#     print(i) #--> will print the keys

#--> 
'''
--------->python dictionary class methods
'''



# a.clear()
# print(a)

# res=dict.fromkeys(["name","age","place"])
# print(res)

# res2=a.get("name")
# print(res2)

# res=a.items()
# print(res)

# for i in res:
#     print(i)
    
# print(a.keys())
# print(a.values())

# res=a.pop("age")
# print(res)
# print(a)

# a.popitem()
# print(a)

# x= a.setdefault("name",'ajithk')
# print(x)
# print(a)

# a.setdefault("last_test",123)
# print(a)

# a.update({"name":"ajith kk"})
# print(a)

# a={1,2,3,3,"apple"}
# print(a)
# a.add("kiwi")
# print(a)
# a.remove("kiwi")
# a.remove(3)
# print(a)


# a ={}

# limit = int(input("enter limit: "))

# for i in range(limit):

#     key=input("enter key: ")
#     valu=input("enter value:  ")

#     a.setdefault(key,valu)

#     a.update({key:valu})

# print(a)

# s = {*()} #--> set 
# print(type(s))

# st ="apple apple apple banana grape grape"
# # st = input("enter your string: ")
# emp_di={}

# splitted = st.split(" ")
# for i in splitted:
#     if i in emp_di:
#         emp_di[i]+=1
#     else:
#         emp_di[i]=1

# print(emp_di)

