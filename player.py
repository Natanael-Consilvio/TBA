class Player():
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history=[]
    
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
        return True

    def go_back(self):
        if len(self.history)<1:
            return False
        previous_room=self.history.pop()

        self.current_room=previous_room

        print(self.current_room.get_long_description())
        return True

    def get_history_string(self):
        if not self.history:
            return "\nVous n'avez pas encore visité d'autres pièces."
        output= "\nVous avez déjà visité les pièces suivantes:"

        for room in self.history:
            output += f"\n\t-{room.description}"
        return output
