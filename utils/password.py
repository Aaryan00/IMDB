import bcrypt

class Password:
    
    @staticmethod
    def hash_password(password: str) -> str:
        # Generate a salt
        salt = bcrypt.gensalt()
        # Hash the password with the salt
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')

    @staticmethod
    def verify_password(stored_hash: str, password: str) -> bool:
        # Check if the password matches the stored hash
        return bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8'))
