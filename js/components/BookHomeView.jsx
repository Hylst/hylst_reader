// js/components/BookHomeView.jsx
// Dépend de : window.Icon

const { useState: useStateBookHome, useEffect: useEffectBookHome } = React;

function BookHomeView({ book, onBack, onStartReading }) {
    const Icon = window.Icon;
    const [coverUrl, setCoverUrl] = useStateBookHome(null);
    const [introHtml, setIntroHtml] = useStateBookHome('');
    const [citationCopied, setCitationCopied] = useStateBookHome(false);

    useEffectBookHome(() => {
        if (book.coverBlob) {
            const url = URL.createObjectURL(book.coverBlob);
            setCoverUrl(url);
            return () => URL.revokeObjectURL(url);
        } else if (book.coverPath) {
            setCoverUrl(`public/${book.coverPath}?t=${Date.now()}`);
        }
    }, [book.coverBlob, book.coverPath]);

    useEffectBookHome(() => {
        if (!book.introHtml && book.introPath) {
            window.fetch(`public/${book.introPath}?t=${Date.now()}`)
                .then(r => r.text())
                .then(html => setIntroHtml(html))
                .catch(() => setIntroHtml('<p>Introduction non disponible.</p>'));
        } else {
            setIntroHtml(book.introHtml || '');
        }
    }, [book.id, book.introHtml, book.introPath]);

    const safeIntroHtml = book.isImported
        ? (window.HylstSanitize
            ? window.HylstSanitize.sanitizeHtml(introHtml)
            : '<p>Contenu importé bloqué : le module de sécurité HylstSanitize est indisponible.</p>')
        : introHtml;

    const citationUrl = book.isImported
        ? window.location.href
        : new URL(`livres/${book.id}/`, document.baseURI).href;
    const citationText = `Geoffroy Streit (Hylst), « ${book.title}${book.subtitle ? ` · ${book.subtitle}` : ''} », ${book.year || 's. d.'}. La Bibliothèque de Hylst. ${citationUrl}`;

    const copyCitation = async () => {
        try {
            if (navigator.clipboard && window.isSecureContext) {
                await navigator.clipboard.writeText(citationText);
            } else {
                const area = document.createElement('textarea');
                area.value = citationText;
                area.setAttribute('readonly', '');
                area.style.position = 'fixed';
                area.style.opacity = '0';
                document.body.appendChild(area);
                area.select();
                document.execCommand('copy');
                document.body.removeChild(area);
            }
            setCitationCopied(true);
            window.setTimeout(() => setCitationCopied(false), 2200);
        } catch (e) {
            window.prompt('Copier la citation :', citationText);
        }
    };

    const handleZoom = () => {
        if (coverUrl && typeof window.openLightbox === 'function') {
            window.openLightbox({
                src: coverUrl,
                alt: book.title,
                title: book.title,
                subtitle: `${book.author || ''}${book.year ? ` · ${book.year}` : ''}`
            });
        }
    };

    return (
        <main className="book-home view-enter">
            <div className="book-home-header">
                <button className="btn btn-ghost" onClick={onBack}><Icon.ArrowLeft /> Bibliothèque</button>
            </div>
            <div className="book-home-content">
                <div
                    className={`book-home-cover${coverUrl ? ' zoomable' : ''}`}
                    onClick={coverUrl ? handleZoom : undefined}
                    title={coverUrl ? "Cliquer pour agrandir la couverture" : undefined}
                    role={coverUrl ? "button" : undefined}
                    tabIndex={coverUrl ? 0 : undefined}
                    onKeyDown={coverUrl ? (e) => {
                        if (e.key === 'Enter' || e.key === ' ') {
                            e.preventDefault();
                            handleZoom();
                        }
                    } : undefined}
                >
                    {coverUrl
                        ? (
                            <>
                                <img src={coverUrl} alt={`Couverture de ${book.title}`} />
                                <span className="book-home-cover-zoom-hint">
                                    <Icon.ZoomIn /> Agrandir
                                </span>
                            </>
                        )
                        : <div className="book-cover-fallback book-cover-fallback-home">
                            <span className="book-cover-fallback-title">{book.title}</span>
                            {book.subtitle && <span className="book-cover-fallback-subtitle">{book.subtitle}</span>}
                            <span className="book-cover-fallback-author">{book.author}</span>
                        </div>}
                </div>
                <div className="book-home-meta">
                    <h1 className="book-home-title">{book.title}</h1>
                    <p className="book-home-author">{book.author} {book.year ? `· ${book.year}` : ''}</p>
                    {!book.isImported && (
                        <div className="book-rights-row">
                            <p className="book-rights-line">
                                Texte de <strong>Geoffroy Streit</strong> &middot; &copy; Tous droits réservés &middot;
                                {' '}<a href="droits.html">Citation &amp; IA</a>
                            </p>
                            <button type="button" className="btn btn-ghost book-cite-btn" onClick={copyCitation} title="Copier la référence de cette œuvre">
                                <Icon.Copy /> {citationCopied ? 'Citation copiée' : 'Citer'}
                            </button>
                        </div>
                    )}
                    <button className="btn btn-primary" style={{ padding: '0.85rem 2rem', fontSize: '1rem', marginBottom: '2rem' }} onClick={onStartReading}>
                        Commencer la lecture <Icon.ArrowRight />
                    </button>
                    <div className="book-home-intro reader-article" dangerouslySetInnerHTML={{ __html: safeIntroHtml }} />
                </div>
            </div>
        </main>
    );
}

window.BookHomeView = BookHomeView;
