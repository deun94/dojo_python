# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class User:
    def __init__(self, data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.handle = data['handle']
        self.birthday = data['birthday']
        # self.age = data["age"]
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        # declaring what your query will be coming from
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('twitter').query_db(query)
        # specifying the schema we are calling from and that's why you don't need to do twitter.users
        # Create an empty list to append our instances of users
        print(results)
        users = []
        # Iterate over the db results and create instances of users with cls.
        for user_data in results:

            users.append( cls(user_data) )
        return users
            
    @classmethod
    def one_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(user_id)s;"
        results = connectToMySQL('twitter').query_db(query, data)

        # parsing data 
        # because every id is just one dictionary, 
        # just save things to one instance instead of a list
        print(results)
        return cls(results[0])
