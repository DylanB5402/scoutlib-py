import sqlite3

class ScoutingDatabase:

    def __init__(self, db_file : str):
        self.filename = db_file
        create_table = 'CREATE TABLE IF NOT EXISTS raw_scouting_data (data_id INTEGER PRIMARY KEY, scout_name TEXT, team_number INTEGER, match_number INTEGER, alliance_color TEXT, auto_movement INTEGER, auto_balls_scored INTEGER, auto_balls_missed INTEGER, teleop_balls_scored INTEGER, teleop_balls_missed INTEGER, climb INTEGER, balance INTEGER, comment TEXT);'
        self.execute_void_query(create_table)

    def execute_void_query(self, query_text, *parameters):
        conn = sqlite3.connect(self.filename)
        cur = conn.cursor()
        cur.execute(query_text, parameters)
        conn.commit()

    def execute_return_query(self, query_text, *parameters):
        conn = sqlite3.connect(self.filename)
        cur = conn.cursor()
        cur.execute(query_text, parameters)

        column_names = []
        for column in cur.description:
            column_names.append(column[0])

        rows = cur.fetchall()
        dicts = []
        for row in rows:
            d = dict(zip(column_names, row))
            dicts.append(d)
        conn.close()
        return dicts

    