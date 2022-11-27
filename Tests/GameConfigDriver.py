
import argparse
import sys
import re
sys.path.append('..')

from game_config import GameConfigLoader
from game_config import GlobalsConfigLoader,GlobalsConfig,GameConfig
from game_config import GameMapConfig


class ConfigDriver():
    def __init__(self):
        pass

    def main(self):
        cmdlineArgs = self.process_cmdline()
        args = vars(cmdlineArgs)
        GameConfigLoader().load_game_config(args['game_name'], args['config_path'])

        self.check_gamemap_config() 
        return

        print("\nRunning globals config" )
        self.check_globals_loading(args)        # with namespace
        print("Done globals config, validate output\n")

        print("\nExercising game config (qualities) access\n")
        self.check_qualities()
        print("Done, validate output\n")

    def check_gamemap_config(self):
        gmc = GameMapConfig()
        data = gmc._mutable_raw_data
        dims = gmc.min_max_x
        print("Testing x origin offsetting")
        for i in [0, 1,-1, -10, -10000,10000]:
            data['origin'][0] = i
            dims = gmc.min_max_x
            print(f"{i} {dims} distance {abs(dims[0]-dims[1])}")
        dims = gmc.min_max_y
        print("Testing y origin offsetting")
        for i in [0, 1,-1,-10000,10000]:
            data['origin'][1] = i
            dims = gmc.min_max_y
            print(f"{i} {dims} distance {abs(dims[0]-dims[1])}")


    def check_qualities(self):
        gc = GameConfig()
        suits = gc.get_suits()
        print(f"get_suits(): {suits}" )
        for suit in suits:
            desc = gc.get_suit_descriptor(suit)
            print(f"get_suit_descriptor({suit})")
            print(desc)

        print("\nTesting GameConfig() suits nonmutability")
        print(f"orig: {suits}")
        suits.append("Somebullshit")
        suits.pop()
        suits2 = gc.get_suits()
        print(f"check: {suits}")

        print("\nTesting descriptor nonmutability")
        desc = gc.get_suit_descriptor("HEMLOCK")
        print(f"orig: {desc}")
        desc.sort()
        desc = gc.get_suit_descriptor("HEMLOCK")
        print(f"check: {desc}")


    def check_globals_loading(self,args):

        for i in range(1,3):
            args['dev_mode'] = i
            print("Calling GlobalsConfigLoader()")
            print(f"args: {args}")
            GlobalsConfigLoader(args)

            print("Calling GlobalsConfig(), expecting GlobalsConfigLoader returned")
            gc = GlobalsConfig()
            print(type(gc))
            print(f"dev_mode {gc.dev_mode}")

        

    def process_cmdline(self):
        parser = argparse.ArgumentParser(
            description='Ways to change the game.',
            epilog='We await your decision.'
        )
        parser.add_argument(
            '--config_path', 
            default='..\Config', 
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


drv = ConfigDriver()
drv.main()




