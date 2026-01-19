# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.


# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

class Actions:

    # MODIFICATION : Définition du dictionnaire de traduction pour les synonymes
    # Les clés sont les synonymes longs, les valeurs sont les codes courts (N, E, S, O, U, D).
    TRADUCTION_DIRECTION = {
        "OUEST": "O",
        "EST": "E",
        "NORD": "N",
        "SUD": "S",
        "UP": "U",
        "DOWN": "D"
    }

    def go(game, list_of_words, number_of_parameters):
        
        player = game.player
        l = len(list_of_words)
        
        # 1. Vérification du nombre de paramètres
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        direction = list_of_words[1]


        # MODIFICATION : Utilisation du dictionnaire pour la traduction (synonymes)
        
        # 2. Mise en majuscule : "ouest" -> "OUEST"
        direction = direction.upper() 

        # 3. Traduction : Si la clé est trouvée dans le dictionnaire, elle est remplacée par le code court.
        #    Sinon, on conserve la valeur de 'direction' (le deuxième argument de .get).
        direction = Actions.TRADUCTION_DIRECTION.get(direction, direction)
        
        
        # 4. Gestion direction inconnue : Vérifie si la direction traduite est autorisée dans le jeu
        if direction not in game.directions:
            print(f"\nDirection '{direction}' inconnue. Utilisez : {game.directions}\n")
            return False

        success = player.move(direction)

        if success:
            print(player.get_history_string())
        return success

    def back(game, list_of_words, number_of_parameters):

        l=len(list_of_words)
        if l!=number_of_parameters +1:
            command_word=list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        player=game.player

        success=player.go_back()

        if not success:
            print("\nImpossible de revenir en arrière, vous êtes au point de départ (ou l'historique est vide).\n")
            return False

        print (player.get_history_string())
        # 5. Déplacement (Player.move se charge de vérifier si la porte existe)
    
        return True
    def history(game, list_of_words, number_of_parameters):
            """
            Print the list of visited rooms.
            """
            l = len(list_of_words)
            # Vérification du nombre de paramètres (doit être 0)
            if l != number_of_parameters + 1:
                command_word = list_of_words[0]
                print(MSG0.format(command_word=command_word))
                return False
            
            player = game.player
            print(player.get_history_string())
            return True
    
    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True


    def look(game, list_of_words, number_of_parameters):
        """ Affiche la description de la pièce et son inventaire """
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        player = game.player
        print(player.current_room.get_long_description())
        print(player.current_room.get_inventory_string()) #pour voir les items dans la room actuelle 
        return True

    def take(game, list_of_words, number_of_parameters):
        """ Prend un objet dans la pièce """
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        item_name = list_of_words[1] # c'est le deuxieme mot (take objet) c'est objet
        game.player.take(item_name)
        return True

    def drop(game, list_of_words, number_of_parameters):
        """ Pose un objet au sol """
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        item_name = list_of_words[1]
        game.player.drop(item_name)
        return True

    def check(game, list_of_words, number_of_parameters):
        """ Affiche l'inventaire du joueur """
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        print(game.player.get_inventory_string()) #ici
        return True
    
    def charge(game, list_of_words, number_of_parameters):
        """Charge le beamer avec la pièce actuelle."""
        player = game.player
        # Vérification paramètres
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Vérifier si le joueur a le beamer sur lui
        if "beamer" not in player.inventory:
            print("\nVous n'avez pas de beamer à charger.\n")
            return False

        # Récupérer l'objet beamer depuis l'inventaire
        beamer = player.inventory["beamer"]
       
        # Action de charger
        beamer.charge(player.current_room)
        print(f"\nLe beamer a mémorisé : {player.current_room.name}.\n")
        return True

    def use(game, list_of_words, number_of_parameters):
        """Utilise le beamer."""
        player = game.player
        # Vérification paramètres
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Vérifier si le joueur a le beamer
        if "beamer" not in player.inventory:
            print("\nVous n'avez pas de beamer à utiliser.\n")
            return False

        beamer = player.inventory["beamer"]
       
        # Action d'utiliser
        return beamer.use(player)
    
    def talk(game, list_of_words, number_of_parameters):
        """Parle à un PNJ présent dans la pièce."""
        player = game.player
        l = len(list_of_words)
        
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        character_name = list_of_words[1]

        # Vérifier si le personnage est dans la pièce
        if character_name not in player.current_room.characters:
            print(f"\n{character_name} n'est pas ici.\n")
            return False
        
        character = player.current_room.characters[character_name]
        print(f"\n{character.name} dit : \"{character.get_msg()}\"\n")
        return True


    # vOir les quêtes
    
    def show_quests(game, list_of_words, number_of_parameters):
        """Affiche la liste des quêtes et leur statut."""
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
           
        print("\n--- Journal de Quêtes ---")
        for q in game.quests:
            status = "[TERMINÉE]" if q.is_finished() else "[EN COURS]"
            print(f"{status} {q.title} : {q.description}")
        print("-------------------------")
        return True