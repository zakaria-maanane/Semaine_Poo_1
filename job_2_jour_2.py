class Livre:
    def __init__(self, titre: str, auteur: str, nombre_de_pages: int):
        """
        Constructeur de la classe Livre.
        Initialise les attributs privés avec des valeurs fournies.
        """
        self.__titre = titre  # Attribut privé pour le titre du livre
        self.__auteur = auteur  # Attribut privé pour l'auteur du livre
        self.__nombre_de_pages = None  # Initialisation de l'attribut privé du nombre de pages
        self.set_nombre_de_pages(nombre_de_pages)  # Utilisation du mutateur pour validation

    # Accesseurs (getters)
    def get_titre(self) -> str:
        """Retourne le titre du livre."""
        return self.__titre

    def get_auteur(self) -> str:
        """Retourne le nom de l'auteur du livre."""
        return self.__auteur

    def get_nombre_de_pages(self) -> int:
        """Retourne le nombre de pages du livre."""
        return self.__nombre_de_pages

    # Mutateurs (setters)
    def set_titre(self, titre: str):
        """Modifie le titre du livre."""
        self.__titre = titre

    def set_auteur(self, auteur: str):
        """Modifie l'auteur du livre."""
        self.__auteur = auteur

    def set_nombre_de_pages(self, nombre_de_pages: int):
        """
        Modifie le nombre de pages du livre.
        Vérifie que la valeur est un entier positif avant de l'affecter.
        """
        if isinstance(nombre_de_pages, int) and nombre_de_pages > 0:
            self.__nombre_de_pages = nombre_de_pages
        else:
            print("Erreur : Le nombre de pages doit être un entier positif.")

    # Affichage des informations du livre
    def afficher_livre(self):
        """Affiche les informations du livre."""
        print(f"Titre : {self.__titre}")
        print(f"Auteur : {self.__auteur}")
        print(f"Nombre de pages : {self.__nombre_de_pages}")

# Exemple d'utilisation
livre1 = Livre("Les Misérables", "Victor Hugo", 1232)
livre1.afficher_livre()  # Affiche les informations du livre

livre1.set_nombre_de_pages(-50)  # Test de validation (affichera une erreur)
livre1.set_nombre_de_pages(1500)  # Modification correcte

livre1.afficher_livre()  # Affichage après modification

"""Créer la classe Livre qui prend en attributs privés un titre, un auteur et un
nombre de pages.
Créer les accesseurs et mutateurs nécessaires afin de pouvoir modifier et
afficher les attributs. Pour changer le nombre de pages, ce dernier doit être
un nombre entier positif, sinon la valeur n’est pas changée et un message
d’erreur est affiché."""