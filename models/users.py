from app import mongo
from utils.password import Password

class User:
    @staticmethod
    def create_user(username, password):
        hashed_password = Password.hash_password(password)
        mongo.cx.imdb.users.insert_one({
            "username": username,
            "password": hashed_password
        })
    
    @staticmethod
    def find_by_username(username):
        return mongo.cx.imdb.users.find_one({"username": username})
