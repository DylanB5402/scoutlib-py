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
    db.update_analyzed_data(flask.request.form['team_num'])
    return flask.render_template("submission_success.html", title="Submission Successful!")

@app.route("/team/<int:team>")
def team_view(team : int):
    if (db.contains_team_number(team)):
        title_string = "Team View: " + str(team)
        return flask.render_template("team_view.html", title=title_string, headers=data.raw_match_data_headers_687, raw_match_data = db.get_raw_data_by_team_anonymous(team), highlights=db.get_analyzed_data_highlights(team)[0], robot_image=db.get_team_image(team))
    else:
         return flask.render_template("base.html", title=f"Data for Team #{team} is not available")

@app.route("/data/analyzed")
def analyzed_data():
    return flask.render_template("tabular_data_view.html", title="Analyzed Data", headers=data.analyzed_data_headers, rows=db.get_all_analyzed_data())
    
@app.route("/data/raw")
def raw_data():
    return flask.render_template("tabular_data_view.html", title="Raw Data", headers=data.raw_match_data_headers, rows=db.get_all_raw_data_anonymous())

@app.route("/graphs")
def graphs():
    return flask.render_template("graphs.html", title="Data Graphs")

@app.route("/api/analyzed/auto")
def auto_averages():
    return db_data_to_json(db.get_analyzed_auto_averages())

@app.route("/api/analyzed/teleop")
def teleop_averages():
    return db_data_to_json(db.get_analyzed_teleop_averages())

@app.route("/api/analyzed/climb")
def climb_frequencies():
    return db_data_to_json(db.get_analyzed_climb_frequencies())

# graph data specification: {'x_labels' : [label1, label2, ...], 'y_data' : [10, 20, 30, ...]}
def db_data_to_json(data):
    x_labels = []
    y_data = []
    for (team_number, value) in data:
        x_labels.append(team_number)
        y_data.append(value)
    return { 'x_labels' : x_labels,  'y_data' : y_data}
