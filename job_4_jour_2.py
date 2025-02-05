"""Job 4"""

class Student:
    def __init__(self, nom: str, prenom: str, student_id: int):
        """
        Constructeur de la classe Student.
        Initialise les attributs privés avec des valeurs fournies et un nombre de crédits à 0.
        """
        self.__nom = nom  # Nom de l'étudiant (privé)
        self.__prenom = prenom  # Prénom de l'étudiant (privé)
        self.__student_id = student_id  # Identifiant de l'étudiant (privé)
        self.__credits = 0  # Nombre de crédits initialisé à 0 (privé)
        self.__level = self.__student_eval()  # Niveau de l'étudiant basé sur l'évaluation des crédits

    def add_credits(self, credits: int):
        """
        Ajoute des crédits à l'étudiant.
        Vérifie que la valeur ajoutée est strictement positive.
        """
        if isinstance(credits, int) and credits > 0:
            self.__credits += credits
            self.__level = self.__student_eval()  # Met à jour le niveau après modification des crédits
        else:
            print("Erreur : Le nombre de crédits ajouté doit être un entier strictement positif.")

    def get_credits(self) -> int:
        """Retourne le nombre de crédits de l'étudiant."""
        return self.__credits

    def __student_eval(self) -> str:
        """
        Méthode privée qui évalue le niveau de l'étudiant en fonction de ses crédits.
        Retourne un niveau sous forme de chaîne de caractères.
        """
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def student_info(self):
        """
        Affiche les informations de l'étudiant : nom, prénom, identifiant et niveau.
        """
        print(f"Nom = {self.__nom}")
        print(f"Prénom = {self.__prenom}")
        print(f"id = {self.__student_id}")
        print(f"Niveau = {self.__level}")

# Instanciation d'un étudiant
etudiant = Student("John", "Doe", 145)

# Ajout de crédits à trois reprises
etudiant.add_credits(10)
etudiant.add_credits(20)
etudiant.add_credits(30)

# Affichage du nombre total de crédits
print(f"Le nombre de crédits de {etudiant._Student__nom} {etudiant._Student__prenom} est de {etudiant.get_credits()} points\n")

# Affichage des informations de l'étudiant
etudiant.student_info()

"""Créer une classe nommée Student qui a comme attributs privés un nom, un
prénom, un numéro d’étudiants et un nombre de crédits par défaut à zéro. La
méthode add_credits permet d’ajouter un nombre de crédits au total de
celui de l’étudiant. Ce mutateur doit s’assurer que la valeur passée en
argument est supérieure à zéro pour garantir l’intégrité de la valeur.
Instancier un objet représentant l’étudiant John Doe qui possède le numéro
d’étudiant 145. Ajoutez-lui des crédits à trois reprises et imprimez son total de
crédits en console.  ( suite de l'exo est dans la capture d'ecran )  ; Pour des mesures de confidentialité, l'établissement ne souhaite pas
divulguer la façon dont elle évalue le niveau de ses étudiants. Pour répondre
à cette problématique, créer une méthode nommée student_eval qui sera
privée Cette méthode retourne “Excellent” si le nombre de crédits est égal ou
supérieur à 90, “Très bien” si le nombre est supérieur ou égal à 80, “Bien” si le
nombre est supérieur ou égale à 70, “Passable” si égale ou supérieure à 60 et
“Insuffisant” si inférieur à 60.
Ajouter l’attribut privé nommé level dans le constructeur de la classe Student
qui prend en valeur la méthode student_eval. Créer une méthode
student_info qui écrit en console les informations de l’étudiant (nom,
prénom, identifiant et son niveau)."""