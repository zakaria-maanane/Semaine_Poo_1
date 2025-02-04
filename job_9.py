
"""Job 9 J'ai reussit a faire ce job mais j'ai 
malgré tout compris le code pour progresser """

class Produit:
    def __init__(self, nom, prixHT, TVA):
        """ Constructeur de la classe Produit 
        - Initialise les attributs : nom, prixHT (prix hors taxes) et TVA.
        """
        self.nom = nom  # Nom du produit
        self.prixHT = prixHT  # Prix hors taxes (HT)
        self.TVA = TVA  # Taux de TVA en pourcentage (ex: 20 pour 20%)

    def calculerPrixTTC(self):
        """ Calcule et retourne le prix TTC (Prix avec TVA) """
        return self.prixHT * (1 + self.TVA / 100)

    def afficherInfos(self):
        """ Retourne une chaîne avec toutes les informations du produit """
        return f"Produit : {self.nom}, Prix HT : {self.prixHT}€, TVA : {self.TVA}%, Prix TTC : {self.calculerPrixTTC():.2f}€"

    def modifierNom(self, nouveau_nom):
        """ Modifie le nom du produit """
        self.nom = nouveau_nom

    def modifierPrixHT(self, nouveau_prixHT):
        """ Modifie le prix HT du produit """
        self.prixHT = nouveau_prixHT

    def getNom(self):
        """ Retourne le nom du produit """
        return self.nom

    def getPrixHT(self):
        """ Retourne le prix HT du produit """
        return self.prixHT

    def getTVA(self):
        """ Retourne le taux de TVA du produit """
        return self.TVA

# ======= TEST DU CODE ======= #

# Création de plusieurs produits
produit1 = Produit("Ordinateur", 1000, 20)  # Prix HT = 1000€, TVA = 20%
produit2 = Produit("Smartphone", 800, 20)   # Prix HT = 800€, TVA = 20%
produit3 = Produit("Casque Audio", 150, 10) # Prix HT = 150€, TVA = 10%

# Affichage des informations initiales
infos_produit1 = produit1.afficherInfos()
infos_produit2 = produit2.afficherInfos()
infos_produit3 = produit3.afficherInfos()

print("Informations initiales des produits :")
print(infos_produit1)
print(infos_produit2)
print(infos_produit3)

# Modification des noms et des prix
produit1.modifierNom("PC Gamer")
produit1.modifierPrixHT(1200)

produit2.modifierNom("iPhone Pro")
produit2.modifierPrixHT(950)

produit3.modifierNom("Casque Bluetooth")
produit3.modifierPrixHT(180)

# Affichage des nouvelles informations après modifications
print("\nAprès modification des produits :")
print(produit1.afficherInfos())
print(produit2.afficherInfos())
print(produit3.afficherInfos())










""""Créez la classe Produit avec des attributs nom, prixHT, TVA. Implémentez la
méthode CalculerPrixTTC qui retourne le prix produit avec la TVA. Ajoutez la
méthode afficher qui liste l’ensemble des informations du produit.
Créez plusieurs produits et calculez leurs TVA. Ajoutez des méthodes permettant de modifier le nom du produit et son prix.
Ainsi que des méthodes permettant de retourner chaque information du
produit.
Modifiez le nom et le prix de chaque produit et affichez en console le nouveau
prix des produits.
La fonction print() ne doit pas être utilisée dans la classe Produit.
Sur vos scripts doit apparaître l’ensemble des méthodes appelées tout au
long des exercices."""
