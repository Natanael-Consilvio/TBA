# Fichier : room.py

class Room:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = {}
        self.characters = {}
    
    def get_exit(self, direction):
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    def get_long_description(self):
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"

    def get_inventory_string(self):
        output = ""
        
        if self.inventory:
            output += "\nOn voit :"
            for item in self.inventory.values():
                output += f"\n\t- {item}"
        
        if self.characters:
            if not output: # Si pas d'objets, on met l'en-tête
                output += "\nOn voit :"
            for char in self.characters.values():
                output += f"\n\t- {char}"
                
        if not output:
            return "\t- Il n'y a rien ici."
            
        return output