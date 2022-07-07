class Pet:
    def __init__(self, name, pet_type, tricks):
        self.name = name
        self.type = pet_type
        self.tricks = tricks
        self.health = 100
        self.energy = 100

    def sleep(self):
        print(f"Sleepytime for {self.name}")
        self.energy += 25
        return self

    def eat(self):
        print(f"Nom nom nom nom time for {self.name}")
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        print(f"{self.name} is playing")
        self.health +=  5
        return self

    def noise(self):
        print(f"{self.name} the {self.type} says meowwwww purrrrr")
        return self

class FurryPet(Pet):
    # def __init__(self, name, pet_type, tricks):
    #     super().__init__(name, pet_type, tricks)
    def noise(self):
        print(f"{self.name} the {self.type} says woof")
        return self

class ScalyPet(Pet):
    # def __init__(self, name, pet_type, tricks):
    #     super().__init__(name, pet_type, tricks)
    def noise(self):
        print(f"{self.name} the {self.type} says hissssss")
        return self

class FeatheryPet(Pet):
    # def __init__(self, name, pet_type, tricks):
    #     super().__init__(name, pet_type, tricks)
    def noise(self):
        print(f"{self.name} the {self.type} says quaaaaack")
        return self
