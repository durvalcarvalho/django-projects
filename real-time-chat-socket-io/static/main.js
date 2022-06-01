const alertBox = document.getElementById('alert-box');
const messagesBox = document.getElementById('messages-box');
const messageInput = document.getElementById('message-input');
const sendBtn = document.getElementById('send-btn');


const handleAlerts = (msg, type) => {
    alertBox.innerHTML = `
        <div class="alert alert-${type} alert-dismissible fade show" role="alert">
            <strong>${msg}</strong>
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
    `;
    setTimeout(() => { alertBox.innerHTML = ''; }, 5000);
};

const socket = io('http://localhost:8080/');

socket.on('welcome', msg=> {
    console.log(msg);

    handleAlerts(msg, 'primary');
});

socket.on('chat message', msg => {
    messagesBox.innerHTML += `
        <div class="message">
            <div class="message-text">${msg}</div>
        </div>
    `;
});

socket.on('user disconnected', msg => {
    console.log(msg);
    handleAlerts(msg, 'danger');
});


function sendMessage() {
    const msg = messageInput.value;
    socket.emit('chat message', msg);
    messageInput.value = '';
}

sendBtn.addEventListener('click', () => { sendMessage(); });


// If enter is pressed, send message
messageInput.addEventListener('keypress', e => {
    if (e.key === 'Enter') {
        sendMessage();
    }
});