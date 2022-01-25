from flask_app import app
# because we need bcrypt

from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask import flash

import re

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
# import bcrypt 

# creating an object called bcrypt, made by invoking the function Bcrypt with out app as an argument

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

        if len(data['password']) < 8:
            flash("Password must be at least 8 characters.")
            is_valid = False
        return is_valid

# =======================================
# validating login
# ======================================
    @staticmethod
    def validate_login(data):
        is_valid =- True

        user_in_db = User.get_by_email(data)
        # call on query

        if not user_in_db:
            flash("User does not exist!")
            is_valid = False
            # is not redirect because we are in the models file
        
        # only if email is correct, then you move on to checking password
        elif not bcrypt.check_password_hash(user_in_db.password, data["password"]):
            flash("Invalid Password!")
            is_valid = False
        return is_valid

        


# ========================================
# registering a user
# ======================================

    @classmethod
    def create_user(cls, data):
        query = """INSERT INTO users (first_name, last_name, email, password, created_at, updated_at)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"""

        results = connectToMySQL('login_schema').query_db(query, data)

        print(results)

        return results
    
# ========================================
# grabbing and compare email from db
# =======================
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("login_schema").query_db(query, data)

        # if no match, 
        if len(result) <1:
            return False
        return cls(result[0])

# ===================
# grabbing by id for the dashboard
# ============================
    @classmethod
    def get_user_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(user_id)s;"
        # make sure user_id is called because that's what we named it
        result = connectToMySQL("login_schema").query_db(query, data)

        # if no match, 
        if len(result) <1:
            return False
        return cls(result[0])
