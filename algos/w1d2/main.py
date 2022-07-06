class Student:
    # constructor
    def __init__(self, first_name, last_name, age, instructor, course):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.instructor = instructor
        self.course = course
    # methods
    def print_information(self, message):
        print(f"\n{message}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Instructor: {self.instructor}")
        print(f"Course: {self.course}")

class Course:
    def __init__(self, data):
        self.name = data["name"]
        self.instructor = data["instructor"]
        self.program = data["program"]
    
    def print_instructor_list(self):
        for instructor in self.instructor:
            print(instructor)
            
    def update_instructor(self, new_name, index):
        if index < len(self.instructor) :
            self.instructor[index] = new_name
    
    def print_info(self):
        print(f"\nProgram: {self.program}")
        print(f"Name: {self.name}")
        self.print_instructor_list()
    
    
student_alex = Student("Alex", "Miller","20","Nichole","Web Fundamentals")
student_martha = Student("Martha","Smith","25","Alfredo","Python")

# print(student_alex)

# print(student_alex.first_name, student_alex.last_name, student_alex.age)

student_alex.print_information("Hey There!")
student_martha.print_information("First Day!")

python = {"name" : "Python/Flask",
          "instructor" : ["Alfredo Salazar", "Spencer Rauch", "Tyler Tybault"],
          "program" : "Full stack"}

course_python = Course(python)

course_python.print_info()
course_python.update_instructor("Ryan Mendez", 2)
course_python.print_info()