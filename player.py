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

        self.history.apppend(self.current_room)
        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True
