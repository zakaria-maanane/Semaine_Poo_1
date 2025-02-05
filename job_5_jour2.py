"""Job 5"""
class Voiture:
    def __init__(self, marque: str, modele: str, annee: int, kilometrage: int):
        """
        Constructeur de la classe Voiture.
        Initialise les attributs privés avec des valeurs fournies et un réservoir par défaut à 50.
        """
        self.__marque = marque  # Marque de la voiture (privé)
        self.__modele = modele  # Modèle de la voiture (privé)
        self.__annee = annee  # Année de fabrication (privé)
        self.__kilometrage = kilometrage  # Kilométrage de la voiture (privé)
        self.__en_marche = False  # Indique si la voiture est en marche (privé)
        self.__reservoir = 50  # Réservoir initialisé à 50 litres (privé)

    # Accesseurs (getters)
    def get_marque(self) -> str:
        """Retourne la marque de la voiture."""
        return self.__marque

    def get_modele(self) -> str:
        """Retourne le modèle de la voiture."""
        return self.__modele

    def get_annee(self) -> int:
        """Retourne l'année de fabrication de la voiture."""
        return self.__annee

    def get_kilometrage(self) -> int:
        """Retourne le kilométrage de la voiture."""
        return self.__kilometrage

    def get_en_marche(self) -> bool:
        """Retourne l'état de la voiture (en marche ou arrêtée)."""
        return self.__en_marche

    def get_reservoir(self) -> int:
        """Retourne le niveau du réservoir."""
        return self.__reservoir

    # Mutateurs (setters)
    def set_marque(self, marque: str):
        """Modifie la marque de la voiture."""
        self.__marque = marque

    def set_modele(self, modele: str):
        """Modifie le modèle de la voiture."""
        self.__modele = modele

    def set_annee(self, annee: int):
        """Modifie l'année de la voiture."""
        self.__annee = annee

    def set_kilometrage(self, kilometrage: int):
        """Modifie le kilométrage de la voiture."""
        self.__kilometrage = kilometrage

    def set_reservoir(self, litres: int):
        """Modifie la quantité d'essence dans le réservoir."""
        if isinstance(litres, int) and litres >= 0:
            self.__reservoir = litres
        else:
            print("Erreur : La quantité d'essence doit être un entier positif.")

    # Méthode privée pour vérifier le niveau du réservoir
    def __verifier_plein(self) -> int:
        """
        Méthode privée qui retourne le niveau de carburant du réservoir.
        """
        return self.__reservoir

    # Méthode pour démarrer la voiture
    def demarrer(self):
        """
        Démarre la voiture si le réservoir contient plus de 5 litres de carburant.
        """
        if self.__verifier_plein() > 5:
            self.__en_marche = True
            print("La voiture a démarré.")
        else:
            print("Impossible de démarrer : le réservoir est trop bas.")

    # Méthode pour arrêter la voiture
    def arreter(self):
        """
        Arrête la voiture.
        """
        self.__en_marche = False
        print("La voiture est arrêtée.")

    # Affichage des informations de la voiture
    def afficher_voiture(self):
        """Affiche les informations de la voiture."""
        etat = "En marche" if self.__en_marche else "Arrêtée"
        print(f"Marque : {self.__marque}")
        print(f"Modèle : {self.__modele}")
        print(f"Année : {self.__annee}")
        print(f"Kilométrage : {self.__kilometrage} km")
        print(f"État : {etat}")
        print(f"Réservoir : {self.__reservoir} litres")

# Exemple d'utilisation
voiture1 = Voiture("Toyota", "Corolla", 2020, 35000)
voiture1.afficher_voiture()  # Affiche les informations de la voiture

voiture1.demarrer()  # Essai de démarrer la voiture
voiture1.afficher_voiture()  # Vérification de l'état après démarrage

voiture1.arreter()  # Arrêt de la voiture
voiture1.afficher_voiture()  # Vérification de l'état après arrêt

voiture1.set_reservoir(4)  # Baisse du niveau d'essence
voiture1.demarrer()  # Tentative de démarrage avec un réservoir insuffisant

"""Consigne : Créer une classe Voiture qui a pour attributs privés une marque, un modèle,
une année, un kilométrage et un attribut nommé en_marche initialisé par
défaut à False.
Cette classe doit posséder des mutateurs et assesseurs pour chaque attribut. Créer une méthode demarrer qui change la valeur de l’attribut en_marche
en True, une méthode arreter qui change la valeur de l’attribut en_marche
en False.
Ajouter à la classe Voiture l’attribut privé reservoir qui est initialisé à 50 par
défaut dans le constructeur. Créer une méthode privée verifier_plein qui
retourne la valeur de l’attribut reservoir. Cette méthode est appelée dans la
méthode demarrer. Si la valeur du réservoir est supérieure à 5 la voiture peut
démarrer."""