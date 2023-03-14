from flask import Flask
import webbrowser

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

if __name__ == '__main__':
    # Open the app in the default web browser
    webbrowser.open('http://localhost:5000')
    
    # Start the Flask development server
    app.run(debug=True)
