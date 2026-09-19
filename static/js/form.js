(function () {
  const select = document.getElementById("service-select");
  document.querySelectorAll("[data-service]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      const id = btn.getAttribute("data-service");
      if (select && id) {
        select.value = id;
      }
    });
  });

  const form = document.getElementById("service-form");
  if (!form) return;

  form.addEventListener("submit", function (event) {
    const name = form.elements.name.value.trim();
    const wa = form.elements.whatsapp.value.trim();
    const service = form.elements.service.value;
    const missing = [];
    if (name.length < 2) missing.push("nom");
    if (wa.length < 8) missing.push("WhatsApp");
    if (!service) missing.push("service");
    if (missing.length) {
      event.preventDefault();
      alert("Veuillez remplir les champs obligatoires : " + missing.join(", "));
      return;
    }

    // Formulaire Flask standard - laisser le navigateur gérer la soumission
    const submitBtn = form.querySelector('button[type="submit"]');
    const originalText = submitBtn.textContent;
    submitBtn.textContent = "Envoi en cours...";
    submitBtn.disabled = true;

    // Le formulaire sera soumis normalement
  });
})();
