# for i in range(5,0,-1):
#     for j in range(i):
#         print("  ",end=" ")
#     for k in range(5-i+1):
#         print("  * ",end="  ")
#     print()

# for i in range(6):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# for i in range(6,1,-1):
#     for j in range(i-1):
#         print("*", end=" ")
#     print()

# for i in range(1,6):
#     for j in range(6-i):
#         print(" ",end="")
#     for k in range(i):
#         print("*",end=" ")
#     print()


    
    
  
# class MyClass:
#     x=123

# class tempClass:
#     pass
 
# p1=MyClass()

# print(p1.x)
# class Person:
#   def __init__(self,name,age):
#     self.name=name
#     self.age=age
#   def greet(self):
#     print(f"Hello, my name is {self.name}")
# p1= Person( "John",36)
# p1.greet()


class Myclass:
    def test(self):
        return "hello"
    
    def test2(self):
        msg = self.test()
        print(f"{msg} anas")

p1 = Myclass()
p1.test2()