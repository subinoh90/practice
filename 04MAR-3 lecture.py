class Bank:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount ${amount:.2f} deposited")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Amount ${amount:.2f} withdrawn")

def main():
    bank = Bank()
    while True:
        action = input("Enter action (deposit, withdraw, exit): ").strip().lower()
        if action == 'exit':
            break
        elif action in ['deposit', 'withdraw']:
            amount = float(input(f"Amount to {action} $ "))
            if action == 'deposit':
                bank.deposit(amount)
            else:
                bank.withdraw(amount)
        else:
            print("Invalid action. Please choose 'deposit', 'withdraw', or 'exit'.")

if __name__ == "__main__":
    main()
