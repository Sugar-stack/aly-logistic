(function () {
  const header = document.getElementById("site-header");
  const toggle = document.querySelector(".nav-toggle");
  const mobile = document.getElementById("nav-mobile");

  if (toggle && mobile) {
    toggle.addEventListener("click", function () {
      const open = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!open));
      if (!open) {
        mobile.style.display = "grid";
        mobile.hidden = false;
      } else {
        mobile.style.display = "none";
        mobile.hidden = true;
      }
    });
    mobile.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        mobile.style.display = "none";
        mobile.hidden = true;
        toggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  const io = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
          io.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12 }
  );
  document.querySelectorAll(".reveal").forEach(function (el) {
    io.observe(el);
  });

  window.addEventListener("scroll", function () {
    if (!header) return;
    header.style.boxShadow = window.scrollY > 10 ? "0 4px 20px rgba(0,0,0,.1)" : "none";
  });
})();
