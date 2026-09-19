# Y Aly Logiciel — site vitrine (Flask)

Site professionnel pour **Y Aly Logiciel**, services informatiques à Dakar : installation Windows, logiciels, optimisation PC et assistance pour freelances.

Stack : **Python / Flask**, HTML (Jinja), CSS, JavaScript. Pas de piratage ni d’activation illégale : les licences valides restent à la charge du client.

## Lancer le projet

```bash
cd ~/Projects/vazzy
python -m venv .venv
source .venv/bin/activate   # Windows : .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Ouvrir [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Modifier le numéro WhatsApp

Fichier unique : `config.py`

```python
# Format international, sans + ni espaces. Sénégal : 221 + numéro
WHATSAPP_NUMBER = "221770000000"
PHONE_DISPLAY = "+221 77 000 00 00"
PHONE_TEL = "+221770000000"
```

Le message WhatsApp par défaut se trouve dans `WHATSAPP_DEFAULT_MESSAGE`.

## Modifier les informations de contact

Toujours dans `config.py` :

- `COMPANY_NAME`, `COMPANY_INITIALS`, `COMPANY_TAGLINE`
- `EMAIL`
- `CITY`
- `SERVICE_AREAS` (quartiers desservis)
- `SOCIAL_LINKS` (laisser vide pour masquer une icône)
- `SITE_URL` (SEO / sitemap)

## Modifier les tarifs

Dans `config.py`, dictionnaire `PRICES` (montants en FCFA, prix d’entrée).  
Le bandeau d’avertissement est `PRICE_DISCLAIMER`.

L’affichage des cartes se fait via `data/pricing.py` (ne dupliquez pas les montants ailleurs).

## Modifier les services

Fichier `data/services.py` : titres, listes, exemples de logiciels, mentions légales.  
Avantages, étapes, profils freelance, FAQ et avis : `data/content.py`.

**Avis clients :** `TESTIMONIALS_ARE_DEMO = True` et le bandeau indiquent du contenu fictif. Remplacez les témoignages et passez le drapeau à `False` avant publication.

## Architecture

```
app.py                 # routes Flask
config.py              # nom, WhatsApp, tarifs, SEO
data/services.py
data/pricing.py
data/content.py
templates/             # pages + composants
static/css/style.css
static/js/main.js
static/js/form.js
```

## Déployer

Exemple avec Gunicorn derrière nginx :

```bash
pip install -r requirements.txt
gunicorn -w 2 -b 0.0.0.0:8000 app:app
```

1. Renseigner un vrai numéro WhatsApp et un e-mail dans `config.py`.
2. Changer `app.secret_key` dans `app.py`.
3. Mettre `SITE_URL` sur le domaine réel.
4. Remplacer les avis de démonstration.
5. Pointer le serveur web (nginx, Caddy) vers Gunicorn, ou utiliser un PaaS avec `gunicorn app:app`.
