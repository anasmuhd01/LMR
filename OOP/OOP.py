# # class Laptop:
# #     ram=4
# #     rom=256
    
# #     def booting(self):
# #         print("laptop booting")

# #     def __init__(self): #--> constructor
# #         print("init test")


# # dell=Laptop()

# # print(dell.ram)
# # print(dell.rom)
# # dell.booting()


# class Laptop:
#     #parameterized constructor
#     def __init__(self,ra,ro,pr):
#         self.ram=ra
#         self.rom=ro
#         self.processor=pr

#     def booting(self):
#         print("booting"+self.processor)

# hp=Laptop(4,128,"i3")
# hp.booting()
# # print(hp)

# # print(hp.ram)
# # print(hp.rom)
# # print(hp.processor)

# dell=Laptop(8,256,"i9")
# # print(dell.ram)
# # print(dell.rom)
# # print(dell.processor)
# dell.booting()

# class Arith:
#     def __init__(self,val1,val2):
#         self.val1=val1
#         self.val2=val2

#     def add(self):
#         return self.val1+self.val2
    
#     def po(self,n):
#         print(self.val1**n)
    

# add=Arith(10,20)
# print(add.add())


#WAP where a class student is created for storing student name
#and marks from two subject in an object  define method for calculating 
#toatl marks and average marks of each student

# class Student:
#     def __init__(self,name,mark1,mark2):
#         self.name= name
#         self.mark1=mark1
#         self.mark2=mark2

#     def toatl_mark(self):
#         # global total
#         total=self.mark1+self.mark2
#         print(total)

#     def average_mark(self):
#         avg=(self.mark1+self.mark2)/2
#         print(avg)

# stu1=Student("Anas",10,20)
# stu1.toatl_mark()
# stu1.average_mark()

# class Teacher:
#     def __init__(self,name):
#         self.name=name

#     def __str__(self):
#         return self.name
    
#     def __repr__(self):
#         return self.name

# t1=Teacher("sam")
# print(t1)
# print(repr(t1))

# class Main:
#     name="welcom"
#     name1="test"
#     def __init__(self):
#         print("welocme 1")
#     def __del__(self):
#         print("Destructor")

# m1=Main()
# print(m1.name)

        
# m2=Main()
# print(m2.name)

# print(m1.name1)

