from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask import flash
from flask_app.models.user import User

class Recipe():
    def __init__(self, data):
        self.id = data["id"]

        self.name = data["name"]
        self.description = data["description"]
        self.instruction = data["instruction"]
        self.under_thirty = data["under_thirty"]
        self.date = data["date"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        
    # ===============================
    # validate recipe
    # =========================

    
    @staticmethod
    def validate_recipe(data):
        is_valid = True

        if len(data["name"]) < 3:
            flash("Recipe Name must be at least 3 characters long!")
            is_valid = False
        elif data["name"] < "":
            flash("Recipe Name is required!")
            is_valid = False

        if len(data["description"]) < 3:
            flash("Dog description must be at least 3 characters long!")
            is_valid = False
        elif data["description"] == "":
            flash("Recipe description is required!")
            is_valid = False
        
        if len(data["instruction"]) < 3:
            flash("Instructions must be at least 3 characters long for your recipe!")
            is_valid = False
        elif data["instruction"] == "":
            flash("Recipe instruction is required!")
            is_valid = False

        if data["under_thirty"] == "":
            flash("You must choose yes or no!")
            is_valid = False
        return is_valid


# =================================================================
# creating new recipe and uploading it to our database
# ==================================================================
    @classmethod
    def create_recipe(cls, data):
        query = """
        INSERT INTO recipes (name, description, instruction, under_thirty, date, updated_at, user_id) 
        VALUES (%(name)s,%(description)s,%(instruction)s, %(under_thirty)s, %(date)s, NOW(), %(user_id)s);"""

        results = connectToMySQL("recipes_schema").query_db(query, data)

        return results

    # ========================
    # getting all recipes
    # ========================
    @classmethod
    def get_recipe_user(cls, data):
        query = """
        SELECT * FROM recipes LEFT JOIN users ON recipes.user_id = users.id WHERE recipes.id = %(recipe_id)s;"""

        results = connectToMySQL("recipes_schema").query_db(query, data)

        # all_recipes = []
        
        # for row in results:

        #     recipe = cls(row)

        #     user_data = {
        #         "id": row["users.id"],

        #         "first_name": row["first_name"],
        #         "last_name": row["last_name"],
        #         "email": row["email"],
        #         "password": row["password"],

        #         "created_at": row["users.created_at"],
        #         "updated_at": row["users.updated_at"]
        #     }

        #     recipe.user = user.User(user_data)

        #     all_recipes.append(recipe)

        recipe = cls(results[0])

        user_data = {
            "id" : results[0]['id'],
            "first_name" : results[0]['first_name'],
            "last_name" : results[0]['last_name'],
            "email" : results[0]['email'],
            "password" : results[0]['password'],
            "created_at" : results[0]['created_at'],
            "updated_at" : results[0]['updated_at']
        }
        
        recipe.user = User(user_data)
        return recipe

# =======================================================
# viewing only one recipe via id
# ======================================================
    @classmethod
    def get_all_recipes(cls):
        query = """SELECT * FROM recipes"""

        results = connectToMySQL("recipes_schema").query_db(query)

        user_recipe = []

        for row in results:
            
            user_recipe.append(cls(row))

        return user_recipe

    @classmethod
    def view_one(cls, data):
        query = """
        SELECT * FROM recipes WHERE recipes.id = %(recipe_id)s;"""

        results = connectToMySQL("recipes_schema").query_db(query, data)
        
        recipe = cls(results[0])
        return recipe


# ======================================================
# editing recipe
# ===================================================
    @classmethod
    def update_recipe(cls, data):
        query = """UPDATE recipes SET name = %(name)s, description = %(description)s, instruction = %(instruction)s, under_thirty = %(under_thirty)s, date = %(date)s, updated_at = NOW() WHERE id = %(recipe_id)s;"""

        results = connectToMySQL("recipes_schema").query_db(query, data)
        

        return
    
    # ================================================================================
    # delete
    # =================================================================================

    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id = %(recipe_id)s;"

        results = connectToMySQL("recipes_schema").query_db(query, data)

        return