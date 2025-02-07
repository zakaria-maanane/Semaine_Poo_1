
class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0
    
    def marquerUnBut(self):
        self.buts += 1
        print(f"{self.nom} a marqué un but!")
    
    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1
        print(f"{self.nom} a effectué une passe décisive!")
    
    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1
        print(f"{self.nom} a reçu un carton jaune!")
    
    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1
        print(f"{self.nom} a reçu un carton rouge!")
    
    def afficherStatistiques(self):
        print(f"\nStatistiques de {self.nom} (#{self.numero} - {self.position}):")
        print(f"Buts: {self.buts}, Passes décisives: {self.passes_decisives}, Cartons jaunes: {self.cartons_jaunes}, Cartons rouges: {self.cartons_rouges}\n")

class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []
    
    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)
        print(f"{joueur.nom} a été ajouté à l'équipe {self.nom}.")
    
    def afficherStatistiquesJoueurs(self):
        print(f"\nStatistiques de l'équipe {self.nom}:")
        for joueur in self.joueurs:
            joueur.afficherStatistiques()
    
    def mettreAJourStatistiquesJoueur(self, nom, action):
        for joueur in self.joueurs:
            if joueur.nom == nom:
                if action == "but":
                    joueur.marquerUnBut()
                elif action == "passe":
                    joueur.effectuerUnePasseDecisive()
                elif action == "jaune":
                    joueur.recevoirUnCartonJaune()
                elif action == "rouge":
                    joueur.recevoirUnCartonRouge()
                return
        print("Joueur non trouvé.")

# Création des équipes
teamA = Equipe("Les Aigles")
teamB = Equipe("Les Lions")

# Création des joueurs
joueur1 = Joueur("Paul", 10, "Attaquant")
joueur2 = Joueur("Lucas", 7, "Milieu")
joueur3 = Joueur("Antoine", 5, "Défenseur")
joueur4 = Joueur("Hugo", 1, "Gardien")

# Ajout des joueurs aux équipes
teamA.ajouterJoueur(joueur1)
teamA.ajouterJoueur(joueur2)
teamB.ajouterJoueur(joueur3)
teamB.ajouterJoueur(joueur4)

# Simulation d'un match
teamA.mettreAJourStatistiquesJoueur("Paul", "but")
teamA.mettreAJourStatistiquesJoueur("Lucas", "passe")
teamB.mettreAJourStatistiquesJoueur("Antoine", "jaune")
teamB.mettreAJourStatistiquesJoueur("Hugo", "rouge")

# Affichage des statistiques après le match
teamA.afficherStatistiquesJoueurs()
teamB.afficherStatistiquesJoueurs()



"""consignes : Créer une classe pour représenter un joueur ainsi qu'une classe pour
représenter une équipe de foot. La classe Joueur doit avoir les attributs suivants : nom, numéro, position,
nombre de buts marqués, passes décisives effectuées, cartons jaunes reçus
et cartons rouges reçus. Tous ces attributs doivent être initialisés lors de la
création de l’objet Joueur.

Cette classe doit posséder les méthodes suivantes :
➔ marquerUnBut,
➔ effectuerUnePasseDecisive,
➔ recevoirUnCartonJaune,
➔ recevoirUnCartonRouge,
➔ afficherStatistiques.

Ces méthodes permettent de mettre à jour les statistiques du joueur.

La classe Equipe doit avoir les attributs nom et liste de joueurs. Le nom de
l’équipe et la liste de joueurs (liste vide par défaut) doivent être initialisés
dans le constructeur.  Ajouter les méthodes suivantes dans la classe Equipe :
- ajouterJoueur : cette méthode ajoute un joueur à l’équipe.
- AfficherStatistiquesJoueurs : cette méthode permet d’afficher toutes
les statistiques de l’ensemble des joueurs.
- mettreAJourStatistiquesJoueur : cette méthode permet de mettre à
jour les statistiques d’un joueur (buts, cartons ...). Créez plusieurs joueurs avec les paramètres de votre choix et ajoutez-les aux
équipes.

Présenter l’ensemble des joueurs de chaque équipe. Utiliser les différentes
méthodes afin de simuler un match, marquer un but, avoir un carton rouge...
Et afficher à nouveau les statistiques des joueurs."""