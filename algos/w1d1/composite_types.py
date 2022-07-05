# JS - Array [item, item, item] : Python - lists
grades = [9.8, 8.7, 7.6]
#          0    1    2

print(grades)
print(grades[0])
print(len(grades))

# Add an element to a list JS - .push(element) : Python .append()
grades.append(10.0)
print(grades)

grades_copy1 = grades # is a reference to the original object
grades_copy2 = grades[:]
print(grades_copy1)
print(grades_copy2)

grades.append(8.4)
print(grades_copy1)
print(grades_copy2)

# JS Objects : Python Dictionary  (in JS quotes are optional, python quotes are required)
student = {
    "first_name" : "Alex",
    "last_name" : "Miller",
    "age" : 20,
    "stack" : "Python/Flask",
    "passed" : True,
    "belts" : ["yellow", "red", "black"]
}

print(student)
print(student["first_name"])

name_key = "first_name"
print(student[name_key])
print(student["belts"][2])

student["instructor"] = "Alfredo Salazar"
print(student)

# Python : Tuple (similar to a list), immutable data type
course = ("Python", "4 weeks", "Spencer Rauch")
print(course)
#course.append("Pablo Padilla") #AttributeError: 'tuple' object has no attribute 'append'

print(course[0])

#course[0] = "Web Fundamentals" #TypeError: 'tuple' object does not support item assignment


student = {
    "first_name" : "Alex",
    "last_name" : "Miller",
    "age" : 20,
    "grade" : 9.6,
    "stack" : "Python/Flask",
    "passed" : True,
    "class" : {
        "subject" : "math",
        "instructor" : "Pablo"
    }
}

print(student["class"]["subject"])