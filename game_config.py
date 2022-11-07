
import json
import re
import os.path

def _make_load_path( env_name, cfg_path, cfg_file ):
    """
    Creates the load source filename from passed in parameters.
        Internal class method, not expecting self.
        """
    delim = r'\\'
    pathname = cfg_path + delim + env_name + delim + cfg_file
    return os.path.normpath(pathname)


class GameConfig():
    def __init__(self):
        pass

    def load_config( self, env_name='default', cfg_path='Config', cfg_file='GameSettings.json'):
        """ 
        Loads the game environment.

        Lower level comfiguration of the game environment. 
        Not responsible for restoration of a prior saved game state.
        Assumes configuration file preexisting under cfg_path/env_name/cfg_file.
        Relative to current working directory by default.

        Parameters: 
        env_name ['default']: (string) Name of the environment (i.e. game definitions) to load. Default: 'default'
        cfg_path ['Config']: (string) path to the env_name directory. Default: ;
        cfg_file ['GameSettings.json']: (string) Name of file holding the configuration

        Returns: tbd
        Exceptions: tbd

        """
        self._source_filename = _make_load_path(env_name, cfg_path, cfg_file)
        if os.path.isfile( self._source_filename ):
            print( f'{self._source_filename} exists')
        else:
            print( f'{self._source_filename} does not exist' )





