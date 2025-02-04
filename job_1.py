"""JOB 1 Affichage de l'adresse mémoire (RAM) Ox0000023D6.. : 
Je crée ma classe ,mon constructeur pour que mes objets n'ai pas la meme valeur ,
 j'attribue les propriétés a mes objets avec self 
(ici je n'attribue rien dans operation() donc il me donne l'éspace de stockage) """

class Operation:
    def __init__(self, nombre1=0, nombre2=0): 
    # mon constructeur : __init__  ; mon instance prinicpale : self , et mes objets 
        self.nombre1 = nombre1
        self.nombre2 = nombre2

# Instanciation de la classe (ici elle est vide et il n'y a pas de 
# <print f string >elle ne va rien nous donner)
operation1 = Operation()

#test 
operation2 = Operation(2,2)


# Affichage de l'objet en console
print(operation1)

#test 
print(operation2)

