class Item :
    def __init__(self, name, description, weight):
        self.name = name
        self.description = description
        self.weight = weight

    def __str__(self):
        return f"{self.name} : {self.description} ({self.weight} kg)"
    
class Beamer(Item):
    """
    Un Beamer est un objet magique qui permet de se téléporter.
    Il mémorise une pièce lors de sa charge, et permet d'y retourner lors de son utilisation.
    """
    def __init__(self, name, description, weight):
        super().__init__(name, description, weight)
        self.target_room = None # La pièce mémorisée (aucune au départ)

    def charge(self, current_room):
        """Mémorise la pièce actuelle."""
        self.target_room = current_room
        return True

