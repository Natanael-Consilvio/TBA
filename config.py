# config.py

# --- Données du Monde (ROOM_DATA) ---
ROOM_DATA = {
    "entree": {
        "nom": "Entrée de l'École Raimon",
        "description": "Vous êtes devant le grand portail de l'école. On entend des cris venant du terrain.",
        "sorties": {"nord": "couloir", "ouest": "terrain", "est": "ville"},
        "objets": [],
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
        "sorties": {"est": "couloir"}, 
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
        "verrouille": True, # Consigne: Passage interdit
        "objet_requis": "couteau_suisse" 
    },
    "salle_secrete": {
        "nom": "Salle Secrète du Club",
        "description": "Une pièce cachée remplie de vieux trophées.",
        "sorties": {}, # Consigne: Sens unique
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

# --- Données des Personnages (CHARACTERS) --- 

# L'idee n'est pas terminee, on compte juste mettre 4 joueurs pour faire 2vs2 et devoir recruter un joueur

CHARACTERS = {
    "mark": {
        "name": "Mark Evans",
        "role": "Gardien",
        "stats": {"tir": 40, "defense": 90, "endurance": 80, "tp_max": 100},
        "techniques": ["Main Magique (TP: 30)"],
        "is_recruitable": False
    },
    "axel": {
        "name": "Axel Blaze",
        "role": "Attaquant",
        "stats": {"tir": 95, "defense": 30, "endurance": 70, "tp_max": 80},
        "techniques": ["Tir tout-puissant (TP: 40)"],
        "is_recruitable": True
    },
    "joueur_aleatoire_a": {
        "name": "Joueur Lambda A",
        "role": "Milieu",
        "stats": {"tir": 50, "defense": 50, "endurance": 60, "tp_max": 50},
        "techniques": [],
        "is_recruitable": True
    }
}