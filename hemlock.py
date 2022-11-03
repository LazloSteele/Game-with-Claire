from suit import Suit

class Hemlock(Suit):
    def __init__(self):
        self._descriptors = ['treacherous', 'poisonous', 'wicked', 'thick', 'dense', 'homogenous', 'crowded', 'sickly', 'mournful', 'deadly', 'deceitful']

    @property
    def descriptors(self):
        return self._descriptors
