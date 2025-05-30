from mysqlconnection import connectToMySQL

class User:
    DB = "users_schemas_with_cr"
    def __init__(self, data):
        self.user_id = data['user_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.DB).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users
        
    # the save method will be used when we need to save a new user to our database
    @classmethod
    def save(cls, data):
        query = """INSERT INTO users (first_name, last_name, email)
    		VALUES (%(first_name)s, %(last_name)s, %(email)s);"""
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result

