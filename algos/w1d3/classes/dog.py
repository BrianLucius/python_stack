from classes.animal import Animal

class Dog(Animal):
    list_of_dogs = []
    def __init__(self, name, owner, breed, color):
        super().__init__(name, owner, breed)  # pass in attributes that are being inherited
        self.color = color
        Dog.list_of_dogs.append(self)
        
    #overriding
    def print_info(self):
        super().print_info()
        print(f"Color: {self.color}")
        
    # Polymorphism - from unimplemented method in parent class
    def walk_animal(self):
        print(f"I'm a dog so I need to be walked at least 2 times a day!")
        
    @classmethod
    def print_all_dogs(cls):
        for cat in cls.list_of_dogs:
            cat.print_info()