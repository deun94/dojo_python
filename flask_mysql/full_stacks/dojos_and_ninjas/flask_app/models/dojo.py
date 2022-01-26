from sqlite3 import connect
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja
# connecting to our queries

# =====================================
# creting dojo class
# =====================================
class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.ninjas = []

    # ==================================
    # getting all dojo info
    # =======================
    @classmethod
    def show_all(cls):
        query = "SELECT * from dojos;"
        results = connectToMySQL("dojos_and_ninjas").query_db(query)

        # print(results)
        dojos = []

        for dojo_data in results: 

            dojos.append(cls(dojo_data))
        return dojos


# =========================================
# show one dojo
# ==================================
    @classmethod
    def one_dojo(cls, data):

        query = "SELECT * FROM dojos WHERE id = %(dojo_id)s;"

        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)

        print(results)

        return cls(results[0])
    
# =============================================
# creating new dojo
# ===========================================
    @classmethod
    def add_dojo(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        # remember the syntax is %()s NOT curly bracket

        results = connectToMySQL("dojos_and_ninjas").query_db(query, data)

        print(results)

        return results

# ==================================================
# Dojo with Ninjas
# ==================================================

# getting ninjas attached to selected dojo
    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(dojo_id)s;"
        # remember where to join and which data to pass in

        results = connectToMySQL("dojos_and_ninjas").query_db(query, data)

        dojo = cls(results[0])

        for row_data in results:

            ninja_data={
                "id" : row_data["ninjas.id"],
            # don't forget the id
                "first_name" : row_data["first_name"],
                "last_name" : row_data["last_name"],
                "age" : row_data["age"],

                "created_at" : row_data["ninjas.created_at"],
                "updated_at" : row_data["ninjas.updated_at"],
                # REMEMBER to specify specify
                "dojo_id" : row_data["dojo_id"]
                # needs to match exactly to the init of the other class data
            }
            dojo.ninjas.append( ninja.Ninja(ninja_data))
        return dojo


# for editing
    @classmethod
    def get_ninja_with_dojo(cls, data):
        query = "SELECT * FROM ninjas LEFT JOIN dojos ON ninjas.dojo_id = dojos.id WHERE ninjas.id = %(ninja_id)s;"

        results = connectToMySQL("dojos_and_ninjas").query_db(query, data)