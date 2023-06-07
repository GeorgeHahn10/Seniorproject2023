from Animal import Animal


class Dog(Animal):
    anytext = "something"

    def __init__(self, name, age, breed):
        super().__init__()
        self.age = age
        self.breed = breed

    # def speak(self):
    #     print(self.name + " says woof")

    def setText(self, t):
        Dog.anytext = t
