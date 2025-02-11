import User
import SuperAdminMenu
import AdminMenu
import datetime
import Prompt

def printMenu():
    print('================Console Utilisateur===============')
    print('')
    print('1 pour se connecter')
    print('2 pour quitter')

printMenu()
choix = input('Votre choix : ')

while choix != '2':
    if choix == '1':
        print('Se connecter')
        ban = False
        attempts = 1
        while not ban and attempts <= 3 and attempts > 0:
            login = input('Login : ')
            pwd = input('Mot de passe : ')
            user = User.User.userFromDB(login)
            if user.Ban is not None :
                if (datetime.datetime.now() - user.Ban) > datetime.timedelta(minutes=15) :
                    user.unbanUser()
                else :
                    print('Compte bloqué')
                    ban = True
                    continue
            if not user or not user.verifPWD(pwd):
                print('Login incorrect')
                attempts += 1
                if attempts > 3:
                    print('Compte bloqué durant 15min')
                    user.banUser()
                    ban = True
            else :
                attempts = 0
                if (datetime.datetime.now() - user.PwdModifiedAt) > datetime.timedelta(days=90) :
                    user.set_pwd(Prompt.Prompt.inputPassword())

                if user.TypeName == "Super_Admin":
                    SuperAdminMenu.SuperAdminMenu(user)

                elif user.TypeName == "Admin":
                    AdminMenu.AdminMenu(user)

                else:
                    print('Connecté')
    else:
        print('Choix invalide')
    printMenu()
    choix = input('Votre choix : ')