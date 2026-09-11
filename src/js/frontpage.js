const startButton = document.getElementById("start-button");
const frontpage = document.getElementById("frontpage");
const welcomeMessage = document.getElementById("welcome-message");
 
startButton.addEventListener("click", function() {
    frontpage.classList.add("frontpage-opening");
 
    frontpage.addEventListener("transitionend", () => {
        frontpage.style.display = "none";
        welcomeMessage.classList.add("show");
 
        setTimeout(() => {
            welcomeMessage.classList.remove("show");
        }, 5000); // This is the parameter that controls how long it takes for the welcome message to hide Chameeee aflñdksfj
    }, { once: true });
});