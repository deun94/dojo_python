class User:

    # starting_balance = 0

    def __init__(self, data):
        self.name = data["name"]
        self.balance = data["balance"]
    
    def make_deposit(self, deposit):
        print(f"Your Balance Was {self.balance}")
        self.balance += deposit
        print(F"Successful Deposit your balance is now {self.balance}")
        return self
    
    def make_withdrawal(self, withdraw):
        print(f"Your Balance Was {self.balance}")
        self.balance -= withdraw
        print(f"Successful Withdrawal your balance is now {self.balance}")
        return self

    def display_user_balance(self):
        print (f"User : {self.name} | Current Balance : {self.balance}")
        return self

    def transfer_balance(self, other, balance):
        self.balance -= balance
        other.balance += balance
        print(f"{self.name} has sent {balance} Dollars to {other.name}!")
        # print(f"Sender : {self.name} , Current Balance : {self.balance}")
        # print(f"Sender : {other.name} , Current Balance : {other.balance}")
        self.display_user_balance()
        other.display_user_balance()
        return "Finish"


tom_data = {
    "name" : "Tom",
    "balance" : 2000,
}

jon_data = {
    "name" : "Jon",
    "balance" : 1500,
}

carl_data = {
    "name" : "Carl",
    "balance" : 3000,
}

#can you incorportate random numbers here 

tom = User(tom_data)
jon = User(jon_data)
carl = User(carl_data)



tom.make_deposit(2000).make_deposit(2000).make_withdrawal(500).display_user_balance()

jon.make_deposit(100).make_deposit(500).make_withdrawal(300).make_withdrawal(500).display_user_balance()


carl.make_deposit(1000).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100).display_user_balance()



tom.transfer_balance(carl, 1000)