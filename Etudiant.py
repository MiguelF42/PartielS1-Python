##############  Exemple d'une classe Mere et d'un cas d'héritage ###################
#############    By Céline OULMI  ###################

import Password
import Database

class Etudiant(object):  ## qui hérite de object
    """Classe des étudiants"""           # Documentation de la classe

### Constructeur de la classe : construite et initialiser un  objet
    def __init__(self, nom, pnom, nbEtud, specialite):
        # print ("Création d'un objet étudiant...")
        #self._Nom=nom  ### attribut protégé (en protected, suite héritage, accessibles aux classes qui dérivent self.__Nom = nom  ### attribut privée ( lnaccessible de l'exterieur)
        #self.__Nom=nom  ## attribut privé, inaccessible de l'exterieur
        ### Sinon
        self.Nom=nom.upper()  ## 2 attributs Nom et Prenom en public, accessible à tous
        self.Prenom=pnom.title()
        self.NbEtud=nbEtud
        self.Specialite=specialite
### Les méthodes getter et setter (sécurité d'accès) 
    def get_nom(self):  # Méthode 'get' pour retourner le nom
        return self.Nom
    def get_pnom(self):
        return self.Prenom
    def get_nbEtud(self):
        return self.NbEtud
    def get_specialite(self):
        return self.Specialite
  ### pour toutes les caratéristiques ou attributs de la classe
    def set_nom(self, nouveau_nom):   # Méthode 'set' pour modifier le nom
        if nouveau_nom == "":
            print ("Le nom de l'étudiant ne peut pas être vide!!!!")
        else:
            self.Nom = nouveau_nom
            print ("Le Nom à été modifié.") 
        User.updateUser(self)

    def set_pnom(self, nouveau_pnom):   # Méthode 'set' pour modifier le nom
        if nouveau_pnom == "":
            print ("Le prénom de l'employé ne peut pas être vide!!!!")
        else:
            self.Prenom = nouveau_pnom
            print ("Le Nom à été modifié.")
        User.updateUser(self)

    def set_nbEtud(self, nouveau_nbEtud):   # Méthode 'set' pour modifier le nom
        if nouveau_nbEtud == "":
            print ("Le nombre d'étudiants ne peut pas être vide!!!!")
        else:
            self.NbEtud = nouveau_nbEtud
            print ("Le nombre d'étudiants à été modifié.")
        User.updateUser(self)
    
    def set_specialite(self, nouvelle_specialite):   # Méthode 'set' pour modifier le nom
        if nouvelle_specialite == "":
            print ("La spécialité de l'étudiant ne peut pas être vide!!!!")
        else:
            self.Specialite = nouvelle_specialite
            print ("La spécialité à été modifiée.")
        User.updateUser(self)

### Autres méthode, exemple affichage            
    def afficher(self):
        print (self.Nom, " a été ajouté(e)")
        
### Création d'une nouvelle classe Users
### User est une classe qui hérite de la classe Salarié#

### Les attributs pour la classe User : Nom et Prenom hérités,
### puis Login et Password au moins
### classe User :
    
class User(Etudiant):
### constructeur de la nouvelle classe User
    def __init__(self, nom, pnom, nbEtud, specialite, login="", pwd="", isAdmin=False,id=0,ban=False):
        # print ("Création d'un objet User...")
        ##Salarié.__init__(self,nom, pnom)  #### ou bien faire référence par super()
        super().__init__(nom, pnom, nbEtud, specialite)
        ##self.Nom = nom
        ##self.Prenom=pnom
        if login == "":
            self.Login = self.GenLogin()
        else:
            self.Login = login
        if pwd == "":
            self.Password = self.hashPWD(self.GenPWD())
        else:
            self.Password = pwd
        self.isAdmin = isAdmin
        self.id = id
        self.ban = ban
    ## Les méthodes getter et setter pour les attributs de la classe User
    def get_id(self):
        return self.id

    def get_login(self):
        return self.Login
    
    def get_pwd(self):
        return self.Password
    
    def get_isAdmin(self):
        return self.isAdmin
    
    def get_ban(self):
        return self.ban
    
    def set_login(self, login):
        self.Login = login.lower()
        User.updateUser(self)

    def set_pwd(self, pwd):
        self.Password = self.hashPWD(pwd)
        User.updateUser(self)

    def set_isAdmin(self, admin):
        self.isAdmin = True if admin.lower() == "true" or admin == "1" else False
        User.updateUser(self)

    def set_ban(self, ban):
        self.ban = ban
        User.updateUser(self)
    
    def userFromDB(login): # Méthode Static : Création d'une instance de User à partir de la base de données
        user = Database.selectUser(login.lower())
        self = User(user[4], user[3], user[5], user[6], user[1], user[2], user[7], user[0], user[8])
        return self

    def Afficher_User(self): # Méthode pour afficher les attributs de la classe User
        print("User : ", self.get_nom(),"", self.get_pnom())

    def afficherUsers(): # Méthode Static : Afficher tous les utilisateurs
        users = Database.selectAllUsers()
        print("======== Liste des utilisateurs =========")
        for user in users:
            print(user)
        print("=========================================")

    def registerUser(self): # Méthode Enregistrant un utilisateur dans la base de données
        Database.insertUser(self.get_nom(), self.get_pnom(), self.get_nbEtud(), self.get_specialite(), self.get_login(), self.get_pwd(), self.get_isAdmin())
        print("User enregistré")

    def updateUser(self): # Méthode pour mettre à jour un utilisateur
        Database.updateUser(self.get_nom(), self.get_pnom(), self.get_nbEtud(), self.get_specialite(), self.get_login(), self.get_pwd(), self.get_isAdmin(), self.get_id())
        print("User mis à jour")

    def deleteUser(self): # Méthode pour supprimer un utilisateur
        Database.deleteUser(self.id)

    def banUser(self): # Méthode pour bannir un utilisateur
        Database.banUser(self.id)

    def unbanUser(self): # Méthode pour débannir un utilisateur
        self.set_ban(False)

    def GenLogin(self): # Méthode pour générer un login
        print ("Génération d'un login")
        login = self.get_nom()[0] + self.get_pnom()
        print ("Login = ", login)
        return login.lower()

    def GenPWD(self): # Méthode pour générer un mot de passe
        print ("Génération d'un mot de passe")
        pwd = Password.generate_password()
        print ("Mot de passe = ", pwd)
        return pwd

    def hashPWD(self, pwd, algo="sha256"): # Méthode pour hasher un mot de passe
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
        