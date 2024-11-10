from werkzeug.security import generate_password_hash
from pymongo import ASCENDING
from app import mongo

class User:
    @staticmethod
    def create_user(username, password):
        hashed_password = generate_password_hash(password)
        mongo.cx.imdb.users.insert_one({
            "username": username,
            "password": hashed_password
        })
    
    @staticmethod
    def find_by_username(username):
        return mongo.cx.imdb.users.find_one({"username": username})
