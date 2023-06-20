document.getElementById("send-btn").addEventListener("click", function() {
    const userInput = document.getElementById("user-input").value;
    const chatBox = document.getElementById("chat-box");

    // Display user's message
    chatBox.innerHTML += `<div>User: ${userInput}</div>`;

    // Send message to server
    // Changed endpoint to '/api/chat'
    fetch('/api/chat', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify([{role: "user", content: userInput}])
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("HTTP error " + response.status);
        }
        return response.json();
    })
    .then(data => {
        // Display chatbot's response
        // Assuming the server returns the whole response as a string
        const botResponse = data[0].content;  // change here: accessing content of the first response
        chatBox.innerHTML += `<div>Bot: ${botResponse}</div>`;
    })
    .catch(function(error) {
        chatBox.innerHTML += `<div>Error: ${error.message}</div>`;
    });

    // Clear input
    document.getElementById("user-input").value = '';
});
