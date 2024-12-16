import bcrypt
import hashlib
import secrets

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def generate_password():
    return secrets.token_urlsafe(12)

def hash_password_sha256(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_password_sha256(password, hashed):
    return hashed == hashlib.sha256(password.encode()).hexdigest()