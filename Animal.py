class Animal:
    def __int__(self, species, name):
        self.species = species
        self.name = name

    def speak(self):
        print("Hello! I am a " + str(self.species))
