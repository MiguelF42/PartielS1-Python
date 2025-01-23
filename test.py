import Database
import Password

pwd = Password.hash_password_sha256("sadmin")
Database.insertUser("admin", "super", 1, 1, "sadmin", pwd, None)