from app import mongo

class Upload:
    @staticmethod
    def create_upload(username, filename):
        return mongo.cx.imdb.uploads.insert_one({
            "username": username,
            "filename": filename,
            "status": "Pending"
        })
    
    @staticmethod
    def get_upload_status(upload_id):
        return mongo.cx.imdb.uploads.find_one({"_id": upload_id})
    
    @staticmethod
    def update_status(upload_id, status):
        mongo.cx.imdb.uploads.update_one({"_id": upload_id}, {"$set": {"status": status}})

    @staticmethod
    def get_uploads_by_user(username):
        return list(mongo.cx.imdb.uploads.find({"username": username}))
