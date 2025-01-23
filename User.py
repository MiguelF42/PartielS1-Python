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
        if pwd == 0:
            self.Password = self.NewPWD(12)
        else:
            self.Password = pwd
        self.Type = type
        self.Region = region
        self.PwdModifiedAt = pwdModifiedAt
        self.Id = id
        self.Ban = ban
        self.TypeName = self.getTypeName()

    def createUserByPrompt(userSession=None): # Méthode Static : Création d'un utilisateur par prompt
        if userSession == None:
            return None
        nom = input('Nom : ')
        prenom = input('Prenom : ')

        if userSession.TypeName == "Super_Admin":
            regions = Database.selectAllRegions()
            for reg in regions:
                print(reg[0], " pour ", reg[1])
            region = input('Region : ')
        else :
            region = userSession.get_region()
        typeId = User.inputType(userSession)
        user = User(nom, prenom, typeId, region)
        print('Utilisateur créé')
        user.registerUser()
        return user
    
    def modifyUserByPrompt(userSession): # Méthode Static : Modifier un utilisateur par prompt
        login = input('Login : ')
        user = User.userFromDB(login)
        if not user:
            print('Utilisateur non trouvé')
            return None
        print('1 pour modifier le nom')
        print('2 pour modifier le prénom')
        print('3 pour modifier le type d\'utilisateur')
        if User.get_typeName(userSession) == "Super_Admin":
            print('4 pour modifier la region')
        print('5 pour modifier le login')
        print('6 pour régénérer un nouveau mot de passe')
        print('7 pour retour')
        choix2 = input('Votre choix : ')
        if choix2 == '1':
            nom = input('Nouveau nom : ')
            user.set_nom(nom)
        elif choix2 == '2':
            prenom = input('Nouveau prénom : ')
            user.set_prenom(prenom)
        elif choix2 == '3':
            user.set_type(User.inputType(userSession))
        elif choix2 == '4' and User.get_typeName(userSession) == "Super_Admin":
            user.set_region(User.inputRegion(userSession))
        elif choix2 == '5':
            login = input('Nouveau login : ')
            user.set_login(login)
        elif choix2 == '6':
            pwd = User.inputPassword()
            user.set_pwd(pwd)
        elif choix2 == '7':
            print('Retour')
        else:
            print("Choix invalide")
        user.updateUser()

    def deleteUserByPrompt(userSession=None): # Méthode Static : Supprimer un utilisateur par prompt
        login = input('Login : ')
        user = User.userFromDB(login)
        type = User.get_typeName(userSession)
        if type == "Admin" and userSession.get_typeName() != "Super_Admin":
            print("Vous n'avez pas les droits")
            return None
        if not user:
            print('Utilisateur non trouvé')
            return None
        user.deleteUser()
        print('Utilisateur supprimé')
            
    def inputPassword():
        pwd = int(input('Longueur du mot de passe (Defaut = 12) : '))
        while not pwd.is_integer():
            print("Veuillez saisir un nombre")
            pwd = int(input('Longueur du mot de passe (Defaut = 12) : '))
        return User.NewPWD(pwd)

    def inputType(userSession=None): # Méthode Static : Saisir un type
        types = Database.selectAllTypes()
        typeIds = []
        for type in types:
            print(type[0], " pour ", type[1])
            typeIds.append(type[0])
        type = int(input('Type : '))
        while type not in typeIds:
            print("Type invalide")
            if Database.selectTypeById(type)[1] == "Super_Admin":
                if User.getTypeName(userSession) != "Super_Admin":
                    print("Vous n'avez pas les droits")
            if Database.selectTypeById(type)[1] == "Admin":
                if User.getTypeName(userSession) != "Super_Admin":
                    print("Vous n'avez pas les droits")
            type = int(input('Type : '))
        return type
    
    def inputRegion(userSession=None): # Méthode Static : Saisir une région
        regions = Database.selectAllRegions()
        regionIds = []
        for region in regions:
            print(region[0], " pour ", region[1])
            regionIds.append(region[0])
        region = int(input('Region : '))
        while region not in regionIds:
            print("Region invalide")
            region = int(input('Region : '))
        return region

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

    def getTypeName(userSession):
        return Database.selectTypeById(userSession.get_type())[1]

###### Les méthodes pour générer, hasher et vérifier un mot de passe ######

    def GenLogin(self): # Méthode pour générer un login
        print ("Génération d'un login")
        login = self.get_nom()[0] + self.get_prenom()
        print ("Login = ", login)
        return login.lower()

    def NewPWD(length=12): # Méthode pour générer un nouveau mot de passe hashé
        return User.hashPWD(User.GenPWD(length))

    def GenPWD(length=12): # Méthode pour générer un mot de passe
        print ("Génération d'un mot de passe")
        pwd = Password.generate_password(length)
        print ("Mot de passe = ", pwd)
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