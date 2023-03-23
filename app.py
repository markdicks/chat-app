"""
This is a simple Flask application that utilizes Flask-SocketIO for real-time communication between the client and server. 
"""

from flask import Flask, render_template
from flask_socketio import SocketIO, send
import webbrowser

app = Flask(__name__)

# Set a secret key for the app
app.config['SECRET'] = "secret!123"

# Initialize the SocketIO instance
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('message')
def handle_message(message):
    """
    Function that handles messages received from the client.

    Parameters:
        message (str): The message received from the client.

    Returns:
        None
    """
    print(f"Received message: {message}")
    if message != "User connected!":
        send(message, broadcast=True)

@app.route('/')
def index():
    """
    Route handler for the root URL.

    Parameters:
        None

    Returns:
        (str) The HTML content to be displayed on the page.
    """
    return render_template("index.html")

if __name__ == '__main__':
    # Open the app in the default web browser
    webbrowser.open('http://20.20.10.120:5000')

    # Start the Flask development server
    socketio.run(app, host="20.20.10.120")
