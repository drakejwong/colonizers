"""
Module for Player, Building, etc.
"""
import card


class Player:

    def __init__(self, color):
        self._materials = {"wood": 0, "sheep": 0,
                           "brick": 0, "ore": 0, "wheat": 0}
        self._devcards = []
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
