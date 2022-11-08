
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
        self._suits = []
        self._cfg_data = {}
        self._source_filename = 'Filename has not been initialized (pending call to load_config ?)'

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

        Returns: boolean (for now)
        Exceptions: JSONDecodeError and tbd (for now)

        """

        self._source_filename = _make_load_path( env_name, cfg_path, cfg_file )
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
        return rv


    def _organize( self, data ):
        """ 
        Business logic to decode the raw data from the higer level organization.
        Questionable approach but will see if it shakes out

        Assumed a "private method" where data will be the self._cfg_data unless called from unit test code
        """
        # versionings, when/if needed assumed under top level object 'version' as [major, minor ] in the cfg data
        self._suits = list( data['suit_attrs'].keys() )

    def get_suits(self):
        """
        Returns list of available suits
        """
        return self._suits

    def get_suit_descriptor(self, suit):
        """
        Returns desciptor from passed in suit
        Todo: define error handling, can throw if access invalid
        """
        suit_vals = self._cfg_data['suit_attrs'][suit]
        return suit_vals['descriptors']


        





