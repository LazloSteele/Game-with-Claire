from suit import Suit

class Relic(Suit):
    def __init__(self):
        self._descriptors = ['steep', 'winding', 'ancient', 'mysterious', 'grey', 'rusted', 'broken', 'layered', 'crumbling', 'cracking', 'burnt']

    @property
    def descriptors(self):
        return self._descriptors

