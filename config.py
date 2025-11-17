# config.py

# --- Statistiques de base pour les personnages ---
# TP = Points de Technique (Spirit)

CHARACTERS = {
    "mark": {
        "name": "Mark Evans",
        "role": "Gardien",
        "stats": {"tir": 40, "defense": 90, "endurance": 80, "tp_max": 100},
        "techniques": ["Main Magique (TP: 30)"],
        "is_recruitable": False  # Le joueur principal
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

# --- Lieux (Rooms) ---
ROOMS = {
    "terrain_principal": {
        "name": "Terrain de foot principal",
        "description": "Le terrain d'entraînement. Le gazon est un peu boueux, mais le temps est idéal pour un match.",
        "exits": {"nord": "club_house", "sud": "rue_commercante"},
        "npcs": ["axel"],
        "challenge": True
    },
    "club_house": {
        "name": "Club-house de Raimon",
        "description": "Un petit local désordonné. L'équipement est rangé dans un coin.",
        "exits": {"sud": "terrain_principal"},
        "npcs": ["joueur_aleatoire_a"],
        "challenge": False
    },
    "rue_commercante": {
        "name": "Rue Commerçante",
        "description": "Une rue animée. On entend l'écho des discussions. Vous cherchez peut-être un magasin d'équipement ?",
        "exits": {"nord": "terrain_principal"},
        "npcs": [],
        "challenge": False
    }
}

# --- Objets (Items) ---
ITEMS = {
    "cahier_vent": {
        "name": "Cahier : Leçons du Vent",
        "description": "Permet d'apprendre une technique de dribble de type Vent.",
        "effect": {"learn_technique": "Tornade d'Acier"},
        "is_consumable": True
    },
    "bouteille_eau": {
        "name": "Bouteille d'eau",
        "description": "Restaure 20 Points de Technique (TP).",
        "effect": {"restore_tp": 20},
        "is_consumable": True
    }
}