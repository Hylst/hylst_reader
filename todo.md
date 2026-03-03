# Améliorations Futures (TODO / Idées)

## 1. Ergonomie Lecteur & Personnalisation (UI/UX)
- **Menu de style ("Settings") dans le `ReaderView`** : Proposer une modale (ou un drawer en bas) permettant à l'utilisateur de :
  - Modifier la taille de la police : `var(--font-size-multiplier)`.
  - Forcer l'alignement (`justify` ou `left`) : `var(--text-alignment)`.
  - Basculer le mode sombre (`dark` / `light` / `auto`) via l'attribut global HTML `data-theme`.
- **Mode Focus** : Disparition complète de la Top-Bar et du scrollbar lors du scroll (ou via un switch UI).
- **Contrôles Tactiles (Gestures)** : Swipe Gauche/Droit pour naviguer entre les chapitres sur terminaux mobiles.

## 2. Fonctionnalités de la Liseuse Pure
- **Signets et Surlignages** : Permettre à l'utilisateur de sélectionner du texte, de le surligner et d'ajouter une note, puis de stocker ces signets dans `IndexedDB`.
- **Recherche plein texte** : Indexation asynchrone pour la recherche de mots à l'intérieur d'un ouvrage (local ou pré-intégré).
- **Temps estimé de lecture** : Calcul basé sur le nombre de mots du chapitre pour afficher un `X minutes restants`.

## 3. Format et Architecture (Data)
- **Markdown / Extensions** : Apporter une librairie (ex: `marked.js` en CDN) pour parser du Markdown au lieu du simple `.txt` dans l'import `app.js` et le `build_books.py`.
- **Export de la bibliothèque** : Fonctionnalité pour exporter la base IndexedDB dans un fichier de sauvegarde (`.json` compressé), permettant la continuité depuis plusieurs appareils.

## 4. Outils de Déploiement
- **Script interactif Node.js / Python** (côté développeur) pour pouvoir éditer la couleur des livres (`config.json`) via une pseudo-interface CLI Terminal locale plutot que d'éditer manuellement les fichiers `.json`.
