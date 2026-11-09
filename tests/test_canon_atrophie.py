from pathlib import Path
import unittest

BIBLE_PATH = Path("docs/superpowers/specs/bible-atrophie-canon.md")

DASH_CHARS = {
    "\u2012": "FIGURE DASH",
    "\u2013": "EN DASH",
    "\u2014": "EM DASH",
    "\u2015": "HORIZONTAL BAR",
    "\ufe58": "SMALL EM DASH",
}

MANDATORY_TERMS = [
    "Écœurement Sémantique",
    "Fers de marche",
    "Tonicité Dégressive",
    "Rupture d'antihistaminiques",
    "Frisson Divin",
]

MANDATORY_SECTIONS = [
    "Chronologie",
    "S.Y.N.D.I.C.",
    "Barnabé",
    "Marthe",
    "Tristan",
    "Le Cliquet",
    "Léonce",
    "Galeries",
]


class TestCanonAtrophie(unittest.TestCase):
    def test_bible_file_exists(self):
        self.assertTrue(BIBLE_PATH.exists(), f"Le fichier de canon est introuvable : {BIBLE_PATH}")

    def test_mandatory_terms_present(self):
        content = BIBLE_PATH.read_text(encoding="utf-8")
        for term in MANDATORY_TERMS:
            self.assertIn(term, content, f"Terme obligatoire manquant dans la Bible : '{term}'")

    def test_chronology_span(self):
        content = BIBLE_PATH.read_text(encoding="utf-8")
        self.assertIn("2038", content, "La chronologie doit débuter ou inclure 2038")
        self.assertIn("2080", content, "La chronologie doit s'étendre jusqu'à 2080")

    def test_mandatory_sections_and_characters(self):
        content = BIBLE_PATH.read_text(encoding="utf-8")
        for section in MANDATORY_SECTIONS:
            self.assertIn(section, content, f"Section ou personnage obligatoire manquant : '{section}'")

    def test_zero_forbidden_dashes(self):
        content = BIBLE_PATH.read_text(encoding="utf-8")
        found_dashes = []
        for lineno, line in enumerate(content.splitlines(), 1):
            for char, name in DASH_CHARS.items():
                if char in line:
                    found_dashes.append((lineno, name, line))
        self.assertEqual(
            found_dashes,
            [],
            f"Tirets cadratins/demi-cadratins interdits détectés dans {BIBLE_PATH} : {found_dashes}",
        )


if __name__ == "__main__":
    unittest.main()
