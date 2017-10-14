import enum


class Position(enum.Enum):
    goalkeeper = 1
    defender = 2
    midfielder = 3
    forward = 4


class Player(object):
    def __init__(self, data):
        self.data = data

    def __getattr__(self, item):
        if item in self.data:
            return self.data[item]

    def __str__(self):
        return '{first_name} {second_name}'.format(**self.data) + " " + str(self.now_cost/10) + " " + self.team
