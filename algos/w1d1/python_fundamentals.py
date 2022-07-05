""""
Data types - JS
Primitives:
String
Numbers
Boolean
null
undefined

Composites:
Array
Objects
"""

# This is an inline comment
# JS - let/var/const var_name = "value";


# Python uses snake_ase for var and function names
# boolean:
from locale import format_string


flag = True   # (in python it MUST be True or False, first letter uppercase)

# Numbers: integers / floats
grade = 9.45
age = 20

# Strings:
first_name = "Alex"
last_name = 'Miller'
siblings = None

# can use + to concatenate strings
print(first_name + last_name)

# JS - console.log(variable_name);
print(flag)
print(grade)
print(first_name)
print(last_name)
print(siblings)

# Type casting
#print(last_name + age)
print(last_name + " " + str(age))
print(f"Hello there my name is {first_name} {last_name} and I am {age} years old.")

#age = "twenty"
#print(last_name + age)

#determine variable type
print(type(age))
print(type(flag))
print(type(first_name))

print (int(grade), grade)  # Int will always "round down", i.e. it is equivalent truncation 

print(len(first_name), len(last_name))
print(first_name.upper())

