# player.py

class Player:
    def __init__(self, player_id, initial_room_id):
        # nous utilisons les IDs de config.py
        self.id = player_id
        self.current_room_id = initial_room_id
        
        # Votre inventaire initial (pour tester le passage interdit : CONSIGNE)
        self.inventory = ["couteau_suisse"] 

    def check_inventory(self):
        """Affiche le contenu de l'inventaire."""
        if not self.inventory:
            return "Votre inventaire est vide."
        
        output = "\n--- Inventaire du joueur ---\n"
        output += ", ".join(self.inventory)
        return output