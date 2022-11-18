
import json
import re
import os.path

# XXX -- migrate the current loadedConfig object into objects for different domains (e.g. PlayerConfig,etc)

# loaded Config gets initialed to a GameConfigLoader as the final step in the load_game_config.
# In turn copied by the GameConfig class which is meant to be the interface to the configuration
loadedConfig = None 
globalsConfig = None

class InitGlobals():
    # self,cmdline_args):
    def __init__(self,cmdline_args):
        global globalsConfig
        globalsConfig = _GlobalsConfig(cmdline_args)

class Globals():
    """ usages e.g. Globals.get().dev_mode(0) """
    @staticmethod 
    def get(): return globalsConfig

class _GlobalsConfig():
    def __init__(self,cmdline_args):
        self._args = vars(cmdline_args)
        global globalsConfig
        globalsConfig = self    #GlobalsConfig(cmdline_args)

    # XXX doens't belong here, but will sort out when player config is flushed out
    def player_name( self, default="Guest" ):
        return self._get_arg_val('player_name', default)

    def dev_mode(self,default=0):
        return self._get_arg_val("dev_mode", default)

    def _get_arg_val( self, key, default ):
        return self._args[key] if key in self._args else default


class GameConfigLoader():
    """
    GameConfigLoader loads in the game configuration from the specified json file then copies self
    to the module level global 'loadedConfig'
    Only method meant to be called externally is load_game_config
    """
    def __init__(self):
        pass

    @staticmethod
    def _make_load_path( env_name, cfg_path, cfg_file ):
        """
        Creates the load source filename from passed in parameters.
        Internal class method, not expecting self.
        Static to facilitate unit testing
        """
        delim = r'\\'
        pathname = cfg_path + delim + env_name + delim + cfg_file
        return os.path.normpath(pathname)


    def load_game_config( self, env_name='default', cfg_path='Config', cfg_file='GameSettings.json'):
        """ 
        Top level function to loads the game environment.

        Lower level comfiguration of the game environment. 
        Not responsible for restoration of a prior saved game state.
        Assumes configuration file preexisting under cfg_path/env_name/cfg_file.
        Relative to current working directory by default.

        Parameters: 
        env_name ['default']: (string) Name of the environment (i.e. game definitions) to load. Default: 'default'
        cfg_path ['Config']: (string) path to the env_name directory. Default: ;
        cfg_file ['GameSettings.json']: (string) Name of file holding the configuration

        Returns: boolean (for now)
        Exceptions: JSONDecodeError and tbd (for now)

        """

        self._source_filename = GameConfigLoader._make_load_path( env_name, cfg_path, cfg_file );
        if not os.path.isfile( self._source_filename ):
            print( f'{self._source_filename} does not exist' )
            return False

        rv = True
        try: 
            fp = open( self._source_filename )
            self._cfg_data = json.load( fp )
        except JSONDecodeError(msg,doc,pos):
            print('An error occurred in doc: msg')
            raise JSONDecodeError(msg,poc,pos)
        except OSError(errno, strerror):
            print( f'OSError exception caught, {errno}, {strerror}' )
            raise OSError(errno, strerror)
        except:
            print('Unknown exception caught, probably in open')
            rv = False
        finally:
            fp.close()

        self._organize( self._cfg_data )
        global loadedConfig
        loadedConfig = self;
        return rv

    def _organize( self, data ):
        """ 
        Business logic to decode the raw data from the higer level organization.
        Questionable approach but will see if it shakes out

        Assumed a "private method" where data will be the self._cfg_data unless called from unit test code
        """
        # versionings, when/if needed assumed under top level object 'version' as [major, minor ] in the cfg data
        self._suits = list( data['suit_attrs'].keys() )
        # XXX questionable spot for it but for hack the globals config instantiation here


class GameConfig():
    """ 
    GameConfig provides the interface to the attributes in a previously loaded GameConfigLoader
    """
    def __init__(self):
        global loadedConfig
        self._loaded_cfg = loadedConfig 


    def get_suits(self):
        """
        Returns list of available suits
        """
        return self._loaded_cfg._suits

    def get_suit_descriptor(self, suit):
        """
        Returns desciptor from passed in suit
        Todo: define error handling, can throw if access invalid
        """
        suit_vals = self._loaded_cfg._cfg_data['suit_attrs'][suit]
        return suit_vals['descriptors']


