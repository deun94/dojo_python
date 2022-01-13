from . import pet

class Ninja:
    # implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, data):
        self.first_name= data["first_name"]
        self.last_name = data["last_name"]
        self.treats = data["treats"]
        self.pet_food= data["pet_food"]
        self.pet= data["pet"]

    
    # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        return self
    # feed() - feeds the ninja's pet invoking tssssshe pet eat() method
    def feed(self, amount):
        # total_food = self.pet_food["salmon"]
        food_type = self.pet_food["type"]
        if (self.pet_food["amount"] <= 0):
            print("Oh no! need more food")
        else:
            self.pet.eat()
            self.pet_food["amount"] -= amount
            left_over = self.pet_food["amount"]
            print(f"Feeding him {food_type} flavor pet food. Food is now {left_over}")
        return self
    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.noise()
        return self

    def my_Info(self):
        print(f"My Name is {self.first_name} {self.last_name}")

tom_data = {
    "first_name" : "Tom",
    "last_name" : "Riddle",
    "treats" : ["Pig ears", "liver", "gizzards"],
    "pet_food" : {
                "type": "salmon", 
                "amount": 100},
    "pet" : rambo,
}

kai_data = {
    "first_name" : "Kai",
    "last_name" : "Elias",
    "treats" : ["tomato", "cucumber", "stick"],
    "pet_food" : {
                "type": "chicken", 
                "amount": 50
                },
                # to make my life easier.. cuz you have same keys and different values 
    "pet" : gura,
}

tom = Ninja(tom_data)
kai = Ninja(kai_data)

print(locals)