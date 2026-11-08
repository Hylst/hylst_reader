# Guide de Test, de Build et de Déploiement · La Bibliothèque de Hylst

Ce guide explique pas-à-pas comment tester l'application **La Bibliothèque de Hylst** sur votre ordinateur sous Windows, comment générer la version statique et comment la déployer de façon premium sur votre VPS Hostinger géré par **Coolify** au sein d'un container Nginx, spécifiquement dans un sous-dossier `/books_reader/` pour l'URL : `https://hylst.fr/books_reader/`.

---

## 💻 1. Tester en local sous Windows

L'application est statique, mais le JSX doit être précompilé et les polices viennent de la plateforme. Le test fiable se fait donc sur le miroir de production, pas sur la racine du dépôt source.

### Méthode A : miroir local (recommandée)
1. Compiler et synchroniser depuis le dépôt source :
   ```powershell
   cd D:\0CODE\AntiGravity\Hylst_Reader
   node scripts/build_jsx.js
   node scripts/build_jsx.js --check
   powershell -ExecutionPolicy Bypass -File .\scripts\sync-to-platform.ps1
   ```
2. Servir la racine de la plateforme :
   ```powershell
   cd D:\0CODE\AntiGravity\Cours_Memos\Docker
   python -m http.server 8765 --bind 127.0.0.1
   ```
3. Ouvrir [http://127.0.0.1:8765/books_reader/](http://127.0.0.1:8765/books_reader/).

Le miroir fournit `/assets/fonts/fonts.css`, `js/dist` et l'index de production. Tester avec et sans slash, puis en navigation privée pour le Service Worker.

### Méthode B : avec Node.js
Après le sync, lancer `npx serve` depuis `Cours_Memos/Docker` et ouvrir `/books_reader/`.

> [!CAUTION]
> Ne pas servir la racine du dépôt source pour valider une version : `index.html` référence `js/dist` et `/assets/fonts`, qui ne sont pas à la racine source.

### Vérifier le mode hors ligne
1. Utiliser un profil Chromium neuf, sans Service Worker existant.
2. Charger `http://127.0.0.1:8765/books_reader/` et attendre l'activation du Service Worker (`navigator.serviceWorker.ready`).
3. Dans DevTools, onglet Application, vérifier le cache `hylst-reader-<build>` : 322 entrées au build `41e979fdec9e`, dont les 28 illustrations de chapitre, les 5 couvertures à venir et les 77 fontes de la plateforme.
4. Passer en mode hors ligne (Network, Offline), puis ouvrir la bibliothèque, `droits.html`, chaque fiche avec et sans slash, puis un livre dans la liseuse.
5. Vérifier que le texte et les illustrations s'affichent, sans requête en erreur. Les PDF de *Sciences et technologie* ne sont pas précachés : ce comportement est attendu.

---

## 🏗️ 2. Build JSX et compilation des livres

Deux étapes de build sont nécessaires avant un déploiement :

1. **Précompiler le JSX** : `node scripts/build_jsx.js` régénère `js/dist/`. Le mode `--check` échoue si la sortie est périmée. `scripts/sync-to-platform.ps1` exécute les deux automatiquement.
2. **Compiler les livres** si vous modifiez ou ajoutez des écrits bruts :
   - Placez vos textes originaux dans `livres_pour_import/2 futurs un choix/`.
   - Exécutez `python build_books.py`.
   - Le script analyse les chapitres, applique la structure HTML sémantique (dropcaps, styles de titres), copie les couvertures et actualise `public/books.json`.

---

## 🚀 3. Déploiement VPS Hostinger via Coolify (Container Nginx statique)

### 3.0 Déploiement réel sur la plateforme Hylst

Le déploiement actuel ne se fait pas via un service Coolify dédié au lecteur, mais dans le **dépôt de la plateforme Hylst** :

| Élément | Valeur |
|---|---|
| Dossier de production | `D:\0CODE\AntiGravity\Cours_Memos\Docker\books_reader` |
| Dépôt plateforme | `Hylst/cours_info` (privé, branche `main`) |
| Racine du dépôt | `D:\0CODE\AntiGravity\Cours_Memos\Docker` |
| Conteneur | Nginx statique, app Coolify `hylst-cours` |
| URL | `https://hylst.fr/books_reader/` |
| Build | Précompilation JSX (`scripts/build_jsx.js`) puis copie statique, pas de Dockerfile dédié |

Procédure recommandée :

```powershell
# 1. Précompiler le JSX et vérifier la sortie
node scripts/build_jsx.js
node scripts/build_jsx.js --check

# 2. Synchroniser vers le miroir de production (relance le build JSX et les fiches)
powershell -ExecutionPolicy Bypass -File .\scripts\sync-to-platform.ps1

# 3. Vérifier, puis committer (option -Commit), et pousser manuellement
git -C D:\0CODE\AntiGravity\Cours_Memos\Docker status --short -- books_reader
git -C D:\0CODE\AntiGravity\Cours_Memos\Docker push origin main
```

Points critiques :
- **Ne pas écraser `books_reader/index.html`** avec l'index source : celui de production contient le patch plateforme (`vendor/`, `/assets/fonts/fonts.css`, `canonical`). Le script le préserve et vérifie ses marqueurs.
- **Ne pas copier `.env`** ni `livres_pour_import/` dans le miroir. Le script supprime le `.env` local du miroir et ne copie que les fichiers runtime.
- **Musique** : `Docker/hml/` (~2,9 Go) est exclu de l'image Docker et servi par le bind mount Coolify `/var/www/mp3` → `/app/mp3` via `location ^~ /hml/`. Une mise à jour musicale doit aussi être copiée dans `/var/www/mp3/hml` sur le VPS.
- **Après push** : attendre `Finished` dans Coolify, puis lancer `bash scripts/verifier-prod.sh --full books_reader` et tester en navigation privée.

Les sections 3.1 à 3.4 ci-dessous décrivent la configuration Coolify générique ; la section 3.5 documente le 301 réellement appliqué à Books Reader.

Pour héberger l'application sur votre VPS Hostinger configuré avec Coolify sous l'URL `https://hylst.fr/books_reader/`, suivez ces étapes détaillées.

### Étape 3.1 : Création du Service sur Coolify
1. Connectez-vous à votre console **Coolify**.
2. Allez dans votre **Projet** > **Environnement** > **Ajouter une ressource**.
3. Choisissez **Static Sites** ou **Application** puis sélectionnez votre dépôt GitHub (ex: `Hylst_Reader`).
4. Dans la liste des configurations prédéfinies, sélectionnez la stack **Nginx (Static)** ou **HTML/CSS/JS (Static)**.

### Étape 3.2 : Configuration des Variables et Emplacements
Coolify va cloner votre projet et le servir au travers d'un container Docker équipé d'un serveur Nginx.

* **Base Directory** : `./` (la racine de votre projet).
* **Destination Directory** (répertoire servi) : `./` (puisqu'il n'y a pas de dossier `dist/` ou `build/` intermédiaire, tous vos fichiers `index.html`, `sw.js`, `css/` et `js/` sont à la racine).
* **URL de destination (FQDN)** : Indiquez votre domaine suivi du sous-dossier exact :
  ```
  https://hylst.fr/books_reader/
  ```

### Étape 3.3 : Pourquoi les chemins ne se cassent pas en sous-dossier ?
L'application a été conçue pour utiliser des **chemins relatifs et non absolus** :
- **Correct (Relatif)** : `css/variables.css`, `js/dist/app.js` (ou `./public/covers/...`).
- **Absolu volontaire** : `/assets/fonts/fonts.css` et `/hml/...` sont servis à la racine de la plateforme, pas dans `/books_reader/`.

Grâce à cette précaution, le container Nginx statique créé par Coolify servira tous vos fichiers à la perfection au sein de `/books_reader/`.

### Étape 3.4 : [Optionnel] Configuration Nginx avancée
Si vous devez gérer le routage Nginx ou le fallback d'URL (utile pour éviter les erreurs 404 lors du rafraîchissement d'une page profonde), Coolify vous permet de personnaliser le fichier de configuration Nginx du container. Vous pouvez y ajouter cette règle simple :

```nginx
server {
    listen 80;
    server_name localhost;

    location /books_reader/ {
        alias /usr/share/nginx/html/;
        index index.html index.htm;
        try_files $uri $uri/ /books_reader/index.html;
    }
}
```
*(Exemple générique. La configuration réellement utilisée par hylst.fr est `Cours_Memos/Docker/nginx-coolify-reference.conf`, appliquée dans le panel Coolify ; ne pas utiliser ce bloc seul pour remplacer la configuration existante).*

### Étape 3.5 : Redirection des fiches livres sans slash

La configuration de référence `Cours_Memos/Docker/nginx-coolify-reference.conf` contient le bloc appliqué en production le 04/11/2026 pour rediriger `/books_reader/livres/<id>` vers `/books_reader/livres/<id>/` en 301, query conservée :

```nginx
location ~ ^/books_reader/livres/([^/]+)$ {
    return 301 /books_reader/livres/$1/$is_args$args;
}
```

Le bloc regex ne capte ni `/books_reader/livres/` ni les fichiers `.html`. La configuration est enregistrée dans la base Coolify et dans le conteneur `hylst-cours`, avec sauvegarde préalable dans `/root/hylst-nginx-backup-20261104-booksreader301/`.
