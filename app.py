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
    return flask.render_template("team_view.html", title=title_string, headers=data.raw_match_data_headers_687, raw_match_data = data.raw_match_data_687, highlights=data.analyzed_data_team_highlights)

@app.route("/data/analyzed")
def analyzed_data():
    return flask.render_template("tabular_data_view.html", title="Analyzed Data", headers=data.analyzed_data_headers, rows=data.analyzed_data)

@app.route("/data/ranked")
def ranked_data():
    return flask.render_template("tabular_data_view.html", title="Ranked Data", headers=data.ranked_data_headers, rows=data.ranked_data)

@app.route("/data/raw")
def raw_data():
    return flask.render_template("tabular_data_view.html", title="Raw Data", headers=data.raw_match_data_headers, rows=data.raw_match_data)