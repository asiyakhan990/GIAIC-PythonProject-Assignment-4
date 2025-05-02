class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit


c = 25
f = TemperatureConverter.celsius_to_fahrenheit(c)
print(f"{c}°C is equal to {f}°F")
