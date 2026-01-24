class Quest:
    def __init__(self, title, description, reward=None):
        self.title = title
        self.description = description
        self.reward = reward
        self.started = False # La quête est-elle active ?
        self.completed = False # La quête est-elle finie ?

    def start(self):
        """Active la quête."""
        if not self.started:
            self.started = True
            print(f"\n--- NOUVELLE QUÊTE : {self.title} ---")
            print(f"{self.description}\n")

    def complete(self):
        """Marque la quête comme terminée."""
        if not self.completed:
            self.completed = True
            print(f"\n--- QUÊTE TERMINÉE : {self.title} ---")
            if self.reward:
                print(f"Récompense : {self.reward}")

    def check(self, game):
        """Vérifie si les conditions de réussite sont remplies. À surcharger."""
        return self.completed

    def is_finished(self):
        return self.completed

# Quête : Avoir un objet spécifique dans son inventaire
class ItemQuest(Quest):
    def __init__(self, title, description, item_name, reward=None):
        super().__init__(title, description, reward)
        self.item_name = item_name

    def check(self, game):
        if self.completed: return True
        # On vérifie si le joueur a l'objet
        if self.item_name in game.player.inventory:
            self.complete()
        return self.completed

# Quête : Aller dans un lieu spécifique
class MoveQuest(Quest):
    def __init__(self, title, description, room_name, reward=None):
        super().__init__(title, description, reward)
        self.room_name = room_name

    def check(self, game):
        if self.completed: return True
        # On vérifie si le joueur est dans la bonne pièce
        if game.player.current_room.name == self.room_name:
            self.complete()
        return self.completed

# Quête : Parler à un PNJ spécifique
class InteractionQuest(Quest):
    def __init__(self, title, description, character_name, reward=None):
        super().__init__(title, description, reward)
        self.character_name = character_name

    def check(self, game):
        if self.completed: return True
        # On cherche le personnage dans tout le jeu pour voir s'il a parlé
        for char in game.characters:
            if char.name == self.character_name and char.has_spoken:
                self.complete()
                break
        return self.completed

