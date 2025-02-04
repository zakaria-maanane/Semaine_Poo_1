"""Job 4  dans mon constructeur __init__ je met
 mes objets nom et prénom  , création de ma methode SePresenter  
 puis je reurn un f string  , puis instranciation avec les prénoms et noms , 
 je print mes variables personne1 2 .. 
 intanté avec ma class conteneant ma methode """

class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def SePresenter(self):
        return (f"Je suis {self.prenom} {self.nom}.")


# Instanciation des variables 
personne1 = Personne("Dupont", "Jean")

personne2 = Personne("Zakaria", "Maanane")
personne3 = Personne("Cristiano", "Messi")

# Print mes variables intentés
print(personne1.SePresenter())
print(personne2.SePresenter())
print(personne3.SePresenter())
