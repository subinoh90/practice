# class account
# class bank
# class manager
# class customer

class Bank:
    def __init__(self, balance=1000):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited: ${amount:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Amount withdrawn: ${amount:.2f}")

    def show_balance(self):
        print(f"Starting balance: ${self.balance:.2f}")

def main():
    bank = Bank()
    actions = {'d': 'deposit', 'w': 'withdraw', 's': 'show_balance', 'x': 'exit'}

    action = input("Start banking (deposit/withdraw/showbalance/exit): ")
    while action != 'x':
        if action == 's':
            bank.show_balance()
        elif action in ['d', 'w']:
            amount = float(input("Amount to deposit: $" if action == 'd' else "Amount to withdraw: $"))
            if action == 'd':
                bank.deposit(amount)
            else:
                bank.withdraw(amount)
        else:
            print("Invalid choice")

        action = input("Continue banking (d/w/s/x): ")

    print("Exiting the system...")

if __name__ == "__main__":
    main()
