import random
from game_object import GameObject

class Plant(GameObject):
    def __init__(self):
        super().__init__()
        
        self._growth_habit = NotImplemented
        self._water_requirement = NotImplemented
        self._cold_hardiness = NotImplemented
        self._seasons = NotImplemented

    def clumping(self):
        pass

    def scandent(self):
        pass

    def prostrate(self):
        pass

    def erect(self):
        pass
