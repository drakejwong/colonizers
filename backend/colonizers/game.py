"""
Module for Game
"""
from player import Player, Building
import board
import card
import random


class Game():

    def __init__(self, num_players):
        self._players = [Player() for n in num_players]
        self._turn = 0
        self._longest_road = [None, 0]
        self._largest_army = [None, 0]
    
    @property
    def curr(self):
        return self._players[self._turn]

    def next_turn(self):
        self._turn = (self._turn + 1) % len(self._players)

    def roll():
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        self.harvest(die1 + die2)

    def harvest(self, roll):
        # for all hexes, for all buildings, house.player.transact

    def build_settlement(self):
        pass

    def build_road(self):
        pass

    def build_dev_card(self):
        pass

    def upgrade_settlement(self):
        pass

    def trade(self):
        pass

    def use_dev_card(self):
        pass

    def move_robber(self):
        pass
