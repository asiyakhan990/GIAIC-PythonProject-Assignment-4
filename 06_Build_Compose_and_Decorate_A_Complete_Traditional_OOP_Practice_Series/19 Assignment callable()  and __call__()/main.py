class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

times_three = Multiplier(3)

print("Is times_three callable?", callable(times_three))

result = times_three(10)
print("Result of times_three(10):", result)
