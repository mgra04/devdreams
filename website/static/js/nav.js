document.addEventListener("DOMContentLoaded", () => {
  const hamburgerMenu = document.getElementById("hamburger-menu");
  const navigation = document.getElementById("navigation");
  const hamburgerIcon = document.getElementById("hamburger-icon");
  const closeIcon = document.getElementById("close-icon");
  const topNav = document.querySelector(".top-nav");

  hamburgerMenu.addEventListener("click", () => {
    if (navigation.classList.contains("active")) {
      navigation.classList.remove("active");
      navigation.classList.add("inactive");
    } else {
      navigation.classList.remove("inactive");
      navigation.classList.add("active");
    }

    hamburgerIcon.style.display =
      hamburgerIcon.style.display === "none" ? "block" : "none";
    closeIcon.style.display =
      closeIcon.style.display === "none" ? "block" : "none";
  });

  window.addEventListener("scroll", () => {
    if (window.scrollY > 0) {
      topNav.classList.add("scrolled");
    } else {
      topNav.classList.remove("scrolled");
    }
  });
});
