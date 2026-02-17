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

class Arith:
    def __init__(self,val1,val2):
        self.val1=val1
        self.val2=val2

    def add(self):
        return self.val1+self.val2
    
    def po(self,n):
        print(self.val1**n)
    

add=Arith(10,20)
print(add.add())
