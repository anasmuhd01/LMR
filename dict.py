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

x= a.setdefault("name",'ajithk')
print(x)
print(a)

a.setdefault("last_test",123)
print(a)

a.update({"name":"ajith kk"})
print(a)