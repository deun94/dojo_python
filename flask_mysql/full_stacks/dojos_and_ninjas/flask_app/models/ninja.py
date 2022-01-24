from flask_app.config.mysqlconnection import connectToMySQL
# connecting to our queries

# =====================================
# creting ninja class
# =====================================
class Ninja:
    def __init__(self, data):
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.dojo_id = data["dojo_id"]
