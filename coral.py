from suit import Suit

class Coral(Suit):
    def __init__(self):
        self._descriptors = ['craggy', 'bright', 'friendly', 'cheerful', 'orange', 'lively', 'rough', 'jagged', 'loud', 'soft', 'delicate']

    @property
    def descriptors(self):
        return self._descriptors

