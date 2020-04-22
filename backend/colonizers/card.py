"""
Module for Card, MatCard, DevCard, etc.
"""
//do I need to import the other modules?
//made the use() method for dev cards have Player as a param

import player

__all__ = [
    "Knight",
    "YearOfPlenty",
    "TwoRoads",
    "Monopoly",
    "VPCard",
]


class Card:
    def __init__(self, category):
        self.category = category // MatCard or DevCard


class MatCard(Card):
    def __init__(self, category, material):
        super().__init__(category)
        self.material = material

class DevCard(Card):
    def __init__(self, category):
        super().__init__(category)
        _used = False

class Knight(DevCard):
    def __init__(self, category):
        super().__init__(category)
    def use(Player):
        //Should Game handle move_robber? spec says owner.move_robber
        move_robber(Player, Hex)
        _used = True

class YearOfPlentyDevCard):
    def __init__(self, category):
        super().__init__(category)
    def use(Player, mat1, mat2):
        Player.materials[mat1] += 1
        Player.materials[mat2] += 2
        _used = True

class TwoRoads(DevCard):
    def __init__(self, category):
        super().__init__(category)
    def use(Player):
        //spec says build_road(List[Hex])
        build_road(Player, Start, End)
        _used = True

class Monopoly(DevCard):
    def __init__(self, category):
        super().__init__(category)
    def use(mat_type_str, Player):
        //no sure how we are handling trade
        //??
        Player.trade(Other_player, P_input, O_input, P_amt, O_amt)
        _used = True

class VPCard(DevCard):
    def __init__(self, category):
        super().__init__(category)
    def use(Player):
        Player.add_vp(1) //do we want to show this? Points from VP cards are hidden until end
        _used = True
