# scoutlib-py

## Context: 

During high school I did competitive robotics in the [FIRST Robotics Competition](https://www.firstinspires.org/robotics/frc). During the playoffs of a tournament, each of the top 8 teams selects 2 other teams to play alongside them. Teams "scout" robots to gather quantitative data on robot performance to determine which teams to pick for the playoffs. As a senior in high school, I wrote a scouting system that used a Python script to automate analysis of data submitted via Google Forms/Sheets. This is meant to fulfill a similar role, except built as a web application.

## User stories:

- Users should be able to submit a variety of quantitative and qualitative scouting data to the server.
    - Users should view a confirmation screen after submitting data that allows them to submit scouting data again
    - Should be able to return to scouting form from any page
- Users should be able to view the data (analyzed and raw) of each team scouted individually
    - Page should be accessible from a list of teams
        - List of teams should be accessible from home page
- Users should be able to view a selection of analyzed data for the entire event
    - Page should be accessible from home page

## Views:

- Scouting Form 
- Individual Team Data
- Entire Event Analyzed Data
- Raw Data 
- List of teams
