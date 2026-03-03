# Résumé du Projet : Hylst Books & Reader

## 📖 Contexte du Projet
**Hylst Books & Reader** est une application web progressive (PWA) de lecture de livres numériques (EPUB/HML). L'application mise sur une esthétique premium, une expérience utilisateur fluide et des fonctionnalités avancées pour les lecteurs. Le projet intègre une bibliothèque musicale pour accompagner la lecture.

## 👤 Votre Rôle (USER) : Geoffroy Streit
Vous êtes le **créateur et producteur musical** ainsi que le **donneur d'ordre technique**. Vous fournissez :
- Les assets musicaux et les œuvres littéraires.
- La vision artistique et fonctionnelle.
- Le pilotage du projet par des instructions précises et des retours itératifs.

## 🎼 Contexte de la Tâche Actuelle : Design du Lecteur et Optimisation
L'objectif principal actuel est d'affiner l'expérience de lecture et la performance :
- **Optimisation** : Conversion de toutes les images PNG en WEBP (couvertures, illustrations de chapitres) pour de meilleures performances et mise à jour de l'ensemble des références.
- **Design du Lecteur** : Résolution des problèmes d'affichage sur la préface de l'Odyssée de l'IA, harmonisation de l'interface de lecture, et correction des disparités (tailles, polices, couleurs) du texte en cours de lecture.
- **Musique** : 8 prompts "text to music" pour générer des musiques instrumentales propices à la lecture des livres ont été fournis. Le lecteur audio en ligne est en cours de développement.

## ✅ Tâches Récemment Accomplies
- [x] **Optimisation Images** : Conversion PNG vers WEBP effectuée, `app.jsx`, `books.json` et les fichiers HTML mis à jour.
- [x] **Music Player (UI)** : Restauration du bouton Paramètres, génération des prompts de musiques instrumentales.
- [x] **Bibliothèque** : Séparation natif/importé, correction de bugs d'IndexedDB.

## 🛠️ Stack Technique
- **Frontend** : React 18 (via CDN), Vanilla CSS, Lucide Icons.
- **Stockage** : IndexedDB (`idb-keyval`) pour l'offline total.
- **Automation** : Python pour le build des livres et la conversion d'images.
- **Versioning** : Git (Github: [hylst_reader](https://github.com/Hylst/hylst_reader)).

---
*Ce document sert de référence pour maintenir la continuité du développement 
