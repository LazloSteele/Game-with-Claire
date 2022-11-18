
from controller import PlayerController

class PlayerContext():
    def __init__(self,game_state,name):
        self._name = name
        self._game_state = game_state

    @property
    def name(self):
        return self._name

class Player(PlayerContext):
    def __init__(self, game_state, name):
        super().__init__(game_state,name)
        self._location = [0, 0]

    def take_turn(self, interpreter):
        pass

    @property
    def location(self):
        return self._location       

    @location.setter
    def location(self, new_location):
        self._location = new_location


class HumanPlayer(Player):
    def __init__(self,game_state,name):
        self._controller = PlayerController(game_state)   # XXX change to human controller when/if migrating
        super().__init__(game_state,name)

    def take_turn(self):
        command = input("What do you do?")
        if command.upper() == 'QUIT':
            return 1
        self._controller.interpret(command)
        return 0

