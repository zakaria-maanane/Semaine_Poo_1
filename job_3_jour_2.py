"""Job 3"""

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
        self.__disponible = True  # Attribut privé pour la disponibilité du livre (True = disponible)

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

    # Gestion de la disponibilité
    def verification(self) -> bool:
        """
        Vérifie si le livre est disponible.
        Retourne True si disponible, sinon False.
        """
        return self.__disponible

    def emprunter(self):
        """
        Permet d'emprunter un livre.
        Le livre doit être disponible pour être emprunté.
        """
        if self.verification():  # Vérifie si le livre est disponible
            self.__disponible = False
            print(f"Le livre '{self.__titre}' a été emprunté.")
        else:
            print(f"Le livre '{self.__titre}' est déjà emprunté.")

    def rendre(self):
        """
        Permet de rendre un livre.
        Le livre doit être actuellement emprunté pour être rendu.
        """
        if not self.verification():  # Vérifie si le livre est indisponible
            self.__disponible = True
            print(f"Le livre '{self.__titre}' a été rendu et est maintenant disponible.")
        else:
            print(f"Le livre '{self.__titre}' n'a pas été emprunté, donc il ne peut pas être rendu.")

    # Affichage des informations du livre
    def afficher_livre(self):
        """Affiche les informations du livre."""
        statut = "Disponible" if self.__disponible else "Emprunté"
        print(f"Titre : {self.__titre}")
        print(f"Auteur : {self.__auteur}")
        print(f"Nombre de pages : {self.__nombre_de_pages}")
        print(f"Statut : {statut}")

# Exemple d'utilisation
livre1 = Livre("Les Misérables", "Victor Hugo", 1232)
livre1.afficher_livre()  # Affiche les informations du livre

livre1.emprunter()  # Emprunt du livre
livre1.afficher_livre()  # Vérification du statut après emprunt

livre1.rendre()  # Retour du livre
livre1.afficher_livre()  # Vérification du statut après retour

livre1.rendre()  # Tentative de rendre un livre déjà disponible (message d'erreur)






























"""Récupérer la classe Livre.

Ajouter l'attribut privé suivant :
- disponible est initialisé par défaut à True. Créer une méthode nommée vérification qui vérifie si le livre est disponible,
c'est-à-dire que la valeur de son attribut disponible est égale à True. Cette
méthode doit retourner True ou False.

Ajouter une méthode emprunter qui rend le livre indisponible, autrement dit
la valeur de disponible devient False. Bien sûr, pour pouvoir emprunter un
livre, il faut que celui-ci soit disponible, vérifiez donc que celui-ci soit
disponible sans utiliser l’attribut disponible.

Après avoir emprunté un livre, il faut pouvoir le rendre. Créer une méthode
rendre qui dans un premier temps vérifie si le livre a bien été emprunté ( sans
utiliser l’attribut disponible), puis change la valeur de l’attribut disponible."""