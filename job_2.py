"""JOB 2 Affichage des valeurs  : 
Je crée ma classe ,mon constructeur pour que mes objets n'ai pas la meme valeur ,
# Les propriétés sont attribuées aux objets avec self  
 """

class Operation:
    def __init__(self, nombre1=0, nombre2=0): 
    # mon constructeur : __init__  ; mon instance prinicpale : self , et mes objets 
        self.nombre1 = nombre1
        self.nombre2 = nombre2

# Instanciation de la classe
operation1 = Operation(12,3)

print(f"Le nombre1 est {operation1.nombre1} et Le nombre2 est {operation1.nombre2}")

# Affichage de l'objet en console
print(operation1)

