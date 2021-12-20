import requests
import auth_token
import json

def get_data(data : str):
    # tba auth token is in an auth_token.py file, which has been gitignored
    header = { 'X-TBA-Auth-Key' : auth_token.token}
    tba_url = "https://www.thebluealliance.com/api/v3"
    response = requests.get(tba_url + data, headers=header)
    tba_data = json.loads(response.content)
    return tba_data

def get_team_image(team_number : int):
    media_data = get_data(f'/team/frc{team_number}/media/2020')
    for data in media_data:
        if (data['direct_url'] != '' and data['type'] == 'imgur'):
            return data['direct_url']
    media_data = get_data(f'/team/frc{team_number}/media/2021')
    for data in media_data:
        if (data['direct_url'] != '' and data['type'] == 'imgur'):
            return data['direct_url']

# print(get_team_image(687))