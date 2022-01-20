class BankAccount:
    # don't forget to add some default values for these parameters!
    # balance = 0
    # savings
    # accounts = []
    # different accounts associated with each user
    number_of_accounts = 0
    all_accounts = ["checking", "saving"]

    def __init__(self, data, accounts): 
        self.type = data["type"]
        self.int_rate = data["int_rate"]
        self.balance = data["balance"]

        BankAccount.number_of_accounts +=1
        BankAccount.all_accounts.append(self)


    @classmethod
        def print_all_account_info(cls):
            for account in BankAccount.all_accounts:
                # print (f"forthis account checking & saving you have this amount 1& 2 and the owner of the account is the user 

    def deposit(self, amount):

        self.balance += amount
        return self

    def withdraw(self, amount):

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

        print(f"Balance : ${self.balance}")
        return self

    def yield_interest(self):
        # your code here
        self.interest = 0
        if(self.balance > 0):
            self.interest = self.int_rate * self.balance
            print(f"Your interst is : {self.int_rate}")
        return self

# ---------------------------------User class
class User:

    # starting_balance = 0

    def __init__(self, name, accounts):
        self.name = name
        # self.balance = data["balance"]
        # self.account = BankAccount(0.02, 0)

        # for multiple accounts for one user
        self.accounts = accounts
        

    
    def make_deposit(self, amount, account):
        self.account.deposit(amount)
        print(F"Successful Deposit your balance is now {self.account.balance}")
        return self
    
    def make_withdrawal(self, amount, account):

        # we want to be able to pass the parameters because you need the arguments
        self.withdraw(amount)
        print(f"Successful Withdrawal your balance is now {self.balance}")
        return self

    def display_user_balance(self):

        print (f"User : {self.name} | Current Balance : $ {self.balance}")
        return self

    # def transfer_balance(self, other):
    #     self.account.balance -= balance
    #     other.account.balance += balance
    #     print(f"{self.name} has sent {balance} Dollars to {other.name}!")
    #     # print(f"Sender : {self.name} , Current Balance : {self.balance}")
    #     # print(f"Sender : {other.name} , Current Balance : {other.balance}")
    #     self.display_user_balance()
    #     other.display_user_balance()
    #     return "Finish"


# tom_data = {
#     "name" : "Tom",
#     "balance" : 2000,
# }

# jon_data = {
#     "name" : "Jon",
#     "balance" : 1500,
# }

# carl_data = {
#     "name" : "Carl",
#     "balance" : 3000,
# }

#can you incorportate random numbers here 



checking_data = {
    "type" : "checkings",
    "int_rate" : 0.05,
    "balance" : 0,
}
checking = BankAccount(checking_data)

saving_data = {
    "type" : "savings",
    "int_rate" : 0.02,
    "balance": 1000
}

saving = BankAccount(saving_data)
# tom.transfer_balance(carl, 1000)

tom = User("Tom", [checking, saving])
jon = User("John", [checking, saving])
carl = User("Carl", [checking, saving])


tom.make_deposit(2000).make_deposit(2000).make_withdrawal(500).display_user_balance()
jon.make_deposit(100).make_deposit(500).make_withdrawal(300).make_withdrawal(500).display_user_balance()
carl.make_deposit(1000).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100).display_user_balance()

tom.make_deposit(2000, checking).display_user_balance()



