from player import Player
from controller import Controller
from game_state import GameState
from game_config import GameConfig
import argparse

class Game():
    def __init__(self):
        self._cmdline_args = self.process_cmdline()
        print( 'Cmdline Args:', self._cmdline_args)
        print( self._cmdline_args.config_path)
        self._player = Player()
        self._game_state = GameState(self._player)
    
        self._controller = Controller(self._game_state)

        self._current_room = self._game_state.current_room()

        self.main()

    def process_cmdline(self):
        parser = argparse.ArgumentParser(
            description='Ways to change the game.',
            epilog='We await your decision.'
        )
        parser.add_argument(
            '--config_path', 
            default='.\Config', 
            metavar='GameConfigFolder',
            help='Path to the game_name .json config'
        )
        parser.add_argument(
            '--game_name', 
            default='Default' ,
            metavar='GameConfig',
            help='Name of the game, assumed a .json filename'
        )
        parser.add_argument(
            '--player_name', 
            default='Guest',
            help='Your name -- pending implementation'
            )
        return parser.parse_args()

    def main(self):
        playing = True

        print('Type "QUIT" at any time to exit the game.')
        self._controller.look(None)
        
        while playing == True:
        
            command = input("What do you do?")

            if command.upper() == 'QUIT':
                playing == False
                return

            self._controller.interpret(command)
            
if __name__ == "__main__":
    game = Game()


