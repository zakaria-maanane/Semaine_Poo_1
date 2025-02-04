"""JOB 7  Ici je met une methode par direction et je crée une methode position pour retourner les x et y a jour  """


class Personnage:
    def __init__(self, x, y):
        """ Constructeur de la classe Personnage 
        x : position initiale sur l'axe horizontal (colonnes du plateau)
        y : position initiale sur l'axe vertical (lignes du plateau)"""
        
        self.x = x  # Attribut représentant la position horizontale du personnage
        self.y = y  # Attribut représentant la position verticale du personnage

    def gauche(self):
        """ Déplace le personnage vers la gauche (diminue x) """
        self.x -= 1  # Décrémente la position x

    def droite(self):
        """ Déplace le personnage vers la droite (augmente x) """
        self.x += 1  # Incrémente la position x

    def haut(self):
        """ Déplace le personnage vers le haut (diminue y) """
        self.y -= 1  # Décrémente la position y

    def bas(self):
        """ Déplace le personnage vers le bas (augmente y) """
        self.y += 1  # Incrémente la position y

    def position(self):
        """ Retourne la position actuelle sous forme de tuple (x, y) """
        return (self.x, self.y)  # Retourne les coordonnées actuelles



# [instantation] Création d'un personnage à la position initiale (2, 3)
joueur = Personnage(2, 3)

# Affichage de la position initiale
print(f"Position initiale : {joueur.position()}")  # Doit afficher (2, 3)

# Déplacement du personnage
joueur.gauche()  # Va à gauche => x - 1
print(f"Après déplacement à gauche : {joueur.position()}")  # Doit afficher (1, 3)

joueur.droite()  # Va à droite => x + 1
print(f"Après déplacement à droite : {joueur.position()}")  # Doit afficher (2, 3)

joueur.haut()  # Va en haut => y - 1
print(f"Après déplacement en haut : {joueur.position()}")  # Doit afficher (2, 2)

joueur.bas()  # Va en bas => y + 1
print(f"Après déplacement en bas : {joueur.position()}")  # Doit afficher (2, 3)




"""TEST pour comprendre"""
joueur2 = Personnage(12, 23)

# Affichage de la position initiale
print(f"Position initiale : {joueur2.position()}")  # Doit afficher (2, 3)

# Déplacement du personnage
joueur2.gauche()  # Va à gauche => x - 1
print(f"Après déplacement à gauche : {joueur2.position()}")  # Doit afficher (1, 3)

joueur2.droite()  # Va à droite => x + 1
print(f"Après déplacement à droite : {joueur2.position()}")  # Doit afficher (2, 3)

joueur2.haut()  # Va en haut => y - 1
print(f"Après déplacement en haut : {joueur2.position()}")  # Doit afficher (2, 2)

joueur2.bas()  # Va en bas => y + 1
print(f"Après déplacement en bas : {joueur2.position()}")  # Doit afficher (2, 3)

"""Consignes : Créez une classe Personnage représentant un personnage de jeu. 
Le plateau de jeu est représenté par une matrice. Le joueur est défini par 
ses attributs x et y, représentant les index du tableau.

Créez le constructeur de cette classe en initialisant la position (x et y).

Créez les méthodes : gauche, droite, bas et haut permettant respectivement
de faire avancer à gauche et à droite, en haut ou en bas.

Implémentez une méthode “position” renvoyant les coordonnées sous forme
d’un tuple.   """