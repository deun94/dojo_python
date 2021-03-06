from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo
# connecting to our queries

# =====================================
# creting ninja class
# =====================================
class Ninja:
    def __init__(self, data):
        self.id = data["id"]
        # don't forget the id
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.dojo_id = data["dojo_id"]

    @classmethod
    def get_ninja(cls):

        query = "SELECT * FROM ninjas;"

        results = connectToMySQL('dojos_and_ninjas').query_db(query)

        print(results)
        ninjas = []

        for ninja_data in results:

            ninjas.append( cls(ninja_data) )
        return ninjas


# ==========================================
# adding new ninja
# =================================

    @classmethod
    def add_ninja(cls, data):
        query = """INSERT INTO ninjas (first_name, last_name, age, created_at, dojo_id)
        VALUES (%(first_name)s, %(last_name)s, %(age)s, NOW(), %(dojo_id)s);"""

        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)

        print(results)

        return results

# # ================================================
# # editing one ninja info
# # ===============================================
# for editing
    @classmethod
    def get_ninja_with_dojo(cls, data):
        query = "SELECT * FROM ninjas LEFT JOIN dojos ON ninjas.dojo_id = dojos.id WHERE ninjas.id = %(ninja_id)s;"

        results = connectToMySQL("dojos_and_ninjas").query_db(query, data)

        ninja = cls(results[0])

        dojo_data = {
            "id" : results[0]["dojos.id"],
            # don't forget the id
            "name" : results[0]["name"],

            "created_at" : results[0]["dojos.created_at"],
            "updated_at" : results[0]["dojos.updated_at"]
        }
        ninja.dojo = dojo.Dojo(dojo_data)

        return ninja

    @classmethod
    def update_ninja(cls, data):
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s, updated_at = NOW(), dojo_id = %(dojo_id)s;"

        results = results = connectToMySQL("dojos_and_ninjas").query_db(query, data)

        return

# ===========================================
# delete one ninja info
# ===========================================

    @classmethod
    def delete_ninja(cls, data):

        query = """DELETE FROM ninjas 
        WHERE id = %(ninja_id)s;"""

        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)


        print(results)

        return
        