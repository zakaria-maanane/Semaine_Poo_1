import random
import tkinter as tk
from tkinter import messagebox

class Part:
    def __init__(self, name, material):
        self.name = name
        self.material = material
    
    def change_material(self, new_material):
        self.material = new_material
    
    def __str__(self):
        return f"{self.name} en {self.material}"

class Ship:
    def __init__(self, name):
        self.name = name
        self.__parts = {
            "Mât": Part("Mât", "Bois"),
            "Coque": Part("Coque", "Acier"),
            "Voile": Part("Voile", "Tissu")
        }
        self.history = []
    
    def display_state(self):
        return "\n".join(str(part) for part in self.__parts.values())
    
    def replace_part(self, part_name, new_part):
        if part_name in self.__parts:
            self.__parts[part_name] = new_part
            self.history.append(f"Remplacement de {part_name} par {new_part}")
    
    def change_part(self, part_name, new_material):
        if part_name in self.__parts:
            self.__parts[part_name].change_material(new_material)
            self.history.append(f"Modification de {part_name}: {new_material}")
    
    def random_event(self):
        event = random.choice(["usure", "tempête"])
        if event == "usure":
            part_name = random.choice(list(self.__parts.keys()))
            self.__parts[part_name].change_material("Endommagé")
            self.history.append(f"{part_name} a subi une usure !")
        elif event == "tempête":
            part_name = random.choice(list(self.__parts.keys()))
            self.__parts[part_name].change_material("Cassé")
            self.history.append(f"{part_name} a été cassé par une tempête !")

class RacingShip(Ship):
    def __init__(self, name, max_speed):
        super().__init__(name)
        self.max_speed = max_speed
    
    def display_speed(self):
        return f"Vitesse maximale: {self.max_speed} noeuds"

class ShipApp:
    def __init__(self, root, ship):
        self.root = root
        self.ship = ship
        self.root.title("Gestion du Bateau")
        
        self.label = tk.Label(root, text=f"État du {self.ship.name}")
        self.label.pack()
        
        self.state_text = tk.Text(root, height=10, width=40)
        self.state_text.pack()
        
        self.update_state()
        
        self.change_button = tk.Button(root, text="Modifier une pièce", command=self.change_part)
        self.change_button.pack()
        
        self.history_button = tk.Button(root, text="Voir l'historique", command=self.show_history)
        self.history_button.pack()
        
        self.event_button = tk.Button(root, text="Événement aléatoire", command=self.trigger_event)
        self.event_button.pack()
    
    def update_state(self):
        self.state_text.delete(1.0, tk.END)
        self.state_text.insert(tk.END, self.ship.display_state())
    
    def change_part(self):
        part_name = tk.simpledialog.askstring("Changer pièce", "Nom de la pièce:")
        new_material = tk.simpledialog.askstring("Changer pièce", "Nouveau matériau:")
        if part_name and new_material:
            self.ship.change_part(part_name, new_material)
            self.update_state()
    
    def show_history(self):
        messagebox.showinfo("Historique", "\n".join(self.ship.history))
    
    def trigger_event(self):
        self.ship.random_event()
        self.update_state()

if __name__ == "__main__":
    ship = RacingShip("Barba Rossa", 25)
    root = tk.Tk()
    app = ShipApp(root, ship)
    root.mainloop()

"""Le paradoxe de Thésée vous a inspiré à appliquer les concepts de la
programmation orientée objet que vous connaissez bien, tels que
l'encapsulation, l'abstraction, le passage par référence, et l'héritage, et à
explorer ce thème.
1. Création de la classe Part
○ Définissez une classe Part avec les attributs name (ex. "Mât") et
material (ex. "Bois").
○ Ajoutez une méthode change_material(new_material) pour
modifier le matériau.
○ Implémentez une méthode __str__ pour afficher une description
de la pièce.

2. Création de la classe Ship
○ Définissez une classe Ship avec un nom et un dictionnaire privé
__parts contenant plusieurs instances de Part.
○ Ajoutez une méthode display_state() pour lister les pièces du
bateau.
○ Implémentez une méthode replace_part(part_name,
new_part) pour remplacer une pièce existante.

3. Passage par référence
a. Ajoutez une méthode change_part(part_name, new_material)
pour changer directement le matériau d'une pièce existante.
b. Montrez que les objets Part sont modifiés directement en
mémoire.

4. Création de la classe dérivée RacingShip
○ Créez une classe RacingShip qui hérite de Ship.
○ Ajoutez un attribut supplémentaire max_speed.
○ Ajoutez une méthode display_speed() pour afficher la vitesse
maximale.

5. Interaction et personnalisation
○ Créez un menu interactif avec des options pour remplacer des
pièces, modifier des matériaux, ou afficher l'état du bateau.
○ Ajoutez un historique des modifications pour suivre l'évolution du
bateau.

6. Les plus
1. Ajoutez une interface utilisateur
○ Utilisez Tkinter pour créer une interface graphique simple
permettant de remplacer les pièces ou de consulter l'état du
bateau.

2. Intégrez un suivi historique
○ Enregistrez toutes les modifications apportées au bateau pour
visualiser les étapes de son évolution.

3. Simulation avancée
○ Ajoutez des événements aléatoires (usure des pièces, tempêtes)
pour enrichir la simulation."""