"""
Module for Card, MatCard, DevCard, etc.
"""
import player
"""
player.transact("wood", 2)
    --> adds 2 wood to that player's mats
player.transact(["wood", "stone"], [1, -3])
    --> +1 wood, -3 stone for a player. (3:1 port functionality)
"""


__all__ = [
    "Knight",
    "YearOfPlenty",
    "TwoRoads",
    "Monopoly",
    "VPCard",
]
class DevCard(object):
    def __init__(self):
        self._used = False

class Knight(DevCard):
    def __init__(self):
        super().__init__()
        self.description = "Move the robber." \
                           "Steal 1 resource from the owner of a settlement or city" \
                           "adjacent to the robber's new hex"
    def use(self, self, player):
        #Should Game handle move_robber? spec says owner.move_robber
        # move_robber(player, Hex)
        self._used = True

class YearOfPlentyDevCard(DevCard):
    def __init__(self):
        super().__init__()
        self.description = "Take any two resources from the bank. Add them to your hand." \
                           "Can be 2 of the same resource or 2 different resources."
    def use(self, player, mat1, mat2, amt1, amt2):
        player.transact([mat1, mat2], [amt1, amt2])
        self._used = True

class TwoRoads(DevCard):
    def __init__(self):
        self.super().__init__()
        self.description = "Place 2 new roads as if you had just built them."
    def use(self, player):
        #spec says build_road(List[Hex])
        # Game will handle
        # build_road(player, Start, End)
        self._used = True

class Monopoly(DevCard):
    def __init__(self):
        super().__init__()
        self.description = "When you play this card, announce 1 type of resource." \
                           "All players must give you all of their resources of that type."
    def use(self, mat_type_str, player):
        #no sure how we are handling trade
        #??
        player.trade(Other_player, [], mat_type_str, P_amt, O_amt)
        self._used = True

class VPCard(DevCard):
    def __init__(self):
        super().__init__()
        self.description = "1 Victory Point!"
    def use(self, player):
        player.add_vp(1) #do we want to show this? Points from VP cards are hidden until end
        self._used = True
