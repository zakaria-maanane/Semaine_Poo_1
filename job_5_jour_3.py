
"""Job 5 """
import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie
    
    def attaquer(self, adversaire):
        degats = random.randint(5, 15)
        adversaire.vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} et inflige {degats} points de dégâts!")
    
    def est_vivant(self):
        return self.vie > 0
    
    def afficher_vie(self):
        print(f"{self.nom} a {self.vie} points de vie restants.")

class Jeu:
    def __init__(self):
        self.niveau = None
    
    def choisirNiveau(self):
        print("Choisissez un niveau de difficulté: \n1. Facile (Vie: 50)\n2. Moyen (Vie: 40)\n3. Difficile (Vie: 30)")
        choix = input("Entrez le numéro du niveau: ")
        if choix == "1":
            self.niveau = 50
        elif choix == "2":
            self.niveau = 40
        elif choix == "3":
            self.niveau = 30
        else:
            print("Choix invalide, sélection par défaut: Moyen (Vie: 40)")
            self.niveau = 40
    
    def lancerJeu(self):
        self.choisirNiveau()
        joueur = Personnage("Héros", self.niveau)
        ennemi = Personnage("Monstre", self.niveau)
        
        print(f"Début du combat! {joueur.nom} ({joueur.vie} PV) vs {ennemi.nom} ({ennemi.vie} PV)\n")
        
        while joueur.est_vivant() and ennemi.est_vivant():
            input("Appuyez sur Entrée pour attaquer...")
            joueur.attaquer(ennemi)
            ennemi.afficher_vie()
            
            if ennemi.est_vivant():
                ennemi.attaquer(joueur)
                joueur.afficher_vie()
                print(f"{joueur.nom}: {joueur.vie} PV | {ennemi.nom}: {ennemi.vie} PV\n")
        
        self.verifierGagnant(joueur, ennemi)
    
    def verifierGagnant(self, joueur, ennemi):
        if joueur.est_vivant():
            print(f"{joueur.nom} a gagné le combat! Félicitations!")
        else:
            print(f"{ennemi.nom} a gagné! Vous avez perdu...")

if __name__ == "__main__":
    jeu = Jeu()
    jeu.lancerJeu()




"""Créez un jeu de combat en utilisant la POO.

À tour de rôle, votre personnage et l’ennemi attaquent. Le but étant de
vaincre l’ennemi (vie à zéro).

Votre programme doit contenir au minimum deux classes, Personnage et
Jeu.

Commencer par créer une classe nommée Personnage prenant des
paramètres de construction : nom (string) et vie(int).
Créez au minimum une méthode attaquer qui enlève des points à son
adversaire.

Ensuite créer la classe Jeu ne prenant pas de paramètre. Créer une méthode
choisirNiveau qui permet de demander au joueur le niveau de difficulté.
Celui-ci sera stocké dans l’attribut niveau. En fonction du niveau choisi, le nombre de points de vie du joueur ainsi que
de l'ennemi seront différents.
Créer lancerJeu, méthode qui utilise l’attribut niveau. Cette méthode aura
pour but d’instancier deux objets Personnage, un qui représente le joueur et
l’autre l'ennemi avec un nombre de points défini en fonction du niveau.

Implémenter le déroulement d’une partie en demandant au joueur le niveau
de difficulté et pensez à ajouter une méthode qui vérifie la santé de vos
personnages ainsi qu’une méthode permettant de vérifier qui a gagné."""