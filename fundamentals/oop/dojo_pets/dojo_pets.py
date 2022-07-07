class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self

class Pet:
    def __init__(self, name, pet_type, tricks):
        self.name = name
        self.type = pet_type
        self.tricks = tricks
        self.health = 100
        self.energy = 100

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health +=  5
        return self

    def noise(self):
        print(f"{self.name} the {self.type} says meowwwww purrrrr")
        return self

ninja = Ninja("Brian","Lucius","tuna","kibble",Pet("boots","cat","attack"))

ninja.feed().walk().bathe()

print(f"Pet Energy: {ninja.pet.energy} \nPet Health: {ninja.pet.health}")
