from flask import Flask
import flask

import data

app = Flask(__name__)

@app.route("/")
def feed():
    return flask.render_template("scout_form.html", title="Scouting Form")

@app.route("/submit", methods=['GET', 'POST'])
def test_submit():
    return flask.request.form

@app.route("/team/<int:team>")
def team_view(team : int):
    title_string = "Team View: " + str(team)
    return flask.render_template("team_view.html", title=title_string, headers=data.raw_match_data_headers, raw_match_data = data.raw_match_data, highlights=data.analyzed_data_highlights)