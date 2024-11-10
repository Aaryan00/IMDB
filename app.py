from flask import Flask
from flask_pymongo import PyMongo
from config import Config

# Initialize Flask application
app = Flask(__name__)
app.config.from_object(Config)


mongo = PyMongo(app)

with app.app_context():
    # Create index only once when the app starts
    mongo.cx.imdb.users.create_index([("username")], unique=True)
    mongo.cx.imdb.uploads.create_index([("username")])
    mongo.cx.imdb.movies.create_index([("date_added")])
    mongo.cx.imdb.movies.create_index([("release_year")])
    mongo.cx.imdb.movies.create_index([("duration")])
    mongo.cx.imdb.movies.create_index([("show_id")], unique=True)

    print("Index created")

# Register Blueprints (Organizing routes into modular components)
from services.auth_service import auth_bp
from services.upload_service import upload_bp
from services.movie_service import movie_bp

app.register_blueprint(auth_bp)
app.register_blueprint(upload_bp)
app.register_blueprint(movie_bp)


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
