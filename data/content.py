"""Contenus marketing : avantages, étapes, profils, FAQ, avis (démo)."""

ADVANTAGES = [
    {"icon": "zap", "title": "Installation rapide", "text": "Intervention claire, sans perdre votre journée."},
    {"icon": "wrench", "title": "Configuration complète", "text": "Système, pilotes et outils prêts à l'emploi."},
    {"icon": "shield", "title": "Installation propre et sécurisée", "text": "Windows propre, mises à jour et bases de sécurité."},
    {"icon": "cpu", "title": "Optimisation des performances", "text": "Démarrage, disque et services passés en revue."},
    {"icon": "pin", "title": "Service disponible à Dakar", "text": "Base à Dieuppeul 2, intervention à domicile dans Dakar et ses environs."},
    {"icon": "phone", "title": "Assistance après installation", "text": "Un suivi si un réglage bloque encore."},
]

STEPS = [
    {
        "num": "01",
        "title": "Vous nous contactez",
        "text": "Expliquez votre besoin : Windows, logiciels, PC lent ou configuration freelance.",
    },
    {
        "num": "02",
        "title": "Nous analysons votre demande",
        "text": "Nous déterminons la prestation adaptée et un prix selon le PC et la complexité.",
    },
    {
        "num": "03",
        "title": "Installation / configuration",
        "text": "Le PC est installé et configuré selon vos outils de travail, avec licences valides.",
    },
    {
        "num": "04",
        "title": "PC prêt à travailler",
        "text": "Vous récupérez un ordinateur opérationnel, prêt à créer, coder ou freelancer.",
    },
]

FREELANCE_PROFILES = [
    {
        "name": "Développeur",
        "tools": ["VS Code", "Git", "Python", "Node.js", "Chrome", "Windows Terminal"],
    },
    {
        "name": "Designer",
        "tools": ["Figma", "Adobe CC", "Chrome", "cloud", "tablette graphique"],
    },
    {
        "name": "Community Manager",
        "tools": ["Chrome", "Canva / Adobe", "Zoom", "Teams", "suite bureautique"],
    },
    {
        "name": "Comptable",
        "tools": ["Excel / Office", "PDF", "logiciel de gestion", "sauvegarde", "imprimante"],
    },
    {
        "name": "Monteur vidéo",
        "tools": ["Adobe / DaVinci", "stockage", "codecs", "Chrome", "sauvegarde"],
    },
    {
        "name": "Étudiant",
        "tools": ["Windows", "Office", "Chrome", "Zoom", "PDF", "VLC"],
    },
    {
        "name": "Entrepreneur",
        "tools": ["Office", "Teams / Zoom", "compta", "cloud", "imprimante"],
    },
]

FAQ = [
    {
        "q": "Est-ce que vous installez Windows 11 ?",
        "a": (
            "Oui, lorsque le PC est compatible (processeur, TPM, Secure Boot, RAM). "
            "Sinon nous installons Windows 10, ou nous vous expliquons les options avant d'intervenir."
        ),
    },
    {
        "q": "Pouvez-vous installer Windows sur un PC lent ?",
        "a": (
            "Oui. Une installation propre et une optimisation aident souvent. "
            "Si le matériel est trop limité (disque saturé, RAM insuffisante), "
            "nous le disons clairement après diagnostic — le prix n'est confirmé qu'à ce moment."
        ),
    },
    {
        "q": "Est-ce que mes fichiers seront supprimés ?",
        "a": (
            "Une installation propre de Windows peut nécessiter un formatage du disque système "
            "et entraîner la perte des données présentes sur cette partition. "
            "Une sauvegarde doit être effectuée avant toute opération risquant d'effacer vos fichiers. "
            "Dites-nous si vous avez des documents importants : nous indiquons la marche à suivre avant d'agir."
        ),
    },
    {
        "q": "Pouvez-vous installer les logiciels dont j'ai besoin pour mon travail ?",
        "a": (
            "Oui : bureautique, développement, design, montage, communication, etc. "
            "Listez vos outils dans le formulaire. Les logiciels payants (Office, Adobe, Windows…) "
            "sont installés."
        ),
    },
    {
        "q": "Faites-vous des interventions à distance ?",
        "a": (
            "Oui, lorsque le problème le permet (configuration, logiciels, certains dépannages). "
            "Une réinstallation complète de Windows ou un PC qui ne démarre plus se fait en général sur place."
        ),
    },
    {
        "q": "Intervenez-vous à domicile à Dakar ?",
        "a": (
            "Oui. Le service est disponible à Dakar et ses environs, avec base à Dieuppeul 2. "
            "Précisez votre quartier dans la demande pour confirmer le déplacement."
        ),
    },
    {
        "q": "Combien coûte une installation Windows ?",
        "a": (
            "À partir de 7000 FCFA. Le montant final dépend du modèle, de l'état du PC "
            "et des logiciels à configurer. Nous confirmons après analyse de votre demande."
        ),
    },
    {
        "q": "Dois-je avoir une licence Windows ?",
        "a": (
            "Non cela n'est pas nécessaire sauf si vous voulez la version officielle de windows."
            "Dans ce cas où vous voulez la version officielle utilisez la licence déjà liée à votre machine, une clé officielle, ou un achat auprès de Microsoft / un revendeur."
        ),
    },
]

# DEMO ONLY — remplacer par de vrais avis clients avant publication.
TESTIMONIALS_ARE_DEMO = True

TESTIMONIALS = [
    {
        "first_name": "Awa",
        "activity": "Graphiste freelance",
        "stars": 5,
        "comment": (
            "PC réinstallé le matin, Adobe et Figma configurés l'après-midi. "
            "J'ai pu livrer un client le soir même."
        ),
    },
    {
        "first_name": "Mamadou",
        "activity": "Développeur",
        "stars": 5,
        "comment": (
            "Windows propre, Git, VS Code et Node.js. Explications claires, sans usine à gaz."
        ),
    },
    {
        "first_name": "Fatou",
        "activity": "Comptable",
        "stars": 5,
        "comment": (
            "Ordinateur lent depuis des mois. Après optimisation, Excel et les PDF s'ouvrent normalement."
        ),
    },
    {
        "first_name": "Ibrahima",
        "activity": "Community manager",
        "stars": 4,
        "comment": (
            "Pack freelance nickel : Chrome, Office, Zoom. Intervention à Dieuppeul 2, ponctuel."
        ),
    },
    {
        "first_name": "Khady",
        "activity": "Étudiante",
        "stars": 5,
        "comment": (
            "Installation Windows 11 et outils de cours. Prix expliqué avant, pas de surprise."
        ),
    },
    
]
