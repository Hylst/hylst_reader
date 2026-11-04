// js/modalA11y.js
// Accessibilite commune des modales : fermeture par Echap et piege de focus.
// A appeler dans un composant React avec une ref sur .modal-content.

(function () {
    const FOCUSABLE = [
        'a[href]',
        'button:not([disabled])',
        'input:not([disabled])',
        'select:not([disabled])',
        'textarea:not([disabled])',
        '[tabindex]:not([tabindex="-1"])'
    ].join(',');

    window.useModalA11y = function (onClose, containerRef, active) {
        const closeRef = React.useRef(onClose);

        React.useEffect(() => {
            closeRef.current = onClose;
        }, [onClose]);

        React.useEffect(() => {
            const container = containerRef.current;
            if (!container || active === false) return undefined;

            const previous = document.activeElement;
            const visibleFocusable = () => Array.from(container.querySelectorAll(FOCUSABLE))
                .filter(el => !el.hasAttribute('disabled') && el.getClientRects().length > 0);

            const initial = visibleFocusable()[0];
            if (initial) {
                initial.focus();
            } else {
                container.setAttribute('tabindex', '-1');
                container.focus();
            }

            const onKeyDown = (event) => {
                if (event.key === 'Escape') {
                    event.preventDefault();
                    event.stopPropagation();
                    closeRef.current();
                    return;
                }
                if (event.key !== 'Tab') return;

                const items = visibleFocusable();
                if (items.length === 0) {
                    event.preventDefault();
                    return;
                }

                const first = items[0];
                const last = items[items.length - 1];
                if (event.shiftKey && document.activeElement === first) {
                    event.preventDefault();
                    last.focus();
                } else if (!event.shiftKey && document.activeElement === last) {
                    event.preventDefault();
                    first.focus();
                }
            };

            document.addEventListener('keydown', onKeyDown, true);
            return () => {
                document.removeEventListener('keydown', onKeyDown, true);
                if (previous && typeof previous.focus === 'function') {
                    previous.focus();
                }
            };
        }, [containerRef, active]);
    };
})();
