# Hylst Books & Reader - TODO

## 🎯 Priorités Actuelles
- [ ] **Refactorisation CSS** : Diviser `css/base.css` et autres styles en modules encore plus fins ou harmoniser le chargement.
- [ ] **Export de Bibliothèque** : Permettre de télécharger un backup `.json` de ses livres importés pour partage et sauvegarde.
- [ ] **Preset Lecture Longue** : Ajouter une option pour réduire automatiquement toutes les animations après 20 minutes de lecture.

## ✅ Terminé (Récemment)
- [x] **Navigation lecteur (1.4.0)** : bloc « Fin de la partie » dans le flux, pastille `1 / 7 · Suivant` quand les commandes sont masquées, bloc « Fin du livre ».
- [x] **Les Ficelles du bonheur (1.3.1)** : corrections de coquilles sélectionnées, couverture illustrée Qwen-Image-2.1 local, version 1.3.1, cache SW v45.
- [x] **Les Ficelles du bonheur (1.3.0)** : intégration de la pièce Halloween en 7 chapitres, didascalies bleues, lien direct `?book=les-ficelles-du-bonheur`, couverture typographique de secours.
- [x] **Sécurité 1.2.1** : dépendances auto-hébergées, DOMPurify sur les imports, audit OSV sans CVE connue, `rel="noopener noreferrer"`, script `scripts/sync-to-platform.ps1`.
- [x] **Intégration du Chapitre 5** : Nettoyage littéraire des tics d'IA (caractères `—`, `✦` et « Dualis-IA ») et création de la couverture `chapitre-5-cover.webp` (v1.2.0).
- [x] **Modularisation de l'Application** : Découpe de `js/app.jsx` (2000 lignes) en composants React ES6 réutilisables au sein de `js/components/` (v1.2.0).
- [x] **Mise en cache PWA Robuste** : sw.js optimisé pour la mise en cache offline-first des CDN externes (unpkg, jsdelivr), garantissant le fonctionnement hors-ligne (v1.2.0).
- [x] **Documentation Complète** : Rédaction des fichiers `structure.md`, `features.md`, `readme-dev.md` et du guide débutant `test_build_deploy.md` (v1.2.0).
- [x] **Système de Musique** : Intégration complète et mini-player flottant persistant (v1.1).
- [x] **Signets & Lecture** : Calcul du temps restant de lecture et mémorisation automatique de la progression IndexedDB.

## 💡 Idées Futures
- **Audio Sync** : Synchroniser finement le défilement du chapitre avec la lecture audio ou des ambiances musicales changeant de manière contextuelle.
- **Signets enrichis** : Pouvoir ajouter des notes et commentaires personnels sur les chapitres d'un livre.
- **Recherche Plein Texte** : Ajouter un outil d'indexation locale pour chercher un mot dans tout le contenu des chapitres d'un livre.
