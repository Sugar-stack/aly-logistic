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

// =========================
// ASSISTANT IA ALY TECH
// =========================

const aiChatToggle = document.getElementById("ai-chat-toggle");
const aiChatWindow = document.getElementById("ai-chat-window");
const aiChatClose = document.getElementById("ai-chat-close");
const aiChatForm = document.getElementById("ai-chat-form");
const aiChatInput = document.getElementById("ai-chat-input");
const aiChatMessages = document.getElementById("ai-chat-messages");

if (
    aiChatToggle &&
    aiChatWindow &&
    aiChatClose &&
    aiChatForm &&
    aiChatInput &&
    aiChatMessages
) {
    aiChatToggle.addEventListener("click", () => {
        aiChatWindow.classList.toggle("active");

        if (aiChatWindow.classList.contains("active")) {
            aiChatInput.focus();
        }
    });

    aiChatClose.addEventListener("click", () => {
        aiChatWindow.classList.remove("active");
    });

    aiChatForm.addEventListener("submit", async (event) => {
        event.preventDefault();

        const message = aiChatInput.value.trim();

        if (!message) return;

        const userMessage = document.createElement("div");
        userMessage.className = "user-message";
        userMessage.textContent = message;

        aiChatMessages.appendChild(userMessage);
        aiChatInput.value = "";

        const loadingMessage = document.createElement("div");
        loadingMessage.className = "ai-message";
        loadingMessage.textContent = "Je réfléchis...";
        aiChatMessages.appendChild(loadingMessage);

        aiChatMessages.scrollTop = aiChatMessages.scrollHeight;

        try {
            const response = await fetch("/api/chat", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    message: message
                })
            });

            const data = await response.json();

            loadingMessage.remove();

            const aiMessage = document.createElement("div");
            aiMessage.className = "ai-message";
            aiMessage.textContent = data.reply || "Une erreur est survenue.";

            aiChatMessages.appendChild(aiMessage);

        } catch (error) {
            loadingMessage.textContent =
                "Impossible de contacter l'assistant pour le moment.";
        }

        aiChatMessages.scrollTop = aiChatMessages.scrollHeight;
    });
}

// =========================
// AVIS CLIENTS — NEON
// =========================

async function loadRealReviews() {
    const reviewsContainer = document.getElementById("real-reviews");

    if (!reviewsContainer) return;

    try {
        const response = await fetch("/api/reviews");

        if (!response.ok) {
            throw new Error("Erreur lors du chargement des avis");
        }

        const data = await response.json();

        reviewsContainer.innerHTML = "";

        data.reviews.forEach(review => {
            const article = document.createElement("blockquote");
            article.className = "card quote reveal";

            const stars = "★".repeat(review.rating) +
                          "☆".repeat(5 - review.rating);

            article.innerHTML = `
                <p class="stars" aria-label="${review.rating} sur 5">
                    ${stars}
                </p>

                <p>${escapeHtml(review.comment)}</p>

                <footer>
                    <strong>${escapeHtml(review.name)}</strong>
                </footer>
            `;

            reviewsContainer.appendChild(article);
        });

    } catch (error) {
        console.error("Erreur avis :", error);
    }
}

function escapeHtml(text) {
    const div = document.createElement("div");
    div.textContent = text;
    return div.innerHTML;
}

loadRealReviews();

// =========================
// ENVOI D'UN AVIS CLIENT
// =========================

const reviewForm = document.getElementById("review-form");
const reviewMessage = document.getElementById("review-message");

if (reviewForm && reviewMessage) {
    reviewForm.addEventListener("submit", async (event) => {
        event.preventDefault();

        const name = document.getElementById("review-name").value.trim();
        const rating = document.getElementById("review-rating").value;
        const comment = document.getElementById("review-comment").value.trim();

        if (!name || !rating || !comment) {
            reviewMessage.textContent = "Veuillez remplir tous les champs.";
            return;
        }

        reviewMessage.textContent = "Envoi de votre avis...";

        try {
            const response = await fetch("/api/reviews", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    name: name,
                    rating: rating,
                    comment: comment
                })
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || "Une erreur est survenue.");
            }

            reviewMessage.textContent = data.message;

            reviewForm.reset();

        } catch (error) {
            console.error("Erreur envoi avis :", error);
            reviewMessage.textContent =
                "Impossible d'envoyer votre avis pour le moment.";
        }
    });
}
