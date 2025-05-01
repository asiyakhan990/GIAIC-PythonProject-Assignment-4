class Bank:
    bank_name = "Default Bank"

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display_info(self):
        print(f"Bank: {Bank.bank_name}")
        print(f"Account Holder: {self.account_holder}")

if __name__ == "__main__":
    bank1 = Bank("Alice")
    bank2 = Bank("Bob")

    print("Before Changing Bank Name:")
    bank1.display_info()
    bank2.display_info()

    Bank.change_bank_name("Global Bank")

    print("\nAfter Changing Bank Name:")
    bank1.display_info()
    bank2.display_info()
