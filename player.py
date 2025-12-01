# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
    
    # Define the move method.
    def move(self, direction):
        
        # MODIFICATION : Gestion direction inconnue (Exercice "Votre propre univers")
        # Vérifie si la direction existe dans les clés (N, E, S, O) avant d'essayer d'y accéder
        if direction not in self.current_room.exits:
            print(f"\nDirection '{direction}' inconnue ! Utilisez N, E, S ou O.\n")
            return False

        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True
