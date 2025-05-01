class Employee:
    def __init__(self, name, salary, ssn):
        # Public variable
        self.name = name
        
        # Protected variable
        self._salary = salary
        
        # Private variable
        self.__ssn = ssn

    def display_info(self):
        print("Inside class:")
        print(f"Name (Public): {self.name}")
        print(f"Salary (Protected): {self._salary}")
        print(f"SSN (Private): {self.__ssn}")


emp = Employee("Alice Johnson", 75000, "123-45-6789")

print("Outside class:")
print(f"Name (Public): {emp.name}")         

print(f"Salary (Protected): {emp._salary}")

try:
    print(f"SSN (Private): {emp.__ssn}")   
except AttributeError as e:
    print(f"SSN (Private): Cannot access directly: {e}")

print(f"SSN (Private via mangling): {emp._Employee__ssn}")  

print("\nUsing class method:")
emp.display_info()
