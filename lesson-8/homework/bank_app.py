import os

class Account:
    def __init__(self, account_num, name, balance=0):
        self.account_num = account_num
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Account Number: {self.account_num}\nName: {self.name}\nBalance: ${self.balance:.2f}"
    
    def deposit(self, amount):
        """Deposit the money into the account"""
        if amount <= 0:
            print("Deposit should be positive")
            return False
        else:
            self.balance += amount
            return True
    
    def withdraw(self, amount):
        """Withdraw money from the account"""
        if amount <= 0:
            print("Withdraw money should be positive")
            return False
        if amount > self.balance:
            print("Insufficient balance")
            return False
        else:
            self.balance -= amount
            return True
    
    def save_to_file(self, file_name='account.txt'):
        """Save account details to the account file"""
        with open(file_name, 'a') as file:
            file.writelines(f"{self.account_num},{self.name},{self.balance}\n")


class Bank:
    def __init__(self, file_name='account.txt'):
        self.accounts = {}
        self.file_name = file_name
        self.load_from_file()  # Load accounts from file when the Bank object is created
    
    def generate_account_number(self):
        """Generate a unique account number."""
        account_num = len(self.accounts) + 1
        while account_num in self.accounts or self.is_account_num_in_file(account_num):
            account_num += 1
        return account_num

    def is_account_num_in_file(self, account_num):
        """Check if the account number exists in the file."""
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                return any(int(line.split(",")[0]) == account_num for line in file)
        return False

    def create_account(self, name, initial_dep):
        """Create a new account with the provided details."""
        if initial_dep < 0:
            print("Initial deposit must be non-negative.")
            return
        
        account_num = self.generate_account_number()
        new_account = Account(account_num, name, initial_dep)
        
        # Store the account in the dictionary
        self.accounts[account_num] = new_account
        print(f"Account created successfully! Account Number: {account_num}")
        new_account.save_to_file(self.file_name)  # Save account details to file

    def view_account(self, account_num):
        """View account details for a given account number."""
        account = self.accounts.get(account_num)
        if account:
            print(account)
        else:
            print("Account not found.")

    def deposit(self, account_num, amount):
        """Deposit money into an account."""
        account = self.accounts.get(account_num)
        if account:
            if account.deposit(amount):
                print(f"${amount:.2f} deposited successfully! New balance: ${account.balance:.2f}")
                account.save_to_file(self.file_name)  # Save the updated account
            else:
                print("Deposit failed.")
        else:
            print("Account not found.")

    def withdraw(self, account_num, amount):
        """Withdraw money from an account."""
        account = self.accounts.get(account_num)
        if account:
            if account.withdraw(amount):
                print(f"${amount:.2f} withdrawn successfully! New balance: ${account.balance:.2f}")
                account.save_to_file(self.file_name)  # Save the updated account
            else:
                print("Withdrawal failed.")
        else:
            print("Account not found.")

    def load_from_file(self, filename="account.txt"):
        """Load account details from a text file."""
        if os.path.exists(filename):
            with open(filename, "r") as file:
                for line in file:
                    account_num, name, balance = line.strip().split(",")
                    account_num = int(account_num)
                    balance = float(balance)
                    self.accounts[account_num] = Account(account_num, name, balance)


def main():
    bank = Bank(file_name="account.txt")  # Set file_name as 'account.txt'

    while True:
        print("\n----- Bank Menu -----")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == "1":
            name = input("Enter account holder's name: ")
            initial_dep = float(input("Enter initial deposit: $"))
            bank.create_account(name, initial_dep)
        
        elif choice == "2":
            account_num = int(input("Enter account number to view: "))
            bank.view_account(account_num)
        
        elif choice == "3":
            account_num = int(input("Enter account number to deposit into: "))
            deposit_amount = float(input("Enter deposit amount: $"))
            bank.deposit(account_num, deposit_amount)
        
        elif choice == "4":
            account_num = int(input("Enter account number to withdraw from: "))
            withdraw_amount = float(input("Enter withdrawal amount: $"))
            bank.withdraw(account_num, withdraw_amount)
        
        elif choice == "5":
            print("Thank you for using the bank!")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
