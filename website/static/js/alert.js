const alert = document.querySelector(".alert");
const closeButtons = document.querySelectorAll(".close");

document.addEventListener("DOMContentLoaded", () => {
  if (alert) {
    alert.classList.add("show");

    setTimeout(() => {
      alert.classList.remove("show");
    }, 5000);
  }

  closeButtons.forEach((button) => {
    button.addEventListener("click", () => {
      const alert = button.parentElement;
      alert.classList.add("fade-out");

      setTimeout(() => {
        alert.style.display = "none";
      }, 300);
    });
  });
});
