"""Job 6"""
class Commande:
    def __init__(self, numero: int):
        """
        Constructeur de la classe Commande.
        Initialise les attributs avec un numéro de commande, une liste de plats vide et un statut "En cours".
        """
        self.__numero = numero  # Numéro unique de la commande (privé)
        self.__plats = {}  # Dictionnaire contenant les plats commandés (nom du plat -> prix)
        self.__statut = "En cours"  # Statut initial de la commande (privé)

    # Accesseur (getter) pour le numéro de commande
    def get_numero(self) -> int:
        """Retourne le numéro de la commande."""
        return self.__numero

    # Accesseur pour le statut
    def get_statut(self) -> str:
        """Retourne le statut actuel de la commande."""
        return self.__statut

    # Méthode pour ajouter un plat à la commande
    def ajouter_plat(self, nom_plat: str, prix: float):
        """
        Ajoute un plat à la commande sous forme de dictionnaire {nom: prix}.
        """
        if self.__statut == "En cours":  # Vérifie si la commande est toujours modifiable
            if prix > 0:
                self.__plats[nom_plat] = prix
                print(f"Le plat '{nom_plat}' a été ajouté à la commande.")
            else:
                print("Erreur : Le prix doit être supérieur à zéro.")
        else:
            print("Impossible d'ajouter un plat : La commande est déjà terminée ou annulée.")

    # Méthode privée pour calculer le total de la commande
    def __calculer_total(self) -> float:
        """
        Calcule et retourne le total de la commande (prix total des plats).
        """
        return sum(self.__plats.values())

    # Méthode pour calculer la TVA (20% du total)
    def calculer_TVA(self) -> float:
        """
        Retourne le montant de la TVA (20% du total).
        """
        return self.__calculer_total() * 0.20

    # Méthode pour annuler la commande
    def annuler_commande(self):
        """
        Annule la commande si elle est encore en cours.
        """
        if self.__statut == "En cours":
            self.__statut = "Annulée"
            self.__plats.clear()  # Supprime tous les plats de la commande
            print("La commande a été annulée.")
        else:
            print("Impossible d'annuler : La commande est déjà terminée ou annulée.")

    # Méthode pour terminer la commande
    def terminer_commande(self):
        """
        Termine la commande si elle est toujours en cours.
        """
        if self.__statut == "En cours":
            self.__statut = "Terminée"
            print("La commande est maintenant terminée.")
        else:
            print("Impossible de terminer : La commande est déjà terminée ou annulée.")

    # Méthode pour afficher le résumé de la commande
    def afficher_commande(self):
        """
        Affiche les détails de la commande, y compris le total et la TVA.
        """
        print("\n========== RÉCAPITULATIF DE LA COMMANDE ==========")
        print(f"Numéro de commande : {self.__numero}")
        print(f"Statut : {self.__statut}")

        if not self.__plats:
            print("Aucun plat dans la commande.")
        else:
            print("Plats commandés :")
            for plat, prix in self.__plats.items():
                print(f"- {plat} : {prix:.2f} €")

            total = self.__calculer_total()
            tva = self.calculer_TVA()
            print(f"\nTotal HT : {total:.2f} €")
            print(f"TVA (20%) : {tva:.2f} €")
            print(f"Total TTC : {total + tva:.2f} €")
        print("==============================================\n")


# =================== TEST DU PROGRAMME ===================

# Création d'une nouvelle commande
commande1 = Commande(101)

# Ajout de plats
commande1.ajouter_plat("Pizza Margherita", 12.50)
commande1.ajouter_plat("Pâtes Carbonara", 14.00)
commande1.ajouter_plat("Tiramisu", 6.00)

# Affichage de la commande
commande1.afficher_commande()

# Terminer la commande
commande1.terminer_commande()

# Tenter d'ajouter un plat après la terminaison
commande1.ajouter_plat("Café", 2.50)  # Ne fonctionnera pas

# Affichage final
commande1.afficher_commande()

# Essai d'annuler une commande déjà terminée
commande1.annuler_commande()

"""Consigne : Créer une classe Commande avec les attributs privés, numéro de
commande, liste de plats commandés et statut de la commande (en cours,
terminée ou annulée).

Ajouter des méthodes permettant d’ajouter un plat à la commande, annuler
une commande, calculer le total d’une commande privée et afficher une
commande avec son total à payer, ainsi qu’une méthode permettant de
calculer la TVA.

Utiliser l’encapsulation et l’abstraction pour créer cette classe de manière que
les attributs ne puissent pas être modifiés de l’extérieur. La liste des plats
commandés doit être représentée sous forme de dictionnaire avec les noms
des plats, le prix ainsi que le statut de la commande. Sur votre script doit apparaître l’ensemble des méthodes appelées tout au
long de cet exercice."""