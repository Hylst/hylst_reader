// Test des garde-fous du Service Worker, sans navigateur ni dépendance.
// Charge sw.js dans un contexte VM et vérifie les fonctions de politique.

const assert = require('assert');
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const listeners = {};
const context = {
    self: {
        registration: { scope: 'https://example.test/books_reader/' },
        location: { origin: 'https://example.test' },
        addEventListener(type, handler) { listeners[type] = handler; },
        skipWaiting() { },
        clients: { claim() { } }
    },
    caches: {
        open: async () => { throw new Error('caches.open ne doit pas être appelé ici'); },
        keys: async () => [],
        match: async () => undefined,
        delete: async () => false
    },
    fetch: async () => { throw new Error('fetch ne doit pas être appelé ici'); },
    console: { log() { }, warn() { }, error() { } },
    URL,
    Request,
    Response,
    Headers,
    setTimeout,
    clearTimeout
};

vm.createContext(context);
const swPath = path.join(__dirname, '..', 'sw.js');
vm.runInContext(fs.readFileSync(swPath, 'utf8'), context);

function test(name, fn) {
    if (typeof fn !== 'function') throw new Error('test invalide : ' + name);
    return Promise.resolve().then(fn).then(
        () => console.log('OK ' + name),
        (error) => {
            console.error('KO ' + name);
            console.error(error.stack || error.message || error);
            process.exitCode = 1;
        }
    );
}

function request(url, options = {}) {
    const headers = new Headers(options.headers || {});
    return {
        url,
        method: options.method || 'GET',
        destination: options.destination || '',
        headers
    };
}

(async () => {
    await test('isCacheableResponse accepte uniquement 200 basic', () => {
        assert.strictEqual(context.isCacheableResponse({ status: 200, type: 'basic' }), true);
        assert.strictEqual(context.isCacheableResponse({ status: 206, type: 'basic' }), false);
        assert.strictEqual(context.isCacheableResponse({ status: 204, type: 'basic' }), false);
        assert.strictEqual(context.isCacheableResponse({ status: 304, type: 'basic' }), false);
        assert.strictEqual(context.isCacheableResponse({ status: 200, type: 'opaque' }), false);
        assert.strictEqual(context.isCacheableResponse({ status: 0, type: 'opaqueredirect' }), false);
        assert.strictEqual(context.isCacheableResponse(null), false);
    });

    await test('shouldBypassCache refuse audio, Range et extensions sonores', () => {
        const base = new URL('https://example.test/books_reader/');
        assert.strictEqual(context.shouldBypassCache(request('https://example.test/hml/track.mp3'), new URL('https://example.test/hml/track.mp3')), true);
        assert.strictEqual(context.shouldBypassCache(request('https://example.test/hml/track.mp3', { destination: 'audio' }), new URL('https://example.test/hml/track.mp3')), true);
        assert.strictEqual(context.shouldBypassCache(request('https://example.test/books_reader/video.webm', { destination: 'video' }), new URL('https://example.test/books_reader/video.webm')), true);
        assert.strictEqual(context.shouldBypassCache(request('https://example.test/books_reader/file.json', { headers: { Range: 'bytes=0-10' } }), new URL('https://example.test/books_reader/file.json')), true);
        assert.strictEqual(context.shouldBypassCache(request('https://example.test/books_reader/file.wav'), new URL('https://example.test/books_reader/file.wav')), true);
        assert.strictEqual(context.shouldBypassCache(request('https://example.test/books_reader/'), new URL('https://example.test/books_reader/')), false);
        assert.strictEqual(context.shouldBypassCache(request('https://example.test/hml/cover.webp', { destination: 'image' }), new URL('https://example.test/hml/cover.webp')), false);
        assert.strictEqual(context.shouldBypassCache(request('https://example.test/books_reader/data.json', { method: 'POST' }), new URL('https://example.test/books_reader/data.json')), true);
    });

    await test('trimCache conserve les entrées les plus récentes', async () => {
        const entries = ['a', 'b', 'c', 'd'];
        const cache = {
            async keys() { return entries.map((url) => ({ url })); },
            async delete(key) {
                const index = entries.indexOf(key.url);
                if (index === -1) return false;
                entries.splice(index, 1);
                return true;
            }
        };
        await context.trimCache(cache, 2);
        assert.deepStrictEqual(entries, ['c', 'd']);
    });

    await test('cacheUrl retente après un échec réseau', async () => {
        let calls = 0;
        const puts = [];
        context.fetch = async () => {
            calls++;
            if (calls === 1) throw new Error('réseau indisponible');
            return new Response('ok', { status: 200 });
        };
        const cache = { put: async (url, response) => { puts.push({ url, response }); } };
        const ok = await context.cacheUrl(cache, 'asset.txt', 2);
        assert.strictEqual(ok, true);
        assert.strictEqual(calls, 2);
        assert.strictEqual(puts.length, 1);
        assert.strictEqual(puts[0].url, 'https://example.test/books_reader/asset.txt');
    });

    await test('cacheUrl échoue après deux réponses non 200', async () => {
        let calls = 0;
        let puts = 0;
        context.fetch = async () => { calls++; return new Response('absent', { status: 404 }); };
        const cache = { put: async () => { puts++; } };
        const ok = await context.cacheUrl(cache, 'absent.txt', 2);
        assert.strictEqual(ok, false);
        assert.strictEqual(calls, 2);
        assert.strictEqual(puts, 0);
    });

    if (process.exitCode) {
        console.error('Échec des tests de politique du Service Worker.');
    } else {
        console.log('Tous les tests de politique du Service Worker passent.');
    }
})();
