// sw.js - Service Worker Hylst Reader v1.2.2
// Stratégie: Network-First avec fallback cache pour le local, et Cache-First pour les CDNs.

const CACHE_NAME = 'hylst-reader-v42';

self.addEventListener('install', (event) => {
    self.skipWaiting();
});

self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys().then((keys) => Promise.all(
            keys.map((key) => {
                if (key !== CACHE_NAME) {
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

    // NETWORK-FIRST pour tous les assets locaux
    // On nettoie l'URL des paramètres de requête (comme ?t=...) pour éviter de gonfler le cache
    // et pour permettre une correspondance parfaite hors-ligne.
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
            .catch(() => {
                return caches.match(cleanUrl).then((cached) => {
                    if (cached) return cached;
                    if (event.request.mode === 'navigate') {
                        return caches.match('./index.html');
                    }
                    // Retourner une réponse d'erreur propre plutôt que undefined (qui cause ERR_FAILED)
                    return new Response(JSON.stringify({ error: 'offline' }), {
                        status: 503,
                        statusText: 'Service Unavailable (offline)',
                        headers: { 'Content-Type': 'application/json' }
                    });
                });
            })
    );
});
