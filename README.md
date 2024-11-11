# IMDB Dashboard - File Upload and Movie Management System

# Overview
This project is an IMDB Dashboard where users can:

Sign up and log in to their accounts.
Upload CSV files containing movie data.
Track the progress of their file uploads.
View the uploaded movie data with pagination and sorting options.

The application uses Flask as the web framework and MongoDB as the database to store user and movie data. Background tasks like processing uploaded files are handled using Python threading to ensure the main application thread isn't blocked.
 
# Features
## User Authentication: 
User can sign up, log in, and log out.
## CSV Upload: 
Users can upload CSV files containing movie data (with background processing for large files).
## Progress Tracking: 
Users can check the progress of their uploads.
## Movie Dashboard: 
Movies can be viewed with sorting and pagination options.

# Tech Stack
### Backend: 
Flask web framework for building the server-side logic.
### Database: 
MongoDB (with pymongo integration)
### Background Task Processing: 
Python threading
### Frontend: 
HTML (Basic UI for login, signup, dashboard)
### File Handling: 
werkzeug for secure file uploads 
### Hashing
Bcrypt for hashing passwords

# Requirements
Before you begin, make sure you have the Python 3.x installed

# Installation
1. Clone the repository
2. Install the required dependencies

Db is running on cloud so there is no need to setup in local.

# Running the App in Development Mode
To start the Flask app in development mode, run the following command:
python app.py

# Testing the Application
For testing purposes, you can use the following pre-created users to log in:

**Username**: Aryan Agrawal
**Password**: Aryan

**Username**: guest
**Password**: guest

These credentials are already available in the system for quick login and testing.

# How to Use the Application
## 1. User Authentication
Users can sign up, log in, and log out of their accounts.
### Sign Up: 
Navigate to /signup to create a new user account.
### Login: 
After signing up, log in to your account via the /login page.
### Logout: 
You can log out by clicking the "Logout" button which clears your session.

## 2. File Upload
Navigate to the Dashboard page after logging in.
Use the Upload CSV form to upload movie data files.
The file will be processed in the background using **Python threading**. You can check the progress of your upload on the dashboard.

## 3. Movie Dashboard
On the Movie Dashboard page, you'll see the list of movies uploaded by you.
Movies can be **sorted** by date_added, release_year, and duration.
The movies are displayed with **pagination** (default is 5 per page).

## Logs
All the logs can be seen in logs folder which will be created automatically when server start

# Author
This project was developed by Aryan Agrawal.
