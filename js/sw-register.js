// Enregistrement du Service Worker (PWA).
if ('serviceWorker' in navigator) {
    window.addEventListener('load', function () {
        navigator.serviceWorker.register('sw.js').then(function (reg) {
            console.log('ServiceWorker registration successful', reg.scope);
            requestPersistentStorage();
        }).catch(function (err) {
            console.log('ServiceWorker registration failed: ', err);
        });
    });
}

// Demande la persistance du stockage : sans elle, le navigateur peut évincer
// le précache hors ligne quand l'espace disque manque.
function requestPersistentStorage() {
    if (!navigator.storage || !navigator.storage.persist) return;
    var alreadyPersisted = navigator.storage.persisted
        ? navigator.storage.persisted()
        : Promise.resolve(false);
    alreadyPersisted.then(function (persisted) {
        if (persisted) return;
        return navigator.storage.persist().then(function (granted) {
            console.log('Persistent storage:', granted ? 'granted' : 'not granted');
        });
    }).catch(function (err) {
        console.log('Persistent storage request failed: ', err);
    });
}
