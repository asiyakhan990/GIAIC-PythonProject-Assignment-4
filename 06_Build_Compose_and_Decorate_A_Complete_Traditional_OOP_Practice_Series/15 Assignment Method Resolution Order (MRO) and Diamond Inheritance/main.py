# Class A
class A:
    def show(self):
        print("Show method from class A")

# Class B inherits from A
class B(A):
    def show(self):
        print("Show method from class B")

# Class C also inherits from A
class C(A):
    def show(self):
        print("Show method from class C")

# Class D inherits from both B and C
class D(B, C):
    pass

# Create an object of D and call show
d = D()
d.show()

# Display the Method Resolution Order MRO
print("MRO of class D:", D.__mro__)
