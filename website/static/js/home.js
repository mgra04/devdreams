document.addEventListener("DOMContentLoaded", () => {
  const exploreBtn = document.querySelector(".explore-btn");
  const exploreSection = document.querySelector(".home-divider-box");

  exploreBtn.addEventListener("click", () => {
    exploreSection.scrollIntoView({ behavior: "smooth" });
  });
});
