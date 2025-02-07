
"""Job 3 """

class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def get_longueur(self):
        return self.__longueur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur
    
    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)
    
    def surface(self):
        return self.__longueur * self.__largeur

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur
    
    def get_hauteur(self):
        return self.__hauteur
    
    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur
    
    def volume(self):
        return self.surface() * self.__hauteur

# Instanciation de la classe Rectangle
rect = Rectangle(10, 5)
print(f"Périmètre du rectangle: {rect.perimetre()}")
print(f"Surface du rectangle: {rect.surface()}")

# Instanciation de la classe Parallelepipede
para = Parallelepipede(10, 5, 3)
print(f"Volume du parallélépipède: {para.volume()}")











""" Consignes , Créer une classe Rectangle avec comme attribut privé longueur et largeur.
Créer la méthode perimètre permettant de calculer le périmètre du
rectangle ainsi que la méthode surface permettant de calculer la surface du
rectangle.

Créer les assesseurs et mutateurs permettant de manipuler les attributs de
la classe.

Créer une classe Parallelepipede héritant de la classe Rectangle avec en
plus un attribut hauteur et une autre méthode volume, permettant de
calculer le volume du parallélépipède. Instancier la classe Rectangle
et assurez-vous que toutes les méthodes fonctionnent."""