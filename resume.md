# Résumé du Projet : Hylst Reader - Intégration Music Player

## 📖 Contexte du Projet
**Hylst Reader** est une application web progressive (PWA) de lecture de livres numériques (EPUB/HML). L'application mise sur une esthétique premium, une expérience utilisateur fluide et des fonctionnalités avancées pour les lecteurs. Le projet est actuellement en phase d'enrichissement fonctionnel.

## 👤 Votre Rôle (USER)
Vous êtes le **créateur et producteur musical** ainsi que le **donneur d'ordre technique**. Vous fournissez :
- Les assets musicaux (compositions propres hébergées sur `hylst.fr`).
- La vision artistique et fonctionnelle (intégration d'un lecteur audio discret et élégant).
- Le pilotage du projet par des instructions précises et des retours itératifs.

## 🎼 Contexte de la Tâche Actuelle
L'objectif principal est l'intégration d'un **Lecteur de Musique en Ligne** au sein de l'application.
- **Source des données** : Fichiers MP3 et illustrations JPG hébergés sur `https://hylst.fr/hml/`.
- **Metadata** : Basées sur les fichiers `mp3_online.csv` et `mp3_online.txt`.
- **Infrastructure** : Utilisation de Git pour le versioning (initialisé avec `.gitignore` et premier commit effectué).

## ✅ Tâches en Cours et Accomplies
### Accomplies :
- [x] **Traitement des Données** : Script Python `gen_music_data.py` créé pour générer `js/music_data.js` à partir du CSV et du TXT.
- [x] **Développement UI** : Création du composant `MusicPlayerModal` dans `js/app.jsx` avec recherche, liste de pistes et contrôles.
- [x] **Intégration** : Ajout du bouton "Musique" dans le header de `LibraryView` et gestion de l'état global du modal.
- [x] **Design** : Ajout de styles CSS détaillés dans `styles.css` pour une interface premium (animations de vagues, mode responsive).
- [x] **Versioning** : Création de `.gitignore` et `git commit` initial.

### En cours / À finaliser :
- [ ] **Vérification Critique** : Test complet du flux de lecture (Play, Pause, Loop, Recherche) via le navigateur.
- [ ] **Polissage UI** : Ajustements finaux basés sur les rendus visuels réels.
- [ ] **Correction de Bugs** : Résolution des erreurs de syntaxe ou de linting résiduelles dans `app.jsx`.

## 🛠️ Stack Technique
- **Frontend** : React (via CDN), Vanilla CSS.
- **Stockage** : IndexedDB (`idb-keyval`).
- **Automation** : Python (pour la génération de données).
- **Versioning** : Git.

---
*Ce document sert de référence pour maintenir la continuité du développement et la compréhension des objectifs.*
