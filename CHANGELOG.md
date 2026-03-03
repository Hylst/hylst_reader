# Changelog
Toutes les modifications notables apportées au projet **Hylst Reader** seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/).

## [Unreleased]
### Ajouté
- Début du développement.
- Interface pure CSS haut-de-gamme et design system dynamique gérant un CSS-in-JSON (`config.json` par dossier).
- Fichier `index.html`, point d'entrée avec service worker enregistré.
- Librairies chargées numériquement sans Build Process : React 18, Babel Standalone.
- Système de module ES avec IndexedDB (`idb-keyval`).
- Vue `ReaderView` intégrant la sauvegarde de progression `handleScroll`.
- Gestion des couvertures hybrides (locales sur disque et via IndexedDB BLOB).
- Composant JSX global `app.jsx`.
- Script pré-intégration `build_books.py` convertissant les `.txt` sources de Hylst en public `.html`.
- Génération automatique stylisée d'une "Préface" si le dossier ne possède pas d'`intro.txt`.

### Modifié
- Amélioration de la typographie du Mode Lecteur avec renfort graphique (ombres, justifié, suppression d'indentation post-titre).
- Basculement de l'architecture Vite demandée en `Pure Frontend` (HTML classique et scripts) selon le nouveau souhait du client (Hylst).
