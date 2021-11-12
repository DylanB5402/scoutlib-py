from flask import Flask
import flask

app = Flask(__name__)

@app.route("/")
def feed():
    return flask.render_template("home.html")
