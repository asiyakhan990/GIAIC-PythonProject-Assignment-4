class Student:
    def __init__(self, name, marks):
        self.name = name       
        self.marks = marks    

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)

if __name__ == "__main__":

    student1 = Student("Aswad", 87)
    student2 = Student("Asiya", 92)

    print("Details of Student 1:")
    student1.display()
    print("\nDetails of Student 2:")
    student2.display()
