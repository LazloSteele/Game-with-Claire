
from game_config import GlobalsConfigLoader,GameConfigLoader
from game_impl import GenesisGame
import argparse

class Game():
    def __init__(self):
        cmdline_args = self.process_cmdline()
        GlobalsConfigLoader(vars(cmdline_args))
        GameConfigLoader().load_game_config(cmdline_args.game_name,cmdline_args.config_path)
        self.main()

    def process_cmdline(self):
        parser = argparse.ArgumentParser(
            description='Ways to change the game.',
            epilog='We await your decision.'
        )
        parser.add_argument(
            '--config_path', 
            default='Config', 
            metavar='GameConfigFolder',
            help='Path to the game_name .json config'
        )
        parser.add_argument(
            '--game_name', 
            default='Genesis' ,
            metavar='GameConfig',
            help='Name of the game, assumed a .json filename'
        )
        parser.add_argument(
            '--player_name', 
            default='Guest',
            help='Your name -- pending implementation'
            )
        parser.add_argument(
            '--dev_mode', 
            default='0',
            help='Sets devmode -- pending implementation'
            )
        return parser.parse_args()

    def main(self):
        the_game = GenesisGame()
        return the_game.run()

            
if __name__ == "__main__":
    game = Game()


