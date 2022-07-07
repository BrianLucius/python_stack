# from package_name import module/variable/function/class

# from classes.animal import name, greeting

# print(name)
# greeting()

# from classes import animal

# print(animal.name)
# animal.greeting()

from classes.animal import Animal
from classes.dog import Dog
from classes.cat import Cat

max = Animal("Max", "Alex", "Retriever")
max.print_info()

jagger = Dog("Jagger", "Alfredo", "Golden Retriever", "golden")
jagger.print_info()
jagger.walk_animal()

boots = Cat("Boots", "Brian", "Tuxedo", "B&W", 13)
boots.print_info()
boots.walk_animal()