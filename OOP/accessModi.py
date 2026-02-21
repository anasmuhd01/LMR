#public
class PubEx:
    name="test_name"
    def dis(self):
        print(self.name)


class PubEx:
    __name="test_name"
    def dis(self):
        print(self._name)

ob= PubEx()

print(ob._PubEx__name) #name mangling to access private member but dont use