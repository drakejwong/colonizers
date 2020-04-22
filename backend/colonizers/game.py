"""
Module for Game
"""
import player, board, card
import random
from collections import OrderedDict

class Game():

    def __init__(self, num_players):
        self._players = [player.Player() for n in num_players]
        self._winner = None
        self._current_turn = 0
        self._longest_road = (None, 0)
        self._largest_army = (None, 0)

    def next_turn():
        # Updates turn 
        self._current_turn = (self._current_turn + 1) % len(self._players)
    
    def roll():
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        self._curr_roll = die1 + die2
        self.harvest()

    def harvest():
        pass

    def build_settlement():
        pass

    def build_road():
        pass

    def build_dev_card():
        pass

    def upgrade_settlement():
        pass

    def trade():
        pass

    def use_dev_card():
        pass

    def move_robber():
        pass
    
