"""
Module for Player, Building, etc.
"""
import card


class Player():

    def __init__(self, color):
        self._materials = {"wood": 0, "sheep": 0,
                           "brick": 0, "ore": 0, "wheat": 0}
        self._devcards = dict(zip(__all__, [0] * len(__all__)))
        self._color = color

    @property
    def materials(self):
        return self._materials

    def transact(self, mat, amt):
        """
        Add/subtract according amt(s) of mat(s)
        """
        if isinstance(mats, list):
            for m, a in zip(mat, amt)
            self._materials[m] += a
        else:
            self._materials[mat] += amt

    @property
    def devcards(self):
        return self._devcards

    def add_devcard(self, card):
        self._devcards[card.__name__] += 1

    def use_devcard(self, card):
        assert(self_devcards[card.__name__] - 1 >= 0)
        self._devcards[card.__name__] -= 1

    @property
    def color(self):
        return self._color


class Building():

    def __init__(self, player):
        self._owner = player

    @property
    def color(self):
        return self._owner.color
