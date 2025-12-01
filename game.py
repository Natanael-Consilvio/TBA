# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
    
    # Setup the game
    def setup(self): 

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go
        
        # Setup rooms

        Club_de_Raimon = Room("Club de Raimon", "C'est l'iconique club de foot du collège Raimon.")
        self.rooms.append(Club de Raimon)
        Terrain = Room("Terrain", "Le terrain de foot du collège Raimon.")
        self.rooms.append(Terrain)
        Vestiaire = Room("Vestiaire", "Vestiaire du club. Vous pouvez discuter avec les joueurs du club présent.")
        self.rooms.append(Vestiaire)
        Salle_secrète = Room("Salle secrète", "Lieu résidant un mystérieux bouquin.")
        self.rooms.append(Salle secrète)
        Le_magasin_de_sports = Room("Le magasin de sports", "Lieu pour acheter des équipements afin d'améliorer vos personnages.")
        self.rooms.append(Le magasin de sports)
        La_zone_de_recrutement = Room("La zone de recrutement", "Lieu pour recruter des joueurs afin d'améliorer son équipe.")
        self.rooms.append(La zone de recrutement)

        Le_club_Kirkwood = Room("Le club Kirkwood", "Le club du collège Kirkwood, adversaire de Raimon.")
        self.rooms.append(Le club Kirkwood)

        Forêt = Room("Forêt", "Forêt liant le club Raimon et Kirkwood.")
        self.rooms.append(Forêt)

        # Create exits for rooms

        # MODIFICATION : Sens unique (Exercice "Première version")
        # On peut aller de Forest vers Cave (N), mais on ne pourra pas revenir (voir cave.exits)
        Club_de_Raimon.exits = {"N" : Terrain, "E" : Le_magasin_de_sports, "S" : None, "O" : Forêt}
        
        Terrain.exits = {"N" : La_zone_de_recrutement, "E" : Vestiaire, "S" : Club_de_Raimon, "O" : Le_club_Kirkwood}
        
        # Cave : La sortie SUD vers Forest est None (Sens unique, impossible de revenir)
        Vestiaire.exits = {"N" : Salle_secrete, "E" : None, "S" : None, "O" : Terrain}
        
        # MODIFICATION : Connexion vers le nouveau lieu "Attic" (Grenier) au Nord
        Salle_secrète.exits = {"N" : None, "E" : None, "S" : None, "O" : None}
        
        # Sorties du Grenier (on ne peut que redescendre au Sud)
        Le_magasin_de_sports.exits = {"N" : None, "E" : None, "S" : None, "O" : Club_de_Raimon}

        La_zone_de_recrutement.exits = {"N" : None, "E" : None, "S" : Terrain, "O" : None}
        
        # MODIFICATION : Passage interdit et connexion Dungeon
        # Passage interdit : "E" vers swamp est mis à None (on ne peut pas aller au marais depuis le château)
        # Connexion Dungeon : "O" mène au donjon
        Le_club_Kirkwood.exits = {"N" : None, "E" : Terrain, "S" : Forêt, "O" : None}

        # Sorties du Donjon (on revient au chateau par l'Est)
        Forêt.exits = {"N" : Le_club_Kirkwood, "E" : Club_de_Raimon, "S" : None, "O" : None}

        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = Club_de_Raimon

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

        # MODIFICATION : Gestion commande vide (Exercice "Première version")
        if not command_string.strip():
            return

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()

