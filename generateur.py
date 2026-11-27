import os
import json

# Le dossier où se trouve ce script
dossier_principal = os.path.dirname(os.path.abspath(__file__))
playlists = {}

# On parcourt tous les dossiers et sous-dossiers
for racine, dossiers, fichiers in os.walk(dossier_principal):
    # On ignore le dossier .git si jamais il est là
    dossiers[:] = [d for d in dossiers if d != '.git']
    
    # On cherche uniquement les fichiers .mp3
    mp3_files = [f for f in fichiers if f.lower().endswith('.mp3')]
    
    if mp3_files:
        # Si on est à la racine, on appelle la playlist "Mes Sons"
        # Si on est dans un sous-dossier, la playlist prend le nom du dossier
        nom_playlist = os.path.basename(racine) if racine != dossier_principal else "Mes Sons"
        
        playlists[nom_playlist] = []
        
        for f in mp3_files:
            # On nettoie le nom pour faire un joli titre (on enlève le .mp3 et les tirets)
            titre = f.rsplit('.', 1)[0].replace('_', ' ').replace('-', ' ').title()
            
            playlists[nom_playlist].append({
                "title": titre,
                "artist": "Artiste Inconnu", # Tu pourras changer ça plus tard
                "src": f # Le nom exact du fichier
            })

# On crée le fichier playlist.json
with open(os.path.join(dossier_principal, "playlist.json"), "w", encoding="utf-8") as f:
    json.dump(playlists, f, ensure_ascii=False, indent=4)

print("✅ Super ! Le fichier playlist.json a été généré avec succès.")