from suit import Suit

class Dragon(Suit):
    def __init__(self):
        self._descriptors = ['rich', 'splendid', 'grand', 'majestic', 'tall', 'sturdy', 'emerald', 'golden', 'wrathful', 'angry', 'intimidating']

    @property
    def descriptors(self):
        return self._descriptors

