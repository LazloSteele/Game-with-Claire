
from game_config import GameConfig
from game_state import GameState
from controller import Controller


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
        self._game_state = GameState()
        self._controller = Controller(self._game_state)
        pass

    def run(self):
        playing = True

        print('Type "QUIT" at any time to exit the game.')
        self._game_state.current_room()
        self._controller.look(None)
        while playing == True:
            command = input("What do you do?")
            if command.upper() == 'QUIT':
                return 1
            self._controller.interpret(command)

        return 0

