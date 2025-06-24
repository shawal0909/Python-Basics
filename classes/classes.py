class Human:
    def __init__(self, name, age):
        self.__name = name      # Private attribute
        self.__age = age        # Private attribute

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Getter for age
    def get_age(self):
        return self.__age

    # Setter for age
    def set_age(self, age):
        self.__age = age

    def greet(self):
        print(f"Hello, my name is {self.__name} and I am {self.__age} years old.")

class Student(Human):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.__student_id = student_id  # Private attribute

    # Getter for student_id
    def get_student_id(self):
        return self.__student_id

    # Setter for student_id
    def set_student_id(self, student_id):
        self.__student_id = student_id

    def study(self):
        print(f"{self.get_name()} is studying.")

# Usage demonstrating encapsulation
student1 = Student("Ali", 20, "S123")
student1.greet()
student1.study()

# Accessing and modifying attributes via getters and setters
print("Student ID:", student1.get_student_id())
student1.set_student_id("S456")
print("Updated Student ID:", student1.get_student_id())

# Changing name and age using setters
student1.set_name("Ahmed")
student1.set_age(21)
student1.greet()