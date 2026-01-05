# Fichier : character.py

import random

class Character:
    """
    Cette classe représente un personnage non-joueur (PNJ).
    """
    def __init__(self, name, description, current_room, msgs):
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs # Liste des messages que le PNJ peut dire

    def __str__(self):
        return f"{self.name} : {self.description}"

    def move(self):
        """
        Déplace le personnage au hasard vers une pièce adjacente.
        Retourne True si le personnage s'est déplacé, False sinon.
        """
        # Une chance sur deux de se déplacer
        if random.choice([True, False, False, False, False]):
            exits = self.current_room.exits
            # Filtrer les sorties valides (celles qui ne sont pas None)
            valid_exits = [room for room in exits.values() if room is not None]
            
            if len(valid_exits) > 0:
                next_room = random.choice(valid_exits)
                
                # On retire le personnage de la pièce actuelle
                del self.current_room.characters[self.name]
                
                # On met à jour sa pièce actuelle
                self.current_room = next_room
                
                # On l'ajoute dans la nouvelle pièce
                self.current_room.characters[self.name] = self
                return True
        
        return False

    def get_msg(self):
        """
        Affiche le prochain message du personnage de manière cyclique.
        """
        if not self.msgs:
            return "Ce personnage n'a rien à dire."
        
        # Récupère le premier message et le retire de la liste
        msg = self.msgs.pop(0)
        # Remet le message à la fin de la liste pour le cycle
        self.msgs.append(msg)
        return msg