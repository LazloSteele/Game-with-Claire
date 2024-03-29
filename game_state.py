
from game_config import Globals
from player import HumanPlayer
from room import Room

class GameState():
    def __init__(self):
        self._map = {}
        self._player_name = Globals().get().player_name("You")
        self._player = HumanPlayer(self,self._player_name)
        self._season = 'SUMMER'

    @property
    def player(self):
        return self._player

    @property
    def map(self):
        return self._map

    def current_room(self):
        try:
            return self.map[tuple(self._player.location)]
        
        except KeyError:
            self.update_map()

    def new_room(self):
        self.map[tuple(self.player.location)] = Room()

    def update_map(self):
                
        if tuple(self.player.location) not in self.map.keys():
            self.new_room()
