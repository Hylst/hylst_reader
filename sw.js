// sw.js - Service Worker La Bibliothèque de Hylst v1.8.29
// Stratégie : précache versionné de l'app shell, des livres, des illustrations
// et des fontes, puis Network-First avec repli cache pour le local. Le cache
// d'exécution est séparé et plafonné.

const CACHE_NAME = 'hylst-reader-v85';
// Le stockage de caches est partagé par toute l'origine hylst.fr : ne jamais
// supprimer les caches des autres applications hébergées sur le même domaine.
const CACHE_PREFIX = 'hylst-reader-';
// Les réponses consultées à la demande vivent dans un cache distinct du
// précache. Le nom dérive de CACHE_NAME pour suivre le build injecté.
const RUNTIME_CACHE_NAME = CACHE_NAME + '-runtime';
const RUNTIME_CACHE_LIMIT = 200;
const PRECACHE_ATTEMPTS = 2;
const BOOKS_INDEX = 'public/books.json';
const FONT_STYLESHEET = '/assets/fonts/fonts.css';
const AUDIO_EXTENSIONS = /\.(mp3|wav|ogg|oga|flac|m4a|aac)$/i;

// App shell minimal : de quoi démarrer la liseuse et afficher la bibliothèque
// hors ligne. Les contenus de livres sont ajoutés dynamiquement à partir de
// public/books.json lors de l'installation.
const APP_SHELL = [
    './',
    './index.html',
    './manifest.json',
    './droits.html',
    './css/book-fonts.css',
    './css/book-page.css',
    './css/droits.css',
    './css/variables.css',
    './css/base.css',
    './css/layout.css',
    './css/components.css',
    './css/modals.css',
    './css/music.css',
    './css/reader.css',
    './css/responsive.css',
    './vendor/react.production.min.js',
    './vendor/react-dom.production.min.js',
    './vendor/idb-keyval.js',
    './vendor/jszip.min.js',
    './vendor/epub.min.js',
    './vendor/purify.min.js',
    './js/music_data.js',
    './js/sanitize.js',
    './js/db.js',
    './js/importAPI.js',
    './js/modalA11y.js',
    './js/theme-boot.js',
    './js/sw-register.js',
    './js/dist/components/Icon.js',
    './js/dist/components/Ambience.js',
    './js/dist/components/AboutModal.js',
    './js/dist/components/GlobalSettingsModal.js',
    './js/dist/components/MusicPlayerModal.js',
    './js/dist/components/ImageLightbox.js',
    './js/dist/components/BookHomeView.js',
    './js/dist/components/LibraryView.js',
    './js/dist/components/ReaderView.js',
    './js/dist/app.js',
    './public/books.json',
    './public/icons/icon-32.png',
    './public/icons/icon-192.png',
    './public/icons/icon-512.png',
    './public/icons/icon-512-maskable.png',
    './public/icons/apple-touch-icon.png',
    // Couvertures des livres à venir affichées dans la bibliothèque.
    './public/covers/cover_etheria.webp',
    './public/covers/cover_existentiel.webp',
    './public/covers/cover_autre_en_moi.webp',
    './public/covers/cover_astrakan.webp',
    './public/covers/cover_murder.webp',
    './public/covers/cover_maths.webp',
    './public/covers/cover_physique.webp',
    './public/covers/cover_optique.webp',
    './public/covers/cover_electronique.webp',
    './public/covers/cover_informatique.webp',
    './public/covers/cover_algorithm_love.webp',
    './public/covers/cover_godefroi.webp',
    './public/covers/cover_atrophie.webp',
    './public/covers/cover_nouvelles_alsaciennes.webp',
    './public/covers/cover_automatisation_ia.webp',
    './public/covers/cover_eclats_corbeau.webp'
];

function scopeUrl(path) {
    return new URL(path, self.registration.scope).href;
}

function isCacheableResponse(response) {
    return !!response && response.status === 200 && response.type === 'basic';
}

function shouldBypassCache(request, url) {
    if (request.method !== 'GET') return true;
    if (request.destination === 'audio' || request.destination === 'video') return true;
    if (request.headers && request.headers.has('range')) return true;
    return AUDIO_EXTENSIONS.test(url.pathname);
}

async function trimCache(cache, limit) {
    const keys = await cache.keys();
    if (keys.length <= limit) return;
    for (const key of keys.slice(0, keys.length - limit)) {
        await cache.delete(key);
    }
}

async function fetchFresh(url, attempts = PRECACHE_ATTEMPTS) {
    let lastError = null;
    for (let attempt = 1; attempt <= attempts; attempt++) {
        try {
            const response = await fetch(new Request(url, { cache: 'reload' }));
            if (response.status !== 200) {
                throw new Error(`HTTP ${response.status}`);
            }
            return response;
        } catch (error) {
            lastError = error;
            if (attempt < attempts) {
                await new Promise((resolve) => setTimeout(resolve, 150 * attempt));
            }
        }
    }
    throw lastError || new Error('réseau indisponible');
}

async function cacheUrl(cache, path, attempts = PRECACHE_ATTEMPTS) {
    const url = scopeUrl(path);
    try {
        const response = await fetchFresh(url, attempts);
        await cache.put(url, response);
        return true;
    } catch (error) {
        console.warn('[SW] Précache ignoré :', url, error.message);
        return false;
    }
}

// Les réponses consultées à la demande vont dans le cache d'exécution, jamais
// dans le précache versionné. On évite aussi de dupliquer un fichier déjà
// précaché, même si sa réponse réseau est plus récente.
async function storeRuntimeResponse(url, response) {
    const precache = await caches.open(CACHE_NAME);
    if (await precache.match(url)) return;
    const runtime = await caches.open(RUNTIME_CACHE_NAME);
    await runtime.put(url, response);
    await trimCache(runtime, RUNTIME_CACHE_LIMIT);
}

async function cacheInBatches(cache, paths, size = 6) {
    let cached = 0;
    for (let index = 0; index < paths.length; index += size) {
        const batch = paths.slice(index, index + size);
        const results = await Promise.all(batch.map((path) => cacheUrl(cache, path)));
        cached += results.filter(Boolean).length;
    }
    return cached;
}

async function precacheBooks(cache) {
    const indexUrl = scopeUrl(BOOKS_INDEX);
    const response = await fetchFresh(indexUrl);
    const books = await response.clone().json();
    if (!Array.isArray(books) || books.length === 0) {
        throw new Error('books.json vide ou invalide');
    }
    await cache.put(indexUrl, response);

    const paths = new Set();
    for (const book of books) {
        if (!book || !book.id) continue;
        paths.add(`livres/${book.id}/`);
        if (book.coverPath) {
            paths.add(`public/${book.coverPath}`);
        }
        if (book.introPath) {
            paths.add(`public/${book.introPath}`);
        }
        for (const chapter of book.chapters || []) {
            if (chapter && chapter.path) {
                paths.add(`public/${chapter.path}`);
            }
        }
    }

    const cached = await cacheInBatches(cache, [...paths]);
    if (cached !== paths.size) {
        throw new Error(`Précache des livres incomplet : ${cached}/${paths.size}`);
    }
    console.log(`[SW] Précache : ${cached}/${paths.size} contenus de livres.`);
    return books;
}

// Les illustrations vivent dans les HTML de chapitre : on les extrait des
// réponses déjà précachées pour que le premier passage hors ligne soit complet.
async function precacheChapterImages(cache, books) {
    const paths = new Set();
    for (const book of books) {
        if (!book || !book.id) continue;
        const htmlPaths = [];
        if (book.introPath) htmlPaths.push(`public/${book.introPath}`);
        for (const chapter of book.chapters || []) {
            if (chapter && chapter.path) htmlPaths.push(`public/${chapter.path}`);
        }
        for (const htmlPath of htmlPaths) {
            const response = await cache.match(scopeUrl(htmlPath));
            if (!response) continue;
            const html = await response.text();
            for (const match of html.matchAll(/<img\b[^>]*\bsrc=["']([^"']+)["']/gi)) {
                const src = match[1].trim();
                if (!src || src.startsWith('data:')) continue;
                let target;
                if (src.startsWith('http')) {
                    if (new URL(src).origin !== self.location.origin) continue;
                    target = src;
                } else if (src.startsWith('/')) {
                    target = new URL(src, self.location.origin).href;
                } else if (src.startsWith('public/')) {
                    target = scopeUrl(src);
                } else {
                    // Le rendu de la liseuse préfixe les images relatives avec
                    // le dossier du livre.
                    target = scopeUrl(`public/books/${book.id}/${src}`);
                }
                paths.add(target);
            }
        }
    }
    const cached = await cacheInBatches(cache, [...paths], 3);
    console.log(`[SW] Précache : ${cached}/${paths.size} illustrations de chapitre.`);
}

// Les fontes de la plateforme sont hors du dossier de l'application mais
// partagent la même origine. On lit la feuille de style pour suivre les
// empreintes des fichiers générés.
async function precachePlatformFonts(cache) {
    try {
        const cssUrl = new URL(FONT_STYLESHEET, self.location.origin).href;
        const response = await fetchFresh(cssUrl);
        await cache.put(cssUrl, response.clone());
        const css = await response.text();
        const paths = new Set();
        for (const match of css.matchAll(/url\('([^']+\.woff2)'\)/g)) {
            const value = match[1].trim();
            paths.add(value.startsWith('/') ? new URL(value, self.location.origin).href : new URL(value, cssUrl).href);
        }
        const cached = await cacheInBatches(cache, [...paths]);
        console.log(`[SW] Précache : ${cached}/${paths.size} fontes de la plateforme.`);
    } catch (error) {
        console.warn('[SW] Précache des fontes ignoré :', error.message);
    }
}

self.addEventListener('install', (event) => {
    self.skipWaiting();
    event.waitUntil((async () => {
        const cache = await caches.open(CACHE_NAME);
        const shellCached = await cacheInBatches(cache, APP_SHELL);
        if (shellCached !== APP_SHELL.length) {
            throw new Error(`App shell incomplet : ${shellCached}/${APP_SHELL.length}`);
        }
        console.log(`[SW] Précache : ${shellCached}/${APP_SHELL.length} fichiers de l'app shell.`);
        const books = await precacheBooks(cache);
        try {
            await precacheChapterImages(cache, books);
        } catch (error) {
            console.warn('[SW] Précache des illustrations incomplet :', error.message);
        }
        await precachePlatformFonts(cache);
    })());
});

self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys().then((keys) => Promise.all(
            keys.map((key) => {
                const keep = key === CACHE_NAME || key === RUNTIME_CACHE_NAME;
                if (!keep && key.startsWith(CACHE_PREFIX)) {
                    console.log('[SW] Suppression de l\'ancien cache:', key);
                    return caches.delete(key);
                }
            })
        ))
    );
    self.clients.claim();
});

self.addEventListener('fetch', (event) => {
    if (!event.request.url.startsWith('http')) return;

    const url = new URL(event.request.url);
    // Aucun CDN au runtime : le Service Worker ne s'occupe que de l'origine.
    if (url.origin !== self.location.origin) return;
    // L'audio et la vidéo utilisent des réponses partielles que le Cache API
    // ne peut pas stocker. On laisse le navigateur gérer le streaming.
    if (shouldBypassCache(event.request, url)) return;

    // NETWORK-FIRST pour tous les assets locaux.
    // On nettoie l'URL des paramètres de requête (comme ?t=...) pour éviter de
    // gonfler le cache et pour permettre une correspondance hors-ligne exacte.
    const cleanUrl = url.href.split('?')[0];
    const isNavigation = event.request.mode === 'navigate';

    event.respondWith(
        fetch(event.request)
            .then((networkResponse) => {
                if (!isNavigation && isCacheableResponse(networkResponse)) {
                    const responseToCache = networkResponse.clone();
                    event.waitUntil(
                        storeRuntimeResponse(cleanUrl, responseToCache).catch((error) => {
                            console.warn('[SW] Cache d\'exécution ignoré :', cleanUrl, error.message);
                        })
                    );
                }
                return networkResponse;
            })
            .catch(async () => {
                const cached = await caches.match(cleanUrl);
                if (cached) return cached;

                // Repli de navigation : l'app shell répond aux routes de la
                // liseuse, et les fiches statiques précachées restent accessibles.
                if (event.request.mode === 'navigate') {
                    // Hors ligne, la redirection Nginx /livres/<id> vers /livres/<id>/
                    // n'existe pas : on tente la fiche avec slash dans le cache.
                    const parsed = new URL(cleanUrl);
                    if (/\/livres\/[^/]+$/.test(parsed.pathname)) {
                        const withSlash = await caches.match(parsed.origin + parsed.pathname + '/');
                        if (withSlash) return withSlash;
                    }
                    const shell = await caches.match(scopeUrl('index.html'));
                    if (shell) return shell;
                }

                // Réponse d'erreur propre plutôt que undefined (qui cause ERR_FAILED).
                return new Response(JSON.stringify({ error: 'offline' }), {
                    status: 503,
                    statusText: 'Service Unavailable (offline)',
                    headers: { 'Content-Type': 'application/json' }
                });
            })
    );
});
