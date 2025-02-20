### Création d'une nouvelle classe Users

import Database
import Password
import re

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
        if login == "": # Si le login est vide, on génère un nouveau login
            self.Login = self.genLogin()
        else:
            self.Login = login
        if isinstance(pwd,int): # Si le mot de passe est un entier, on génère un nouveau mot de passe
            self.Password = self.newPWD(pwd)
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
        User.updateUserPassword(self)

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

    def set_typeName(self):
        self.TypeName = self.getTypeName()

###### Les méthodes de la classe User pour la base de données ######
    
    def userFromDB(login): # Méthode Static : Création d'une instance de User à partir de la base de données
        user = Database.selectUser(login.strip().lower()) # Récupération de l'utilisateur par login
        self = User(user[2], user[1], user[6], user[7], user[3], user[4], user[5], user[0], user[8]) # Création de l'instance de User
        return self

    def Afficher_User(self): # Méthode pour afficher les attributs de la classe User
        print("User : ", self.get_nom(),"", self.get_pnom())

    def afficherUsers(): # Méthode Static : Afficher tous les utilisateurs
        users = Database.selectAllUsers() # Récupération de tous les utilisateurs
        print("======== Liste des utilisateurs =========")
        for user in users:
            print(user)
        print("=========================================")

    def afficherUsersByRegion(region): # Méthode Static : Afficher les utilisateurs par région
        users = Database.selectUserByRegion(region) # Récupération des utilisateurs par région
        print("======== Liste des utilisateurs =========")
        for user in users:
            print(user)
        print("=========================================")

    def afficherUsersBannis(): # Méthode Static : Afficher les utilisateurs bannis
        users = Database.selectUserBannis() # Récupération des utilisateurs bannis
        print("======== Liste des utilisateurs bannis =========")
        for user in users:
            print(user)
        print("================================================")

    def afficherUsersByType(type): # Méthode Static : Afficher les utilisateurs par type
        users = Database.selectUserByType(type) # Récupération des utilisateurs par type
        print("======== Liste des utilisateurs =========")
        for user in users:
            print(user)
        print("=========================================")

    def registerUser(self): # Méthode Enregistrant un utilisateur dans la base de données
        Database.insertUser(self.get_nom(), self.get_prenom(), self.get_region(), self.get_type(), self.get_login(), self.get_pwd())
        print("User enregistré")

    def updateUser(self): # Méthode pour mettre à jour un utilisateur
        Database.updateUser(self.get_nom(), self.get_prenom(), self.get_region(), self.get_type(), self.get_login(), self.get_id())
        print("User mis à jour")

    def updateUserPassword(self): # Méthode pour mettre à jour le mot de passe d'un utilisateur
        Database.updateUserPassword(self.get_pwd(), self.get_id())
        print("Mot de passe mis à jour")

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

    def genLogin(self): # Méthode pour générer un login
        print ("Génération d'un login")
        login = self.get_prenom()[0] + self.get_nom()
        print ("Login = ", login)
        return login.lower()

    def newPWD(length=12): # Méthode pour générer un nouveau mot de passe hashé
        return User.hashPWD(User.genPWD(length))
    
    def isValidPWD(password):
        pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[+-*/=,;:!?./%$&é\"(-è_çà)=@])[A-Za-z\d+-*/=,;:!?./%$&é\"(-è_çà)=@]{12,}$') # Vérification de la validité du mot de passe
        # La regex vérifie que le mot de passe contient au moins 12 caractères, une majuscule, une minuscule, un chiffre et un caractère spécial
        return bool(pattern.match(password)) # Retourne True si le mot de passe est valide, False sinon

    def genPWD(length=12): # Méthode pour générer un mot de passe
        print ("Génération d'un mot de passe")
        x = length if length >= 8 else 12
        pwd = Password.generate_password(x)
        print ("Mot de passe =", pwd)
        return pwd

    def hashPWD(pwd, algo="sha256"): # Méthode pour hasher un mot de passe
        print ("Hashage du mot de passe")
        if algo == "sha256": # Si l'algorithme est sha256
            return Password.hash_password_sha256(pwd)
        else:
            return Password.hash_password(pwd)
    
    def verifPWD(self, pwd): # Méthode pour vérifier un mot de passe
        print ("Vérification du mot de passe")
        if pwd.startswith("$2b$"): # Si le mot de passe est hashé avec bcrypt
            return Password.check_password(pwd, self.Password)
        else:
            return Password.check_password_sha256(pwd, self.Password)
    
