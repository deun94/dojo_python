class Pet:
    # implement __init__( name , type , tricks ):
    def __init__(self, data):
        self.name = data["name"]
        self.type = data["type"]
        self.tricks = data ["tricks"]
        self.sound = data["sound"]
        self.health = 100
        self.energy = 50

    # implement the following methods:
    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        print(f"{self.name} is sleeping! His energy is now {self.energy}")
        return self
    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name} has been fed! His energy is now {self.energy} and his health is {self.health}")
        return self
    # play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        print(f"Walking {self.name}! His health is now {self.health}")
        return self
    # noise() - prints out the pet's sound
    def noise(self):
        print(self.sound)

    def pet_Info(self):
        print(f"This is {self.name}. He is a {self.type}. He can {self.tricks[0]}")

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



rambo_data = {
    "name" : "Rambo",
    "type" : "Miniature Schnauzer",
    "tricks" : ["be gentle", "have nice mustache"],
    "sound": "Worh Worh"
}

gura_data = {
    "name" : "Gura",
    "type" : "Mixed Breed",
    "tricks" : ["roll over", "jiggle belly", "glare"],
    "sound": "OOF OOF"
}

rambo = Pet(rambo_data)
gura = Pet(gura_data)
# pass this instance directly into the data structure to associate


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

# rambo.sleep().eat().eat().play()

# print(rambo.noise()) ->will return none after noise because it is two print statements
# rambo.noise()
# rambo.pet_Info()
# tom.my_Info()
tom.walk().feed(10).bathe().feed(90).feed(10)