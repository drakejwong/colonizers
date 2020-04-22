"""
Module for Card, MatCard, DevCard, etc.
"""

class Card:
    def __init__(self, category):
        self.category = category //MatCard or DevCard

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

class YearOfPlentyDevCard):
    def __init__(self, category):
        super().__init__(category)

class TwoRoads(DevCard):
    def __init__(self, category):
        super().__init__(category)

class Monopoly(DevCard):
    def __init__(self, category):
        super().__init__(category)

class VPCard(DevCard):
    def __init__(self, category):
        super().__init__(category)
    def use():
        Player.add_vp(1)