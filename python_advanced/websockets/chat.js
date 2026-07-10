const socket = new WebSocket("ws://127.0.0.1:8000/ws");
const messagesDiv = document.getElementById("messages");
const messageInput = document.getElementById("messageInput");
const sendButton = document.getElementById("sendButton");

socket.onmessage = (event) => {
    const newMessage = document.createElement("div");
    newMessage.textContent = "Reçu : " + event.data;
    newMessage.className = "message received";
    messagesDiv.appendChild(newMessage);

    messagesDiv.scrollTop = messagesDiv.scrollHeight;
};

function sendMessage() {
    const message = messageInput.value.trim();
    if (message !== "") {
        socket.send(message);

        const sentMessage = document.createElement("div");
        sentMessage.textContent = "Envoyé : " + message;
        sentMessage.className = "message sent";
        messagesDiv.appendChild(sentMessage);
        messageInput.value = "";
    }
}

sendButton.addEventListener("click", sendMessage);

messageInput.addEventListener("keypress", (event) => {
    if (event.key === "Enter") {
        sendMessage();
    }
});
