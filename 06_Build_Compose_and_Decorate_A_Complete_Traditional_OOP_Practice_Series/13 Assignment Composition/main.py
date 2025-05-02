class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine with {self.horsepower} HP started.")

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine  

    def start_car(self):
        print(f"Starting car: {self.brand}")
        self.engine.start()  

my_engine = Engine(500)

my_car = Car("BMW", my_engine)

my_car.start_car()
