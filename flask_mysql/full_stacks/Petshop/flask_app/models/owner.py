from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import pet
# importing pet file it self

class Owner:
    db = "owners_pets_schema"
    def __init__(self, data):
        self.id = data["id"]

        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        
        self.created_at = data["created_at"]
        self.update_at = data["updated_at"]
        
        self.pets = []

        # the loop in owners_with _pets will only go over the data defined here  in the for loop
        # only in the project level
        # does not change the database itself


    @classmethod
    def owners_with_pets(cls):
        query = "SELECT * FROM owners LEFT JOIN pets on owners.id = pets.owner_id;"
        results = connectToMySQL(cls.db).query_db(query)
        print(results)

        owners = []
        owner_ids =[]

        for data in results:
            if data["id"] not in owner_ids:
                owner_ids.append(data['id'])
                owners.append(cls(data))

            pet_data = {
                "id": data["pets.id"],
                "pet_name" : data["pet_name"],
                "tyoe" : data["tyoe"],
                "age" : data["pets.age"],
                "created_at" : data["pets.created_at"],
                "updated_at" : data["pets.updated_at"],
                "owner_id" : data["owner_id"]
            }
            owners[len(owners)-1].pets.append(pet.Pet(pet_data))
            # how to figure how who to attach the given pet data
            # len -1 because of the index rule (starting at 0) says most recent owner until we find another id
            # pet.Pet(pet_data) is saying In pet py file, goto PET class, and get the pet_data in there
        return owners
    

    @classmethod
    def get_one_owner(cls, data):
        query = "SELECT * FROM owners LEFT JOIN pets ON owners.id = pets.owner_id WHERE owners.id = %(owner_id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)

        owner = cls(results[0])
        # singular instance from our list

        for pet_info in results:
            pet_data = {
                "id": data["pets.id"],
                "pet_name" : data["pet_name"],
                "tyoe" : data["tyoe"],
                "age" : data["pets.age"],
                "created_at" : data["pets.created_at"],
                "updated_at" : data["pets.updated_at"],
                # because user data also has these fields because they appear more than once. specify by ___
                "owner_id" : data["owner_id"]
            }
            
            owner.pets.append(pet.Pet(pet_data))
        
        return owner