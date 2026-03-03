# Hylst Reader

**Hylst Reader** est une application web de lecture de livres numériques (PWA) conçue avec une architecture *Offline-First* et *Pure Frontend* (sans build Node.js). L'accent a été mis sur le confort de lecture, l'esthétique premium et la capacité à stocker sa bibliothèque localement dans son navigateur via IndexedDB.

Ce projet inclut par défaut les premiers chapitres de l'ouvrage *L'odyssée de l'IA - 2 futurs, un choix* (de Hylst).

## Architecture
- **HTML/CSS/JS** purs. Un seul point d'entrée : `index.html`.
- **Framework** : React chargé via CDN (avec Babel Standalone pour le rendu JSX à la volée).
- **Stockage** : Librairie `idb-keyval` (IndexedDB) pour sauvegarder les livres, la progression de lecture et le thème.
- **Service Worker** : `sw.js` fait à la main pour le cache de l'application et la PWA.
- **Génération statique** : Un script Python (`build_books.py`) permet de parser simplement des dossiers contenant des fichiers textes pour les intégrer à l'application.

## Fonctionnalités
- PWA installable sur desktop, mobile ou tablette.
- Thèmes modulables par livre : Chaque livre intégre dans son `config.json` ses propres polices, couleurs de textes et styles d'arrière-plan.
- Design ultra-premium : Interface sombre globale optionelle et expérience de lecture typographique soignée (Inter, Playfair Display, Georgia).
- Génération automatique de préfaces si l'introduction (`intro.txt`) est manquante tout en générant le HTML depuis vos simples `.txt`.

## Comment tester et héberger l'application

Puisqu'il n'y a pas de dépendance `Node.js` d'exécution, le déploiement est trivial.

### En local (sur votre machine)
1. Ouvrez un terminal dans le dossier principal.
2. Démarrez un serveur HTTP basique avec Python (ou Live Server) :
   ```bash
   python -m http.server 8000
   ```
3. Ouvrez votre navigateur sur `http://localhost:8000`.

### Sur Coolify / Nginx 
1. Créez un nouveau projet/service sur Coolify pointant sur ce dépôt (ou le dossier du projet déployé).
2. Choisissez le type "Serveur web statique (Nginx)".
3. Dirigez le document root sur la racine (`/`). Nginx servira automatiquement `index.html` !
4. Pensez à relancer `python build_books.py` au préalable si vous importez de nouveaux dossiers statiques de M. Streit ou de vous-même dans le dossier `livres_pour_import/`. L'application les chargera nativement via le fetch du `books.json`.

---
*Ce lecteur a été conçu par Antigravity pour Hylst.*
