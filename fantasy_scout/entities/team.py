from clint.textui import colored


class Team(object):

    def __init__(self, players):
        assert(len(players) == 15)

        self.players = players

    def __str__(self):
        lines = [str(colored.red('Player'))]
        for player in self.players:
            lines.append(str(player))
        return '\n'.join(lines)
