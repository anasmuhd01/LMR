class Laptop:
    ram=4
    rom=256
    
    def booting(self):
        print("laptop booting")

    def __init__(self): #--> constructor
        print("init test")


dell=Laptop()

print(dell.ram)
print(dell.rom)
dell.booting()

