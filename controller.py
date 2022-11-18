from describe_room import DescribeRoom
from navigation import Navigation

class Controller():
    def __init__(self, game_state):
        self._possible_actions = {'LOOK': self.look, 'GO': self.move}
        self._game_state = game_state

    def interpret(self, command):
        command = command.upper().split()
        action = command[0]
        target = command[1] if len(command)>1 else None
#        try:
#            target = command[1]
#        except:
#            target = None
        self.dispatcher(action,target)

    def dispatcher(self,action,target):
        try:
            self._possible_actions[action](target)
        except KeyError:
            self.action_error(action)

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


    def action_error(self,action):
        print(f'I am sorry, "{action}" is not valid')


# XXX just a proxy for Controller, first step in migrating to subclass
class PlayerController(Controller):
    def __init__(self, game_state):
        super().__init__(game_state)


