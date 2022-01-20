class BankAccount:
    # don't forget to add some default values for these parameters!
    balance = 0
    num_of_accounts = 0
    accounts = []

    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.num_of_accounts += 1
        BankAccount.accounts.append(self)

# classmethod here =============================================
    @classmethod

    def print_accounts(cls):
        for account in cls.accounts:
            account.yield_interest()
            account.display_account_info()

    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self


    def withdraw(self, amount):
        # your code here
        if (amount < self.balance):
            self.balance -= amount
            return self
        elif(amount > self.balance):
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self
        
        # else
        #     print("No Money!")

    def display_account_info(self):
        # your code here
        print(f"Balance : ${self.balance}")
        return self

    def yield_interest(self):
        # your code here
        self.interest = 0
        if(self.balance > 0):
            self.interest = self.int_rate * self.balance
            print(f"Your interst is : {self.interest}")
        return self

one = BankAccount(0.02, 0)
two = BankAccount(0.03, 0)

one.deposit(500).deposit(500).deposit(500).withdraw(500).yield_interest().display_account_info()
two.deposit(1000).deposit(1000).withdraw(200).withdraw(200).withdraw(200).withdraw(200).yield_interest().display_account_info()

BankAccount.print_accounts()
