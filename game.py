# game.py

#on importe les autres fichiers

from config import ROOM_DATA
from room import Room
from player import Player

class Game:
    def __init__(self):
        self.map = self._load_rooms()
        # Le joueur commence à 'entree', son ID est 'mark'
        self.player = Player("mark", "entree")
        self.is_running = True #le jeu est en marche, si on active l'option "quitter" alors '= False'

    def _load_rooms(self):
        """Charge toutes les pièces en objets Room."""
        map_objects = {}
        for id, data in ROOM_DATA.items():
            map_objects[id] = Room(id, data)
        return map_objects

    def change_room(self, direction):
        """Implémente la logique de déplacement et du passage interdit."""
        current_room = self.map[self.player.current_room_id]
        next_room_id = current_room.check_exit(direction)
        
        if next_room_id:
            next_room = self.map[next_room_id]
            
            # 1. Gestion du Passage Interdit (Consigne 1)
            if next_room.is_locked:
                if next_room.required_item in self.player.inventory:
                    print(f"> Vous utilisez {next_room.required_item} pour dégager le passage !")
                    next_room.is_locked = False # Déverrouillé (mise à jour de l'objet Room)
                    self.player.current_room_id = next_room_id
                else:
                    print(f"> PASSAGE INTERDIT ! Le chemin est bloqué. Il vous faudrait : {next_room.required_item}")
            
            # 2. Déplacement si non verrouillé
            else:
                self.player.current_room_id = next_room_id
                
        else:
            # Consigne: Gestion direction inconnue (implémentée dans le 'else' final)
            print("> Vous ne pouvez pas aller par là.")


    def run(self):
        """Boucle de jeu principale."""
        print("⚽ Bienvenue dans notre INAZUMA ADVENTURE ! ⚡")
        print("Actions de base: 'aller [direction]', 'inventaire', 'quitter'.")

        while self.is_running:
            # Afficher la description du lieu actuel
            current_room = self.map[self.player.current_room_id]
            print(current_room.get_description())

            # Demander la commande au joueur
            choix_brut = input("\n> Que faites-vous ? ").lower().strip()

            if choix_brut == "quitter":
                self.is_running = False
                continue

            # Consigne 3: Commande vide
            if not choix_brut:
                print("Commande vide. Essayez une action.")
                continue

            # Analyse de la commande (simplifiée pour le mouvement)
            mots = choix_brut.split()
            verbe = mots[0]
            argument = " ".join(mots[1:])

            if verbe == "aller":
                self.change_room(argument)
            elif verbe == "inventaire":
                print(self.player.check_inventory())
            else:
                print(f"Action '{verbe}' inconnue.")
                
            print("-" * 40)


if __name__ == "__main__":
    game = Game()
    game.run()