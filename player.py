class Player():
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history=[]
        self.inventory = {} 
        self.max_weight = 10 #poids max pour inventaire

    def move(self, direction):
        if direction not in self.current_room.exits:
            print(f"\nDirection '{direction}' inconnue ! Utilisez N, E, S, O, U ou D.\n")
            return False

        next_room = self.current_room.exits[direction]

        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False

        self.history.append(self.current_room)
        self.current_room = next_room
        print(self.current_room.get_long_description())
        print(self.current_room.get_inventory_string()) #inventaire exercice
        return True

    def go_back(self):
        if len(self.history)<1:
            return False
        previous_room=self.history.pop()

        self.current_room=previous_room

        print(self.current_room.get_long_description())

        print(self.current_room.get_inventory_string()) #inventaire exercice aussi

        return True

    def get_history_string(self):
        if not self.history:
            return "\nVous n'avez pas encore visité d'autres pièces."
        output= "\nVous avez déjà visité les pièces suivantes:"

        for room in reversed(self.history):
            output += f"\n\t-{room.description}"
        return output

    def take(self, item_name):
        # Vérifier si l'objet est dans la pièce
        if item_name not in self.current_room.inventory:
            print(f"\nL'objet '{item_name}' n'est pas ici.\n")
            return False
        
        item = self.current_room.inventory[item_name]
        
        # Vérifier le poids
        current_weight = sum(i.weight for i in self.inventory.values())
        if current_weight + item.weight > self.max_weight:
            print(f"\nCet objet est trop lourd. Poids actuel: {current_weight}/{self.max_weight} kg.\n")
            return False

        # Transférer l'objet
        del self.current_room.inventory[item_name]
        self.inventory[item_name] = item
        print(f"\nVous avez pris : {item_name}.\n")
        return True

    def drop(self, item_name):
        # Vérifier si le joueur a l'objet
        if item_name not in self.inventory:
            print(f"\nVous n'avez pas l'objet '{item_name}'.\n")
            return False
        
        item = self.inventory[item_name]
        
        # Transférer l'objet 
        del self.inventory[item_name]
        self.current_room.inventory[item_name] = item
        print(f"\nVous avez déposé : {item_name}.\n")
        return True

    def get_inventory_string(self):
        if not self.inventory:
            return "\nVotre inventaire est vide."
        
        output = "\nVous disposez des items suivants :"
        for item in self.inventory.values():
            output += f"\n\t- {item}"
        return output