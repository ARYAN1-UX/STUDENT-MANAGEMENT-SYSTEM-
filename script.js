const loginForm = document.getElementById("loginForm");

const emailInput = document.getElementById("email");

const passwordInput = document.getElementById("password");

const roleInput = document.getElementById("role");

const message = document.getElementById("message");


loginForm.addEventListener("submit", function(event) {

    event.preventDefault();

    const email = emailInput.value;

    const password = passwordInput.value;

    const role = roleInput.value;


    if (email === "" || password === "") {

        message.textContent = "Please fill all fields.";

        return;
    }


    message.textContent =
        "Login successful as " + role;

});  