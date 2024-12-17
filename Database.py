import mysql.connector

mydb = mysql.connector.connect(
  host="localhost", 
  user="root",
  password="root",
  database="python"
)

table="hospital"

mycursor = mydb.cursor()

###===================== Type =====================###

def selectTypeById(id):
    sql = "SELECT * FROM type WHERE id = %s"
    val = [id]
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    return myresult[0]

def selectTypeByName(name):
    sql = "SELECT * FROM type WHERE name = %s"
    val = [name]
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    return myresult[0]

def selectAllTypes():
    sql = "SELECT * FROM type"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult

###===================== Region =====================###
def selectAllRegions():
    sql = "SELECT * FROM region"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult

###===================== User =====================###
# Insert Request
def insertUser(nom, prenom, region, type, login, password, pwdModifiedAt):
    sql = "INSERT INTO "+table+" (lname, fname, region, type, login, password, pwd_modified_at) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (nom, prenom, region, type, login, password, pwdModifiedAt)
    mycursor.execute(sql, val)
    mydb.commit()

# Select Request
def selectUser(login):
    sql = "SELECT * FROM "+table+" WHERE login = %s"
    val = [login]
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    return myresult[0]

def selectUserByRegion(region):
    sql = "SELECT * FROM "+table+" WHERE region = %s"
    val = [region]
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    return myresult

def selectUserBannis():
    sql = "SELECT * FROM "+table+" WHERE ban_date IS NOT NULL"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult

def selectAllUsers():
    sql = "SELECT * FROM "+table+""
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult

# Update Request
def updateUser(nom, prenom, region, type, login, password, pwdModifiedAt, id):
    sql = "UPDATE "+table+" SET lname = %s, fname = %s, region = %s, type = %s, password = %s, login = %s, pwd_modified_at = %s  WHERE id = %s"
    val = (nom, prenom, region, type, password, login, pwdModifiedAt, id)
    mycursor.execute(sql, val)
    mydb.commit()

# Delete Request
def deleteUser(id):
    sql = "DELETE FROM "+table+" WHERE id = %s"
    val = [id]
    mycursor.execute(sql, val)
    mydb.commit()

# Ban Request
def banUser(id):
    sql = "UPDATE "+table+" SET ban_date = NOW() WHERE id = %s"
    val = [id]
    mycursor.execute(sql, val)
    mydb.commit()
