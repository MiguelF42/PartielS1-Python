import mysql.connector

mydb = mysql.connector.connect(
  host="localhost", 
  user="root",
  password="root",
  database="python"
)

userTable="hospital_users"
typeTable="hospital_user_types"
regionTable="hospital_regions"

mycursor = mydb.cursor()

###===================== Type =====================###

def selectTypeById(id):
    sql = "SELECT * FROM "+typeTable+" WHERE id = %s"
    val = [id]
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    return myresult[0]

def selectTypeByName(name):
    sql = "SELECT * FROM "+typeTable+" WHERE name = %s"
    val = [name]
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    return myresult[0]

def selectAllTypes():
    sql = "SELECT * FROM "+typeTable+""
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult

###===================== Region =====================###
def selectAllRegions():
    sql = "SELECT * FROM "+regionTable+""
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult

###===================== User =====================###
# Insert Request
def insertUser(nom, prenom, region, type, login, password):
    sql = "INSERT INTO "+userTable+" (lname, fname, region, type, login, password) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (nom, prenom, region, type, login, password)
    mycursor.execute(sql, val)
    mydb.commit()

# Select Request
def selectUser(login):
    sql = "SELECT * FROM "+userTable+" WHERE login = %s"
    val = [login]
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    return myresult[0]

def selectUserByRegion(region):
    sql = "SELECT * FROM "+userTable+" WHERE region = %s"
    val = [region]
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    return myresult

def selectUserBannis():
    sql = "SELECT * FROM "+userTable+" WHERE ban_date IS NOT NULL"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult

def selectUserByType(type):
    sql = "SELECT * FROM "+userTable+" WHERE type = %s"
    val = [type]
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    return myresult

def selectAllUsers():
    sql = "SELECT * FROM "+userTable+""
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult

# Update Request
def updateUser(nom, prenom, region, type, login, id):
    sql = "UPDATE "+userTable+" SET lname = %s, fname = %s, region = %s, type = %s, login = %s  WHERE id = %s"
    val = (nom, prenom, region, type, login, id)
    mycursor.execute(sql, val)
    mydb.commit()

def updateUserPassword(password, id):
    sql = "UPDATE "+userTable+" SET password = %s, pwd_modified_at = NOW() WHERE id = %s"
    val = (password, id)
    mycursor.execute(sql, val)
    mydb.commit()

# Delete Request
def deleteUser(id):
    sql = "DELETE FROM "+userTable+" WHERE id = %s"
    val = [id]
    mycursor.execute(sql, val)
    mydb.commit()

# Ban Request
def banUser(id):
    sql = "UPDATE "+userTable+" SET ban_date = NOW() WHERE id = %s"
    val = [id]
    mycursor.execute(sql, val)
    mydb.commit()

def unbanUser(id):
    sql = "UPDATE "+userTable+" SET ban_date = NULL WHERE id = %s"
    val = [id]
    mycursor.execute(sql, val)
    mydb.commit()
