# Socialautomation

Ce dépôt contient un script d’automatisation de publication de médias pour **Instagram** et **TikTok**.

## Contenu du dépôt

```text
Socialautomation/
├── README.md
└── auto-poster/
    ├── auto_post.py
    ├── lance_auto_post.bat
    └── README.md
```

Le script principal est dans :  
`/home/runner/work/Socialautomation/Socialautomation/auto-poster/auto_post.py`

## Ce que fait le script

- Sélectionne un média (image/vidéo) aléatoirement depuis un dossier local
- Publie sur Instagram via `instagrapi`
- Publie sur TikTok via `tiktok-uploader`
- N’exécute la publication qu’aux heures autorisées : **5h, 8h, 11h, 14h, 17h, 20h**

## Prérequis

- Windows
- Python 3 installé (commande `python` disponible)
- Compte Instagram et TikTok (idéalement comptes de test)
- Dépendance Python Instagram :
  ```bat
  pip install instagrapi
  ```
- Projet `tiktok-uploader` cloné en local :  
  https://github.com/FunnyMin/tiktok-uploader

## Installation et configuration

1. Ouvrir le fichier :
   `/home/runner/work/Socialautomation/Socialautomation/auto-poster/auto_post.py`
2. Renseigner les variables de configuration en haut du script :
   - `MEDIA_FOLDER`
   - `INSTAGRAM_USERNAME`
   - `INSTAGRAM_PASSWORD`
   - `INSTAGRAM_CAPTION`
   - `TIKTOK_UPLOADER_PATH`
   - `TIKTOK_USERNAME`
   - `TIKTOK_DESCRIPTION`
   - `PYTHON_EXECUTABLE`
3. Vérifier que le dossier configuré dans `MEDIA_FOLDER` contient des fichiers compatibles :
   - Images : `.jpg`, `.jpeg`, `.png`, `.webp`
   - Vidéos : `.mp4`, `.mov`, `.avi`, `.mkv`

## Lancer le script

Depuis le dossier :
`/home/runner/work/Socialautomation/Socialautomation/auto-poster`

Exécution via batch Windows :

```bat
lance_auto_post.bat
```

## Automatiser (Planificateur de tâches Windows)

Exemple recommandé :
- Déclenchement quotidien
- Répétition toutes les 3 heures
- Heure de départ 05:00
- Action : lancer `lance_auto_post.bat`

Le script ignore automatiquement les exécutions hors créneau.

## Journaux et diagnostic rapide

Le script affiche des logs en console :
- dossier média introuvable
- dépendance Instagram manquante
- script TikTok CLI introuvable
- erreurs de publication

## Sécurité et bonnes pratiques

- Utiliser des comptes de test avant production
- Respecter les CGU des plateformes
- Éviter de stocker des mots de passe en clair sur une machine partagée

## Documentation détaillée

La documentation détaillée du module est disponible dans :  
`/home/runner/work/Socialautomation/Socialautomation/auto-poster/README.md`
