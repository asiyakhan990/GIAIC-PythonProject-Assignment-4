def add_greeting(cls):

    def greet(self):
        return "Hello from Decorator!"
    
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"My name is {self.name}")

p = Person("Alice")
p.show_name()

print(p.greet())
