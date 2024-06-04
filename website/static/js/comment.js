document.addEventListener("DOMContentLoaded", function () {
  const replyBases = document.querySelectorAll(".reply-base");

  replyBases.forEach((replyBase) => {
    replyBase.addEventListener("click", function () {
      const parent = replyBase.closest(".reply-box");
      if (parent) {
        const newReplyBox = parent.querySelector(".new-reply-box");
        if (newReplyBox) {
          if (
            newReplyBox.style.display === "none" ||
            newReplyBox.style.display === ""
          ) {
            newReplyBox.style.display = "flex";
          } else {
            newReplyBox.style.display = "none";
          }
        }
      }
    });
  });
});

document.addEventListener("DOMContentLoaded", function () {
  const repliesBases = document.querySelectorAll(".replies-base");

  repliesBases.forEach((repliesBase) => {
    repliesBase.addEventListener("click", function () {
      const parent = repliesBase.closest(".replies-box");
      if (parent) {
        const allReplies = parent.querySelector(".all-replies");
        if (allReplies) {
          if (
            allReplies.style.display === "none" ||
            allReplies.style.display === ""
          ) {
            allReplies.style.display = "flex";
          } else {
            allReplies.style.display = "none";
          }
        }
      }
    });
  });
});

document.addEventListener("DOMContentLoaded", (event) => {
  document.querySelectorAll(".cancel-btn").forEach((button) => {
    button.addEventListener("click", (e) => {
      e.target.closest(".new-reply-box").style.display = "none";
    });
  });
});
