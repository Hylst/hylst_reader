from pathlib import Path

def test_chapter_assets():
    assets_dir = Path("public/books/chronique-une-atrophie-programmee/assets")
    assert assets_dir.exists(), "Le dossier d'assets n'existe pas"
    for i in range(1, 49):
        img = assets_dir / f"chapter-{i:02d}.webp"
        assert img.exists(), f"Image manquante: {img}"
        size = img.stat().st_size
        assert size > 5000 and size < 600000, f"Image {img} de taille anormale: {size}"
    print("ALL 48 CHAPTER ASSETS OK")

if __name__ == "__main__":
    test_chapter_assets()
