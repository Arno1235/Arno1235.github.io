(function () {
  var key = "ave-theme";

  function prefersDark() {
    try {
      var stored = localStorage.getItem(key);
      if (stored === "dark") return true;
      if (stored === "light") return false;
    } catch (e) {}
    return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
  }

  function markup(dark) {
    return dark
      ? '<button type="button" data-set="light">light</button> / <span>dark</span>'
      : '<span>light</span> / <button type="button" data-set="dark">dark</button>';
  }

  function paint(dark) {
    document.documentElement.classList.toggle("dark", dark);
    document.body.classList.toggle("dark", dark);
    document.documentElement.style.colorScheme = dark ? "dark" : "light";
    document.body.style.colorScheme = dark ? "dark" : "light";
    document.querySelectorAll("[data-theme-toggle]").forEach(function (el) {
      el.innerHTML = markup(dark);
    });
  }

  paint(prefersDark());

  document.addEventListener("click", function (e) {
    var btn = e.target.closest && e.target.closest("[data-theme-toggle] [data-set]");
    if (!btn) return;
    var dark = btn.getAttribute("data-set") === "dark";
    try { localStorage.setItem(key, dark ? "dark" : "light"); } catch (err) {}
    paint(dark);
  });

  document.querySelectorAll(".project").forEach(function (row) {
    var link = row.querySelector(".name");
    if (!link) return;
    row.addEventListener("click", function (e) {
      if (e.target.closest("a")) return;
      location.href = link.getAttribute("href");
    });
  });
})();
