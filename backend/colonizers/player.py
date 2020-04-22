"""
Module for Player, Building, etc.
"""
import card

class Player:

    def __init__(materials):
        self._materials = {'wood': 0, 'sheep': 0, 'brick': 0, 'ore': 0, 'wheat': 0}
        self._buildings: {'roads': 0, 'settlements': 0, 'cities': 0}
        self._devcards = []
        self._color = None

    def change_mats(mats, ct):
        # Takes in list of materials and corresponding list of counts and changes player's materials
        self._materials[m] += ct for m in mats