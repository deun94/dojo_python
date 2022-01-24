from flask_app.config.mysqlconnection import connectToMySQL
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

    # ==================================
    # getting all dojo info
    # =======================
    @classmethod
    def show_all(cls):
        query = "SELECT * from dojos;"
        results = connectToMySQL("dojos_and_ninjas").query_db(query)

        print(results)
        dojos = []

        for dojo_data in results: 

            dojos.append(cls(dojo_data))
        return dojos
