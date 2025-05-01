class Logger:

    def __init__(self, name):
        self.name = name
        print(f"Logger object '{self.name}' created.")

    def __del__(self):
        print(f"Logger object '{self.name}' is being destroyed.")

if __name__ == "__main__":

    logger1 = Logger("Log1")

    del logger1

    logger2 = Logger("Log2")
