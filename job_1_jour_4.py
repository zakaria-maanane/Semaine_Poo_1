"""Job 1 jour 4 """


class Personne:
    def __init__(self, age=14):
        self.age = age  # Attribut age initialisé à 14 par défaut
    
    def afficherAge(self):
        print(f"J'ai {self.age} ans")  # Affichage de l'âge
    
    def bonjour(self):
        print("Hello")  # Message de bienvenue
    
    def modifierAge(self, nouvel_age):
        self.age = nouvel_age  # Modification de l'âge


# Définition de la classe Eleve qui hérite de Personne
class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")  
    
    def afficherAge(self):
        print(f"J'ai {self.age} ans")  # Affichage spécifique à l'élève



class Professeur:
    def __init__(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee  # Attribut privé
    
    def enseigner(self):
        print("Le cours va commencer")  


# Instanciation des objets
personne = Personne()
eleve = Eleve()

# Affichage de l'âge de l'élève par défaut
eleve.afficherAge()





"""Créer une classe Personne qui aura comme attribut age prenant un entier et
initialisé à 14 par défaut. Ajouter une méthode afficherAge qui affichera en
console l'âge de la personne et une méthode bonjour qui écrit en console
‘Hello’. Créer une méthode modifierAge prenant en paramètre un entier et
permettant de modifier l'âge de la personne.
Créer une classe Eleve qui hérite de la classe Personne qui n’a pas d’attribut
et une méthode publique allerEnCours qui affiche : “Je vais en cours” ainsi
qu’une méthode afficherAge qui écrit en console : “J’ai XX ans”.
Créer une classe Professeur avec un attribut privé matiereEnseignee, qui
indiquera la matière du professeur, et une méthode publique enseigner qui
affiche : “Le cours va commencer”. Instancier une classe Personne et une classe Eleve. Afficher l'âge par défaut
de l’élève en console."""