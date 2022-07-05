num1 = 42 # variable declaration, initialize number
num2 = 2.3 # variable declaration, initialize number
boolean = True # variable declaration, initialize boolean
string = 'Hello World' # variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration, initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration, initialize tuple
print(type(fruit)) # function print tuple
print(pizza_toppings[1]) # function print index 1 from list pizza_toppings
pizza_toppings.append('Mushrooms') # function list add value
print(person['name']) # function print "name" attribute from person dictionary
person['name'] = 'George' # dictionary person change value name
person['eye_color'] = 'blue' # dictionary person change value eye_color
print(fruit[2]) # function print index 2 from tuple fruit

if num1 > 45:   # conditional if
    print("It's greater")  # function print string
else:   # conditional else
    print("It's lower") # function print string

if len(string) < 5: # conditional if length of string is < 5 characters
    print("It's a short word!") # function print string
elif len(string) > 15: # conditional else if string > 15 characters
    print("It's a long word!") # function print string
else: # conditional else
    print("Just right!") # function print string

for x in range(5): # for loop, iterate 5 times
    print(x) # function print variable x
for x in range(2,5): # for loop, iterate from 2 to 5
    print(x) # function print variable x
for x in range(2,10,3): # for loop, iterate from 2 to 3, skipping 3 each time
    print(x) # function print variable x
x = 0 # variable declaration, initialize to 0
while(x < 5): # while loop, x must be less than 5
    print(x) # print variable x
    x += 1 # variable assignment, increment by 1

pizza_toppings.pop()  # list delete last value
pizza_toppings.pop(1) # list delete index 1

print(person)  # function print person dictionary
person.pop('eye_color') # dictionary remove the 'eye_color' attribute
print(person)  # function print person dictionary

for topping in pizza_toppings: # for loop start
    if topping == 'Pepperoni': # conditional if
        continue # for loop continue
    print('After 1st if statement')  #function print text
    if topping == 'Olives':  # conditional if 
        break # exit for loop

def print_hello_ten_times(): # function definition
    for num in range(10):  # for loop start
        print('Hello')  #function print text

print_hello_ten_times()  # function call

def print_hello_x_times(x): # function definition, accept parameter
    for num in range(x): # for loop start
        print('Hello') # function print text

print_hello_x_times(4) #function call passing argument

def print_hello_x_or_ten_times(x = 10):  # function definition, accept parameter, set default to 10
    for num in range(x): # for loop start
        print('Hello') # function print text

print_hello_x_or_ten_times() # function call, no arguments passed, use default in function
print_hello_x_or_ten_times(4) # function call, pass argument, override default


"""                 # multi-line comment
Bonus section
"""

# print(num3)  # NameError: name <variable name> is not defined
# num3 = 72
# fruit[0] = 'cranberry' # TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) # KeyError: 'favorite_team'
# print(pizza_toppings[7]) # IndexError: list index out of range
#   print(boolean)  # IndentationError: unexpected indent
# fruit.append('raspberry') # AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) # AttributeError: 'tuple' object has no attribute 'pop'