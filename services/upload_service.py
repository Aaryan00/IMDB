from flask import Blueprint, request, jsonify, session, redirect, url_for
import os
from werkzeug.utils import secure_filename
import threading
import csv
from utils.logging import Logger

upload_bp = Blueprint('upload', __name__)
logger = Logger.get_logger()

@upload_bp.route('/upload', methods=['POST'])
def upload_csv():
    from app import app
    from models.upload import Upload

    username = session.get('username')
    if not username:
        logger.warning("User not logged in, redirecting to login")
        return redirect(url_for('auth.login_get'))
    
    if 'file' not in request.files:
        logger.warning("No file selected for upload")
        return jsonify({"message": "No file part"}), 400
    
    file = request.files['file']
    
    if file.filename == '' or not allowed_file(file.filename):
        logger.warning("Invalid file type uploaded")
        return jsonify({"message": "Invalid file format"}), 400

    filename = secure_filename(file.filename)
    upload_id = Upload.create_upload(username, filename)
    
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    logger.info(f"File {filename} uploaded successfully for user: {username}")

    processing_thread = threading.Thread(target=process_csv_in_background, args=(file_path, upload_id.inserted_id))
    processing_thread.start()

    return jsonify({"message": "File will be uploaded in some time", "upload_id": str(upload_id)}), 200

def allowed_file(filename):
    from app import app
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


def process_csv_in_background(file_path, upload_id):
    """Function that will run in a separate thread to process the CSV"""
    from models.upload import Upload
    from models.movie import Movie
    try:
        logger.info(f"Started processing file: {file_path} for id: {upload_id}")
        Upload.update_status(upload_id, 'Processing')

        batch_size = 25  
        batch = []
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                batch.append(row)
                if len(batch) >= batch_size:
                    Movie.insert_movie_batch(batch) 
                    batch.clear()

            if batch:
                Movie.insert_movie_batch(batch)

        logger.info(f"Finished processing file: {file_path}")

        Upload.update_status(upload_id, 'Completed')

    except Exception as e:
        # In case of error, update status to 'Failed'
        Upload.update_status(upload_id, 'Failed')
        logger.error(f"Error while processing CSV file: {e}")
