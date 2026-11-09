from pathlib import Path
import re
import unittest

BOOK_DIR = Path("public/books/chronique-une-atrophie-programmee")

DASH_CHARS = {
    "\u2012": "FIGURE DASH",
    "\u2013": "EN DASH",
    "\u2014": "EM DASH",
    "\u2015": "HORIZONTAL BAR",
    "\ufe58": "SMALL EM DASH",
}


class TestAct4Expansion(unittest.TestCase):
    def get_chapter_path(self, num: int) -> Path:
        matches = list(BOOK_DIR.glob(f"{num:02d}-*.html"))
        self.assertEqual(len(matches), 1, f"Fichier pour chapitre {num} introuvable")
        return matches[0]

    def count_words(self, html: str) -> int:
        clean = re.sub(r"<[^>]+>", " ", html)
        return len(re.findall(r"\b\w+\b", clean))

    def test_chapter_files_exist(self):
        for i in range(37, 49):
            self.assertTrue(self.get_chapter_path(i).is_file())
        interlude = BOOK_DIR / "interlude-04-liturgie-du-frisson.html"
        self.assertTrue(interlude.is_file(), f"Fichier d'interlude manquant : {interlude}")

    def test_word_counts(self):
        ch47_path = self.get_chapter_path(47)
        ch47_words = self.count_words(ch47_path.read_text(encoding="utf-8"))
        self.assertGreaterEqual(
            ch47_words, 2500, f"Le chapitre 47 (Chapitre-Pilier) doit dépasser 2 500 mots (actuel: {ch47_words})"
        )

        total_words = 0
        for i in range(37, 49):
            p = self.get_chapter_path(i)
            words = self.count_words(p.read_text(encoding="utf-8"))
            total_words += words
            self.assertGreaterEqual(words, 750, f"Le chapitre {i} doit dépasser 750 mots (actuel: {words})")

        interlude_path = BOOK_DIR / "interlude-04-liturgie-du-frisson.html"
        self.assertTrue(interlude_path.is_file(), f"Fichier d'interlude manquant : {interlude_path}")
        i_words = self.count_words(interlude_path.read_text(encoding="utf-8"))
        total_words += i_words
        self.assertGreaterEqual(i_words, 400, f"L'interlude 04 doit dépasser 400 mots (actuel: {i_words})")

        self.assertGreaterEqual(
            total_words, 13500, f"L'Acte 4 complet doit atteindre au moins 13 500 mots (actuel: {total_words})"
        )

    def test_html_structure_and_tags(self):
        for i in range(37, 49):
            content = self.get_chapter_path(i).read_text(encoding="utf-8")
            self.assertIn('<div class="chapter-content">', content)
            self.assertIn(f"Chapitre {i} :", content)
            self.assertIn('<p class="chapter-byline">ACTE 4 : L\'Hérésie du Pollen</p>', content)
            self.assertIn(f"chapter-{i:02d}.webp?v=5", content)
            self.assertIn('<p class="chapter-paragraph">', content)
            self.assertTrue(content.strip().endswith("</div>"))

        interlude_path = BOOK_DIR / "interlude-04-liturgie-du-frisson.html"
        if interlude_path.is_file():
            content = interlude_path.read_text(encoding="utf-8")
            self.assertIn('<div class="chapter-content">', content)
            self.assertIn("Interlude IV", content)
            self.assertIn('<p class="chapter-paragraph">', content)
            self.assertTrue(content.strip().endswith("</div>"))

    def test_canon_concepts_act4(self):
        # Heist and assault on Tour Zephyr (ch 41 to 44)
        ch41 = self.get_chapter_path(41).read_text(encoding="utf-8").lower()
        self.assertTrue("zéphyr" in ch41 or "zephyr" in ch41)
        self.assertTrue("turbine" in ch41 or "aspiration" in ch41)
        self.assertTrue("fers" in ch41 or "cliquet" in ch41 or "marthe" in ch41)

        ch44 = self.get_chapter_path(44).read_text(encoding="utf-8").lower()
        self.assertTrue("herse" in ch44)
        self.assertTrue("mollet" in ch44 or "jambe" in ch44 or "chair" in ch44)

        # Biological impact and civilian toll (ch 45-46)
        ch45 = self.get_chapter_path(45).read_text(encoding="utf-8").lower()
        self.assertTrue("ambroisie" in ch45 or "pollen" in ch45)
        self.assertTrue("belleville" in ch45 or "alvéole" in ch45 or "alveole" in ch45)

        ch46 = self.get_chapter_path(46).read_text(encoding="utf-8").lower()
        self.assertTrue("asphyxie" in ch46 or "quincke" in ch46 or "étouff" in ch46 or "etouff" in ch46 or "œdème" in ch46 or "oedeme" in ch46)
        self.assertTrue("tristan" in ch46)
        self.assertTrue("antihistaminique" in ch46 or "adrénaline" in ch46 or "adrenaline" in ch46 or "dispensaire" in ch46)

        # Coup de maitre and Tristan's fate in Frisson Divin (ch 47)
        ch47 = self.get_chapter_path(47).read_text(encoding="utf-8").lower()
        self.assertTrue("frisson divin" in ch47)
        self.assertTrue("dopamine" in ch47)
        self.assertTrue("histamine" in ch47)
        self.assertTrue("tristan" in ch47)
        self.assertTrue("danse" in ch47 or "dansent" in ch47 or "dansai" in ch47)

        # Barnabe's deathbed vigil, burial and Romainville (ch 48)
        ch48 = self.get_chapter_path(48).read_text(encoding="utf-8").lower()
        self.assertTrue("barnabé" in ch48)
        self.assertTrue("graine" in ch48 or "semence" in ch48)
        self.assertTrue("meulière" in ch48 or "meuliere" in ch48 or "terre" in ch48)
        self.assertTrue("romainville" in ch48)
        self.assertTrue("marthe" in ch48)
        self.assertTrue("cliquet" in ch48)

        # Interlude 04
        interlude_path = BOOK_DIR / "interlude-04-liturgie-du-frisson.html"
        if interlude_path.is_file():
            i4 = interlude_path.read_text(encoding="utf-8").lower()
            self.assertTrue("frisson divin" in i4)
            self.assertTrue("dopamine" in i4)
            self.assertTrue("s.y.n.d.i.c." in i4)

    def test_zero_forbidden_dashes(self):
        found_dashes = []
        for i in range(37, 49):
            p = self.get_chapter_path(i)
            text = p.read_text(encoding="utf-8")
            for lineno, line in enumerate(text.splitlines(), 1):
                for char, name in DASH_CHARS.items():
                    if char in line:
                        found_dashes.append((p.name, lineno, name, line))

        interlude_path = BOOK_DIR / "interlude-04-liturgie-du-frisson.html"
        if interlude_path.is_file():
            text = interlude_path.read_text(encoding="utf-8")
            for lineno, line in enumerate(text.splitlines(), 1):
                for char, name in DASH_CHARS.items():
                    if char in line:
                        found_dashes.append((interlude_path.name, lineno, name, line))

        self.assertEqual(found_dashes, [], f"Tirets interdits détectés : {found_dashes}")


if __name__ == "__main__":
    unittest.main()
