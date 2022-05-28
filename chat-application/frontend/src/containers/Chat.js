import React from 'react';
import Sidepanel from './Sidepanel/Sidepanel';

import WebSocketInstance from '../websocket';


class Chat extends React.Component {
    constructor(props) {
        super(props);
        this.state = {}

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
                    console.log("Connection is made")
                    callback();
                    return;
                } else {
                    console.log("wait for connection...")
                    component.waitForSocketConnection(callback);
                }
            }, 100);
    }

    addMessage(message) {
        this.setState({ messages: [...this.state.messages, message] });
    }

    setMessages(event) {
        const messages = event.messages;
        this.setState({ messages: messages.reverse() });
    }

    messageChangeHandler = (event) => {
        this.setState({
            message: event.target.value
        })
    }

    sendMessageHandler = (e) => {
        e.preventDefault();
        const messageObject = {
            from: "admin",
            content: this.state.message,
        };
        WebSocketInstance.newChatMessage(messageObject);
        this.setState({
            message: ''
        });
    }

    renderMessages = (messages) => {
        const currentUser = "admin";

        function formatTimestamp(timestamp) {
            // Format timestamp to days, hours, minutes ago
            const now = new Date();
            const msg_time = new Date(timestamp);
            const diff = (now.getTime() - msg_time.getTime()) / 1000;

            const days = Math.floor(diff / 86400);
            const hours = Math.floor(diff / 3600);
            const minutes = Math.floor(diff / 60);

            if (days > 0) {
                return days + "days ago";
            }

            if (hours > 0) {
                return `${hours} hours and ${minutes} minutes ago`;
            }

            return `${minutes} minutes ago`;
        }

        return messages.map((message, i) => (
            <li
                key={message.id}
                className={message.author === currentUser ? 'sent' : 'replies'}>
                <img src="http://emilcarlsson.se/assets/mikeross.png" />
                <p>{message.content}
                    <br />
                    <small className={message.author === currentUser ? 'sent' : 'replies'}>
                        { formatTimestamp(message.created_at) }
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
                                    placeholder="Write your message..." />
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