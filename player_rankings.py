import os
import json

TOTAL_SEASON_WEEKS = 38
CURRENT_SEASON_WEEK = 1

team_lookup = {}
for directory, _, files in os.walk("local_data/teams"):
    for team_file_path in files:
        with open(os.path.join(directory, team_file_path), "r") as player_file:
            team_json = json.load(player_file)
            team_lookup[team_json["id"]] = team_json["name"]

position_lookup = {1: "Goalkeeper", 2: "Defender", 3: "Midfielder", 4: "Forward"}


def last_season_data(historical_data):
    last_season_list = [h for h in historical_data if h["season_name"] == "2016/17"]
    if len(last_season_list) == 1:
        return last_season_list[0]
    else:
        return None


def this_season_data(current_data):
    total_score = 0
    for game in current_data:
        total_score = total_score + game["total_score"]
    current_data["total_points"] = total_score
    return current_data


def compute_r_rating(player_data):
    if player_data["status"] == "s" or player_data["status"] == "i" or player_data["status"] == "d":
        return 0.0
    last_season = last_season_data(player_data['history_past'])
    # this_season = this_season_data(player_data['history'])
    if last_season:
        if last_season["minutes"] > 2500:
            player_data["last_season_points"] = last_season["total_points"]
            return (last_season["total_points"] / (last_season["minutes"] / 90)) / (player_data["now_cost"] / 10)
        else:
            return 0.0
    else:
        return 0.0


players = []
for directory, _f, files in os.walk("local_data/players"):
    for player_file_path in files:
        with open(os.path.join(directory, player_file_path), "r") as player_file:
            players.append(json.load(player_file))

print(len(players))

for player in players:
    player["rach_rating"] = compute_r_rating(player)

players.sort(key=lambda p: p["rach_rating"], reverse=True)

goalkeepers = []  # id = 1
defenders = []  # id = 2
midfielders = []  # id = 3
forwards = []  # id = 4

for p in players:
    if p["element_type"] == 1:
        goalkeepers.append(p)
    elif p["element_type"] == 2:
        defenders.append(p)
    elif p["element_type"] == 3:
        midfielders.append(p)
    elif p["element_type"] == 4:
        forwards.append(p)

squad = []
squad.extend(goalkeepers[:2])
squad.extend(defenders[:5])
squad.extend(midfielders[:5])
squad.extend(forwards[:3])

random_squad_ids = [375, 2, 101, 377, 7, 380, 103, 274, 207, 373, 232, 106, 134, 160, 209]
random_squad = []
for p in players:
    if p["id"] in random_squad_ids:
        random_squad.append(p)
print(len(random_squad))

"""
for p in squad:
    print("{first_name} {second_name}, {rach_rating}".format(**p))
    print("Will cost {now_cost} and has scored {total_points} so far this season".format(**p))
    print("Plays for {0}".format(team_lookup[p["team"]]))
    print("Position: {0}".format(position_lookup[p["element_type"]]))
"""

for p in squad:
    print("{0} {1}, {2} for {3} : {4}".format(p["first_name"], p["second_name"],
                                              position_lookup[p["element_type"]], team_lookup[p["team"]],
                                              p["now_cost"]/10))

print("")
# compute total cost of the team

total_cost = 0
for p in squad:
    total_cost = total_cost + p["now_cost"]
print("Total Cost for team: {0} million".format(total_cost / 10))

# compute counts for each real team and print a warning message if over limit
team_counts = {}
expected_overall_points = 0
players_missing_data = 0
for p in squad:
    if "last_season_points" in p:
        expected_overall_points = expected_overall_points + p["last_season_points"]
    else:
        players_missing_data = players_missing_data + 1
    if p["team"] not in team_counts:
        team_counts[p["team"]] = 1
    else:
        team_counts[p["team"]] = team_counts[p["team"]] + 1
print("Expected total points over the season: {0}".format(
    expected_overall_points * (15 / (15 - players_missing_data)) * 11 / 15))

team_size_ok = True
for team in team_counts:
    if team_counts[team] > 3:
        team_size_ok = False
        print("TOO MANY FOR TEAM: {0}".format(team_lookup[team]))
if team_size_ok:
    print("Fantasy team within real-life team size limits")
