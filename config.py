"""
Configuration unique de Aly Logistic.
Modifiez ce fichier pour changer le nom, les contacts, WhatsApp et les tarifs.
"""

# --- Identité ---
COMPANY_NAME = "Aly IT Services"
COMPANY_INITIALS = "AIT"
COMPANY_TAGLINE = "Services informatiques à Dakar"
COMPANY_SHORT = "Installation Windows, logiciels et optimisation PC"

# --- Contact (facile à modifier) ---
# Numéro WhatsApp au format international, SANS + ni espaces. Ex. Sénégal : 221771234567
WHATSAPP_NUMBER = ""
PHONE_DISPLAY = "+221 70 721 69 86"
PHONE_TEL = "+221707216986"
EMAIL = "alylatyr@gmail.com"
CITY = "Dieuppeul 2, Dakar, Sénégal"

# Zones desservies (pas d'adresse physique tant qu'elle n'est pas fournie)
SERVICE_AREAS = [
    "Dieuppeul 2",
    "Dakar-Plateau",
    "Almadies",
    "Ngor",
    "Ouakam",
    "Mermoz",
    "Sacré-Cœur",
    "Point E",
    "Fann",
    "Liberté",
    "Grand Dakar",
    "Parcelles Assainies",
]

# Réseaux sociaux : laisser une chaîne vide pour masquer l'icône
SOCIAL_LINKS = {
    "facebook": "",
    "instagram": "",
    "linkedin": "",
    "tiktok": "",
}

# --- WhatsApp ---
WHATSAPP_DEFAULT_MESSAGE = (
    "Bonjour, je souhaite avoir des informations concernant vos services "
    "d'installation Windows et logiciels."
)

# --- Tarifs (FCFA) — prix d'entrée, pas des forfaits définitifs ---
PRICES = {
    "windows": {
        "id": "windows",
        "name": "Installation Windows + pilotes + configuration de base",
        "from_amount": 7000,
        "unit": "",
        "highlight": False,
        "features": [
            "Windows 8, 10 ou 11 selon compatibilité",
            "Installation propre",
            "Pilotes et mises à jour",
            "Configuration de base",
        ],
    },
    "freelance": {
        "id": "freelance",
        "name": "Pack Freelance",
        "from_amount": 15000,
        "unit": "",
        "highlight": True,
        "features": [
            "Installation Windows incluse",
            "Outils bureautique et communication",
            "PC immédiatement opérationnel",
        ],
    },
    "software": {
        "id": "software",
        "name": "Installation de logiciels",
        "from_amount": 3000,
        "unit": " / logiciel",
        "highlight": False,
        "features": [
            "Selon votre métier",
            "Configuration de base",
            "Plusieurs logiciels possibles",
        ],
    },
    "optimize": {
        "id": "optimize",
        "name": "Optimisation PC",
        "from_amount": 5000,
        "unit": "",
        "highlight": False,
        "features": [
            "Diagnostic des ralentissements",
            "Nettoyage et démarrage",
            "Espace disque",
            "Windows plus fluide",
        ],
    },
    "complete": {
        "id": "complete",
        "name": "Installation de jeux tels que assassin creed black flag et suite, la saga resident evil etc",
        "from_amount": 10000,
        "unit": "",
        "highlight": False,
        "features": [
            "Assassin creed",
            "Pes Fifa",
            "tomb raider",
            "Max payne",
            "Specs Ops etc",
        ],
    },
}

PRICE_DISCLAIMER = (
    "Le prix final peut varier selon le modèle du PC, le nombre de logiciels "
    "et la complexité de l'intervention. Un diagnostic précède toute confirmation."
)

# --- SEO ---
SEO_TITLE = f"Installation Windows Dakar | Logiciels PC | Optimisation | {COMPANY_NAME} - Dieuppeul 2"
SEO_DESCRIPTION = (
    f"Expert informatique à Dakar, basé à Dieuppeul 2. Installation Windows 10/11, "
    f"logiciels professionnels, optimisation PC, configuration freelance. "
    f"Intervention à domicile dans tout Dakar. Service rapide et fiable. "
    f"Contactez {COMPANY_NAME} pour vos besoins informatiques."
)
SEO_KEYWORDS = (
    "installation Windows Dakar, informaticien Dakar, installation logiciels Dakar, "
    "optimisation PC Dakar, dépannage informatique Dakar, maintenance PC Dakar, "
    "configuration ordinateur Dakar, services informatiques Dieuppeul 2, "
    "installation Windows Sénégal, assistance informatique Dakar, "
    "réparation PC Dakar, formatage ordinateur Dakar, "
    "installateur Windows Dakar Plateau, informaticien à domicile Dakar, "
    "support informatique Sénégal, technicien informatique Dakar"
)

SITE_URL = "https://aly-tech.vercel.app"
