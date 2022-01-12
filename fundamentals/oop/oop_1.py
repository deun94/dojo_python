class Car:
    manufacturer = "GNC"
    number_of_cars = 0
    all_cars = []
    #every instances in this Car has the same manufacturer

    #this would be a class attribute
    # def __init__(self, tank_size, color, year, make, model):
    def __init__(self, data):        
        #thanks to self each car now shares same attribute called tank size, but different tank size for eachself.
        self.tank_size = data["tank_size"] 
        # you still need to clarify

        # self.color = "Silver"
        #all car color deafults to silver
        self.color = data["color"]
        self.gallons = 0
        self.year = data["year"]
        self.make = data["make"]
        self.model = data["Model"]
    # ======================to change the number of cars in the ini
        Car.number_of_cars+= 1
        Car.all_cars.append(self)
        # increase by 1 everytime an instance is created
    #=======================================================
    #class methods here

    @classmethod
    def total_gallons(cls):
        total_gallons = 0

        for car in Car.all_cars:
            total_gallons += car.gallons
        return total_gallons

# ===========================static methods

    @staticmethod
    def enough_gas(total_gas, gas_needed):
        if total_gas < gas_needed:
            print("Sorry! Not enough fuel")
            return False
        else:
            print("enjoy your trip")
            return True

    def fill_tank(self):
        self.gallons = self.tank_size


    # def drive(self, miles):
    #     if(self.tank_size < miles):
    #         print("Not enough tank!")
    #     else: 
    #         self.tank_size -= miles
        #reducing individual tank size by miles travel

    
    def drive(self, miles):
        # if(self.gallons < miles):
        #     print("Not enough tank!")

        # we can call staticmethod here instead
        if Car.enough_gas(self.gallons, miles):
            self.gallons -= miles
        else: 
            # self.gallons -= miles
            print("check the gas tank!")

    def get_car_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}" )

subaru_data = {
    "tank_size": 18,
    "color": "Blue",
    "make": "Subaru",
    "Model": "Legacy",
    "year": 2019,
}


civic_data = {
    "tank_size": 12,
    "color": "Silver",
    "make": "Honda",
    "Model": "Civic",
    "year": 2002,
}
#data chunking
subaru = Car(subaru_data)
# tacoma = Car(tacoma_data)
civic = Car(civic_data)

# ==========================class attributes
print(subaru.manufacturer)
print(civic.manufacturer)

subaru.manufacturer = "Subaru"

print(subaru.manufacturer)
print(civic.manufacturer)

Car.manufacturer = "Honda"

print(subaru.manufacturer)
print(civic.manufacturer)

print(Car.number_of_cars)

# =========================methods

print(Car.all_cars)

# ===========================classmethod about gallons
subaru.fill_tank()
civic.fill_tank()

subaru.drive(5)
print(Car.total_gallons())

# [<__main__.Car object at 0x00000261B646FFD0>, <__main__.Car object at 0x00000261B646FFA0>]
# giving u a list of a memory location of the instances being created cannot easily be translated into easy english


#all instances of a Car but not yet defined
#okay now specifically defined as each tank size

# print(subaru.tank_size)
# # print(tacoma.tank_size)
# print(civic.tank_size)

# print(subaru.color)
# # print(tacoma.color)
# print(civic.color)

# subaru.color = "red"
# #only changes the print output but not the data in the dictionary
# print(subaru.color)



# #================================
# #method
# subaru.drive(5)
# print(subaru.tank_size)
# subaru.drive(5)
# print(subaru.tank_size)
# subaru.drive(5)
# print(subaru.tank_size)
# subaru.drive(5)
# print(subaru.tank_size)
# subaru.drive(5)
# print(subaru.tank_size)
# #not enuf tank and stuck at the tank size



# subaru.get_car_info()

