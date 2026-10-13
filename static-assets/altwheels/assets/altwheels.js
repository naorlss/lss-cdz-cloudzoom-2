"use strict";
if (navigator.clipboard && window.isSecureContext) {
  document.querySelectorAll("[data-copy]").forEach((button) => {
    button.hidden = false;
    button.addEventListener("click", async () => {
      const text = document.getElementById(button.dataset.copy);
      const status = button.parentElement.querySelector(".copy-status");
      if (!text || !status) return;
      try {
        await navigator.clipboard.writeText(text.textContent);
        status.textContent = "Prompt copied.";
      } catch {
        status.textContent = "Copy unavailable. Select the prompt text or download the file.";
      }
    });
  });
}
