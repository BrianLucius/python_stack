from classes.animal import Animal

class Cat(Animal):
    list_of_cats = []
    def __init__(self, name, owner, breed, color, age):
        super().__init__(name, owner, breed)
        self.color = color
        self.age = age
        Cat.list_of_cats.append(self)
        
    def print_info(self):
        super().print_info()
        print(f"Color: {self.color}")
        print(f"Age: {self.age}")
        
    # Polymorphism - from unimplemented method in parent class
    def walk_animal(self):
        print(f"I'm a cat, I need to sleep 20 hours per day!")
        
    def print_info(self):
        super().print_info()
        print(f"Age: {age}")
        
    @classmethod
    def print_all_cats(cls):
        for cat in cls.list_of_cats:
            cat.print_info()