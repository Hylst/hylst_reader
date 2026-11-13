/* Moteur de lecture du livre web statique.
 * Aucun appel externe : donnees chargees localement depuis data/book.json.
 */
"use strict";

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
    app.innerHTML = '<p class="error">Impossible de charger le livre : ' + err.message + "</p>";
  }
}

function renderBook(container, book) {
  container.innerHTML = "";

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
  container.appendChild(header);

  var pages = book.pages || [];
  pages.forEach(function (page, pageIdx) {
    var pageElem = document.createElement("section");
    pageElem.className = "comic-page";
    pageElem.id = page.id || "page-" + (pageIdx + 1);

    if (page.title) {
      var h3 = document.createElement("h3");
      h3.className = "page-title";
      h3.textContent = page.title;
      pageElem.appendChild(h3);
    }

    var grid = document.createElement("div");
    grid.className = "panel-grid";

    (page.panels || []).forEach(function (panel, panelIdx) {
      var panelElem = document.createElement("article");
      panelElem.className = "comic-panel";
      panelElem.id = panel.id || "panel-" + (panelIdx + 1);

      if (panel.image) {
        var imgWrapper = document.createElement("div");
        imgWrapper.className = "panel-image-wrapper";
        var img = document.createElement("img");
        img.src = panel.image;
        img.alt = panel.caption || "Case " + (panelIdx + 1);
        img.loading = "lazy";
        imgWrapper.appendChild(img);
        panelElem.appendChild(imgWrapper);
      }

      if (panel.caption) {
        var recitatif = document.createElement("p");
        recitatif.className = "panel-caption";
        recitatif.textContent = panel.caption;
        panelElem.appendChild(recitatif);
      }

      if (panel.dialogues && panel.dialogues.length > 0) {
        var dialogueBox = document.createElement("div");
        dialogueBox.className = "panel-dialogues";
        panel.dialogues.forEach(function (d) {
          var bubble = document.createElement("p");
          bubble.className = "speech-bubble";
          var speaker = document.createElement("strong");
          speaker.textContent = d.speaker + " : ";
          bubble.appendChild(speaker);
          bubble.appendChild(document.createTextNode("« " + d.text + " »"));
          dialogueBox.appendChild(bubble);
        });
        panelElem.appendChild(dialogueBox);
      }

      grid.appendChild(panelElem);
    });

    pageElem.appendChild(grid);
    container.appendChild(pageElem);
  });
}

document.addEventListener("DOMContentLoaded", boot);
