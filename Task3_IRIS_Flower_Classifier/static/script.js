// static/script.js
document.getElementById("irisForm").addEventListener("submit", function (event) {
    const fields = ["sepal_length", "sepal_width", "petal_length", "petal_width"];
    let valid = true;

    fields.forEach(field => {
        const input = document.getElementById(field);
        const error = document.getElementById("error_" + field);
        const value = input.value.trim();

        error.style.display = "none";
        error.innerText = "";

        if (value === "") {
            error.innerText = "This field is required.";
            error.style.display = "block";
            valid = false;
        } else if (isNaN(value) || Number(value) <= 0) {
            error.innerText = "Please enter a valid positive number.";
            error.style.display = "block";
            valid = false;
        }
    });

    if (!valid) {
        event.preventDefault();
    }
});
