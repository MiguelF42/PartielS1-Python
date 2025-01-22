import bcrypt
import hashlib
import random

def hash_password(password): # Fonction pour hasher un mot de passe avec bcrypt
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def check_password(password, hashed): # Fonction pour vérifier un mot de passe avec bcrypt
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def generate_password(length): # Fonction pour générer un mot de passe aléatoire
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-*/=,;:!?./%$&é\"'(-è_çà)="
    password = ""
    for i in range(length):
        password += characters[random.randint(0, len(characters) - 1)]
    return password

def hash_password_sha256(password): # Fonction pour hasher un mot de passe avec sha256
    return hashlib.sha256(password.encode()).hexdigest()

def check_password_sha256(password, hashed): # Fonction pour vérifier un mot de passe avec sha256
    return hashed == hashlib.sha256(password.encode()).hexdigest()