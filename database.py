import sqlite3

class Database:

    def __init__(self, db_file : str):
        self.filename = db_file
        create_raw_data_table = 'CREATE TABLE IF NOT EXISTS raw_scouting_data (data_id INTEGER PRIMARY KEY AUTOINCREMENT, scout_name TEXT, team_number INTEGER, match_number INTEGER, alliance_color TEXT, auto_movement INTEGER, auto_balls_scored INTEGER, auto_balls_missed INTEGER, teleop_balls_scored INTEGER, teleop_balls_missed INTEGER, climb INTEGER, comment TEXT);'
        create_analyzed_data_table = 'CREATE TABLE IF NOT EXISTS analyzed_scouting_data(team_number INTEGER, average_teleop_balls REAL, max_teleop_balls INTEGER, average_auto_balls REAL, max_auto_balls INTEGER, climb_frequency REAL);'
        self.execute_void_query(create_raw_data_table)
        self.execute_void_query(create_analyzed_data_table)

    def execute_void_query(self, query_text, *parameters):
        conn = sqlite3.connect(self.filename)
        cur = conn.cursor()
        cur.execute(query_text, parameters)
        conn.commit()

    def execute_return_query(self, query_text,  *parameters, headers=True):
        conn = sqlite3.connect(self.filename)
        cur = conn.cursor()
        cur.execute(query_text, parameters)

        column_names = []
        for column in cur.description:
            column_names.append(column[0])

        rows = cur.fetchall()
        if (headers):
            dicts = []
            for row in rows:
                d = dict(zip(column_names, row))
                dicts.append(d)
            conn.close()
            return dicts
        else:
            return rows

    def insert_raw_data(self, data):
        query = 'INSERT INTO raw_scouting_data (scout_name, team_number, match_number, alliance_color, auto_movement, auto_balls_scored, auto_balls_missed, teleop_balls_scored, teleop_balls_missed, climb, comment) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);'
        self.execute_void_query(query, data['scout_name'], data['team_num'], data['match_num'], data['alliance_color'], data['auto_movement'], data['auto_balls_scored'], data['auto_balls_missed'], data['teleop_balls_scored'], data['teleop_balls_missed'], data['climbed'], data['comments'])

    def get_raw_data_by_team_anonymous(self, team_number : int):    
        query = 'SELECT match_number, auto_movement, auto_balls_scored, auto_balls_missed, teleop_balls_scored, teleop_balls_missed, climb FROM raw_scouting_data WHERE team_number = ?;'
        return self.execute_return_query(query, team_number, headers=False)

    def get_all_raw_data_anonymous(self):
        query = 'SELECT team_number, match_number, auto_movement, auto_balls_scored, auto_balls_missed, teleop_balls_scored, teleop_balls_missed, climb FROM raw_scouting_data;'
        return self.execute_return_query(query, headers=False)

    def update_analyzed_data(self, team_number : int):
        select_query = 'SELECT AVG(teleop_balls_scored) AS avg_teleop_balls, MAX(teleop_balls_scored) AS max_teleop_balls, AVG(auto_balls_scored) AS avg_auto_balls, MAX(auto_balls_scored) AS max_auto_balls, SUM(climb) AS climb_count, COUNT(*) AS num_matches FROM raw_scouting_data WHERE team_number = ?;'
        analyzed_data = self.execute_return_query(select_query, team_number)[0]
        if (self.execute_return_query(' SELECT COUNT(*) AS count FROM analyzed_scouting_data WHERE team_number=?;', team_number)[0]['count'] != 0):
            update_query = 'UPDATE analyzed_scouting_data SET average_teleop_balls = ?, max_teleop_balls = ?, average_auto_balls = ?, max_auto_balls = ?, climb_frequency = ? WHERE team_number = ?;'
            self.execute_void_query(update_query, analyzed_data['avg_teleop_balls'], analyzed_data['max_teleop_balls'], analyzed_data['avg_auto_balls'], analyzed_data['max_auto_balls'], analyzed_data['climb_count']/analyzed_data['num_matches'], team_number)
        else:
            insert_query = 'INSERT INTO analyzed_scouting_data VALUES (?, ?, ?, ?, ?, ?);'
            self.execute_void_query(insert_query, team_number, analyzed_data['avg_teleop_balls'], analyzed_data['max_teleop_balls'], analyzed_data['avg_auto_balls'], analyzed_data['max_auto_balls'], analyzed_data['climb_count']/1)

    def get_analyzed_data_by_team(self, team_number : int):
        query = 'SELECT * FROM analyzed_scouting_data WHERE team_number = ?;'
        return self.execute_return_query(query, team_number, headers=False)

    def get_all_analyzed_data(self):
        query = 'SELECT * FROM analyzed_scouting_data ORDER BY team_number;'
        return self.execute_return_query(query, headers=False)

    def analyze_all_teams(self):
        for team in self.get_all_team_numbers():
            self.update_analyzed_data(team[0])

    def get_all_team_numbers(self):
        query = 'SELECT DISTINCT team_number FROM raw_scouting_data ORDER BY team_number;'
        return self.execute_return_query(query, headers=False)

    def contains_team_number(self, team_number):
        query = 'SELECT COUNT(*) FROM raw_scouting_data WHERE team_number = ?;'
        return self.execute_return_query(query, team_number, headers=False)[0][0] > 0

db = Database("scouting_data.db")
# print(db.get_all_team_numbers())
# db.analyze_all_teams()
# db.update_analyzed_data(687)
# # db.update_analyzed_data(1323)
# print(db.get_analyzed_data_by_team(687))
print(db.contains_team_number(1323))
print(db.contains_team_number(4201))
