from describe_room import DescribeRoom
from navigation import Navigation

class Controller():
    def __init__(self, game_state):
        
        self._action = None
        self._target = None
        
        self._possible_actions = {'LOOK': self.look, 'GO': self.move}

        self._game_state = game_state

    def interpret(self, command):
        command = command.upper().split()

        self._action = command[0]
        try:
            self._target = command[1]
        except:
            pass

        self.dispatcher()

    def dispatcher(self):
        try:
            self._possible_actions[self._action](self._target)
        except KeyError:
            self.action_error()

        self._action = None
        self._target = None
        
    def look(self, target):
        sights = self._game_state.current_room().contents

        
        if target == None:
            print(DescribeRoom(self._game_state.current_room()).look())
        else:
            print(f'You look at the {target}...')

    def move(self, target):
        if target == None:
            target = input("Where would you like to go?")
        Navigation(self._game_state).travel(target)
        print(DescribeRoom(self._game_state.current_room()).enter())


    def action_error(self):
        print('I am sorry, that action is not valid')
