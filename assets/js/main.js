// =========================================================================
// Ulises Rodriguez — Portfolio — shared behaviour
// =========================================================================

(function () {
  "use strict";

  /* ---------------- language toggle ---------------- */
  var LANG_KEY = "ur_portfolio_lang";
  var html = document.documentElement;

  function applyLang(lang) {
    html.setAttribute("data-lang", lang);
    document.querySelectorAll("[data-lang-target]").forEach(function (el) {
      el.textContent = lang.toUpperCase();
    });
    localStorage.setItem(LANG_KEY, lang);
  }

  var savedLang = localStorage.getItem(LANG_KEY) || "es";
  applyLang(savedLang);

  document.querySelectorAll(".lang-toggle").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var current = html.getAttribute("data-lang") || "es";
      applyLang(current === "es" ? "en" : "es");
    });
  });

  /* ---------------- mobile nav ---------------- */
  var navToggle = document.querySelector(".nav-toggle");
  var navLinks = document.querySelector(".nav-links");
  if (navToggle && navLinks) {
    navToggle.addEventListener("click", function () {
      navLinks.classList.toggle("open");
    });
    navLinks.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        navLinks.classList.remove("open");
      });
    });
  }

  /* ---------------- scroll reveal ---------------- */
  var revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && revealEls.length) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("in");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12 }
    );
    revealEls.forEach(function (el) {
      io.observe(el);
    });
  } else {
    revealEls.forEach(function (el) {
      el.classList.add("in");
    });
  }

  /* ---------------- active nav link on scroll ---------------- */
  var sections = document.querySelectorAll("section[id]");
  var navAnchors = document.querySelectorAll(".nav-links a[href^='#']");
  if (sections.length && navAnchors.length) {
    var spy = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          var id = entry.target.getAttribute("id");
          var link = document.querySelector('.nav-links a[href="#' + id + '"]');
          if (!link) return;
          if (entry.isIntersecting) {
            navAnchors.forEach(function (a) {
              a.classList.remove("active");
            });
            link.classList.add("active");
          }
        });
      },
      { rootMargin: "-45% 0px -50% 0px" }
    );
    sections.forEach(function (s) {
      spy.observe(s);
    });
  }

  /* ---------------- hero role typing effect ---------------- */
  var roleEl = document.querySelector("[data-role-type]");
  if (roleEl) {
    var rolesEs = ["Ingeniería en Computación", "Software & Hardware", "Sistemas Embebidos", "IEEE FACET · Presidente"];
    var rolesEn = ["Computer Engineering", "Software & Hardware", "Embedded Systems", "IEEE FACET · Chapter Chair"];
    var i = 0, charIdx = 0, deleting = false;

    function currentList() {
      return (html.getAttribute("data-lang") === "en") ? rolesEn : rolesEs;
    }

    function tick() {
      var list = currentList();
      if (i >= list.length) i = 0;
      var word = list[i];

      if (!deleting) {
        charIdx++;
        roleEl.textContent = word.slice(0, charIdx);
        if (charIdx === word.length) {
          deleting = true;
          setTimeout(tick, 1700);
          return;
        }
      } else {
        charIdx--;
        roleEl.textContent = word.slice(0, charIdx);
        if (charIdx === 0) {
          deleting = false;
          i++;
        }
      }
      setTimeout(tick, deleting ? 35 : 65);
    }
    tick();
  }

  /* ---------------- oscilloscope / waveform canvas (hero signature) ---------------- */
  var scopeSvg = document.querySelector("[data-scope]");
  if (scopeSvg) {
    var path = scopeSvg.querySelector("path");
    var w = 300, h = 46, points = 60;
    var t = 0;

    function buildWave() {
      var d = "M0," + h / 2;
      for (var p = 0; p <= points; p++) {
        var x = (p / points) * w;
        var y =
          h / 2 +
          Math.sin(p * 0.35 + t) * 8 * Math.sin(t * 0.4) +
          Math.sin(p * 0.9 + t * 1.6) * 5 +
          Math.sin(p * 0.12 + t * 0.6) * 4;
        d += " L" + x.toFixed(1) + "," + y.toFixed(1);
      }
      path.setAttribute("d", d);
      t += 0.05;
      requestAnimationFrame(buildWave);
    }
    if (!window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      buildWave();
    }
  }

  /* ---------------- project category filter (index page) ---------------- */
  var filterBtns = document.querySelectorAll(".proj-filter");
  var projCards = document.querySelectorAll(".proj-card");
  if (filterBtns.length && projCards.length) {
    filterBtns.forEach(function (btn) {
      btn.addEventListener("click", function () {
        filterBtns.forEach(function (b) {
          b.classList.remove("active");
        });
        btn.classList.add("active");
        var cat = btn.getAttribute("data-filter");
        projCards.forEach(function (card) {
          var show = cat === "all" || card.getAttribute("data-cat") === cat;
          card.style.display = show ? "" : "none";
        });
      });
    });
  }

  /* ---------------- current year ---------------- */
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
