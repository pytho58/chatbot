async function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    const chatbox = document.getElementById("chatbox");

    if (userInput.trim() !== "") {
        // Show user message
        chatbox.innerHTML += `<div class="message user-message"><strong>You:</strong> ${userInput}</div>`;

        // Show 'Bot is typing...'
        const typingMessage = document.createElement('div');
        typingMessage.className = "message bot-message typing";
        typingMessage.innerHTML = "<em>Bot is typing...</em>";
        chatbox.appendChild(typingMessage);
        chatbox.scrollTop = chatbox.scrollHeight;

        // Send message to Flask
        const response = await fetch('/get', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: userInput })
        });

        const data = await response.json();

        // Remove 'Bot is typing...'
        typingMessage.remove();

        // Show bot reply
        chatbox.innerHTML += `<div class="message bot-message"><strong>Bot:</strong> ${data.reply}</div>`;
        chatbox.scrollTop = chatbox.scrollHeight;

        // Clear input box
        document.getElementById("user-input").value = "";
    }
}