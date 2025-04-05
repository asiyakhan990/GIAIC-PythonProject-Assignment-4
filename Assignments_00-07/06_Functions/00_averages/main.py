def average(a, b):
    return (a + b) / 2

def main():
    first_input = input("Enter the first number: ")
    second_input = input("Enter the second number: ")

    num1 = float(first_input)
    num2 = float(second_input)

    result = average(num1, num2)

    print(f"The average of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()
