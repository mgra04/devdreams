document.addEventListener("DOMContentLoaded", function () {
  const switchToSignUpBtn = document.getElementById("switch-to-sign-up");
  const switchToSignInBtn = document.getElementById("switch-to-sign-in");
  const signInForm = document.querySelector(".sign-in-form");
  const signUpForm = document.querySelector(".sign-up-form");
  const signInFormBtn = document.querySelector(".form-sign-in-btn");
  const signUpFormBtn = document.querySelector(".form-sign-up-btn");
  const signInRightSide = document.querySelector(".sign-in-right-side");
  const signUpRightSide = document.querySelector(".sign-un-right-side");

  switchToSignUpBtn.addEventListener("click", function (event) {
    event.preventDefault();
    signInForm.style.display = "none";
    signUpForm.style.display = "flex";
    signInFormBtn.style.display = "none";
    signUpFormBtn.style.display = "flex";
    signInRightSide.style.display = "none";
    signUpRightSide.style.display = "block";
  });

  switchToSignInBtn.addEventListener("click", function (event) {
    event.preventDefault();
    signInForm.style.display = "flex";
    signUpForm.style.display = "none";
    signInFormBtn.style.display = "flex";
    signUpFormBtn.style.display = "none";
    signInRightSide.style.display = "block";
    signUpRightSide.style.display = "none";
  });
});
