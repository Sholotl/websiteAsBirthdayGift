const startButton = document.getElementById("start-button");
const frontpage = document.getElementById("frontpage");
 
startButton.addEventListener("click", function() {
    frontpage.classList.add("frontpage-opening");
 
    frontpage.addEventListener("transitionend", () => {
        frontpage.style.display = "none";
    }, { once: true });
});
 