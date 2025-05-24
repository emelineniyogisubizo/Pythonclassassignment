class Account:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.deposits = [] 
        self.withdrawals = []  
        self.frozen = False
        self.loan = []
        self.transaction =[]
        self.min_balance = 1000
        self.new_account = []


    def deposit(self, amount):
        if amount <= 0:
            return "can only deposit positive amount"
        self.deposits.append(amount)  
        self.balance += amount  
        self.transaction.append(f"You have deposited {amount}")
        return f"Confirmed,new balance is {self.balance}."

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal must be positive"
        if self.balance < self.min_balance:
            return "You can not withdraw if your balance is less than minimum balance"
        if amount <= self.balance:
            self.withdrawals.append(amount)  
            self.balance -= amount  
            self.transaction.append(f"You have withdrawn {amount}") 
            return f"your new balnce is {self.balance}"
        if amount > self.balance:
            return "Insufficient funds."

        
    def transfer_funds(self, amount):
        if amount <=0:
            return "You can only transfer positive amount"
        self.new_account.append(amount)
        self.balance -= amount
        self.transaction.append(f"Transferred {amount} to {self.new_account}")
        return f"New balance is {self.balance}"
        

    def get_balance(self):
        return f" Your current balance is {self.balance}"

    def get_loan(self, amount):
        if amount <= 0:
            return "You can not borrow negative amount"
        self.loan.append(amount)
        self.balance += amount
        self.transaction.append(f"You requested a loan of {amount}")
        return f"Your new balance is {self.balance}"

    def pay_loan(self, amount):
        if amount <= 0:
            return "You can repay negative amount"
        for i in self.loan:
            i -= amount
            self.balance -= amount
            self.transaction.append(f"You paid aloan of {amount}")
            return f"Your new balance is {self.balance}"

    def account_details(self):
        return f"Acount owner is {self.name},your balance is {self.balance} and your loan is {self.loan}"

    def transfer_ownership (self, new_name):
        self.name = new_name
        return f"Account owner ship changed to {self.name}"
    
    def statement (self):
        for i in self.transaction:
            return f"Your transaction is {self.transaction}"

    def interest (self):
        interest = self.balance * 0.05
        self.balance += interest
        self.transaction.append(f"Your interest is applied to amount is {interest}")
        return f"Your interest was {interest}and your new balance is {self.balance}"

    def freez(self):
        self.frozen = True
        return f"Account has been frozen for security reason"

    def un_freeze(self):
        self.frozen = False
        return f"Account has been unfrozen"

    def close_account(self):
        self.balance = 0
        self.deposits.clear() 
        self.withdrawals.clear()
        self.loan.clear()
        self.transaction.clear()
        self.min_balance = 0