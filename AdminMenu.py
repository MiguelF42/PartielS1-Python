import User

def AdminMenu(userSession):
    print('================Console Admin===============')
    print('')
    print('1 pour créer un utilisateur')
    print('2 pour afficher les utilisateurs utilisateur')
    print('3 pour modifier un utilisateurs')
    print('4 pour supprimer un utilisateur')
    print('5 pour quitter')
    choix=input('Votre choix : ')

    while choix != '5':
        if choix == '1':
            User.User.createUserByPrompt(userSession.get_region())
        elif choix == '2':
            print('Afficher les utilisateurs')
            User.User.afficherUsers()
        elif choix == '3':
            print('Modifier un utilisateur')
            login = input('Login : ')
            user = User.User.userFromDB(login)
            if not user:
                print('Utilisateur non trouvé')
            else:
                ###===================== ToDo =====================###
                # refactoriser ce code en fonction dans la classe User#
                print('1 pour modifier le nom')
                print('2 pour modifier le prénom')
                print('3 pour modifier le nombre d\'étudiants')
                print('4 pour modifier la spécialité')
                print('5 pour modifier le login')
                print('6 pour modifier le mot de passe')
                print('7 pour modifier le statut admin')
                print('8 pour retour')
                choix2 = input('Votre choix : ')
                if choix2 == '1':
                    nom = input('Nouveau nom : ')
                    user.set_nom(nom)
                elif choix2 == '2':
                    prenom = input('Nouveau prénom : ')
                    user.set_pnom(prenom)
                elif choix2 == '3':
                    nbEtud = input('Nouveau nombre d\'étudiants : ')
                    user.set_nbEtud(nbEtud)
                elif choix2 == '4':
                    specialite = input('Nouvelle spécialité : ')
                    user.set_specialite(specialite)
                elif choix2 == '5':
                    login = input('Nouveau login : ')
                    user.set_login(login)
                elif choix2 == '6':
                    pwd = input('Nouveau mot de passe : ')
                    user.set_pwd(pwd)
                elif choix2 == '7':
                    admin = input('Statut admin (True=1/False=0) : ')
                    user.set_isAdmin(admin)
                elif choix2 == '8':
                    print('Retour')
                else:
                    print('Choix invalide')
        elif choix == '4':
            print('Supprimer un utilisateur')
            login = input('Login : ')
            user = User.User.userFromDB(login)
            if not user:
                print('Utilisateur non trouvé')
            else:
                user.deleteUser()
        else:
            print('Choix invalide')

        print('')
        print('1 pour créer un utilisateur')
        print('2 pour afficher les utilisateurs utilisateur')
        print('3 pour modifier un utilisateurs')
        print('4 pour supprimer un utilisateur')
        print('5 pour quitter')
        choix=input('Votre choix : ')