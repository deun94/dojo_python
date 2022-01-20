class Car:
    # CLASS ATTRIBUTES
    manufacturer = "GNC"
    number_of_cars = 0
    all_cars = []
    # INIT METHODS/INSTACE ATTRIBUTES
    def __init__(self, data):        
        self.tank_size = data["tank_size"] 
        self.color = data["color"]
        self.gallons = 0
        self.year = data["year"]
        self.make = data["make"]
        self.model = data["Model"]

        Car.number_of_cars+= 1
        Car.all_cars.append(self)

    #=======================================================
    #class methods here

    @classmethod #decorater
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


    def drive(self, miles):
        if Car.enough_gas(self.gallons, miles):
            self.gallons -= miles
        else:
            print("Looks like a nice stay at home today!")

    
    # def drive(self, miles):
    #     # if(self.gallons < miles):
    #     #     print("Not enough tank!")

    #     # we can call staticmethod here instead
    #     if Car.enough_gas(self.gallons, miles):
    #         self.gallons -= miles
    #     else: 
    #         # self.gallons -= miles
            # print("check the gas tank!")

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

# driver class NEW CLASS
class Driver:
    def __init__(self, data, cars):
        self.name = data["name"]
        self.age = data["age"]
        # self.car = data["car"] for one car

        self.cars = cars
    
    # def car_info(self):
    #     self.car.get_car_info()

    # show car info with multiple cars

    def drive(self, miles):
        # need to follow the same parameters
        print(f"Driver : {self.name}, is going for a ride")
        self.car.drive(miles)

    def get_gas(self):
        self.car.fill_tank()
    
    def check_fuiel(self):
        print(f"The current Fuel level is  {self.car.gallons}")

driver1_data = {
    "name" : "Steve",
    "age" : 27,
    # "car" : subaru
}

driver1 = Driver(driver1_data, [civic, subaru])
print(driver1)
print(driver1.car.color)

driver1.drive(4)
