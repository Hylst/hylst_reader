// sw.js - Service Worker La Bibliothèque de Hylst v1.8.13
// Stratégie: précache de l'app shell et des livres, puis Network-First avec
// repli cache pour le local. Cache-First pour les CDNs.

const CACHE_NAME = 'hylst-reader-v69';
// Le stockage de caches est partagé par toute l'origine hylst.fr : ne jamais
// supprimer les caches des autres applications hébergées sur le même domaine.
const CACHE_PREFIX = 'hylst-reader-';
const BOOKS_INDEX = 'public/books.json';

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
    './public/icons/apple-touch-icon.png'
];

function scopeUrl(path) {
    return new URL(path, self.registration.scope).href;
}

async function cacheUrl(cache, path) {
    const url = scopeUrl(path);
    try {
        const response = await fetch(new Request(url, { cache: 'reload' }));
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }
        await cache.put(url, response);
        return true;
    } catch (error) {
        console.warn('[SW] Précache ignoré :', url, error.message);
        return false;
    }
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
    const response = await fetch(new Request(indexUrl, { cache: 'reload' }));
    if (!response.ok) {
        throw new Error(`books.json HTTP ${response.status}`);
    }
    const books = await response.clone().json();
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
    console.log(`[SW] Précache : ${cached}/${paths.size} contenus de livres.`);
}

self.addEventListener('install', (event) => {
    self.skipWaiting();
    event.waitUntil((async () => {
        const cache = await caches.open(CACHE_NAME);
        const shellCached = await cacheInBatches(cache, APP_SHELL);
        console.log(`[SW] Précache : ${shellCached}/${APP_SHELL.length} fichiers de l'app shell.`);
        try {
            await precacheBooks(cache);
        } catch (error) {
            console.warn('[SW] Précache des livres incomplet :', error.message);
        }
    })());
});

self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys().then((keys) => Promise.all(
            keys.map((key) => {
                if (key !== CACHE_NAME && key.startsWith(CACHE_PREFIX)) {
                    console.log('[SW] Suppression de l\'ancien cache:', key);
                    return caches.delete(key);
                }
            })
        ))
    );
    self.clients.claim();
});

self.addEventListener('fetch', (event) => {
    if (event.request.method !== 'GET') return;

    const url = event.request.url;
    if (!url.startsWith('http')) return;

    // CDNs concernés par la mise en cache offline-first
    const isCDN = url.includes('fonts.googleapis.com') ||
        url.includes('fonts.gstatic.com') ||
        url.includes('unpkg.com') ||
        url.includes('cdnjs.cloudflare.com') ||
        url.includes('cdn.jsdelivr.net');

    // Pour les CDNs, stratégie Cache-First
    if (isCDN) {
        event.respondWith(
            caches.match(event.request).then((cachedResponse) => {
                if (cachedResponse) {
                    return cachedResponse;
                }
                return fetch(event.request).then((networkResponse) => {
                    if (networkResponse && networkResponse.ok) {
                        const responseToCache = networkResponse.clone();
                        caches.open(CACHE_NAME).then((cache) => {
                            cache.put(event.request, responseToCache);
                        });
                    }
                    return networkResponse;
                }).catch((err) => {
                    console.error('[SW] Erreur de récupération CDN:', err);
                });
            })
        );
        return;
    }

    // NETWORK-FIRST pour tous les assets locaux.
    // On nettoie l'URL des paramètres de requête (comme ?t=...) pour éviter de
    // gonfler le cache et pour permettre une correspondance hors-ligne exacte.
    const cleanUrl = url.split('?')[0];

    event.respondWith(
        fetch(event.request)
            .then((networkResponse) => {
                if (networkResponse && networkResponse.ok && networkResponse.type === 'basic') {
                    const responseToCache = networkResponse.clone();
                    caches.open(CACHE_NAME).then((cache) => {
                        cache.put(cleanUrl, responseToCache);
                    });
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
