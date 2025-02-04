"""Job 6 Ici on crée une methode qui a la fonction 
de changer la valeur de "age" ,  j'intente ma classe ( crée un objet de ma class ) ,
je print f-sting avec mon attribue d'instance de class "mon_animal.age """
class Animal:
    def __init__(self):
        self.age = 0       # Attribut d'instance
        self.prenom = ""   # Attribut d'instance

    def vieillir(self):    # Méthode qui permet de faire vieillir l'animal
        self.age += 1

# Instanciation de l'objet Animal (Création d'un objet de la classe Animal)
mon_animal = Animal()

# Âge initial
print(f"Âge initial de l'animal: {mon_animal.age}")

# Appel de la méthode vieillir() pour modifier l'attribut age
mon_animal.vieillir()

# Âge mis à jour
print(f"Âge de l'animal après avoir vieilli: {mon_animal.age}")


"""Consignes : Créez une classe Animal avec un attribut age initialisé à zéro et prenom
initialisé vide dans son constructeur.
Instanciez un objet Animal et affichez en console l’attribut âge. Créez une
méthode vieillir qui ajoute 1 à l'âge de l’animal. Faites vieillir votre animal et
affichez son âge mis à jour en console."""
