# Auto Poster Instagram + TikTok (Windows)

## Objectif
Ce dossier contient un script Python qui publie automatiquement un média (image ou vidéo) choisi aléatoirement depuis un dossier local sur Instagram et TikTok.

Le script ne publie que pendant les créneaux suivants : **5h, 8h, 11h, 14h, 17h, 20h**.

## Arborescence

```text
auto-poster/
├── auto_post.py
├── lance_auto_post.bat
└── README.md
```

## Prérequis
- Windows
- Python 3 installé et accessible avec `python`
- Un compte Instagram de test
- Un compte TikTok de test
- `instagrapi` pour Instagram
- `tiktok-uploader` pour TikTok : https://github.com/FunnyMin/tiktok-uploader

## Installation
1. Installer Python 3 (cocher "Add Python to PATH").
2. Installer la dépendance Instagram :
   ```bat
   pip install instagrapi
   ```
3. Cloner `tiktok-uploader` sur votre PC (exemple : `C:\\tools\\tiktok-uploader`).
4. Installer les dépendances de `tiktok-uploader` selon sa documentation.
5. Ouvrir `auto_post.py` et configurer les variables en haut du script :
   - `MEDIA_FOLDER`
   - `INSTAGRAM_USERNAME`
   - `INSTAGRAM_PASSWORD`
   - `INSTAGRAM_CAPTION`
   - `TIKTOK_UPLOADER_PATH`
   - `TIKTOK_USERNAME`
   - `TIKTOK_DESCRIPTION`
   - `PYTHON_EXECUTABLE`

## Exécution manuelle
Depuis ce dossier :
```bat
lance_auto_post.bat
```

## Planification Windows (Planificateur de tâches)
Exemple simple :
1. Ouvrir **Planificateur de tâches**.
2. Créer une tâche de base.
3. Déclencheur : **Tous les jours**.
4. Répéter la tâche : **toutes les 3 heures**, démarrage à **05:00**.
5. Action : **Démarrer un programme**.
6. Programme/script : chemin vers `lance_auto_post.bat`.
7. Valider.

Le script vérifie lui-même les heures autorisées, donc il ignore les exécutions hors créneau.

## Sécurité et avertissements
- Utiliser des **comptes de test** avant tout usage en production.
- Respecter les **CGU** d’Instagram et TikTok.
- L’automatisation peut entraîner des restrictions de compte.
- Éviter de stocker les mots de passe en clair dans un environnement partagé.

## Crédits
- Instagram : [instagrapi](https://github.com/adw0rd/instagrapi)
- TikTok : [tiktok-uploader](https://github.com/FunnyMin/tiktok-uploader)
