# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class User:
    def __init__(self, data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

    # ===============getting all users
    # =========================
    @classmethod
    def get_all(cls):
        # declaring what your query will be coming from
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users_schema').query_db(query)
        # specifying the schema we are calling from and that's why you don't need to do twitter.users
        # Create an empty list to append our instances of users
        print(results)
        users = []
        # Iterate over the db results and create instances of users with cls.
        for user_data in results:

            users.append( cls(user_data) )
        return users

# ====================================
# add a user
# ==================================

    @classmethod
    def create_user(cls, data):
        query = """INSERT INTO users (first_name, last_name, email, created_at) 
        VALUEs(%(first_name)s,%(last_name)s, %(email)s, NOW());"""

        results = connectToMySQL("users_schema").query_db(query, data)
        print(results)
        return results

