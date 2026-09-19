# Guide de déploiement - Aly Logistic

## Configuration locale

1. Créer un mot de passe d'application Gmail :
   - https://myaccount.google.com/security
   - Authentification à 2 facteurs > Mots de passe d'application
   - Créer un mot de passe pour "Mail"

2. Configurer le fichier `.env` :
   ```
   MAIL_USERNAME=alylatyr@gmail.com
   MAIL_PASSWORD=votre_mot_de_passe_application
   MAIL_DEFAULT_SENDER=alylatyr@gmail.com
   MAIL_USE_TLS=True
   MAIL_PORT=587
   MAIL_SERVER=smtp.gmail.com
   SECRET_KEY=votre_clé_secrète
   ```

3. Installer les dépendances :
   ```bash
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. Tester localement :
   ```bash
   python app.py
   ```

## Déploiement sur Render

1. Créer un compte sur https://render.com

2. Créer un nouveau "Web Service"

3. Connecter votre repository GitHub

4. Configuration :
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Runtime**: Python 3

5. Variables d'environnement (dans Render) :
   - `MAIL_USERNAME`: alylatyr@gmail.com
   - `MAIL_PASSWORD`: votre_mot_de_passe_application
   - `MAIL_DEFAULT_SENDER`: alylatyr@gmail.com
   - `MAIL_USE_TLS`: True
   - `MAIL_PORT`: 587
   - `MAIL_SERVER`: smtp.gmail.com
   - `SECRET_KEY`: générer une clé aléatoire

6. Déployer !

## Déploiement sur PythonAnywhere

1. Créer un compte sur https://www.pythonanywhere.com

2. Créer un nouveau "Web App"

3. Configuration :
   - **Python version**: 3.11
   - **Web framework**: Flask
   - **Working directory**: /home/yourusername/vazzy

4. Upload du code :
   - Via Git ou Drag & Drop

5. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

6. Configurer les variables d'environnement dans les paramètres

7. Redémarrer l'application

## Avantages de cette solution

- ✅ Pas de problèmes de spam comme Formspree
- ✅ Envoi direct depuis votre Gmail
- ✅ Contrôle total sur le format des emails
- ✅ Pas de service tiers pour les formulaires
- ✅ Fonctionne parfaitement avec Flask
