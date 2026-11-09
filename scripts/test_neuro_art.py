from pathlib import Path
from PIL import Image

def test_neuro_art():
    img_dir = Path("public/books/approche-de-la-neurodiversite/images")
    for name in ["partie-1-couverture.webp", "partie-2-couverture.webp", "partie-3-couverture.webp", "epilogue-couverture.webp"]:
        p = img_dir / name
        assert p.exists(), f"Image manquante: {p}"
        im = Image.open(p)
        assert im.format == "WEBP", f"Format non webp: {im.format}"
        assert p.stat().st_size > 5000 and p.stat().st_size < 600000, f"Taille anormale: {p.stat().st_size}"
    print("ALL 4 NEURO ART ASSETS OK")

if __name__ == "__main__":
    test_neuro_art()
