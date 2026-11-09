from pathlib import Path
import xml.etree.ElementTree as ET

def test_neuro_svgs():
    img_dir = Path("public/books/approche-de-la-neurodiversite/images")
    assert img_dir.exists(), "Le dossier images n'existe pas"
    for name in ["neuro-schema-1-familles.svg", "neuro-schema-2-pedagogie.svg", "neuro-schema-3-bequilles.svg"]:
        p = img_dir / name
        assert p.exists(), f"Fichier manquant: {p}"
        tree = ET.parse(p)
        root = tree.getroot()
        assert "viewBox" in root.attrib, f"Pas de viewBox dans {name}"
        assert len(root.findall(".//{http://www.w3.org/2000/svg}text")) > 5, f"Texte insuffisant dans {name}"
    print("ALL 3 NEURO SVG SCHEMAS OK")

if __name__ == "__main__":
    test_neuro_svgs()
