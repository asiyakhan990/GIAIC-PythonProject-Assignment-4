class Counter:
    object_count = 0

    def __init__(self):
        Counter.object_count += 1

    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.object_count}")


if __name__ == "__main__":
    obj1 = Counter()
    obj2 = Counter()
    obj3 = Counter()

    Counter.display_count()
