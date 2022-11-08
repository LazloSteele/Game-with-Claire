import assets
import random
from hemlock import Hemlock
from coral import Coral
from dragon import Dragon
from relic import Relic

class GameObject():
    def __init__(self):
        self._name = NotImplemented
        
        self._suit = NotImplemented
        self._descriptors = NotImplemented
        self._features = NotImplemented

        #self._suit = self.suit_factory(random.choice(assets.Suits))
        self._suit = self.suit_factory( assets.Suits().random_suit() )

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, new_suit):
        self._suit = new_suit

    @staticmethod
    def suit_factory(suit):
        try:
            if suit == "HEMLOCK":
                return Hemlock()
            elif suit == "RELIC":
                return Relic()
            elif suit == "CORAL":
                return Coral()
            elif suit == "DRAGON":
                return Dragon()
            raise AssertionError("Suit is not valid.")
        except AssertionError as e:
            print(e)

    def adjective(self):
        adjectives = list(self._descriptors.intersection(self._suit.descriptors))

        try:
            return random.choice(adjectives)
        except IndexError:
            return "non-descript"
