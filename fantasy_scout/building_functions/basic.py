import math
from collections import defaultdict

from fantasy_scout.entities.player import Position
import itertools

from fantasy_scout.entities.team import Team
from clint.textui import progress


def basic_build(players_by_score: list):
    # pick captain (highest overall score in list)

    # pick the best n for each position to get a team that respects positions but not cost or irl teams
    selected_players = defaultdict(list)
    for player in players_by_score:
        if len(selected_players[player.position]) < Team.VALID_POSITION_COUNTS[player.position]:
            selected_players[player.position].append(player)
        if Team.correct_position_counts([p for position_list in selected_players.values() for p in position_list]):
            break
    """
    # while team cost > 100
        # pick the best one in the lineup to trade
        # pick the best one in the rest of the cheaper options to trade

    # pick some garbage destined for the bench (cheapest goalkeeper, defender, midfielder)
    cheapest_in_position = {
        Position.goalkeeper: None,
        Position.defender: None,
        Position.midfielder: None
    }
    players_by_cost = sorted(players_by_score, key=lambda p: p.now_cost, reverse=True)
    for player in players_by_cost:
        if player.position != Position.forward and cheapest_in_position[player.position] is None:
            cheapest_in_position[player.position] = player
        if all(cheapest_in_position.values()):
            break
    for picked_player in cheapest_in_position.values():
        players_by_score.remove(picked_player)
        players_by_cost.remove(picked_player)

    # pick an EV goalie and defender, brings down remaining brute force to 9!

    players_by_cost_effectiveness = sorted(players_by_score, key=lambda p: p.ranking_score / p.now_cost)
    ev_goalie = next(p for p in players_by_cost_effectiveness if p.position == Position.goalkeeper)
    ev_defender = next(p for p in players_by_cost_effectiveness if p.position == Position.defender)

    players_by_score = [p for p in players_by_score if p.position != Position.goalkeeper]
    players_by_score.remove(ev_defender)

    remaining_player_combos = []
    with progress.Bar(label="Crunching Team Combos: ", expected_size=math.factorial(9)) as bar:
        count = 0
        for remaining_player_combo in itertools.combinations(players_by_score, 9):
            count += 1
            bar.show(count)
            combo_score = sum([p.ranking_score for p in remaining_player_combo])
            combo_cost = sum([p.now_cost for p in remaining_player_combo])
            remaining_player_combos.append((remaining_player_combo, combo_score, combo_cost))

    remaining_player_combos.sort(key=lambda combo: combo[1])

    for remaining_player_combo in remaining_player_combos:
        full_team = remaining_player_combo + [captain, ev_defender, ev_goalie] + list(cheapest_in_position.values())
        if Team.team_cost_within_bounds(full_team) \
                and Team.correct_position_counts(full_team)\
                and Team.correct_team_counts(full_team):
            break
    else:
        raise Exception("Didn't find any valid teams")"""

    return [p for position_list in selected_players.values() for p in position_list]
