import datetime

class BankAccount:
    def __init__(self, account_number, balance, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.openingdate = datetime.date.today()
        self.customer_name = customer_name
        
    def deposit(self, amount):
        self.amount = amount
        return amount
        
    def withdraw(self, amount):
        self.amount = amount
        if self.balance < amount:
            return "insufficient"
        else:
            self.balance == amount
            return "sufficient funds"
            
    def check_balance(self):
        self.amount = balance + depositedamount
        return self.amount
        
    def customer_details(self):
        print("Customer Name:", self.customer_name)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)
        print("Total:", self.amount)
        print("Opening Date:", self.openingdate)

customer_name = input("Input your name: ")
account_number = input("Input your account number: ")
balance = float(input("Input your balance: "))
account = BankAccount(account_number, balance, customer_name)

depositedamount = float(input("Input amount to deposit: "))
print("Amount deposited:", account.deposit(depositedamount))

withdrawamount = float(input("Input amount to withdraw: "))
print("Amount withdrawn:", account.withdraw(withdrawamount))

account.check_balance()
account.customer_details()
