'''

CURRENTLY: trying to make this assets list turn into objects

ALSO: Need to tie the description engine into actual objects too

'''

from game_config import GameConfig
import random

#Suits = ['HEMLOCK', 'DRAGON', 'CORAL', 'RELIC']
class Suits(): 
    def __init__(self):
        self._suits = GameConfig().get_suits()

    def random_suit(self):
        return random.choice(self._suits)

Trees = ['ELM']
#'ASPEN', 'OAK', 'MAPLE', 'PINE', 'SPRUCE', 'ASH', 'CEDAR', 'APPLE', 'PEAR', 'PLUM', 'CHERRY']

Plants = [Trees]

