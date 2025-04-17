def in_range(n, low, high):
    """ Returns True if n is between low and high, inclusive. """
    return low <= n <= high

def main():
    number = int(input("Enter a number: "))
    low = int(input("Enter the lower limit: "))
    high = int(input("Enter the upper limit: "))
    
    if in_range(number, low, high):
        print("True")
    else:
        print("False")

if __name__ == '__main__':
    main()