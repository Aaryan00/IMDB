
class Config:
    # MongoDB settings
    MONGO_URI = "mongodb+srv://Aryan2000:Aryanag@dailyround.gc7yg.mongodb.net/?retryWrites=true&w=majority&appName=DailyRound"
    MONGO_DBNAME = "imdb"

    # Flask settings
    SECRET_KEY = '3a571de28e705d2681f97333394fa322'
    UPLOAD_FOLDER = './uploads'
    ALLOWED_EXTENSIONS = {'csv'}
    # MAX_CONTENT_LENGTH = 10 * 1024 * 1024 * 1024  # Max file size (10 GB)
    MAX_CONTENT_LENGTH = 1 * 1024 * 1024  # MAx file size 1 MB
