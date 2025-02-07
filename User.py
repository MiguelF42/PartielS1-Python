### Création d'une nouvelle classe Users

import Database
import Password

### Création d'une nouvelle classe Users
### User est une classe qui hérite de la classe Salarié#

### Les attributs pour la classe User : Nom et Prenom hérités,
### puis Login et Password au moins
### classe User :
    
class User(object):
### constructeur de la nouvelle classe User
    def __init__(self, nom, pnom, type, region, login="", pwd=0, pwdModifiedAt=None,id=0,ban=False):
        self.Nom=nom.upper()  ## 2 attributs Nom et Prenom en public, accessible à tous
        self.Prenom=pnom.title()
        ##self.Nom = nom
        ##self.Prenom=pnom
        if login == "":
            self.Login = self.GenLogin()
        else:
            self.Login = login
        if isinstance(pwd,int):
            self.Password = self.NewPWD(pwd)
        else:
            self.Password = pwd
        self.Type = type
        self.Region = region
        self.PwdModifiedAt = pwdModifiedAt
        self.Id = id
        self.Ban = ban
        self.TypeName = self.getTypeName()

###### Les méthodes getter et setter pour les attributs de la classe User ######
    def get_id(self):
        return self.Id
    
    def get_prenom(self):
        return self.Prenom

    def get_nom(self):
        return self.Nom

    def get_login(self):
        return self.Login
    
    def get_pwd(self):
        return self.Password
    
    def get_PwdModifiedAt(self):
        return self.PwdModifiedAt

    def get_type(self):
        return self.Type
    
    def get_region(self):
        return self.Region
    
    def get_ban(self):
        return self.Ban
    
    def get_typeName(self):
        return self.TypeName
    
    def set_prenom(self, pnom):
        self.Prenom = pnom.title()
        User.updateUser(self)

    def set_nom(self, nom):
        self.Nom = nom.upper()
        User.updateUser(self)

    def set_login(self, login):
        self.Login = login.lower()
        User.updateUser(self)

    def set_pwd(self, pwd):
        self.Password = pwd
        User.updateUser(self)

    def set_PwdModifiedAt(self, pwdModifiedAt):
        self.PwdModifiedAt = pwdModifiedAt
        User.updateUser(self)

    def set_type(self, type):
        self.Type = type
        User.updateUser(self)
        self.__set_typeName()

    def set_region(self, region):
        self.Region = region
        User.updateUser(self)

    def set_ban(self, ban):
        self.Ban = ban
        User.updateUser(self)

    def __set_typeName(self):
        self.TypeName = self.getTypeName()

###### Les méthodes de la classe User pour la base de données ######
    
    def userFromDB(login): # Méthode Static : Création d'une instance de User à partir de la base de données
        user = Database.selectUser(login.lower())
        self = User(user[2], user[1], user[6], user[7], user[3], user[4], user[5], user[0], user[8])
        return self

    def Afficher_User(self): # Méthode pour afficher les attributs de la classe User
        print("User : ", self.get_nom(),"", self.get_pnom())

    def afficherUsers(): # Méthode Static : Afficher tous les utilisateurs
        users = Database.selectAllUsers()
        print("======== Liste des utilisateurs =========")
        for user in users:
            print(user)
        print("=========================================")

    def afficherUsersByRegion(region): # Méthode Static : Afficher les utilisateurs par région
        users = Database.selectUserByRegion(region)
        print("======== Liste des utilisateurs =========")
        for user in users:
            print(user)
        print("=========================================")

    def afficherUsersBannis(): # Méthode Static : Afficher les utilisateurs bannis
        users = Database.selectUserBannis()
        print("======== Liste des utilisateurs bannis =========")
        for user in users:
            print(user)
        print("================================================")

    def afficherUsersByType(type): # Méthode Static : Afficher les utilisateurs par type
        users = Database.selectUserByType(type)
        print("======== Liste des utilisateurs =========")
        for user in users:
            print(user)
        print("=========================================")

    def registerUser(self): # Méthode Enregistrant un utilisateur dans la base de données
        Database.insertUser(self.get_nom(), self.get_prenom(), self.get_region(), self.get_type(), self.get_login(), self.get_pwd(), self.get_PwdModifiedAt())
        print("User enregistré")

    def updateUser(self): # Méthode pour mettre à jour un utilisateur
        Database.updateUser(self.get_nom(), self.get_prenom(), self.get_region(), self.get_type(), self.get_login(), self.get_pwd(), self.get_PwdModifiedAt(), self.get_id())
        print("User mis à jour")

    def deleteUser(self): # Méthode pour supprimer un utilisateur
        Database.deleteUser(self.Id)

    def banUser(self): # Méthode pour bannir un utilisateur
        Database.banUser(self.Id)

    def unbanUser(self): # Méthode pour débannir un utilisateur
        self.set_ban(False)
        Database.unbanUser(self.Id)

    def getTypeName(userSession):
        return Database.selectTypeById(userSession.get_type())[1]

###### Les méthodes pour générer, hasher et vérifier un mot de passe ######

    def GenLogin(self): # Méthode pour générer un login
        print ("Génération d'un login")
        login = self.get_prenom()[0] + self.get_nom()
        print ("Login = ", login)
        return login.lower()

    def NewPWD(length=12): # Méthode pour générer un nouveau mot de passe hashé
        print(length)
        return User.hashPWD(User.GenPWD(length))

    def GenPWD(length=12): # Méthode pour générer un mot de passe
        print ("Génération d'un mot de passe")
        x = length if length >= 8 else 12
        pwd = Password.generate_password(x)
        print ("Mot de passe =", pwd)
        return pwd

    def hashPWD(pwd, algo="sha256"): # Méthode pour hasher un mot de passe
        print ("Hashage du mot de passe")
        if algo == "sha256":
            return Password.hash_password_sha256(pwd)
        else:
            return Password.hash_password(pwd)
    
    def VerifPWD(self, pwd): # Méthode pour vérifier un mot de passe
        print ("Vérification du mot de passe")
        if pwd.startswith("$2b$"):
            return Password.check_password(pwd, self.Password)
        else:
            return Password.check_password_sha256(pwd, self.Password)