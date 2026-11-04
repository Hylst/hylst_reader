// Enregistrement du Service Worker (PWA).
if ('serviceWorker' in navigator) {
    window.addEventListener('load', function () {
        navigator.serviceWorker.register('sw.js').then(function (reg) {
            console.log('ServiceWorker registration successful', reg.scope);
        }).catch(function (err) {
            console.log('ServiceWorker registration failed: ', err);
        });
    });
}
