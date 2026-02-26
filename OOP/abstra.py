from abc import ABC,abstractmethod

# class AbstractExample(ABC):
#     @abstractmethod
#     def show(self):
#         pass


# class Child(AbstractExample):
#     def show(self):

#         return super().show()
    
    
# ob=Child()

class Vehicle(ABC):
    @abstractmethod
    def accelarate(self):
        pass
    @abstractmethod
    def breaking(self):
        pass


class Car(Vehicle):
    def accelarate(self):
        print("car moves")

    def breaking(self):
        print("car stops")


ob=Car()
ob.accelarate()
ob.breaking()
