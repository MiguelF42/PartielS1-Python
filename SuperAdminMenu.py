import User

def SuperAdminMenu(userSession):
    print('===============================Console SuperAdmin==============================')
    print('')
    print('1 pour créer un utilisateur')
    print('2 pour afficher les utilisateurs')
    print('3 pour modifier un utilisateur')
    print('4 pour supprimer un utilisateur')
    print('5 pour afficher les utilisateurs par région')
    print('10 pour afficher les utilisateurs par type')
    print('6 pour afficher les utilisateurs bannis')
    # print('7 pour bannir un utilisateur')
    # print('8 pour débannir un utilisateur')
    # print('9 pour ajouter une région')
    # print('10 pour supprimer une région')
    # print('11 pour ajouter un type')
    # print('12 pour supprimer un type')
    print('13 pour quitter')
    choix=input('Votre choix : ')

    print('')
    while choix != '13':
        if choix == '1':
            print('Créer un utilisateur')
            User.User.createUserByPrompt(userSession)
        elif choix == '2':
            print('Afficher les utilisateurs')
            User.User.afficherUsers(userSession.get_region(),userSession)
        elif choix == '3':
            print('Modifier un utilisateur')
            User.User.modifyUserByPrompt(userSession)
        elif choix == '4':
            print('Supprimer un utilisateur')
            User.User.deleteUserByPrompt(userSession)
        elif choix == '5':
            print('Afficher les utilisateurs par région')
            region = User.User.inputRegion(userSession)
            User.User.afficherUsersByRegion(region)
        elif choix == '6':
            print('Afficher les utilisateurs bannis')
            User.User.afficherUsersBannis()
        elif choix == '13':
            print('Quitter')
        else:
            print('Choix invalide')

        print('')
        print('1 pour créer un utilisateur')
        print('2 pour afficher les utilisateurs')
        print('3 pour modifier un utilisateur')
        print('4 pour supprimer un utilisateur')
        print('5 pour afficher les utilisateurs par région')
        print('10 pour afficher les utilisateurs par type')
        print('6 pour afficher les utilisateurs bannis')
        # print('7 pour bannir un utilisateur')
        # print('8 pour débannir un utilisateur')
        # print('9 pour ajouter une région')
        # print('10 pour supprimer une région')
        # print('11 pour ajouter un type')
        # print('12 pour supprimer un type')
        print('13 pour quitter')
        choix=input('Votre choix : ')
