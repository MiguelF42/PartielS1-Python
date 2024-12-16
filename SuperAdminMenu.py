import User

def SuperAdminMenu():
    print('===============================Console SuperAdmin==============================')
    print('')
    print('1 pour créer un utilisateur')
    print('2 pour afficher les utilisateurs')
    print('3 pour modifier un utilisateur')
    print('4 pour supprimer un utilisateur')
    print('5 pour afficher les utilisateurs par région')
    print('10 pour afficher les utilisateurs par type')
    print('6 pour afficher les utilisateurs bannis')
    print('7 pour bannir un utilisateur')
    print('8 pour débannir un utilisateur')
    print('9 pour ajouter une région')
    print('10 pour supprimer une région')
    print('11 pour ajouter un type')
    print('12 pour supprimer un type')
    print('13 pour quitter')
    choix=input('Votre choix : ')

    print('')
    while choix != '13':
        if choix == '1':
            print('Créer un utilisateur')