def print_divisors(num):
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)

def main():
    number = int(input("Enter a number: "))
    print(f"Here are the divisors of {number}")
    print_divisors(number)

if __name__ == '__main__':
    main()
