# name = "Alex"

# def greeting():
#     print("Hello there")


class Animal:
    def __init__(self, name, owner, breed):
        self.name = name
        self.owner = owner
        self.breed = breed
        
    def print_info(self):
        print(f"\nName of animal: {self.name}")
        print(f"Owner: {self.owner}")
        print(f"Breed: {self.breed}")
        
    # Polymorphism
    def walk_animal(self):
        raise NotImplemented