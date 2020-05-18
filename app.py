from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    headline = 'Hello World!'
    return render_template("index.html", headline=headline)

@app.route('/login')
def login():
    headline = 'Successfully login!'
    return render_template("index.html", headline=headline)

@app.route('/home')
def home():
    headline = 'Coming soon!'
    return render_template("home.html", headline=headline)
