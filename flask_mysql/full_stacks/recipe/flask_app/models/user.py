from flask_app import app
from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask import flash
# from flask_app.models.recipe import Recipe

import re

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data["id"]

        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.recipes = []
# ====================================
# validating registration data
# ====================================
    @staticmethod
    def validate_user(data):
        is_valid = True # we assume this is true

        if len(data['first_name']) < 2:
            flash("First Name must be at least 2 characters.")
            is_valid = False
            
        if len(data['last_name']) < 2:
            flash("Last Name must be at least 2 characters.")
            is_valid = False
            
        if not EMAIL_REGEX.match(data["email"]):
            flash("Invalid email address!")
            is_valid = False

        if User.get_by_email(data):
            flash("Email already in use! Please register new email or login!")
            is_valid = False

        if data["password"] != data["pass_conf"]:
            flash("Passwords must match the Password Confirmation!")
            is_valid = False
        return is_valid


# =================================
# validating login
# ===============================

    @staticmethod
    def validate_login(data):
        is_valid = True

        user_in_db = User.get_by_email(data)

        if not user_in_db:
            flash("Invalid Email!")
            is_valid = False
        # need to be elif in the model file because you don't want no user and match password
        elif not bcrypt.check_password_hash(user_in_db.password, data["password"]):
            flash("Invalid password!")
            is_valid = False

        return is_valid
# =============================================================
# fetching email data from the database to compare to the input
# =============================================================

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("recipes_schema").query_db(query, data)

        if len(result) <1:
            return False
        return cls(result[0])



# =======================================================
# registering new user in to the queries
# ======================================================
    @classmethod
    def create_user(cls, data):
        query ="""INSERT INTO users (first_name, last_name, email, password, created_at, updated_at)
        VALUES (%(first_name)s,%(last_name)s, %(email)s, %(password)s, NOW(), NOW()); """

        results = connectToMySQL("recipes_schema").query_db(query, data)

        return results

# =============================================
# retrieving the passed in user id and getting it's one info
# ==============================================
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(user_id)s;"
        result = connectToMySQL("recipes_schema").query_db(query, data)

        # if no match, 
        if len(result) <1:
            return False
        return cls(result[0])

    # @classmethod
    # def get_user_recipes(cls, data):
    #     query = """SELECT * FROM users LEFT JOIN recipes ON recipes.user_id = users.id WHERE users.id = %(user_id)s"""

    #     results = connectToMySQL("recipes_schema").query_db(query, data)

    #     user = cls(results[0])

    #     for row in results:

    #         recipe_data = {
    #             "id" : row["recipes.id"],

    #             "name": row["name"],
    #             "under_thirty": row["under_thirty"],
    #             "description": row["description"],
    #             "instruction": row["instruction"],

    #             "created_at": row["created_at"],
    #             "updated_at": row["updated_at"],

    #             "user_id": row["user_id"]
    #         }
    #         user.recipes.append(recipe.Recipe(recipe_data))
    #     return user