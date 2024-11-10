from flask import Blueprint, render_template, request, redirect, url_for, session
from werkzeug.security import check_password_hash
from utils.logging import Logger

auth_bp = Blueprint('auth', __name__)

logger = Logger.get_logger()

# Route for rendering the login page (GET request)
@auth_bp.route('/login', methods=['GET'])
def login_get():
    logger.info("Rendering login page")
    return render_template('login.html')

# Route for processing the login form (POST request)
@auth_bp.route('/login', methods=['POST'])
def login_post():
    from models.users import User
    username = request.form['username']
    password = request.form['password']

    user = User.find_by_username(username)
    
    if user and check_password_hash(user['password'], password):
        session['username'] = username  
        logger.info('Login successful!') 
        return redirect(url_for('movie.home'))  
    else:
        logger.warning(f"Invalid login attempt for username: {username}")
        logger.info('Invalid username or password')  
        return redirect(url_for('auth.login_get'))

# Route for rendering the signup page (GET request)
@auth_bp.route('/signup', methods=['GET'])
def signup_get():
    logger.info("Rendering signup page")
    return render_template('signup.html')

# Route for processing the signup form (POST request)
@auth_bp.route('/signup', methods=['POST'])
def signup_post():
    from models.users import User
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    if password != confirm_password:
        logger.info('Passwords do not match.')
        return redirect(url_for('auth.signup_get')) 

    existing_user = User.find_by_username(username)
    if existing_user:
        logger.info('Username already exists. Please choose another one')
        return redirect(url_for('auth.signup_get')) 

    User.create_user(username, password)

    logger.info(f"User {username} signed up successfully")
    logger.info('Signup successful! Please log in')
    return redirect(url_for('auth.login_get')) 

# Logout Route
@auth_bp.route('/logout')
def logout():
    session.clear() 

    logger.info("User logged out")
    return redirect(url_for('auth.login_get')) 
