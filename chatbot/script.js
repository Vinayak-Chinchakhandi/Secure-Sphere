// script.js
document.getElementById('sendButton').addEventListener('click', () => {
    const userInput = document.getElementById('userInput').value;
    if (!userInput.trim()) return;

    displayUserMessage(userInput);
    document.getElementById('userInput').value = '';

    document.getElementById('loading').style.display = 'block';
    document.getElementById('loadingMessage').textContent = 'Processing...';

    fetch('http://127.0.0.1:5000/cyber_assist', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userInput }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        document.getElementById('loading').style.display = 'none';

        if (data.result) {
            displayAIMessage(data.result);
        } else if (data.error) {
            let errorMessage = "An unknown error occurred.";
            if (data.error.includes("API key")) {
                errorMessage = "API Key Invalid. Please check your API key.";
            } else if (data.error.includes("timeout")) {
                errorMessage = "Connection Timeout. Please check your internet connection.";
            }
            displayAIMessage(`Error: ${errorMessage}`);
        }
    })
    .catch(error => {
        document.getElementById('loading').style.display = 'none';
        displayAIMessage(`Network Error: ${error.message}`);
    });
});

function displayUserMessage(message) {
    const chatMessages = document.getElementById('chat-messages');
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', 'user-message');
    messageDiv.textContent = message;
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function displayAIMessage(message) {
    const chatMessages = document.getElementById('chat-messages');
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', 'ai-message');
    message = message.replace(/\*\*(.*?)\*\*/g, '<b>$1</b>');
    message = message.replace(/\*(.*?)\*/g, '<i>$1</i>');
    message = message.replace(/`(.*?)`/g, '<code class="inline-code">$1</code>');
    message = message.replace(/```([\s\S]*?)```/g, '<pre><code class="block-code">$1</code></pre>');
    messageDiv.innerHTML = message;
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}