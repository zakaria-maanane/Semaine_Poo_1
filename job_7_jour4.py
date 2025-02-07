"""Job 7"""



import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur
    
    def points(self):
        if self.valeur in ['J', 'Q', 'K']:
            return 10
        elif self.valeur == 'A':
            return 11  # L'as peut aussi valoir 1, la gestion se fait dans Jeu
        else:
            return int(self.valeur)
    
    def __str__(self):
        return f"{self.valeur} de {self.couleur}"

class Jeu:
    def __init__(self):
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']
        self.paquet = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
        random.shuffle(self.paquet)
        self.joueur_main = []
        self.croupier_main = []
    
    def tirer_carte(self, main):
        main.append(self.paquet.pop())
    
    def calculer_score(self, main):
        score = sum(carte.points() for carte in main)
        as_count = sum(1 for carte in main if carte.valeur == 'A')
        while score > 21 and as_count:
            score -= 10  # Transformer un As de 11 à 1
            as_count -= 1
        return score
    
    def afficher_main(self, main):
        return ', '.join(str(carte) for carte in main)
    
    def jouer(self):
        self.joueur_main = [self.paquet.pop(), self.paquet.pop()]
        self.croupier_main = [self.paquet.pop(), self.paquet.pop()]
        
        print(f"Votre main: {self.afficher_main(self.joueur_main)} (Score: {self.calculer_score(self.joueur_main)})")
        print(f"Carte visible du croupier: {self.croupier_main[0]}")
        
        while self.calculer_score(self.joueur_main) < 21:
            action = input("Voulez-vous prendre une carte ? (o/n) ")
            if action.lower() == 'o':
                self.tirer_carte(self.joueur_main)
                print(f"Votre main: {self.afficher_main(self.joueur_main)} (Score: {self.calculer_score(self.joueur_main)})")
                if self.calculer_score(self.joueur_main) > 21:
                    print("Vous avez dépassé 21 ! Vous avez perdu.")
                    return
            else:
                break
        
        print("Le croupier joue...")
        while self.calculer_score(self.croupier_main) < 17:
            self.tirer_carte(self.croupier_main)
        
        print(f"Main du croupier: {self.afficher_main(self.croupier_main)} (Score: {self.calculer_score(self.croupier_main)})")
        
        joueur_score = self.calculer_score(self.joueur_main)
        croupier_score = self.calculer_score(self.croupier_main)
        
        if croupier_score > 21 or joueur_score > croupier_score:
            print("Félicitations, vous avez gagné !")
        elif joueur_score < croupier_score:
            print("Le croupier a gagné.")
        else:
            print("Match nul !")

# Lancer une partie
jeu = Jeu()
jeu.jouer()






"""Développer votre version du célèbre jeu Blackjack. Le but est de faire le plus
de points sans dépasser 21. Chaque carte représente une valeur :
- de 2 à 10 : ces cartes ont pour valeur sa valeur nominale
- une figure a pour valeur 10 points
- un as 1 ou 11 points au choix  Le jeu commence avec les joueurs qui reçoivent chacun 2 cartes. Ensuite, le
joueur peut choisir de "prendre" (recevoir) une ou plusieurs cartes
supplémentaires pour tenter d'améliorer sa main, ou de "passer" et laisser le
tour au croupier. Le croupier prend des cartes jusqu'à ce qu'il ait au moins 17
points, puis s'arrête. Si la main du joueur dépasse 21, il perd immédiatement.
Si le total de la main du joueur est supérieur à celui du croupier, le joueur
gagne. Sinon, c'est le croupier qui gagne.

Créer au minimum deux classes Carte et Jeu.

La classe Carte aura au minimum un attribut valeur et couleur. La classe Jeu
quant à elle devra gérer l’ensemble des cartes. Les cartes du jeu seront
stockées dans un attribut paquet représenté par une liste et contenant 52
cartes.

Créer toutes les méthodes nécessaires pour jouer une partie."""