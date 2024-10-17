from flask_app.config.mysqlconnection import DB , connectToMySQL
from flask_app.models.user import User

class Review:
    def __init__(self , data):
        self.id = data['id']
        self.title = data['title']
        self.rating = data['rating']
        self.date_watched = data['date_watched']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        self.user = None

    # ! CRUD Operations
    # READ ALL
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM reviews LEFT JOIN users ON reviews.user_id = users.id;"
        results = connectToMySQL(DB).query_db(query)

        if not results:
            return []
        reviews = []
        for row in results:
            review = cls(row)
            user_data = {
                'id': row['users.id'],
                'fullname': row['fullname'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at'],
            }
            review.user = User(user_data)
            reviews.append(review)  
        return reviews
    
    # READ ONE BY ID
    @classmethod
    def get_by_id(cls , data):
        query = "SELECT * FROM reviews LEFT JOIN users ON reviews.user_id = users.id WHERE reviews.id = %(id)s;"
        result = connectToMySQL(DB).query_db(query , data)

        if not result:
            return None
        review = cls(result[0])
        user_data = {
            'id': result[0]['users.id'],
            'fullname': result[0]['fullname'],
            'email': result[0]['email'],
            'password': result[0]['password'],
            'created_at': result[0]['users.created_at'],
            'updated_at': result[0]['users.updated_at'],
        }
        review.user = User(user_data)
        return review

    # CREATE
    @classmethod
    def create(cls , data):
        print("*"*100)
        print(data)
        query = "INSERT INTO reviews (title , rating, date_watched, content, user_id) VALUES(%(title)s , %(rating)s, %(date_watched)s, %(content)s , %(user_id)s)"
        return connectToMySQL(DB).query_db(query , data)
    
    # UPDATE
    @classmethod
    def update(cls , data):
        query = "UPDATE reviews SET title=%(title)s , rating=%(rating)s , date_watched=%(date_watched)s , content=%(content)s WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query , data)
    
    # DELETE
    @classmethod
    def delete(cls , data):
        query = "DELETE FROM reviews WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query , data)

