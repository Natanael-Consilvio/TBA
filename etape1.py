monde = {
    "entree": {
        "nom": "Entrée de l'École Raimon",
        "description": "Vous êtes devant le grand portail de l'école. On entend des cris venant du terrain.",
        "sorties": {"nord": "couloir", "ouest": "terrain", "est": "ville"},
        "objets": [],  # Inventaire du lieu vide
        "pnj": []
    },
    
    "couloir": {
        "nom": "Couloir Principal",
        "description": "Un long couloir avec des casiers. Ça sent la cire et le vieux papier.",
        "sorties": {"sud": "entree", "ouest": "vestiaires", "est": "bureau_coach"},
        "objets": ["distributeur"],
        "pnj": ["eleve"]
    },

    "vestiaires": {
        "nom": "Vestiaires du Club",
        "description": "L'odeur de transpiration est forte. Les bancs sont en désordre.",
        "sorties": {"est": "couloir"}, # Sortie unique vers l'est
        "objets": ["couteau_suisse", "bouteille_eau", "ballon_use"],
        "pnj": ["mark_evans"]
    },

    "terrain": {
        "nom": "Terrain de Football",
        "description": "La pelouse est parfaite. Les gradins sont vides pour l'instant.",
        "sorties": {"est": "entree", "nord": "passage_service"},
        "objets": [],
        "pnj": ["adversaire"]
    },

    "passage_service": {
        "nom": "Passage de Service",
        "description": "Un chemin étroit et sombre derrière les tribunes.",
        "sorties": {"sud": "terrain", "nord": "salle_secrete"},
        "objets": ["carton_vide"],
        "pnj": [],
        "verrouille": True, # Pour gérer le "Passage interdit"
        "objet_requis": "couteau_suisse" # L'objet qu'il faut pour débloquer
    },

    "salle_secrete": {
        "nom": "Salle Secrète du Club",
        "description": "Une pièce cachée remplie de vieux trophées.",
        "sorties": {}, # SENS UNIQUE : Pas de sortie définie ici (piège) !
        "objets": ["cahier_techniques"],
        "pnj": []
    },
    
    "ville": {
        "nom": "Ruelle de la Ville",
        "description": "C'est calme ici. Il y a une boutique fermée.",
        "sorties": {"ouest": "entree"},
        "objets": [],
        "pnj": []
    }
}

CHARACTERS = {
    "mark": {
        "name": "Mark Evans"







# Variable pour savoir où est le joueur actuellement
position_actuelle = "entree"
inventaire_joueur = ["couteau_suisse"] 

def afficher_lieu(lieu_id):
    lieu = monde[lieu_id]
    print(f"\n=== {lieu['nom']} ===")
    print(lieu['description'])
    
    # Afficher les sorties possibles (pour aider le joueur ou non)
    directions = ", ".join(lieu['sorties'].keys())
    print(f"Directions possibles : {directions}")
    
    # Afficher les objets visibles (Consigne: Observer l’environnement)
    if lieu['objets']:
        print(f"Objets visibles : {', '.join(lieu['objets'])}")
    if lieu['pnj']:
        print(f"Personnes présentes : {', '.join(lieu['pnj'])}")

def changer_lieu(direction):
    global position_actuelle
    
    lieu_courant = monde[position_actuelle]
    
    # 1. Vérifier si la direction existe (Consigne : Gestion direction inconnue)
    if direction in lieu_courant['sorties']:
        prochain_lieu_id = lieu_courant['sorties'][direction]
        prochain_lieu = monde[prochain_lieu_id]
        
        # 2. Vérifier si c'est un passage interdit (Consigne : Passage interdit)
        # On regarde si la clé 'verrouille' existe et est True
        if prochain_lieu.get("verrouille", False):
            objet_cle = prochain_lieu.get("objet_requis")
            if objet_cle in inventaire_joueur:
                print(f"> Vous utilisez {objet_cle} pour dégager le passage !")
                prochain_lieu["verrouille"] = False # On déverrouille pour toujours
                position_actuelle = prochain_lieu_id
                afficher_lieu(position_actuelle)
            else:
                print(f"> PASSAGE INTERDIT ! Le chemin est bloqué. Il vous faudrait : {objet_cle}")
        
        else:
            # Déplacement normal
            position_actuelle = prochain_lieu_id
            afficher_lieu(position_actuelle)
            
    else:
        print("> Vous ne pouvez pas aller par là.")

# --- Petite boucle de test ---
afficher_lieu(position_actuelle)

while True:
    choix = input("\nOù voulez-vous aller ? (nord, sud, est, ouest, quitter) : ").lower()
    
    if choix == "quitter":
        break
    elif choix == "":
        print("Commande vide. Essayez une direction.") # Consigne: Commande vide
    else:
        changer_lieu(choix)
