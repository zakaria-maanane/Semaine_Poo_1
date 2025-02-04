"""JOB 3 Affichage des valeurs  : 
Je crée une méthode ( une fonction de class ) qu'on appel addition 
et on crée une variable résultat qui stocke le calcul
 """

class Operation:
    def __init__(self, nombre1=0, nombre2=0): 
        # Mon constructeur : __init__ ; mon instance principale : self, et mes objets
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    # ma Methode : addition
    def addition(self):

        resultat = self.nombre1 + self.nombre2
        print(f"Le résultat de l'addition est : {resultat}")

# Instanciation de la classe
operation1 = Operation(12, 3)


print(f"Le nombre1 est {operation1.nombre1} et Le nombre2 est {operation1.nombre2}")


print(operation1)


operation1.addition()

