#Multiple Inheritance

# class A:
#     aname="A"
# class B:
#     bname="B"
# class C(A,B):
#     cname="C"

# ob=C()
# print(ob.aname)
# print(ob.bname)
# print(ob.cname)

#Multi-level Inheritance
# class A:
#     aname="A"
# class B(A):
#     bname="B"
# class C(B):
#     cname="C"

# ob=C()
# print(ob.aname)
# print(ob.bname)
# print(ob.cname)

#Hierarchical Inheritance

# class A:
#     aname="A"
# class B(A):
#     bname="B"
# class C(A):
#     cname="C"


#over riding

class A:
    name="A"
class B(A):
    name="B"
ob=B()
print(ob.name)


