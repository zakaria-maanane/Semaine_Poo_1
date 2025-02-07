
"""Job 2 """

class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    
    def bonjour(self):
        print(f"Bonjour, je m'appelle {self.nom}.")

class Eleve(Personne):
    def __init__(self, nom, age=15):  # Age défini par défaut à 15 ans
        super().__init__(nom, age)
    
    def allerEnCours(self):
        print("Je vais en cours.")

class Professeur(Personne):
    def __init__(self, nom, age, matiere):
        super().__init__(nom, age)
        self.matiere = matiere
    
    def enseigner(self):
        print("Le cours commence.")

# Création d'un élève et appel des méthodes
eleve = Eleve("Lucas")
eleve.bonjour()
eleve.allerEnCours()

# Création d'un professeur et appel des méthodes
professeur = Professeur("M. Dupont", 40, "Mathématiques")
professeur.bonjour()
professeur.enseigner()

""" Consigne : À l’aide de la classe Personne, Eleve et Professeur créent au-dessus, faites
dire bonjour à votre élève grâce à la méthode bonjour ainsi que “Je vais en
cours” grâce à la méthode allerEnCours. Redéfinir l'âge de l’élève à 15 ans.

Créez un objet Professeur, 40 ans, faites dire bonjour à votre professeur et
commencez le cours grâce à la méthode enseigner."""
