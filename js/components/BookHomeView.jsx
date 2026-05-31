// js/components/BookHomeView.jsx
// Dépend de : window.Icon

const { useState: useStateBookHome, useEffect: useEffectBookHome } = React;

function BookHomeView({ book, onBack, onStartReading }) {
    const Icon = window.Icon;
    const [coverUrl, setCoverUrl] = useStateBookHome(null);
    const [introHtml, setIntroHtml] = useStateBookHome('');

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

    return (
        <div className="book-home view-enter">
            <div className="book-home-header">
                <button className="btn btn-ghost" onClick={onBack}><Icon.ArrowLeft /> Bibliothèque</button>
            </div>
            <div className="book-home-content">
                <div className="book-home-cover">
                    {coverUrl && <img src={coverUrl} alt={`Couverture – ${book.title}`} />}
                </div>
                <div className="book-home-meta">
                    <h1 className="book-home-title">{book.title}</h1>
                    <p className="book-home-author">{book.author} {book.year ? `· ${book.year}` : ''}</p>
                    <button className="btn btn-primary" style={{ padding: '0.85rem 2rem', fontSize: '1rem', marginBottom: '2rem' }} onClick={onStartReading}>
                        Commencer la lecture <Icon.ArrowRight />
                    </button>
                    <div className="book-home-intro reader-article" dangerouslySetInnerHTML={{ __html: introHtml }} />
                </div>
            </div>
        </div>
    );
}

window.BookHomeView = BookHomeView;
