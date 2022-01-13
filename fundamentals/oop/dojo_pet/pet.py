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