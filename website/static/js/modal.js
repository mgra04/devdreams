document.querySelector(".subscribe-btn").addEventListener("click", function () {
  var modal = document.getElementById("newsletterModal");
  modal.style.display = "flex";
  setTimeout(function () {
    modal.style.display = "none";
  }, 5000);
});

window.addEventListener("click", function (event) {
  var modal = document.getElementById("newsletterModal");
  if (event.target == modal) {
    modal.style.display = "none";
  }
});

document.querySelector(".modal-close").addEventListener("click", function () {
  var modal = document.getElementById("newsletterModal");
  modal.style.display = "none";
});
