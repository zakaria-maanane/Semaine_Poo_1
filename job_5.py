"""Job 5 Ici on a crée des methodes 
pour changer les valeurs de nos attributs ,
 pour reafficher avec le changment il faut reappeler
   nos methodes afficher"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    
    def afficherLesPoints(self):
        print(f"Coordonnées du point: ({self.x}, {self.y})")
    

    #methode afficherX afficherY
    def afficherX(self):
        print(f" x = {self.x}")
    
    def afficherY(self):
        print(f" y = {self.y}")
    


    #methodes chargerX chargerY
    def changerX(self, changement_x):
        self.x = changement_x
    
    def changerY(self, changement_y):
        self.y = changement_y

#========================
point = Point(3, 3)

point.afficherLesPoints()
point.afficherX()
point.afficherY()

#changement
point.changerX(5)
point.changerY(6)

#affichage du changement 
point.afficherLesPoints()
point.afficherX()
point.afficherY()

"""Job 5 Créez une classe nommée Point avec les attributs x et y correspondant aux
coordonnées horizontales et verticales du point. Les deux attributs doivent
être initialisés dans le constructeur.

La classe Point doit posséder les méthodes suivantes :
➔ afficherLesPoints qui affiche les coordonnées des points.
➔ afficherX et afficherY qui affiche respectivement x et y.
➔ changerX et changerY qui change la valeur des attributs x et y."""