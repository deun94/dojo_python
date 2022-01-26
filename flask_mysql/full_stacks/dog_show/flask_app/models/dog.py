from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
# from flask_app import app
from flask import flash
from flask_app.models import owner

class Dog():
    def __init__(self, data):
        self.id = data["id"]

        self.name = data["name"]
        self.breed = data["breed"]
        self.age = data["age"]
        self.owner_id = data["owner_id"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.owner = {}
        # empty dictionary instead of list because each dog has only one owner
        # placeholder we will replace empty dict with a proper owner instance as we parse


    @staticmethod
    def validate_dog(data):
        is_valid = True

        if len(data["name"]) < 2:
            flash("Dog name must be at least 2 characters long!")
            is_valid = False

        if len(data["breed"]) < 3:
            flash("Dog breed must be at least 3 characters long!")
            is_valid = False
        
        if data["age"] == "":
        # if len(data["age"]) <= 0
            flash("Please enter an age for your dog!")
            is_valid = False

        elif int(data["age"]) <3:
            flash("Must be at least 3 years of age or older to participate")
            is_valid = False


        return is_valid
    
    @classmethod
    def create_dog(cls, data):
        query = """
        INSERT INTO dogs (name, breed, age, owner_id, created_at, updated_at) 
        VALUES (%(name)s,%(breed)s,%(age)s, %(owner_id)s, NOW(), NOW());"""

        results = connectToMySQL("dogshow_schema").query_db(query, data)

        return results
    
    # ===================================
    # dog info
    # ==================================
    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM dogs LEFT JOIN owners ON dogs.owner_id = owners.id;"""

        results = connectToMySQL("dogshow_schema").query_db(query)
        # we don't have data so don't put in data

        # instances of a dog and each has instance of owner attached to it

        all_dogs = []

        for row in results:
            # dog and then owner following in the row
            # creating instance of our dog based on row data
            dog = cls(row)

            owner_data = {
                "id": row["owners.id"],

                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "password": row["password"],

                "created_at": row["owners.created_at"],
                "updated_at": row["owners.updated_at"],
            }

            dog.owner = owner.Owner(owner_data)
            # referencing to the empty dict
            # creating instance of the owner 
            # and add a new instance of the gathered owner to replace the empty dict

            # need to attach the owner data collected to the dog
            all_dogs.append(dog)

            # make sure spacings are good keep the append in the loop, then outside of the loop
            # return the finished list
        return all_dogs

    @classmethod
    def get_dog_with_owner(cls, data):
        query = """
        SELECT * FROM dogs LEFT JOIN owners ON dogs.owner_id = owners.id
        WHERE dogs.id = %(dog_id)s"""

        results = connectToMySQL("dogshow_schema").query_db(query, data)
        # pass in data

        dog = cls(results[0])
        # list to the first position to created our outer instance
        # go to the same spot and get the owner info

        owner_data = {
            "id": results[0]["owners.id"],

            "first_name": results[0]["first_name"],
            "last_name": results[0]["last_name"],
            "email": results[0]["email"],
            "password": results[0]["password"],

            "created_at": results[0]["owners.created_at"],
            "updated_at": results[0]["owners.updated_at"],
        }
        dog.owner = owner.Owner(owner_data)
        return dog


    @classmethod
    def update_dog_info(cls, data):
        query = "UPDATE dogs SET name = %(name)s,breed = %(breed)s, age = %(age)s, updated_at = NOW() WHERE id = %(dog_id)s;"

        results = connectToMySQL("dogshow_schema").query_db(query, data)

        return 
    

    # ==============delete
    @classmethod
    def delete_dog_info(cls, data):
        query = "DELETE FROM dogs WHERE id = %(dog_id)s;"

        results = connectToMySQL("dogshow_schema").query_db(query, data)

        return