import User
import Prompt

def printMenu():
    print('===============================Console Admin==============================')
    print('')
    print('1 pour créer un utilisateur')
    print('2 pour afficher les utilisateurs')
    print('3 pour modifier un utilisateur')
    print('4 pour supprimer un utilisateur')
    print('5 pour quitter')

def AdminMenu(userSession):
    printMenu()
    choix=input('Votre choix : ')

    while choix != '5':
        if choix == '1':
            Prompt.Prompt.createUserByPrompt(userSession)
        elif choix == '2':
            print('Afficher les utilisateurs')
            User.User.afficherUsersByRegion(userSession.get_region()) 
        elif choix == '3':
            print('Modifier un utilisateur')
            login = input('Login : ')
            user = User.User.userFromDB(login)
            if not user:
                print('Utilisateur non trouvé')
            else:
                Prompt.Prompt.modifyUserByPrompt(userSession)
        elif choix == '4':
            print('Supprimer un utilisateur')
            Prompt.Prompt.deleteUserByPrompt(userSession)
        else:
            print('Choix invalide')

        print('')
        printMenu()
        choix=input('Votre choix : ')