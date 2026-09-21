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
