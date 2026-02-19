class Main:
    name="Main"
    file="oop.py"

    def display(self):
        print(self.name)


class Sub(Main):
    location="c:\\user\oop"

s=Sub()
print(s.name)
print(s.file)
s.display()