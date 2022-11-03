import random


class GameObject():
    def __init__(self):
        self._name = NotImplemented
        
        self._suit = SuitFactory(random.choice(['HEMLOCK', 'DRAGON', 'CORAL', 'RELIC']))
        self._descriptors = NotImplemented
        self._features = NotImplemented

        print(self._suit)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    def adjective(self):
        adjectives = list(self._descriptors.intersection(self._suit.descriptors))

        return random.choice(adjectives)
