# room.py

class Room:
    def __init__(self, room_id, data):
        self.id = room_id
        self.name = data["nom"]
        self.description = data["description"]
        self.exits = data["sorties"]  # {direction: room_id}
        self.items = data["objets"]   # Liste des ID d'objets (strings)
        self.npc_ids = data["pnj"]    # Liste des ID de PNJ (c'est strings aussi)
        
        # Logique du Passage Interdit (CONSIGNE)
        self.is_locked = data.get("verrouille", False) #on check si la salle est verouillee
        self.required_item = data.get("objet_requis") #on check si il faut un objet requis pour ouvrir la salle (exemple : couteau_suisse)

    def get_description(self):
        """Formate la description complete de la piece."""
        
        output = f"\n=== {self.name.upper()} ===\n"    #le nom de la piece
        output += f"{self.description}\n"              #la description de la piece
        
        # Affichage des sorties
        directions = ", ".join(self.exits.keys())            #on check les sorties du dico sorties cf : data["sorties"]
        output += f"Directions possibles : {directions}\n"   #pour l'affichage des directions nord sud est ouest
        
        # Affichage des objets visibles dans la piece (idee : si salle = salle piegee alors activer l'option Fouiller pour obtenir un objet, cf : livre des techniques dans salle_secrete))
        if self.items:
            output += f"Objets visibles : {', '.join(self.items)}\n"   
            
        # Affichage des PNJ
        if self.npc_ids:
            # On utilise les IDs comme noms pour l'instant (pnj est une liste de strings)
            output += f"Personnes présentes : {', '.join(self.npc_ids)}\n" 
            
        return output

    def check_exit(self, direction):
        """Vérifie si une sortie existe. Retourne l'ID de la prochaine pièce ou None."""
        return self.exits.get(direction)