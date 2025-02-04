
""" Job 8 J'ai reussit a faire ce job mais j'ai 
malgré tout compris le code pour progresser """

import math  # Module math pour utiliser la valeur de π (pi)

class Cercle:
    def __init__(self, rayon):
        """ Constructeur de la classe Cercle 
        - Initialisation de l'attribut rayon.
        """
        self.rayon = rayon  # Attribut d'instance qui stocke le rayon du cercle

    def changerRayon(self, nouveau_rayon):
        """ Modifie la valeur du rayon du cercle """
        self.rayon = nouveau_rayon  # Mise à jour de l'attribut rayon

    def afficherInfos(self):
        """ Affiche les informations du cercle (rayon, diamètre, circonférence, aire) """
        print(f"Cercle de rayon : {self.rayon}")
        print(f"Diamètre : {self.diametre()}")
        print(f"Circonférence : {self.circonference():.2f}")  # Format arrondi à 2 décimales
        print(f"Aire : {self.aire():.2f}\n")

    def circonference(self):
        """ Retourne la circonférence du cercle (2 * π * r) """
        return 2 * math.pi * self.rayon  # Formule de la circonférence

    def aire(self):
        """ Retourne l'aire du cercle (π * r²) """
        return math.pi * (self.rayon ** 2)  # Formule de l'aire

    def diametre(self):
        """ Retourne le diamètre du cercle (2 * r) """
        return 2 * self.rayon  # Formule du diamètre

# ======= TEST DU CODE ======= #

# Création de deux cercles avec des rayons 4 et 7
cercle1 = Cercle(4)
cercle2 = Cercle(7)

# Affichage des informations du premier cercle
print("Informations du premier cercle :")
cercle1.afficherInfos()

# Affichage des informations du deuxième cercle
print("Informations du deuxième cercle :")
cercle2.afficherInfos()

# Modification du rayon du premier cercle
cercle1.changerRayon(10)
print("Après modification du rayon du premier cercle :")
cercle1.afficherInfos()


        


"""Consigne : Créez la classe “Cercle” recevant en argument son rayon, également initialisé
dans le constructeur.
Ajoutez les méthodes suivantes :
- changerRayon qui permet de modifier le rayon.
- afficherInfos qui permet d’afficher toutes les informations du cercle.
- circonférence qui permet de retourner la circonférence.
- aire qui permet de retourner l’aire du cercle.
- diametre qui permet de retourner le diamètre du cercle.

Créez deux cercles avec comme rayon 4 et 7. Pour chaque cercle, affichez ses
informations, affichez sa circonférence, son diamètre et son aire."""        