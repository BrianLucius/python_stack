from classes.animal import Animal
from classes.dog import Dog
from classes.cat import Cat

# first_name = input("Please enter your first name: ")
# print(f"It's nice to meet you {first_name}")

print("****** Options Menu ******")
print(f"0) Exit animal house")
print(f"1) Add a cat")
print(f"2) Add a doc")
print(f"3) Print all Dogs")
print(f"4) Print All Cats")
option = input("Select animal to add: ")

while option != '0':
    if option == "1":
        name = input("Name of your cat: ")
        owner = input("Who is the owner: ")
        breed = input("Breed of your cat: ")
        color = input("Color of your cat: ")
        age = input("Age of cat: ")
        new_cat = Cat(name, owner, breed, color, age)
    elif option == "2":
        name = input("Name of your dog: ")
        owner = input("Who is the owner: ")
        breed = input("Breed of your dog: ")
        color = input("Color of your dog: ")
        new_dog = Dog(name, owner, breed, color)
    elif option == "3":
        Dog.print_all_dogs()
    elif option == "4":
        Cat.print_all_cats()
    print("****** Options Menu ******")
    print(f"0) Exit animal house")
    print(f"1) Add a cat")
    print(f"2) Add a doc")
    print(f"3) Print all Dogs")
    print(f"4) Print All Cats")
    option = input("Select animal to add: ")