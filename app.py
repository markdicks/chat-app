from flask import Flask, render_template
from flask_socketio import SocketIO, send
import webbrowser

app = Flask(__name__)
app.config['SECRET'] = "secret!123"
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on('message')
def handle_message(message):
    print(f"Received message: {message}")
    if message != "User connected!":
        send(message, broadcast=True)


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    # Open the app in the default web browser
    webbrowser.open('http://localhost:5000')
    # Start the Flask development server
    socketio.run(app, host="localhost")
