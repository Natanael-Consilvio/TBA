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

        self.directions = ["N", "E", "S", "O", "U", "D"] #rajout des directions dans la classe
    
    # Setup the game
    def setup(self): 

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer (N, E, S, O, U, D)", Actions.go, 1)
        self.commands["go"] = go
        
        # Setup rooms
        history = Command("history", " : afficher l'historique des pièces visitées", Actions.history, 0)
        self.commands["history"] = history
        
        back = Command("back", " : revenir à la pièce précédente", Actions.back, 0)
        self.commands["back"] = back


        look = Command("look", " : regarder autour de soi", Actions.look, 0)
        self.commands["look"] = look
        
        take = Command("take", " <item> : prendre un objet", Actions.take, 1)
        self.commands["take"] = take
        
        drop = Command("drop", " <item> : poser un objet", Actions.drop, 1)
        self.commands["drop"] = drop
        
        check = Command("check", " : voir son inventaire", Actions.check, 0)
        self.commands["check"] = check
   
        # 11 lieux dont ceux de U et D
        
        Club_de_Raimon = Room("Club de Raimon", "à l'iconique club de foot du collège Raimon.")
        self.rooms.append(Club_de_Raimon)
        Terrain = Room("Terrain", "au terrain de foot.")
        self.rooms.append(Terrain)
        Tribunes = Room("Tribunes", "aux tribunes du terrain de foot")
        self.rooms.append(Tribunes)
        Vestiaire = Room("Vestiaire", "au vestiaire du club. Vous pouvez discuter avec les joueurs du club présent.")
        self.rooms.append(Vestiaire)
        Salle_secrete = Room("Salle secrète", "dans un lieu où réside un mystérieux bouquin.")
        self.rooms.append(Salle_secrete)
        Le_magasin_de_sports = Room("Le magasin de sports", "au lieu pour acheter des équipements afin d'améliorer vos personnages.")
        self.rooms.append(Le_magasin_de_sports)
        Etage_du_magasin = Room("Etage du magasin", "à l'étage du magasin de sport")
        self.rooms.append(Etage_du_magasin)
        La_zone_de_recrutement = Room("La zone de recrutement", "au lieu pour recruter des joueurs afin d'améliorer son équipe.")
        self.rooms.append(La_zone_de_recrutement)
        Sous_sol = Room("Sous sol", "au sous sol de la zone de recrutement")
        self.rooms.append(Sous_sol)
        Le_club_Kirkwood = Room("Le club Kirkwood", "au club du collège Kirkwood, adversaire de Raimon.")
        self.rooms.append(Le_club_Kirkwood)
        Foret = Room("Forêt", "dans la forêt liant le club Raimon et Kirkwood.")
        self.rooms.append(Foret)


        Club_de_Raimon.exits = {"N" : Terrain, "E" : Le_magasin_de_sports, "S" : None, "O" : Foret}
        
        Terrain.exits = {"N" : La_zone_de_recrutement, "E" : Vestiaire, "S" : Club_de_Raimon, "O" : Le_club_Kirkwood, "U" : Tribunes}
        
        Tribunes.exits = {"D" : Terrain}

        Vestiaire.exits = {"N" : Salle_secrete, "E" : None, "S" : None, "O" : Terrain}
        
        Salle_secrete.exits = {"N" : None, "E" : None, "S" : None, "O" : None}
        
        Le_magasin_de_sports.exits = {"N" : None, "E" : None, "S" : None, "O" : Club_de_Raimon, "U" : Etage_du_magasin}

        Etage_du_magasin.exits = {"D" : Le_magasin_de_sports}

        La_zone_de_recrutement.exits = {"N" : None, "E" : None, "S" : Terrain, "O" : None, "D": Sous_sol}
        
        Sous_sol.exits = {"U" : La_zone_de_recrutement}

        Le_club_Kirkwood.exits = {"N" : None, "E" : Terrain, "S" : Foret, "O" : None}

        Foret.exits = {"N" : Le_club_Kirkwood, "E" : Club_de_Raimon, "S" : None, "O" : None}


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

