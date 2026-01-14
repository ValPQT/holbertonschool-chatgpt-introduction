#!/usr/bin/python3
"""
checkbook.py

A simple checkbook application that allows a user to:
- deposit money
- withdraw money
- check balance
- exit the program

The program includes error handling to prevent crashes
from invalid user input.
"""

class Checkbook:
    """
    A class representing a simple checkbook.
    """

    def __init__(self):
        """
        Initializes the checkbook with a balance of 0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Adds money to the balance.

        :param amount: float, amount to deposit
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Removes money from the balance if funds are sufficient.

        :param amount: float, amount to withdraw
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Prints the current balance.
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main loop of the program.
    Handles user input and calls appropriate Checkbook methods.
    """
    cb = Checkbook()

    while True:
        action = input(
            "What would you like to do? (deposit, withdraw, balance, exit): "
        ).lower()

        if action == 'exit':
            print("Goodbye!")
            break

        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                if amount < 0:
                    print("Amount must be positive.")
                else:
                    cb.deposit(amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")

        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                if amount < 0:
                    print("Amount must be positive.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")

        elif action == 'balance':
            cb.get_balance()

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
