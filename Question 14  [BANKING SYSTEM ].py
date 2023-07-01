""""Create a python class called Bank Account with attribute balance, date of opening and customer name, and methods like deposit, withdraw check balance and customer details

    i. The deposit method should return the amount deposit

    ii. The withdraw method return insufficient balance if count balance is less than amont to be withdrawn else it should return the amount that has been withdrawn

    The check balance method should print the current balance. 

    iv. The customer details method should print customer name, account number, date of account opening and balance"""



class BankAccount:
    def __init__(self, account_number, customer_name):
        self.account_number = account_number
        self.balance = 0
        self.date_of_opening = "2022-01-01"  # You can use the current date here
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        return amount

    def withdraw(self, amount):
        if self.balance < amount:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return amount

    def check_balance(self):
        return self.balance

    def customer_details(self):
        return f"Customer Name: {self.customer_name}\nAccount Number: {self.account_number}\nDate of Account Opening: {self.date_of_opening}\nBalance: {self.balance}"


# Example of usage:

account = BankAccount("123456789", "John Doe")

print(account.deposit(3500))  # Output: 3500

print(account.withdraw(500))  # Output: 500

print(account.check_balance())  # Output: 500

print(account.customer_details())




















