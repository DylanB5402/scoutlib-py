from flask import Flask
import flask

import data
import database

app = Flask(__name__)
db = database.Database("scouting_data.db")

@app.route("/")
def feed():
    return flask.render_template("scout_form.html", title="Scouting Form")

@app.route("/submit", methods=['POST'])
def test_submit():
    db.insert_raw_data(flask.request.form)
    return flask.render_template("submission_success.html", title="Submission Successful!")

@app.route("/team/<int:team>")
def team_view(team : int):
    title_string = "Team View: " + str(team)
    return flask.render_template("team_view.html", title=title_string, headers=data.raw_match_data_headers_687, raw_match_data = db.get_raw_data_by_team_anonymous(687), highlights=data.analyzed_data_team_highlights)

@app.route("/data/analyzed")
def analyzed_data():
    return flask.render_template("tabular_data_view.html", title="Analyzed Data", headers=data.analyzed_data_headers, rows=data.analyzed_data)

@app.route("/data/ranked")
def ranked_data():
    return flask.render_template("tabular_data_view.html", title="Ranked Data", headers=data.ranked_data_headers, rows=data.ranked_data)

@app.route("/data/raw")
def raw_data():
    return flask.render_template("tabular_data_view.html", title="Raw Data", headers=data.raw_match_data_headers, rows=db.get_all_raw_data_anonymous())