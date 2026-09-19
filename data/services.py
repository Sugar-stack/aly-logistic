"""Catalogue des prestations Y Aly Logiciel. Modifiez ce fichier pour changer les services."""

SERVICES = [
    {
        "id": "windows",
        "icon": "windows",
        "name": "Installation Windows",
        "summary": (
            "Installation propre de Windows avec configuration complète du système, "
            "pilotes, mises à jour et paramètres essentiels."
        ),
        "points": [
            "Windows 10 / Windows 11 selon compatibilité",
            "Installation propre",
            "Pilotes",
            "Windows Update",
            "Configuration de base",
            "Optimisation",
        ],
        "cta": "Choisir ce service",
        "legal": "Aucune licence Windows n'est nécessaire sauf si vous voulez la version officielle",
    },
    {
        "id": "freelance",
        "icon": "briefcase",
        "name": "Pack Freelance",
        "summary": (
            "Un ordinateur immédiatement opérationnel pour votre activité : "
            "Windows, outils du quotidien et configuration de base, sans perdre de temps."
        ),
        "points": [
            "Installation Windows",
            "Google Chrome",
            "Microsoft Office (licence client)",
            "Lecteur PDF",
            "7-Zip",
            "VLC",
            "Outils de visioconférence",
            "Outils de communication",
            "Configuration système",
        ],
        "cta": "Choisir le Pack Freelance",
        "legal": "Les logiciels payants  peuvent être installés officiellement ou en version crackés (la méthode choisi peux faire varier es prix).",
    },
    {
        "id": "software",
        "icon": "apps",
        "name": "Logiciels professionnels",
        "summary": (
            "Installation et configuration de logiciels selon votre métier. "
            "Vous indiquer la liste ; nous préparons un environnement de travail propre."
        ),
        "points": [
            "Bureautique",
            "Comptabilité",
            "Programmation",
            "Design",
            "Montage vidéo",
            "Architecture",
            "Gestion",
            "Communication",
            "Outils freelance",
        ],
        "cta": "Demander des logiciels",
        "legal": (
            "Y Aly Logiciel installe  des logiciels cracks et des logiciels officiels. "
            "Pour tout logiciel payant, le client doit disposer d'une licence valide ou se procurer le crack."
        ),
        "examples": [
            "Microsoft Office",
            "Visual Studio Code",
            "Adobe Creative Cloud",
            "Figma",
            "Zoom",
            "Microsoft Teams",
            "Google Chrome",
            "Git",
            "Python",
            "Node.js",
            "VLC",
            "7-Zip",
        ],
    },
    {
        "id": "optimize",
        "icon": "gauge",
        "name": "Optimisation PC",
        "summary": (
            "Votre ordinateur est lent ? Nous diagnostiquons les causes du ralentissement "
            "et optimisons Windows pour améliorer les performances."
        ),
        "points": [
            "Nettoyage logiciel",
            "Désinstallation des programmes inutiles",
            "Optimisation du démarrage",
            "Vérification des services",
            "Nettoyage des fichiers temporaires",
            "Optimisation Windows",
            "Vérification de l'espace disque",
        ],
        "cta": "Optimiser mon PC",
        "legal": "",
    },
    {
        "id": "complete",
        "icon": "desktop",
        "name": "Configuration PC pour freelance",
        "summary": (
            "Transformer un PC fraîchement installé en véritable poste de travail : "
            "système, outils, sécurité, sauvegarde et cloud."
        ),
        "points": [
            "Windows",
            "Navigateurs",
            "Bureautique",
            "Outils de communication",
            "Outils de travail",
            "Sécurité de base",
            "Sauvegarde",
            "Configuration du cloud",
        ],
        "cta": "Configurer mon poste",
        "legal": "",
    },
    {
        "id": "support",
        "icon": "headset",
        "name": "Assistance informatique",
        "summary": (
            "Un problème ponctuel ou une configuration qui bloque ? "
            "Nous intervenons à domicile à Dakar ou à distance selon le cas."
        ),
        "points": [
            "PC lent",
            "Problèmes Windows",
            "Installation de logiciels",
            "Pilotes",
            "Wi-Fi",
            "Imprimante",
            "Bluetooth",
            "Problèmes de démarrage",
            "Configuration générale",
        ],
        "cta": "Demander de l'aide",
        "legal": "",
    },
]

SOFTWARE_CATEGORIES = [
    {
        "name": "Bureautique",
        "items": ["Microsoft Office", "LibreOffice", "Google Chrome", "lecteur PDF", "7-Zip"],
    },
    {
        "name": "Comptabilité",
        "items": ["Outils de facturation", "tableurs avancés", "suite bureautique"],
    },
    {
        "name": "Programmation",
        "items": ["Visual Studio Code", "Git", "Python", "Node.js", "terminaux et SDK"],
    },
    {
        "name": "Design",
        "items": ["Figma", "Adobe Creative Cloud", "outils de prototypage"],
    },
    {
        "name": "Montage vidéo",
        "items": ["suites Adobe", "lecteurs et codecs", "stockage et export"],
    },
    {
        "name": "Architecture",
        "items": ["logiciels CAO du client", "visualiseurs, PDF et bureautique"],
    },
    {
        "name": "Gestion",
        "items": ["outils de suivi", "cloud", "messagerie professionnelle"],
    },
    {
        "name": "Communication",
        "items": ["Zoom", "Microsoft Teams", "WhatsApp Desktop", "e-mail"],
    },
    {
        "name": "Outils freelance",
        "items": ["navigateur", "visioconférence", "cloud", "sauvegarde", "imprimante"],
    },
]
