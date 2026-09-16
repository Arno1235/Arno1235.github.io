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

  function paint(dark) {
    document.documentElement.classList.toggle("dark", dark);
    document.body.classList.toggle("dark", dark);
    var el = document.getElementById("theme");
    if (!el) return;
    var prefix = el.getAttribute("data-prefix");
    var toggle = dark
      ? '<a href="#light">light</a> / dark'
      : 'light / <a href="#dark">dark</a>';
    el.innerHTML = prefix ? prefix + " · " + toggle : toggle;
  }

  paint(prefersDark());

  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("#theme a");
    if (!a) return;
    e.preventDefault();
    var dark = a.getAttribute("href") === "#dark";
    try {
      localStorage.setItem(key, dark ? "dark" : "light");
    } catch (err) {}
    paint(dark);
  });
})();
