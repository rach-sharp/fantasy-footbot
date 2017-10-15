import requests
import json


def update_position_data(position_data):
    with open("local_data/positions.json", "w") as positions_file:
        json.dump(position_data, positions_file, indent=2)


def update_player_data(player_data):

    for player in player_data:
        player_response = requests.get("https://fantasy.premierleague.com/drf".format(**player))
        # history - summary of performance for current season
        # explain - explaining where points have come from(?)
        player_full_data = player_response.json()
        player['history'] = player_full_data['history']
        player['history_past'] = player_full_data['history_past']
        with open("local_data/players/{second_name}, {first_name}".format(**player), "w") as player_file:
            json.dump(player, player_file, indent=2)


def update_team_data(team_data):
    for team in team_data:
        with open("local_data/teams/{name}.json".format(**team), "w") as team_file:
            json.dump(team, team_file, indent=2)


response = requests.get("https://fantasy.premierleague.com/drf/bootstrap-static")
print(response)
fpl_raw_data = response.json()
print(fpl_raw_data.keys())
print(fpl_raw_data['teams'][0])

# update_player_data(fpl_raw_data['elements'])
# update_position_data(fpl_raw_data['element_types'])
# update_team_data(fpl_raw_data['teams'])

