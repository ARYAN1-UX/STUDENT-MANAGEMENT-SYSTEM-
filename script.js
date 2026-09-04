const loginForm = document.getElementById("loginForm");

const emailInput = document.getElementById("email");
const passwordInput = document.getElementById("password");
const roleInput = document.getElementById("role");
const message = document.getElementById("message");


loginForm.addEventListener("submit", async function(event) {

    event.preventDefault();

    const email = emailInput.value;
    const password = passwordInput.value;
    const role = roleInput.value;


    if (email === "" || password === "") {

        message.textContent = "Please fill all fields.";

        return;
    }


    try {

        const response = await fetch(
            "http://127.0.0.1:5000/login",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    email: email,
                    password: password,
                    role: role
                })
            }
        );


        const data = await response.json();


        message.textContent = data.message;


        if (data.success) {

            console.log("Login successful");

        }

    }

    catch (error) {

        message.textContent =
            "Unable to connect to backend.";

        console.error(error);

    }

});