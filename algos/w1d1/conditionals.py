# > < >= <= == != ! and or not

num = 14
if num > 15:
    print(f"{num} is greater than 15")
    print("Check next number...")
else:
    if num == 15:
        print(f"{num} is exactly 15.")
    else:
        print( f"{num} is less than 15")
    
print("Outside of if statement block")


num = 14
if num > 15:
    print(f"{num} is greater than 15")
    print("Check next number...")
elif num == 15:
    print(f"{num} is exactly 15.")
else:
    print( f"{num} is less than 15")
    
print("Outside of if statement block")

"""
Order of execution:
1.   ()
2.   * / %
3.   + -
4.   not
5.   < > <= >= ==
6.   and or
6.5. += -=
7.   =
"""