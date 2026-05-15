from __future__ import annotations

import random
import subprocess
from datetime import datetime
from pathlib import Path

MEDIA_FOLDER = r"C:\\chemin\\vers\\dossier_medias"
INSTAGRAM_USERNAME = "votre_identifiant_instagram"
INSTAGRAM_PASSWORD = "votre_mot_de_passe_instagram"
INSTAGRAM_CAPTION = "Publication automatisée"

TIKTOK_UPLOADER_PATH = r"C:\\chemin\\vers\\tiktok-uploader"
TIKTOK_USERNAME = "votre_identifiant_tiktok"
TIKTOK_DESCRIPTION = "Publication automatisée"
PYTHON_EXECUTABLE = "python"

HEURES_AUTORISEES = {5, 8, 11, 14, 17, 20}
EXTENSIONS_IMAGES = {".jpg", ".jpeg", ".png", ".webp"}
EXTENSIONS_VIDEOS = {".mp4", ".mov", ".avi", ".mkv"}


def journaliser(message: str) -> None:
    horodatage = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{horodatage}] {message}")


def est_dans_un_creneau_valide() -> bool:
    return datetime.now().hour in HEURES_AUTORISEES


def recuperer_medias(dossier: Path) -> list[Path]:
    extensions = EXTENSIONS_IMAGES | EXTENSIONS_VIDEOS
    return [
        fichier
        for fichier in dossier.iterdir()
        if fichier.is_file() and fichier.suffix.lower() in extensions
    ]


def choisir_media_aleatoire() -> Path | None:
    dossier = Path(MEDIA_FOLDER)
    if not dossier.exists() or not dossier.is_dir():
        journaliser(f"Dossier média introuvable : {dossier}")
        return None

    medias = recuperer_medias(dossier)
    if not medias:
        journaliser("Aucun média compatible trouvé dans le dossier configuré.")
        return None

    return random.choice(medias)


def publier_instagram(media: Path) -> None:
    try:
        from instagrapi import Client
    except ImportError:
        journaliser("Erreur Instagram : instagrapi n'est pas installé.")
        return

    try:
        client = Client()
        client.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)

        if media.suffix.lower() in EXTENSIONS_VIDEOS:
            client.video_upload(path=str(media), caption=INSTAGRAM_CAPTION)
        else:
            client.photo_upload(path=str(media), caption=INSTAGRAM_CAPTION)

        journaliser("Publication Instagram réussie.")
    except Exception as erreur:
        journaliser(f"Erreur Instagram : {erreur}")


def publier_tiktok(media: Path) -> None:
    dossier_uploader = Path(TIKTOK_UPLOADER_PATH)
    script_cli = dossier_uploader / "cli.py"

    if not script_cli.exists():
        journaliser(f"Erreur TikTok : script introuvable ({script_cli}).")
        return

    commande = [
        PYTHON_EXECUTABLE,
        str(script_cli),
        "upload",
        "-u",
        TIKTOK_USERNAME,
        "-v",
        str(media),
        "-t",
        TIKTOK_DESCRIPTION,
    ]

    try:
        resultat = subprocess.run(
            commande,
            cwd=str(dossier_uploader),
            capture_output=True,
            text=True,
            check=True,
        )
        if resultat.stdout.strip():
            journaliser(f"TikTok stdout : {resultat.stdout.strip()}")
        if resultat.stderr.strip():
            journaliser(f"TikTok stderr : {resultat.stderr.strip()}")
        journaliser("Publication TikTok terminée.")
    except Exception as erreur:
        journaliser(f"Erreur TikTok : {erreur}")


def main() -> None:
    if not est_dans_un_creneau_valide():
        journaliser("Hors créneau autorisé (5h, 8h, 11h, 14h, 17h, 20h).")
        return

    media = choisir_media_aleatoire()
    if media is None:
        return

    journaliser(f"Média sélectionné : {media}")
    publier_instagram(media)
    publier_tiktok(media)


if __name__ == "__main__":
    main()
