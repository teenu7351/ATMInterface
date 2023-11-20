class User:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.balance = 0
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
        else:
            print("Insufficient funds!")

    def transfer(self, amount, recipient):
        if amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transferred ${amount} to {recipient.user_id}")
        else:
            print("Insufficient funds!")

    def get_transaction_history(self):
        return self.transaction_history


class ATM:
    def __init__(self):
        self.users = {}

    def create_user(self, user_id, pin):
        new_user = User(user_id, pin)
        self.users[user_id] = new_user
        return new_user

    def authenticate_user(self, user_id, pin):
        if user_id in self.users and self.users[user_id].pin == pin:
            return self.users[user_id]
        else:
            return None


class ConsoleATM:
    def __init__(self):
        self.atm = ATM()
        self.current_user = None

    def start(self):
        print("Welcome to Console ATM!")
        user_id = input("Enter your user ID: ")
        pin = input("Enter your PIN: ")
1
        user = self.atm.authenticate_user(user_id, pin)
        if user:
            print("Authentication successful!")
            self.current_user = user
            self.show_menu()
        else:
            print("Authentication failed!")

    def show_menu(self):
        while True:
            print("\nATM Menu:")
            print("1. Transaction History")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Transfer")
            print("5. Quit")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.display_transaction_history()
            elif choice == "2":
                self.withdraw()
            elif choice == "3":
                self.deposit()
            elif choice == "4":
                self.transfer()
            elif choice == "5":
                print("Thank you for using Console ATM! Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

    def display_transaction_history(self):
        history = self.current_user.get_transaction_history()
        print("\nTransaction History:")
        for transaction in history:
            print(transaction)

    def withdraw(self):
        amount = float(input("Enter the amount to withdraw: "))
        self.current_user.withdraw(amount)

    def deposit(self):
        amount = float(input("Enter the amount to deposit: "))
        self.current_user.deposit(amount)

    def transfer(self):
        recipient_id = input("Enter the recipient's user ID: ")
        recipient = self.atm.authenticate_user(recipient_id, "")
        if recipient:
            amount = float(input("Enter the amount to transfer: "))
            self.current_user.transfer(amount, recipient)
        else:
            print("Recipient not found.")


# Sample usage
if __name__ == "__main__":
    console_atm = ConsoleATM()
    console_atm.start()
