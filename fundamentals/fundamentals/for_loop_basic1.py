#1. Basic
print("\n1. Basic")
for x in range(151):
    print(x)

print("\n2. Multiples of Five")
#2. Multiples of Five
for x in range(5, 1001, 5):
    print(x)

# ---- or using the conditional approach ----
for x in range (5, 1001):
    if x % 5 == 0:
        print(x)

#3.Counting, the Dojo Way
print("\n3. Counting, the Dojo Way")
for x in range(101):
    if x % 10 == 0:
        print("Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)

#4. Whoa. that Sucker's Huge
print("\n4. Whoa. that Sucker's Huge")
sum = 0;        
for x in range(500001):
    if x % 2 != 0:
        sum += x
print(f"Final sum is: {sum}")

#5. Countdown by Fours
print("\n5. Countdown by Fours")
for x in range(2018, 0, -4):
        print(x)

#6. Flexible Counter
print("\n6. Flexible Counter")
lowNum = 2
highNum = 9
mult = 3

for x in range(lowNum, highNum+1):
    if x % mult == 0:
        print(x)