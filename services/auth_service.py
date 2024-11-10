from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import check_password_hash

# Define the blueprint for authentication
auth_bp = Blueprint('auth', __name__)

# Route for rendering the login page (GET request)
@auth_bp.route('/login', methods=['GET'])
def login_get():
    return render_template('login.html')

# Route for processing the login form (POST request)
@auth_bp.route('/login', methods=['POST'])
def login_post():
    from models.users import User
    username = request.form['username']
    password = request.form['password']

    user = User.find_by_username(username)
    
    if user and check_password_hash(user['password'], password):
        session['username'] = username  # Store username in session
        print('Login successful!') 
        return redirect(url_for('movie.home'))  # Redirect to home page after successful login
    else:
        print('Invalid username or password')  # Flash error message if login fails
        return redirect(url_for('auth.login_get'))  # Redirect back to the login page if credentials are incorrect

# Route for rendering the signup page (GET request)
@auth_bp.route('/signup', methods=['GET'])
def signup_get():
    return render_template('signup.html')

# Route for processing the signup form (POST request)
@auth_bp.route('/signup', methods=['POST'])
def signup_post():
    from models.users import User
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    # Validate that passwords match
    if password != confirm_password:
        print('Passwords do not match.')
        return redirect(url_for('auth.signup_get'))  # Redirect to the signup page if passwords don't match

    # Check if the user already exists
    existing_user = User.find_by_username(username)
    if existing_user:
        print('Username already exists. Please choose another one')
        return redirect(url_for('auth.signup_get'))  # Redirect back to signup page if username exists

    # Create the new user
    User.create_user(username, password)

    print('Signup successful! Please log in')
    return redirect(url_for('auth.login_get'))  # Redirect to login page after successful signup

# Logout Route
@auth_bp.route('/logout')
def logout():
    session.clear()  # Remove username from session (logout)
    print('You have been logged out')
    return redirect(url_for('auth.login_get'))  # Redirect to login page
