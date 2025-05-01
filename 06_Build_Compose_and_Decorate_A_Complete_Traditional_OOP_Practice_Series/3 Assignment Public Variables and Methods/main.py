class Car:
    brand = ""

    def __init__(self, brand):
        self.brand = brand 

    def start(self):
        print(f"{self.brand} is starting...")

if __name__ == "__main__":
    my_car = Car("BMW")

    print("Car Brand:", my_car.brand)

    my_car.start()
