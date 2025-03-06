window.onload = function() {
    console.log("Unity Bridge script loaded.");

    window.Bridge = {
        onUnityButtonClick: function() {
            console.log("Unity Button Clicked! Sending request to Django...");

            fetch("http://127.0.0.1:8000/start/unity-button/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ action: "button_clicked" })
            })
            .then(response => response.json())
            .then(data => console.log("Django Response:", data))
            .catch(error => console.error("Error:", error));
        }
    };

    console.log("window.Bridge is now defined.");
};
