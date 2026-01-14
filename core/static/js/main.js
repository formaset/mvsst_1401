const navToggle = document.querySelector(".nav-toggle");
const nav = document.querySelector(".site-nav");

if (navToggle && nav) {
  navToggle.addEventListener("click", () => {
    const open = nav.classList.toggle("open");
    navToggle.setAttribute("aria-expanded", open);
  });
}

const lightbox = document.getElementById("lightbox");
if (lightbox) {
  const img = lightbox.querySelector("img");
  const closeBtn = lightbox.querySelector(".lightbox-close");
  document.querySelectorAll(".lightbox-trigger").forEach((button) => {
    button.addEventListener("click", () => {
      const src = button.getAttribute("data-lightbox-src");
      if (src) {
        img.src = src;
        lightbox.classList.add("open");
      }
    });
  });
  closeBtn.addEventListener("click", () => {
    lightbox.classList.remove("open");
    img.removeAttribute("src");
  });
  lightbox.addEventListener("click", (event) => {
    if (event.target === lightbox) {
      lightbox.classList.remove("open");
      img.removeAttribute("src");
    }
  });
}
