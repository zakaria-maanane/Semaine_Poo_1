"""Job 1 jour 3 Immutabilité - Mutabilité """

class Ville:
    def __init__(self, nom: str, habitants: int):
        """
        Constructeur de la classe Ville.
        Initialise le nom et le nombre d'habitants de la ville.
        """
        self.__nom = nom  # Nom de la ville (privé)
        self.__habitants = habitants  # Nombre d'habitants (privé)

    def get_habitants(self) -> int:
        """
        Retourne le nombre d'habitants de la ville.
        """
        return self.__habitants

    def ajouter_habitant(self):
        """
        Incrémente le nombre d'habitants de la ville de 1.
        """
        self.__habitants += 1

class Personne:
    def __init__(self, nom: str, age: int, ville: Ville):
        """
        Constructeur de la classe Personne.
        Initialise le nom, l'âge et la ville de résidence.
        """
        self.__nom = nom  # Nom de la personne (privé)
        self.__age = age  # Âge de la personne (privé)
        self.__ville = ville  # Ville où réside la personne (privé)

        # Lorsqu'une personne est créée, on incrémente directement la population de sa ville
        self.__ville.ajouter_habitant()


  


# ========== INSTANCIATION DES VILLES ==========
paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

# Affichage du nombre d'habitants initial
print(f"Nombre d'habitants à Paris : {paris.get_habitants()}")
print(f"Nombre d'habitants à Marseille : {marseille.get_habitants()}")

# ========== INSTANCIATION DES PERSONNES ==========
john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

# Affichage du nombre d'habitants après ajout des personnes
print(f"Nombre d'habitants à Paris après ajout : {paris.get_habitants()}")
print(f"Nombre d'habitants à Marseille après ajout : {marseille.get_habitants()}")


    









"""Créer une classe Ville avec comme attributs privés un nom et un nombre
d'habitants.
Créer une classe Personne avec les attributs privés suivants : nom, âge et un
objet de la classe ville.
Ajouter la méthode ajouterPopulation dans la classe Personne qui permet
d’augmenter de 1 le nombre d’habitants de la ville.

Créer un objet Ville avec comme arguments “Paris” et 1000000.
Afficher en console le nombre d’habitants de la ville de Paris.

Créer un autre objet Ville avec comme arguments “Marseille” et 861635.
Afficher en console le nombre d’habitants de la ville de Marseille.

Créer les objets suivants :
- John, 45 ans, habitant à Paris
- Myrtille, 4 ans, habitant à Paris.
- Chloé, 18 ans, habitant à Marseille.""" 




"""Voici les lignes de code en littéral sans le code lui-même :

    Créer une classe Ville
        Définir un constructeur prenant en paramètres le nom de la ville et le nombre d’habitants.
        Initialiser deux attributs privés : nom et nombre d’habitants.
        Ajouter un accesseur pour récupérer le nombre d’habitants.

    Créer une classe Personne
        Définir un constructeur prenant en paramètres le nom, l’âge et une instance de la classe Ville.
        Initialiser trois attributs privés : nom, âge et ville.
        Ajouter une méthode ajouterPopulation qui incrémente de 1 le nombre d’habitants de la ville associée à la personne.

    Créer un objet Ville "Paris" avec 1 000 000 habitants.
        Afficher le nombre d’habitants de Paris.

    Créer un objet Ville "Marseille" avec 861 635 habitants.
        Afficher le nombre d’habitants de Marseille.

    Créer trois objets Personne avec leurs informations respectives :
        John, 45 ans, habitant à Paris.
        Myrtille, 4 ans, habitant à Paris.
        Chloé, 18 ans, habitant à Marseille.

    Appeler la méthode ajouterPopulation pour chaque personne créée.

    Afficher le nombre d’habitants de Paris après l’ajout des habitants.

    Afficher le nombre d’habitants de Marseille après l’ajout des habitants."""