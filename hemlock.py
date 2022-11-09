from suit import Suit
from game_config import GameConfig

class Hemlock(Suit):
    def __init__(self):
        self._descriptors = GameConfig().get_suit_descriptor("HEMLOCK")
        #print( self._descriptors )
        #self._descriptors = ['treacherous', 'poisonous', 'wicked', 'thick', 'dense', 'homogenous', 'crowded', 'sickly', 'mournful', 'deadly', 'deceitful']

    @property
    def descriptors(self):
        return self._descriptors
