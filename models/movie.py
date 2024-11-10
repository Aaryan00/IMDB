from pymongo import ASCENDING
from app import mongo

class Movie:
    @staticmethod
    def insert_movie(data):
        mongo.cx.imdb.movies.insert_one(data)

    def insert_movie_batch(data):        
        mongo.cx.imdb.movies.insert_many(data, ordered=False)

    @staticmethod
    def get_movies(sort_by, order, skip, limit):
        return list(mongo.cx.imdb.movies.find().sort(sort_by, order).skip(skip).limit(limit))
    
    @staticmethod
    def count_documents():
        return mongo.cx.imdb.movies.count_documents({})
