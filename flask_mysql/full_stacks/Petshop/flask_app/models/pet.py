from flask_app.config.mysqlconnection import connectToMySQL

class Pet:
    def __init__(self, data):
        self.id = data["id"]

        self.pet_name = data["pet_name"]
        self.tyoe = data["tyoe"]
        self.age = data["age"]
        
        self.created_at = data["created_at"]
        self.update_at = data["updated_at"]