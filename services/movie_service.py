# services/movie_service.py
from flask import Blueprint, render_template, request, redirect, url_for, session
from flask import session
from utils.logging import Logger

movie_bp = Blueprint('movie', __name__)

logger = Logger.get_logger()

# Home Route (Show movies if logged in)
@movie_bp.route('/')
def home():
    from models.upload import Upload
    username = session.get('username')
    # Need to use session.get("username")
    if not username or username not in session['username']:
        logger.warning("User not logged in, redirecting to login")
        return redirect(url_for('auth.login_get'))

    uploads = Upload.get_uploads_by_user(session['username'])

    logger.info(f"Rendering movie dashboard for user: {username}")
    return render_template('dashboard.html', uploads=uploads)
# , movies=movies, page=page)

@movie_bp.route('/get_movies')
def get_movies():
    from models.movie import Movie

    username = session.get('username')
    if not username or username not in session['username']: 
        logger.warning("User not logged in, redirecting to login")
        return redirect(url_for('auth.login_get')) 
    

    sort_by = request.args.get('sort_by', 'date_added')  # Default to 'date_added'
    sort_order = request.args.get('sort_order', 'desc')  # Default to 'desc'
    page = int(request.args.get('page', 1))  # Default to page 1
    per_page = int(request.args.get('per_page', 5))  # Default to 5 items per page
    
    # Calculate the "skip" and "limit" values for MongoDB query
    skip = (page - 1) * per_page
    limit = per_page

    logger.info(f"Fetching movies for user: {username}, sorting by {sort_by} in {sort_order} order")

    sort_direction = -1 if sort_order == 'desc' else 1  # MongoDB sorts: -1 for descending, 1 for ascending
    sort_field = sort_by  

    # Query MongoDB to get the movies with pagination and sorting
    movies_cursor = Movie.get_movies(sort_field, sort_direction, skip, limit)

    # Convert the cursor to a list of movies
    movies = list(movies_cursor)

    # Calculate total movies to handle pagination
    total_movies = Movie.count_documents()
    total_pages = (total_movies + per_page - 1) // per_page 

    logger.info(f"Total movies: {total_movies}, Total pages: {total_pages}")
    
    return render_template('movies.html', 
                           movies=movies, 
                           current_page=page,
                           total_pages=total_pages,
                           sort_by=sort_by,
                           sort_order=sort_order,
                           per_page=per_page)
