from datetime import datetime

class Transaction:
    def __init__(self, narration, amount, transaction_type):
        self.date_time = datetime.now()
        self.narration = narration
        self.amount = amount
        self.transaction_type = transaction_type

    def __str__(self):
        return f"{self.date_time}: {self.transaction_type} of {self.amount}. Narration: {self.narration}"

class Account:
    def __init__(self, name, account_number):
        self.name = name
        self._balance = 0 
        self.deposits = [] 
        self.withdrawals = []  
        self.frozen = False
        self.loan = 0  
        self.transactions = []  
        self.min_balance = 1000
        self.account_number = account_number  

    def deposit(self, amount):
        if amount <= 0:
            return "Can only deposit positive amount"
        self.deposits.append(amount)  
        self._balance += amount  
        transaction = Transaction(f"You have deposited {amount}", amount, "Deposit")
        self.transactions.append(transaction)
        return f"Confirmed, new balance is {self.get_balance()}."
    
    def calculate_loan_limit(self):
        total_deposit = sum(self.deposits)
        loan_limt = total_deposit//3
        return loan_limt

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal must be positive"
        if self.get_balance() < self.min_balance:
            return "You cannot withdraw if your balance is less than minimum balance"
        if self.frozen:
            return "Your account is frozen"
        if amount <= self.get_balance():
            self.withdrawals.append(amount)  
            self._balance -= amount  
            transaction = Transaction(f"You have withdrawn {amount}", amount, "Withdrawal")
            self.transactions.append(transaction)
            return f"Your new balance is {self.get_balance()}"
        return "Insufficient funds."

    def transfer_funds(self, amount):
        if self.frozen:
            return "Account is frozen. Can't transfer funds."
        if amount <= 0:
            return "You can only transfer positive amount"
        if self._balance - amount < self.min_balance:
            return "Insufficient funds"
        
        self._balance -= amount
        transaction = Transaction(f"Transferred {amount} to another account", amount, "Transfer")
        self.transactions.append(transaction)
        return f"New balance is {self.get_balance()}"

    def get_balance(self):
        return self._balance  

    def get_loan(self, amount):
        if amount <= 0:
            return "You cannot borrow a negative amount"
        
        if amount <= self.calculate_loan_limit():
            self.loan += amount  
            self._balance += amount
            transaction = Transaction(f"You requested a loan of {amount}", amount, "Loan")
            self.transactions.append(transaction)
            return f"Your new balance is {self.get_balance()}"
        else:
            return "You are not eligible for the loan"

    def pay_loan(self, amount):
        if amount <= 0:
            return "Repayment amount must be positive."
        if amount <= self.loan:
            self.loan -= amount
            self._balance -= amount
            transaction = Transaction(f"Loan repaid: {amount}", amount, "Loan Repayment")
            self.transactions.append(transaction)
            return f"You repaid {amount} and your remaining loan is {self.loan}."
        else:
            excess_payment = amount - self.loan
            self._balance -= self.loan
            self.loan = 0  
            self._balance += excess_payment 
            transaction = Transaction(f"Loan repaid: {self.loan} (excess payment: {excess_payment})", self.loan, "Loan Repayment")
            self.transactions.append(transaction)
            return f"You repaid your loan. Excess payment of {excess_payment} has been deposited back to your account."

    def account_details(self):
        return f"Account owner is {self.name}, your balance is {self.get_balance()} and your loan is {self.loan}"

    def transfer_ownership(self, new_name):
        self.name = new_name
        return f"Account ownership changed to {self.name}"
    
    def statement(self):
        return "\n".join(str(transaction) for transaction in self.transactions)

    def interest(self):
        interest = self.get_balance() * 0.05
        self._balance += interest
        transaction = Transaction(f"Interest applied", interest, "Interest")
        self.transactions.append(transaction)
        return f"Your interest was {interest} and your new balance is {self.get_balance()}"

    def freeze(self):
        self.frozen = True
        return "Account has been frozen for security reasons"

    def unfreeze(self):
        self.frozen = False
        return "Account has been unfrozen"

    def close_account(self):
        self._balance = 0
        self.deposits.clear() 
        self.withdrawals.clear()
        self.loan = 0  
        self.transactions.clear()
        self.min_balance = 0