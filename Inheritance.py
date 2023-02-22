class Mammel:
    def walk(self):
        print("walk")


class Dog(Mammel):
    def bark(self):
        print("Bark")


class Cat(Mammel):
    def be_annoying(self):
        print("annoying")


dog1 = Dog()
dog1.walk()
