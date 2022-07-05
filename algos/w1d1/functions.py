"""
JS:
function add(num1, num2) {
    return num1  +  num 2;
}
"""

# def add(num1, num2):
#     x = num1 + num2
#     return x

# print(add(10, 12))

def add_three(num1, num2=3):
    print(num1)
    print(num2)
    return num1 + num2

print(add_three(5))

print(add_three(8, 4))

print(add_three(num2=5, num1=7))

print(add_three(num2=5, num1=7))