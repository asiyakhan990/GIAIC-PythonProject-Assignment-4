class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or above."):
        super().__init__(message)

def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. You must be at least 18.")
    else:
        print("Age is valid. You may proceed.")

try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print("Custom Exception Caught:", e)
except ValueError:
    print("Please enter a valid integer for age.")
