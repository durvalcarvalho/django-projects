const http = require('http');
const socketio = require('socket.io');

const server = http.createServer();
const io = socketio(server, {
    cors: {
        origin: '*',
        methods: ['GET', 'POST'],
    }
});

const room = 'testRoom';

io.on('connection', socket => {
    console.log('user connected');

    socket.join(room);

    // io.to(room).emit('welcome', 'Welcome to the room');

    socket.broadcast.emit('welcome', 'Another user has joined the room');

    // socket.on('disconnect', () => {
    //     console.log('user disconnected');
    // });
    // socket.on('chat message', (msg) => {
    //     console.log('message: ' + msg);
    //     io.emit('chat message', msg);
    // });


    socket.on('chat message', msg => {
        console.log('message: ' + msg);
        io.to(room).emit('chat message', msg);
    });

    socket.on('disconnect', () => {
        console.log('user disconnected');
        io.to(room).emit('user disconnected', 'An user has left the room');
    });

});

server.listen(8080, () => { console.log('listening on port 127.0.0.1:8080') });
