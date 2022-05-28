import React from 'react';
import Sidepanel from './Sidepanel/Sidepanel';

import WebSocketInstance from '../websocket';


class Chat extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            message: '',
        }

        this.waitForSocketConnection(() => {
            WebSocketInstance.addCallbacks(
                this.setMessages.bind(this),
                this.addMessage.bind(this)
            );

            WebSocketInstance.fetchMessages(this.props.currentUser);
        });
    }

    waitForSocketConnection(callback) {
        const component = this;
        setTimeout(
            function () {
                if (WebSocketInstance.state() === 1) {
                    // console.log("Connection is made");
                    callback();
                    return;
                } else {
                    // console.log("wait for connection...")
                    component.waitForSocketConnection(callback);
                }
            }, 100);
    }

    addMessage(data) {
        this.setState({ messages: [...this.state.messages, data.message] });
    }

    setMessages(event) {
        const messages = event.messages;
        this.setState({ messages: messages });
    }

    messageChangeHandler = (event) => {
        this.setState({ message: event.target.value });
    }

    sendMessageHandler = (e) => {
        e.preventDefault();

        const messageObject = { from: "admin", content: this.state.message };

        WebSocketInstance.newChatMessage(messageObject);
        this.setState({ message: '' });
    }

    renderMessages = (messages) => {
        function formatTimestamp(created_at) {
            const now = new Date();
            const date = new Date(created_at);

            const diff_ms = now.getTime() - date.getTime();

            const days = Math.floor(diff_ms / 86400000);
            const hours = Math.floor((diff_ms % 86400000) / 3600000);
            const minutes = Math.floor(((diff_ms % 86400000) % 3600000) / 60000);
            const seconds = Math.floor((((diff_ms % 86400000) % 3600000) % 60000) / 1000);

            let msg = '';

            if (days > 0) {
                msg += `${days} days`;
                return msg + ' ago';
            }

            if (hours > 0) {
                if (msg) { msg += ', '; }
                msg += `${hours} hours`;
                return msg + ' ago';
            }

            if (minutes > 0) {
                if (msg) { msg += ', '; }
                msg += `${minutes} minutes`;
                return msg + ' ago';
            }

            if (seconds > 0) {
                if (msg) { msg += ', '; }
                msg += `${seconds} seconds`;
                return msg + ' ago';
            }

            return msg + ' ago';
        }

        String.prototype.hashCode = function () {
            var hash = 0, i, chr;
            if (this.length === 0) return hash;
            for (i = 0; i < this.length; i++) {
                chr = this.charCodeAt(i);
                hash = ((hash << 5) - hash) + chr;
                hash |= 0; // Convert to 32bit integer
            }
            return hash;
        };

        const currentUser = "admin";
        return messages.map((message, i) => (
            <li
                key={message.id}
                className={message.author === currentUser ? 'sent' : 'replies'}>
                <img src="http://emilcarlsson.se/assets/mikeross.png" />
                <p>{message.content}
                    <br />
                    <small className={message.author === currentUser ? 'sent' : 'replies'}>
                        {formatTimestamp(message.created_at)}
                    </small>
                </p>
            </li>
        ));
    }

    render() {
        const messages = this.state.messages;
        return (
            <div id="frame">
                <Sidepanel />
                <div className="content">
                    <div className="contact-profile">
                        <img src="http://emilcarlsson.se/assets/harveyspecter.png" alt="" />
                        <p>username</p>
                        <div className="social-media">
                            <i className="fa fa-facebook" aria-hidden="true"></i>
                            <i className="fa fa-twitter" aria-hidden="true"></i>
                            <i className="fa fa-instagram" aria-hidden="true"></i>
                        </div>
                    </div>
                    <div className="messages">
                        <ul id="chat-log">
                            {
                                messages &&
                                this.renderMessages(messages)
                            }
                        </ul>
                    </div>
                    <div className="message-input">
                        <form onSubmit={this.sendMessageHandler}>
                            <div className="wrap">
                                <input
                                    onChange={this.messageChangeHandler}
                                    value={this.state.message}
                                    required
                                    id="chat-message-input"
                                    type="text"
                                    placeholder="Write your message..."
                                />

                                <i className="fa fa-paperclip attachment" aria-hidden="true"></i>

                                <button id="chat-message-submit" className="submit">
                                    <i className="fa fa-paper-plane" aria-hidden="true"></i>
                                </button>
                            </div>

                        </form>
                    </div>
                </div>
            </div>
        );
    };
}

export default Chat;