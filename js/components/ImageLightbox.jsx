// js/components/ImageLightbox.jsx
// Visionneuse plein écran pour les couvertures et illustrations
// Dépend de : window.Icon

const { useEffect: useEffectLightbox, useRef: useRefLightbox } = React;

function ImageLightbox({ data, onClose }) {
    const Icon = window.Icon;
    const dialogRef = useRefLightbox(null);
    const closeBtnRef = useRefLightbox(null);

    useEffectLightbox(() => {
        if (!data) return;

        const previouslyFocused = document.activeElement;
        if (closeBtnRef.current) {
            closeBtnRef.current.focus();
        }

        const handleKeyDown = (e) => {
            if (e.key === 'Escape') {
                e.preventDefault();
                e.stopPropagation();
                e.stopImmediatePropagation();
                onClose();
            } else if (e.key === 'Tab' && dialogRef.current) {
                const focusable = dialogRef.current.querySelectorAll('button, [tabindex="0"]');
                if (focusable.length === 0) return;
                const first = focusable[0];
                const last = focusable[focusable.length - 1];
                if (e.shiftKey && document.activeElement === first) {
                    e.preventDefault();
                    last.focus();
                } else if (!e.shiftKey && document.activeElement === last) {
                    e.preventDefault();
                    first.focus();
                }
            }
        };

        const originalOverflow = document.body.style.overflow;
        document.body.style.overflow = 'hidden';

        window.addEventListener('keydown', handleKeyDown, true);
        return () => {
            document.body.style.overflow = originalOverflow;
            window.removeEventListener('keydown', handleKeyDown, true);
            if (previouslyFocused && typeof previouslyFocused.focus === 'function') {
                previouslyFocused.focus();
            }
        };
    }, [data, onClose]);

    if (!data) return null;

    const { src, alt = '', title = '', subtitle = '' } = data;

    return (
        <div
            className="lightbox-backdrop"
            onClick={(e) => e.target === e.currentTarget && onClose()}
            role="dialog"
            aria-modal="true"
            aria-label={title || "Agrandissement de l'image"}
            ref={dialogRef}
        >
            <div className="lightbox-dialog">
                <button
                    type="button"
                    className="btn btn-ghost btn-icon lightbox-close-btn"
                    onClick={onClose}
                    title="Fermer (Échap)"
                    aria-label="Fermer la vue agrandie"
                    ref={closeBtnRef}
                >
                    <Icon.X />
                </button>

                <div className="lightbox-image-wrapper">
                    <img
                        src={src}
                        alt={alt || title}
                        className="lightbox-image"
                        loading="eager"
                    />
                </div>

                {(title || subtitle) && (
                    <div className="lightbox-caption">
                        {title && <div className="lightbox-caption-title">{title}</div>}
                        {subtitle && <div className="lightbox-caption-subtitle">{subtitle}</div>}
                    </div>
                )}
            </div>
        </div>
    );
}

window.ImageLightbox = ImageLightbox;
