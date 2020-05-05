"""
Module for Game
"""
from player import Player, Building
from board import Board, Hex, Port
import card
import random


class Game():

    def __init__(self, num_players):
        self._board = Board()
        self._players = [Player() for n in num_players]
        self._turn = 0
        self._longest_road = [None, 0]
        self._largest_army = [None, 0]
    
    @property
    def curr(self):
        return self._players[self._turn]
    
    def play_turn(self):
        # ask curr to play devcard or roll
        # if inputs play devcard: self.curr.use_devcard(i)
        # if inputs roll:
        roll = self._roll()
        
        if roll == 7:
            for p in self._players:
                amt = sum(p.materials.values())
                if amt > 7:
                    pass
                    # ask p to discard amt // 2 mats
            # some_hex = ask player to pick hex for robber
            self._board.move_robber(some_hex)
        else:
            self._board.harvest(roll)
        
        # loop ask curr to trade or play devcard or build or end turn
        #
        # if inputs trade:
        # trade request, fulfill bank request
        #
        # if inputs play devcard:
        # self.curr.use_devcard(i)
        #
        # if inputs build (some_hex, some_edge or some_corner = clicked loc):
        # self.curr.transact requisite materials
        # some_hex.place(some_edge, some_building)
        #
        # if inputs build devcard:
        # self.curr.transact(["stone", "wool", "wheat"], [1] * 3)
        # self.curr.add_devcard()
        #
        # if inputs end turn:
        self.next_turn()

    def next_turn(self):
        self._turn = (self._turn + 1) % len(self._players)

    def _roll(self):
        return random.randint(1, 6) + random.randint(1, 6)

    def build_road(self):
        pass

    def build_settlement(self):
        pass

    def upgrade_settlement(self):
        pass

    def build_devcard(self):
        pass

    def trade(self):
        pass

    def use_dev_card(self):
        pass
