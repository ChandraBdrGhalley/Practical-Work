##########################################################################################################
#Name: Chandra Bdr Ghalley
#Department: B.E First Year Electrical Engineering
#Student ID: 02230057
#####################################
#            References
#https://www.geeksforgeeks.org/python-program-to-create-bankaccount-class-with-deposit-withdraw-function/
#https://www.freecodecamp.org/news/how-to-build-an-online-banking-system-python-oop-tutorial/
#https://youtu.be/BRssQPHZMrc?si=Totx1cnORqDAFyVw
#https://youtu.be/xTh-ln2XhgU
#https://pythonmania.org/python-program-for-bank-account-using-class/
##########################################################################################################

import random

class Account:
    def __init__(self, account_number, password, account_type):
        self.account_number = account_number
        self.password = password  # Store password directly (not secure)
        self.account_type = account_type
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Invalid amount or insufficient funds.")

    def transfer(self, amount, target_account):
        if 0 < amount <= self.balance:
            self.balance -= amount
            target_account.balance += amount
            print(f"Transferred ${amount:.2f} to account {target_account.account_number}.")
        else:
            print("Insufficient funds or invalid amount.")

    def check_balance(self):
        print(f"Current balance: ${self.balance:.2f}")

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_type):
        account_number = str(random.randint(100000, 999999))
        password = str(random.randint(1000, 9999))
        self.accounts[account_number] = Account(account_number, password, account_type)
        print(f"Account created. Account Number: {acc_num}, Password: {pwd}")

    def login(self, account_number, password):
        account = self.accounts.get(account_number)
        if account and account.password == password:
            print("Login successful.")
            return account
        print("Incorrect account number or password.")
        return None

def main():
    bank = Bank()

    while True:
        choice = input("\n1. Open Account\n2. Login\n3. Exit\nEnter your choice: ")

        if choice == "1":
            account_type = input("Enter account type (Personal/Business): ")
            if account_type in ["Personal", "Business"]:
                bank.create_account(account_type)
            else:
                print("Invalid account type.")
        elif choice == "2":
            account_number = input("Enter account number: ")
            password = input("Enter password: ")
            account = bank.login(account_number, password)
            if account:
                while True:
                    user_choice = input("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Transfer\n5. Logout\nEnter your choice: ")
                    if user_choice == "1":
                        account.check_balance()
                    elif user_choice == "2":
                        account.deposit(float(input("Enter amount to deposit: ")))
                    elif user_choice == "3":
                        account.withdraw(float(input("Enter amount to withdraw: ")))
                    elif user_choice == "4":
                        target_account_number = input("Enter target account number: ")
                        target_account = bank.accounts.get(target_account_number)
                        if target_account:
                            account.transfer(float(input("Enter amount to transfer: ")), target_account)
                        else:
                            print("Target account does not exist.")
                    elif user_choice == "5":
                        print("Logged out successfully.")
                        break
                    else:
                        print("Invalid choice. Please select a valid option.")

        elif choice == "3":
            print("Exiting the application. Thank you!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
