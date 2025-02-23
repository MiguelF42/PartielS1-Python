import Prompt
import User

def printMenu():
    print('===============================Console SuperAdmin==============================')
    print('')
    print('1 pour créer un utilisateur')
    print('2 pour afficher les utilisateurs')
    print('3 pour modifier un utilisateur')
    print('4 pour supprimer un utilisateur')
    print('5 pour afficher les utilisateurs par région')
    print('6 pour afficher les utilisateurs bannis')
    print('7 pour afficher les utilisateurs par type')
    print('8 pour bannir un utilisateur')
    print('9 pour débannir un utilisateur')
    print('10 pour quitter')

def SuperAdminMenu(userSession):
    printMenu()
    choix=input('Votre choix : ')

    print('')
    while choix != '14':
        if choix == '1':
            print('Créer un utilisateur')
            Prompt.Prompt.createUserByPrompt(userSession) # Création d'un utilisateur via la console
        elif choix == '2':
            print('Afficher les utilisateurs')
            User.User.afficherUsers() # Affichage de tous les utilisateurs
        elif choix == '3':
            print('Modifier un utilisateur')
            Prompt.Prompt.modifyUserByPrompt(userSession) # Modification d'un utilisateur via la console
        elif choix == '4':
            print('Supprimer un utilisateur')
            Prompt.Prompt.deleteUserByPrompt(userSession) # Suppression d'un utilisateur via la console
        elif choix == '5':
            print('Afficher les utilisateurs par région')
            region = Prompt.Prompt.inputRegion(userSession)
            User.User.afficherUsersByRegion(region) # Affichage des utilisateurs par région
        elif choix == '6':
            print('Afficher les utilisateurs bannis')
            User.User.afficherUsersBannis() # Affichage des utilisateurs bannis
        elif choix == '7':
            print('Afficher les utilisateurs par type')
            type = Prompt.Prompt.inputType(userSession)
            User.User.afficherUsersByType(type) # Affichage des utilisateurs par type
        elif choix == '8':
            print('Bannir un utilisateur')
            Prompt.Prompt.banUserByPrompt(userSession) # Bannissement d'un utilisateur via la console
        elif choix == '9':
            print('Débannir un utilisateur')
            Prompt.Prompt.unbanUserByPrompt(userSession) # Débannissement d'un utilisateur via la console
        elif choix == '10': 
            print('Quitter')
        else:
            print('Choix invalide')

        print('')
        printMenu()
        choix=input('Votre choix : ')
