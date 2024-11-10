from flask import Flask
from flask_pymongo import PyMongo
from utils.config import Config
from utils.logging import Logger
import os 


# Initialize Flask application
app = Flask(__name__)
app.config.from_object(Config)

upload_folder = 'uploads'
if not os.path.exists(upload_folder):
    os.makedirs(upload_folder)

Logger.set_logger()

logger = Logger.get_logger()


with app.app_context():
    mongo = PyMongo(app)

    # Create index only once when the app starts
    mongo.cx.imdb.users.create_index([("username")], unique=True)
    mongo.cx.imdb.uploads.create_index([("username")])
    mongo.cx.imdb.movies.create_index([("date_added")])
    mongo.cx.imdb.movies.create_index([("release_year")])
    mongo.cx.imdb.movies.create_index([("duration")])
    mongo.cx.imdb.movies.create_index([("show_id")], unique=True)

    logger.info("Index created")

# Register Blueprints (Organizing routes into modular components)
from services.auth_service import auth_bp
from services.upload_service import upload_bp
from services.movie_service import movie_bp

app.register_blueprint(auth_bp)
app.register_blueprint(upload_bp)
app.register_blueprint(movie_bp)


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
