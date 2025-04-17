inventory = {
    "apple": 500,
    "banana": 150,
    "orange": 0,
    "grape": 75
}

def num_in_stock(fruit):
    return inventory.get(fruit.lower(), 0)

def main():
    fruit = input("Enter a fruit: ").strip().lower()
    stock = num_in_stock(fruit)
    
    if stock > 0:
        print("This fruit is in stock! Here is how many:")
        print(stock)
    else:
        print("This fruit is not in stock.")

if __name__ == '__main__':
    main()
