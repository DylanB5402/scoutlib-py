from flask import Flask
import flask

app = Flask(__name__)

@app.route("/")
def feed():
    return flask.render_template("scout_form.html", title="Scouting Form")

@app.route("/submit", methods=['GET', 'POST'])
def test_submit():
    return flask.request.form