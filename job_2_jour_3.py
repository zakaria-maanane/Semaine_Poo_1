"""Job 2 jour 3"""
class CompteBancaire:
    def __init__(self, numero, nom, prenom, solde, decouvert=False):
        self.__numero = numero
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert
    
    def afficher(self):
        print(f"Compte N°{self.__numero} - Titulaire : {self.__prenom} {self.__nom} - Solde : {self.__solde}€")
    
    def afficherSolde(self):
        print(f"Solde actuel : {self.__solde}€")
    
    def versement(self, montant):
        if montant > 0:
            self.__solde += montant
            print(f"Versement de {montant}€ effectué. Nouveau solde : {self.__solde}€")
        else:
            print("Le montant doit être positif.")
    
    def retrait(self, montant):
        if montant > 0:
            if self.__solde >= montant or self.__decouvert:
                self.__solde -= montant
                print(f"Retrait de {montant}€ effectué. Nouveau solde : {self.__solde}€")
            else:
                print("Fonds insuffisants et découvert non autorisé.")
        else:
            print("Le montant doit être positif.")
    
    def agios(self, taux=5):
        if self.__solde < 0:
            frais = abs(self.__solde) * (taux / 100)
            self.__solde -= frais
            print(f"Agios de {frais}€ appliqués. Nouveau solde : {self.__solde}€")
    
    def virement(self, compte_destinataire, montant):
        if montant > 0:
            if self.__solde >= montant or self.__decouvert:
                self.__solde -= montant
                compte_destinataire.versement(montant)
                print(f"Virement de {montant}€ vers le compte N°{compte_destinataire.__numero} éxecuté.")
            else:
                print("Virement impossible : fonds insuffisants et découvert non autorisé.")
        else:
            print("Le montant doit être positif.")



# Création des comptes
compte1 = CompteBancaire(12345, "Dupont", "Jean", 1000)
compte2 = CompteBancaire(67890, "Martin", "Sophie", -200, decouvert=True)


compte1.afficher()
compte2.afficher()


compte1.retrait(300)
compte2.agios()
compte1.virement(compte2, 200)


compte1.afficherSolde()
compte2.afficherSolde()





"""Voici une description en mots du code Python correspondant à votre demande :  

1. **Création de la classe `CompteBancaire`** avec des attributs privés :
   - Un **numéro de compte**  
   - Un **nom**  
   - Un **prénom**  
   - Un **solde**  
   - Un **attribut découvert** (booléen indiquant si le découvert est autorisé)  

2. **Définition des méthodes :**  
   - `afficher` : Affiche les informations du compte (numéro, nom, prénom, solde).  
   - `afficherSolde` : Affiche uniquement le solde du compte.  
   - `versement` : Ajoute un montant au solde.  
   - `retrait` :  
     - Si le solde est suffisant, soustrait le montant demandé.  
     - Si le solde est insuffisant et que le découvert est autorisé, autorise le retrait.  
     - Sinon, affiche un message d’erreur.  
   - `agios` : Applique des frais supplémentaires si le solde est négatif.  
   - `virement` :  
     - Vérifie si le solde permet le virement.  
     - Déduit le montant du compte source et l’ajoute au compte bénéficiaire.  
     - Affiche un message de confirmation ou d’erreur.  

3. **Création d'une première instance** avec un solde positif.  
4. **Création d'une deuxième instance** avec un solde négatif et un découvert autorisé.  
5. **Test des différentes méthodes :**  
   - Vérification de l’affichage des comptes.  
   - Effectuer un retrait, un versement et vérifier les mises à jour du solde.  
   - Appliquer des agios sur le compte à découvert.  
   - Réaliser un virement du premier compte vers le second pour remettre ce dernier à zéro.  

Cela donne une simulation complète du fonctionnement d'un compte bancaire avec découvert et transactions inter-comptes. 🚀
"""