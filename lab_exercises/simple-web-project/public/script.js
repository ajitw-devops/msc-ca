document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault();

    let formData = new FormData(this);
    fetch("/login", {
        method: "POST",
        body: new URLSearchParams(formData)
    })
    .then(response => response.text())
    .then(data => {
        document.getElementById("message").textContent = data;
    })
    .catch(error => console.error("Error:", error));
});
