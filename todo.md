# Hylst Books & Reader - TODO

## 🎯 Priorités Actuelles
- [ ] **Refactorisation CSS** : Diviser `css/base.css` et autres styles en modules encore plus fins ou harmoniser le chargement.
- [ ] **Export de Bibliothèque** : Permettre de télécharger un backup `.json` de ses livres importés pour partage et sauvegarde.
- [ ] **Preset Lecture Longue** : Ajouter une option pour réduire automatiquement toutes les animations après 20 minutes de lecture.

## ✅ Terminé (Récemment)
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
