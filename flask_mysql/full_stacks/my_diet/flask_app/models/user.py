from flask_app import app
from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask import flash

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

        self.posts = []
# =================================

    @staticmethod
    def validate_user(data):
        is_valid = True

        if len(data['first_name']) < 3:
            flash("First Name must be at least 3 characters!!")
            is_valid = False

        elif data["first_name"] =="":
            flash("First name is a required field!")
            is_valid = False
            
        if len(data['last_name']) < 2:
            flash("Last Name must be at least 3 characters!!")
            is_valid = False

        elif data["last_name"] =="":
            flash("Last name is a required field!")
            is_valid = False
            
        if not EMAIL_REGEX.match(data["email"]):
            flash("Invalid email address! Please enter correct email syntax")
            is_valid = False

        if data["email"] == "":
            flash("Email Address is required!")
            is_valid = False

        if User.get_by_email(data):
            flash("Email already in use! Please register new email or login!")
            is_valid = False

        if len(data["password"]) < 8:
            flash("Password must be at least 8 characters!!")
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
            flash("Invalid Email! Email is not registered")
            is_valid = False

        elif not bcrypt.check_password_hash(user_in_db.password, data["password"]):
            flash("Invalid password! Please enter correct password")
            is_valid = False

        return is_valid

# classmethods!!

# =======================================================
# registering new user in to the queries
# ======================================================
    @classmethod
    def create_user(cls, data):
        query ="""INSERT INTO users (first_name, last_name, email, password, created_at, updated_at)
        VALUES (%(first_name)s,%(last_name)s, %(email)s, %(password)s, NOW(), NOW()); """

        results = connectToMySQL("diet_schema").query_db(query, data)

        return results

# =============================================================
# fetching email data from the database to compare to the input
# =============================================================

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("diet_schema").query_db(query, data)

        if len(result) <1:
            return False
        return cls(result[0])
# =============================================
# retrieving the passed in user id and getting it's one info
# ==============================================
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(user_id)s;"
        result = connectToMySQL("diet_schema").query_db(query, data)

        # if no match, 
        if len(result) <1:
            return False
        return cls(result[0])

# # =======================================================
#     @classmethod
#     def like_post(cls, data):
#         query