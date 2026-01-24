# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item, Beamer
from character import Character
from quest import ItemQuest, MoveQuest, InteractionQuest

DEBUG = True


class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None

        self.directions = ["N", "E", "S", "O", "U", "D"] #rajout des directions dans la classe
        self.characters = []
        self.quests = []

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

        charge = Command("charge", " : charger le beamer dans la pièce actuelle", Actions.charge, 0)
        self.commands["charge"] = charge

        use = Command("use", " : utiliser le beamer pour se téléporter", Actions.use, 0)
        self.commands["use"] = use
   
        talk = Command("talk", " <nom> : parler à un personnage", Actions.talk, 1)
        self.commands["talk"] = talk

        quests_cmd = Command("quests"," : afficher les quêtes en cours", Actions.show_quests, 0)
        self.commands["quests"] = quests_cmd

        # 11 lieux dont ceux de U et D
        
        Club_de_Raimon = Room("Club de Raimon", "au club de foot du collège Raimon.")
        self.rooms.append(Club_de_Raimon)
        Terrain = Room("Terrain", "au terrain de foot.")
        self.rooms.append(Terrain)
        Tribunes = Room("Tribunes", "aux tribunes du terrain de foot.")
        self.rooms.append(Tribunes)
        Vestiaire = Room("Vestiaire", "au vestiaire du club.")
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

        #Création des objets
        ballon = Item("ballon", "un ballon de football officiel", 1)
        crampons = Item("crampons", "une paire de crampons usés", 2)
        manuel = Item("manuel", "le manuel technique de l'équipe", 3)
        
        carnet = Item("carnet", "un carnet d'espionnage", 1)
        La_zone_de_recrutement.inventory["carnet"] = carnet

        # Ajout des objets dans les pièces 
        Club_de_Raimon.inventory["ballon"] = ballon
        Vestiaire.inventory["crampons"] = crampons
        Salle_secrete.inventory["manuel"] = manuel

        beamer = Beamer("beamer", "un dispositif de téléportation étrange", 5) # 5kg
        Tribunes.inventory["beamer"] = beamer

        mark = Character("Mark", "le capitaine", Club_de_Raimon, ["Il nous faut des infos sur Kirkwood !", "Va chercher le carnet, vite !"])
        self.characters.append(mark) # On l'ajoute à la liste globale pour le mouvement
        Club_de_Raimon.characters["Mark"] = mark # On l'ajoute à la pièce

        # Exemple 2 : Axel Blaze (Attaquant)
        axel = Character("Axel", "l'attaquant de feu", Vestiaire, ["N'oublie pas les objectifs !", "Passe-moi le ballon !"])
        self.characters.append(axel)
        Vestiaire.characters["Axel"] = axel

        # Exemple 3 : Un rival à Kirkwood
        rival = Character("Rival", "Capitaine de Kirkwood", Le_club_Kirkwood, ["Raimon ne nous battra jamais.", "Pff, amateurs."])
        self.characters.append(rival)
        Le_club_Kirkwood.characters["Rival"] = rival

        q1 = InteractionQuest("Le Capitaine", "Parlez à Mark pour recevoir tes ordres.","Mark")
        self.quests.append(q1)

        q2 = ItemQuest("Le Savoir", "Trouvez le manuel technique dans la Salle Secrète.", "manuel")
        self.quests.append(q2)
       
        q3 = MoveQuest("Espionnage", "Infiltrez-vous dans le club Kirkwood (attention, il vous faut le carnet !).", "Le club Kirkwood")
        self.quests.append(q3)

        # On démarre toutes les quêtes au début (ou on pourrait les activer via PNJ)
        for q in self.quests:
            q.start()

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
            # Vérifier les quêtes et les conditions de fin à chaque tour
            self.check_quests()
            self.check_win_loose()
        return None

    #Vérifier l'état des quêtes
    def check_quests(self):
        for q in self.quests:
            if not q.is_finished():
                q.check(self)

    #Conditions de Victoire / Défaite
    def check_win_loose(self):
        # Défaite : Entrer à Kirkwood SANS le carnet d'espionnage
        if self.player.current_room.name == "Le club Kirkwood" and "carnet" not in self.player.inventory:
            print("\n--- DÉFAITE ---")
            print("Vous êtes entré chez l'ennemi sans vos notes d'espionnage ! Vous êtes repéré et expulsé.")
            self.finished = True
            return

        #Victoire : Toutes les quêtes sont terminées
        all_finished = True
        for q in self.quests:
            if not q.is_finished():
                all_finished = False
                break
       
        if all_finished:
            print("\n--- VICTOIRE ! ---")
            print("Félicitations ! Vous avez accompli toutes les missions de l'équipe Raimon !")
            self.finished = True

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

            # MODIFICATION : Après chaque commande du joueur, on fait bouger les PNJ
            for char in self.characters:
                moved = char.move()
                if moved and DEBUG:
                    print(f"DEBUG: {char.name} s'est déplacé vers {char.current_room.name}")

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

