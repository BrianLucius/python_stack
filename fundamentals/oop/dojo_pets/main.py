from classes import pet,ninja

ninja_owner = ninja.Ninja("Brian","Lucius","tuna","kibble",pet.Pet("boots","cat","attack"))
ninja_owner.feed().walk().bathe()
print(f"Pet Energy: {ninja_owner.pet.energy} \nPet Health: {ninja_owner.pet.health}")

print()

ninja_owner2 = ninja.Ninja("Frankie","Johnny","worms","crickets",pet.ScalyPet("simon","snake","slither"))
ninja_owner2.feed().feed().bathe()
print(f"Pet Energy: {ninja_owner2.pet.energy} \nPet Health: {ninja_owner2.pet.health}")

print()

ninja_owner3 = ninja.Ninja("Jane","Doe","beer","pancakes",pet.FeatheryPet("howard","duck","talks"))
ninja_owner3.feed().walk().feed().walk().bathe()
print(f"Pet Energy: {ninja_owner3.pet.energy} \nPet Health: {ninja_owner3.pet.health}")
