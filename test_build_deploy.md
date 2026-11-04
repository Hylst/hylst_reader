# Guide de Test, de Build et de Déploiement · La Bibliothèque de Hylst

Ce guide explique pas-à-pas comment tester l'application **La Bibliothèque de Hylst** sur votre ordinateur sous Windows, comment générer la version statique et comment la déployer de façon premium sur votre VPS Hostinger géré par **Coolify** au sein d'un container Nginx, spécifiquement dans un sous-dossier `/books_reader/` pour l'URL : `https://hylst.fr/books_reader/`.

---

## 💻 1. Tester en local sous Windows

L'application étant « Pure Frontend » (sans compilation Node.js requise pour s'exécuter), un simple serveur HTTP statique suffit pour faire tourner le site en local.

> [!CAUTION]
> **Pourquoi ne pas ouvrir directement `index.html` en double-cliquant dessus ?**
> Les navigateurs bloquent les requêtes locales (protocole `file:///`) par mesure de sécurité CORS. Les modules JavaScript, le Service Worker et la récupération de fichiers (comme `books.json` ou les chapitres HTML) ne fonctionneront pas sans un serveur web local (protocole `http://localhost`).

### Méthode A : Avec Python (Intégré et rapide)
Si vous possédez Python installé sur Windows :
1. Ouvrez votre terminal (PowerShell ou CMD) dans le dossier du projet : `d:\0CODE\AntiGravity\Hylst_Reader`.
2. Lancez la commande suivante :
   ```powershell
   python -m http.server 8000
   ```
3. Ouvrez votre navigateur et accédez à : [http://localhost:8000](http://localhost:8000).

### Méthode B : Avec Node.js (`npx`)
Si vous préférez utiliser l'écosystème Node :
1. Dans votre dossier de projet, lancez :
   ```powershell
   npx serve
   ```
2. Accédez à l'URL affichée dans le terminal (généralement `http://localhost:3000` ou `5000`).

---

## 🏗️ 2. Build JSX et compilation des livres

L'application n'a pas de bundler généraliste, mais deux étapes de build sont nécessaires avant un déploiement :

1. **Précompiler le JSX** : `node scripts/build_jsx.js` régénère `js/dist/`. Le mode `--check` échoue si la sortie est périmée. `scripts/sync-to-platform.ps1` exécute les deux automatiquement.
2. **Compiler les livres** si vous modifiez ou ajoutez des écrits bruts dans le dossier de source :
1. Assurez-vous d'avoir placé vos textes originaux dans le dossier `livres_pour_import/2 futurs un choix/`.
2. Exécutez le script de build Python à la racine du projet :
   ```powershell
   python build_books.py
   ```
3. Ce script va analyser les chapitres, appliquer la structure sémantique premium (dropcaps, styles de titres), copier les images de couverture et actualiser le catalogue officiel dans `public/books.json`.

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

Les sections 3.1 à 3.4 ci-dessous décrivent la configuration Coolify générique ; elles restent utiles pour comprendre le fonctionnement du conteneur Nginx.

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
*(Dans la plupart des cas de sites Pure Statiques simples, la configuration par défaut de Coolify sans Nginx complexe fonctionne directement).*

### Étape 3.5 : Redirection des fiches livres sans slash

La configuration de référence `Cours_Memos/Docker/nginx-coolify-reference.conf` contient le bloc à appliquer dans le panel Coolify pour rediriger `/books_reader/livres/<id>` vers `/books_reader/livres/<id>/` en 301, query conservée :

```nginx
location ~ ^/books_reader/livres/([^/]+)$ {
    return 301 /books_reader/livres/$1/$is_args$args;
}
```

Le bloc regex ne capte ni `/books_reader/livres/` ni les fichiers `.html`. La référence locale ne déploie rien : la modification doit être collée dans la configuration Nginx du service `hylst-cours` dans Coolify.
