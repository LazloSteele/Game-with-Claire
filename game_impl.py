
from game_config import GameConfig
from game_state import GameState
from comm_channel import SegregatedOutput

"""
GameImpl defines the interface that all game implementations are expected to have
    Not really neccessary to inherit from at this point
    Not meant to be directly instantiated though not enforced at this point. To enforce:
from abc import ABC
class GameImpl(ABC):
"""

class GameImpl():
    def __init__(self):
        pass

    def run(self):
        pass
    

class GenesisGame():
    def __init__(self):
        SegregatedOutput().startup()
        SegregatedOutput.get().send_message( "Creating GameState")
        self._game_state = GameState()
        pass

    def run(self):
        print('Type "QUIT" at any time to exit the game.')
        self._game_state.current_room() # initial first room, to be removed 
        next_actor = self._game_state.player
        while True:
            result = next_actor.take_turn()     # should return ControlAction::Continue, or ControlAction::Terminate
            if result == 1:
                return result;
        SegregatedOutput.get().shutdown()
        return 0

