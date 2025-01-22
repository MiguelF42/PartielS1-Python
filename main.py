import User
import AdminMenu
import datetime

print('================Console Utilisateur===============')
print('')
print('1 pour se connecter')
print('2 pour créer un compte')
print('3 pour quitter')

choix = input('Votre choix : ')

while choix != '3':
    if choix == '1':
        print('Se connecter')
        ban = False
        attempts = 1
        while not ban and attempts <= 3 and attempts > 0:
            login = input('Login : ')
            pwd = input('Password : ')
            user = User.User.userFromDB(login)
            if datetime.timedelta(minutes=5) < datetime.datetime.now() - user.ban:
                user.unbanUser()
            else :
                print('Compte bloqué')
                ban = True
                continue
            if not user or not user.VerifPWD(pwd):
                print('Login incorrect')
                attempts += 1
                if attempts > 3:
                    print('Compte bloqué durant 5min')
                    user.banUser()
                    ban = True
            else :
                attempts = 0
                if user.isAdmin:
                    AdminMenu.AdminMenu(user)
                else:
                    print('Connecté')
    elif choix == '2':
        print('Créer un compte')
        nom = input('Nom : ')
        pnom = input('Prénom : ')
        nbEtud = input('Numéro étudiant : ')
        specialite = input('Spécialité : ')
        user = User.User(nom, pnom, nbEtud, specialite)
        User.User.registerUser(user)
    else:
        print('Choix invalide')
    print('')
    print('1 pour se connecter')
    print('2 pour créer un compte')
    print('3 pour quitter')
    choix = input('Votre choix : ')
