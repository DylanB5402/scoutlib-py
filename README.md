For Epischool's Coding for Founders course, I decided to make a sample FRC scouting webapp that can hopefully be expanded on into an end-to-end scouting solution for FRC teams to use

Based off FRC 687's 2020 scouting forms: https://docs.google.com/forms/d/e/1FAIpQLSeTJWROl-exc2Vi0vgaBVz9z6laLctTKCqgzZtgxSTAwS3YDQ/viewform?usp=sf_link

The webapp uses 

Possible future plans:
- Scouting schedule generation
- Ranked data analysis
- TheBlueAlliance integration
- Data validation using TBA
- Tools for Pick list generation (254's Robot tinder?)
- Google Sheets integration

run locally with auto reload on: FLASK_APP=app.py FLASK_ENV=development flask run

workflow notes:
user submits match data for one team's performance in a match -> raw data is stored in raw data table -> analyzed data for that team is re-calculated and stored in analyzed data table