async function send() {

    const message = document.getElementById("query").value;

    const response = await fetch("/chat", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            message: message
        })
    });

    const data = await response.json();

    document.getElementById("response").textContent =
        JSON.stringify(data, null, 2);
}