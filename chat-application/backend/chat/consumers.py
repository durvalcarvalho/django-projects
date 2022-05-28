import json

from django.contrib.auth.models import User

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from chat.models import Message


class ChatConsumer(WebsocketConsumer):

    def fetch_messages(self, data):
        messages = Message.objects.last_10_messages()

        content = {
            'command': 'messages',
            'messages': [message.to_json() for message in messages]
        }
        self.send_message(content)

    def new_message(self, data):
        author = User.objects.filter(username=data['from']).first()
        message = Message.objects.create(author=author, content=data['message'])
        content = { 'command': 'new_message', 'message': message.to_json()}
        self.send_chat_message(content)

    commads = {
        'fetch_messages': fetch_messages,
        'new_message': new_message,
    }

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        data = json.loads(text_data)
        command_name = data['command']
        self.commads[command_name](self, data)

    def send_chat_message(self, message):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def send_message(self, data):
        self.send(text_data=json.dumps(data))

    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({**message}))
