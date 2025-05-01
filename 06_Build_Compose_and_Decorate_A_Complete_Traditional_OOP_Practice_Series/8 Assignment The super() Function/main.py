class Person:
    def __init__(self, name):
        self.name = name
        print(f"[Person] Name set to: {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  
        self.subject = subject
        print(f"[Teacher] Subject set to: {self.subject}")

    def display_info(self):
        print(f"Teacher Name: {self.name}")
        print(f"Subject: {self.subject}")


teacher1 = Teacher("Mr. Ahmed", "Mathematics")

print("\nTeacher Information:")
teacher1.display_info()
