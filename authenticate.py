

def authenticated(username,password):
    nom_utilisateur = "etienne"
    mot_de_pass="Etienne123"
    if username == nom_utilisateur and password == mot_de_pass:
        print(f"Vous êtes Connecté en tant que {username}")
       
    else:
        print("Nom d'utilisateur ou mot de passe incorrect")
        
        
if __name__ == "__main__":
    username = input("Entrez votre nom d'utilisateur: ")
    password = input("Entrez votre mot de passe: ")
    authenticated(username, password)
    