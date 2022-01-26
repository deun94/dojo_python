from http.client import TOO_MANY_REQUESTS
from unittest import TestResult
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class User:
    def __init__(self, data):
        self.id = data["id"]

        self.name = data["name"]
        self.location = data["location"]
        self.gender = data["gender"]
        self.language = data["language"]
        self.comment = data["comment"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @staticmethod
    def validate_user(data):
        is_valid = True

        if len(data["name"]) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False

        if data["location"] =="":
            flash("Please select location!")
            is_valid = False

        if data["language"] =="":
            flash("Please Select Language!")
            is_valid = False

        if len(data["comment"]) > 110:
            flash("Comment cannot be longer than 110 characters!")
            is_valid = False
        return is_valid

    @classmethod
    def create_user(cls, data):
        query = """
        INSERT INTO dojos (name, location, language, comment, created_at)
        VALUES (%(name)s, %(location)s, %(language)s, %(comment)s, NOW());"""

        results = connectToMySQL("dojo_survey_schema").query_db(query, data)
        return results
    
    @classmethod
    def show_one(cls, data):
        query = """SELECT * FROM dojos WHERE id = %(id)s;"""

        results = results = connectToMySQL("dojo_survey_schema").query_db(query, data)
        return results