/* Moteur de lecture du livre web statique.
 * Aucun appel externe : donnees chargees localement depuis data/book.json.
 * Deux modes : album (page de BD) et webtoon (lecture lineaire).
 */
"use strict";

var MODE_KEY = "le-discours-bd-mode";

function preferredMode() {
  try {
    var stored = window.localStorage.getItem(MODE_KEY);
    if (stored === "album" || stored === "webtoon") {
      return stored;
    }
  } catch (err) {
    /* stockage indisponible : on retombe sur la taille d'ecran */
  }
  return window.matchMedia("(max-width: 760px)").matches ? "webtoon" : "album";
}

function applyMode(mode) {
  document.body.dataset.mode = mode;
  var toggle = document.getElementById("mode-toggle");
  if (!toggle) {
    return;
  }
  var webtoon = mode === "webtoon";
  toggle.textContent = webtoon ? "Mode album" : "Mode webtoon";
  toggle.setAttribute("aria-pressed", webtoon ? "true" : "false");
}

function initModeToggle() {
  applyMode(preferredMode());
  var toggle = document.getElementById("mode-toggle");
  if (!toggle) {
    return;
  }
  toggle.addEventListener("click", function () {
    var next = document.body.dataset.mode === "webtoon" ? "album" : "webtoon";
    applyMode(next);
    try {
      window.localStorage.setItem(MODE_KEY, next);
    } catch (err) {
      /* stockage indisponible : le choix ne survit pas a la session */
    }
  });
}

async function boot() {
  var app = document.getElementById("app");
  if (!app) {
    return;
  }

  try {
    var response = await fetch("data/book.json");
    if (!response.ok) {
      throw new Error("HTTP " + response.status);
    }
    var book = await response.json();
    renderBook(app, book);
  } catch (err) {
    app.textContent = "Impossible de charger le livre : " + err.message;
  }
}

function renderBook(container, book) {
  container.textContent = "";

  var header = document.createElement("div");
  header.className = "book-intro";
  var h2 = document.createElement("h2");
  h2.textContent = book.meta.title;
  header.appendChild(h2);

  if (book.meta.author) {
    var pAuthor = document.createElement("p");
    pAuthor.className = "book-author";
    pAuthor.textContent = "Par " + book.meta.author;
    header.appendChild(pAuthor);
  }

  if (book.meta.note) {
    var pNote = document.createElement("p");
    pNote.className = "book-note";
    pNote.textContent = book.meta.note;
    header.appendChild(pNote);
  }

  container.appendChild(header);

  var pages = book.pages || [];
  pages.forEach(function (page, pageIdx) {
    var pageElem = document.createElement("section");
    pageElem.className = "comic-page";
    pageElem.id = page.id || "page-" + (pageIdx + 1);
    pageElem.dataset.layout = page.layout || "A";

    if (page.title) {
      var h3 = document.createElement("h3");
      h3.className = "page-title";
      h3.textContent = page.title;
      pageElem.appendChild(h3);
    }

    var sheet = document.createElement("div");
    sheet.className = "page-sheet";

    var grid = document.createElement("div");
    grid.className = "panel-grid";

    (page.panels || []).forEach(function (panel, panelIdx) {
      var panelElem = document.createElement("article");
      panelElem.className = "comic-panel panel--" + (panel.format || "portrait");
      panelElem.id = panel.id || "panel-" + (panelIdx + 1);

      var frame = document.createElement("div");
      frame.className = "panel-frame";

      if (panel.image) {
        var img = document.createElement("img");
        img.src = panel.image;
        img.alt = panel.alt || "Case " + (panel.id || panelIdx + 1).replace("panel-", "");
        img.loading = "eager";
        img.decoding = "async";
        frame.appendChild(img);
      }

      var overlay = document.createElement("div");
      overlay.className = "panel-overlay";

      (panel.dialogues || []).forEach(function (dialogue) {
        var bubble = document.createElement("p");
        bubble.className = "speech-bubble tail-" + (dialogue.tail || "bl");
        bubble.style.setProperty("--bx", (dialogue.x != null ? dialogue.x : 50) + "%");
        bubble.style.setProperty("--by", (dialogue.y != null ? dialogue.y : 20) + "%");
        bubble.style.setProperty("--bw", (dialogue.w != null ? dialogue.w : 40) + "%");

        var speaker = document.createElement("strong");
        speaker.className = "bubble-speaker";
        speaker.textContent = dialogue.speaker;

        var text = document.createElement("span");
        text.className = "bubble-text";
        text.textContent = "« " + dialogue.text + " »";

        bubble.appendChild(speaker);
        bubble.appendChild(text);
        overlay.appendChild(bubble);
      });

      if (panel.caption) {
        var recitatif = document.createElement("p");
        recitatif.className = "panel-caption pos-" + (panel.caption_pos || "tl");
        recitatif.textContent = panel.caption;
        if (panel.caption_width) {
          recitatif.style.setProperty("--caption-w", panel.caption_width + "%");
        }
        overlay.appendChild(recitatif);
      }

      frame.appendChild(overlay);
      panelElem.appendChild(frame);
      grid.appendChild(panelElem);
    });

    sheet.appendChild(grid);
    pageElem.appendChild(sheet);
    container.appendChild(pageElem);
  });
}

document.addEventListener("DOMContentLoaded", function () {
  initModeToggle();
  boot();
});
