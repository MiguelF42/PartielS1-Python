import User
import Database

class Prompt:
    def createUserByPrompt(userSession=None): # Méthode Static : Création d'un utilisateur par prompt
        if userSession == None:
            return None
        nom = input('Nom : ')
        prenom = input('Prenom : ')

        if userSession.get_typeName() == "Super_Admin":
            region = Prompt.inputRegion(userSession) # Saisie de la région
        else :
            region = userSession.get_region() # Récupération de la région de l'utilisateur connecté
        typeId = Prompt.inputType(userSession) # Saisie du type
        pwd = Prompt.inputPassword() # Saisie du mot de passe
        user = User.User(nom, prenom, typeId, region,pwd=pwd) # Création de l'utilisateur
        print('Utilisateur créé')
        user.registerUser() # Enregistrement de l'utilisateur dans la base de données
        return user
    
    def modifyUserByPrompt(userSession=None): # Méthode Static : Modifier un utilisateur par prompt
        if userSession == None:
            return None
        login = input('Login : ')
        user = User.User.userFromDB(login) # Récupération de l'utilisateur
        if not user: # Si l'utilisateur n'existe pas
            print('Utilisateur non trouvé')
            return None
        print('1 pour modifier le nom')
        print('2 pour modifier le prénom')
        print('3 pour modifier le type d\'utilisateur')
        if User.User.get_typeName(userSession) == "Super_Admin":
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
            user.set_type(Prompt.inputType(userSession))
        elif choix2 == '4' and User.User.get_typeName(userSession) == "Super_Admin":
            user.set_region(Prompt.inputRegion(userSession))
        elif choix2 == '5':
            login = input('Nouveau login : ')
            user.set_login(login)
        elif choix2 == '6':
            pwd = Prompt.inputPassword()
            user.set_pwd(pwd)
        elif choix2 == '7':
            print('Retour')
        else:
            print("Choix invalide")
        user.updateUser()

    def banUserByPrompt(userSession=None): # Méthode Static : Bannir un utilisateur par prompt
        if userSession == None:
            return None
        login = input('Login : ')
        user = User.User.userFromDB(login)
        if not user:
            print('Utilisateur non trouvé')
            return None
        user.banUser()
        print('Utilisateur banni')
    
    def unbanUserByPrompt(userSession=None): # Méthode Static : Débannir un utilisateur par prompt
        if userSession == None: # Si l'utilisateur n'est pas connecté
            return None
        login = input('Login : ')
        user = User.User.userFromDB(login) # Récupération de l'utilisateur
        if not user: # Si l'utilisateur n'existe pas
            print('Utilisateur non trouvé')
            return None
        if not user.get_ban(): # Si l'utilisateur n'est pas banni
            print('Utilisateur non banni')
            return None
        user.unbanUser() # Débannissement de l'utilisateur
        print('Utilisateur débanni')

    def deleteUserByPrompt(userSession=None): # Méthode Static : Supprimer un utilisateur par prompt
        if userSession == None:
            return None
        login = input('Login : ')
        user = User.User.userFromDB(login) # Récupération de l'utilisateur
        type = User.User.get_typeName(userSession) # Récupération du type de l'utilisateur
        if type == "Admin" and userSession.get_typeName() != "Super_Admin":
            print("Vous n'avez pas les droits")
            return None
        if not user:
            print('Utilisateur non trouvé')
            return None
        user.deleteUser()
        print('Utilisateur supprimé')
            
    def inputPassword(): # Méthode Static : Saisir un mot de passe
        choix = input('Voulez-vous générer un mot de passe ? (O/N) : ')
        if choix == 'O':
            pwd = input('Longueur du mot de passe (Defaut = 12) : ')
            if pwd == '':
                pwd = 12
            else:
                while not pwd.isdigit(): # Vérification que la valeur est bien un nombre
                    print("Veuillez saisir un nombre")
                    pwd = input('Longueur du mot de passe (Defaut = 12) : ')
            return User.User.newPWD(pwd) # Génération d'un mot de passe
        else:
            pwd = input('Mot de passe : ')
            while not User.User.isValidPWD(pwd): # Vérification de la validité du mot de passe
                print("Mot de passe invalide")
                print("Le mot de passe doit contenir au moins 12 caractères, une majuscule, une minuscule, un chiffre et un caractère spécial")
                pwd = input('Mot de passe : ')
        return User.User.hashPWD(pwd) # Hashage du mot de passe

    def inputType(userSession=None): # Méthode Static : Saisir un type
        types = Database.selectAllTypes() # Récupération de tous les types
        typeIds = []
        for type in types:
            if (type[1] == "Super_Admin" or type[1] == "Admin") and userSession.get_typeName() != "Super_Admin": # Si le type est Super_Admin ou Admin et que l'utilisateur n'est pas Super_Admin
                continue
            print(type[0], " pour ", type[1])
            typeIds.append(type[0]) # Ajout de l'id du type dans la liste des id
        type = int(input('Type : '))
        while type not in typeIds:
            print("Type invalide")
            if Database.selectTypeById(type)[1] == "Super_Admin" or Database.selectTypeById(type)[1] == "Admin": # Si le type est Super_Admin ou Admin et que l'utilisateur n'est pas Super_Admin
                if User.User.getTypeName(userSession) != "Super_Admin": # Si l'utilisateur n'est pas Super_Admin
                    print("Vous n'avez pas les droits")
            type = int(input('Type : '))
        return type
    
    def inputRegion(userSession=None): # Méthode Static : Saisir une région
        regions = Database.selectAllRegions() # Récupération de toutes les régions
        regionIds = [] 
        for region in regions: 
            print(region[0], " pour ", region[1]) # Affichage de toutes les régions
            regionIds.append(region[0]) # Ajout de l'id de la région dans la liste des id
        region = int(input('Region : '))
        while region not in regionIds: # Tant que la région saisie n'est pas dans la liste des id
            print("Region invalide")
            region = int(input('Region : '))
        return region