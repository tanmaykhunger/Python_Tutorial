class Person:
    def __init__(self , name):
        self.name = name

    def talk(self):
        print(f"Hi I am {self.name}")


Chahat = Person("Tanmay Khunger")
print(Chahat.name)
Chahat.talk()
Chahat = Person("Chahat Khunger")
print(Chahat.name)
Chahat.talk()

