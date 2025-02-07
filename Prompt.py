import User
import Database

class Prompt:
    def createUserByPrompt(userSession=None): # Méthode Static : Création d'un utilisateur par prompt
        if userSession == None:
            return None
        nom = input('Nom : ')
        prenom = input('Prenom : ')

        if userSession.get_typeName() == "Super_Admin":
            regions = Database.selectAllRegions()
            for reg in regions:
                print(reg[0], " pour ", reg[1])
            region = input('Region : ')
        else :
            region = userSession.get_region()
        typeId = Prompt.inputType(userSession)
        pwd = Prompt.inputPassword()
        user = User.User(nom, prenom, typeId, region,pwd=pwd)
        print('Utilisateur créé')
        user.registerUser()
        return user
    
    def modifyUserByPrompt(userSession=None): # Méthode Static : Modifier un utilisateur par prompt
        if userSession == None:
            return None
        login = input('Login : ')
        user = User.User.userFromDB(login)
        if not user:
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

    def deleteUserByPrompt(userSession=None): # Méthode Static : Supprimer un utilisateur par prompt
        if userSession == None:
            return None
        login = input('Login : ')
        user = User.User.userFromDB(login)
        type = User.User.get_typeName(userSession)
        if type == "Admin" and userSession.get_typeName() != "Super_Admin":
            print("Vous n'avez pas les droits")
            return None
        if not user:
            print('Utilisateur non trouvé')
            return None
        user.deleteUser()
        print('Utilisateur supprimé')
            
    def inputPassword(): # Méthode Static : Saisir un mot de passe
        pwd = int(input('Longueur du mot de passe (Defaut = 12) : '))
        while not pwd.is_integer():
            print("Veuillez saisir un nombre")
            pwd = int(input('Longueur du mot de passe (Defaut = 12) : '))
        return User.User.NewPWD(pwd)

    def inputType(userSession=None): # Méthode Static : Saisir un type
        types = Database.selectAllTypes()
        typeIds = []
        for type in types:
            if (type[1] == "Super_Admin" or type[1] == "Admin") and userSession.get_typeName() != "Super_Admin":
                continue
            print(type[0], " pour ", type[1])
            typeIds.append(type[0])
        type = int(input('Type : '))
        while type not in typeIds:
            print("Type invalide")
            if Database.selectTypeById(type)[1] == "Super_Admin" or Database.selectTypeById(type)[1] == "Admin":
                if User.User.getTypeName(userSession) != "Super_Admin":
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