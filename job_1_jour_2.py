"""Job 1 """

class Rectangle:
    def __init__(self, longueur, largeur):
        """ Constructeur de la classe Rectangle
        - Initialise les attributs privés __longueur et __largeur.
        """
        self.__longueur = longueur  # Attribut privé : longueur du rectangle
        self.__largeur = largeur    # Attribut privé : largeur du rectangle

    # ====== Accesseurs (Getters) ======
    def get_longueur(self):
        """ Retourne la longueur du rectangle """
        return self.__longueur

    def get_largeur(self):
        """ Retourne la largeur du rectangle """
        return self.__largeur

    # ====== Mutateurs (Setters) ======
    def set_longueur(self, nouvelle_longueur):
       
        self.__longueur = nouvelle_longueur

    def set_largeur(self, nouvelle_largeur):
      
        self.__largeur = nouvelle_largeur

    # ====== Méthode pour afficher les dimensions ======
    def afficher_infos(self):
        
        return f"Rectangle - Longueur: {self.__longueur}, Largeur: {self.__largeur}"

# ======= TEST DU CODE ======= #

# Création d'un rectangle avec longueur 10 et largeur 5
mon_rectangle = Rectangle(10, 5)

# Affichage des dimensions initiales
infos_initiales = mon_rectangle.afficher_infos()
print("Dimensions initiales du rectangle :")
print(infos_initiales)

# Modification des dimensions
mon_rectangle.set_longueur(15)  # Changement de la longueur à 15
mon_rectangle.set_largeur(8)    # Changement de la largeur à 8

# Vérification des nouvelles dimensions
infos_modifiees = mon_rectangle.afficher_infos()
print("\nAprès modification des dimensions :")
print(infos_modifiees)


"""Consignes : Créer une classe Rectangle avec des attributs privés, longueur et largeur
initialisées dans le constructeur.
Créer des accesseurs et mutateurs afin de pouvoir afficher et modifier les
attributs de la classe.

Créer un rectangle avec les valeurs suivantes : longueur 10 et largeur 5.
Changer la valeur de la longueur et de la largeur et vérifier que les
modifications soient bien prises en compte."""
